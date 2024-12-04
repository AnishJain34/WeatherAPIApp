import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter a city name:",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
       
        self.setStyleSheet("""
QLabel,QPushButton{
                  font-family: calibri;
               }
QLabel#city_label{
                           font-size: 40px;
                           font-weight: bold;
                           font-style:italic;
                           }
QLineEdit#city_input{
                           font-size: 40px;
                           }
QPushButton#get_weather_button{
                           font-size:30px;
                           font-weight:bold;
                           }
QLabel#temperature_label{
                           font-size: 75px;
                           }
QLabel#emoji_label{
                           font-size:  100px;
                           font-family: Segoe UI emoji;
                           }

QLabel#description_label{
                           font-size:50px;
                           }
    
                           """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key="first login go to  my api keys your_api_key"
        city=self.city_input.text()
        url=f"Goto: https://openweathermap.org/current and selt first api call link in ##Built-in API request by city name"
        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            
            if data["cod"]==200:
                self.display_we(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\n PLease check your input")
                case 401:
                    self.display_error("Unauthorised:\n Invalid Api key")
                case 403:
                    self.display_error("Forbidden:Access is denied")
                case 404:
                    self.display_error("Not Found:\nCity is not found")
                case 500:
                   self.display_error("Internal server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the sever")
                case 503:
                    self.display_error("Service Unavailable:\n Server is down")
                case 504:
                    self.display_error("Gateway Timeout:\nplease try again later")
                case _:
                    self.display_error(f"An error occurred{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("ConnectionError\n Check your Internet")
        except requests.exceptions.Timeout:
            self.display_error("TimeoutError\n requests timed out")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")



    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
    def display_we(self,data):
        self.temperature_label.setStyleSheet("font-size:75px;")
        temp_k=data["main"]["temp"]
        temperature_c=temp_k-273.15
        weather_id=data["weather"][0]["id"]
        self.temperature_label.setText(f"{temperature_c:.2f}°C")
        self.emoji_label.setText(self.get_we_em(weather_id))
        des=data["weather"][0]["description"]
        d=des.upper()
        self.description_label.setText(f"{d}")
    @staticmethod
    def get_we_em(weather_id):
        if 200<=weather_id <=232:
            return "⛈️"
        elif 300<=weather_id<=321:
            return "🌥️"
        elif 500<=weather_id<=531:
            return "🌧️"
        elif 600<=weather_id<=622:
            return "❄️"
        elif 701<=weather_id<=781:
            return "🌫️"
        elif weather_id==762:
            return "🌋"
        elif weather_id==771:
            return "💨"
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "☀️"
        elif 801<=weather_id<=804:
            return "☁️"


if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
