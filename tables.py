import mysql.connector

db = mysql.connector.connect(host='localhost', database='', user='root', password='mysql123')

cursor = db.cursor()
cursor.execute("CREATE DATABASE reg12 ")
cursor.execute("use reg12")

ql = """CREATE TABLE playerinfo(GID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
        playername CHAR(20) NOT NULL,\
        gamingname CHAR(20) NOT NULL,\
        age INT NOT NULL,\
        wins INT ,\
        loss INT,\
        level INT,\
        ranked CHAR(15),
        points int default 2500 )"""

cursor.execute(ql)

ql1 = """CREATE TABLE rankedinfo1( GID INT,\
         kills INT ,\
         deaths INT,\
         result CHAR(5),\
         points INT,\
         CONSTRAINT LB1 FOREIGN KEY(GID) REFERENCES playerinfo(GID))"""

cursor.execute(ql1)

ql2 = """CREATE TABLE casualinfo1( GID INT ,\
         kills INT ,\
         deaths INT,\
         result CHAR(5),\
         points INT,\
         CONSTRAINT LB2 FOREIGN KEY(GID) REFERENCES playerinfo(GID))"""

cursor.execute(ql2)
