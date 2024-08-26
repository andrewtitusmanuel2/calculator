import streamlit as st

st.header("Calculator APP")
st.write("This app is created by Andrew Titus Manuel")

num1 = st.number_input(label="Enter the first number",value=0)
option = st.selectbox("Select an Operation",["+","-","*","/"])
num2 = st.number_input(label="Enter the second number",value=0)
btn = st.button("Calculate")

if btn:
    if option=="+":
        st.subheader(num1+num2)
    elif option=="-":
        st.subheader(num1-num2)
    elif option=="*":
        st.subheader(num1*num2)
else:
    st.subheader(num1/num2)

