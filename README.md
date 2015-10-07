NOTE: THE LIVE DESKTOP FEATURE ONLY WORKS ON WINDOWS AS OF THIS COMMIT

# Description
- Parses sunsrise/sunset data from US Naval Observatory standardized export
- Takes sunrise/sunset data and creates a graph showing the current year on the X axis, and the hours in a day on the Y axis.
- Plots current day as a vertical line, and plots the location of the sun as a large yellow scatterplot point.
- Fills daytime with light color, and nighttime with dark color (potential to add dawn/dusk colors)

# Folder structure
Main folder = Contains license, readme, and batch files to run scripts more easily (see How to Use / Running Scripts)
- .GIT = Folder for Github history etc
- Inputs = Files used as inputs for scripts
- Outputs = Outputs from scripts
- Scripts = Where actual scripts live ("X_" at the beginning of a script means it holds functions and shouldn't be executed independently)
- Testing = Just for testing

# INPUT/OUTPUT
Input data from http://aa.usno.navy.mil/data/docs/RS_OneYear.php
- Use Form A or Form B to get a table of current year sunrise/sunset data
- Put that data into astro/inputs/
- Configure variables under #PARAMS section of astro.py before running script
- Chart output goes to astro/outputs/
- FILE MUST BE NAMED IN THE FOLLOWING FORMAT >>> 'Sunrise Sunset-' + str(year) + '.txt'

# CONFIGURATION
- Non-helper files (No "X_" at the begnning) have a section called "#PARAMS" at the beginning with parameters that can be customized. As of this commit, there is only one param in each, which is the difference from UTC. Just set this to the UTC offset for the timezome you would like to show in your chart (I use an int, but a float should work). The US Naval Observatory gives data in UTC Timezone, which is why this parameter is necessary.
- If you want to further customize within helper files (have an "X_" at the beginning), I haven't done much work to make configuration easy, so you will need to read the code yourself.

# RUNNING SCRIPTS
- I use the batch files in the main folder of the repository to run the script. They will need to be configured for wherever you store your repository on your computer.
- Alternatively, you can run the files via command prompt. Only the non helper files (no "X_" at the beginning) should be executed independently.
- Scripts should still run properly via other methods (i.e. ipython notebooks), but I haven't tested them there.
