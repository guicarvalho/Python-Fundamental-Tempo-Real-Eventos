# coding: utf-8

import tkMessageBox

import tkSimpleDialog

from Tkinter import *

from operacoes import Controlador


def limpar_campos_do_formulario():
    for entry in entry_widgets:
        entry.delete(0, END)
    entry_widgets[0].focus_set()


def cadastrar_livro():
    db.cadastrar(
        ano=entry_ano.get(),
        autor=entry_autor.get(),
        isbn=entry_isbn.get(),
        titulo=entry_titulo.get()
    )

    limpar_campos_do_formulario()

    tkMessageBox.showinfo(message='Livro cadastrado com sucesso!')


def preencher_lista_livros():
    list_livros.delete(0, END)
    
    for index, regs in enumerate(db.ler()):
    	list_livros.insert(index, regs[3])


def selecionar_livro(evt):
    widget = evt.widget
    index = int(widget.curselection()[0])
    value = widget.get(index)
    
    info_livro_selecionado = db.buscar_livro_por_titulo(value)[0]

    limpar_campos_do_formulario()

    entry_isbn.insert(0, info_livro_selecionado[1])
    entry_autor.insert(0, info_livro_selecionado[2])
    entry_titulo.insert(0, info_livro_selecionado[3])
    entry_ano.insert(0, info_livro_selecionado[4])

    global titulo_do_ultimo_livro_selecionado
    titulo_do_ultimo_livro_selecionado = entry_titulo.get()


def excluir_livro():
    resp = tkMessageBox.askquestion('Excluir livro', 'Quer excluir esse livro?', icon='warning')

    if resp == 'yes':
        db.excluir(entry_titulo.get())
        tkMessageBox.showinfo('Sucesso', 'Livro excluido com sucesso!')


def alterar_livro():
    resp = tkMessageBox.askquestion('Alterar livro', 'Quer alterar esse livro?', icon='warning')
    if resp == 'yes':
        db.alterar(
            titulo_antigo=titulo_do_ultimo_livro_selecionado,
            ano=entry_ano.get(),
            autor=entry_autor.get(),
            isbn=entry_isbn.get(),
            titulo=entry_titulo.get()
        )
        tkMessageBox.showinfo('Sucesso', 'Livro alterado com sucesso!')

# banco de dados
db = Controlador()

root = Tk()
root.title("Minha biblioteca 1.0")
root.geometry("500x550+0+0")

entry_widgets = []

titulo_do_ultimo_livro_selecionado = ''

Label(root, text="ISBN").pack(fill=X)
entry_isbn = Entry(root)
entry_isbn.pack(fill=X)

Label(root, text="Autor").pack(fill=X)
entry_autor = Entry(root)
entry_autor.pack(fill=X)

Label(root, text="Título").pack(fill=X)
entry_titulo = Entry(root)
entry_titulo.pack(fill=X)

Label(root, text="Ano").pack(fill=X)
entry_ano = Entry(root)
entry_ano.pack(fill=X)

list_livros = Listbox(root)
list_livros.pack(fill=X, pady=10)
list_livros.bind('<<ListboxSelect>>', selecionar_livro)

Button(root, text="Cadastrar", bg="green", fg="white", command=cadastrar_livro).pack(fill=X)
Button(root, text="Atualizar", bg="blue", fg="white", command=alterar_livro).pack(fill=X)
Button(root, text="Remover", bg="red", fg="white", command=excluir_livro).pack(fill=X)
Button(root, text="Novo", bg="white", command=limpar_campos_do_formulario).pack(fill=X)
Button(root, text="Recarregar", command=preencher_lista_livros).pack(fill=X)

entry_widgets.append(entry_isbn)
entry_widgets.append(entry_autor)
entry_widgets.append(entry_ano)
entry_widgets.append(entry_titulo)

mainloop()
