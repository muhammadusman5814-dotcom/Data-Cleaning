import pandas as pd 
df = pd.read_excel('Data Cleaning\Customer Call List.xlsx')
print(df)

df = df.drop_duplicates()
print("Data after removing duplicates")
df['Last_Name'] = df['Last_Name'].str.strip('[^0-9a-zA-Z-/\_.]')
print(df)

# df['Phone_Number'] = df['Phone_Number'].astype(str)
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','',regex=True)
df['Phone_Number'] = df['Phone_Number'].apply(lambda x : str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:9] + '-')
df['Phone_Number'] = df['Phone_Number'].str.rstrip('-')
df['Phone_Number'] = df['Phone_Number'].str.replace('nan','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na','')

df[['Street Name','State','Zip Code']] = df['Address'].str.split(',',expand=True)

df['Paying Customer'] = df['Paying Customer'].str.replace('N','No')
df['Paying Customer'] = df['Paying Customer'].str.replace('Y','Yes')
df['Paying Customer'] = df['Paying Customer'].str.replace('N/a','No')
df['Paying Customer'] = df['Paying Customer'].str.replace('Yeses','Yes')
df['Paying Customer'] = df['Paying Customer'].str.replace('Noo','No')
df['Paying Customer'] = df['Paying Customer'].str.replace('No/a','No')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('N','No')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Noo','No')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Y','Yes')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yeses','Yes')

df['Not_Useful_Column'] = df['Not_Useful_Column'].astype(str)
df['Not_Useful_Column'] = df['Not_Useful_Column'].str.replace('TRUE','True')
df['Not_Useful_Column'] = df['Not_Useful_Column'].str.replace('FALSE','False')

df['Last_Name'] = df['Last_Name'].str.strip('')
df = df.fillna("")

for x in df.index:
    if df.loc[x,'Phone_Number'] == '':
        df.drop(x, inplace=True)
df = df.reset_index(drop=True)        
print(df)

df.to_excel('Data Cleaning\Cleaned .xlsx', index=False)









                                                      


