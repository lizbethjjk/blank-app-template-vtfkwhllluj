import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HDB Resale Price Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Report a bug": "https://github.com/eeshawn11/HDB_Resale_Dashboard/issues",
        "About": "Thanks for dropping by!"
        }
    )

@st.cache_data(show_spinner=False, max_entries=1, ttl=2_630_000)  # dataset is updated monthly
def load_data():
    df_web = f.get_data()
    df_stored = pd.read_parquet("./assets/dataset.parquet")
    df = pd.concat([df_web, df_stored], axis=0)
    hdb_coordinates = f.get_coords_df()
    geo_df = f.get_chloropeth()
    return df, hdb_coordinates, geo_df
