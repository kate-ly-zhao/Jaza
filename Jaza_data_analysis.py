# Analysis: Jaza Data
# Kate Zhao

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.interactive(False)

# Importing data
df = pd.read_excel(r'/Users/Downloads/Jaza Discharge Data.xlsx', sheet_name = 'Data')

# Creating variables
power = pd.concat([df.iloc[:, 3:13]])
soc = pd.concat([df.iloc[:, 13:18]])
tod = pd.concat([df.iloc[:, 18:30]])

power.loc['mean'] = (power.mean())/60  # Conversion from mins into hours
soc.loc['mean'] = soc.mean()/60  # Conversion from mins into hours
tod.loc['mean'] = tod.mean()

df.loc[:,'duration'] = (df.loc[:, 'duration'])/60 # Changing duration into units of hours

# Basic Stats
print "Energy Output: "
print df["energy_out"].describe()

print "Max Power Output:"
print df["max_power"].describe()

print "Duration"
print df["duration"].describe()

# Visualizations

power.loc['mean'].plot()
plt.title('Figure 1. Power Over Time')
plt.xlabel('Power (W)')
categories = ('0', '1.7', '3.4', '5.1', '6.8', '8.5', '10.2', '11.9', '13.6', '15.3', '17.0')
pos = np.arange(len(categories))
plt.xticks(pos, categories)
plt.ylabel('Average Elapsed Time (hrs)')
plt.show(block=True)

soc.plot.box()
plt.title('Figure 2. State of Charge Over Time')
plt.xlabel('State of Charge (%)')
categories2 = ('0-25', '25-50', '50-75', '75-100', '100')
pos2 = np.arange(1,len(categories2)+1)
plt.xticks(pos2, categories2)
plt.ylabel('Average Elapsed Time (mins)')
plt.show(block=True)

tod.loc['mean'].plot.bar()
plt.title('Figure 3. Energy Usage Over 24h')
plt.xlabel('Time Intervals (UTC)')
categories3 = ('0:00', '2:00', '4:00', '6:00', '8:00', '10:00', '12:00',
               '14:00', '16:00', '18:00', '20:00', '22:00', '0:00')
pos3 = np.arange(-1, len(categories3)) + 0.5
plt.xticks(pos3, categories3)
plt.ylabel('Average Energy Usage (W)')
plt.show(block=True)

df.plot.scatter(x = 'duration', y = 'max_power')
plt.title('Figure 4. Max Power vs. Discharge Cycle Duration')
plt.xlabel('Total Discharge Cycle Duration (hrs)')
plt.ylabel('Maximum Power (W)')
plt.show(block=True)
print np.corrcoef(df["duration"], df["max_power"])
