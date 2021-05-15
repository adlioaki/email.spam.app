import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer




#DB Managemnet
import sqlite3
conn = sqlite3.connect('database.db')
c =conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password =?',(username,password))
	database = c.fetchall()
	return database

def view_all_user(username,password):
	c.execute('SELECT * FROM userstable')
	database = c.fetchall()
	return database




model=pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))



def main():

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.title("Words Email Spam Classification ")
		st.subheader("Spam email have become problem on the internet today that can affect our industry and individual by sending unwanted emails. There is ton of messages email everyday that have been sent but there is unwanted email that disturbed our inbox. By sending a lot of incoming email and it would be threat to user. User hard to find and classify the that intruder send email to user.  Tracing spam email have been difficult to trace because it may consume a lot of time to delete on by one spam emails.")
		st.subheader("To use this program, you must first sign up and then login.")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("Username")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			#if password =='12345':
			create_usertable()
			result = login_user(username,password)
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Classification" ,"Profile"])
				
				if task == "Classification":
					st.subheader("Classification")
					st.title("Email Spam Detection using Naïve Bayes Classifier")
					st.subheader("Now lets start to classify your text mails")
					msg=st.text_input("Enter your text:")


					if st.button("Predict"):
						data=[msg]
						vect=cv.transform(data).toarray()
						prediction=model.predict(vect)
						result=prediction[0]
					if result==1:
						st.error("This is Spam Mail")

			
					else:
						st.success("This is Not Spam Mail") 


				elif task == "Profiles":
					st.subheader("User Profiles")
					user_results = view_all_user()
					clean_db = pd.dataframe(user_results,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,new_password)
			st.success("You have sucessfully created your account")
			st.info("Go to login Menu to login")
		
main()




