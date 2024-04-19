import streamlit as st 

# from streamlit_option_menu import option_menu
import pandas as pd
from sql import *
import base64
import datetime


def get_base64(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = "<style> .stApp{background-image: url('data:image/png;base64,%s');background-size: cover;background-repeat: no-repeat;}</style>"%bin_str  
    st.markdown(page_bg_img,unsafe_allow_html=True)

# set_background('images/windowsImg.jpg')

with st.sidebar:
    selected = st.selectbox("Main Menu",["Home","TodaysEntry","Visiulize"])



if selected == "Home":
    

    st.write("Home")
    # st.write(sum_coloumn)    
    css = """ 
    #u{
    background-color:#ffffffac;
    width:200px;
    height: 100px;
    text-align:center;
    
    border-radius: 5px;
    padding:5px;
    color:green;
    font-weight:bold;
    font-size:25px;
    }
    h1{
    font-size:30px;
    }     
"""
    st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        data = fetchTotalStockData()
        netStock = pd.DataFrame(data)
        sum_netStock = netStock.iloc[-1][0]
        st.markdown("""<h1>Total Stock</h1><div id = "u">"""+str(sum_netStock)+"""</div>""",unsafe_allow_html=True)

    with col2:
        data = fetchDueAmountData()
        dueAmount = pd.DataFrame(data)
        # sum_dueAmount = sum(dueAmount[0])
        sum_dueAmount = dueAmount.iloc[-1][0]
        st.markdown("""<h1>Due Amount</h1><div id = "u">"""+str(sum_dueAmount)+"""</div>""",unsafe_allow_html=True)

    with col3:
        data = fetchNetProfit()
        netProfit = pd.DataFrame(data,columns=["col1","col2"])
        sum_netProfit = netProfit.iloc[-1][0]
        st.markdown("""<h1>Net Profit</h1><div id = "u">"""+str(sum_netProfit)+"""</div>""",unsafe_allow_html=True)

    
    col1,col2,col3 = st.columns(3)
    with col1:
        data = fetchTotalCash()
        totalCash = pd.DataFrame(data)
        sum_totalCash = totalCash.iloc[-1][0] 
        st.markdown("""<br><h1>Total Cash</h1><div id = "u">"""+str(sum_totalCash)+"""</div>""",unsafe_allow_html=True)
        
    with col2:
        # data = fetchLogData()
        # logData = pd.DataFrame(data)
        # st.markdown("""<br><h1>Cash Log</h1>""",unsafe_allow_html=True)
        # st.dataframe(logData,use_container_width=True)
        pass


def addEntry():
    print("line 42 ")
    pass

if selected == "TodaysEntry":
    st.header("TodaysEntry")
    

        
    st.header("enter the detaials of todays earning")
    col1,col2 = st.columns(2)
    with col1:
        TodaysSales = st.number_input("Enter todays sales",value=0)
        if st.button("Add",key=1):
            addTodaysEntry(TodaysSales)
        
    with col2:
        OnlinePayment = st.number_input("Enter todays online payment",value=0)
        if st.button("Add",key=2):
            addOnlinePayment(OnlinePayment)


    st.header("Enter the  deatils of expenditure")
    col1,col2 = st.columns(2)
    with col1:
        PaymentTo = st.number_input("Enter todays payment given to",value=0)
        name = st.text_input("Name of the receiver")
        if st.button("Add",key=4):
            addPaymentTo(name,PaymentTo)
    
    with col2:
        HomeExpenditure = st.number_input("Enter todays Home expenditure",value=0)
        reason = st.text_input("Enter the reason")
        name = st.text_input("Name of the reciver1")
        if st.button("Add",key=5):
            addHomeExpenditure(reason,name,HomeExpenditure)
    
    col1,col2 = st.columns(2)
    with col1:
        LariBhado = st.number_input("Enter todays lari bhado",value=0)
        name = st.text_input("Name of the reciver2")
        if st.button("Add",key=6):
            addLoriBhado(name,LariBhado)
    
    with col2:
        OtherPayment = st.number_input("Enter todays otherPayment",value=0)
        name = st.text_input("Name of the reciver3")
        if st.button("Add",key=7):
            addOtherPayment(name,OtherPayment)
    



if selected == "Visiulize":
    st.write("Visiulize")
    st.date_input("Enter Date",datetime.date(2024,1,1))
    col1,col2 = st.columns(2)
    with col1:
        data = fetchLogData()
        logData = pd.DataFrame(data,columns=["sales","Date"])
        st.markdown("""<br><h1>Cash Log</h1""",unsafe_allow_html=True)
        st.dataframe(logData,use_container_width=True)

    with col2:
        data = fetchPaymentTo()
        paymentTo = pd.DataFrame(data)
        st.markdown("""<br><h1>Payment To</h1>""",unsafe_allow_html=True)
        st.dataframe(paymentTo,use_container_width=True)
    st.markdown("""<br><br>""",unsafe_allow_html=True)
    print(logData)
    st.line_chart(logData,x="Date",y="sales", use_container_width=True)
    st.markdown("""<br><br>""",unsafe_allow_html=True)

    data = fetchNetProfit()
    netProfit = pd.DataFrame(data,columns=["NetProfit","Date"])
    st.line_chart(netProfit,x="Date",y="NetProfit",use_container_width=True)




