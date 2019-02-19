import csv
import pandas
import pyfpgrowth
import StringIO
import io

def on_input(data1,data2):
    soid_data= {}
    final = ""
    df1 = pandas.read_csv(io.StringIO(data1), low_memory=False)
    df2 = pandas.read_csv(io.StringIO(data2), low_memory=False)
    df1 = df1.merge(df2, on='PRODUCTID')
    df3 = df1[['SALESORDERID','PRODUCTNAME']]
    df3.to_csv('itemSet.csv',index = False)
    with open('itemSet.csv', mode ='rU') as f:
        reader = csv.reader(f)
        for n, row in enumerate(reader):
            if not n:
                # Skip header row (n = 0).
                continue  
            soid, pname = row
            if soid not in soid_data:
                soid_data[soid] = list()
            soid_data[soid].append((pname))
    patterns = pyfpgrowth.find_frequent_patterns(soid_data.values(), 8)
    rules = pyfpgrowth.generate_association_rules(patterns, 0.8)
    for key, value in rules.iteritems():
        if (len(key)<=2 and len(value[0])<=1):
            final = final + str(key) + ":" + str(value[0]) + "\n" 
    api.send("output", "Rules :" + final)
api.set_port_callback(["input1", "input2"], on_input)
