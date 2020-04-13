import pandas

print("Hello again")

data = pandas.read_csv('pdl1.csv')

data.info()

print("age mean:", data["Age"].mean())