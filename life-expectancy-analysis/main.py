import csv

countries = ['China', 'Georgia', 'Netherlands']
data = {country: [] for country in countries}

with open("life-expectancy.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if row[0] in ['China', 'Georgia', 'Netherlands']:
            data[row[0]].append((int(row[2]), float(row[3])))
for country in countries: 
    records = sorted(data[country])

    if records:
        first_year, first_value = records[0]
        last_year, last_value = records[-1]

        change = last_value - first_value

        print(country)
        print("First year:", first_year)
        print("Last year:", last_year)
        print("Change in life expectancy:", round(change, 2), "years")
        print()

print("Comparison in the latest available year:")
for country in countries:
    records = sorted(data[country])
 
    if records:

        year, value = records[-1]
        print(country, "-", round(value, 2), "years in", year)