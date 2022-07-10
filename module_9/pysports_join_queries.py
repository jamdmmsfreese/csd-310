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
    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    print ("-- DISPLAYING PLAYER RECORDS --")
    players = cursor.fetchall()
    for player in players:
        print("Player ID {}".format(player[0]), 
              "\nFirst Name: {}".format(player[1]), 
              "\nLast Name: {}".format(player[2]),
              "\nTeam Name: {}\n".format(player[3]))

        
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