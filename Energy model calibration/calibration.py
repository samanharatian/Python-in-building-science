# Developed by Al Mitchell
# Updated on: 11/14/20222
# Contact: amitche8@hawk.iit.edu

# // Copyright (c) 2022-2023 The Built Environment Research Group (BERG)
# // Distributed under the MIT software license, see the accompanying
# // file LICENSE or http://www.opensource.org/licenses/mit-license.php.

# Description: Calculate CVRSME and NMBE from lists, good for calibration

from statistics import mean

def cvrsme(meterData, simData):
    data = []
    n = len(meterData)
    y_bar = mean(meterData)
    for m,s in zip(meterData,simData):
        data.append((((m-s)**2)/(n-1)))
    CVRSME = 100*(1/y_bar)*(sum(data)**(1/2))
    return CVRSME

def nmbe(meterData, simData):
    data = []
    n = len(meterData)
    y_bar = mean(meterData)
    for m,s in zip(meterData,simData):
        data.append(m-s)
    NMBE = (((sum(data))/((n-1)*y_bar))*100)
    return NMBE

     
meter = [1,1,3,4,5]
model = [1,1,3,4,5]


print(cvrsme(meter, model))
print(nmbe(meter,model))
