import streamlit as st
import numpy as np
import pickle


pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Prediction")

#company
company = st.selectbox("Brand",df['Brand'].unique())

#processor brand 
P_brand = st.selectbox("Processor brand",df['Processor_brand'].unique())

#processor name 
p_name = st.selectbox("Processor name",df['Processor_name'].unique())

#processor generation
p_gen = st.selectbox("Processor Generation",[1,3,4,5,6,7,8,9,10,11,12,13,14,'Apple'])

#ram
ram = st.selectbox("Ram",[2,4,6,8,12,16,32,64])

#SSD
ssd = st.selectbox("SSD",[64,128,256,512,1000,2000])

#gpu
gpu = st.selectbox("GPU",df['Graphics_brand'].unique())

#screen size
scr_size = st.number_input('Screen Size')

#resolution
resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#touch screen
touchscreen = st.selectbox("TouchScreen",['Yes','No'])

#operating system
opsys = st.selectbox("Operating System",df['Operating_system'].unique())


if st.button('Predict Price'):
    
    ppi = None

    if touchscreen=='Yes':
        touchscreen = 1
    else:
        touchscreen = 0 

    if p_gen=='Apple':
        p_gen = 15
    
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    
    ppi = ((x_res**2)+(y_res**2))**0.5/scr_size

    querry = [company,P_brand,p_name,p_gen,ram,ssd,gpu,scr_size,ppi,touchscreen,opsys]

    feature_list = np.array(querry,dtype=object)

    feature_list = feature_list.reshape(1,11)

    price = (int(np.exp(pipe.predict(feature_list)[0])))
    min_price = price - 5000
    max_price = price + 5000

    st.title("Predicted Price: " + str(min_price) + " to " + str(max_price)+" Rs.")