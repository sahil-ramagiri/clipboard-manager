from pynput import keyboard, mouse
import pyperclip
import time
import json

def clear_db(arr = None, keep = None):
    if arr is None and keep is None:
        db = {'history': []}
    elif arr:
        for i in arr:
            db['history'].pop(i)
    else:
        db['history'] = db['history'][-last:]

    with open("db.json", 'w') as file:
        json.dump(db, file, indent = 2)

def copy_last(l):
    s = '\n'.join(db['history'][-l]['text'])
    pyperclip.copy(s)

def copy_handler(t):
    if time.time() - t < 0.1:
        time.sleep(0.1)
        clip = pyperclip.paste().split('\n')
        empty = len(db['history']) == 0

        if empty or db['history'][-1]['text'] != clip:
            db['history'].append({'text':clip})
            with open("db.json", 'w') as file:
                json.dump(db, file, indent = 2)


def on_click(x, y, button, pressed):
    if button.name == 'right':
        copy_handler(time.time())
    return True

def on_press(key):
    try:
        if key.name == 'ctrl_l':
            copy_handler(time.time())

        if key.name == 'insert':
            for l in listeners:
                l.stop()
            return False
    except AttributeError:
        pass
    return True

db = None
listeners = []

def main():
    global db
    try:
        with open("db.json", 'r') as file:
            db = json.load(file)
        print("db connected")
    except:
        clear_db()
        print("db created")

    listeners.append(keyboard.Listener(on_press=on_press))
    listeners.append(mouse.Listener(on_click=on_click))

    for l in listeners:
        l.start()

    while True:
        i = input('>')
        if i == 'exit':
            break

        parsed = i.split()
        n = int(parsed[1]) if len(parsed) > 1 else None
        if parsed[0] == 'clear':
            clear_db() if n is None else clear_db(last = n)
        if parsed[0] == 'last':
            copy_last(2) if n is None else copy_last(n+1)

if __name__ == '__main__':
    main()
