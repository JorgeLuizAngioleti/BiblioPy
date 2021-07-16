from tkinter import*
from tkinter import messagebox
import sqlite3
import datetime# datas e dia da semana
#Autor: Jorge Luiz Angioleti
# Versão 1.3
#Data da criação 31-03-2017
agora = datetime.date.today()
data=agora.strftime('%d/%m/%Y')
'''Uso livre para escolas publicas'''
def gravar():
        if not ed1.get()or not au.get() or not ed2.get(): 
               messagebox.showinfo("Empréstimo",'Preencher todos\n os campos.')
        else:
                conexao = sqlite3.connect("exemplo.sqlite") 
                cursor = conexao.cursor() 
                a1=data
                dado2=ed1.get()
                a2="Aluno(a): "+dado2.upper()
                dado3=ed2.get()
                a3="Nome do Livro: "+dado3.upper()
                a4=au.get()
                cursor.execute('''create table if not exists agenda(data text,nome text, telefone text, turma text)''') 
                cursor.execute('''insert into agenda (data, nome , telefone, turma) values(?,?,?,?)''', (a1,a2,a3,a4)) 
            
                conexao.commit() 

                messagebox.showinfo("Empréstimo", "Livro emprestado com sucesso!")
                cursor.close() 
                conexao.close()
                limpar()
        
    
def consulta():
        limpar()
        if  not di.get()or not me.get():
               messagebox.showinfo("Data", 'Você não prencheu\n a data da consulta.')
        else:
               conexao = sqlite3.connect("exemplo.sqlite") 
               cursor = conexao.cursor()
               dado1=di.get()+me.get()
               a1=dado1+'%'
               #cursor.execute('''SELECT rowid, nome, telefone FROM agenda''')
               cursor.execute("""SELECT rowid,data,nome,telefone,turma FROM agenda WHERE data like ?""",(a1,))
            
               for row in cursor.fetchall(): 
                   list.insert(END,str(row)) 
            
               cursor.close() 
               conexao.close()
               lb3['fg']='green'
               lb3['text'] = 'Consultando pela data.'

def con_nome():
        limpar()
        if  not ed5.get():
            messagebox.showinfo("Nome", 'Você não prencheu\n o nome da consulta.')
        else:
               conexao = sqlite3.connect("exemplo.sqlite") 
               cursor = conexao.cursor() 
               dado5=ed5.get()
               a5="Aluno(a): "+dado5.upper()+'%'
               #acima o sinal de % pesquisa por parte do nome
               cursor.execute("""SELECT rowid,data,nome,telefone,turma FROM agenda WHERE nome like ?""",(a5,))
            
               for row in cursor.fetchall(): 
                   list.insert(END, str(row)) 
            
               cursor.close() 
               conexao.close()
               lb3['fg']='green'
               lb3['text'] = 'Consultando pelo nome.'

def con_livro():
        limpar()
        if  not ed5.get():
               messagebox.showinfo("Livro", 'Você não prencheu\n o livro da consulta.')
        else:
               conexao = sqlite3.connect("exemplo.sqlite") 
               cursor = conexao.cursor() 
               dado5=ed5.get()
               a5="Nome do Livro: "+dado5.upper()+'%'
               #cursor.execute('''SELECT rowid, nome, telefone FROM agenda''')
               cursor.execute("""SELECT rowid,data,nome,telefone,turma FROM agenda WHERE telefone like ?""",(a5,))
            
               for row in cursor.fetchall(): 
                   list.insert(END, str(row)) 
            
               cursor.close() 
               conexao.close()
               lb3['fg']='green'
               lb3['text'] = 'Consultando pelo livro.'

def tudo():
       limpar()
       conexao = sqlite3.connect("exemplo.sqlite") 
       cursor = conexao.cursor() 
    
       cursor.execute('''SELECT rowid,data, nome, telefone, turma FROM agenda''')
       
    
       for row in cursor.fetchall(): 
           list.insert(END, str(row)) 
    
       cursor.close() 
       conexao.close()
       lb3['fg']='green'
       lb3['text'] = 'Consultando tudo.'

    
def excluir():
        if  not ed3.get():
               messagebox.showinfo("ID", 'Você não prencheu\n o ID da para devolver.')
        else:
               conexao = sqlite3.connect("exemplo.sqlite") 
               cursor = conexao.cursor() 
            
               cursor.execute('''DELETE FROM agenda WHERE rowid = ?''', (ed3.get(),)) 
            
               conexao.commit() 
               #messagebox.showinfo("Excluir", 'Deseja devolver o livro de registro %s?\n clique em OK '% ed3.get())
               cursor.close() 
               conexao.close()
               limpar()
               ed5.delete(0,END)
               lb3['fg']='green'
               lb3['text'] = 'Livro devolvido\n com sucesso!.'
              
    
def limpar(): 
       list.delete(0, END)
       ed1.delete(0,END)
       ed2.delete(0,END)
       ed3.delete(0,END)
       lb3['fg']='black'
       lb3['text']='Mensagem'
    
   # Parte gráfica 
janela = Tk() 
janela.geometry('1100x900+200+200')
janela.title('Biblioteca_Py')
    
   # Widgets 
lb1 = Label(janela,font="Arial 12 bold", text='Digite nome do aluno: ') 
lb2 = Label(janela,font="Arial 12 bold", text='Digite o livro: ') 
lb3 = Label(janela,font="Arial 15 bold", text='Mensagem') 
lb4 = Label(janela,font="Arial 12 bold", text='Utilize o ID para \n devolver livros.') 
lb5 = Label(janela, text='Data:',font="Arial 12 bold") 
lb6 = Label(janela,text='Invoices...')
imginv1=PhotoImage(file="livro.png")
lb6['image']=imginv1
lb7 = Label(janela,font="Arial 15 bold", text='Bliblioteca escolar      Autor: Jorge Luiz Angioleti     Data:   '+data)
lb8 = Label(janela, text='Consultar:',font="Arial 12 bold") 
lb9 = Label(janela,font="Arial 12 bold", text='Selecione a turma: ')     
list = Listbox(janela,height=20,width=122,font="Arial 14 bold") 
    
ed1 = Entry(janela,width=50,font="Arial 12 bold") 
ed2 = Entry(janela,width=50,font="Arial 12 bold") 
ed3 = Entry(janela,font="Arial 16 bold",width=5)
ed5 = Entry(janela,width=15,font="Arial 16 bold")

    
bt1 = Button(janela,width=10, text='EMPRESTAR',bg="green",font="Arial 12 bold", command=gravar) 
bt2 = Button(janela,width=20, text='CONSULTA PELA DATA',bg="yellow",font="Arial 12 bold", command=consulta)  
bt4 = Button(janela,width=10, text='DEVOLVER',bg="red",font="Arial 12 bold", command=excluir) 
bt5 = Button(janela,width=10, text='LIMPAR',bg='blue',font="Arial 12 bold", command=limpar)
bt6 = Button(janela,width=15, text='CONSULTAR TUDO',bg='yellow',font="Arial 12 bold", command=tudo)
bt7 = Button(janela,width=20, text='CONSULTA PELO NOME',bg="yellow",font="Arial 12 bold", command=con_nome)
bt8 = Button(janela,width=20, text='CONSULTA PELO LIVRO',bg="yellow",font="Arial 12 bold", command=con_livro)
#************************************************************************************************************
#mes
me = StringVar(janela)
ee = ('/01', '/02', '/03', '/04', '/05', '/06','/07', '/08', '/09', '/10', '/11', '/12')
option = OptionMenu(janela, me, *ee)
option.place(x=350, y=60)

#dia
ee1= ('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
di = StringVar(janela)
option = OptionMenu(janela, di, *ee1)
option.place(x=280, y=60)
# aula
au = StringVar(janela)
aa = ('1ºano mat','2ºano mat','3ºano mat','4ºano mat','5ºano mat','6ºano mat','7ºano mat','8ºano mat','9ºano mat','\n',
      '1ºano vesp','2ºano vesp','3ºano vesp','4ºano vesp','5ºano vesp','6ºano vesp','7ºano vesp','8ºano vesp','9ºano vesp')

option = OptionMenu(janela, au, *aa)
option.place(x=160, y=160)
    
# Posição dos widgets na tela 
lb1.place(x=0,y=100) 
lb2.place(x=0,y=130)  
lb3.place(x=1125,y=177)#mensagem 
lb4.place(x=950,y=178)#
lb5.place(x=210,y=60)
lb6.place(x=1000,y=0)
lb7.place(x=0,y=0)#titulo do app
lb8.place(x=450,y=60)
lb9.place(x=0,y=160)
ed1.place(x=180,y=100)
ed2.place(x=180,y=130)
ed5.place(x=550,y=60)#entrada data
ed3.place(x=860,y=180)#rowis  
bt1.place(x=470,y=180)#emprestar 
bt2.place(x=760,y=135)#consultar data
bt7.place(x=760,y=55)#consultar nome
bt8.place(x=760,y=95)#consultar livro
bt4.place(x=730,y=180) #devolver
bt5.place(x=600,y=180)#limpar
bt6.place(x=300,y=180)#tudo 
list.place(x=10,y=225)   
janela.mainloop()
