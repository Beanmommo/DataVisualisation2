import csv

resultFileName = 'result.csv'

countryInContinent = {
    "Africa": 51,
    "Asia": 47,
    "Europe": 39,
    "South America": 13,
    "North America": 18,
    "Oceania": 7    
}
#Open csv file
with open('other_continent_country.csv', mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    #Continent, Country, Type, Year, Value
    with open(resultFileName, 'w', newline="") as resultFile:
        csvwriter = csv.writer(resultFile)
        csvwriter.writerow(header)
        for row in csvreader:
            continent = row[0]
            type = row[2]
            year = row[3]
            value = row[4]
            with open(continent+'.txt') as continentFile:
                value = round(int(float(value)) / countryInContinent[continent], 1)
                for country in continentFile:
                    country = country.replace('\n', '')
                    csvline = []
                    csvline.append(continent)
                    csvline.append(country)
                    csvline.append(type)
                    csvline.append(year)
                    csvline.append(value)
                    csvwriter.writerow(csvline)
            continentFile.close()

    resultFile.close()
file.close()