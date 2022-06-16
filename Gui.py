import os
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import random
from EncounterGenerator import Generator
import tkinter.font as tkf
# from Controller import Controller
# from configparser import ConfigParser


class app:
    def __init__(self):
        self.window = Tk()
        self.window.title('D&D Encounter Generator')
        self.window.iconphoto(False, PhotoImage(file='images/icon.ico'))

        self.create_menu()

        self.choices = tk.Frame(self.window)        # frame for deciding type of encounter, season, party lvl, etc.
        self.place_variable = StringVar()
        self.season_variable = StringVar()
        self.day_variable = StringVar()
        self.type_variable = StringVar()
        self.level_variable = StringVar()
        self.add_choices()

        self.dices = tk.Frame(self.window)          # frame for rolling dices
        self.modifier_frame = tk.Frame(self.dices)
        self.modifier_label = tk.Label(self.modifier_frame, text='Roll modifier:')
        self.modifier = 0
        self.modifier_string = StringVar()
        self.modifier_string.set('0')
        self.modifier_string.trace_add('write', self.check_modifier)
        self.modifier_entry = tk.Entry(self.modifier_frame, textvariable=self.modifier_string)
        self.result_frame = tk.Frame(self.dices)
        self.dices_rolled = tk.Label(self.result_frame, text='')
        self.dices_rolled_array = [0, 0, 0, 0, 0, 0, 0, 0]
        self.last_roll = list()
        self.result_label = tk.Label(self.result_frame, text='Rolled value:')
        self.result = tk.Label(self.result_frame, text='0')
        self.dice_management_button_frame = tk.Frame(self.dices)
        self.dices_images = []
        self.dice_buttons = []
        self.add_dices()

        self.log_path = ''                          # path to file with logs
        self.log_file = ''

        self.encounter = tk.Frame(self.window)      # frame for encounter text and buttons for managing it
        self.encounter_place = tk.Text(self.encounter)
        self.encounter_text = 'Here will be written the generated encounter'
        self.add_encounter()

        self.encounters = Generator()

        self.window.resizable(False, False)
        self.window.mainloop()

    def file_new(self, *args):
        while True:
            try:
                my_filetypes = [('text files', '.txt')]
                self.log_path = filedialog.askopenfilename(parent=self.window, initialdir=os.getcwd(),
                                                           title="Choose a file to save your encounters:",
                                                           filetypes=my_filetypes)
                self.log_file = open(self.log_path, 'a')
                break
            except FileNotFoundError:
                messagebox.showinfo('No destination file chosen',
                                    'Encounter text could not have been saved\nPlease chose file to save encounters')
                break

    def change_dices_to_black(self, *args):
        self.dices_images.clear()
        for image, i in (
                ('images/black/d2.gif', 0),
                ('images/black/d4.gif', 1),
                ('images/black/d6.gif', 2),
                ('images/black/d8.gif', 3),
                ('images/black/d10.gif', 4),
                ('images/black/d12.gif', 5),
                ('images/black/d20.gif', 6),
                ('images/black/d100.gif', 7)):
            image = os.path.join(os.path.dirname(__file__), image)
            image = tkinter.PhotoImage(file=image)
            self.dices_images.append(image)
            self.dice_buttons[i].configure(image=self.dices_images[i])

    def change_dices_to_crystal(self, *args):
        self.dices_images.clear()
        for image, i in (
                ('images/crystal/d2.gif', 0),
                ('images/crystal/d4.gif', 1),
                ('images/crystal/d6.gif', 2),
                ('images/crystal/d8.gif', 3),
                ('images/crystal/d10.gif', 4),
                ('images/crystal/d12.gif', 5),
                ('images/crystal/d20.gif', 6),
                ('images/crystal/d100.gif', 7)):
            image = os.path.join(os.path.dirname(__file__), image)
            image = tkinter.PhotoImage(file=image)
            self.dices_images.append(image)
            self.dice_buttons[i].configure(image=self.dices_images[i])

    def change_dices_to_metal(self, *args):
        self.dices_images.clear()
        for image, i in (
                ('images/metal/d2.gif', 0),
                ('images/metal/d4.gif', 1),
                ('images/metal/d6.gif', 2),
                ('images/metal/d8.gif', 3),
                ('images/metal/d10.gif', 4),
                ('images/metal/d12.gif', 5),
                ('images/metal/d20.gif', 6),
                ('images/metal/d100.gif', 7)):
            image = os.path.join(os.path.dirname(__file__), image)
            image = tkinter.PhotoImage(file=image)
            self.dices_images.append(image)
            self.dice_buttons[i].configure(image=self.dices_images[i])

    def create_menu(self):
        menubar = tkinter.Menu(self.window)
        self.window["menu"] = menubar

        file_menu = tkinter.Menu(menubar)
        file_menu.add_command(label="New file to encounters", underline=0, command=self.file_new, accelerator="Ctrl+N")
        self.window.bind("<Control-n>", self.file_new)
        menubar.add_cascade(label="File", menu=file_menu, underline=0)

        dice_menu = tkinter.Menu(menubar)
        for label, command, shortcut_text, shortcut in (
                ("Change dice set to black", self.change_dices_to_black, "Ctrl+B", "<Control-b>"),
                ("Change dice set to crystal", self.change_dices_to_crystal, "Ctrl+K", "<Control-k>"),
                ("Change dice set to metal", self.change_dices_to_metal, "Ctrl+M", "<Control-m>")):
            dice_menu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
            self.window.bind(shortcut, command)
        menubar.add_cascade(label="Dices", menu=dice_menu, underline=0)

    def load_encounter(self):
        self.encounter_text = self.encounters.get_encounter(self.place_variable.get(), self.season_variable.get(),
                                                            self.day_variable.get(), self.type_variable.get(),
                                                            self.level_variable.get())
        self.encounter_place.delete(1.0, "end")
        self.encounter_place.insert(1.0, self.encounter_text)

    def add_choices(self):
        # labels informing what data is needed
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

        # arrays of values available for OptionMenus
        PLACE = ['Arctic', 'Coastal', 'Desert', 'Forest', 'Grassland', 'Hill', 'Mountain', 'Ocean', 'Swamp',
                 'Town', 'Underdark', 'Underwater']
        SEASON = ['Spring', 'Summer', 'Fall', 'Winter']
        PART_OF_THE_DAY = ['Morning', 'Afternoon', 'Evening', 'Night']
        ENCOUNTER_TYPE = ['Fight', 'Gathering resources', 'Meeting', 'Hunting', 'Random']

        # variables needed in self.load_encounter()
        self.place_variable.set(PLACE[0])

        self.season_variable.set(SEASON[0])

        self.day_variable.set(PART_OF_THE_DAY[0])

        self.type_variable.set(ENCOUNTER_TYPE[0])

        self.level_variable.set('1')

        # OptionMenus
        dropdown = OptionMenu(self.choices, self.place_variable, *PLACE)
        dropdown.grid(row=0, column=1)

        dropdown = OptionMenu(self.choices, self.season_variable, *SEASON)
        dropdown.grid(row=1, column=1)

        dropdown = OptionMenu(self.choices, self.day_variable, *PART_OF_THE_DAY)
        dropdown.grid(row=2, column=1)

        dropdown = OptionMenu(self.choices, self.type_variable, *ENCOUNTER_TYPE)
        dropdown.grid(row=3, column=1)

        dropdown = OptionMenu(self.choices, self.level_variable, *range(1, 21))
        dropdown.grid(row=4, column=1)

        # button for drawing random encounters
        button = tk.Button(self.choices, command=self.load_encounter, text='Show random encounter')
        button.grid(row=5, column=0, columnspan=2)
        button.configure(width=37)

        self.choices.grid(row=0, column=0, sticky=tkinter.NSEW)

    def check_modifier(self, *args):
        entry = self.modifier_entry.get()
        if entry.isnumeric() or entry == '' or (entry[0] == '-' and entry[1:].isnumeric()):
            self.result['text'] = str(int(self.result['text']) - self.modifier)
            if entry == '':
                self.modifier = 0
            else:
                self.modifier = int(entry)
            self.result['text'] = str(int(self.result['text']) + self.modifier)
        elif entry == '-':
            pass
        else:
            messagebox.showinfo('Written modifier is improper',
                                'Please write modifier that is a number')

    def roll_d2(self):
        rolled = random.randint(1, 2)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((0, rolled))
        self.dices_rolled_array[0] += 1
        self.format_dice_rolled()

    def roll_d4(self):
        rolled = random.randint(1, 4)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((1, rolled))
        self.dices_rolled_array[1] += 1
        self.format_dice_rolled()

    def roll_d6(self):
        rolled = random.randint(1, 6)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((2, rolled))
        self.dices_rolled_array[2] += 1
        self.format_dice_rolled()

    def roll_d8(self):
        rolled = random.randint(1, 8)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((3, rolled))
        self.dices_rolled_array[3] += 1
        self.format_dice_rolled()

    def roll_d10(self):
        rolled = random.randint(1, 10)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((4, rolled))
        self.dices_rolled_array[4] += 1
        self.format_dice_rolled()

    def roll_d12(self):
        rolled = random.randint(1, 12)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((5, rolled))
        self.dices_rolled_array[5] += 1
        self.format_dice_rolled()

    def roll_d20(self):
        rolled = random.randint(1, 20)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((6, rolled))
        self.dices_rolled_array[6] += 1
        self.format_dice_rolled()

    def roll_d100(self):
        rolled = random.randint(1, 100)
        self.result['text'] = str(int(self.result['text']) + rolled)
        self.last_roll.append((7, rolled))
        self.dices_rolled_array[7] += 1
        self.format_dice_rolled()

    def roll_reset(self):
        self.result['text'] = str(self.modifier)
        self.dices_rolled_array = [0, 0, 0, 0, 0, 0, 0, 0]
        self.last_roll = list()
        self.format_dice_rolled()

    def re_roll(self):
        self.result['text'] = str(self.modifier)
        for i in range(len(self.last_roll)):
            dice = self.last_roll[i][0]
            if dice == 0:
                roll = random.randint(1, 2)
            elif dice == 1:
                roll = random.randint(1, 4)
            elif dice == 2:
                roll = random.randint(1, 6)
            elif dice == 3:
                roll = random.randint(1, 8)
            elif dice == 4:
                roll = random.randint(1, 10)
            elif dice == 5:
                roll = random.randint(1, 12)
            elif dice == 6:
                roll = random.randint(1, 20)
            else:
                roll = random.randint(1, 100)
            self.last_roll[i] = (dice, roll)
            self.result['text'] = str(int(self.result['text']) + roll)

    def unroll_last_roll(self):
        if len(self.last_roll) > 0:
            self.dices_rolled_array[self.last_roll[len(self.last_roll)-1][0]] -= 1
            self.result['text'] = str(int(self.result['text']) - self.last_roll[len(self.last_roll)-1][1])
            self.last_roll.pop()
            self.format_dice_rolled()
        else:
            messagebox.showinfo('No previous dice rolled',
                                'Program can\'t unroll any more dice')

    def format_dice_rolled(self):
        self.dices_rolled['text'] = ''
        if self.dices_rolled_array[0] > 0:  # formatting for d2s
            self.dices_rolled['text'] += f'{self.dices_rolled_array[0]}d2'
        if self.dices_rolled_array[1] > 0:  # formatting for d6s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[1]}d4'
        if self.dices_rolled_array[2] > 0:  # formatting for d8s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[2]}d6'
        if self.dices_rolled_array[3] > 0:  # formatting for d10s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[3]}d8'
        if self.dices_rolled_array[4] > 0:  # formatting for d12s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[4]}d10'
        if self.dices_rolled_array[5] > 0:  # formatting for d20s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[5]}d12'
        if self.dices_rolled_array[6] > 0:  # formatting for d12s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[6]}d20'
        if self.dices_rolled_array[7] > 0:  # formatting for d100s
            if self.dices_rolled['text'] != '':
                self.dices_rolled['text'] += ' + '
            self.dices_rolled['text'] += f'{self.dices_rolled_array[7]}d100'

    def add_dices(self):
        # place for roll modifier
        self.modifier_frame.grid(row=0, column=1)
        self.modifier_label.grid(row=0, column=0)
        self.modifier_entry.grid(row=1, column=0)

        # amount of different dices rolled and total of the rolled dices
        self.result_frame.grid(row=1, column=1, rowspan=2)
        self.dices_rolled.grid(row=0, column=0)
        self.dices_rolled.configure(width=45)
        self.result_label.grid(row=1, column=0)
        self.result.grid(row=2, column=0)

        # adding buttons for rolling dices
        for image, command in (
                ('images/black/d2.gif', self.roll_d2),
                ('images/black/d4.gif', self.roll_d4),
                ('images/black/d6.gif', self.roll_d6),
                ('images/black/d8.gif', self.roll_d8),
                ('images/black/d10.gif', self.roll_d10),
                ('images/black/d12.gif', self.roll_d12),
                ('images/black/d20.gif', self.roll_d20),
                ('images/black/d100.gif', self.roll_d100)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.dices_images.append(image)
                self.dice_buttons.append(tk.Button(self.dices, image=image, command=command))
                self.dice_buttons[len(self.dices_images) - 1].grid(column=int(int(len(self.dices_images) - 1)/4)*2,
                                                                   row=(len(self.dices_images) - 1) % 4)
            except tkinter.TclError as err:
                print(err)

            self.dice_management_button_frame.grid(row=3, column=1)

            button = tk.Button(self.dice_management_button_frame, command=self.roll_reset, text='Reset rolls')
            button.grid(row=0, column=0)

            button = tk.Button(self.dice_management_button_frame, command=self.re_roll, text='Re roll dices')
            button.grid(row=1, column=0)

            button = tk.Button(self.dice_management_button_frame, command=self.unroll_last_roll,
                               text='Unroll the last roll')
            button.grid(row=2, column=0)

        self.dices.grid(row=0, column=1, sticky=tkinter.NSEW)

    def show_original(self):
        self.encounter_place.delete(1.0, "end")
        self.encounter_place.insert(1.0, self.encounter_text)

    def save_to_file(self):
        if str(self.encounter_place.get("1.0", END)) == 'Here will be written the generated encounter':
            if self.log_path == '':
                self.file_new(None)

            if self.log_path != '':
                self.log_file = open(self.log_path, 'a')
                self.log_file.write(self.encounter_place.get("1.0", END))
                self.log_file.write('\n-----------------------------\n')
                self.log_file.close()
        else:
            messagebox.showinfo('No encounter generated', 'Generate an encounter or write something on your own')

    def add_encounter(self):
        # place for random encounter text
        self.encounter_place.grid(row=0, column=0, rowspan=2)
        self.encounter_place.configure(height=10, width=70, font=tkf.Font(family="Arial", size=12, weight="bold",
                                                                          slant="italic"))
        self.encounter_place.insert(1.0, 'Here will be written the generated encounter')

        button = tk.Button(self.encounter, command=self.show_original, text='Show original encounter')
        button.grid(row=0, column=1)
        button.configure(width=20)

        button = tk.Button(self.encounter, command=self.save_to_file, text='Save encounter to file')
        button.grid(row=1, column=1)
        button.configure(width=20)

        self.encounter.grid(row=1, column=0, columnspan=2, sticky=tkinter.NSEW)
