#Codigo para um Robô que acessa o Google Chrome e realiza uma pesquisa ou entra em um site especifico 
# utilizando o mouse e clicando nas cordenadas para realizar a função completa.

import pyautogui, time, keyboard

print("Robô sendo iniciado...")
time.sleep(4)
pyautogui.press('win')

time.sleep(0.5)
pyautogui.write("chrome")

time.sleep(0.5)
pyautogui.press('enter')

time.sleep(0.5)
pyautogui.write("o que é adjetivo?")
pyautogui.press('enter')

print("Robô Desligado")