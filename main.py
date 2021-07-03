import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt
import requests


def main():
	   
	
	
	st.sidebar.title("Filter")
	st.sidebar.title("")
	Host_Country =st.sidebar.selectbox('Select a State ', ('State Wise Latest Reports','Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadar Nagar Haveli', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra',  'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',  'Odisha', 'Puducherry', 'Punjab',  'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'))

	



	df0=pd.DataFrame({})
	url = "https://api.rootnet.in/covid19-in/stats/daily"
	r = requests.get(url)
	r=r.json()
	
	df1=json_normalize(r['data'] ,record_path=['regional'],meta=['day'])
	if Host_Country=='State Wise Latest Reports':	
		st.title("Covid-19 Dashboard")
		df1=df1[["loc","totalConfirmed","discharged","deaths","confirmedCasesIndian"]]
		df2=df1[["deaths"]]

		st.subheader("State Wise Latest Reports")
		st.write(df1.set_index("loc").tail(35))
	
	
	if Host_Country!='State Wise Latest Reports':
		st.title("Covid-19 Dashboard")
		stateDeaths = []
		stateDay = []
		stateTotalConfirmed = []
		stateTotalDischarged = []
		st.write("Thank you Lord")
		for index, row in df1.iterrows():
			
			if row['loc'] == Host_Country:
				stateDeaths.append(row['deaths'])
				stateDay.append(row['day'])
				stateTotalConfirmed.append(row['totalConfirmed'])
				stateTotalDischarged.append(row['discharged'])	
		stateDeath=np.array(stateDeaths).ravel()
		stateDay=np.array(stateDay).ravel()
		stateTotalConfirmed = np.array(stateTotalConfirmed).ravel()
		stateTotalDischarged = np.array(stateTotalDischarged).ravel()
		dfs = pd.DataFrame({"Total Discharged" : stateTotalDischarged[-30:], 
		"Date" :stateDay[-30:] ,'Total Confirmed':stateTotalConfirmed[-30:]})
		dfd=pd.DataFrame({"Death":stateDeath[-30:],"Date" :stateDay[-30:]})
		
		st.write("State: "+Host_Country)
		st.write("Total Confirmed: "+str(stateTotalConfirmed[-1]))
		st.write("Total Deaths: "+str(stateDeath[-1]))
		st.write("Total Discharged: "+str(stateTotalDischarged[-1]))
		st.write(" ")
		st.write(" ")
		st.line_chart(dfs.rename(columns={'Date':'index'}).set_index('index'),width = 0,height=350)
		st.line_chart(dfd.rename(columns={'Date':'index'}).set_index('index'),width = 0,height=350)
	
		

	

	



if __name__ == '__main__':
	main()

