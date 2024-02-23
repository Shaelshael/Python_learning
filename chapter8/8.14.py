# функция с произвольным набором именованных аргументов
def user_profile(first_name, last_name, **user_info):
    """возвращает содержимое в виде словаря"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


user_information = user_profile('иван', 'иванов', location='россия', work='слесарь')
print(user_information)
