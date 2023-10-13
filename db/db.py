import sqlite3



def connect():
    connect = sqlite3.connect('db/preferences.db')
    #! To test, please comment out the following line and comment the previous one to get the right path
    #connect = sqlite3.connect('preferences.db')
    cursor = connect.cursor() # (to me) behaves like a pointer
    return connect, cursor

connect_, cursor = connect()


#method to fetch data
def fetch_all(table):
    cursor.execute('SELECT * FROM ' + table)
    data = cursor.fetchall()
    if data:
        return data
    else:
        return None
    
def fetch_one(table = 'settings', column = '*'):
    cursor.execute('SELECT ' + column + ' FROM ' + table )
    data = cursor.fetchall()
    if data:
        return data[0][0] 
    else:
        return None
    
def change_val(table, preference, value):
    cursor.execute('UPDATE ' +table + ' SET ' + preference + ' = ? WHERE _id = 1', (value,))
    connect_.commit()
    return True

def change_values(table, settings):
    if type(settings) != dict:
        raise TypeError('A dictionay was expected as argument') 
    if len(settings) == 0 or settings == None:
        raise ValueError('A non-empty dictionary was expected as argument')

            
    try:
        for setting, value in settings.items():
            cursor.execute('UPDATE ' + table + ' SET ' + setting + ' = ? WHERE _id = 1', (value,))
            print(setting,  "updated to", value)
        connect_.commit()
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
    connect_.commit()
    return True


## Uncomment the following lines to test the methods
#! I added a parameter 'table' for these methods, but Im not really feeling like updating this part. You'll have to do it; sorry🙃
#insert()
#print(fetch_all('settings'))
#print(change_val('theme', 'dark'))
#print(change_values({'theme': 'light', 'key_theme': 1}))
#print(fetch_one())