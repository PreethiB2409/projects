import sqlite3
connection=sqlite3.connect("museum.db")
connection=sqlite3.connect(":memory:")
cur=connection.cursor()
#print("database created")
cur.execute('''CREATE TABLE ARTIST_INFORMATION(PAINTING_ID INT PRIMARY KEY,
                                                ARTIST_NAME VARCHAR(50) NOT NULL,
                                               YOB INT NOT NULL)''')
cur.execute('''CREATE TABLE PAINTINGS(PAINTING_ID INT,
                                      PAINTING_NAME VARCHAR(50) NOT NULL,
                                      YOR INT NOT NULL, FOREIGN KEY(PAINTING_ID) REFERENCES ARTIST_INFORMATION(PAINTING_ID))''')
cur.execute('''CREATE TABLE PAINTING_INFORMATION(PAINTING_ID INT,
                                                 ABOUT VARCHAR(150) NOT NULL, FOREIGN KEY(PAINTING_ID) REFERENCES ARTIST_INFORMATION(PAINTING_ID))''')

cur.execute('''INSERT INTO ARTIST_INFORMATION(PAINTING_ID,ARTIST_NAME,YOB)values(1,'Vincent van Gogh',1853)''')
cur.execute('''INSERT INTO ARTIST_INFORMATION(PAINTING_ID,ARTIST_NAME,YOB)values(2,'Johannes Vermeer','1632')''')
cur.execute('''INSERT INTO ARTIST_INFORMATION(PAINTING_ID,ARTIST_NAME,YOB)values(3,'Édouard Manet',1832)''')
cur.execute('''INSERT INTO ARTIST_INFORMATION(PAINTING_ID,ARTIST_NAME,YOB)values(4,'Grant Wood',1891)''')

cur.execute('''INSERT INTO PAINTINGS(PAINTING_ID,PAINTING_NAME,YOR)values(1,'ALMOND BLOSSOMS',1890)''')
cur.execute('''INSERT INTO PAINTINGS(PAINTING_ID,PAINTING_NAME,YOR)values(2,'GIRL WITH A PEARL EARRING',1665)''')
cur.execute('''INSERT INTO PAINTINGS(PAINTING_ID,PAINTING_NAME,YOR)values(3,'OLYMPIA',1863)''')
cur.execute('''INSERT INTO PAINTINGS(PAINTING_ID,PAINTING_NAME,YOR)values(4,'AMERICAN GOTHIC',1930)''')

cur.execute('''INSERT INTO PAINTING_INFORMATION(PAINTING_ID,ABOUT)values(1,'A group of several paintings of blossoming almond trees. Flowering trees were special to van Gogh. They represented awakening and hope. He enjoyed them aesthetically and found joy in painting flowering trees')''')
cur.execute('''INSERT INTO PAINTING_INFORMATION(PAINTING_ID,ABOUT)values(2,'Became known by its present title towards the end of the 20th century after the earring worn by the girl portrayed there.')''')
cur.execute('''INSERT INTO PAINTING_INFORMATION(PAINTING_ID,ABOUT)values(3,'Shows a nude woman lying on a bed being brought flowers by a servant. Olympia was modelled by Victorine Meurent and Olympias servant by the art model Laure.')''')
cur.execute('''INSERT INTO PAINTING_INFORMATION(PAINTING_ID,ABOUT)values(4,'Wood was inspired to paint what is now known as the American Gothic House in Eldon, Iowa, along with "the kind of people [he] fancied should live in that house".')''')

"""cur.execute('DROP TABLE ARTIST_INFORMATION')
cur.execute('DROP TABLE PAINTINGS')
cur.execute('DROP TABLE PAINTING_INFORMATION')"""

res1=cur.execute('''SELECT PAINTING_NAME FROM PAINTINGS WHERE PAINTING_ID IN 
                    (SELECT PAINTING_ID FROM ARTIST_INFORMATION WHERE ARTIST_NAME = 'Johannes Vermeer')''')

painting_name = cur.fetchone()[0]
print("Painting by Johannes Vermeer:", painting_name)

res2=cur.execute('''SELECT ABOUT FROM PAINTING_INFORMATION WHERE PAINTING_ID IN
                    (SELECT PAINTING_ID FROM PAINTINGS WHERE PAINTING_NAME='ALMOND BLOSSOMS')''')

painting_about=cur.fetchone()[0]
print("ALMOND BLOSSOM->",painting_about)

res3=cur.execute('''SELECT YOB FROM ARTIST_INFORMATION WHERE PAINTING_ID IN
                    (SELECT PAINTING_ID FROM PAINTINGS WHERE PAINTING_NAME='AMERICAN GOTHIC')''')

yob_artist=cur.fetchone()[0]
print("Year of birth of artist behind AMERICAN GOTHIC is",yob_artist)

res4=cur.execute('''SELECT YOR FROM PAINTINGS WHERE PAINTING_ID IN
                    (SELECT PAINTING_ID FROM ARTIST_INFORMATION WHERE ARTIST_NAME='Édouard Manet')''')

release=cur.fetchone()[0]
print("Year is:",release)

res5=cur.execute('''SELECT PAINTINGS.PAINTING_NAME FROM ARTIST_INFORMATION
                    JOIN PAINTINGS ON ARTIST_INFORMATION.PAINTING_ID = PAINTINGS.PAINTING_ID
                    ORDER BY ARTIST_INFORMATION.YOB ASC''')

print("Paintings sorted by year of birth of the artist:")
painting_names=cur.fetchall()
for name in painting_names:
    print(name[0])
