# использование функции из модуля разными вариантами импорта
# импорты должны быть в начале файла, но тут располагаю их последовательно, чтобы проверить все способы импорта
import user_profile

user_information = user_profile.user_profile('иван', 'иванов', location='россия', work='слесарь')
print(user_information)

from user_profile import user_profile

user_information = user_profile('иван', 'иванов', location='россия', work='слесарь')
print(user_information)

from user_profile import user_profile as up

user_information = up('иван', 'иванов', location='россия', work='слесарь')
print(user_information)

import user_profile as us_pr

user_information = us_pr.user_profile('иван', 'иванов', location='россия', work='слесарь')
print(user_information)

from user_profile import *

user_information = user_profile('иван', 'иванов', location='россия', work='слесарь')
print(user_information)
