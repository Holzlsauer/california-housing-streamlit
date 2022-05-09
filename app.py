import numpy as np
import streamlit as st
from lib.data import load_data


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

data_load_state = st.text('Loading data...')
data = load_data(10000, DATE_COLUMN, DATA_URL)
data_load_state = st.text('Loading data... Done! (using cache)')

if st.checkbox('Show raw data', disabled=False):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

st.subheader('Map of pickups by hour')
time = st.slider('Hour:', min_value=0, max_value=23, value=[0, 23], step=1)
filtered_data = data[data[DATE_COLUMN].dt.hour >= time[0]]
filtered_data = filtered_data[filtered_data[DATE_COLUMN].dt.hour <= time[1]]
st.map(filtered_data)
