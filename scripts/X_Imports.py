######################################
########## ASTRO IMPORTS #############
######################################

import os
import time
import datetime as dt
import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.dates as mdates
from matplotlib.dates import date2num, num2date
from matplotlib import ticker
from pandas import DataFrame, Series, ExcelWriter
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, \
     AnnotationBbox
from matplotlib.cbook import get_sample_data
from matplotlib.ticker import FuncFormatter

import X_Header as header
import X_Astro as astro