#!/usr/bin/python
description = 'Produces new astro chart every minute while script runs and sets it as desktop background. Parses data once at beginning. For more see repository README.' 
inputs = {'astro' : 'C:/Users/Nathan/Dropbox/GitHub/astro/inputs'}
outputs = {'astro' : 'C:/Users/Nathan/Dropbox/GitHub/astro/outputs'}
from X_Imports import *
import datetime as dt
script = str(os.path.realpath(__file__)) if '__file__' in globals() else 'Current Script Unknown'
header.scriptsummary(script, inputs, outputs)
pd.options.mode.chained_assignment = None
########################################################################################

# PARAMS
difference_from_utc_standard = -8

# GET AND PARSE DATA
temp = astro.parse_sr_ss(inputs, difference_from_utc_standard)
s_set = temp['s_set']
s_rise = temp['s_rise']
year = temp['year']

# PLOT EVERY MINUTE AND CHANGE DESKTOP BACKGROUND
os.chdir(outputs['astro'])

while (1==1):
	# Produce chart
	astro.astroplot(s_rise, s_set, outputs, year)
	# Set desktop background (only works on windows 10 if you have admin on your machine)
	SPI_SETDESKWALLPAPER = 20
	image_path =  str(outputs['astro']) + "/current-astro-time.png"
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 3)
	print('Updated ' + dt.datetime.now().strftime('%Y-%m-%d %I:%M'))
	# Wait 60 seconds before producing a new graph
	time.sleep(60)