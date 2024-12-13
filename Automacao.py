import pyautogui
import time 

pyautogui.PAUSE = 0.3

# pegar posições do mouse e da tela 
print(pyautogui.position())
print(pyautogui.size())

#funções do mouse
time.sleep(5)

#pyautogui.moveTo(x=498, y=967, duration=1)
#pyautogui.click(x=498, y=967)
#pyautogui.scroll(-200) # numero negativo - scroll para baixo 


#funções de teclado
pyautogui.write("Teste")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")