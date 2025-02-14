username = input('Enter Username: ')
password = input('Enter Password: ')

if username == "admin":
    if password == "1234":
     print('Access granted!')
    else:
     print('Access denied!')
else:
  print('Access denied!')