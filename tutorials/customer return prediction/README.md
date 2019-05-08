## Customer Return Prediction

### Prerequisite

1. you should have an instance of mysql server up and running.

   create a table called "return"  in mysql and load the data in this table from [return.csv](../../data/return.csv).
  
2. To run this pipeline you should have one s3 account.

    upload the [customer.csv](../../data/customer.csv) and [product.csv](../../data/product.csv) in s3 bucket.
    
3. One Hana system should be up and running.
    
    create a table called "soHeader" in Hana and upload the data from [soHeader.csv](../../data/soHeader.csv) file.


### Creating pipeline for return prediction

1) Open the Data Hub dashboard and open the modeler.

   ![Alt text](./images/Capture1.JPG "Optional title")

2) Create a new graph by clicking on the "+" sign on the top.

   ![Alt text](./images/2.JPG "Optional title")

3) Search for the "MySQL Table Consumer" operator in the operator's section.

   ![Alt text](./images/3.JPG "Optional title")

4) Drag and drop "MySQL Table Consumer" operator in to the graph.

   ![Alt text](./images/4.JPG "Optional title")

5) Click on “Open Configuration” and provide the connection details for your mysql server. Select the source table as "return" which you have create in prerequisite section.

   ![Alt text](./images/5.JPG "Optional title")

6) Next drag and drop "Flowagent CSV Producer" operator in the graph.

   ![Alt text](./images/6.JPG "Optional title")

7) Connect the above two operators.

   ![Alt text](./images/7.JPG "Optional title")

8) Next step is to connect to the hana system. For that in datahub we have "HANA Table Consumer" operator which allows us to consume hana table. drag and drop this operator in the graph.

   ![Alt text](./images/8.JPG "Optional title")

9) Click on "Open Configuration" and provide the connection details for your HANA system. select the source table as "soHeader" which you would have created in the prerequisite steps.

   ![Alt text](./images/9.JPG "Optional title")
   
10) Drag and drop "Flowagent CSV Producer" in the graph and connect it with the "HANA Table Consumer" as shown below.

   ![Alt text](./images/10.JPG "Optional title")

11) Drag and drop two read file operators to read data from youe s3 bucket. For this scenario we are consuming product and customer data from s3.

   ![Alt text](./images/11.JPG "Optional title")

12) select the first "ReadFile" operator and assign the below property.

   <b>Service: s3 </b>
   
   <b>Connection: Connection details for s3</b>
   
   <b>Bucket: Bucket name</b>
   
   <b>Path: product.csv</b>
   
   ![Alt text](./images/12.JPG "Optional title")
   
13) Similarly select the second "ReadFile" operator and give the below properties.

   <b>Service:s3</b>
   
   <b>Connection: Connection details for s3</b>
   
   <b>Bucket: Bucket name</b>
   
   <b>Path: customer.csv</b>
   
   ![Alt text](./images/13.JPG "Optional title")
   
14) Now we need to install required python libraries to run our python code. To do that, select the Repository tab. Expand dockerfiles and create a folder named as “Return_Prediction_Docker_File” under that.

   ![Alt text](./images/14.JPG "Optional title")

15) Right click on “Return_Prediction_Docker_File” and select “Create File”.

   ![Alt text](./images/15.JPG "Optional title")

16) A create Docker window will pop up. Name it as “dockerfile”. Click on "Create".

   ![Alt text](./images/16.JPG "Optional title")

17) Copy the code from this [file](./dockerfile ) and paste it in the script section.

   ![Alt text](./images/17.JPG "Optional title")

18)Select the configuration for this docker file. Click on the “+” icon on the right side of Tags and add the following tags to the configuration by simply entering the library’s name and press enter.

   ![Alt text](./images/tags.png "Optional title")

19) Save the file and build this docker file by clicking build button. Once completed it will show you the build status as completed, and orange circle will turn to green.

   ![Alt text](./images/19.JPG "Optional title")

20) Again, go back to the graph and search for the "multiplexer" in the operators section.

   ![Alt text](./images/20.JPG "Optional title")

21) Drag and drop "1:2 Multiplexer" operator in the graph.

   ![Alt text](./images/21.JPG "Optional title")

22) Join the "Flowagent CSV Producer" which is connected to the "MySQL Table Consumer", to this python operator so we can read return data in to this python operator.

   ![Alt text](./images/22.JPG "Optional title")
   
23) Now search for the python2operator in the operators section and drag and drop it to the graph.

   ![Alt text](./images/23.JPG "Optional title")

24) Now let’s add 1 input port and 2 output ports to the python operator. To do that select the python operator and click on “add port”.

   ![Alt text](./images/24.JPG "Optional title")
   
25) Give the following properties for input port and then click OK.

   ![Alt text](./images/25.JPG "Optional title")
   
26) Similarly add the output ports. provide the below properties to the output ports.

   ![Alt text](./images/26.JPG "Optional title")
   
   ![Alt text](./images/27.JPG "Optional title")

27) Connect the input port of python operator to output port of multiplexer as shown below.

   ![Alt text](./images/28.JPG "Optional title")

28) The graph will look like below.

   ![Alt text](./images/29.JPG "Optional title")
   
29) Now select the python operator. It will show you all the available option with this operator, then choose open script option.

   ![Alt text](./images/30.JPG "Optional title")

30)  A new page will open where you can write python code. Copy the [code](./code%20snippets/PredictReturn.py) from here and paste it. This code will run decision tree algorithm on return data and create a tree for that.

   ![Alt text](./images/31.JPG "Optional title")

   Go back to the graph

31)  Now next thing is to tell the graph where we can find the python libraries that we installed. For that right click on python operator and select “Group”.

   ![Alt text](./images/32.JPG "Optional title")

32) Select the entire group and open the configuration for that.

   ![Alt text](./images/33.JPG "Optional title")

33) Next step is to add tags. Tags describe the runtime requirements of the operator and force the execution in a specific Docker image instance whose Docker file was annotated with the same Tag and Version.

   ![Alt text](./images/34.JPG "Optional title")

34) Click on “+” button to add tags. Add the below tags

  ![Alt text](./images/tags.png "Optional title")
  
35) Now add "Wiretap" and "HTML Viewer" operators to the graph and connect it to the "output" and "output1" port of the python operator as show below. Here "HTML Viewer" operator is use to render html code to the browser.
 
   ![Alt text](./images/35.JPG "Optional title")

36) Drag and drop another python operator in the graph.

   ![Alt text](./images/36.JPG "Optional title")

37) Create 4 input port namely "input1" , "input2", "input3", "input4" and one output port "output" in this python operator.

   ![Alt text](./images/37.JPG "Optional title")

38) connect the different data sources to this python operator as shown in below diagram.

   ![Alt text](./images/38.JPG "Optional title")

39) Again add "Group" to this python operator. For adding Group please follow step 22 to step 25.

   ![Alt text](./images/39.JPG "Optional title")

40) Now Open the script section of this python operator and copy and paste [this](./code%20snippets/JoiningDataset.py) code here.

   ![Alt text](./images/40.JPG "Optional title")

41) Add a terminal to this operator's output.

42) The final graph will look like below.

   ![Alt text](./images/41.JPG "Optional title")

43) Save the pipeline and run it.

   ![Alt text](./images/42.JPG "Optional title")

44) Once running you can select the "HTML Viewer" and select "OPEN UI". Here you will see the decision tree that had been created for the return dataset.

   ![Alt text](./images/43.JPG "Optional title")

45) This pipeline also joins the data from different data sources and save it in the "masterData.csv" file at /vrep/vflow/data/masterData.csv. To see this file just open "System Management" from your Datahub launchpad. 

   ![Alt text](./images/44.JPG "Optional title")

46) Choose files. Under files -> vflow -> data, you can see "masterData.csv" file.

   ![Alt text](./images/45.JPG "Optional title")

### Creating graph using SAP Analytics cloud.

1) login into your SAC account.

2) Create new story by clicking create -> new story button on the right hand side panel.

   ![Alt text](./images/46.JPG "Optional title")
   
3) Select "Access & Explore Data".

   ![Alt text](./images/47.JPG "Optional title")

4) Upload the "masterData.csv" file in SAC.

   ![Alt text](./images/48.JPG "Optional title")

5) By default SAC create dimention and measure autometically. If you want to change it you can chage it by clicking on the column and then from left hand side select the property. For example: If you want to change "return" to measure from dimention, you can simply click on return and change the property to measure.

   ![Alt text](./images/49.JPG "Optional title")

6) Now go to the story tab and add chart. Here you can create diffrent types of graph like pie chart, bar chart or donut chart etc.

   ![Alt text](./images/51.JPG "Optional title")

7) For more information about how to create graphs in SAC please refer [SAP analytics cloud documentation](https://www.sap.com/india/products/cloud-analytics.html)

8) Some of the sample graphs are shown below.

   ![Alt text](./images/SAC_Graphs.JPG "Optional title")
