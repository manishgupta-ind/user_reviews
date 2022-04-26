**Analysis of user reviews on play store**

**Problem statement -** There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. Your goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. 

**Deploy it using -** Flask/Streamlit etc and share the live link. 

**Important** In this data app - the user will upload a csv and you would be required to display the reviews where the content doesn’t match ratings.  This csv will be in the same format as the DataSet Link

**Bonus Points -** If you deploy the app with Authentication. 


**SOLUTION:** For this project, I used Happy Transformer module since we do not have training data to create and train model from scratch. Also Happy Transformer is a package built on top of Hugging Face’s transformer library that makes it easy to utilize state-of-the-art NLP models.

* I deployed model using streamlit which is exremely simple and fast to deploy. I implemented simple authentication process to use API on this page as per instructions.
* I saved model as pickle file for deployment in static directory. 
* main.py contains main code for project for interaction with user. It accepts csv file from user, convert it into dataframe and pass it to predictor function in helper.py
* helper.py uses saved model in static directory to make prediction and return the result back to main.py
* main.py converts returned dataframe from helper.py into a csv file and makes it available to be downloaded by user. 


**Link of deployed App:** https://share.streamlit.io/manishgupta-ind/user_reviews/main/main.py

**Credential to use APP:**
  - username: guest
  - password: guest123
