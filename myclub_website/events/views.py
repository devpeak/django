from django.shortcuts import render
import calendar 
from calendar import HTMLCalendar
from datetime import datetime

def home(request,year,month):
	name = "John"
	month = month.capitalize() #capitalize the month name

	#convert month from name to number
	month_number = list(calendar.month_name).index(month)
	
	month_number = int(month_number)

	#create a calendar
	cal = HTMLCalendar().formatmonth(year,month_number)

	#Get curren year
	now = datetime.now()
	current_year = now.year

	#Get current time
	time = now.strftime('%I:%M %p') #I - 11, H- 23 #%H:%M:%S

	return render(request, 
		'home.html', {
		"name": name,
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal":cal,
		"current_year": current_year,
		"time":time,

		})
