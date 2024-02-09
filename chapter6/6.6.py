favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}
people_to_participate = ['jen', 'ivan', 'phil', 'arkadii']
for name in people_to_participate:
    if name in favorite_languages.keys():
        print(f'{name.title()}, hope you enjoyed our survey!')
    else:
        print(f'{name.title()}, you should partricipate in our survey.')
