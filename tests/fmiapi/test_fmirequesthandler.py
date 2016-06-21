from fmiapi.fmirequesthandler import FMIRequestHandler
from datetime import datetime
from tests.testUtils import *
from unittest import mock
from unittest.mock import call
import pytz

timezone = pytz.timezone('Europe/Helsinki')


class TestFMIRequestHandler():
    def setup(self):
        self.fmi_handler = FMIRequestHandler('apikey')
        self._DAILY_REQUEST_MAX_RANGE_HOURS = 8928
        self._REALTIME_REQUEST_MAX_RANGE_HOURS = 168

    @mock.patch('fmiapi.fmirequesthandler.FMIRequest', spec=True)
    def should_get_year_in_one_request(self, mock_fmirequest):
        query = {'request': 'getFeature',
                 'storedquery_id': 'fmi::observations::weather::daily::multipointcoverage',
                 'fmisid': '1234',
                 'starttime': datetime(2010, 1, 1, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                 'endtime': datetime(2011, 1, 5, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone)
                 }

        expected = {'starttime': datetime(2010, 1, 1, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                    'endtime': datetime(2011, 1, 5, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                    'fmisid': '1234',
                    'request': 'getFeature',
                    'storedquery_id': 'fmi::observations::weather::daily::multipointcoverage'
                    }

        mock_instance = mock_fmirequest.return_value
        mock_instance.get.return_value = 'data'

        handler = FMIRequestHandler('apikey')
        result = handler.request(query, max_timespan=self._DAILY_REQUEST_MAX_RANGE_HOURS, progress_callback=None)

        mock_instance.get.assert_has_calls([call(expected)])
        assertEqual(1, mock_instance.get.call_count)
        assertEqual(1, len(result))

    @mock.patch('fmiapi.fmirequesthandler.FMIRequest', spec=True)
    def should_call_fmirequest_in_two_parts_for_372_day_time_span(self, mock_fmirequest):
        query = {'request': 'getFeature',
                 'storedquery_id': 'fmi::observations::weather::daily::multipointcoverage',
                 'fmisid': '1234',
                 'starttime': datetime(2010, 1, 1, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                 'endtime': datetime(2011, 1, 23, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone)
                 }
        expected = [{'starttime': datetime(2010, 1, 1, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                     'endtime': datetime(2011, 1, 7, hour=23, minute=1, second=0, microsecond=0, tzinfo=timezone),
                     'fmisid': '1234',
                     'request': 'getFeature',
                     'storedquery_id': 'fmi::observations::weather::daily::multipointcoverage'
                     },
                    {'starttime': datetime(2011, 1, 8, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                     'endtime': datetime(2011, 1, 23, hour=0, minute=1, second=0, microsecond=0, tzinfo=timezone),
                     'fmisid': '1234',
                     'request': 'getFeature',
                     'storedquery_id': 'fmi::observations::weather::daily::multipointcoverage'
                     }]

        expected_calls = [call(expected[0]), call(expected[1])]
        mock_instance = mock_fmirequest.return_value
        mock_instance.get.return_value = 'data'

        handler = FMIRequestHandler('apikey')
        result = handler.request(query, max_timespan=self._DAILY_REQUEST_MAX_RANGE_HOURS, progress_callback=None)

        mock_instance.get.assert_has_calls(expected_calls)
        assertEqual(2, mock_instance.get.call_count)
        assertEqual(2, len(result))
