# CovidDailyStats
Daily desktop notification with the covid-19 stats for the country specified in it (default being Portugal but change it at your own will).
In case you want to change the country being monitored you can choose wherever you want to be notified of.
###### The data is being fetched by a public API (https://corona-rest-api.herokuapp.com/Api/portugal).
The information contained in each notification are the following fields: 
  * Total Cases 
  * Cases Today
  * Deaths Today
  * Active Cases

<p align="center"><img src="https://i.imgur.com/Z4ufOTT.png" width="350" height="200" alt="Layout of the website"></p>
  
To let it run in background so that you can get the notifications daily run it as:

*pythonw .\covidStats.py*
