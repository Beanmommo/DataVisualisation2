import json

continent = ['Africa', 'Asia', 'Europe', 'South America', 'North America', 'Oceania']

with open("ne_110m_admin_0_countries.json", encoding="utf8") as data_file:
    data = json.load(data_file)
    for selected_continent in continent:
        file = open((selected_continent + ".txt"), "a")
        for geometry in data['objects']['ne_110m_admin_0_countries']['geometries']:
            geoContinent = geometry['properties']['CONTINENT']
            if geoContinent == selected_continent:
                countryName = geometry['properties']['NAME_EN']
                file.writelines(countryName+"\n")
            print("update "+selected_continent)
        file.close()