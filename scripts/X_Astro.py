########################################
########## ASTRO FUNCTIONS #############
########################################


def parse_sr_ss(inputs, difference_from_utc_standard):
  
  import datetime as dt

  now = dt.datetime.now()
  year = now.year
  columns = ['period','month','day','event','rawtime','min','hour','time','test']
  filename = 'Sunrise Sunset-' + str(year) + '.txt'
  firstdata = 9
  maxdays = 31
  start = dt.datetime(year,1,1,0,0)

  ## NOTE: Input files must be named in the format: name + "-" + date("YYYY-MM-DD")
  # FIND OPPORTUNITY DATA
  os.chdir(inputs['astro'])

  # Using the newer with construct to close the file automatically.
  with open(filename) as f:
      data = f.readlines()

  # cut off extra crap
  raw = data[firstdata:firstdata+maxdays]
      
  test = raw

  data = pd.DataFrame(columns=columns)
  temp = pd.DataFrame([[dt.datetime(year,1,1),0,0,'a','a',0,0,dt.datetime(year,1,1,0,0),'a']], columns=columns)

  start_space = [4,5, #jan
                 6,5, #feb
                 6,5, #mar
                 6,5, #apr
                 6,5, #may
                 6,5, #jun
                 6,5, #jul
                 6,5, #aug
                 6,5, #sep
                 6,5, #oct
                 6,5, #nov
                 6,5] #dec

  events = ['01_r','01_s',
            '02_r','02_s',
            '03_r','03_s',
            '04_r','04_s',
            '05_r','05_s',
            '06_r','06_s',
            '07_r','07_s',
            '08_r','08_s',
            '09_r','09_s',
            '10_r','10_s',
            '11_r','11_s',
            '12_r','12_s']


  for i in range(0,len(test)):
      # find day
      start = 0
      end = 2
      temp['day'] = raw[i][start:end]
      # find times
      for j in range(0,len(events)):
          temp['month'] = events[j].split("_")[0]
          temp['event'] = events[j].split("_")[1]
          start += start_space[j]
          end = start + 4
          temp['rawtime'] = raw[i][start:end]
          temp['period'] = temp['month'] + '_' +  temp['day']
          data = data.append(temp, ignore_index=True)

  for i in range(0,len(data)):
      data['test'][i] = data['rawtime'][i].count(' ')
          
  #remove days that don't exist
  data = data[(data['test'] < 1)].reset_index(drop=True)

  for i in range(0,len(data)):
      data['hour'][i] = data['rawtime'][i][0:2]
      data['min'][i] = data['rawtime'][i][2:4]
      data['time'][i] = dt.datetime(year,1,2,int(data['hour'][i]),int(data['min'][i]))
      data['period'][i] = dt.datetime(year,int(data['month'][i]),int(data['day'][i]))

  s_rise = data[data['event'] == 'r'].sort('period').reset_index(drop=True)
  s_set = data[data['event'] == 's'].sort('period').reset_index(drop=True)

  for i in range(0,len(s_rise['time'])):
      s_rise['time'][i] = s_rise['time'][i] + dt.timedelta(hours = difference_from_utc_standard)
      s_rise['time'][i] = s_rise['time'][i].replace(day=1)
      s_set['time'][i] = s_set['time'][i] + dt.timedelta(hours = difference_from_utc_standard)
      s_set['time'][i] = s_set['time'][i].replace(day=1)

  return {'s_set' : s_set, 's_rise' : s_rise}