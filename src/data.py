import src.functions as fn
import pandas as pd
import numpy as np

def csv():
    allcharacters = pd.read_csv('input/marvelcharactersdata.csv')
    allcharacters.columns = fn.clean_header(allcharacters.columns)
    #limpiamos con Unknowns
    fn.fill_value(allcharacters['eye'], 'Unkown')
    fn.fill_value(allcharacters['hair'], 'Unkown')
    fn.fill_value(allcharacters['sex'], 'Unkown')
    fn.fill_value(allcharacters['align'], 'Unkown')
    #limpiamos la columna gsm con Heterosexual
    fn.fill_value(allcharacters['gsm'], 'Heterosexual')
    allcharacters['name1'] = allcharacters['name'].str.split('(')
    allcharacters['alias']= [x[0] for x in allcharacters['name1']]
    allcharacters.to_csv('output/marvel_characters.csv', index=False)

csv()
