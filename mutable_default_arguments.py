def create_account (name: str, holder: str, account_holder: list = []):
    if not account_holder:
        account_holder = []

    account_holder.append(holder)



    return {
        'name': name,
        'main_account_holder' : holder,
         'account_holders': account_holder
    }

a1 = create_account('cheking', 'sam')
a2 = create_account('savings', 'JOHN')

print(a2)