from datetime import date, timedelta
from suntime import Sun, SunTimeException
 


class DaySplicer:

	def __init__(self):
		# Sun longitude and latitude are set to London
		self.sun = Sun(51.05,  0.12)
		self.interval = 0
	

	def get_date(self, text):
		print(text)
		year =  input("Enter year: ")
		month = input("Enter month: ")
		day = input("Enter day: ")
		date_input = date(int(year), int(month), int(day))
		return date_input

	def calculate_sunrise(self, day):
		sunrise_time = self.sun.get_local_sunrise_time(day)
		return sunrise_time

	def calculate_sunset(self, day):
                sunset_time = self.sun.get_local_sunset_time(day)
                return sunset_time

	def get_interval(self):
		return self.interval

	def set_interval(self):
		start_date = self.get_date("Enter a start date")
		sunrise = self.calculate_sunrise(start_date)
		print("Sunrise on ")
		print(start_date)
		print(sunrise)
		end_date = self.get_date("Enter an end date")
		sunset = self.calculate_sunset(end_date)
		print("Sunset on ")
		print(end_date)
		print(sunset)
		number_of_days = end_date - start_date
		print("Number of days ") 
		print(number_of_days.days)
		sunset_proxy = sunset - timedelta(days=number_of_days.days)
		daylight_hours = (sunset_proxy - sunrise)
		print("Daylight hours: ") 
		print(daylight_hours)
		number_of_minutes = daylight_hours.total_seconds() / 60
		print("Total minutes between sunrise and sunset:" )
		print(number_of_minutes)
		self.interval = number_of_minutes/number_of_days.days
		print("photo time will rise each dat by")
		print(self.interval)	
