import math
import os
import random
import re
import sys

if __name__ == '__main__':

	time = "12:05:45AM"

	military_hours = {"01":"13","02":"14","03":"15","04":"16","05":"17","06":"18","07":"19","08":"20","09":"21","10":"22","11":"23","12":"00"}
	
	hour = time.split(':', maxsplit=1)[0]
	
	print("hour is: %s" %hour)
	
	if(time.strip('0123456789:') == "PM"):		

		military_time = time.split("PM")[0]	
		
		if(hour != "12"):
			military_time = military_time.replace(hour, military_hours[hour])
	else:
	
		military_time = time.split("AM")[0]
	
		if(hour == "12"):
			military_time = military_time.replace(hour, military_hours[hour])
	
	print(military_time)
