# How to Download Outdoor Weather Data
This [repository](https://github.com/Karlheinzniebuhr/the-weather-scraper) is a great resource to download outdoor weather data. The only changes that you need to do is:

* Change the `stations.txt` file to the desired weather station (e.g., `KILCHICA594` for the Chicago Loop). The followning text could be added:
```
 https://www.wunderground.com/dashboard/pws/KILCHICA594
```
* Update the `config.py` file to the desired dates. For example:

```
START_DATE = date(2022, 1, 1)
END_DATE = date(2023, 9, 25)
```
