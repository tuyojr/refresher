travel_log = [
    {
        "country": "Spain",
        "visits": 12,
        "cities": ["Barcelona", "Madrid", "Valencia"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Munich", "Dusseldorf", "Koln"]
    },
]

def add_new_country(country, number_of_visits, cities_visited):
    new_country = {}
    values = [country, number_of_visits, cities_visited]
    
    for item in travel_log:
        index = 0
        for key in item:
            new_country[key] = values[index]
            index += 1
    
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "St Petersburg"])
print(travel_log)