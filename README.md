# Applied-Data-Science---Landing-success-rate-of-the-first-stage-of-a-rocket-launch
As a new rocket company, SpaceY, our attention is to compete with SpaceX founded by Elon Musk. We found the reason that SpaceX can launch rockets in a lower price is SpaceX can recover and reuse the first stage. Therefore, if we can determine if the first stage will land, we can determine the cost of a launch. 

This project aims to analyze data information from SpaceX and to find out the success rate of landing. In order to compete with SpaceX, we need to predict if SpaceX will reuse the first stage to decrease its cost, then we can determine the price of each launch in SpaceY properly and reasonably.

In this project, we used SpaceX REST API and web scraping methodologies to do data collection, and then used Data Wrangling to transform raw data into a clean dataset. We then performed Exploratory Data Analysis to see the visualization of the data. Next, SQL queries were used to select the specific information we need from the whole dataset. We performed interactive visual analytics using Folium and dashboard using Plotly Dashboard, which may product interactive maps and dashboard to show more interesting and useful information of our data intuitively. Then in order to predict the landing results of the launches and to determine the cost of a launch, we created a machine learning pipeline to predict if the first stage will land.

From the EDA we see the flight number seems to have little effect on landing success, while the payload seems to have more impact on it. And from 2010 to 2017, the success rate of landing was increase continuously.

From the predictive analysis, We calculated the accuracy of each classification model (logistic regression, svm, decision tree, KNN) and plotted the confusion matrix of each of them. Then we chose the decision Tree classifier as the model used to predict.
