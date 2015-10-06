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
s_set = temp['s_rise']

os.chdir(outputs['astro'])

#PLOTTING
# Set up figure
edgecolor='None'
linewidth=5
sun_area = 500
plt.style.use('ggplot')
matplotlib.rc('xtick', labelsize=8) 
matplotlib.rc('ytick', labelsize=8) 
fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(13,9))

xr = list(pd.to_datetime(s_rise['period']))
sr = list(pd.to_datetime(s_rise['time']))
xs = list(pd.to_datetime(s_set['period']))
ss = list(pd.to_datetime(s_set['time']))

bottom = dt.datetime(year,1,1,0,0)
top = dt.datetime(year,1,2,0,0)
start = dt.datetime(year,1,1,0,0)
end = dt.datetime(year+1,1,1,0,0)
now = dt.datetime.now()

#sunrise
ax.plot(xr,sr, color = 'orange', label='sunrise', linewidth = linewidth)
ax.fill_between(xr,bottom,sr, facecolor = '#00001F', edgecolor = edgecolor)

#sunset
ax.plot(xs,ss, color = 'purple', label='sunset', linewidth = linewidth)
ax.fill_between(xs,ss,top, facecolor = '#00001F', edgecolor = edgecolor)

#daytime
ax.fill_between(xs,sr,ss, facecolor = '#3399FF', edgecolor = edgecolor)

#today
ax.axvline(x=dt.datetime.now(), linewidth=linewidth, ls = '--', color='k', label = 'today', alpha = .5, zorder=998)

curr_hour = now.hour
curr_min = now.minute

ax.scatter(now, dt.datetime(year,1,1,curr_hour,curr_min), s=sun_area, c='#FFCC00', alpha=1, zorder=999, label = 'sun location')



# Style Customization
ax.set_title("Astronomical time for " + "today " + "in Woodland, WA" , fontsize=18)
ax.set_ylabel("Time", fontsize=8)
ax.set_xlabel("Date", fontsize=8)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
ax.tick_params( axis='both', which ='both', bottom='off', top ='off', left='off', right='off')
ax.set_ylim([bottom, top])
ax.set_xlim([start, end])

plt.savefig('current-astro-time')
plt.close(fig)