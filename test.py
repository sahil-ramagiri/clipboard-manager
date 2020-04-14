from pynput import keyboard, mouse
import time

def on_click(x, y, button, pressed):
    print(button.name == 'right')
    return True

def on_press(key):
    print(key)
    print(dir(key))
    try:
        if key.name == 'ctrl_l':
            print("ctrl pressed")
    except:
        pass
    if key == keyboard.Key.insert:
        for l in listeners:
            l.stop()
        return False

def main():

    listeners = []

    listeners.append(keyboard.Listener(on_press=on_press))
    listeners.append(mouse.Listener(on_click=on_click))
    for l in listeners:
        l.start()

    a = 4
    while a < 5:
        print("sleeping")
        time.sleep(10)
        a = a+1

if __name__ == '__main__':
    main()
