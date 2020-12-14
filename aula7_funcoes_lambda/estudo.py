
def myfunc(x):
    return x['car']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
]

cars.sort(key=myfunc)
print(cars)