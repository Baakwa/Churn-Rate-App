import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sklearn

st.set_page_config(
    page_title= 'View Predict',
    page_icon= '',
    layout= 'wide'
)
st.title = ('Prediction')


#logTransformer class
class LogTransformer():
    def __init__(self, constant=1e-5):
        self.constant = constant

    def fit(self, x, y=None):
        return self
    def transform (self,x):
        return np.log1p(x + self.constant)
    

#Create function to load models and cache them
st.cache_resource(show_spinner='Model Loading')
def load_LR_pipeline():
    pipeline = joblib.load('./models/finished_model.joblib')
    return pipeline


st.cache_resource(show_spinner='Model Loading')   
def load_GB_pipeline():
    pipeline = joblib.load('./models/Gradient_boosting_model.joblib')
    return pipeline


#Create a select model function
def choose_model():

    columns1, columns2, columns3 = st.columns(3)
    
    with columns1:
            st.selectbox('Choose a Model',options=['Logistic Regression', 'Gradient Booster'],
            key = 'choose_model')
    with columns2:
        pass

    if st.session_state['choose_model'] == 'Logistic Regression':
        pipeline =  load_LR_pipeline()
    else:
        pipeline = load_GB_pipeline()

    #Load encoder from joblib
   
    encoder = joblib.load('./Models/encoder.joblib')

    return pipeline, encoder

#['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
#       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
 #      'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
  #     'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
   #    'MonthlyCharges', 'TotalCharges'],

#Define functions that makes prediction
def make_predictions(pipeline ,encoder):
    #Create variables for each field by extracting using the session_state
    gender = st.session_state['gender']
    SeniorCitizen = st.session_state['SeniorCitizen']
    Partner = st.session_state['Partner']
    Dependents = st.session_state['Dependents']
    tenure = st.session_state['tenure']
    PhoneService = st.session_state['PhoneService']
    MultipleLines = st.session_state['MultipleLines']
    InternetService = st.session_state['InternetService']
    StreamingMovies = st.session_state['StreamingMovies']
    OnlineSecurity = st.session_state['OnlineSecurity']
    OnlineBackup = st.session_state['OnlineBackup']
    DeviceProtection = st.session_state['DeviceProtection']
    TechSupport = st.session_state['TechSupport']
    StreamingTV = st.session_state['StreamingTV']
    Contract = st.session_state['Contract']
    PaperlessBilling = st.session_state['PaperlessBilling']
    PaymentMethod = st.session_state['PaymentMethod']
    MonthlyCharges = st.session_state['MonthlyCharges']
    TotalCharges = st.session_state['TotalCharges']

    #Creating column names
    columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges']

    #create a data
    data = [[gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,
             InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
             StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]]
    
    #creating a dataframe
    Predict_df = pd.DataFrame(data,columns=columns)

    
    #Predict a value from Predict_df
    Predict = pipeline.predict(Predict_df)
    Prediction = int(Predict[0])
    Prediction = encoder.inverse_transform(Predict)
    

    #Get probabilities
    Probability = pipeline.predict_proba(Predict_df)

    #Update state
    st.session_state['Prediction'] = Prediction
    st.session_state['Probability'] = Probability
    
    return Prediction, Probability
    
 
if 'Prediction' not in st.session_state:
    st.session_state['Prediction'] = None
if 'Probability' not in st.session_state:
    st.session_state['Probability'] = []



#Create columns for prediction page
def predict_page():

   with st.form('input_variables'):
        
        pipeline, encoder = choose_model() 

        columns1,columns2,columns3,columns4 = st.columns(4)

        with columns1:
            st.write('#### Customer Demographics')
            st.selectbox('Enter gender', options=('Female', 'Male'), key='gender')
            st.selectbox('Are you a senior citizen?', options=[0,1],key = 'SeniorCitizen')
            st.selectbox('Do you have a partner?', options=('Yes','No'), key='Partner')
            st.selectbox('Do you have a dependent?', options =('Yes','No'),key='Dependents')

            
        with columns2:
            st.write('#### Basic Services')
            st.number_input('Enter number of months', min_value = 0, max_value = 70, step=1,key='tenure')
            st.selectbox('Do you have a phone service?', options=('Yes', 'No'), key='PhoneService')
            st.selectbox('Do you use multiple line?', options =('Yes', 'No'),key='MultipleLines')
            st.selectbox('Choose your internet service provider', options=('DSL','Fiber optic','No'),key='InternetService')
            st.selectbox('Do you have streaming movies',options=('Yes','No','No internet service'),key='StreamingMovies')

        with columns3:
            st.write('#### Additional Services')
            st.selectbox('Do you have an online security',options = ('Yes','No','No internet service'), key= 'OnlineSecurity')    
            st.selectbox('Do you have an online back up', options=('Yes','No','No internet service'),key='OnlineBackup')  
            st.selectbox('Do you have a device protection', options=('Yes','No','No internet service'),key='DeviceProtection')
            st.selectbox('Do you have a tech support',options=('Yes','No','No internet service'),key='TechSupport')
            st.selectbox('Do you have a streaming Tv?',options=('Yes','No','No internet service'),key= 'StreamingTV')
           
        with columns4:
            st.write('#### Billing Information')
            st.selectbox('Select your contract term',options=('Month-to-month','One year','Two year'),key='Contract')
            st.selectbox('Do you have paperless billing?',options=('Yes','No'),key='PaperlessBilling')
            st.selectbox('Choose your payment method',options=('Electronic check','Mailed check','Bank Transfer (automatic)','Credit card (automatic)'), key='PaymentMethod')
            st.number_input('Enter monthly charges', min_value= 18, max_value= 119, key='MonthlyCharges')
            st.number_input('Enter your total charges',min_value =18, max_value=8671,key='TotalCharges')

        st.form_submit_button('Submit',on_click=make_predictions,kwargs=dict
        (pipeline=pipeline, encoder=encoder))



if __name__ == "__main__":
    st.markdown("### Make a Prediction")
    #choose_model()
    predict_page()

#Final_prdeiction = st.session_state['Prediction']
#st.write(Final_prdeiction)

if 'Prediction' not in st.session_state:
    st.session_state['Prediction'] = None
else:
    pred = st.session_state['Prediction'] 

    st.write(pred[0])


st.write(st.session_state)

#st.markdown(f"### The predict state of the person is {Prediction}")
 