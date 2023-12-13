from tkinter import *
from tkinter import messagebox, ttk
import os
import sqlite3

#aba de cadastro de clientes
def cliente ():

    path = os.path.dirname(__file__)

    favicon = path+'\\petshop.ico'  

    conn = sqlite3.connect('cliente.db')
    c = conn.cursor()
    app = Tk()

    c.execute("""CREATE TABLE IF NOT EXISTS cliente(id integer PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cep integer,
                numero integer,
                complemento TEXT NOT NULL,
                cpf TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL)""")

    def inserir():

        conn = sqlite3.connect('cliente.db')
        c = conn.cursor()

        try:

            nome = vnome.get()
            cep = vcep.get()
            numero = vnumero.get()
            complemento = vcomplemento.get()
            cpf = vcpf.get()
            email = vemail.get()
            telefone = vtelefone.get()

            c.execute("INSERT INTO cliente VALUES(NULL, :nome, :cep, :numero, :complemento, :cpf, :email, :telefone)",
                    {'nome': nome,
                    'cep': cep,
                    'numero': numero,
                    'complemento': complemento,
                    'cpf': cpf,
                    'email': email,
                    'telefone': telefone
                    })

            if (vnome.get() == '') or (vcep.get() == '') or (vcpf.get() == '') or (vemail.get() == '') or (vtelefone.get() == ''):
                messagebox.showwarning('Atenção', 'Por favor, preencha todos os campos necessários.')
            else:
                conn.commit()
                messagebox.showinfo('Atenção', 'Cliente registrado.')
                listar()
                conn.close()
        except ValueError:
            messagebox.showwarning('Atenção', 'Valores inválidos.')
        finally:
            vnome.delete(0, END)
            vcep.delete(0, END)
            vnumero.delete(0, END)
            vcomplemento.delete(0, END)
            vcpf.delete(0, END)
            vemail.delete(0, END)
            vtelefone.delete(0, END)
            Entry.focus(vnome)


    def consultar():
        conn = sqlite3.connect('cliente.db')
        c = conn.cursor()

        nome = vnome.get()
        cep = vcep.get()
        numero = vnumero.get()
        complemento = vcomplemento.get()
        cpf = vcpf.get()
        email = vemail.get()
        telefone = vtelefone.get()

        if nome == '' and cep == '' and numero == '' and complemento == '' and cpf == '' and email == '' and telefone == '':
            messagebox.showwarning("Atenção", 'Você precisa digitar algo que deseja consultar.')
        else:
            if nome != '':
                c.execute("SELECT * FROM cliente WHERE nome like '%" + nome + "%'")
                rows = c.fetchall()
            elif cep != '':
                c.execute("SELECT * FROM cliente WHERE cep like '%" + str(cep) + "%'")
                rows = c.fetchall()
            elif numero != '':
                c.execute("SELECT * FROM cliente WHERE numero like '%" + str(numero) + "%'")
                rows = c.fetchall()
            elif complemento != '':
                c.execute("SELECT * FROM cliente WHERE complemento like '%" + complemento + "%'")
                rows = c.fetchall()
            elif cpf != '':
                c.execute("SELECT * FROM cliente WHERE cpf like '%" + cpf + "%'")
                rows = c.fetchall()
            elif email != '':
                c.execute("SELECT * FROM cliente WHERE email like '%" + email + "%'")
                rows = c.fetchall()
            elif telefone != '':
                c.execute("SELECT * FROM cliente WHERE telefone like '%" + telefone + "%'")
                rows = c.fetchall()
            try:
                if len(rows) == 0:
                    messagebox.showinfo('Atenção', 'Registro não encontrado.')
                    limpar(False)
                else:
                    limpar(False)
                    for x in range(len(rows)):
                        vid = rows[x][0]
                        nome = rows[x][1]
                        cep = str(rows[x][2])
                        numero = str(rows[x][3])
                        complemento = rows[x][4]
                        cpf = rows[x][5]
                        email = rows[x][6]
                        telefone = rows[x][7]

                        listRegistro.insert('', 'end', iid=None,
                                            values=(vid, nome, cep, numero, complemento, cpf, email, telefone))
            except UnboundLocalError:
                pass

    def listar():
        conn = sqlite3.connect('cliente.db')
        c = conn.cursor()

        c.execute("SELECT * FROM cliente ORDER BY id")

        rows = c.fetchall()
        conn.close()
        limpar()

        if len(rows) == 0:
            messagebox.showinfo('Atenção', 'Nenhum registro encontrado.')
        else:
            for x in range(len(rows)):
                vid = str(rows[x][0])
                nome = rows[x][1]
                cep = str(rows[x][2])
                numero = str(rows[x][3])
                complemento = rows[x][4]
                cpf = rows[x][5]
                email = rows[x][6]
                telefone = rows[x][7]

                listRegistro.insert('', 'end', iid=None,
                                    values=(vid, nome, cep, numero, complemento, cpf, email, telefone))


    def get_values():
        selected = listRegistro.selection()
        values = listRegistro.item(selected)['values']
        return values


    def preencher(event):
        values = get_values()

        vnome.delete(0, END)
        vnome.insert(END, values[1])
        vcep.delete(0, END)
        vcep.insert(END, values[2])
        vnumero.delete(0, END)
        vnumero.insert(END, values[3])
        vcomplemento.delete(0, END)
        vcomplemento.insert(END, values[4])
        vcpf.delete(0, END)
        vcpf.insert(END, values[5])
        vemail.delete(0, END)
        vemail.insert(END, values[6])
        vtelefone.delete(0, END)
        vtelefone.insert(END, values[7])
        return


    def atualizar():
        conn = sqlite3.connect('cliente.db')
        c = conn.cursor()

        try:
            vid = get_values()[0]

            nome = vnome.get()
            cep = vcep.get()
            numero = vnumero.get()
            complemento = vcomplemento.get()
            cpf = vcpf.get()
            email = vemail.get()
            telefone = vtelefone.get()

            if vid == '':
                messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')
                listar()

            else:

                if (vnome.get() == '') or (vcep.get() == '') or (vcpf.get() == '') or (vemail.get() == '') or (vtelefone.get() == ''):
                    messagebox.showwarning('Atenção', 'Por favor, preencha todos os campos.')

                else:
                    c.execute("UPDATE cliente SET nome='" + nome + "', cep='" + str(cep) + "', numero='" + str(numero) + "', "
                            "complemento='" + complemento + "', cpf='" + cpf + "', email='" + email + "', telefone='" + telefone + "' "
                            "WHERE  id='"+str(vid)+"' ")

                    conn.commit()
                    messagebox.showinfo('Mensagem Importante', 'Informações atualizadas com sucesso.')

        except IndexError:
            messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')

        finally:

            c.close()

            vnome.delete(0, END)
            vcep.delete(0, END)
            vnumero.delete(0, END)
            vcomplemento.delete(0, END)
            vcpf.delete(0, END)
            vemail.delete(0, END)
            vtelefone.delete(0, END)
            Entry.focus(vnome)
            listar()


    def excluir():
        conn = sqlite3.connect('cliente.db')
        c = conn.cursor()
        try:

            vid = get_values()[0]

            if vid == '':
                messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')
                listar()
            else:
                if messagebox.askyesno('Atenção', 'Deseja mesmo excluir este registro?'):
                    c.execute("DELETE FROM cliente WHERE id='"+str(vid)+"'")
                    conn.commit()
                else:
                    pass
        except IndexError:
            messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')

        finally:

            c.close()

            vnome.delete(0, END)
            vcep.delete(0, END)
            vnumero.delete(0, END)
            vcomplemento.delete(0, END)
            vcpf.delete(0, END)
            vemail.delete(0, END)
            vtelefone.delete(0, END)
            Entry.focus(vnome)
            listar()


    def limpar(tudo=True):

        if tudo:

            listRegistro.delete(*listRegistro.get_children())

            vnome.delete(0, END)
            vcep.delete(0, END)
            vnumero.delete(0, END)
            vcomplemento.delete(0, END)
            vcpf.delete(0, END)
            vemail.delete(0, END)
            vtelefone.delete(0, END)

        else:

            listRegistro.delete(*listRegistro.get_children())


    vnome = Entry(app, width=60)
    vnome.grid(row=0, column=1, columnspan=2, padx=20, pady=10)

    vcep = Entry(app, width=60)
    vcep.grid(row=1, column=1, columnspan=2, pady=10)

    vnumero = Entry(app, width=60)
    vnumero.grid(row=2, column=1, columnspan=2, pady=10)

    vcomplemento = Entry(app, width=60)
    vcomplemento.grid(row=3, column=1, columnspan=2, padx=20, pady=10)

    vcpf = Entry(app, width=60)
    vcpf.grid(row=4, column=1, columnspan=2, pady=10)

    vemail = Entry(app, width=60)
    vemail.grid(row=5, column=1, columnspan=2, pady=10)

    vtelefone = Entry(app, width=60)
    vtelefone.grid(row=6, column=1, columnspan=2, pady=10)

    nomel = Label(app, text='Nome: ', bg='yellow')
    nomel.grid(row=0, column=0, sticky='e')

    cepl = Label(app, text='CEP: ', bg='yellow')
    cepl.grid(row=1, column=0, sticky='e')

    numerol = Label(app, text='Número: ', bg='yellow')
    numerol.grid(row=2, column=0, sticky='e')

    complementol = Label(app, text='Complemento: ', bg='yellow')
    complementol.grid(row=3, column=0, sticky='e')

    cpfl = Label(app, text='CPF: ', bg='yellow')
    cpfl.grid(row=4, column=0, sticky='e')

    emaill = Label(app, text='E-mail: ', bg='yellow')
    emaill.grid(row=5, column=0, sticky='e')

    telefonel = Label(app, text='Telefone: ', bg='yellow')
    telefonel.grid(row=6, column=0, sticky='e')

    treeColunas = ('ID', 'Nome', 'CEP', 'Número', 'Complemento', 'CPF', 'E-mail', 'Telefone')
    listRegistro = ttk.Treeview(app, columns=treeColunas, selectmode='browse')

    listscrl = ttk.Scrollbar(app, orient='vertical', command=listRegistro.yview)
    listscrl.grid(row=9, column=5, sticky='ns', pady=10)
    listRegistro.configure(yscrollcommand=listscrl.set)

    listRegistro.heading('#0', text='')
    listRegistro.heading('ID', text='ID')
    listRegistro.heading('Nome', text='Nome')
    listRegistro.heading('CEP', text='CEP')
    listRegistro.heading('Número', text='Número')
    listRegistro.heading('Complemento', text='Complemento')
    listRegistro.heading('CPF', text='CPF')
    listRegistro.heading('E-mail', text='E-mail')
    listRegistro.heading('Telefone', text='Telefone')

    listRegistro.column('#0', width=0, stretch=NO)
    listRegistro.column('ID', minwidth=0, width=50, anchor='center')
    listRegistro.column('Nome', minwidth=0, width=100, anchor='center')
    listRegistro.column('CEP', minwidth=0, width=100, anchor='center')
    listRegistro.column('Número', minwidth=0, width=75, anchor='center')
    listRegistro.column('Complemento', minwidth=0, width=100, anchor='center')
    listRegistro.column('CPF', minwidth=0, width=100, anchor='center')
    listRegistro.column('E-mail', minwidth=0, width=100, anchor='center')
    listRegistro.column('Telefone', minwidth=0, width=100, anchor='center')

    listRegistro.grid(row=9, column=1, columnspan=4, pady=10)

    listRegistro.tag_bind('selecionar', '<<TreeviewSelect>>', preencher)

    botao1 = Button(app, text='Adicionar Cliente', command=inserir, bg='#fff')
    botao1.grid(row=0, column=4, pady=10, padx=10, ipadx=10)

    botao2 = Button(app, text='Consultar Cliente', command=consultar, bg='#fff')
    botao2.grid(row=1, column=4, pady=10, padx=10, ipadx=10)

    botao3 = Button(app, text='Mostrar Clientes', command=listar, bg='#fff')
    botao3.grid(row=2, column=4, pady=10, padx=10, ipadx=12.5)

    botao4 = Button(app, text='Atualizar Cliente', command=atualizar, bg='#fff')
    botao4.grid(row=3, column=4, pady=10, padx=10, ipadx=13)

    botao5 = Button(app, text='Excluir Cliente', command=excluir, bg='#fff')
    botao5.grid(row=4, column=4, pady=10, padx=10, ipadx=19)

    botao6 = Button(app, text='Limpar Tela', command=limpar, bg='#fff')
    botao6.grid(row=5, column=4, pady=10, padx=10, ipadx=27)

    conn.commit()
    conn.close()

    if __name__ == '__main__':

        listRegistro.bind('<<TreeviewSelect>>', preencher)
        app.title('Sistema Petshop')
        app.iconbitmap(favicon)
        app.geometry('900x600')
        app.configure(bg='yellow')
        app.mainloop()

#aba de cadastro de animais
def animal ():

    path = os.path.dirname(__file__)

    favicon = path+'\\petshop.ico'

    conn = sqlite3.connect('animal.db')
    c = conn.cursor()
    app = Tk()

    c.execute("""CREATE TABLE IF NOT EXISTS animal(id integer PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                tipo TEXT NOT NULL,
                raca TEXT,
                cpf TEXT NOT NULL)""")

    def inserir():

        conn = sqlite3.connect('animal.db')
        c = conn.cursor()

        try:

            nome = vnome.get()
            tipo = vtipo.get()
            raca = vraca.get()
            cpf = vcpf.get()

            c.execute("INSERT INTO animal VALUES(NULL, :nome, :tipo, :raca, :cpf)",
                    {'nome': nome,
                    'tipo': tipo,
                    'raca': raca,
                    'cpf': cpf,
                    })

            if (vtipo.get() == '') or (vcpf.get() == ''):
                messagebox.showwarning('Atenção', 'Por favor, preencha todos os campos necessários.')
            else:
                conn.commit()
                messagebox.showinfo('Atenção', 'Animal registrado.')
                listar()
                conn.close()
        except ValueError:
            messagebox.showwarning('Atenção', 'Valores inválidos.')
        finally:
            vnome.delete(0, END)
            vtipo.delete(0, END)
            vraca.delete(0, END)
            vcpf.delete(0, END)
            Entry.focus(vnome)


    def consultar():
        conn = sqlite3.connect('animal.db')
        c = conn.cursor()

        nome = vnome.get()
        tipo = vtipo.get()
        raca = vraca.get()
        cpf = vcpf.get()

        if nome == '' and tipo == '' and raca == '' and cpf == '':
            messagebox.showwarning("Atenção", 'Você precisa digitar algo que deseja consultar.')
        else:
            if nome != '':
                c.execute("SELECT * FROM animal WHERE nome like '%" + nome + "%'")
                rows = c.fetchall()
            elif tipo != '':
                c.execute("SELECT * FROM animal WHERE tipo like '%" + tipo + "%'")
                rows = c.fetchall()
            elif raca != '':
                c.execute("SELECT * FROM animal WHERE raca like '%" + raca + "%'")
                rows = c.fetchall()
            elif cpf != '':
                c.execute("SELECT * FROM animal WHERE cpf like '%" + cpf + "%'")
                rows = c.fetchall()
            try:
                if len(rows) == 0:
                    messagebox.showinfo('Atenção', 'Registro não encontrado.')
                    limpar(False)
                else:
                    limpar(False)
                    for x in range(len(rows)):
                        vid = rows[x][0]
                        nome = rows[x][1]
                        tipo = rows[x][2]
                        raca = rows[x][3]
                        cpf = rows[x][4]

                        listRegistro.insert('', 'end', iid=None,
                                            values=(vid, nome, tipo, raca, cpf))
            except UnboundLocalError:
                pass

    def listar():
        conn = sqlite3.connect('animal.db')
        c = conn.cursor()

        c.execute("SELECT * FROM animal ORDER BY id")

        rows = c.fetchall()
        conn.close()
        limpar()

        if len(rows) == 0:
            messagebox.showinfo('Atenção', 'Nenhum registro encontrado.')
        else:
            for x in range(len(rows)):

                vid = rows[x][0]
                nome = rows[x][1]
                tipo = rows[x][2]
                raca = rows[x][3]
                cpf = rows[x][4]

                listRegistro.insert('', 'end', iid=None,
                                    values=(vid, nome, tipo, raca, cpf))


    def get_values():
        selected = listRegistro.selection()
        values = listRegistro.item(selected)['values']
        return values


    def preencher(event):

        values = get_values()

        vnome.delete(0, END)
        vnome.insert(END, values[1])
        vtipo.delete(0, END)
        vtipo.insert(END, values[2])
        vraca.delete(0, END)
        vraca.insert(END, values[3])
        vcpf.delete(0, END)
        vcpf.insert(END, values[4])
        return


    def atualizar():
        conn = sqlite3.connect('animal.db')
        c = conn.cursor()

        try:
            vid = get_values()[0]

            nome = vnome.get()
            tipo = vtipo.get()
            raca = vraca.get()
            cpf = vcpf.get()

            if vid == '':
                messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')
                listar()

            else:

                if (vtipo.get() == '') or (vcpf.get() == ''):
                    messagebox.showwarning('Atenção', 'Por favor, preencha todos os campos.')

                else:
                    c.execute("UPDATE animal SET nome='" + nome + "', tipo='" + tipo + "', raca='" + raca + "', "
                            "cpf='" + cpf + "' "
                            "WHERE  id='"+str(vid)+"' ")

                    conn.commit()
                    messagebox.showinfo('Mensagem Importante', 'Informações atualizadas com sucesso.')

        except IndexError:
            messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')

        finally:

            c.close()

            vnome.delete(0, END)
            vtipo.delete(0, END)
            vraca.delete(0, END)
            vcpf.delete(0, END)
            Entry.focus(vnome)
            listar()


    def excluir():
        conn = sqlite3.connect('animal.db')
        c = conn.cursor()
        try:

            vid = get_values()[0]

            if vid == '':
                messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')
                listar()
            else:
                if messagebox.askyesno('Atenção', 'Deseja mesmo excluir este registro?'):
                    c.execute("DELETE FROM animal WHERE id='"+str(vid)+"'")
                    conn.commit()
                else:
                    pass
        except IndexError:
            messagebox.showwarning('Atenção', 'Você precisa selecionar um registro.')

        finally:

            c.close()

            vnome.delete(0, END)
            vtipo.delete(0, END)
            vraca.delete(0, END)
            vcpf.delete(0, END)
            Entry.focus(vnome)
            listar()


    def limpar(tudo=True):

        if tudo:

            listRegistro.delete(*listRegistro.get_children())

            vnome.delete(0, END)
            vtipo.delete(0, END)
            vraca.delete(0, END)
            vcpf.delete(0, END)
            Entry.focus(vnome)

        else:

            listRegistro.delete(*listRegistro.get_children())


    vnome = Entry(app, width=60)
    vnome.grid(row=0, column=1, columnspan=2, padx=20, pady=10)

    vtipo = Entry(app, width=60)
    vtipo.grid(row=1, column=1, columnspan=2, pady=10)

    vraca = Entry(app, width=60)
    vraca.grid(row=2, column=1, columnspan=2, pady=10)

    vcpf = Entry(app, width=60)
    vcpf.grid(row=3, column=1, columnspan=2, pady=10)

    nomel = Label(app, text='Nome do Animal: ', bg='yellow')
    nomel.grid(row=0, column=0, sticky='e')

    tipol = Label(app, text='Tipo do Animal: ', bg='yellow')
    tipol.grid(row=1, column=0, sticky='e')

    racal = Label(app, text='Raça do Animal: ', bg='yellow')
    racal.grid(row=2, column=0, sticky='e')

    cpfl = Label(app, text='CPF do Dono: ', bg='yellow')
    cpfl.grid(row=3, column=0, sticky='e')

    treeColunas = ('ID', 'Nome do Animal', 'Tipo do Animal', 'Raça do Animal', 'CPF do Dono')
    listRegistro = ttk.Treeview(app, columns=treeColunas, selectmode='browse')

    listscrl = ttk.Scrollbar(app, orient='vertical', command=listRegistro.yview)
    listscrl.grid(row=9, column=5, sticky='ns', pady=10)
    listRegistro.configure(yscrollcommand=listscrl.set)

    listRegistro.heading('#0', text='')
    listRegistro.heading('ID', text='ID')
    listRegistro.heading('Nome do Animal', text='Nome')
    listRegistro.heading('Tipo do Animal', text='Tipo')
    listRegistro.heading('Raça do Animal', text='Raça')
    listRegistro.heading('CPF do Dono', text='CPF')

    listRegistro.column('#0', width=0, stretch=NO)
    listRegistro.column('ID', minwidth=0, width=50, anchor='center')
    listRegistro.column('Nome do Animal', minwidth=0, width=100, anchor='center')
    listRegistro.column('Tipo do Animal', minwidth=0, width=100, anchor='center')
    listRegistro.column('Raça do Animal', minwidth=0, width=100, anchor='center')
    listRegistro.column('CPF do Dono', minwidth=0, width=100, anchor='center')

    listRegistro.grid(row=9, column=1, columnspan=4, pady=10)

    listRegistro.tag_bind('selecionar', '<<TreeviewSelect>>', preencher)

    botao1 = Button(app, text='Adicionar Animal', command=inserir, bg='#fff')
    botao1.grid(row=0, column=4, pady=10, padx=10, ipadx=10)

    botao2 = Button(app, text='Consultar Animal', command=consultar, bg='#fff')
    botao2.grid(row=1, column=4, pady=10, padx=10, ipadx=10)

    botao3 = Button(app, text='Mostrar Animal', command=listar, bg='#fff')
    botao3.grid(row=2, column=4, pady=10, padx=10, ipadx=12.5)

    botao4 = Button(app, text='Atualizar Animal', command=atualizar, bg='#fff')
    botao4.grid(row=3, column=4, pady=10, padx=10, ipadx=13)

    botao5 = Button(app, text='Excluir Animal', command=excluir, bg='#fff')
    botao5.grid(row=4, column=4, pady=10, padx=10, ipadx=19)

    botao6 = Button(app, text='Limpar Tela', command=limpar, bg='#fff')
    botao6.grid(row=5, column=4, pady=10, padx=10, ipadx=27)

    conn.commit()
    conn.close()

    if __name__ == '__main__':

        listRegistro.bind('<<TreeviewSelect>>', preencher)
        app.title('Sistema Petshop')
        app.iconbitmap(favicon)
        app.geometry('900x600')
        app.configure(bg='yellow')
        app.mainloop()

path = os.path.dirname(__file__)
favicon = path+'\\petshop.ico'
app = Tk()

botaoCliente = Button(app, text='Cadastro de Clientes', command=cliente, bg='#fff')
botaoCliente.grid(row=5, column=4, pady=10, padx=10, ipadx=27)

botaoAnimal = Button(app, text='Cadastro de Animais', command=animal, bg='#fff')
botaoAnimal.grid(row=6, column=4, pady=10, padx=10, ipadx=27)

if __name__ == '__main__':
    
    app.title('Sistema Petshop')
    app.iconbitmap(favicon)
    app.geometry('900x600')
    app.configure(bg='yellow')
    app.mainloop()