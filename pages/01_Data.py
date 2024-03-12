#Import modules and packages to be used
import streamlit as st
import pandas as pd
import pyodbc 


st.set_page_config(
    page_title= 'View Data',
    page_icon= '',
    layout= 'wide'
)
st.markdown('# 🗃️Data from Vodafone')

#Cache connection used to connect database
@st.cache_data()


#Loading environment variables from secret.toml file into a dictionary
def load_data():
    environment_variables = st.secrets['database']

     #Getting the values for the credentials you set in the '.env' file
    server = environment_variables['server_name']
    database = environment_variables['database']
    username = environment_variables['user']
    password = environment_variables['password']

    #Creating a connection string
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    #establishing a connestion to the database using pyodbc library
    connection = pyodbc.connect(connection_string)

    #retrieving data from database
    query = 'Select * From dbo.LP2_Telco_churn_first_3000'
    df = pd.read_sql(query,connection)

    connection.close()
    return df


df = load_data()
st.dataframe(df)

# Get list of numerical and categorical columns
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

# Create dropdown menus for selecting columns
selected_numeric_column = st.selectbox('Select Numerical Column:', numeric_columns)
selected_categorical_column = st.selectbox('Select Categorical Column:', categorical_columns)

# Display data based on selected columns
if st.checkbox('Show Data'):
    if selected_numeric_column and selected_categorical_column:
        selected_columns = [selected_numeric_column, selected_categorical_column]
        st.dataframe(df[selected_columns])
    elif selected_numeric_column:
        st.dataframe(df[selected_numeric_column])
    elif selected_categorical_column:
        st.dataframe(df[selected_categorical_column])
    else:
        st.warning('Please select at least one column.')


'Data Dictionary'

'The following describes the columns present in the data.'

'Gender : Whether the customer is a male or a female'

'SeniorCitizen : Whether a customer is a senior citizen or not?'

'Partner:  Whether the customer has a partner or not (Yes, No)'

'Dependents : Whether the customer has dependents or not (Yes, No)'

'Tenure : Number of months the customer has stayed with the company'

'Phone Service : Whether the customer has a phone service or not (Yes, No)'

'MultipleLines : Whether the customer has multiple lines or not'

'InternetService : Customer internet service provider (DSL, Fiber Optic, No)'

'OnlineSecurity : Whether the customer has online security or not (Yes, No, No Internet)'

'OnlineBackup -- Whether the customer has online backup or not (Yes, No, No Internet)'

'DeviceProtection -- Whether the customer has device protection or not (Yes, No, No internet service)'

'TechSupport -- Whether the customer has tech support or not (Yes, No, No internet)'

'StreamingTV -- Whether the customer has streaming TV or not (Yes, No, No internet service)'

'StreamingMovies -- Whether the customer has streaming movies or not (Yes, No, No Internet service)'

'Contract -- The contract term of the customer (Month-to-Month, One year, Two year)'

'PaperlessBilling -- Whether the customer has paperless billing or not (Yes, No)'

"Payment Method -- The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))"

'MonthlyCharges -- The amount charged to the customer monthly'

'TotalCharges -- The total amount charged to the customer'