# Importing the libraries
from datetime import datetime
import pandas as pd
import numpy as np
import glob
import os


# Start timer :
start_time = datetime.now()

# Open all csv files in the current directory, select the corect column/row 
# and add them to a list of dataframe df :
os.chdir("./")
list_df = []
for f, file in enumerate(glob.glob("*.csv")) :  
    list_df.append(pd.read_csv(file).iloc[11: ,1:4].values)
del(f,file)
#print(list_df)

list_activity_tot = []
# Iterate thrue the list of dataframe to clean them :
for dataframe in range(len(list_df)) :
    df = list_df[dataframe]            
    #print(df)    
    
# Create a list of activity from the dataframe df and iterate thrue it to   
# clean the activity :
    list_activity = df[:,2]
    for i in range(len(list_activity)) :
        list_activity[i] = list_activity[i].lower()
        list_activity[i] = list_activity[i].strip()
        list_activity[i] = list_activity[i].replace(" ", "")
        list_activity[i] = list_activity[i].replace("(", "")        
        list_activity[i] = list_activity[i].replace(")", "")  
        list_activity[i] = list_activity[i].replace(",", "")
        list_activity[i] = list_activity[i].replace('"', "")
        list_activity[i] = list_activity[i].replace('"', "")
    del(i)
    #print(list_activity)
# Replace activities in daframe df with the clean list_activity for all 
# the entries and if the activity not in list_activity_tot, add them :
    for i in range(len(list_activity)) :
            df[i,2] = list_activity[i]
            if list_activity[i] not in list_activity_tot :
                list_activity_tot.append(list_activity[i])
    del(list_activity,i)
    #print(df) 
    
# Create a list of the time list_hour when a entry occure, split hour, minutes,
# secondes and convert evrything in seconds :
    list_hour = df[:, 0]
    for i in range(len(list_hour)) :          
        if ':' in list_hour[i] and "'" in list_hour[i] and '"' in list_hour[i] :
            list_hour[i] = list_hour[i].replace('"', "")
            list_hour[i] = str(list_hour[i]).split("'")
            s = int(list_hour[i][1])
            list_hour[i] = str(list_hour[i][0]).split(":")
            h = int(list_hour[i][0])
            m = int(list_hour[i][1])
            list_hour[i] = h*3600 + m*60 + s
            del(h,m,s)
            continue
        if "'"in list_hour[i] and '"' in list_hour[i] :
            list_hour[i] = list_hour[i].replace('"', "")
            list_hour[i] = str(list_hour[i]).split("'")
            h = 0
            m = int(list_hour[i][0])
            s = int(list_hour[i][1])
            list_hour[i] = h*3600 + m*60 + s
            del(h,m,s)
            continue 
        if '"' in list_hour[i] :
            list_hour[i] = list_hour[i].replace('"', "")
            h = 0
            m = 0
            s = int(list_hour[i][0])
            list_hour[i] = h*3600 + m*60 + s
            del(h,m,s)
            continue
    del(i)
    #print(list_hour) 
    
# Take the last value of time in list_hour, calcul the factor to convert it 
# to 24h in secondes and multiply the values in list_hour by this factor and 
# replace it in df :
    F= (86400 / int(list_hour[-1]))
    for i in range(len(list_hour)) :
        list_hour[i] = F * list_hour[i]
        df[i,0] = list_hour[i]
    del(i)
    #print(df)
    #print(F)

# Take all the duration in df and put them in a list, multiply it by the 
# converting factor and replace the corrected value in df :
    list_duration = df[:, 1]    
    for i in range(len(list_duration)) :
                df[i, 1] = F * float(list_duration[i])
    del(list_duration,i,F) 
    #print(df)
    
# Iterate thrue list_hour and determine if its day (1) or night (0),
# add the value to a new list and delete the variable list_hour after :        
    list_day = []   
    for i in range(len(list_hour)) :
        if int(list_hour[i])<28800 or int(list_hour[i])>=64800 :
              list_day.append(1)
        else :         
              list_day.append(0) 
    del(i,list_hour) 
    #print(list_day)
    
# Add a new column for days from list_day at the end of the dataframe df 
# and delete the variable list_day after :
    list_day = np.array(list_day)
    list_day = list_day.reshape((len(list_day), 1))
    df = np.append(df, list_day, axis=1)
    #print(df)
    del(list_day)  
    
# delete first column of df (time in seconds) array and put back df in 
# dataframe panda (probably not the right way to do it)
    df = np.delete(df, 0, 1) 
    df = pd.DataFrame(df, index=None, columns=None)  
    #print(df)
   
# Put back df in list_df. Dont know why but not all variables are updated 
# in the list_df (like column day) and clean df for an another iteration : 
    list_df[dataframe] = df
    del(df) 
    
# End of the loop thrue list_df
del(dataframe) 

# Sort the activities :
list_activity_tot.sort()
#print(list_activity_tot)
print("Total number of activitiy :", len(list_activity_tot))

# Add the key day at the end of the list :
list_activity_tot.insert(len(list_activity_tot), "day")
#print(list_activity_tot)

# Create a dictionary with the sorted activities with value 0 for each key :
dict_activity = { i : 0 for i in list_activity_tot }
#print(dict_activity)

# Create an empty list tha will take all windows, decide the time windows :
list_by_windows = []
windows = 1800
timer = 0

# Iterate thrue the list of dataframe df to get the time windows :
for dataframe in range(len(list_df)) :
    df = list_df[dataframe].iloc[: ,:].values
# Iterate thrue df to get the duration off the activity, add the duration off the 
# activity in the dictionnary with activities to the right activity. Add the dictionary
# in a list of dictionnary/windows. If the total duration of the activities in the 
# dictionnary is biger than the time windows, split the duration of the activity 
# and put the remainning duration in a new dictionary/windows :    
    for i in range(len(df)) :  
        duration = float(df[i,0])
        
        while (timer + duration) > windows :
            dict_activity[df[i,1]] = float(dict_activity[df[i,1]]) + windows
            dict_activity['day'] = df[i,2]
            list_by_windows.append(dict(dict_activity))
            dict_activity = { i : 0 for i in dict_activity }
            duration = duration - (windows - timer)
            timer = 0                  
        
        if (timer + duration) < windows : 
            dict_activity[df[i,1]] = float(dict_activity[df[i,1]]) + duration  
            dict_activity['day'] = df[i,2]
            timer = timer + duration
            continue
            
        if (timer + duration) == windows :
            dict_activity[df[i,1]] = float(dict_activity[df[i,1]]) + duration  
            dict_activity['day'] = df[i,2]
            list_by_windows.append(dict_activity)
            timer = 0
            dict_activity = { i : 0 for i in dict_activity }
            continue
           
del(i,timer,windows,list_activity_tot,dict_activity,dataframe,df,duration)

# Create the clean dataframe for cluster analysis with all df combined :
df_cluster = pd.DataFrame()
df_cluster =pd.concat(list_df,ignore_index=True)


# Create the clean dataframe for windows analysis :
df_windows = pd.DataFrame(list_by_windows)
del(list_by_windows,list_df)

# Try to Creates a folder in the current directory called Processed_data
# if it doesnt exist :
try:
    if not os.path.exists('./Processed_data/'):
        os.makedirs('./Processed_data/')  
except OSError:
    pass          

# Create new csv cluster file in the Processed_data folder:
df_cluster.to_csv('./Processed_data/Cluster_data.csv',header = ["Duration","Activities","Day"],  index = False)            
del(df_cluster) 
           
# Create new csv windows file in the Processed_data folder:
df_windows.to_csv('./Processed_data/Windows_data.csv', index = False)            
del(df_windows)

# End timer and display it :
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
