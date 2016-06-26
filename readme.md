Ilmatieteenlaitoksen säädatan lataaja / FMI Weather Downloader
==============================
[Webpage of the application with downloads & guides](http://tumetsu.github.io/FMI-weather-downloader/)
![screenshot](http://i.imgur.com/CzXFzIQ.png)

This is a simple application to provide a graphical user interface to download weather data from [Finnish Meteorological Institute's open data service](https://ilmatieteenlaitos.fi/avoin-data). The application was originally developed for [Lammi Biological Station's](http://www.helsinki.fi/lammi/) needs.

At this point application supports downloads of daily and real time obseration data from FMI's Finnish weather stations and has Finnish and Eglish user interface. For more information about the usage and downloads, head to the website of the application or go directly to [download page](https://github.com/Tumetsu/Ilmatieteenlaitoksen-saadata-lataaja/releases) 

Please note that this application **is not made by FMI!** It only uses the open data service provided by FMI.


Material
---------
The data downloaded by this program is directly from FMI's server. User should follow the [license of the data described in FMI's service](http://ilmatieteenlaitos.fi/avoin-data-lisenssi). When using the data in your work, research etc. it is your responsibility to follow the guidelines and licenses of the FMI.

For software developers
-------------

This application was put together rapidly using Python3, PyQt5 and few other libraries. As such especially the GUI code haven't been cleaned that much. I might clean it in near future by breaking it to several smaller functions and classes. Note however, that the API-code has been placed into its own module. I'm not sure if I'll do much further development for this project, so forks and pull requests are welcome if you are so inclined. Finnish researchers really seem to have a need for this kind of application. 

I think that this kind of tool might work better as a webservice. I decided to build a standalone version to avoid having to maintain server. The fmi-module's code should be easily portable to a backend Python frameworks as it is (for example Django).

Install for development
--------------------

First install `Python 3.5` and `virtualenv` package for it. Then in project root run:
```
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

On Windows, you can package the app to runnable exe with `cx_Freeze` tool by running following command in project root
after installing [cx_Freeze 5.0 Windows binary wheel](https://github.com/sekrause/cx_Freeze-Wheels):

    `python setup_win_cx.py build`
The build folder can be transformed into install setup with. [InnoSetup](http://www.jrsoftware.org/isinfo.php) There is a script for it which
can be run in root directory to create a install exe to the build/ directory on Windows.

Thanks
---------
Thank you to John Loehr from University of Helsinki for proof reading the English translations as well as getting the application submitted to University's software portal.
