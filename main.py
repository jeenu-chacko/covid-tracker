import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt
import requests


def main():
	st.title("Covid-19 Dashboard For India")
	st.markdown('The dashboard will visualize the Covid-19 Situation in India')
	st.sidebar.title("Select State")

	url = "https://api.rootnet.in/covid19-in/stats/daily"
	r = requests.get(url)
	r=r.json()
	deaths=[]
	day=[]
	df0=json_normalize(r['data'] ,record_path=['regional'],meta=['day'])
	df0=df0[["day","confirmedCasesIndian","confirmedCasesForeign","discharged","deaths","totalConfirmed"]]
	df1=df0[["deaths"]]
	st.write(df0.tail(120))
	for index, row in df0.iterrows():
		np.append(deaths,row['deaths'])
		np.append(day,row['day'])
	st.write(type(np.array(deaths[1:10]).ravel()))
	df = pd.DataFrame({"Year" : day, 
        "Salary_Hike" :deaths})
	plt.figure(figsize=(8,8))
	st.write(df.tail())
	plt.plot(df["Year"], df["Salary_Hike"])
	

	
	st.line_chart(df0)
	st.line_chart(df1.iloc[1:])
	



if __name__ == '__main__':
	main()

