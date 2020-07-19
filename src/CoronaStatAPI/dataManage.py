import pandas as pd
import numpy as np

class dataManage:

    covid = 'teste.xlsx'

    def __init__(self):
        pass

    def read_data(self):
        self.data = pd.read_excel(dataManage.covid,
                                  usecols=['regiao', 'estado', 'municipio', 'data', 'casosAcumulado', 'casosNovos',
                                           'obitosAcumulado', 'obitosNovos', 'codmun'])
        self.data = self.data.set_index(['data'])
        self.state_names = []
        self.dates = []
        self.dates.append(self.data.index.min())
        self.dates.append(self.data.index.max())
        for i in self.data['estado']:
            if i not in self.state_names:
                self.state_names.append(i)

    def get_start_end_date(self):
        return self.dates

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
    def by_state(self, name_state):
        state = self.data.query('estado == @name_state')
        return state

    def get_name_city(self, name_state):
        state = self.data.query('estado == @name_state')
        city_names = []
        for i in state['municipio']:
            if i not in city_names and i.isNotNull():
                city_names.append(i)
        return city_names

    """
    MODIFIED HERE SO WE DONT NEED AUXILIARY CLASSES
    """
    def state_cases(self, name_state, start_date, end_date):
        state = self.data.query('estado == @name_state')
        state = state.loc[start_date:end_date]
        state = state.loc[state['municipio'].isnull()]
        state = state.loc[state['codmun'].isnull()]
        #state = self.by_state(name_state)
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

    def city_cases(self, name_city):
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
    data1.read_data()
    print(data1.get_start_end_date())
    #brazil = data1.region_cases('Brasil')
#data1.open_xlsx()

if(__name__ == "__main__"):
    main()

