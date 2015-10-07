#!/usr/bin/python
description = 'Produces new astro chart every minute while script runs and sets it as desktop background. Parses data once at beginning. For more see repository README.' 
inputs = {'astro' : 'C:/Users/Nathan/Dropbox/GitHub/astro/inputs'}
outputs = {'astro' : 'C:/Users/Nathan/Dropbox/GitHub/astro/outputs'}
script = str(os.path.realpath(__file__)) if '__file__' in globals() else 'Current Script Unknown'
from X_Imports import *
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

# PLOT ONCE AND SAVE IN OUTPUT FOLDER
os.chdir(outputs['astro'])
astro.astroplot(s_rise, s_set, outputs, year)