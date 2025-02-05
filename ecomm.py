import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt


def main():
    st.title("This is my Data Profiling app")
    st.sidebar.title("you can upload your file here")
    
    upload_file = st.sidebar.file_uploader("uploadd your file" ,type=['csv' , 'xlsx'])
    
    if upload_file is not None :
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("file uploaded succefully")

            st.subheader("i am going to show you a data details ")
            st.dataframe(data.head())
            
            st.subheader("lets see some more details in data")
            st.write("shape of the data" , data.shape)
            st.write("the column name inside data is " , data.columns)
            st.write("missing value into column" , data.isnull().sum())
            
            st.subheader("i will show you the bit of stats ")
            st.write(data.describe())

            # Streamlit App
            #st.title("Dynamic Data Visualizations")
            #st.sidebar.title("Upload and Visualize")

            # File uploader
            #uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx"])


            # Dropdowns for column selection
            numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
            categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
            
            option = st.selectbox("Choose a visualization", ["Bar Chart", "Histogram", "Pie Chart", "Scatter Plot", "Box Plot"])
            
            if option == "Bar Chart":
                cat_col = st.selectbox("Select a Categorical Column", categorical_columns)
                num_col = st.selectbox("Select a Numeric Column", numeric_columns)
                st.subheader(f"Average {num_col} by {cat_col}")
                fig, ax = plt.subplots(figsize=(8, 5))
                data.groupby(cat_col)[num_col].mean().plot(kind="bar", ax=ax)
                ax.set_xlabel(cat_col)
                ax.set_ylabel(f"Average {num_col}")
                ax.set_title(f"Average {num_col} by {cat_col}")
                st.pyplot(fig)
            
            elif option == "Histogram":
                num_col = st.selectbox("Select a Numeric Column", numeric_columns)
                st.subheader(f"Distribution of {num_col}")
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.histplot(data[num_col], bins=30, kde=True, ax=ax)
                ax.set_xlabel(num_col)
                ax.set_ylabel("Frequency")
                ax.set_title(f"Distribution of {num_col}")
                st.pyplot(fig)
            
            elif option == "Pie Chart":
                cat_col = st.selectbox("Select a Categorical Column", categorical_columns)
                num_col = st.selectbox("Select a Numeric Column", numeric_columns)
                st.subheader(f"{num_col} Distribution by {cat_col}")
                pie_data = data.groupby(cat_col)[num_col].sum()
                fig, ax = plt.subplots(figsize=(7, 7))
                ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=140)
                ax.set_title(f"{num_col} Distribution by {cat_col}")
                st.pyplot(fig)
            
            elif option == "Scatter Plot":
                x_col = st.selectbox("Select X-axis Numeric Column", numeric_columns)
                y_col = st.selectbox("Select Y-axis Numeric Column", numeric_columns)
                st.subheader(f"Scatter Plot: {x_col} vs {y_col}")
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.scatterplot(x=data[x_col], y=data[y_col], alpha=0.5, ax=ax)
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"Scatter Plot: {x_col} vs {y_col}")
                st.pyplot(fig)
            
            elif option == "Box Plot":
                cat_col = st.selectbox("Select a Categorical Column", categorical_columns)
                num_col = st.selectbox("Select a Numeric Column", numeric_columns)
                st.subheader(f"{num_col} Distribution by {cat_col}")
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.boxplot(x=cat_col, y=num_col, data=data, ax=ax)
                ax.set_xlabel(cat_col)
                ax.set_ylabel(num_col)
                ax.set_title(f"{num_col} Distribution by {cat_col}")
                st.pyplot(fig)

        except Exception as e :
            print(e)

if __name__ == "__main__":
    main()
