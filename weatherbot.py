from bs4 import BeautifulSoup
import requests
import time

while True:
    try:
        def get_weather():
            html_text = requests.get(
                "https://forecast.weather.gov/MapClick.php?lat=37.510088600000074&lon=-77.61887949999993").text
            soup = BeautifulSoup(html_text, "lxml")
            weather = soup.find("div", class_= "panel panel-default")
            location_richmond = weather.find("h2", class_= "panel-title").text
            temperature_richmond = weather.find("p", class_= "myforecast-current-lrg").text
            current_conditions_richmond = weather.find("p", class_= "myforecast-current").text
            richmond_weather = f"""
                               {location_richmond}
                               {temperature_richmond}
                               {current_conditions_richmond}
                               """


            html_text = requests.get(
                "https://forecast.weather.gov/MapClick.php?lat=40.78605090000008&lon=-73.97620439999997").text
            soup = BeautifulSoup(html_text, "lxml")
            weather = soup.find("div", class_= "panel panel-default")
            location_new_york = weather.find("h2", class_= "panel-title").text
            temperature_new_york = weather.find("p", class_= "myforecast-current-lrg").text
            current_conditions_new_york = weather.find("p", class_= "myforecast-current").text
            new_york_weather = f"""
                               {location_new_york}
                               {temperature_new_york}
                               {current_conditions_new_york}
                               """


            html_text = requests.get(
                "https://weather.com/weather/today/l/cf6bf06fb8f4e072c2f147003f80e99100f42ae627370a982ea413a33ca8d302").text
            soup = BeautifulSoup(html_text, "lxml")
            location_aomori = soup.find("h1", class_="CurrentConditions--location--kyTeL").text
            temperature_aomori = soup.find("span", class_="CurrentConditions--tempValue--3a50n").text
            current_conditions_aomori = soup.find("div", class_="CurrentConditions--phraseValue--2Z18W").text
            aomori_weather = f"""
                             {location_aomori}
                             {temperature_aomori}
                             {current_conditions_aomori}
                             """


             # placeholder

            payload = {
                "content": f"Current weather: \n"
                           f"{richmond_weather} \n"
                           f"{new_york_weather} \n"
                           f"{aomori_weather} \n"
                           f"\n"
                           f"Will post another weather update in 30 minutes..."
            }


            header = {
                "authorization": "placeholder"
            }
            r = requests.post("placeholder", data=payload, headers=header)


        if __name__ == "__main__":
            while True:
                get_weather()
                time_wait = 1800
                time.sleep(time_wait)

    except AttributeError:
        print("Trying again...")
        get_weather()
