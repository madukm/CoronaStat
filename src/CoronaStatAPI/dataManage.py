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
        self.dates.append(self.data.index.min().strftime("%Y/%m/%d"))
        self.dates.append(self.data.index.max().strftime("%Y/%m/%d"))
        for i in self.data['estado']:
            if i not in self.state_names:
                self.state_names.append(i)

    def get_start_end_date(self):
        return self.dates
    """
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
    """
    #Por estado
    def by_state(self, name_state, start_date, end_date):
        state = self.data.query('estado == @name_state')
        state = state.loc[start_date:end_date]
        state = state.loc[state['municipio'].isnull()]
        state = state.loc[state['codmun'].isnull()]
        return state

    def state_cases(self, name_state, start_date, end_date):
        return self.by_state(name_state, start_date, end_date)['casosAcumulado']

    def state_deaths(self, name_state, start_date, end_date):
        return self.by_state(name_state, start_date, end_date)['obitosAcumulado']

    def state_recovered(self, name_state, start_date, end_date):
        return self.by_state(name_state, start_date, end_date)['Recuperadosnovos']

    #Casos por cidade
    def by_city(self, name_state, name_city, start_date, end_date):
        city = self.data.query('estado == @name_state')
        city = city.query('municipio == @name_city')
        city = city.loc[start_date:end_date]
        return city

    def city_cases(self, name_state, name_city, start_date, end_date):
        return self.by_city(name_state, name_city, start_date, end_date)['casosAcumulado']

    def city_deaths(self, name_state, name_city, start_date, end_date):
        return self.by_city(name_state, name_city, start_date, end_date)['obitosAcumulado']

    def city_recovered(self, name_state, name_city, start_date, end_date):
        return self.by_city(name_state, name_city, start_date, end_date)['Recuperadosnovos']

    #Regarding names
    def get_name_cities(self, name_state):
        return self.data.query('estado == @name_state')['municipio'].dropna().unique()

    def get_name_states(self):
        return self.data['estado'].dropna().unique()
