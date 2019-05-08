import pandas as pd
import io
import os
import re
import pydotplus
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier


def on_input(data):
    
    ## Reading Dataset
    dataset = pd.read_csv(io.StringIO(data),names=['SalesOrderID','CustomerID','ItemID','TotalItems','TotalPrice','MultipleSize','MultipleColor','Price','Discount','Freebies','PaymentMethod','SerialReturner','Return'], low_memory=False)
    dataset=dataset.drop(['SalesOrderID','CustomerID','ItemID','TotalPrice','Price','PaymentMethod'],axis=1)
    
    # Preparing training and testing data
    train_features = dataset.iloc[:100,:-1]
    test_features = dataset.iloc[90:,:-1]
    train_targets = dataset.iloc[:100,-1]
    test_targets = dataset.iloc[90:,-1]
    
    ## Creating model
    tree = DecisionTreeClassifier(criterion = 'entropy').fit(train_features,train_targets)
    
    ## predicting test data
    prediction = tree.predict(test_features)
    
    ## Model Accuracy
    accuracy = tree.score(test_features,test_targets)*100
    api.send("output", "Prediction" + str(accuracy) + "%")
    
    # Visualization
    data_feature_names = ["Total_Item","Multi_Size","Multi_Color","Discount_Voucher","Freebies","Serial_Returner"]
    data_targets = ["0","1"]
    #dot_data = StringIO()
    export_graphviz(tree, out_file='dot_data.dot',
				feature_names=data_feature_names,
				class_names=data_targets,
				impurity=False,
                filled=True, rounded=True,
                special_characters=True)
    
    f = pydotplus.graph_from_dot_file('dot_data.dot').to_string()
    f = re.sub('(\\\\nsamples = [0-9]+)(\\\\nvalue = \[[0-9]+, [0-9]+, [0-9]+\])', '', f)
    f = re.sub('(samples = [0-9]+)(\\\\nvalue = \[[0-9]+, [0-9]+, [0-9]+\])\\\\n', '', f)
    
    with open('tree_modified.dot', 'w') as file:
        file.write(f)
        
    cmd = "dot -T png tree_modified.dot -o /vrep/vflow/data/tree.png"
    os.system(cmd)

    api.send("output", "Open HTMl Viewer to see the tree")
    
    global code
    code = '''<!DOCTYPE html><html><head></head><body><h2>Tree Diagram</h2><img src="/app/pipeline-modeler/service/v1/repository/files/data/tree.png" alt="No Image Found"  width="1000" height="550"></body></html>'''
    
    display_graph()
    
    
api.set_port_callback("input", on_input)

def display_graph():
    api.send("output2", code)
