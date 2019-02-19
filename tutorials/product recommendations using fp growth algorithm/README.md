
## Product recommendations using FP Growth Algorithm

![Alt text](./images/Picture1.png "Optional title")

> <b><i> Load the data required for the scenario by following this [tutorial](https://github.wdf.sap.corp/refapps/datahub-dine/blob/master/tutorials/loading%20of%20data/README.md) </i> </b>

1. Open the Data Hub dashboard and open the modeler.

  ![Alt text](./images/1.jpg "Optional title")


2. Modeler welcome page Will look something like this.

  ![Alt text](./images/2.jpg "Optional title")


3. Create a new graph by clicking on the "+" sign on the top.

  ![Alt text](./images/3.jpg "Optional title")


4. Search for the read file operator in the operator's section.

  ![Alt text](./images/4.jpg "Optional title")


5. Drag and drop "Read File" into the graph.

  ![Alt text](./images/5.jpg "Optional title")


6. Click on “Open Configuration” and provide the following properties.

    <b>Service: file</b>
    
    <b>Path: data/product.csv</b>
    
    <b>Only read on change: true</b>

    Let the other properties remains the same.
    
  ![Alt text](./images/6.jpg "Optional title")
    
    
7. Again Drag and drop “Read File” into the graph.

  ![Alt text](./images/7.jpg "Optional title")


8. Click on “Open Configuration” and provide the following properties.

  <b>Service: file</b>
  
  <b>Path: data/soItem.csv</b>
  
  <b>Only read on change: true</b>
  
  Let the other properties remains the same.

  ![Alt text](./images/8.jpg "Optional title")


9. Now we need to install required python libraries to run FPGrowth algorithm. To do that, select the Repository tab. Expand Docker File and create a folder named as “python library” under that.

  ![Alt text](./images/9.jpg "Optional title")


10. Right click on “python Libraries” and select “Create Docker File”.

  ![Alt text](./images/10.jpg "Optional title")


11. A create Docker window will pop up. Name it as “RecommenderLibraries”. Click on OK.

  ![Alt text](./images/11.jpg "Optional title")


12. Copy the commands from this [file](./dockerfile ) and paste it in the script section.

  ![Alt text](./images/12.jpg "Optional title")


13. Select the configuration for this docker file. Click on the “+” icon on the right side of Tags and add the following tags to the configuration by simply entering the library’s name and press enter.

-	pyfpgrowth
-	pandas
-	python27

  ![Alt text](./images/13.jpg "Optional title")


14. Save the file and build this docker file by clicking build button.  Once completed it will show you the build status as completed, and orange circle will turn to green.

  ![Alt text](./images/14.jpg "Optional title")


15. Again, go back to the graph and search for the python2operator in the operators section.

  ![Alt text](./images/15.jpg "Optional title")


16. Drag and drop this operator in the graph.

  ![Alt text](./images/16.jpg "Optional title")


17. Now let’s add 2 input ports and 1 output port to the python operator. Select the python operator and click on “add port”.

  ![Alt text](./images/17.jpg "Optional title")


18. Give the following properties for input port and then click OK.

  Similarly add one more input port and called it “input2”

  ![Alt text](./images/18.jpg "Optional title")

  ![Alt text](./images/19.jpg "Optional title")


19. Similarly add the output port.

  ![Alt text](./images/20.jpg "Optional title")


20. Join “Read File 1” operator to “input1” port of “python2operator” and
“Read File 2” operator to “input2” port of “python2operator” as shows in the figure below.

  ![Alt text](./images/21.jpg "Optional title")


21. Select the ToString Convertor if prompted and then click OK.

  ![Alt text](./images/22.jpg "Optional title")


22. The graph will look like below.

  ![Alt text](./images/23.jpg "Optional title")


23. Now select the python operator. It will show you all the available option with this operator, then choose open script option.

  ![Alt text](./images/24.jpg "Optional title")


24. A new page will open where you can write python code. Copy the [code](./code%20snippets/FPGrowthAlgorithm.py) from here and paste it.

  ![Alt text](./images/25.jpg "Optional title")
  
  Go back to the graph


25. Now next thing is to tell the graph where we can find the python libraries that we installed. For that right click on python operator and select “Group”.

  ![Alt text](./images/26.jpg "Optional title")


26. Select the entire group and open the configuration for that.

  ![Alt text](./images/27.jpg "Optional title")

27. Next step is to add tags. Tags describe the runtime requirements of the operator and force the execution in a specific Docker image instance whose Docker file was annotated with the same Tag and Version.


28. Click on “+” button to add tags as below.
pyfpgrowth
pandas
python27

  ![Alt text](./images/28.jpg "Optional title")


29. Next step is to see the output on the terminal. For that search Terminal operator and add it to the graph.

  ![Alt text](./images/29.jpg "Optional title")


30. Connect output port of the “Python2Operator” to input port of the Terminal

  ![Alt text](./images/30.jpg "Optional title")


31. Save the pipeline and call it as “Recommender”.

  ![Alt text](./images/31.jpg "Optional title")


32. Click on run to run the pipeline.

  ![Alt text](./images/32.jpg "Optional title")


33. See the output as below

  ![Alt text](./images/34.png "Optional title")
  
  ![Alt text](./images/33.jpg "Optional title")



