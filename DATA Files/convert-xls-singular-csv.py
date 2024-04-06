#importing pandas as pd 
import xlrd
#must be installed on local computer to work xlrd (possibly mac only)
import csv
import pandas as pd 

# Read and store content 
# of an excel file 
read_file = pd.read_excel ("DATA Files/epicaDC.deuttemp.EDC3-AICC.xls") 

# Write the dataframe object 
# into csv file 
read_file.to_csv ("epica-deutertemp.csv", 
				index = None, 
				header=True) 
	
# read csv file and convert 
# into a dataframe object 
df = pd.DataFrame(pd.read_csv("epica-deutertemp.csv")) 

# show the dataframe 
df

