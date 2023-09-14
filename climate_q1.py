import sqlite3

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData ORDER BY Year ASC")
data = cursor.fetchall()

connection.close()

years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

# Display the data in a simple table format
print(f"{'Year':<6}{'CO2':<6}{'Temperature':<6}")
print("--------------------")

for y, c, t in zip(years, co2, temp):
    print(f"{y:<5} {c:<5} {t:<5}")