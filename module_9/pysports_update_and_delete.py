import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Springtrk#22",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    #Insert Player
    cursor = db.cursor()
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk',1)")
    
    print ("-- DISPLAYING PLAYER AFTER INSERT --")
    players = cursor.fetchall()
    for player in players:
        print("Player ID {}".format(player[0]), 
              "\nFirst Name: {}".format(player[1]), 
              "\nLast Name: {}".format(player[2]),
              "\nTeam Name: {}\n".format(player[3]))
    
    #Update Player
    cursor = db.cursor()
    cursor.execute("UPDATE player SET team_id = 2 WHERE first_name = ''Smeagol'")
    
    print ("-- DISPLAYING PLAYER AFTER UPDATE --")
    players = cursor.fetchall()
    for player in players:
        print("Player ID {}".format(player[0]), 
              "\nFirst Name: {}".format(player[1]), 
              "\nLast Name: {}".format(player[2]),
              "\nTeam Name: {}\n".format(player[3]))
    
    #Delete Player
    cursor = db.cursor()
    cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol'")
    
    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    print ("-- DISPLAYING PLAYER AFTER DELETE --")
    players = cursor.fetchall()
    for player in players:
        print("Player ID {}".format(player[0]), 
              "\nFirst Name: {}".format(player[1]), 
              "\nLast Name: {}".format(player[2]),
              "\nTeam Name: {}\n".format(player[3]))
    db.commit()
        
    input("\n\n  End of program, press any key to exit... ") 
    
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
        
    else:
        print(err)
finally:
    db.close()