import streamlit as st
import pandas as pd
import numpy as np
# import gspread as gs
import json
import urllib3
import certifi
url="https://api.thingspeak.com/channels/1836919/feeds.json?api_key=JYPUQP0P5P9C21ZN&results=2"
http = urllib3.PoolManager(
       cert_reqs='CERT_REQUIRED',
       ca_certs=certifi.where())
r = http.request('GET', url)
print(r.status)
data = json.loads(r.data.decode('utf-8'))
print(data)
df = pd.json_normalize(data, 'feeds')
print(df.head(10))


# gc = gs.service_account(filename='silicon-data-359717-e9efc5aa2712.json')

# sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1M8VpueMKAxAoIVbhofqVxkj5z_ajeIMyDCK5vo-cr7U/edit?usp=sharing")
# sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1vxyaK4dDdXzDJ5Axakrvik4CUxzGyHvgmmBQJ3Qo7dE/edit?usp=sharing')

# ws = sh.worksheet('sample')
# df = pd.DataFrame(ws.get_all_records())
df=pd.DataFrame(df)
def date_(x):
  return x.split("T")[0]
def time_(x):
       return x.split("T")[1]
def timex(x):
       return x.split("Z")[0]

df["Date"]=df['created_at'].apply(date_)
df["Time1"]=df['created_at'].apply(time_)
df["Time"]=df['Time1'].apply(timex)
df['Humidity OFF']=df['field5']
df['Humidity ON']=df['field6']
df['Moisture OFF']=df['field1']
df['Moisture ON']=df['field2']
df['Temperature OFF']=df['field3']
df['Temperature ON']=df['field4']
df["Date"]=df['created_at'].apply(date_)
df["Time1"]=df['created_at'].apply(time_)
df["Time"]=df['Time1'].apply(timex)
df1=df.drop(['field1','entry_id','created_at','field2','field3','field4','field5','field6','Time1','field7','field8'],axis=1)
# humidity_1=h['field5'].iloc[0]
# humidity_2=h['field5'].iloc[1]
# humidity_3=h['field5'].iloc[1]

# hum_1=h['field6'].iloc[0]
# hum_2=h['field6'].iloc[1]
# hum_3=h['field6'].iloc[1]

# m_1=h['field1'].iloc[0]
# m_2=h['field1'].iloc[1]
# m_3=h['field1'].iloc[1]

# mo_1=h['field2'].iloc[0]
# mo_2=h['field2'].iloc[1]
# mo_3=h['field2'].iloc[1]

# temp_1=h['field3'].iloc[0]
# temp_2=h['field3'].iloc[1]
# temp_3=h['field3'].iloc[1]

# tem_1=h['field4'].iloc[0]
# tem_2=h['field4'].iloc[1]
# tem_3=h['field4'].iloc[1]
# st.write(humidity)
# st.header("Intelligent Rain Prediction Irrigation System")
st.markdown(f'<p style="color:#33ff33;font-size:32px;border-radius:2%;">{"INTELLIGENT RAIN PREDICTION IRRIGATION SYSTEM"}</p>', unsafe_allow_html=True)

# st.markdown("""---""")
# col1,col2=st.columns(2)
# col1.subheader("MOISTURE")
# col2.subheader("MOISTURE")
# col1,col2=st.columns(2)
# col1.write("MOTOR ON")
# col2.write("MOTOR OFF")
# col1, col2,  = st.columns(2)
# col2.metric("", m_1, "")
# col1.metric("", mo_1, "")
# col1, col2,  = st.columns(2)
# col2.metric("", m_2, "")
# col1.metric("", mo_2, "")
# col1, col2,  = st.columns(2)
# col2.metric("", m_3, "")
# col1.metric("", mo_3, "")
# st.markdown("""---""")

# col1,col2=st.columns(2)
# col1.subheader("TEMPERATURE")
# col2.subheader("TEMPERATURE")
# col1,col2=st.columns(2)
# col1.write("MOTOR ON")
# col2.write("MOTOR OFF")

# st.subheader("Mositure")
# col1, col2,  = st.columns(2)
# col2.metric("", temp_1, "")
# col1.metric("", tem_1, "")
# col1, col2,  = st.columns(2)
# col2.metric("", temp_2, "")
# col1.metric("", tem_2, "")
# col1, col2,  = st.columns(2)
# col2.metric("", temp_3, "")
# col1.metric("", tem_3, "")
# st.markdown("""---""")


# col1,col2=st.columns(2)
# col1.subheader("HUMIDITY")
# col2.subheader("HUMIDITY")
# col1,col2=st.columns(2)
# col1.write("MOTOR ON")
# col2.write("MOTOR OFF")

# st.subheader("Mositure")
# st.subheader("Mositure")
# col1, col2,  = st.columns(2)
# col2.metric("", humidity_1, "")
# col1.metric("", hum_1, "")
# col1, col2,  = st.columns(2)
# col2.metric("", humidity_2, "")
# col1.metric("", hum_2, "")
# col1, col2,  = st.columns(2)
# col2.metric("", humidity_3, "")
# col1.metric("", hum_3, "")
# st.markdown("""---""")
st.markdown(f'<p style="color:#FF0000;font-size:28px;border-radius:2%;">{"TYPE OF CROP: PADDY"}</p>', unsafe_allow_html=True)
#st.subheader('TYPE OF CROP: PADDY')
st.table(df1)
# st.button("ON/OFF")
# st.subheader("MOTOR CURRENT STATUS:")
# motor="OFF"
# if motor=="ON":
#     st.markdown(f'<p style="color:#33ff33;font-size:32px;border-radius:2%;">{"Motor is ON"}</p>', unsafe_allow_html=True)
# else:
#     st.markdown(f'<p style="color:#ff0000;font-size:32px;border-radius:2%;">{"Motor is OFF"}</p>', unsafe_allow_html=True)
# st.markdown("""---""")
# wea="Sunny"
# st.subheader("WEATHER FORECAST:")
# if wea=="Cloudy":
#     st.markdown(f'<p style="color:#add8e6;font-size:32px;border-radius:2%;">{"Cloudy"}</p>', unsafe_allow_html=True)
# elif wea=="Sunny":
#     st.markdown(f'<p style="color:#ddee82;font-size:32px;border-radius:2%;">{"Sunny"}</p>', unsafe_allow_html=True)
# elif wea=="Rainy":
#     st.markdown(f'<p style="color:#1044ff;font-size:32px;border-radius:2%;">{"Rainy"}</p>', unsafe_allow_html=True)
# st.markdown("""---""")
# st.subheader("FAULT STATUS:")
# fault="YES"
# if motor=="NO":
#     st.markdown(f'<p style="color:#33ff33;font-size:32px;border-radius:2%;">{"There is no fault"}</p>', unsafe_allow_html=True)
# else:
#     st.markdown(f'<p style="color:#ff0000;font-size:32px;border-radius:2%;">{"There is a fault"}</p>', unsafe_allow_html=True)
# st.markdown("""---""")


# st.write("Done by:  DARK")
