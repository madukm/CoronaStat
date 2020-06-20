import pandas as pd
import numpy as np

corona = 'HIST_PAINEL_COVIDBR_15jun2020.xlsx'

def load_xlsx(filename):
    data = pd.read_excel(filename, usecols=['regiao', 'estado', 'municipio', 'data', 'casosAcumulado', 'casosNovos', 'obitosAcumulado', 'obitosNovos', 'Recuperadosnovos', 'emAcompanhamentoNovos']) 
    return data

# Casos por região
def by_region(corona, name_region):
    data = load_xlsx(corona)
    brasil = data.query('regiao == "Brasil"')
    return brasil.tolist()

def region_cases(corona, name_region):
    region = by_region(corona, name_region)
    return region['casosAcumulado'].values.tolist()

def region_deaths(corona, name_region):
    region = by_region(corona, name_region)
    return region['obitosAcumulado']

def region_recovered(corona, name_region):
    region = by_region(corona, name_region)
    return region['Recuperadosnovos']

# Casos por estado
def by_state(corona, name_state):
    data = load_xlsx(corona)
    state = data.query('estado == name_state')
    return state

def state_cases(corona, name_state):
    state = by_region(corona, name_state)
    return state['casosAcumulado']

def state_deaths(corona, name_state):
    state = by_region(corona, name_state)
    return state['obitosAcumulado']

def state_recovered(corona, name_state):
    state = by_region(corona, name_state)
    return state['Recuperadosnovos']

#Casos por cidade
def by_city(corona, name_city):
    data = load_xlsx(corona)
    city = data.query('municipio == name_city')
    return city

def city_cases(corona, name_city):
    city = by_region(corona, name_city)
    return city['casosAcumulado']

def city_deaths(corona, name_city):
    city = by_region(corona, name_city)
    return city['obitosAcumulado']

def city_recovered(corona, name_city):
    city = by_region(corona, name_city)
    return city['Recuperadosnovos']

if __name__ == "__main__":
    print(region_cases(corona, 'Brasil'))
