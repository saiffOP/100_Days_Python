# import csv
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

# import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(data)
#
# Gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
# Cinnamon_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# Black_fur_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [Gray_fur_count, Cinnamon_fur_count, Black_fur_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("Squirrel_Count.csv")

import pandas as pd

data = pd.read_csv("weather_data.csv")
monday = data[data.day == "Monday"]
mon_temp = monday.temp
farhenheit_temp = mon_temp * 9 / 5 + 32
print(farhenheit_temp)
