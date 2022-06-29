# read from csv files
import pandas
import os

data1 = pandas.read_csv("data/daily_sales_data_0.csv", sep=",")
data2 = pandas.read_csv("data/daily_sales_data_1.csv", sep=",")
data3 = pandas.read_csv("data/daily_sales_data_2.csv", sep=",")


# check if the product is pink morsels
def get_result(data):
    result = []
    for index, row in data.iterrows():
        if row["product"] == "pink morsel":
            price = row["price"]
            price = price.replace("$", "")
            price = float(price)
            temp = [price * row["quantity"], row["date"], row["region"]]
            result.append(temp)
    return result


def write_to_file(data):
    output = open("data/daily_sales_data_output.csv", "w")
    output.write("sales,date,region\n")
    for row in data:
        output.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "\n")
    output.close()


result1 = get_result(data1)
result2 = get_result(data2)
result3 = get_result(data3)

final = result1 + result2 + result3
write_to_file(final)
