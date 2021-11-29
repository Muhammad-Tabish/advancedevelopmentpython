import re

price = 'Price: $18,649.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0))
print(matches.group(1))


price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)
print(price_number)


#def is_filename_safe(filename):
 #  regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
  #  return re.match(regex, filename) is not None



