import sqlite3
from entities.text_extractor import TextExtractor
from tkinter import *


#Inicializa o extrator de texto e imprime o texto em japonês no console
extrator_texto = TextExtractor("./docs/img/exemplo2.png")
extrator_texto.imprimir_texto_extraido()


#Conexão com o banco de dados
connection = sqlite3.connect('./docs/database/jamdict_database.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM entries WHERE kanji = ? or reading = ?", (extrator_texto.palavra, extrator_texto.palavra))
resultados = cursor.fetchall()


BACKGROUND_COLOR = "#181A1B"
FOREGROUND_COLOR = "#DDDAD6"
FONT_FAMILY = "Ariel"


# Configuração a tela
window = Tk()
window.title("Japanese Kanji Extractor")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#Labels
titulo_label = Label(text="KANJI CAPTURADOS: ", background=BACKGROUND_COLOR)
titulo_label.grid(row=0, column=0)
titulo_label.config(foreground=FOREGROUND_COLOR)

print(resultados)

resultado_dict = {}

for linha in resultados:
    lista_aux = [linha[3], linha[4]]
    resultado_dict[linha[2]] = lista_aux

    print(f"Kanji: {linha[2]}, Leitura: {linha[3]}, Significado: {linha[4]}")

print(resultado_dict)

for index, linha in enumerate(resultados):
    kanji_info = Label(text=linha[2], background=BACKGROUND_COLOR)
    kanji_info.grid(row=1, column=index)
    kanji_info.config(foreground=FOREGROUND_COLOR)


    leitura_info = Label(text=linha[3], background=BACKGROUND_COLOR)
    leitura_info.grid(row=2, column=index)
    leitura_info.config(foreground=FOREGROUND_COLOR)

    significado_info = Label(text=linha[4], background=BACKGROUND_COLOR)
    significado_info.grid(row=3, column=index)
    significado_info.config(foreground=FOREGROUND_COLOR)

    print(f"Kanji: {linha[2]}, Leitura: {linha[3]}, Significado: {linha[4]}")


connection.close()
window.mainloop()