import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
df = pd.read_csv("dataset.csv")  #reading the dataset.
print(df.head())
columns = list(df.columns) # putting the columns in a list.
print(columns)
df['Time Serie'] = pd.to_datetime(df['Time Serie'])  # converting string to datetime. 
df['Time Serie'] = df['Time Serie'].dt.to_period('D')
# we had to hard code a lot because for some reason the format option of python was not working when saving excel files.
df1 = df[[columns[0], columns[1], columns[2]]]
df1.to_excel("australia.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[3]]]
df1.to_excel("europe.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[4]]]
df1.to_excel("new zealand.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[5]]]
df1.to_excel("uk.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[6]]]
df1.to_excel("brazil.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[7]]]
df1.to_excel("canada.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[8]]]
df1.to_excel("china.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[9]]]
df1.to_excel("hong kong.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[10]]]
df1.to_excel("india.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[11]]]
df1.to_excel("korea.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[12]]]
df1.to_excel("mexico.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[13]]]
df1.to_excel("south africa.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[14]]]
df1.to_excel("singapore.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[15]]]
df1.to_excel("denmark.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[16]]]
df1.to_excel("japan.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[17]]]
df1.to_excel("malaysia.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[18]]]
df1.to_excel("norway.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[19]]]
df1.to_excel("sweden.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[20]]]
df1.to_excel("sri lanka.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[21]]]
df1.to_excel("switzerland.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[22]]]
df1.to_excel("taiwan.xlsx", index=False)
df1 = df[[columns[0], columns[1], columns[23]]]
df1.to_excel("thailand.xlsx", index=False)

