import koreanize_matplotlib
import pandas as pd
import plotly.express as px
import streamlit as st
from sas_login import SASLogin

# Page title
st.set_page_config(page_title="SAS Login", layout="wide")

본청_광역 = pd.read_csv('https://www.googleapis.com/drive/v3/files/1SsnRU9nG0Zhk5b18gZjUzInAyQAVFBWa?alt=media&key=AIzaSyAViyxfaLGCnbTU_km6EIOfbV2eIn1rROM',encoding='euc-kr')
plotly_df = 본청_광역.melt(
    id_vars=['PRD_DE', 'C1', 'C1_NM'],
    value_vars=['본청_공무원_비율', '광역_공무원_비율'],
    var_name='비율_종류',
    value_name='비율'
)

# Streamlit app
st.title("본청 및 광역 공무원 비율 대시보드")

# Dropdown for selecting a city
city = st.selectbox("도시를 선택하세요:", plotly_df['C1_NM'].unique())

# Filter data based on selected city
city_data = plotly_df[plotly_df['C1_NM'] == city]

# Plotting using Plotly for interactive features
fig = px.line(
    city_data,
    x='PRD_DE',
    y='비율',
    color='비율_종류',
    title=f'{city} - 본청 및 광역 공무원 비율'
)

# Customize layout
fig.update_layout(
    xaxis_title="연도",
    yaxis_title="비율",
    legend_title="비율 종류",
    template="plotly_white"
)

# Display the plot
st.plotly_chart(fig)


# Create two columns for layout
col1, col2 = st.columns([1, 3])  # Adjust column ratio as needed

# Login form in the left column
with col1:
    st.title("SAS Login")  # Optional, you can also remove this line if you don't want a title

    # Server selection dropdown
    server_options = [
        "US Home Region 1",
        "US Home Region 2",
        "European Home Region 1",
        "Asia Pacific Home Region 1",
        "Asia Pacific Home Region 2"
    ]
    server = st.selectbox("Select Server", server_options)

    # ID and Password input
    id = st.text_input("Enter your ID", type="default")
    password = st.text_input("Enter your Password", type="password")

    # Login button
    if st.button("Login"):
        try:
            # Attempt to log in
            sas_session = SASLogin(id, password,'oda', server)
            
            st.success("Logged in successfully!")
            
            # Display session details if needed
            st.write("Session Info:", sas_session)
            
        except Exception as e:
            st.error(e)

# Optionally, use the right column (col2) for any additional content
with col2:
    st.write("Welcome to the SAS Login portal.")
    # You can add more elements here if needed
