import os
import tkinter
from tkinter import *
# from tkinter import messagebox, filedialog
# from Controller import Controller
# import datetime as dt
import tkinter as tk
# from configparser import ConfigParser
import random


class app:
    def __init__(self):
        self.window = Tk()
        self.window.title('Welcome to D&D encounter generator')

        self.dices = tk.Frame(self.window)  # frame for rolling dices
        self.add_dices()

        self.choices = tk.Frame(self.window)  # frame for deciding type of encounter, season, party lvl, etc.
        self.add_choices()

        self.encounter = tk.Frame(self.window)  # frame for encounter text and buttons for managing it
        self.add_encounter()

        self.window.mainloop()

    def roll_d4(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 4))
        self.dices_rolled_array[0] += 1
        self.format_dice_rolled()

    def roll_d6(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 6))
        self.dices_rolled_array[1] += 1
        self.format_dice_rolled()

    def roll_d8(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 8))
        self.dices_rolled_array[2] += 1
        self.format_dice_rolled()

    def roll_d10(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 10))
        self.dices_rolled_array[3] += 1
        self.format_dice_rolled()

    def roll_d12(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 12))
        self.dices_rolled_array[4] += 1
        self.format_dice_rolled()

    def roll_d20(self):
        # temp = int(self.result["text"])
        # temp+=random.randint(1, 20)
        # self.result["text"]=str(temp)
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 20))
        self.dices_rolled_array[5] += 1
        self.format_dice_rolled()

    def roll_reset(self):
        self.result['text'] = '0'
        self.dices_rolled_array = [0, 0, 0, 0, 0, 0]
        self.format_dice_rolled()

    def format_dice_rolled(self):
        self.dices_rolled['text'] = ''
        if self.dices_rolled_array[0] > 0:  # formatting for d4s
            self.dices_rolled['text'] += '{}d4'.format(self.dices_rolled_array[0])
        if self.dices_rolled_array[1] > 0:  # formatting for d6s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += '{}d6'.format(self.dices_rolled_array[1])
        if self.dices_rolled_array[2] > 0:  # formatting for d8s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += '{}d8'.format(self.dices_rolled_array[2])
        if self.dices_rolled_array[3] > 0:  # formatting for d10s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += '{}d10'.format(self.dices_rolled_array[3])
        if self.dices_rolled_array[4] > 0:  # formatting for d12s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += '{}d12'.format(self.dices_rolled_array[4])
        if self.dices_rolled_array[5] > 0:  # formatting for d20s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += '{}d20'.format(self.dices_rolled_array[5])

    def add_dices(self):
        self.dices_rolled = tk.Label(self.dices, text='')  # amount of different dices rolled
        self.dices_rolled.grid(row=1, column=1)
        self.dices_rolled_array = [0, 0, 0, 0, 0, 0]

        self.result = tk.Label(self.dices, text='0')  # total of the rolled dices
        self.result.grid(row=2, column=1)

        self.dices_images = []
        for image, command in (
                ('images/d4.gif', self.roll_d4),
                ('images/d6.gif', self.roll_d6),
                ('images/d8.gif', self.roll_d8),
                ('images/d10.gif', self.roll_d10),
                ('images/d12.gif', self.roll_d12),
                ('images/d20.gif', self.roll_d20)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.dices_images.append(image)
                button = tk.Button(self.dices, image=image, command=command)
                button.grid(column=0, row=len(self.dices_images) - 1)
            except tkinter.TclError as err:
                print(err)

            button = tk.Button(self.dices, command=self.roll_reset, text='Reset rolls')
            button.grid(row=3, column=1)

        self.dices.grid(row=0, column=1, sticky=tkinter.NSEW)

    def load_encounter(selfself):
        pass

    def add_choices(self):
        label = tk.Label(self.choices, text='Location:')
        label.grid(row=0, column=0)

        label = tk.Label(self.choices, text='Season:')
        label.grid(row=1, column=0)

        label = tk.Label(self.choices, text='Part of the day:')
        label.grid(row=2, column=0)

        label = tk.Label(self.choices, text='Type of encounter:')
        label.grid(row=3, column=0)

        label = tk.Label(self.choices, text='Average party level:')
        label.grid(row=4, column=0)

        PLACE = ['Arctic', 'Costal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Ocean', 'Swamp', 'Town', 'Underdark', 'Underwater']
        SEASON = ['Spring', 'Summer', 'Fall', 'Winter']
        PART_OF_THE_DAY = ['Morning', 'Afternoon', 'Evening', 'Night']
        ENCOUNTER_TYPE = ['Fight', 'Gathering resources']

        self.place_variable = StringVar()
        self.place_variable.set(PLACE[0])

        self.season_variable = StringVar()
        self.season_variable.set(SEASON[0])

        self.day_variable = StringVar()
        self.day_variable.set(PART_OF_THE_DAY[0])

        self.type_variable = StringVar()
        self.type_variable.set(ENCOUNTER_TYPE[0])

        dropdown = OptionMenu(self.choices, self.place_variable, *PLACE)
        dropdown.grid(row=0, column=1)

        dropdown = OptionMenu(self.choices, self.season_variable, *SEASON)
        dropdown.grid(row=1, column=1)

        dropdown = OptionMenu(self.choices, self.day_variable, *PART_OF_THE_DAY)
        dropdown.grid(row=2, column=1)

        dropdown = OptionMenu(self.choices, self.type_variable, *ENCOUNTER_TYPE)
        dropdown.grid(row=3, column=1)

        self.average_level = tk.Entry(self.choices)
        self.average_level.grid(row=4, column=1)

        button = tk.Button(self.choices, command=self.load_encounter, text='Show random encounter')
        button.grid(row=5, column=0, columnspan=2)

        self.choices.grid(row=0, column=0, sticky=tkinter.NSEW)

    def save_to_file(self):
        print(self.place_variable.get(), self.season_variable.get(), self.day_variable.get(), self.type_variable.get())

    def show_original(self):
        self.encounter_space.delete(0, tk.END)
        self.encounter_space.insert(0, self.encounter_text)

    def new_idea(self):
        pass

    def add_encounter(self):
        self.encounter_text = ''
        self.encounter_space = tk.Entry(self.encounter)
        self.encounter_space.grid(row=0, column=0, rowspan=3)

        button = tk.Button(self.encounter, command=self.show_original, text='Show original encounter')
        button.grid(row=0, column=1)

        button = tk.Button(self.encounter, command=self.save_to_file, text='Save encounter to file')
        button.grid(row=1, column=1)

        button = tk.Button(self.encounter, command=self.new_idea, text='Idea for new encounter')
        button.grid(row=2, column=1)

        self.encounter.grid(row=1, column=0, columnspan=2, sticky=tkinter.NSEW)