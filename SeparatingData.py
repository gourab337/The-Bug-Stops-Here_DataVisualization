import pandas as pd
df = pd.read_csv("dataset.csv")  #reading the dataset.
columns = df.columns
#df.drop('index', inplace=True, axis=0)
df = df[df[columns[1:]] != 'ND']
df['Time Serie'] = pd.to_datetime(df['Time Serie'])  # converting string to datetime.
df['Time Serie'] = df['Time Serie'].dt.to_period('D')
print(df['Time Serie'].head())
for i in columns[2:]:
    df[i] = df[i].astype('float64')
df.to_excel("dataset.xlsx")  #saving the data as excel for data visualization in tableau
print(columns)
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
df1 = df.iloc[[-1]]
df1.to_excel("CurrentData.xlsx")

