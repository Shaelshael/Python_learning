def user_profile(first_name, last_name, **user_info):
    """возвращает содержимое в виде словаря"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info
