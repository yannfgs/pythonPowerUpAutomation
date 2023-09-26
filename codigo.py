# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui # importa a biblioteca "pyautogui" # pip install pyautogui
import time # importa a biblioteca "time"

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinacao de teclas)
pyautogui.PAUSE = 0.4

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=737, y=366) # button="left" # clicks=1 # comando para se obter a posicao no arquivo auxiliar.py
pyautogui.write("fgs.yann@gmail.com")

pyautogui.press("tab")
pyautogui.write("Macallan18@!1135")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2) # aguarda x segundos para a pagina carregar

# Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas # nas tabelas do pandas, usamos colhetes [] # pandas analisa as tabelas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index: # no python, index sao as linhas da tabela # se fosse cada coluna, `for coluna in tabela.column`
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=729, y=248)
    

    codigo = tabela.loc[linha, "codigo"] 
   # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        
    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000) # numeros positivos fazem scroll para cima; enquanto numeros negativos fazem scroll para baixo # testar numeros


# para pausar a automacao, colocar o mouse no canto superior esquerdo da tela

# Passo 5: Repetir o cadastro para todos os produtos