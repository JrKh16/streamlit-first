import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


st.header("Hello P!")

st.write("This is my first streamlit")
st.info("info")
st.success("success")
st.error("error")
st.warning("warning")
st.markdown("eiei")

placeholder = st.empty()
status = st.radio("choose one",["error","success"])
status
if status == "success":
    placeholder.success("success")
else:
    placeholder.error("error")


chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["a", "b"])
st.line_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(21, 4), columns=["a", "b", "c","p"])
st.bar_chart(chart_data)


chart_data = pd.DataFrame(
   {
       "col1": list(range(20)) * 3,
       "col2": np.random.randn(60),
       "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
   }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")