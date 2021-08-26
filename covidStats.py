import time #To make it run daily
from datetime import date #To read current date
import requests as req #To request covid api
from plyer import notification #For notifications


data = None
try:
    data = req.get("https://corona-rest-api.herokuapp.com/Api/portugal")
    if(data != None):
        dataJSON = data.json().values()
        val_iter = iter(dataJSON)
        value = next(val_iter)
        print(value)

        
        while(True):
            today = date.today()
            statusDay = "Covid19 Stats on " + today.strftime("%d/%m/%Y")
            notification.notify(
                title = statusDay, 
                message = "Total Cases: " + str(value['cases']) + 
                "\nCases Today: " +  str(value['todayCases']) + 
                "\nDeaths Today: " + str(value['todayDeaths']) +
                "\nActive Cases: " + str(value['active']),
                app_icon = "covid.ico",
                timeout = 30)
            time.sleep(60*60*4)
except Exception as e:
    #Request Failed
    print(e)
    print("Request failed, try again later")