import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
    Load two datasets called categories and messages. 
    Args: 
        messages_filepath - Filepath to the CSV file containing messages 
        categories_filepath - Filepath to the CSV file containing  categories 
        
    Returns:
        df- Dataframe with the combination of messages and categories files.
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on='id')
    return df

def clean_dataset(df):
    '''
     Transform the original dataset into a clean dataframe 
     Args:
        df: Dataframe to be cleaned by the method
        
    Return:
        df: Cleaned dataframe
    '''
     # Split the categories
    categories = df['categories'].str.split(pat=';',expand=True)
    
    #Fix the categories columns name
    row = categories.iloc[[1]]
    category_colnames = [category_name.split('-')[0] for category_name in row.values[0]]
    categories.columns = category_colnames
    
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(np.int)
    
    df = df.drop('categories',axis=1)
    df = pd.concat([df,categories],axis=1)
    df = df.drop_duplicates()
    
    return df
    
def save_data(df, database_filename):
    '''
     Save dataframe to SQLite Database
    Args: 
        df: Dataframe
        database_filepath - Filepath used for saving the database     
    Returns:
        dataframe.db
    '''
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('DisasterResponse', engine, index=False,if_exists='replace')

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df= load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_dataset(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()