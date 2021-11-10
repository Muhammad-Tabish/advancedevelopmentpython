from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(today)
print(tomorrow)

print(today.strftime('%d-%m-%y  %H:%M:%S'))

user_data = input('enter the data and time in format: ')
user_data = datetime.strptime(user_data,'%Y-%m-%d')
print(user_data)