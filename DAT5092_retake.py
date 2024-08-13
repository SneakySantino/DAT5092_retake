import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##################################################

# function for reading a given csv file

def load_csv(file_path):
    data = pd.read_csv(file_path, encoding='unicode_escape')
    return(data)

##################################################

# function for reading first 5 rows of a given dataset 

def head_csv(file_path):
    data = pd.read_csv(file_path, encoding='unicode_escape')
    head = data.head
    return(head)

##################################################

# reading and printing my chosen datasets: COL - Cost of Living Index, SDR - Sustainability Development Report 

data_COL = load_csv(r"C:\Users\Sonny\Documents\London Institute of Technology\Cost_of_Living_Index_by_Country_2024.csv")
data_COL_head = head_csv(r"C:\Users\Sonny\Documents\London Institute of Technology\Cost_of_Living_Index_by_Country_2024.csv")

data_SDR = load_csv(r"C:\Users\Sonny\Documents\London Institute of Technology\SDR Data.csv")
data_SDR_head = head_csv(r"C:\Users\Sonny\Documents\London Institute of Technology\SDR Data.csv")

print (data_COL_head)
print (data_SDR_head)

##################################################

# renaming "Rank" and "Score" columns for clarity after dataset merge (next step)

data_SDR.rename(columns={"Rank" : "SDR Rank"}, inplace=True)
data_SDR.rename(columns={"Score" : "SDR Score"}, inplace=True)
data_COL.rename(columns={"Rank" : "COLI Rank"}, inplace=True)

print (data_SDR.columns)
print (data_COL.columns)

##################################################

# merging the datasets using column "Country" as a key

data_merged = data_COL.merge(data_SDR, on="Country")

columns_order = [
    'Country',
    'Cost of Living Index',
    'Rent Index',
    'Cost of Living Plus Rent Index',
    'Groceries Index',
    'Restaurant Price Index',
    'Local Purchasing Power Index',
    'SDR Rank',
    'COLI Rank',
    'SDR Score'
]

# Reordering columns to above order 
final_data = data_merged[columns_order]

# Saving merged dataset to a new CSV file 
final_data.to_csv('DAT5092_final_data.csv', index=False)

#printing new dataset
print (final_data.head)
print (final_data.columns)

##################################################

# plotting a bar chart comparing SDR and LOCI Rank by country

x_axis = np.arange(len(final_data['Country']))

plt.bar(x_axis - 0.2, final_data['SDR Rank'], 0.4, label = 'SDR Rank') 
plt.bar(x_axis + 0.2, final_data['COLI Rank'], 0.4, label = 'COLI Rank') 

plt.xticks(x_axis, final_data['Country'], rotation = 90) 
plt.xlabel("Country") 
plt.ylabel("Rank") 
plt.title("COLI and SDR Rank comparison") 
plt.legend() 
plt.gca().invert_yaxis()

plt.show()

##################################################

# plotting scatter graphs

a, b = np.polyfit(final_data['SDR Score'],final_data['Cost of Living Index'], 1)
plt.scatter(final_data['SDR Score'],final_data['Cost of Living Index'], marker='x', color = "blue")
plt.plot(final_data['SDR Score'], (a*final_data['SDR Score'])+b)
plt.xlabel("SDR Score") 
plt.ylabel("Cost of Living Index") 
plt.title("Correlation between SDR Score and Cost of Living Index") 
plt.show()


##################################################
a, b = np.polyfit(final_data['SDR Score'],final_data['Rent Index'], 1)
plt.scatter(final_data['SDR Score'],final_data['Rent Index'], marker='x',  color = "red")
plt.plot(final_data['SDR Score'], (a*final_data['SDR Score'])+b)
plt.xlabel("SDR Score") 
plt.ylabel("Rent Index") 
plt.title("Correlation between SDR Score and Rent Index") 
plt.show()

##################################################

a, b = np.polyfit(final_data['SDR Score'],final_data['Cost of Living Plus Rent Index'], 1)
plt.scatter(final_data['SDR Score'],final_data['Cost of Living Plus Rent Index'], marker='x',  color = "orange")
plt.plot(final_data['SDR Score'], (a*final_data['SDR Score'])+b)
plt.xlabel("SDR Score") 
plt.ylabel("Cost of Living Plus Rent Index") 
plt.title("Correlation between SDR Score and Cost of Living Plus Rent Index") 
plt.show()

##################################################

a, b = np.polyfit(final_data['SDR Score'],final_data['Groceries Index'], 1)
plt.scatter(final_data['SDR Score'],final_data['Groceries Index'], marker='x',  color = "green")
plt.plot(final_data['SDR Score'], (a*final_data['SDR Score'])+b)
plt.xlabel("SDR Score") 
plt.ylabel("Groceries Index") 
plt.title("Correlation between SDR Score and Groceries Index") 
plt.show()

##################################################

a, b = np.polyfit(final_data['SDR Score'],final_data['Restaurant Price Index'], 1)
plt.scatter(final_data['SDR Score'],final_data['Restaurant Price Index'], marker='x',  color = "brown")
plt.plot(final_data['SDR Score'], (a*final_data['SDR Score'])+b)
plt.xlabel("SDR Score") 
plt.ylabel("Restaurant Price Index") 
plt.title("Correlation between SDR Score and Restaurant Price Index") 
plt.show()

##################################################
 
a, b = np.polyfit(final_data['SDR Score'],final_data['Local Purchasing Power Index'], 1)
plt.scatter(final_data['SDR Score'],final_data['Local Purchasing Power Index'], marker='x',  color = "purple")
plt.plot(final_data['SDR Score'], (a*final_data['SDR Score'])+b)
plt.xlabel("SDR Score") 
plt.ylabel("Local Purchasing Power Index") 
plt.title("Correlation between SDR Score and Local Purchasing Power Index") 
plt.show()

##################################################




