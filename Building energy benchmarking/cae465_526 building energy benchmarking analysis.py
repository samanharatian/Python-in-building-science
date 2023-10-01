# Developed by Mohammad Heidarinejad, PhD, PE 
# Updated on: 09/04/2023
# Contact: muh182@iit.edu

# // Copyright (c) 2022-2023 The Built Environment Research Group (BERG)
# // Distributed under the MIT software license, see the accompanying
# // file LICENSE or http://www.opensource.org/licenses/mit-license.php.


#libraries used
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

# read the Chicago building energy benchmarking data (different year and city files can be used)
chicagoData = pd.read_csv('Chicago_Energy_Benchmarking_-_2019_Data_Reported_in_2020.csv')

# establish the data frame
initChicagoData = chicagoData.shape[0]

# remove NA values using dropna
chicagoData = chicagoData.dropna(subset=['Site EUI (kBtu/sq ft)', 'Source EUI (kBtu/sq ft)', 'Year Built', 'Gross Floor Area - Buildings (sq ft)'])

# remove outliers to have a clean Chicago Data
# method 1: using some statistcal metrics
# lowerRange = chi["Site EUI (kBtu/sq ft)"].quantile(0.01)
# upperRange  = chi["Site EUI (kBtu/sq ft)"].quantile(0.999)

# method 2: remove values more than 2000 kBtu/ft2
lowerRange = 10 # removing EUIs less than 10 kBtu/sqft (it could be a net zero building but further investigation is needed)
upperRange  = 2000 # removing EUIs more than 2000 kBtu/sqft (above that is unrelastic for any commercial building)

# establish the clean dataset 
chicagoData = chicagoData[(chicagoData["Site EUI (kBtu/sq ft)"] < upperRange) & (chicagoData["Site EUI (kBtu/sq ft)"] > lowerRange)]
finChicagoData = chicagoData[(chicagoData["Site EUI (kBtu/sq ft)"] < upperRange)].shape[0]

# print a summary of NA data removed 
print('The original Chicago dataset had ' + str(initChicagoData) + ', but ' + str(initChicagoData - finChicagoData) + ' were eliminated due to lacking data represeted with NA.  The final total is ' + str(finChicagoData))

# establish the small buildings dataset  
chicagoDataSmall = chicagoData[chicagoData['Gross Floor Area - Buildings (sq ft)'] < 250000]
print(chicagoDataSmall[['Site EUI (kBtu/sq ft)', 'Source EUI (kBtu/sq ft)','Year Built', 'Gross Floor Area - Buildings (sq ft)']].describe())

# establish the large buildings dataset  
chicagoDataLarge = chicagoData[chicagoData['Gross Floor Area - Buildings (sq ft)'] >= 250000]
print(chicagoDataLarge[['Site EUI (kBtu/sq ft)', 'Source EUI (kBtu/sq ft)','Year Built', 'Gross Floor Area - Buildings (sq ft)']].describe())

# plot the histogram of the data
ax = plt.axes()
ax.set_xlabel('EUI (kBtu/ft\u00b2)')
ax.set_ylabel('Frequency')
plt.hist(chicagoData[['Site EUI (kBtu/sq ft)']],bins=50)
plt.show()

# plot the boxplot of the data
labels=["Chicago EUI"]
ax = plt.axes()
ax.set_xlabel('Chicago')
ax.set_ylabel('EUI (kBtu/ft\u00b2)')
plt.boxplot(chicagoData[['Site EUI (kBtu/sq ft)']],labels=labels)
plt.show()

# create a subplot of three different graphs 
fig, (ax1, ax2, ax3) = plt.subplots(1, 3,figsize=(19.5,6.5))
fig.suptitle('Show Chicago Energy Benchmarking Data')

chicagoArea = chicagoData['Gross Floor Area - Buildings (sq ft)']
chicagoSiteEUI = chicagoData['Site EUI (kBtu/sq ft)']
chicagoYearBuilt = chicagoData['Year Built']

ax1.hist(chicagoSiteEUI,bins=50)
ax1.set_xlabel('Site EUI (kBtu/ft\u00b2)')
ax1.set_ylabel('Frequency')
ax1.set_title('Histogram EUI')


ax2.hist(chicagoArea,bins=50)
ax2.set_xlabel('Building area (ft\u00b2)')
ax2.set_ylabel('Frequency')
ax2.set_title('Histogram Building Area')

ax3.hist(chicagoYearBuilt,bins=50)
ax3.set_xlabel('Year Built')
ax3.set_ylabel('Frequency')
ax3.set_title('Histogram Year Built')
plt.show()

# plot a boxplot to comapre diferent building types 
dataF = [chicagoDataLarge[['Site EUI (kBtu/sq ft)']],chicagoDataSmall[['Site EUI (kBtu/sq ft)']]]
b2 = np.array(dataF, dtype=object)
plt.figure(figsize=(10, 6))
ax = sns.boxplot(data = b2)
ax.set_xticklabels(['Small','Large'])
ax.set_xlabel('Building Type',fontweight ='bold')
ax.set_ylabel('Site EUI (kBtu/ft\u00b2)',fontweight ='bold')
plt.show()
