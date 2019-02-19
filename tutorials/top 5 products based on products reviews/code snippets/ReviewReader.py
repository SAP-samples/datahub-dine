import csv
import pandas
import StringIO
import io
import time
def on_input(data1,data2):
   
    product_df = pandas.read_csv(io.StringIO(data1), low_memory=False)
    reviews_df = pandas.read_csv(io.StringIO(data2), low_memory=False)
    
    product_ids = product_df[['PRODUCTID','PRODUCTNAME']]
    review_data= {}
    for index,row in product_ids.iterrows():
        review_data.clear()
        reviews_df.to_csv('review.csv',index = False)
        pid = row['PRODUCTID']
        pname = row['PRODUCTNAME']
        with open('review.csv', mode ='rU') as f:
            reader = csv.reader(f)
            review_data[pid] = list()
            for n, row in enumerate(reader):
                prid, rid, review = row
                if(pid == prid):
                    #review_data[pid].append((review))
                    api.send("output1",str(review))
                    api.send("output2",pname)  
        
    time.sleep(15)
    api.send("output1","eof")  
    api.send("output2","eof")
api.set_port_callback(["input1", "input2"], on_input)