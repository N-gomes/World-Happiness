import csv

files = ["2015.csv","2016.csv","2017.csv","2018.csv","2019.csv",]

def get_country_row_from_file(country, file):
    with open(files, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        in_file = False
        for line in country:
            if line==file[1]:
                return line
                in_file = True
        if not in_file:
            print("File not found")

def print_yearly_data(year, country, rank):
    print("Year: " + year)
    print("Country: " + country)
    print("Rank: " + rank)

country = input("What country are you looking for: ")
country_data = []

for file in files:
    country_data.append(get_country_row_from_file(file, country)

for i in range(len(country_data)):
    print_yearly_data(i + 2015, country_data[i][0], country_data[i][2])