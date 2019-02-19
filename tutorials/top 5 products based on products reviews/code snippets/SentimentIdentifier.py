import os.path
import csv
import operator

def on_input(data1,data2):
   
    positive_count = data1.count("Positive")
    negative_count = data1.count("Negative")
    if positive_count >= negative_count:
        out = "positive"
    else:
        out = "negative"
    
    if (os.path.isfile("tempfile.csv")):
        file = open("/vrep/vflow/data/tempfile.csv","w+")
        file.write(data2+","+out+"\n")
        file.close()
    else:
        with open("/vrep/vflow/data/tempfile.csv","a") as myfile:
            myfile.write(data2+","+out+"\n")
            myfile.close()
            
def on_input1(data1,data2):
    if(data2 == "eof"):
        on_eof()
    else:
        on_input(data1,data2)

def on_eof():
    
    prod_sentiment= {}
    product_catalog = {}
    with open('/vrep/vflow/data/tempfile.csv', mode ='rU') as f:
        reader = csv.reader(f)
        for n, row in enumerate(reader):
            if not n:
                # Skip header row (n = 0).
                continue  
            pid, sentiment = row
            if pid not in prod_sentiment:
                prod_sentiment[pid] = list()
            prod_sentiment[pid].append(sentiment)
       
    for key, value in prod_sentiment.iteritems():
        positive = 0
        negative = 0
        sentiment = ""
        for x in value:
            if x == "positive":
                positive = positive + 1
            else:
                negative = negative + 1
        if(positive >= negative):
            sentiment = "positive"
        else:
            sentiment = "negative"
            
        percentage = float(positive * 100)/(positive + negative)

        product_catalog[key] = percentage
        
        
    sorted_product = sorted(product_catalog.items(), key=operator.itemgetter(1), reverse = True)
    final = sorted_product[:5]
    
    products = [x[0] for x in final]
    for prod in products:    
     api.send("output1", prod)
     
    os.remove("/vrep/vflow/data/tempfile.csv")
    
api.set_port_callback(["input1", "input2"], on_input1)