import pandas as pd

ALL_DATA = pd.read_excel('data.xlsx', index_col=0, header=1)

CHAMPION_LIST = ALL_DATA.get('Attack').keys()

DATA_PARAMS = ALL_DATA.keys()


# print(ALL_DATA.keys())
# print(ALL_DATA.get('Burst')['Amumu'])
# print(ALL_DATA.get('Burst').keys()[1])