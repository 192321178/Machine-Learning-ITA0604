import csv

# The data are written to a CSV file so the program is self-contained.
rows = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change', 'Yes'],
]
header = ['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast', 'EnjoySport']
with open('enjoysport.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

with open('enjoysport.csv', newline='') as file:
    data = list(csv.reader(file))[1:]  # Skip the header row.

hypothesis = ['0'] * (len(data[0]) - 1)
for row in data:
    if row[-1].strip().lower() == 'yes':
        for i, value in enumerate(row[:-1]):
            if hypothesis[i] == '0':
                hypothesis[i] = value
            elif hypothesis[i] != value:
                hypothesis[i] = '?'

print('Most specific hypothesis:', hypothesis)
