import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Weather Data Analysis App")
    st.sidebar.title("Upload your Weather Dataset")
    
    #file uploder
    uploaded_file=st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            data=pd.read_csv(uploaded_file)

            st.sidebar.success("File uploaded successfully")

            st.subheader("Basis Information")
            st.write("Shape osf the dataset",data.shape)
            st.write("Columns in the dataset", list(data.columns))
            st.write("Missing values", data.isnull().sum())

            #Summary Statistics
            st.subheader("Summary Statistics")
            st.write(data.describe())

            #Visualization
            st.subheader("Visualization")

            if 'temperature_celsius' in data.columns:
                st.write("Temperature distribution")
                fig, ax= plt.subplot()
                sns.histplot(data['temperature_celsius'], kde=True,bins=20,color='skyblue',ax=ax)
                ax.set_title("Temperature Distribution ('c)")
                ax.set_xlabel("Temperature('c)")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)

            if 'air_quality_PM2.5' in data.columns:
                st.write("Air Quality (PM2.5) Distribution")
                fig, ax=plt.subplot()
                sns.histplot(data['air_quality_PM2.5'],kde=True,bins=20,color='lightgreen',ax=ax)
                ax.set_title("Air Quality (PM2.5) Distribution")
                ax.set_xlabel("PM2.5 Levels")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
            if 'sunrise' in data.columns and 'sunset' in data.columns:
                #convert sunrise and sunset times to hours 
                data['sunrise_hour']=pd.to_datetime(data['sunrise'],format='%I:%M %p').dt.hour
                data['sunset_hour']=pd.to_datetime(data['sunset'],format='%I:%M %p').dt.hour

                st.write("Sunrise and Sunset Hour Distribution")
                fig,ax=plt.subplot()
                sns.histplot(data['sunrise_hour'],kde=True,bins=12,color='gold',label='Sunrise Hour',ax=ax)
                sns.histplot(data['sunset_hour'],kde=True,bins=12,color='orange',label='Sunset Hour',ax=ax)
                ax.set_title("Sunrise and Sunset Hours Distribution")
                ax.set_xlabel("Hour of the Day")
                ax.set_ylabel("Frequency")
                ax.legend()
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Error loading the file: {e}")
    else:
        st.info("Please upload a dataset to get started")

if __name__=="__main__":
    main()

