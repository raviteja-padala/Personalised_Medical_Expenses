# Personalised_Medical_Expenses

## `Premise` :
> Medicine cost expenses refer to the financial burden individuals incur when purchasing medications for treatment of different medical conditions. These expenses encompass the costs of prescription drugs, over-the-counter medications, and other supplementary medications. The impact of medicine cost expenses on people's lives can be significant and multi-faceted. So it is essential for individuals to assess their medical expenses and optimize their lifestyle and healthcare costs accordingly.



## `About the Data` :

- "The dataset has been carefully curated based on a combination of personal experiences and real-life interactions. It comprises data collected from diverse individuals of varying ages, each with different medical conditions, and their corresponding average medical expenses. The selection process involved identifying the most prevalent medical conditions encountered by people. To ensure accuracy, I employed web scraping to gather information on the top medications available for each specific medical condition from one website, and I also retrieved the prices of these medications from another website. By incorporating this data into the dataset, I aimed to create a comprehensive and reliable resource for medical expenses analysis and prediction."

![image](https://github.com/raviteja-padala/Personalised_Medical_Expenses/blob/main/screenshots/med-pr2.png)


### `About the dataset`

* "The dataset consists of 11 independent variables, including Age, Gender, Cold, Cough, Fever, BP, Diabetes, Thyroid, Arthritis, Acidity, and Others, representing various medical conditions. With the exception of the Age and Gender columns, all other independent variables are represented by boolean values, indicating the presence or absence of the respective medical condition.

* The target variable of interest in this dataset is labeled as 'Expense'. This column contains data on the expenses incurred by individuals for different medical conditions."


## `Description`
The aim of this project to predict Medical expenses depending on the given medical conditions.


## `Tech Stack Used`
1. Python 
2. FlaskAPI 
3. Machine learning
4. HTML 

## `Infrastructure Required`
1. VS Code (you can use any other IDE)
2. GIT
3. GITHUB
4. GIT ACTIONS

## `How to run?`
This app is now available for offline run as well as Deployed on AWS Beanstalk.


### Step 1: Clone the repository
```bash
git clone https://github.com/raviteja-padala/Personalised_Medical_Expenses.git
```

### Step 2- Download the code to local and use any IDE for running the code.

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```


### Step 4 - Run the application server for web app
```bash
1. Run application.py
```

```bash
2. Open this link in browser: http://127.0.0.1:5000
```


## `Web Application Home Page`
![image](https://github.com/raviteja-padala/Personalised_Medical_Expenses/blob/main/screenshots/awsmed.png)



## `AWS Deployment Link` :

AWS Elastic Beanstalk link : [Elastic Beanstalk link](http://medicalexpenseprediction-env.eba-kwg8aq5x.us-east-1.elasticbeanstalk.com/predictdata)



### Approach for the Project

1. Data Ingestion:
   - In the Data Ingestion phase, the data is read as a CSV file.
   - Next, the data is split into training and test datasets and saved as separate CSV files.

2. Data Transformation:
   - During this phase, a ColumnTransformer Pipeline is created to preprocess the data.
   - For Numeric Variables:
     - Missing values are imputed using the median strategy through SimpleImputer.
     - The numeric data is then standardized using Standard Scaling.
   - For Categorical Variables:
     - Missing values are imputed using the most frequent strategy through SimpleImputer.
     - The categorical data is then transformed using ordinal encoding, followed by scaling with Standard Scaler.
   - This preprocessor is saved as a pickle file for later use.

3. Model Training:
   - In this phase, the data is trained with different models and the model peroformance is evaluated, and the best model is selected.
   - Hyperparameter tuning is performed on models to to enhance the overall prediction accuracy.
   - The trained model is saved as a pickle file for future predictions.

4. Prediction Pipeline:
   - The prediction pipeline contains functions to load the saved pickle files and make predictions in Python.

5. Flask App Creation:
   - A Flask web application is developed with a user interface to predict Medical expenses.
   - Users can interact with the web application to input data and receive predicted gemstone prices.

By following this approach, we aim to create an efficient and user-friendly model that predicts medical expenses based on the provided input data. The use of pickle files allows for seamless loading of preprocessed data and models, reducing processing time and improving the application's responsiveness.




### Exploratory Data Analysis Notebook

Link : [EDA Notebook](https://github.com/raviteja-padala/Personalised_Medical_Expenses/blob/main/notebooks/2_EDA_of_Med_Expenses.ipynb)

### Model Training Approach Notebook

Link : [Model Training Notebook](https://github.com/raviteja-padala/Personalised_Medical_Expenses/blob/main/notebooks/3_Model_training_on_Med_Exp_data.ipynb)



#  `Conclusion:`
> Addressing medicine cost expenses requires a multi-faceted approach, involving handling and managing health conditions. Solutions may include advocating for affordable drug pricing, expanding healthcare coverage, promoting generic medications, and investing in preventive measures to reduce the need for costly treatments. By addressing these challenges, we can work towards ensuring that access to essential medications is more equitable and that the burden of medicine cost expenses is alleviated for self, other individuals and communities.
<br>

<br>
Stay Healthy, Stay Happy. <br>
Thank you.
