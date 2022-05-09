import pandas as pd
import streamlit as st


@st.cache
def load_data(nrows: int, DATE_COLUMN: str, DATA_URL: str) -> pd.DataFrame:
    """Download data as csv and return it as a dataframe"""
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
