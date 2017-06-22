import pandas as pd
import re

def load_data():

    olympics=pd.read_csv('files/olympics.csv',skiprows=1)
    olympics.rename(columns={'Unnamed: 0':'Country_name'},inplace= True)
    for i in olympics.columns:
        if bool(re.match(".*01 !.*",i)):
            olympics.rename(columns={i:re.sub('01 !','Gold',i)},inplace=True)
        elif bool(re.match(".*02 !.*",i)):
            olympics.rename(columns={i:re.sub('02 !','Silver',i)},inplace=True)
        elif bool(re.match(".*03 !.*",i)):
            olympics.rename(columns={i:re.sub('03 !','Bronze',i)},inplace=True)
    olympics['Country_name']=olympics['Country_name'].apply(lambda x:x.split("\xc2\xa0")[0])
    df=pd.DataFrame(data = list(olympics['Country_name']),columns = ['1'])
    index=[]
    olympics.index=df['1']
    for i in olympics.index:
        index.append(i.replace('\xc2\xa0', ''))
    olympics.index = index
    olympics=olympics[olympics.Country_name != "Totals"]
    return olympics

def first_country(df):
    return df.iloc[0,:]

def gold_medal(df):
    return df['Country_name'][df['Gold.2']==df['Gold.2'].max()].values[0]


def biggest_difference_in_gold_medal(df):
    return df['Country_name'][abs(df['Total']-df['Total.1'])==abs(df['Total']-df['Total.1']).max()].values[0]

def get_points(df):
    df['points'] = (df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2'])
    return df['points']
