# astro

# DESCRIPTION
- Parses sunsrise/sunset data from US Naval Observatory standardized export
- Takes sunrise/sunset data and creates a graph showing the current year on the X axis, and the hours in a day on the Y axis.
- Plots current day as a vertical line, and plots the location of the sun as a large yellow scatterplot point.
- Fills daytime with light color, and nighttime with dark color (potential to add dawn/dusk colors)

# INPUT/OUTPUT AND SCRIPT USAGE
Input data from http://aa.usno.navy.mil/data/docs/RS_OneYear.php
- Use Form A or Form B to get a table of current year sunrise/sunset data
- Put that data into astro/inputs/
- Configure variables under #PARAMS section of astro.py before running script
- Chart output goes to astro/outputs/

