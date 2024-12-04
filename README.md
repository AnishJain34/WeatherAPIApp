# Weather App - Python GUI Application
Description:
This is a Python-based Weather Application with a sleek graphical user interface (GUI) built using PyQt5. The app fetches real-time weather data using the OpenWeatherMap API and provides:

Current temperature in Celsius.
Weather description in text and emoji form.
Intuitive error messages for common API or network issues.
Features:
Real-Time Weather Data:

Input a city name and retrieve the latest temperature, weather description, and relevant emoji representation.
Error Handling:

Handles HTTP errors (e.g., invalid city, API issues) with user-friendly messages.
Handles network issues like timeouts or connection errors.

Requirements:
Python 3.x
PyQt5
Requests library
Setup:
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/weather-app.git
Install dependencies:
bash
Copy code
pip install PyQt5 requests
Get an API key from OpenWeatherMap and replace the api_key variable in the code:
python
Copy code
api_key = "your_api_key_here"
Run the application:
bash
Copy code
python weather_app.py
