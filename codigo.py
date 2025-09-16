# Passo a passo do projeto
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa -> https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)


# Passo 2: Fazer login

#colocar o email
pyautogui.press("tab")
pyautogui.write("lucas@gmail.com")

#colocar a senha
pyautogui.press("tab")
pyautogui.write("senha123")

#clicar no botão de login
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


# Passo 3: Importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv(r"c:\Users\ZETEC\Desktop\vscode hmk\Hashtag\aula1\produtos.csv")

print(tabela)   
# Passo 4: Cadastrar um produto
for linha in tabela.index: #cada linha da tabela
    pyautogui.click(x=747, y=369)

    codigo = tabela.loc[linha, "codigo"] # pega o código da linha11.0
    pyautogui.write(codigo) # escreve no sistema
    pyautogui.press("tab") # aperta tab pra ir pro próximo campo

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) # tem que ser string
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan": # se tiver alguma observação
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll("1000")

# Passo 5: Repetir o processo de cadastro até o fim
