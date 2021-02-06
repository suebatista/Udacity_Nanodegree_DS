### Disaster Response Pipeline 


### Table of Contents

1. [Installation](#installation)
2. [Project Descriptions](#descriptions)
3. [Files Descriptions](#files)
4. [Instructions](#instructions)
5. [License](#license)

## Installation <a name="installation"></a>

All libraries are available in Anaconda distribution of Python. The used libraries are:

- pandas
- re
- sys
- json
- sklearn
- nltk
- sqlalchemy
- pickle
- Flask
- plotly
- sqlite3

The code should run using Python versions 3.*.


## Project Description <a name="description"></a>



The main goal of this project is to build an app that can help emergency workers analyze incoming messages and sort them into specific categories to speed up aid and contribute to more efficient distribution of people and other resources.



## 3. File Descriptions
- \
	- README.md
	- ETL Pipeline Preparation.ipynb
	- ML Pipeline Preparation.ipynb
- \app
	- run.py
	- \templates
	   - go.html
	   - master.html
- \data
	- DisasterResponse.db - output of the ETL pipeline, i.e. SQLite database containing messages and categories data
	- disaster_categories.csv - dataset including all the categories
	- disaster_messages.csv - dataset including all the messages
	- process_data.py - ETL pipeline scripts to read, clean, and save data into a database
- \models
	- classifier.pkl -- output of the machine learning pipeline, i.e. a trained classifier 
	- train_classifier.py - machine learning pipeline scripts to train and export a classifier






## Instructions <a name="instructions"></a>


     1. Run the following commands in the project's root directory to set up your database and model.

         - To run ETL pipeline that cleans data and stores in database
             `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
         - To run ML pipeline that trains classifier and saves
             `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

     2. Run the following command in the app's directory to run your web app.
         `python run.py`

     3. Go to http://0.0.0.0:3001/
     


## Licensing, Authors, and Acknowledgements <a name="license"></a>
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/xscbsx/Udacity_Nanodegree_DS/blob/main/LICENSE) file for details
