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
    df_stored = pd.read_parquet("./devcontainer/resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014_locationdata.csv")
    df = pd.concat([df_web, df_stored], axis=0)
    hdb_coordinates = f.get_coords_df()
    geo_df = f.get_chloropeth()
    return df, hdb_coordinates, geo_df

with st.spinner("Fetching data..."):
    df, hdb_coordinates, geo_df = load_data()

if "geo_df" not in st.session_state:
        st.session_state.geo_df = geo_df

if "df_raw" not in st.session_state:
    st.session_state.df_raw = df.head(10).copy()

@st.cache_data(show_spinner=False)
def get_planning_areas():
    planning_areas = []
    polygons = []
    for i in range(len(st.session_state.geo_df["features"])):
        planning_areas.append(
            st.session_state.geo_df["features"][i]["properties"]["PLN_AREA_N"]
        )
        try:
            polygons.append(
                Polygon(
                    st.session_state.geo_df["features"][i]["geometry"]["coordinates"][0]
                )
            )
        except:
            polygons.append(
                Polygon(
                    st.session_state.geo_df["features"][i]["geometry"]["coordinates"][
                        0
                    ][0]
                )
            )
    return planning_areas, polygons

planning_areas, polygons = get_planning_areas()
