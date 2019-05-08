import csv
import pandas as pd
import StringIO
import io
from datetime import datetime
from datetime import date

def on_input(returnData,salesData,productData,customerData):
    
    ## reading the dataset
    returnDataset = pd.read_csv(io.StringIO(returnData),names=['SALESORDERID','CUSTOMERID','PRODUCTID','TOTALITEMS','TOTALPRICE','MULTIPLESIZE','MULTIPLECOLOR','PRICE','DISCOUNT','FREEBIES','PAYMENTMETHOD','SERIELRETURNER','RETURN'], low_memory=False)
    productDataset = pd.read_csv(io.StringIO(productData), low_memory=False)
    customerDataset = pd.read_csv(io.StringIO(customerData),low_memory=False)
    salesDataset = pd.read_csv(io.StringIO(salesData),names=['SALESORDERID','CREATEDAT','CHANGEDAT','CUSTOMERID','GROSSAMOUNT','NETAMOUNT','TAXAMOUNT','LIFECYCLESTATUS','BILLINGSTATUS','DELIVERYSTATUS'] ,low_memory= False)
    
    customerDataset['AGE'] = customerDataset['DOB'].apply(calculate_age) 
    
    customerDataset.loc[customerDataset.AGE <= 30, 'AGE_GROUP'] = 'Young'
    customerDataset.loc[(customerDataset.AGE >30) & (customerDataset.AGE <= 50), 'AGE_GROUP'] = 'Middle_aged'
    customerDataset.loc[customerDataset.AGE > 50, 'AGE_GROUP'] = 'Old' 
    
    joinedDataset = returnDataset.merge(customerDataset, on='CUSTOMERID')
    joinedDataset = joinedDataset.merge(productDataset, on='PRODUCTID')
    #joinedDataset = joinedDataset.merge(salesDataset, on='SALESORDERID')
    joinedDataset.to_csv('/vrep/vflow/data/masterDate.csv',index = False)
    api.send("output", str(joinedDataset))
api.set_port_callback(["input1", "input2","input3","input4"], on_input)

def calculate_age(born):
    born = datetime.strptime(born, "%Y-%m-%d").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
