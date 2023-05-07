from tkinter import *
import tkinter.messagebox as messagebox
from validate_docbr import CPF
import brazilcep
import datetime


root = Tk()
root.geometry("600x700")

# Limpar Campos
def limparCampos(tipo):
    if tipo == "todos":
        nomeEntry.delete(0, END)
        maeEntry.delete(0, END)
        cpfEntry.delete(0, END)
        nascimentoEntry.delete(0, END)
        cepEntry.delete(0, END)
    enderecoEntry.delete(0, END)
    numeroEntry.delete(0, END)
    bairroEntry.delete(0, END)
    cidadeEntry.delete(0, END)
    estadoEntry.delete(0, END)


# Função para verificar CEP
def cepCorreios():
    limparCampos("endereco")
    # A variável zipcode está recebendo o conteúdo do campo CEP
    zipcode = cepEntry.get()
    dadosCep = brazilcep.get_address_from_cep(zipcode)

    enderecoEntry.insert(END, dadosCep['street'] )
    cidadeEntry.insert(END, dadosCep['city'])
    bairroEntry.insert(END, dadosCep['district'])
    estadoEntry.insert(END, dadosCep['uf'])
    

# Título
Label(root, text="Cadastro do Conecte SUS", font= "arial 15 bold", fg="blue").grid(row=0, column=3, pady = 20)

# Nome dos campos
nome = Label(root, text="Nome: ", font="arial 12", bg="#E6E6FA")
nome_mae = Label(root, text="Nome da Mãe: ", font="arial 12", bg="#E6E6FA")
cpf = Label(root, text="CPF: ", font="arial 12", bg="#E6E6FA")
data_nascimento = Label(root, text="Data de Nascimento (00/00/00): ", font="arial 12", bg="#E6E6FA")
cep             = Button(text="CEP: ", command = cepCorreios, font="arial 12", bg="#E6E6FA")
endereco        = Label(root, text="Endereço: ", font="arial 12", bg="#E6E6FA")
numero          = Label(root, text="Numero: ", font="arial 12", bg="#E6E6FA")
bairro          = Label(root, text="Bairro: ", font="arial 12", bg="#E6E6FA")
cidade          = Label(root, text="Cidade: ", font="arial 12", bg="#E6E6FA")
estado          = Label(root, text="Estado: ", font="arial 12", bg="#E6E6FA")

# Posicionamento dos campos

nome.grid(row=1, column=2, padx=10, pady=10)
nome_mae.grid(row=2, column=2, padx=10, pady=10)
cpf.grid(row=3, column=2, padx=10, pady=10)
data_nascimento.grid(row=4, column=2, padx=10, pady=10)
cep.grid(row=5, column=2, padx=10, pady=10)
endereco.grid(row = 6, column = 2, padx=10, pady=10)
numero.grid(row = 7, column = 2, padx=10, pady=10)
bairro.grid(row = 8, column = 2, padx=10, pady=10)
cidade.grid(row = 9, column = 2, padx=10, pady=10)
estado.grid(row = 10, column = 2, padx=10, pady=10)


# Variáveis para armazenar os dados
NomeValue = StringVar()
MaeValue = StringVar()
cpfValue = StringVar()
nascimentoValue = StringVar()
checkValue = IntVar()
cepValue = IntVar()
enderecoValue = StringVar()
numeroValue = StringVar()
bairroValue = StringVar()
cidadeValue = StringVar()
estadoValue = StringVar()


# Criação dos campos de entrada (bd = borda)
nomeEntry = Entry(root, textvariable=NomeValue, bd=2)
maeEntry = Entry(root, textvariable=MaeValue, bd=2)
cpfEntry = Entry(root, textvariable=cpfValue, bd=2)
nascimentoEntry = Entry(root, textvariable=nascimentoValue, bd=2)
cepEntry = Entry(root, textvariable=cepValue, bd=2)
enderecoEntry = Entry(root, textvariable=enderecoValue, bd=2)
numeroEntry = Entry(root, textvariable=numeroValue, bd=2)
bairroEntry = Entry(root, textvariable=bairroValue, bd=2)
cidadeEntry = Entry(root, textvariable=cidadeValue, bd=2)
estadoEntry = Entry(root, textvariable=estadoValue, bd=2)

# Posicionamento dos campos de entrada
nomeEntry.grid(row=1, column=3)
maeEntry.grid(row=2, column=3)
cpfEntry.grid(row=3, column=3)
nascimentoEntry.grid(row=4, column=3)
cepEntry.grid(row=5, column=3)
enderecoEntry.grid(row=6, column=3)
numeroEntry.grid(row=7, column=3)
bairroEntry.grid(row=8, column=3)
cidadeEntry.grid(row=9, column=3)
estadoEntry.grid(row=10, column=3)


# Criação da caixa de seleção
checkbtn = Checkbutton(text="Lembrar-me", variable=checkValue, font="arial 12", bg="#E6E6FA", fg="black", relief="groove")
checkbtn.grid(row=11, column=3, padx=10, pady=10)

# Função para salvar as informações no arquivo

def salvar_informacoes():
    # Obter os valores das entradas
    nome = NomeValue.get()
    mae = MaeValue.get()
    cpf = cpfValue.get()
    nascimento = nascimentoValue.get()
    cep = cepValue.get()
    endereco = enderecoValue.get()
    numero = numeroValue.get()
    bairro = bairroValue.get()
    cidade = cidadeValue.get()
    estado = estadoValue.get()


    # Verifica se está em branco
    if nome == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O nome deve ser informado.")
        nomeEntry.focus_set()
        return
    
    if mae == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O nome da mãe deve ser informado.")
        maeEntry.focus_set()
        return
    
    if cpf == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O CPF deve ser informado.")
        cpfEntry.focus_set()
        return
    
    if cep == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O CPF deve ser informado.")
        cepEntry.focus_set()
        return
    
    if nascimento == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O nascimento deve ser informado.")
        cpfEntry.focus_set()
        return

    if numero == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O número deve ser informado.")
        numero.focus_set()
        return
    
    if endereco == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O endereço deve ser informado.")
        enderecoEntry.focus_set()
        return
    
    if bairro == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O bairro deve ser informado.")
        bairroEntry.focus_set()
        
    if cidade == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O nome da cidade ãe deve ser informado.")
        cidadeEntry.focus_set()
        
    if estado == '':
        messagebox.showerror("Cadastro do Conecte SUS", "O nome do estado ãe deve ser informado.")
        estadoEntry.focus_set()

    # Validar o CPF
    cpf_validador = CPF()
    cpf_formatado = cpf_validador.mask(cpf)

    if not cpf_validador.validate(cpf):
        messagebox.showerror("Cadastro do Conecte SUS", "CPF inválido. Por favor, tente novamente.")
        cpf.focus_set()
        return
    elif cpf_formatado != cpf:
        # Atualizar o valor do campo CPF com o CPF formatado
        cpfValue.set(cpf_formatado)
    
    # Validar a data de nascimento
    try:
        datetime.datetime.strptime(nascimento, '%d/%m/%Y')
    except ValueError:
        messagebox.showerror("Cadastro do Conecte SUS", "Data de nascimento inválida.")
        nascimentoEntry.focus_set()
        return

    # Cria uma string com os valores
    dados = f"Nome do Paciente: {nome}\nNome da Mãe: {mae}\nCEP do Paciente: {cep}\nCPF do Paciente: {cpf}\nData de Nascimento do Paciente: {nascimento}\nCEP: {cep}\nEndereço: {endereco}\nNúmero: {numero}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}"

    # Salvar os dados em um arquivo.txt
    with open("cadastro.txt", "w", encoding = "utf-8") as f:
        f.write(dados)


    # Exibir mensagem de sucesso
    messagebox.showinfo("Cadastro do Conecte SUS", "Cadastro salvo com sucesso.")

    limparCampos("todos")
    nomeEntry.focus_set()

# Botão de envio
Button(text="Salvar", command=salvar_informacoes, font="arial 12", bg="#E6E6FA", fg="black", relief="raised", padx=20, pady=10).grid(row=12, column=3, padx=10, pady=10)

root.mainloop()