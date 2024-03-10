import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title= 'View History',
    page_icon= '',
    layout= 'wide'
)
st.markdown('### History of Prediction')

def display_history_of_prediction():
    path = './data/history.csv'
    df = pd.read_csv(path)
    return df
st.markdown("<h1 style='text-align:center;'>View Past Predictions</h1>", unsafe_allow_html=True)
 
 
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed
 
with col1:
    pass
    #st.subheader('Pick Dates') # Placeholder content for the first column
 
with col2:
    st.markdown("<h3 style='text-align:left;'>Pick dates:</h1>", unsafe_allow_html=True)
    col_start_date, col_end_date = st.columns(2)  # Split the column into two
    with col_start_date:
        start_date = st.date_input('Start date', datetime.date.today())
        start_date = start_date.strftime('%Y-%m-%d')  # Convert to string
    with col_end_date:
        end_date = st.date_input('End date', datetime.date.today() + datetime.timedelta(days=1))
        end_date = end_date.strftime('%Y-%m-%d')  # Convert to string
    # if start_date <= end_date:
    #     st.success('Start date: `%s`  -   End date:`%s`' % (start_date, end_date))
 
# Load data based on selected dates
if __name__ == "__main__":
    df = past_predictions()  # Call the past_predictions function
    if 'Date' in df.columns:  # Check if 'Date' column exists
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]  # Filter the DataFrame based on selected dates
        st.dataframe(filtered_df)
    else:
        st.error("The DataFrame does not have a column named 'Date'. Please check your data.")


#if __name__ == '__main__':
#    display_history_of_prediction
