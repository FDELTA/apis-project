from argparse import ArgumentParser
import src.functions as fn  
from src.data import *


parser= ArgumentParser(description='Ojos, pelo, sexo y orientacion sexual de los superheroes')
parser.add_argument('-o' '--eyes',dest='eyes',type=str,help='Escribe el color de ojos del superheroe',default='Brown Eyes')
parser.add_argument('-p' '--hair',dest='hair',type=str,help='Escribe el color de pelo del superheroe', default='Brown Hair')
parser.add_argument('-s' '--sex',dest='sex',type=str,help='Escrribe la orientación sexual del superheroe', default='Female Characters')
parser.add_argument('-g' '--gender',dest='gender',type=str,help='Escribe el título de una película', default='Heterosexual')
args=parser.parse_args()
print(args)

csv()

def superhero(eyes,hair,sex,gender):
    df=pd.read_csv('output/marvel_characters.csv')
    df1=df[df['eye']==f'{eyes}']
    df2=df1[df1['hair']==f'{hair}']
    df3=df2[df2['sex']==f'{sex}']
    df4=df3[df3['gsm']==f'{gender}']
    if df4.shape[0] !=0:
        return print(df4[['eye','hair','sex','gsm','alias','appearances']][:3])
    else:
        print('No data about that superhero')

superhero(args.eyes, args.hair, args.sex, args.gender)

alias=input(str('Introduce character: '))
fn.hash_params(alias)

fn.statistical_info('appearances')

#if __name__ == "__main__":
    #main()
