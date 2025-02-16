person = {'John': 30,'Alice': 25,'Bob': 40,'Eve': 22}
filtered_dict = {key: value for key, value in person.items() if value >= 30}
print(filtered_dict)