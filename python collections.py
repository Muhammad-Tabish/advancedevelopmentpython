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


#defaultdict
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters [coworker].append(place)

#alma_maters.default_factory = None

print(alma_maters['Rolf'])
print(alma_maters['Dam'])
print(alma_maters['Fam'])



my_company = 'tabish'

coworkers = ['jen', 'sam', 'fam', 'ham']
other_coworkers = [('Rolf', 'Apple'), ('Tam', 'google')]
coworker_compaines = defaultdict(lambda : my_company)

for person, company in other_coworkers:
    coworker_compaines [person] = company
print(coworker_compaines [coworker[0]])
print(coworker_compaines['Rolf'])


#orderdict


from collections import OrderedDict

o = OrderedDict()

o['Rolf'] = 2
o['Jen'] = 12
o['Sam'] = 4

print(o)

o.move_to_end('Rolf')
print(o)

o.popitem('Rolf')
print(o)

o.move_to_end('Sam', last = False)
print(o)



#namedtuple

from collections import namedtuple

accounts = ('checking', 1875)
Accounts = namedtuple('Account', ['name', 'balance'])
accounts = Accounts ('checking', 1875)
print(accounts.name)
print(accounts)

accounts = ('checking', 1875)
Accounts = namedtuple('Account', ['name', 'balance'])
accountnamedtuple = Accounts(*accounts)
print(accountnamedtuple._asdict()['balance'])


#deque


from collections import deque

friends = deque(('Sam', 'Ham', 'Fam'))
friends.append('jose')
friends.appendleft('Tam')
print(friends)

friends.pop()
friends.popleft()
print(friends)