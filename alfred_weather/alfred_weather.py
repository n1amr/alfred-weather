from alfred.modules.api.a_base_module import ABaseModule
from alfred.modules.api.a_heading import AHeading
from datetime import datetime
import requests

class AlfredWeather(ABaseModule):

    def __init__(self, *args, **kwargs):
        ABaseModule.__init__(self,*args,**kwargs)
        self.forecast_data=[]

    def callback(self):
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q=Cairo&appid=7e73695b9106e411858e94e01532d30d")
        json_data = r.json()

        for i in range(json_data['cnt']):
            tmp={'date_time' : datetime.fromtimestamp(json_data["list"][i]['dt']).strftime("%a, %d"),
                 'max_temp'  : int(json_data["list"][i]['temp']['day'] - 273.15),
                 'min_temp'  : int(json_data["list"][i]['temp']['night'] - 273.15),
                 'status'    : json_data["list"][i]['weather'][0]['description']
                 }
            self.forecast_data.append(tmp)


    def construct_view(self):
        for i in range (len(self.forecast_data)):
            h1 = AHeading(1, "Date: " + str(self.forecast_data[i]['date_time']))
            h2 = AHeading(2, "Max temp: " + str(self.forecast_data[i]['max_temp']) + "°С")
            h3 = AHeading(2, "Min temp: " + str(self.forecast_data[i]['min_temp']) + "°С")
            h4 = AHeading(2, "Status: " + str(self.forecast_data[i]['status']))

            self.add_component(h1)
            self.add_component(h2)
            self.add_component(h3)
            self.add_component(h4)
