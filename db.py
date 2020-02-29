import sqlite3

conn = sqlite3.connect('alpashop.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('DROP TABLE IF EXISTS lama ;')
    c.execute('DROP TABLE IF EXISTS alpaga ;')
    c.execute('DROP TABLE IF EXISTS animal ;')
    c.execute('DROP TABLE IF EXISTS couleur ;')
    c.execute('DROP TABLE IF EXISTS temperament ;')

    c.execute('CREATE TABLE IF NOT EXISTS lama (id INTEGER PRIMARY KEY, puht REAL, fk_temperament INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS alpaga (id INTEGER PRIMARY KEY, prixLaine REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS animal (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, age INTEGER, poids REAL, image TEXT, description TEXT, fk_couleur INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS couleur (id INTEGER PRIMARY KEY AUTOINCREMENT, libelle TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS temperament (id INTEGER PRIMARY KEY AUTOINCREMENT, libelle TEXT)')

    # c.execute('ALTER TABLE lama(FOREIGN KEY(fk_temperament) REFERENCES temperament(id))')
    # c.execute('ALTER TABLE animal(FOREIGN KEY(fk_couleur) REFERENCES couleur(id))')

def insert_data():

    # INSERT COULEUR
    c.execute("INSERT INTO couleur (libelle) VALUES('BLANC') , ('NOIR') , ('GRIS') , ('MARRON')")

    # INSERT TEMPERAMENT
    c.execute("INSERT INTO temperament (libelle) VALUES('NORMAL') , ('SOCIABLE') , ('INSOCIABLE') , ('PETIT CON')")

    # INSERT animal
    c.execute("INSERT INTO animal (nom, age, poids, fk_couleur, description, image) VALUES('Mati', 4, 35, 1, 'Gentil alpaga très affectueux.', '/images/mati.jpg') , ('Nico', 5, 75, 2, 'Moyennement agréable souvent agacé de la vie.', '/images/mati.jpg') , ('Chloé', 3, 28, 4, 'Lama très gentil se prend pour un cameLEON.', 'https://lh3.googleusercontent.com/proxy/UJVHeivINI3u485jU40IOPK9F6IS-nFveHVfJVnFyIaCSOKrLcfVpPoh_UhViqw4haT_Z5odAfYwmv3Ou0f-Ova8JXoUlDHZP_4QNIe9du0t7c67Q4Mkutk8LpRIUTLuSexug1LPPJP1') , ('Nicho', 14, 56, 2, 'Lama plutôt attardé est persuadé qu il va courrir le marathon.', 'https://www.culture-generale.fr/wp-content/uploads/lama.jpg') , ('Vincent', 13, 46, 1, 'Cet alpaga est un artiste c est lui qui vous prendra en photo.', 'https://fr.metrotime.be/wp-content/uploads/2017/05/Alpagas-Une.jpg') , ('Lola', 55, 32, 3, 'Le plus gentil alpaga de notre élevage malgrés sa petite taille d un pohu dix.','https://www.pairidaiza.eu/sites/default/files/styles/media_text_image/public/media/image/Alpaga-photo%20-%20animalR.jpg?itok=RPv4c9pw')")

    # INSERT LAMA
    c.execute("INSERT INTO lama (id, puht, fk_temperament) VALUES(2, 666, 3) , (3, 550, 1) , (4, 200, 4)")

    # INSERT ALPAGA
    c.execute("INSERT INTO alpaga (id, prixLaine) VALUES(1, 450) , (5, 565) , (6, 800)")

    conn.commit()
    c.close()
    conn.close()

def findLama(id):
    conn = sqlite3.connect('alpashop.db', check_same_thread=False)
    c = conn.cursor()

    if id != "*":
        # retourne tous les lamas
        query = "SELECT nom, age, poids, c.libelle, t.libelle, a.description, a.image, l.puht FROM animal a INNER JOIN lama l ON a.id = l.id INNER JOIN couleur c ON a.fk_couleur = c.id INNER JOIN temperament t ON l.fk_temperament = t.id WHERE l.id = " + str(id)
    else:
        # retourne un lama (id)
        query = "SELECT nom, age, poids, c.libelle, t.libelle, a.description, a.image, l.puht FROM animal a INNER JOIN lama l ON a.id = l.id INNER JOIN couleur c ON a.fk_couleur = c.id INNER JOIN temperament t ON l.fk_temperament = t.id"

    c.execute(query)

    lstLamas = []
    for lama in c:
        # lama[0] = nom, lama[1] = age, lama[2] = poids, lama[3] = couleur, lama[4] = temperament, lama[5] = description, lama[6] = image, lama[7] = puht
        lstLamas.append([lama[0],lama[1],lama[2],lama[3],lama[4],lama[5],lama[6], lama[7]])
    c.close()
    conn.close()

    return lstLamas

def findAll(id):
    conn = sqlite3.connect('alpashop.db', check_same_thread=False)
    c = conn.cursor()

    if id != "*":
        # retourne tous les lamas
        query = "SELECT nom, age, poids, c.libelle, a.description, a.image FROM animal a INNER JOIN couleur c ON a.fk_couleur = c.id WHERE l.id = " + str(id)
    else:
        # retourne un lama (id)
        query = "SELECT nom, age, poids, c.libelle, a.description, a.image FROM animal a INNER JOIN couleur c ON a.fk_couleur = c.id"

    c.execute(query)

    lstLamas = []
    for lama in c:
        # lama[0] = nom, lama[1] = age, lama[2] = poids, lama[3] = couleur, lama[4] = description, lama[5] = image
        lstLamas.append([lama[0],lama[1],lama[2],lama[3],lama[4],lama[5]])
    c.close()
    conn.close()

    return lstLamas

print(str(findAll("*")))

# A décommenter pour reconstruction de la bdd 
# create_table()
# insert_data()







