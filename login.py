user_database = [muhammed,darpan,manish]
usernames_list = [muhammed,darpan,mansh]

print('Enter First Name')
first_name = input().strip().lower()
print('Enter last Name')
last_name = input().strip().lower()
print('Enter User Name')
user_name = input().strip().lower()
print('enter your password')
password = input().strip().lower()
password2 = input().strip().lower()

if password == password2:
    user_database['usernames_list'].insert(user_name)
    user_database[user_name+'_password']= password
    print('hey {} Your Account is Created'.format(user_name))