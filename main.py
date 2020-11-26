import csv

files = ['data/2015.csv', 'data/2016.csv', 'data/2017.csv', 'data/2018.csv', 'data/2019.csv']

def get_country_row_from_file(file, country):
  with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        found = False
        for line in csv_reader:
          if country == line[1]:
              return line
              found = True
        if not found:
          print("Country Not found")
          
def print_yearly_data(year, rank, score):
  print("Year: " + str(year))
  print("Rank: " + rank)
  print("Score: " + score+ "\n")
country = input("What country are you looking for? ")

country_data = []
for file in files:
    country_data.append(get_country_row_from_file(file, country))

#print(country_data)
for i in range(len(country_data)):
    print_yearly_data(i + 2015, country_data[i][0], country_data[i][2])
