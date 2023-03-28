import streamlit as st
import pandas as pd

def main():
	st.title("Forms & Calculators")
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)



	if choice == "Home":
		st.subheader("Forms")


	# Salary Calculator
	with st.form(key="salaryform", clear_on_submit=True):
		col1,col2,col3 = st.columns([3,2,1])

		with col1:
			amount = st.number_input("Hourly Rate in $")
		
		with col2:
			hpw = st.number_input("Hours per Week",8,60)

		with col3:
			st.text("Salary")
			submit_salary = st.form_submit_button(label="Calculate")

	if submit_salary:
		with st.expander("Results"):
			daily = [amount * 8]
			weekly = [amount * hpw]
			df = pd.DataFrame({"hourly" : amount,
							   "daily" : daily,
							   "weekly" : weekly})
			st.dataframe(df.T)
	

	# Method 1
	with st.form(key = "form1"):
		firstname = st.text_input("First Name")
		lastname = st.text_input("Last Name")
		dob = st.date_input(" Birth Date")

		submit_button = st.form_submit_button(label="Sign up")
	
	# Results
	if submit_button:
		st.success("Hello {} {} you have created an accound".format(firstname,lastname))




	# Method 2:
	form2 = st.form(key="form2")
	username = form2.text_input("Username")
	job = form2.selectbox("Job",["Dev","DS","ML","DR"])
	submit_button_2 = form2.form_submit_button("Login")

	template = (f"Welcome {username}")
	st.write(template)







if __name__ == "__main__":
	main()