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

with st.sidebar:
    st.markdown(
        """
        Created by [**eeshawn**](https://eeshawn.com)

        - Connect on [**LinkedIn**](https://www.linkedin.com/in/shawn-sing/)
        - Project source [**code**](https://github.com/eeshawn11/HDB_Resale_Dashboard/)
        - Check out my other projects on [**GitHub**](https://github.com/eeshawn11/)
        """
        )

with st.container():
    st.title("Singapore HDB Resale Price from 2000")
    st.image("./assets/nathan-oh-PWIOX6atM4w-unsplash.jpg")
    st.markdown("<p style='text-align: center;'>Photo by <a href='https://unsplash.com/fr/@nathanohk' target='_blank'>Nathan Oh</a> on <a href='https://unsplash.com/photos/PWIOX6atM4w' target='_blank'>Unsplash</a></p>", unsafe_allow_html=True)
  
    st.markdown(
        """
        This dashboard is inspired by [Inside Airbnb](http://insideairbnb.com/) and various other dashboards I've come across on the web. 
        As a new data professional, this is an ongoing project to document my learning with using Streamlit and various Python libraries 
        to create an interactive dashboard. While this could perhaps be more easily created using PowerBI or Tableau, I am also taking the 
        opportunity to explore the various Python plotting libraries and understand their documentation.

        The project is rather close to heart since I've been looking out for a resale flat after getting married in mid-2022, although with 
        the recent surge in resale prices as of 2022, it still remains out of reach. Hopefully this dashboard can help contribute to my 
        eventual purchase decision, although that may also require adding in various datasets beyond the current historical information.

        Data from the dashboard is retrieved from Singapore's [Data.gov.sg](https://data.gov.sg/), a free portal with access to publicly-available 
        datasets from over 70 public agencies made available under the terms of the [Singapore Open Data License](https://data.gov.sg/open-data-licence). 
        In particular, we dive into the HDB resale flat prices [dataset](https://data.gov.sg/dataset/resale-flat-prices), while town boundaries 
        in the chloropeth map are retrieved from [Master Plan 2014 Planning Area Boundary](https://data.gov.sg/dataset/master-plan-2014-planning-area-boundary-no-sea).
        """
    )

st.markdown("---")

with st.container():
    st.markdown("## Background")
    st.markdown(
        """
        The [Housing & Development Board (HDB)](https://www.hdb.gov.sg/cs/infoweb/homepage) is Singapore's public housing authority, responsible for 
        planning and developing affordable accommodation for residents in Singapore. First established in 1960, over 1 million flats have since been completed 
        in 23 towns and 3 estates across the island.Aspiring homeowners generally have a few options when they wish to purchase their first home, either purchasing a new flat directly from HDB, or 
        purchasing an existing flat from the resale market.
        
        While new flats have been constantly developed to meet the needs of the growing population, HDB has been operating on a Build To Order (BTO) 
        since 2001. As the name suggests, the scheme allows the government to build based on actual demand, requiring new developments to meet 
        a minimum application rate before a tender for construction is called. This generally requires a waiting period of around 3 - 4 years for completion.

        However, 2 years of stoppages and disruptions during COVID caused delays to various projects, lengthening the wait time to around 5 years. This
        caused many people to turn to the resale market instead. Since these are existing developments, resale transactions can usually be expected to 
        complete within 6 months or so, which is a significant reduction in wait time. This surge in demand has also caused a sharp increase in resale prices,
        with many flats even crossing the S$1 million mark.
        """
    )
