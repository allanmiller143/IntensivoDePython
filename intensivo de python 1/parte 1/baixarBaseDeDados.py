import webbrowser
import pyautogui
import time

pyautogui.PAUSE = 1

def baixarBaseDeDados():
    # passo 1: acessar o sistema da empresa
    webbrowser.open('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
    time.sleep(2)
    
    # passo 2: fazer login
    pyautogui.press("tab")
    pyautogui.write("millerallan17@gmail.com")
    pyautogui.press("tab")
    pyautogui.write("32172528")
    pyautogui.press("tab")
    pyautogui.press("enter")

    # passo 3: baixar a base de dados
    time.sleep(2)
    pyautogui.moveTo(371, 310)
    pyautogui.click(button='right')
    pyautogui.click(x=486, y=565)

    time.sleep(5)
