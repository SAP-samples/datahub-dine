# DataHub Interactive Education (DINE)

## Overview

Data Hub INteractive Education(DINE) is an educational content for [SAP Data Hub](https://www.sap.com/products/data-hub.html). Our hands-on exercises are developed to show you how to use SAP Data Hub features. 
SAP Data Hub allows you to connect to different data sources such as SAP HANA, SAP ERP, SAP BW, Oracle DB2, SQL Server, and many more and can process various data types; structured, semi-structured and unstructured using Kafka, streaming engine, text and image analysis, etc. SAP Data Hub can bring all your data together so you can work across them seamlessly. You can quickly develop your prototype on SAP Data Hub and the result can be easily turned to a production level system since SAP Data Hub takes care of execution, orchestration, scheduling, and monitoring. SAP Data Hub is developed on Kubernetes and therefore it is deployable on premise or in the cloud. It runs on a distributed execution engine and is designed for Big Data world by proving understanding on metadata in a Big Data landscape. 

Also go through the [official documentation](https://help.sap.com/viewer/p/SAP_DATA_HUB) of [SAP Data Hub](https://www.sap.com/products/data-hub.html)

DINE makes it easy to learn how to build pipelines in SAP Data Hub using its operators . It acts as reference for application developers and showcases the features of Data Hub in an easy to understand business scenario. This demo content comes complete with:  
- Sample data
- Code snippets
- Tutorials


## Prerequisites

SAP Data Hub Setup - Follow the [Installation Guide for SAP Data Hub](https://help.sap.com/viewer/e66c399612e84a83a8abe97c0eeb443a/2.4.latest/en-US/9f866d8ef9a94c30947f12e73eaf0dd9.html) and setup your SAP Data Hub environment.

You can also use [SAP Data Hub Developer Edition](https://blogs.sap.com/2017/12/06/sap-data-hub-developer-edition/) or [SAP Data Hub Trial Edition](https://blogs.sap.com/2018/04/26/sap-data-hub-trial-edition/)


## Scenarios

![Alt text](./tutorials/product%20recommendations%20using%20fp%20growth%20algorithm/images/Picture1.png "Optional title")

We will learn SAP Data Hub through the below scenarios which are based on dummy entity called as SAP Data Hub Market Place , an e-commerce platform which is developed for the purpose of demo and learning, where customers across the globe make thousands of purchases everyday.

The scenarios are detailed below:

- [Sentiment Analyser](./tutorials/top%205%20products%20based%20on%20products%20reviews/README.md) : This scenario is used to categorize products based on the reviews submitted by customers. This scenario is implemented is Python and uses  VORA text analysis engine to find the 5 most popular products based on customer reviews. Follow the [tutorial](./tutorials/top%205%20products%20based%20on%20products%20reviews/README.md) to implement this scenario.

- [Product Recommender](./tutorials/product%20recommendations%20using%20fp%20growth%20algorithm/README.md) : This scenario is used to recommend the products which are frequently bought together based on sales history. This scenario is implemented using Python Machine Learning Libraries. Follow the [tutorial](./tutorials/product%20recommendations%20using%20fp%20growth%20algorithm/README.md) to implement this scenario.

 
## Datasets

Our dataset for the above scenarios comprise of 6 files, which contain <b>customers</b>, <b>products</b> and <b>sales</b> information.
	
- <b>CUSTOMER</b> table has details  of  customers , this table has <b>ADDRESSID</b> which is mapped to <b>ADDRESS</b> table where details of customers address are stored.
		
- When a Customer buys a Product, Sales Order is generated (<b>SO_HEADER</b>) and each sales order has multiple order items (<b>SO_ITEM</b>).

- <b>SO_HEADER</b> has <b>PARTNERID</b> , a foreign key which links to <b>CUSTOMER</b> table.

- <b>SO_ITEM</b> has SALESORDERID, a foreign key which links to <b>SO_HEADER</b>.

- Each <b>SO_ITEM</b> will have <b>PRODUCTID</b> which is mapped to <b>PRODUCT</b> table where details of products are stored.

- Customer Reviews about the products are stored in <b>REVIEW</b> table.

- So basically we have 6 tables.

> <b><i> It is sythetic dataset derived from [SHINE](https://github.com/SAP/hana-shine-xsa) and is enriched to suit our usecases </i> </b>


### ER Diagram

![Alt text](./data/images/er_diagram.jpg "Optional title")

To access the datasets, explore the [data](./data) folder in this repository.


## Known issues

None


## Support

Please use GitHub [issues](https://github.com/SAP/datahub-dine/issues/new) for any bugs to be reported.


## License

Copyright (c) 2018 SAP SE or an SAP affiliate company. All rights reserved. This file is licensed under SAP Sample Code License Agreement, except as noted otherwise in the [LICENSE](/LICENSE) file.
