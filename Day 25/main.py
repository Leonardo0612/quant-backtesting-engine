# with open("Day 25/weather_data.csv") as data:
#     print(data.readlines())

# import csv

# with open("Day 25/weather_data.csv") as data:
#     next(data)
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("Day 25/weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# temp_in_f = monday.temp[0] * (9 / 5) + 32
# print(temp_in_f)

# data_dict = {
#     "students": ["Leon", "Emi", "Amy"],
#     "scores": [67, 76, 67]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("Day 25/new_data.csv")

data = pandas.read_csv("Day 25/Squirrel_Census.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(cinnamon_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Colour": ["Grey", "Cinnamon", "Red"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day 25/squirrel_count.csv")