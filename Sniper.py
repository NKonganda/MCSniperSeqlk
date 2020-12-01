# import modules
import requests, time, os, sys
from tkinter import *
from PIL import ImageTk, Image, ImageSequence
import datetime as dt
from datetime import datetime

# User-Agent
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'


# Gui
class GUI:
    def __init__(self, window):

        self.we = Button(window, text='Block Method', command=GUI.buildtoken)
        self.we.place(x=90, y=120)

        self.insert_info = Button(window, text='Namechange Method', command=GUI.buildname)
        self.insert_info.place(x=200, y=120)

        self.sm = Button(window, text='Quit Program', command=sys.exit)
        self.sm.place(x=155, y=300)

    # Build the menu
    def buildname():
        global target, bearer_key, username, password, target_button, bearer_key_button, username_button, password_button, insert_info, availability_time, availability, run_before, run_before_button

        try:
            GUI.removethis1()
        except Exception:
            pass
        try:
            GUI.removethis2()
        except Exception:
            pass
        try:
            GUI.removebegin()
        except Exception:
            pass
        target = Label(window, text='target')
        target.place(x=10, y=180)
        target_button = Entry(window, bd=5)
        target_button.place(x=10, y=200)

        bearer_key = Label(window, text='Bearer Key')
        bearer_key.place(x=250, y=180)
        bearer_key_button = Entry(window, bd=5)
        bearer_key_button.place(x=250, y=200)

        username = Label(window, text='Username')
        username.place(x=10, y=260)
        username_button = Entry(window, bd=5)
        username_button.place(x=10, y=280)

        password = Label(window, text='Password')
        password.place(x=250, y=260)
        password_button = Entry(window, bd=5)
        password_button.place(x=250, y=280)

        availability = Label(window, text='Time of Availability')
        availability.place(x=10, y=340)
        availability_time = Entry(window, bd=5)
        availability_time.place(x=10, y=360)
        availability_time.insert(0, dt.datetime.now().strftime("%H:%M:%S"))

        run_before = Label(window, text='Run Before Release Time')
        run_before.place(x=250, y=340)
        run_before_button = Entry(window, bd=5)
        run_before_button.place(x=250, y=360)
        run_before_button.insert(0, '.935')

        insert_info = Button(window, text='Insert Info', command=GUI.insertinfo)
        insert_info.place(x=165, y=200)

    # Build the menu
    def buildtoken():
        global target, target_button, bearer_key, bearer_key_button, insert_info, availability, availability_time, run_before_button, run_before

        try:
            GUI.removethis1()
        except Exception:
            pass
        try:
            GUI.removethis2()
        except Exception:
            pass
        try:
            GUI.removebegin()
        except Exception:
            pass
        target = Label(window, text='target')
        target.place(x=10, y=180)
        target_button = Entry(window, bd=5)
        target_button.place(x=10, y=200)

        bearer_key = Label(window, text='Bearer Key')
        bearer_key.place(x=250, y=180)
        bearer_key_button = Entry(window, bd=5)
        bearer_key_button.place(x=250, y=200)

        availability = Label(window, text='Time of Availability')
        availability.place(x=10, y=340)
        availability_time = Entry(window, bd=5)
        availability_time.place(x=10, y=360)
        availability_time.insert(0, dt.datetime.now().strftime("%H:%M:%S"))

        run_before = Label(window, text='Run Before Release Time')
        run_before.place(x=250, y=340)
        run_before_button = Entry(window, bd=5)
        run_before_button.place(x=250, y=360)
        run_before_button.insert(0, '.935')

        insert_info = Button(window, text='Insert Info', command=GUI.insertinfotoken)
        insert_info.place(x=165, y=200)

    # Removes menu of NameChange Method
    def removethis1():
        target.destroy()
        target_button.destroy()
        bearer_key.destroy()
        bearer_key_button.destroy()
        username.destroy()
        username_button.destroy()
        password.destroy()
        password_button.destroy()
        insert_info.destroy()
        availability.destroy()
        availability_time.destroy()
        run_before.destroy()
        run_before_button.destroy()

    # Removes menu of Blank Method
    def removethis2():
        target.destroy()
        target_button.destroy()
        insert_info.destroy()
        bearer_key_button.destroy()
        bearer_key.destroy()
        availability_time.destroy()
        availability.destroy()
        run_before_button.destroy()
        run_before.destroy()

    # Removes the begin button
    def removebegin():
        we.destroy()

    # Updates info
    def insertinfo():
        global username, password, profileid, auth, we

        # Inputs
        username = target_button.get()  # target

        toke = bearer_key_button.get()  # Bearer Key

        try:
            ff = username_button.get()
            us = req = requests.get(f'https://api.mojang.com/user/profile/agent/minecraft/name/{ff}').json()
            profileid = us['id']  # Profile ID / Trimmed UUID
        except Exception:
            print("That username that doesn't exist!")
            profileid = ''
        password = password_button.get()  # Password

        auth = 'Bearer ' + toke

        # Don't have empty lines
        if username == '':
            print('Missing target Username!')
        elif toke == '':
            print('Missing Bearer Key!')
        elif profileid == '':
            print('Username!')
        elif password == '':
            print('Missing Password!')
        else:
            we = Button(window, text='Begin', command=GUI.name)
            we.place(x=175, y=250)

    # Updates info
    def insertinfotoken():
        global target, auth, we

        # Inputs
        target = target_button.get()  # target

        token = bearer_key_button.get()  # Bearer Key

        auth = 'Bearer ' + token

        # Don't have empty lines
        if target == '':
            print('Missing target Username!')
        elif token == '':
            print('Missing Bearer Key!')
        else:
            we = Button(window, text='Begin', command=GUI.block)
            we.place(x=175, y=250)

    # Change the name
    def name():
        try:
            TimeOfAvailability = availability_time.get()
            h = TimeOfAvailability.split(':')[0]
            m = TimeOfAvailability.split(':')[1]
            s = TimeOfAvailability.split(':')[2]
            if m == '00' and s == '00':
                if int(h) < 11:
                    hh = int(h) - 1
                    hh = '0' + str(hh)
                else:
                    hh = int(h) - 1
                    hh = str(hh)
                date = hh + ':59:59'
            elif s == '00':
                if int(m) < 11:
                    mm = int(m) - 1
                    mm = '0' + str(mm)
                else:
                    mm = int(m) - 1
                    mm = str(mm)
                date = h + ':' + mm + ':59'

            else:
                if int(s) < 11:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + '0' + str(ss)
                else:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + str(ss)

            while True:
                # Grab the time right now
                now = dt.datetime.now().strftime("%H:%M:%S")

                if now == date:
                    if '.' in run_before_button.get():
                        time.sleep(float(run_before_button.get()))
                    else:
                        time.sleep(int(run_before_button.get()))
                    # Change the username
                    for i in range(3):
                        s = requests.post(f'https://api.mojang.com/user/profile/{profileid}/name',
                                          headers={'Authorization': auth, 'User-Agent': useragent},
                                          json={"name": username, "password": password})
                        if s.status_code == 204:
                            print(f'{username} is now yours!')
                            break
                        print(s.status_code)
                        print(s.text)
                    break

        except Exception as e:
            print(e)

    # Block the name
    def block():
        try:
            TimeOfAvailability = availability_time.get()
            h = TimeOfAvailability.split(':')[0]
            m = TimeOfAvailability.split(':')[1]
            s = TimeOfAvailability.split(':')[2]
            if m == '00' and s == '00':
                if int(h) < 11:
                    hh = int(h) - 1
                    hh = '0' + str(hh)
                else:
                    hh = int(h) - 1
                    hh = str(hh)
                date = hh + ':59:59'
            elif s == '00':
                if int(m) < 11:
                    mm = int(m) - 1
                    mm = '0' + str(mm)
                else:
                    mm = int(m) - 1
                    mm = str(mm)
                date = h + ':' + mm + ':59'

            else:
                if int(s) < 11:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + '0' + str(ss)
                else:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + str(ss)
            while True:
                now = dt.datetime.now().strftime("%H:%M:%S")
                if now == date:
                    if '.' in run_before_button.get():
                        time.sleep(float(run_before_button.get()))
                    else:
                        time.sleep(int(run_before_button.get()))
                    for i in range(3):
                        r = requests.put(f'https://api.mojang.com/user/profile/agent/minecraft/name/{target}',
                                         headers={'Authorization': auth, 'User-Agent': useragent})
                        if r.status_code == 204:
                            print(f'{target} is now yours!')
                            break
                        print(r.status_code)
                        print(r.text)
                    break
        except Exception as e:
            print(e)


# Define parent
window = Tk()

# Define title
window.title('Minecraft NameSniper')

# Define size of
window.geometry("400x400")
window.resizable(0, 0)

G2 = Label(window, text="Seqlk's Sniper", font=50)
G2.place(x=150, y=35)
# Run Program
root = GUI(window)
window.mainloop()
