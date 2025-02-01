import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Deepak's ecom app")
    st.sidebar.title('u can upload your files here')

    upload = st.sidebar.file_uploader('Upload your file here', type=['csv','xlsx'])

    if upload is not None:
        try:
            if upload.name.endswith('.csv'):
                df = pd.read_csv(upload)
            else:
                df = pd.read_excel(upload)
            st.sidebar.success('File uploaded successfully')

            st.subheader('I am going to show you a  data details')
            st.dataframe(df.head())

            st.subheader('lets see some more details of data')
            st.write('Shape of data',df.shape)

            st.write('Column Names',df.columns)

            st.write('Missing values',df.isnull().sum())

            st.subheader('I will show you the bit of stats')
            st.write(df.describe())

        except Exception as e:
            st.write('Error:', e)


if __name__ == '__main__':
    main()