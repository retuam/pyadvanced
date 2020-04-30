# Task 1
num_list = list(range(100))
print([i for i in num_list if i and not i % 2])

# Task 2
countries = {
    'Albania': 'Tirane',
    'Algeria': 'Algiers',
    'Argentina': 'Buenos Aires',
    'Belarus': 'Minsk',
    'Bolivia': 'La Paz',
    'Cameroon': 'Yaounde',
    'Canada': 'Ottawa',
    'China': 'Beijing',
    'Croatia': 'Zagreb',
    'Cuba': 'Havana',
    'Ethiopia': 'Addis Ababa',
    'France': 'Paris',
    'Georgia': 'Tbilisi',
    'Ghana': 'Accra',
    'Hungary': 'Budapest',
    'Iceland': 'Reykjavik',
    'Italy': 'Rome',
    'Kuwait': 'Kuwait',
    'Latvia': 'Riga',
    'Lithuania': 'Vilnius',
    'Mexico': 'Mexico',
    'Morocco': 'Rabat',
    'Norway': 'Oslo',
    'Panama': 'Panama',
    'Somalia': 'Mogadishu',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Thailand': 'Bangkok',
    'Togo': 'Lome',
    'Ukraine': 'Kiev',
    'United States': 'Washington',
    'Uruguay': 'Montevideo',
    'Venezuela': 'Caracas',
    'Zambia': 'Lusaka',
}

countries_list = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Angola',
    'Argentina',
    'China',
    'Cuba',
    'Cyprus',
    'Ethiopia',
    'Germany',
    'Greece',
    'Hungary',
    'Iceland',
    'Israel',
    'Japan',
    'Kenya',
    'Kuwait',
    'Latvia',
    'Mexico',
    'Morocco',
    'Netherlands',
    'Panama',
    'Samoa',
    'Sierra Leone',
    'Slovakia',
    'Somalia',
    'South Korea',
    'Swaziland',
    'Sweden',
    'Thailand',
    'Togo',
    'Ukraine',
    'United States',
    'Uruguay'
]

# print(*[countries[i] for i in countries_list if i in countries.keys()])
for i in countries_list:
    if i in countries.keys():
        print(countries[i])

# Task 3
_list = list(range(100))
for i in _list:
    if not i:
        print(i)
    elif not i % 15:
        print('FizzBuzz')
    elif not i % 3:
        print('Fizz')
    elif not i % 5:
        print('Buzz')
    else:
        print(i)

# Task 4
def bank(sum, year, percent):
    year, percent, sum = int(year), float(percent), float(sum)

    for _ in range(year * 12):
        sum += sum * (percent / 1200)

    return sum

print(f'Total amount is {bank(1000, 10, 10)}')