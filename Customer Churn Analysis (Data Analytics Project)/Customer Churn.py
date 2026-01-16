"""
file: WA_Fn-UseC_-Telco-Customer-Churn.csv
name: Irene
-------------------------------
This project is based on the Telco Customer Churn dataset from Kaggle.
I redesigned the problem framing and evaluation process independently.

To optimize the annual program's participant loyalty in Microsoft Taiwan,
I analyzed the participant churn across different projects
and further examined potential reasons behind attrition to develop strategies.
However, I cannot present those datasets directly due to NDA,
so I demonstrate the similar churn analysis process using a public dataset,

# This project analyzes the potential factors contributing to customer churn.
# The raw data contains 7043 rows (customers) and 21 columns (features).
"""

# Import libraries for data processing
import numpy as np
import pandas as pd

# Import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Import library for reading files
import os

# Import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.figure_factory as ff

# global variable
num_features = ['tenure', 'MonthlyCharges', 'TotalCharges']

# read file
data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
data.head()

def main():
    print('\n<Data outline>')
    data_outline()
    print('Data exploration : The outline told me no missing value, and the dataset includes numerous categorical features, '
          '3 numerical features, and 1 binary target variable.\n' + '-' * 50 + '\n\n<Data manipulation>')
    data_manipulation()
    data_visualization＿churn(data) #Yes 26.5% / No 73.5%
    data_visualization＿churn_vs_features(data)
    data_visualization＿numerical_features(data)




# 01_overview data for cleaning
"""
The dataset includes numerous categorical features, 
3 numerical features, (tenure:73, MonthlyCharges:1585, TotalCharges:6531)
1 binary target variable (Churn)
"""
def data_outline():
    print("Rows:", data.shape[0]) #rows
    print("Columns:", data.shape[1]) #columns
    print(f"The number of missing value: {data.isnull().sum().values.sum()}") #missing value
    for col in data.columns:
        print(f"{col} : {data[col].nunique()}")


#02_examine data errors
"""
(改) I identified potential outliers using boxplots and the IQR method, 
and evaluated whether they represented data errors or meaningful customer behavior.
The process focuses on 3 numerical features, (tenure:73, MonthlyCharges:1585, TotalCharges:6531)
"""
def data_manipulation():
    redefined_data()
    examined_data(num_features)
    fix_data()


def redefined_data():
    """
    1. established a list for categorical features to avoid numeric operations.
    2. convert customerID to string to prevent numeric operations.
    3. kept 3 numerical features (tenure, MonthlyCharges, TotalCharges) as numeric for statistical analysis
    """

    # established a list for categorical features to avoid numeric operations
    cate_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'Churn']

    for col in cate_features:
        data[col] = data[col].astype('category')

    # convert customerID to string to prevent numeric operations
    data['customerID'] = data['customerID'].astype(str)

    # Keep 3 numerical features (tenure, MonthlyCharges, TotalCharges) as numeric for statistical analysis
    # convert num_features to global variable


def examined_data(num_features):
    """
    Visualize distributions of 3 numerical features to examine potential extreme values.
    """
    for col in num_features:
        plt.figure(figsize=(10,6)) #matplotlib.pyplot creates figure
        sns.histplot(data[col], kde=True, bins=50)  # seaborn creates histogram
        plt.title(f'{col} Distribution') #matplotlib.pyplot designes title
        plt.show()
        plt.close()

    """
    Figures exploration : 
    1. Tenure Distribution : The tenure distribution shows two clear peaks, 
    meaning most customers are either very new or have stayed with the company for a long time.
    2. MonthlyCharges Distribution : The customer groups concentrated on monthly charges (15-25) > (70-100) > (40-60)
    3. TotalCharge Distribution : Although no NaN values were detected initially, 
    further inspection revealed blank strings in TotalCharges, which require explicit conversion to NaN before analysis.
    """


def fix_data():
    """
    This function solves the problem of outlier in the TotalCharge Distribution
    After understanding the outlier of the TotalCharge Distribution,
    I found that tenure is 0 for these 11 rows, so I decided to fill the missing TotalCharges with 0.
    """
    data['TotalCharges'].dtype
    fake_missing_count = (data['TotalCharges'] == ' ').sum()
    print(f'The number of fake missing values: {fake_missing_count} (these values have to be replaced with null)') #11 fake missing values
    data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan) #replace fake values with null
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'])#convert Total charges to numeric(int or float) for operations
    print('-' * 50)
    print('Check which TotalCharges values are NaN, then look at tenure and MonthlyCharges.\n')
    print(data[data['TotalCharges'].isnull()][['tenure', 'MonthlyCharges']]) #check True or False of the data, then focus on tenure and monthlycharges
    data['TotalCharges'] = data['TotalCharges'].fillna(0)
    print('\nData exploration : after checking the data, I found that tenure is 0 for these 11 rows, so I decided to fill the missing TotalCharges with 0.')


def data_visualization＿churn(data):
    """
    This function calculates the number of churned and non-churned customers and presents
    their proportions to help understand class imbalance in the dataset.
    """
    # extract the labels and values of Churn
    classes, counts = zip(*data.Churn.value_counts().items())
    labels = list(classes)
    values = list(counts)

    # create Pie Chart
    trace = go.Pie(labels=labels, values=values,
                   marker=dict(colors=['pink', 'lightblue'], line=dict(color="white", width=2)),
                   rotation=90, hoverinfo="label+value+percent", hole=0.5)

    # create figure
    fig = go.Figure(data=[trace])
    fig.update_layout(title_text="Customer Attrition in Data", plot_bgcolor="rgb(243,243,243)",
                      paper_bgcolor="rgb(243,243,243)")
    fig.show()


def data_visualization＿churn_vs_features(data):
    """
    Compare churn vs non-churn distribution for a categorical feature
    """
    # clustered churn > Yes / not_churn > No
    churn = data[data['Churn'] == 'Yes']
    not_churn = data[data['Churn'] == 'No']
    data['Churn'] = data['Churn'].astype('category')
    cat_cols = data.select_dtypes(include='category').columns.drop('Churn') #Extract all categorical features, except 'Churn'
    for column in cat_cols:
        churn_yes=go.Pie(values = churn[column].value_counts().values.tolist(),
                         labels = churn[column].value_counts().keys().tolist(),
                         hoverinfo="label+percent+name",
                         domain=dict(x=[0,0.48]),
                         name="Churn Customers",
                         marker=dict(line=dict(width=2, color="rgb(243,243,243)")),hole=0.5)

        churn_no = go.Pie(values=not_churn[column].value_counts().values.tolist(),
                          labels=not_churn[column].value_counts().keys().tolist(),
                          hoverinfo="label+percent+name",
                          domain=dict(x=[0.52, 1]),
                          name="Non churn customers",
                          marker=dict(line=dict(width=2, color="rgb(243,243,243)")),hole=0.5)

        layout = go.Layout(
            title=column + "Customer attrition distribution",
            plot_bgcolor="white",
            paper_bgcolor="rgb(243,243,243)",
            annotations=[dict(text="Churn", font=dict(size=14), showarrow=False, x=0.15, y=0.5),
                         dict(text="Non churn", font=dict(size=14), showarrow=False, x=0.88, y=0.5)])


        import webbrowser
        webbrowser.open("about:blank")
        fig = go.Figure(data=[churn_yes, churn_no], layout=layout)
        fig.show()

        print("Data exploration:")


def data_visualization_numerical_feature(data):
    num_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    for col in num_cols:
        plot_hist(data, col)

def plot_hist(data, column):
    plt.figure(figsize=(8, 5))
    sns.histplot(data[column], kde=True, bins=30, color='skyblue')
    plt.title(f'{column} Distribution')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()


if __name__ == "__main__":
    main()





