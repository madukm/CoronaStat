import pandas as pd
import numpy as np

class dataManage:

    covid = 'teste.xlsx'

    def __init__(self):
        self.data = pd.read_excel(dataManage.covid, usecols=['regiao', 'estado', 'municipio', 'data', 'casosAcumulado', 'casosNovos', 'obitosAcumulado', 'obitosNovos'])

    def by_region(self, name_region):
        brasil = self.data.query('regiao == @name_region')
        return brasil

    def region_cases(self, name_region):
        region = self.by_region(name_region)
        return region['casosAcumulado']

    def region_deaths(self, name_region):
        region = self.by_region(name_region)
        return region['obitosAcumulado']

    def region_recovered(self, name_region):
        region = self.by_region(name_region)
        return region['Recuperadosnovos']

    # Casos por estado
    def by_state(self, corona, name_state):
        state = self.data.query('estado == @name_state')
        return state

    def state_cases(self, name_state):
        state = self.by_state(name_state)
        return state['casosAcumulado']

    def state_deaths(self, name_state):
        state = self.by_state(name_state)
        return state['obitosAcumulado']

    def state_recovered(self, name_state):
        state = self.by_state(name_state)
        return state['Recuperadosnovos']

    #Casos por cidade
    def by_city(self, name_city):
        city = self.data.query('municipio == @name_city')
        return city

    def city_cases(self, corona, name_city):
        city = self.by_city(name_city)
        return city['casosAcumulado']

    def city_deaths(self, name_city):
        city = self.by_city(name_city)
        return city['obitosAcumulado']

    def city_recovered(self, name_city):
        city = self.by_region(name_city)
        return city['Recuperadosnovos']

# TESTING 
def main():
    data1 = dataManage()
    print("ola")
    brazil = data1.region_cases('Brasil')
#data1.open_xlsx()
    print(brazil)

if(__name__ == "__main__"):
    main()

