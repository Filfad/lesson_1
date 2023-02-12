from pprint import pprint

weather = {
    "city":"Москва",
    "temperature":20,
    "date":"12.02.2023"
}

pprint(weather["city"])
weather["temperature"]=weather["temperature"]-5
pprint(weather)
pprint(weather.get("country", "Россия"))
pprint(len(weather))