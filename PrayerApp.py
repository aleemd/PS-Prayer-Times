'''
Created on Feb 3, 2021

Author: Danya Aleem
Team: D41
Project: PlayStation Prayer Times Application

'''
import requests
import json
from datetime import datetime

class GetPrayer:
    def __init__(self):
        """Mandatory fields and base API URL"""
        self.city = "losangeles"
        self.country = "US"
        self.method = "2"
        self.baseURL = "http://api.aladhan.com/v1/timingsByCity?city={ci}&country={co}&method={nu}"
    
    def get_user_input(self):
        """User input for mandatory URL fields"""
        self.city = input("City: ")
        self.country = input("Country: ")
        self.method = input("Method: ")
        
    def jprint(self, obj):
        """Create a formatted string of the JSON object for developer use"""
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    
    def parse_url_for_prayer_json(self):
        """Parse URL to produce JSON and return all prayer times as JSON"""
        newURL = self.baseURL.format(ci = self.city, co = self.country, nu=self.method)
        response = requests.get(newURL)
        result = response.json()
        return result["data"]["timings"]
            
    
    def get_current_prayer(self, d):
        """Compares current time to prayer times for the day to determine what prayer is in now"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time >= d["Fajr"] and current_time < d["Sunrise"]:
            print("Fajr Time")
        elif current_time >= d["Dhuhr"] and current_time < d["Asr"]:
            print("Dhuhr Time")
        elif current_time >= d["Asr"] and current_time < d["Maghrib"]:
            print("Asr Time")
        elif current_time >= d["Maghrib"] and current_time < d["Isha"]:
            print("Maghrib Time")
        elif current_time >= d["Isha"] or current_time >= "00:00" and current_time < d["Fajr"]:
            print("Isha Time")
        else:
            print("No prayer is in")
            
    def notify(self, d):
        """Compares current time to todays prayer times notifies if prayer is in"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        temp = None
        if d["Fajr"] == current_time:
            print("Fajr Time")
            temp = 1
        if d["Dhuhr"] == current_time:
            print("Dhuhr Time")
            temp = 1
        if d["Asr"] == current_time:
            print("Asr Time")
            temp = 1
        if d["Maghrib"] == current_time:
            print("Maghrib Time")
            temp = 1
        if d["Isha"] == current_time:
            print("Isha Time")
            temp = 1
        else:
            print("No Notification")
        return temp
            


if __name__ == '__main__':
    from time import time
    end = time() + 10
    temp = None
    while (time() < end) or (temp == None):
        if temp != None:
            break
        prayerTimes = GetPrayer().parse_url_for_prayer_json()
        temp = GetPrayer().notify(prayerTimes)
        
        
        
    
    
    