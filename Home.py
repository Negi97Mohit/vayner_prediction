import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import base64

st.set_page_config(layout="wide")

def main():
    with open('5183000.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

    st.title('Facebook Marketing Analysis')
    facebook=pd.read_excel('Analyst_Candidate_Dataset_.xlsx',sheet_name='Facebook Data')    
    st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Campaign Dataset!</p>', unsafe_allow_html=True)
    st.write(facebook)
    cols1,cols2=st.columns(2)
    with cols1:
        date_Df=facebook.groupby(['Date']).sum()
        video_columns=date_Df[['Video Views', 'Video Views to 25%','Video Views to 50%', 'Video Views to 75%', 'Video Views to 95%','Video Views to 100%']]
        video_columns.replace(np.NAN,0)
        fig=px.bar(video_columns,barmode='group',height=400,width=600)
        st.plotly_chart(fig)
    with cols2:
        st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<p class="big-font">Insight!</p>', unsafe_allow_html=True)
        st.write('It is clear from the graph that a certain spike in video views was experfienced b/w feb 11 and 14 lets explore why??')
    
def why():
    facebook=pd.read_excel('Analyst_Candidate_Dataset_.xlsx',sheet_name='Question 4- Combining Data')
    cols1,cols2=st.columns(2)
    with cols1:
        groups_gender=facebook.groupby(['Campaign']).sum()
        fig=px.bar(groups_gender[['Total Revenue','Media Spend']],height=400,width=600)
        st.plotly_chart(fig)    
    with cols2:
        groups_gender=facebook.groupby(['Date','Campaign','Gender']).sum()
        groups_gender.reset_index()
        fig=px.bar(groups_gender[['Date','Total Revenue','Media Spend']],height=400,width=600)
        st.plotly_chart(fig)
    
       
if __name__=='__main__':
    main()
    why()