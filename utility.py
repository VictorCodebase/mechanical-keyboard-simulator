
preference_file = 'user_preferences.txt'

def get_preference(preference):
    with open(preference_file, 'r') as file:
        raw = file.readlines()
    for i in raw:
        if preference in i.split(':')[0]:
            return (i.split(':')[1]).split(',')[0]
    return False

def set_preference(preference, value):
    with open(preference_file, 'r') as file:
        raw = file.readlines()
    for i in raw:
        if preference in i.split(':')[0]:
            raw[raw.index(i)] = f'{preference}:{value}\n'
            break
        if preference not in i.split(':')[0] and raw.index(i) == len(raw) - 1:
            Exception (f'The preference "{preference}" not found in {preference_file}')
            #raw.append(f'{preference}:{value}\n')

    with open(preference_file, 'w') as file:
        file.writelines(raw)
    return True

