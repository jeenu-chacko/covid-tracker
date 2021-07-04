import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt
import requests
import datetime,time

st.set_page_config(page_title='Covid19-DashBoard', page_icon=":syringe:", layout='centered', initial_sidebar_state='auto')
def main():
	hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
		footer {
	
	visibility: hidden;
	
	}
	footer:after {
		content:"Made with ❤️ by Jeenu Chacko"; 
		visibility: visible;
		display: block;
		position: relative;
		
		padding: 5px;
		top: 2px;
		color:black;
	}
        </style>
        """
	st.markdown(hide_menu_style, unsafe_allow_html=True)
	st.sidebar.title("")
	Host_Country =st.sidebar.selectbox('Select a State ', ('State Wise Latest Reports','Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra',  'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',  'Odisha', 'Puducherry', 'Punjab',  'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'))


	st.sidebar.title("")
	st.sidebar.title("")

	st.sidebar.title("")
	st.sidebar.title("")

	#st.sidebar.write("made with :heart: by Jeenu Chacko")

	today = time.strftime("%Y-%m-%d")
	urlv="https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date="+today
	rv=requests.get(urlv)
	rv=rv.json()
	
	
	

		
	url = "https://api.rootnet.in/covid19-in/stats/daily"
	r = requests.get(url)
	r=r.json()
	
	df1=json_normalize(r['data'] ,record_path=['regional'],meta=['day'])
	if Host_Country=='State Wise Latest Reports':	
		st.title("Covid-19 🦠 Dashboard")
		df1=df1[["loc","totalConfirmed","discharged","deaths","confirmedCasesIndian"]]
		df2=df1[["deaths"]]

		st.subheader("State Wise Latest Report📝")
		st.write(df1.set_index("loc").tail(35))
		st.write(" ")
		st.write(" ")			
		st.subheader("Vaccination 💉 Latest Report📝")
		dfv0=json_normalize(rv['getBeneficiariesGroupBy'])
		dfv0=dfv0[['title','total','partial_vaccinated','totally_vaccinated']]
		st.write(dfv0.set_index("title"))

	
	if Host_Country!='State Wise Latest Reports':
		st.title("Covid-19 🦠 Dashboard")

		stateDeaths = []
		stateDay = []
		stateTotalConfirmed = []
		stateTotalDischarged = []
	
		dfv0=json_normalize(rv['getBeneficiariesGroupBy'])
		
		for index, row in dfv0.iterrows():						
			if row['state_name']==Host_Country:
				tvaccinated=row['total']
				pvaccinated =row['partial_vaccinated']		
				fvaccinated = row['totally_vaccinated']
		
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
		
	
		st.write(" ")
		st.write(" ")
		st.write("Total Confirmed: "+str(stateTotalConfirmed[-1]))
		st.write("Total Deaths: "+str(stateDeath[-1]))
		st.write("Total Discharged: "+str(stateTotalDischarged[-1]))
		st.write("Total Vaccinated: "+ str(tvaccinated))
		st.write("Partially Vaccinated: "+ str(pvaccinated))
		st.write("Fully Vaccinated: "+ str(fvaccinated))

		st.write(" ")
		st.subheader("Total Confirmed and Total Discharged📈")
		st.write(" ")
		st.write(" ")
		
		st.line_chart(dfs.rename(columns={'Date':'index'}).set_index('index'),use_container_width=False)
		st.subheader("Total Deaths📈")
		st.write(" ")
		st.write(" ")
		st.line_chart(dfd.rename(columns={'Date':'index'}).set_index('index'),use_container_width=False)
			



	

	



if __name__ == '__main__':
	main()

