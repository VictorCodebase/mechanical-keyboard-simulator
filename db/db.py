import sqlite3

connect = sqlite3.connect('preferences.db')
cursor = connect.cursor() # cursor is used to execute SQL commands, like a pointer



#method to fetch data
def fetch_all(table):
    cursor.execute('SELECT * FROM ' + table)
    data = cursor.fetchall()
    if data:
        return data
    else:
        return None
    
def change_val(preference, value):
    cursor.execute('UPDATE settings SET ' + preference + ' = ? WHERE _id = 1', (value,))
    connect.commit()
    return True

def change_values(settings):
    if type(settings) != dict:
        raise TypeError('A dictionay was expected as argument') 
            
    try:
        for setting, value in settings.items():
            cursor.execute('UPDATE settings SET ' + setting + ' = ? WHERE _id = 1', (value,))
            print(setting,  "updated to", value)
        connect.commit()
    except Exception as e:
        print(e)
        return 'Setting update could not be completed'
       
    return ('Settings updated successfully')
    
def insert():
    #FIXME: pass a dictionary as argument for easier insertion
    values = (
        1, #cancel_to_tray
        1, #dynamic_vol
        1.5, #key_vol
        0, #emmersive_feedback
        "Device", #theme
        2 #key_theme
        )
    cursor.execute('INSERT INTO settings ("cancel_to_tray", "dynamic_vol", "key_vol", "emmersive_feedback", "theme", "key_theme") VALUES (?, ?, ?, ?, ?, ?)', values)
    connect.commit()
    return True


## Uncomment the following lines to test the methods
#insert()
#print(fetch_all('settings'))
#print(change_val('theme', 'dark'))
#print(change_values({'theme': 'light', 'key_theme': 1}))