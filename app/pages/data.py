import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    uploaded_file = st.file_uploader("CSV file", type="csv")
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return None

def data_summary(df):
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Column Info")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes,
        'Non-Null Count': df.count(),
        'Null Count': df.isnull().sum()
    })
    st.write(col_info)

def data_manipulation(df):
    st.subheader("Data Manipulation")
    
    # Column selection
    selected_columns = st.multiselect("Select columns to keep", df.columns)
    if selected_columns:
        df = df[selected_columns]
    
    # Sorting
    sort_column = st.selectbox("Sort by column", ["None"] + list(df.columns))
    if sort_column != "None":
        sort_order = st.radio("Sort order", ["Ascending", "Descending"])
        df = df.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))
    
    # Filtering
    filter_column = st.selectbox("Filter by column", ["None"] + list(df.columns))
    if filter_column != "None":
        if df[filter_column].dtype == "object":
            filter_value = st.selectbox(f"Select {filter_column} value", ["All"] + list(df[filter_column].unique()))
            if filter_value != "All":
                df = df[df[filter_column] == filter_value]
        else:
            min_value, max_value = st.slider(f"Select range for {filter_column}",
                                             float(df[filter_column].min()),
                                             float(df[filter_column].max()),
                                             (float(df[filter_column].min()), float(df[filter_column].max())))
            df = df[(df[filter_column] >= min_value) & (df[filter_column] <= max_value)]
    
    return df

def create_chart(df, chart_type, x_axis, y_axis):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if chart_type == "Line Chart":
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Bar Chart":
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Scatter Plot":
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif chart_type == "Box Plot":
        sns.boxplot(data=df, x=x_axis, y=y_axis, ax=ax)
    
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(f"{chart_type}: {y_axis} vs {x_axis}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def main():
    st.title("DATA")

    df = load_data()

    if df is not None:
        st.subheader("Data Preview")
        st.write(df.head())

        data_summary(df)
        
        df = data_manipulation(df)

        st.subheader("Filtered Data Preview")
        st.write(df.head())

        st.subheader("Create Chart")
        chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Box Plot"])
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)

        fig = create_chart(df, chart_type, x_axis, y_axis)
        st.pyplot(fig)

if __name__ == "__main__":
    main()