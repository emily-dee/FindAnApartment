# Searching for an apt, all required
def apt_search1(city: str, max_rent: int, min_beds: int, pets_allowed: bool):
    if pets_allowed:
        print(f'Welcome to ES Rentals. Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, within a budget of ${max_rent} per month...')
    else:
        print(f'Welcome to ES Rentals. Looking up listings in {city} for {min_beds} bedroom apartments, within a budget of ${max_rent} per month...')


apt_search1('Ferndale', 1000, 3, True)
apt_search1('Detroit', 2000, 2, False)
print()


# Searching for an apt, pets and beds optional
def apt_search2(city: str, max_rent: int, min_beds: int = 1, pets_allowed: bool = False):
    if pets_allowed:
        print(f'Welcome to ES Rentals. Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, within a budget of ${max_rent} per month...')
    else:
        print(f'Welcome to ES Rentals. Looking up listings in {city} for {min_beds} bedroom apartments, within a budget of ${max_rent} per month...')


apt_search2('New York City', 4000)
apt_search2('San Francisco', 3500, 2)
apt_search2('Seattle', 1500, pets_allowed=True, min_beds=3)


print()
# lambda functions
plus_one_hundred = lambda x: x + 100
square_num = lambda y: y ** 2
concatenate = lambda z: '- ' + z
divide_by_three = lambda a: a / 3

print(plus_one_hundred(4))
print(square_num(12))
print(concatenate('hi'))
print(divide_by_three(12))
