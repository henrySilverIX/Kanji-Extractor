import sqlite3
from entities.text_extractor import TextExtractor
from tkinter import *
from tkinter import ttk

#Inicializa o extrator de texto e imprime o texto em japonês no console
extrator_texto = TextExtractor("./docs/img/exemplo2.png")
extrator_texto.imprimir_texto_extraido()


#Conexão com o banco de dados
connection = sqlite3.connect('./docs/database/jamdict_database.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM entries WHERE kanji = ? or reading = ?", (extrator_texto.palavra, extrator_texto.palavra))
resultados = cursor.fetchall()



#Customização
BACKGROUND_COLOR = "#181A1B"
FOREGROUND_COLOR = "#DDDAD6"
FONT_FAMILY = "Ariel"





# Configuração a tela
window = Tk()
window.title("Japanese Kanji Extractor")
window.minsize(width=900, height=600)
window.config(background=BACKGROUND_COLOR)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



style = ttk.Style()
style.theme_use("default")  # usa o tema default que é personalizável

style.configure("TNotebook", background=BACKGROUND_COLOR, borderwidth=0)
style.configure("TNotebook.Tab",
                background="#222831",
                foreground="#EEEEEE",
                padding=[10, 5],
                font=(FONT_FAMILY, 10),
                borderwidth=0)
style.map("TNotebook.Tab",
          background=[("selected", BACKGROUND_COLOR)],  # fundo da aba ativa
          foreground=[("selected", FOREGROUND_COLOR)])  # texto da aba ativa



#Criação do notebook para as abas do programa
notebook = ttk.Notebook(window)
notebook.grid(row=0, column=0, sticky="nsew")




# Criação e adição do conteúdo de extração para uma aba
aba_extracao = Frame(notebook, background=BACKGROUND_COLOR, bd=0, highlightthickness=0)
notebook.add(aba_extracao, text="Extração dos Kanji")

# Labels agora são filhos de aba_extracao
titulo_label = Label(aba_extracao, text="KANJI CAPTURADOS: ", background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
titulo_label.grid(row=0, column=0)

print("Resultados obtidos: ", resultados)

conteudo_da_palavra_jpn = []
resultado_dict = {}

for linha in resultados:
    lista_aux = [linha[3], linha[4]]
    conteudo_da_palavra_jpn.append(lista_aux)
    resultado_dict[linha[2]] = conteudo_da_palavra_jpn

print("Valores obtidos em forma de dicionário: ")
for kanji, pron_e_sign in resultado_dict.items():
    print(kanji, pron_e_sign)

# Aqui também: todos os widgets devem pertencer a aba_extracao
linha_atual = 1
for kanji, pronuncia_e_significado in resultado_dict.items():
    kanji_info = Label(aba_extracao, text=kanji, background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
    kanji_info.grid(row=linha_atual, column=0)
    linha_atual += 1

    for leitura in pronuncia_e_significado:
        leitura_info = Label(aba_extracao, text=leitura[0], background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
        leitura_info.grid(row=linha_atual, column=0)
        linha_atual += 1

        significado_info = Label(aba_extracao, text=leitura[1], background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
        significado_info.grid(row=linha_atual, column=0)
        linha_atual += 1





#Criação da aba quiz e de seu conteúdo
aba_para_quiz = Frame(notebook, background=BACKGROUND_COLOR, bd=0, highlightthickness=0)
notebook.add(aba_para_quiz, text="Teste os seus conhecimentos")

pergunta = Label(aba_para_quiz, text="Qual o significado deste kanji: 学 ?", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
pergunta.grid(row=0, column=0, columnspan=2, pady=10)

op1 = Button(aba_para_quiz, text="Estudar")
op2 = Button(aba_para_quiz, text="Fogo")
op3 = Button(aba_para_quiz, text="Água")

op1.grid(row=1, column=0, padx=10, pady=5)
op2.grid(row=1, column=1, padx=10, pady=5)
op3.grid(row=2, column=0, columnspan=2, pady=5)

connection.close()
window.mainloop()