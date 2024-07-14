import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Title of the app
st.title("Data")

# File uploader
uploaded_file = st.file_uploader("CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataframe
    st.write("Data Preview:")
    st.write(data.head())

    # Option to choose the type of chart
    chart_type = st.selectbox(
        "Select Chart Type",
        options=[
            "Line Chart",
            "Bar Chart",
            "Scatter Plot",
            "Histogram",
            "Pie Chart",
            "Box Plot",
            "Heatmap",
            "Pair Plot",
            "Violin Plot",
            "Area Chart",
            "3D Scatter Plot",
            "Bubble Chart",
            "Map",
            "Line Plot with Plotly"
        ]
    )

    # Chart Type Logic
    if chart_type == "Line Chart":
        st.write("Line Chart")
        st.line_chart(data)

    elif chart_type == "Bar Chart":
        st.write("Bar Chart")
        st.bar_chart(data, x="variety", y="yield", color="site", horizontal=True)


    elif chart_type == "Scatter Plot":
        st.write("Select columns for X and Y axes:")
        x_axis = st.selectbox("X-axis", options=data.columns)
        y_axis = st.selectbox("Y-axis", options=data.columns)
        st.write(f"Scatter Plot of {x_axis} vs {y_axis}")
        fig, ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Histogram":
        st.write("Select column for Histogram:")
        column = st.selectbox("Column", options=data.columns)
        st.write(f"Histogram of {column}")
        fig, ax = plt.subplots()
        ax.hist(data[column], bins=30)
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        st.write("Select column for Pie Chart:")
        column = st.selectbox("Column", options=data.columns)
        st.write(f"Pie Chart of {column}")
        fig, ax = plt.subplots()
        data[column].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

    elif chart_type == "Box Plot":
        st.write("Select column for Box Plot:")
        column = st.selectbox("Column", options=data.columns)
        st.write(f"Box Plot of {column}")
        fig, ax = plt.subplots()
        sns.boxplot(data[column], ax=ax)
        st.pyplot(fig)

    elif chart_type == "Heatmap":
        st.write("Select columns for Heatmap:")
        x_axis = st.selectbox("X-axis", options=data.columns, index=0)
        y_axis = st.selectbox("Y-axis", options=data.columns, index=1)
        st.write(f"Heatmap of {x_axis} vs {y_axis}")
        fig, ax = plt.subplots()
        heatmap_data = pd.crosstab(data[x_axis], data[y_axis])
        sns.heatmap(heatmap_data, ax=ax, cmap="viridis")
        st.pyplot(fig)

    elif chart_type == "Pair Plot":
        st.write("Pair Plot of the DataFrame")
        fig = sns.pairplot(data)
        st.pyplot(fig)

    elif chart_type == "Violin Plot":
        st.write("Select column for Violin Plot:")
        column = st.selectbox("Column", options=data.columns)
        st.write(f"Violin Plot of {column}")
        fig, ax = plt.subplots()
        sns.violinplot(data[column], ax=ax)
        st.pyplot(fig)

    elif chart_type == "Area Chart":
        st.write("Area Chart")
        st.area_chart(data)

    elif chart_type == "3D Scatter Plot":
        st.write("Select columns for X, Y, and Z axes:")
        x_axis = st.selectbox("X-axis", options=data.columns)
        y_axis = st.selectbox("Y-axis", options=data.columns)
        z_axis = st.selectbox("Z-axis", options=data.columns)
        st.write(f"3D Scatter Plot of {x_axis}, {y_axis}, and {z_axis}")
        fig = px.scatter_3d(data, x=x_axis, y=y_axis, z=z_axis)
        st.plotly_chart(fig)

    elif chart_type == "Bubble Chart":
        st.write("Select columns for X, Y, and Size:")
        x_axis = st.selectbox("X-axis", options=data.columns)
        y_axis = st.selectbox("Y-axis", options=data.columns)
        size = st.selectbox("Size", options=data.columns)
        st.write(f"Bubble Chart of {x_axis} vs {y_axis}")
        fig = px.scatter(data, x=x_axis, y=y_axis, size=size, hover_name=data.index)
        st.plotly_chart(fig)

    elif chart_type == "Map":
        st.write("Select columns for Latitude and Longitude:")
        lat_col = st.selectbox("Latitude", options=data.columns)
        lon_col = st.selectbox("Longitude", options=data.columns)
        st.write(f"Map with Latitude and Longitude")
        fig = px.scatter_geo(data, lat=lat_col, lon=lon_col)
        st.plotly_chart(fig)

    elif chart_type == "Line Plot with Plotly":
        st.write("Select columns for X and Y axes:")
        x_axis = st.selectbox("X-axis", options=data.columns)
        y_axis = st.selectbox("Y-axis", options=data.columns)
        st.write(f"Line Plot of {x_axis} vs {y_axis} with Plotly")
        fig = px.line(data, x=x_axis, y=y_axis)
        st.plotly_chart(fig)

# Clear the uploaded file
if st.button("Clear File"):
    st.session_state.uploaded_file = None
    st.experimental_rerun()
