import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title= 'View History',
    page_icon= '',
    layout= 'wide'
)
#st.markdown('# History of Prediction')


def display_history_of_prediction():
    path = './Datasets/history.csv'
    df = pd.read_csv(path)
    return df
st.markdown("<h1 style='text-align:center;'>🕰️History of  Past Prediction</h1>", unsafe_allow_html=True)
 
 
if __name__ == '__main__':
   df = display_history_of_prediction()
   st.dataframe(df)




