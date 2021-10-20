"""
*counter
*defaultdict
*ordereddict
*namedtuple
*deque
"""


from collections import Counter, defaultdict
device_temperature = [13.5, 14.5, 14.0, 16.0, 21.0, 12.2, 223.9]

temperature_counter = Counter(device_temperature)
print(temperature_counter [14.5])



coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters [coworker].append(place)

print(alma_maters['Rolf'])
print(alma_maters['Dam'])