import sqlite3

# Create/connect to database
conn = sqlite3.connect('alarm_clock.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS alarms (
    user_uuid TEXT,
    hour INTEGER,
    minutes INTEGER,
    repeat TEXT,
    active INTEGER
)
''')
conn.commit()

def get_alarms(uuid):
    cursor.execute('SELECT *, oid FROM alarms WHERE user_uuid = ? ORDER BY hour, minutes', (uuid,))
    result = cursor.fetchall()
    return result

def add_alarm_to_database(hour, minutes, uuid, repeat, active):
    cursor.execute('''
        INSERT INTO alarms (user_uuid, hour, minutes, repeat, active) 
        VALUES (?, ?, ?, ?, ?)
    ''', (uuid, hour, minutes, repeat, active))
    conn.commit()