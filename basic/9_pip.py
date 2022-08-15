import pandas
house = pandas.read_csv('house.csv')
print(house.head(2))
print(house.describe())