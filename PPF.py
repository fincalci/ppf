import pandas as pd
import math as m
import streamlit as st
import plotly.graph_objects as go

#from EMI import EMI, Amount, Loan, Years, fn
#c=pd.DataFrame()
#import streamlit_tags as stt

Amount = st.slider('Select Annual Invested Amount in Thousands',0,500,10)
#st.write("Loan amount:", Years)
Years=st.slider('Select Tenure Period in Years',0,60,15)
Rate=st.slider('Select Rate of Interest', 0.0,10.0,7.1)
st.write("-----------------------")
Rate=Rate/100  
Amount1=m.ceil(Amount *1000*Years)
Amt=Amount * 1000
pwr=Amt*(pow((1+Rate),Years)-1)/Rate
prr=(pwr*Rate)
#pwr=Amt*(pow(Rate,Years)-1)/Rate
st.write(prr+pwr)
TL=m.ceil(Amt*pwr)
##TL=m.ceil(Amt * (pow(((1 + Rate / 100), Years)-1)/Rate))
#st.write(TL)
I=TL-Amount1
li=['Amount','Interest']
n=[Amount1,I]
fig = go.Figure(
        go.Pie(
        labels = li,
        values = n,
        hoverinfo = "label+percent",
        textinfo = "value"
        ))  
st.subheader("Distribution of Payment")
st.plotly_chart(fig)
