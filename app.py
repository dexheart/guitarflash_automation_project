import pyautogui
from time import sleep
import threading
import keyboard

# Link do jogo - https://guitarflash.com/?lg=pt

green_pressed = False
red_pressed = False
yellow_pressed = False

def checkColor(location, color, key, status_flag):
    global green_pressed, red_pressed, yellow_pressed
    if pyautogui.pixelMatchesColor(location[0], location[1], color):
        if not status_flag:  # Se a tecla ainda não foi pressionada
            pyautogui.press(key)
            return True  # Atualizar o status de que a tecla foi pressionada
            
    else:
        return False  # Atualizar o status de que a cor não está ativa

# Loop principal
while keyboard.is_pressed('x') == False:
    # Verificar a cor verde
    green_pressed = checkColor((1249, 806), (0, 152, 0), 'a', green_pressed)
    
    # Verificar a cor vermelha
    red_pressed = checkColor((1338, 810), (255, 0, 0), 's', red_pressed)
    
    # Verificar a cor amarela
    yellow_pressed = checkColor((1426, 810), (244, 244, 2), 'j', yellow_pressed)

