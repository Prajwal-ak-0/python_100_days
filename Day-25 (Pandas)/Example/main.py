# # import csv
# #
# # temperature = []
# #
# # with open("002 weather-data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append((int(row[1])))
# #     print(temperature)
#
#
# import pandas
#
# data = pandas.read_csv("002 weather-data.csv")
#
# data_to_dict = data.to_dict()
#
# temp_list_1 = data["temp"]
# temp_list_2 = data.temp
#
# print(data.temp.mean())
# print(data.temp.max())
#
# # GET COLUMN AS A DATA
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # CREATING DATA FROM SCRATCH AND FILE
#
# data_dict = {
#     "students": ["John", "Alisa", "Phelex"],
#     "scores": [76, 54, 67]
# }
#
#
# info = pandas.DataFrame(data_dict)
# info.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231116.csv")

sq = data["Primary Fur Color"]
sq = sq.tolist()

Gray = []
Black = []
Red = []

for col in sq:
    if col == "Gray":
        Gray.append(col)

    if col == "Black":
        Black.append(col)

    if col == "Cinnamon":
        Red.append(col)

dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(Gray), len(Red), len(Black)]
}

info = pandas.DataFrame(dict)
info.to_csv("sq_data.csv")
