import sqlite3
import xml.etree.ElementTree as ET


#Caminhos para o xml e database
xml_path = "JMDict-JPN"
db_path = "../database/jamdict_database.db"


#Criar uma conexão com o banco de dados
connection = sqlite3.connect(db_path)
cursor = connection.cursor()


#Criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS entries(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ent_seq INTEGER,
    kanji TEXT,
    reading TEXT,
    glosses TEXT
)
''')


#Análise e estruturação do XML
tree = ET.parse(xml_path)
root = tree.getroot()


for entry in root.findall('entry'):
    ent_seq = entry.findtext('ent_seq')

    #Por ter múltiplos <k_ele> ou <r_ele>, vamos pegar os primeiros
    keb = entry.find('./k_ele/keb')
    reb = entry.find('./r_ele/reb')

    kanji = keb.text if keb is not None else None
    reading = reb.text if reb is not None else None

    #Junta todos os glosses em um só campo
    glosses = entry.findall('./sense/gloss')
    gloss_text = '; '. join(g.text for g in glosses if g.text)

    #Insere no banco de dados
    cursor.execute('INSERT INTO entries (ent_seq, kanji, reading, glosses) VALUES (?, ?, ?, ?)', (ent_seq, kanji, reading, gloss_text))


#Finaliza e fecha a conexão
connection.commit()
connection.close()

print("Banco de dados criado com o sucesso")