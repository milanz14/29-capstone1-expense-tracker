# Budget Tracker App (Budgee)

* API:
  * The api that will be used for this project is an API that I will build myself. It will be seeded with data initially for the test user. As this is a personal expense tracker, the goal is for users to submit their data to the back end API, which will be queried by the user whenever they log into the system and search for transactions or categories

* Schema Design:
  * There will be 5 models part of the schema - the User model, the Transaction model, the Category mode, the UserCategory model and the UserTransaction model. 
  * These are mainly M2M relationships


# Run this App

* You can run the app via the link below
  * `coming soon`

* You can also run this on your machine by typing the following into your terminal
* Please ensure that you have POSTGRES installed 
  1. `python3 -m venv venv`
  2. `source venv/bin/activate`
  3. `pip install -r requirements.txt`
  4. `createdb budgetapp`
  5. `python3 seed.py`
  6. `flask run`

