import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.title("Hello P!")

st.write("eiei")
st.info("info")
st.success("success")
st.error("error")
st.warning("warning")

placeholder = st.empty()
status = st.radio("chose one",["error","success"])

status
if status == "success":
    placeholder.success("success")
else:
    placeholder.error("error")