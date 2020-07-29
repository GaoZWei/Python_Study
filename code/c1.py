# -*- coding: utf-8 -*-
ACCOUNT = 123
PASSWORD = 123

print('账号')
user_account = input()
print(type(user_account))
print('密码')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print('success')
else:
    print('false')
