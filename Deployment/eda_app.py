import pandas as pd
from PIL import Image
import streamlit as st

def run_eda_app():
	st.subheader("Real Estate : Data Analysis")

	submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
	df = pd.read_csv("Final_Project.csv")

	if submenu == "Descriptive":
		img1 = Image.open("IMG\Real_Estate.jpg")
		st.image(img1)
		
		with st.expander("Dataset"):
			st.dataframe(df)

		with st.expander("Data Types"):
			st.dataframe(df.dtypes)

		with st.expander("Data Summary"):
			st.dataframe(df.describe())

		with st.expander("Location Distribution"):
			st.dataframe(df["Region"].value_counts().head(30))

	elif submenu == "Plots":

		with st.expander("Price Range Distribution"):
			img2 = Image.open("IMG\Price_Range_Distribution.png")
			st.image(img2)

		with st.expander("Price with respect to Floor"):
			img3 = Image.open("IMG\Property_Floor_Numbers_Bar.png")
			st.image(img3)
		
		with st.expander("Price with respect to Bedroom and Bathroom"):
			img4 = Image.open("IMG\BednBath_Price_Bar.png")
			st.image(img4)

		with st.expander("Price with respect to Property Age"):
			img5 = Image.open("IMG\Price_Age_Distribution.png")
			st.image(img5)

		with st.expander("Price with respect to SqFt Area"):
			img6 = Image.open("IMG\SqFt_Area_Price_Scatter.png")
			st.image(img6)

		with st.expander("Central Mumbai Property Price"):
			img7 = Image.open("IMG\Central Mumbai.png")
			st.image(img7)

		with st.expander("South Mumbai Property Price"):
			img8 = Image.open("IMG\South Mumbai.png")
			st.image(img8)

		with st.expander("Thane Property Price"):
			img9 = Image.open("IMG\Thane.png")
			st.image(img9)