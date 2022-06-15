import os
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import random
from EncounterGenerator import Generator
# from tkinter import messagebox, filedialog
# from Controller import Controller
# from configparser import ConfigParser


class app:
    def __init__(self):
        self.window = Tk()
        self.window.title('D&D Encounter Generator')

        self.create_menu()

        self.choices = tk.Frame(self.window)        # frame for deciding type of encounter, season, party lvl, etc.
        self.place_variable = StringVar()
        self.season_variable = StringVar()
        self.day_variable = StringVar()
        self.type_variable = StringVar()
        self.level_variable = StringVar()
        self.add_choices()

        self.dices = tk.Frame(self.window)          # frame for rolling dices
        self.dices_rolled = tk.Label(self.dices, text='')
        self.dices_rolled_array = [0, 0, 0, 0, 0, 0, 0, 0]
        self.result = tk.Label(self.dices, text='0')
        self.dices_images = []
        self.dice_buttons = []
        self.add_dices()

        self.log_path = ''                          # path to file with logs

        self.encounter = tk.Frame(self.window)      # frame for encounter text and buttons for managing it
        self.encounter_place = tk.Text(self.encounter)
        self.encounter_text = ''
        self.add_encounter()

        self.encounters = Generator()

        self.window.resizable(False, False)
        self.window.mainloop()

    def file_new(self):
        while True:
            try:
                my_filetypes = [('text files', '.txt')]
                answer = filedialog.askopenfilename(parent=self.window, initialdir=os.getcwd(),
                                                    title="Choose a file to save your encounters:",
                                                    filetypes=my_filetypes)
                print(answer)
                self.log_path = open(answer, 'a')
                break
            except FileNotFoundError:
                messagebox.showinfo('No destination file chosen',
                                    'Encounter text could not have been saved\nPlease chose file to save encounters')
                break

    def change_dices_to_black(self):
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

    def change_dices_to_crystal(self):
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

    def change_dices_to_metal(self):
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
        for label, command, shortcut_text, shortcut in (
                ("New file to encounters", self.file_new, "Ctrl+N", "<Control-n>"),
                ("Change dice set to black", self.change_dices_to_black, "Ctrl+B", "<Control-b>"),
                ("Change dice set to crystal", self.change_dices_to_crystal, "Ctrl+K", "<Control-k>"),
                ("Change dice set to metal", self.change_dices_to_metal, "Ctrl+M", "<Control-m>")):
            file_menu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
            self.window.bind(shortcut, command)
        menubar.add_cascade(label="File", menu=file_menu, underline=0)

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

    def roll_d2(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 2))
        self.dices_rolled_array[0] += 1
        self.format_dice_rolled()

    def roll_d4(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 4))
        self.dices_rolled_array[1] += 1
        self.format_dice_rolled()

    def roll_d6(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 6))
        self.dices_rolled_array[2] += 1
        self.format_dice_rolled()

    def roll_d8(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 8))
        self.dices_rolled_array[3] += 1
        self.format_dice_rolled()

    def roll_d10(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 10))
        self.dices_rolled_array[4] += 1
        self.format_dice_rolled()

    def roll_d12(self):
        self.result['text'] = str(int(self.result['text'])+random.randint(1, 12))
        self.dices_rolled_array[5] += 1
        self.format_dice_rolled()

    def roll_d20(self):
        self.result['text'] = str(int(self.result['text']) + random.randint(1, 20))
        self.dices_rolled_array[6] += 1
        self.format_dice_rolled()

    def roll_d100(self):
        self.result['text'] = str(int(self.result['text']) + random.randint(1, 100))
        self.dices_rolled_array[7] += 1
        self.format_dice_rolled()

    def roll_reset(self):
        self.result['text'] = '0'
        self.dices_rolled_array = [0, 0, 0, 0, 0, 0, 0, 0]
        self.format_dice_rolled()

    def re_roll(self):
        self.result['text'] = '0'
        for i in range(self.dices_rolled_array[0]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 2))
        for i in range(self.dices_rolled_array[1]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 4))
        for i in range(self.dices_rolled_array[2]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 6))
        for i in range(self.dices_rolled_array[3]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 8))
        for i in range(self.dices_rolled_array[4]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 10))
        for i in range(self.dices_rolled_array[5]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 12))
        for i in range(self.dices_rolled_array[6]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 20))
        for i in range(self.dices_rolled_array[7]):
            self.result['text'] = str(int(self.result['text']) + random.randint(1, 100))

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
        # amount of different dices rolled
        self.dices_rolled.grid(row=1, column=1)
        self.dices_rolled.configure(width=45)

        # total of the rolled dices
        self.result.grid(row=2, column=1)

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

            button = tk.Button(self.dices, command=self.roll_reset, text='Reset rolls')
            button.grid(row=3, column=1)

            button = tk.Button(self.dices, command=self.re_roll, text='Re roll dices')
            button.grid(row=4, column=1)

        self.dices.grid(row=0, column=1, sticky=tkinter.NSEW)

    def show_original(self):
        self.encounter_place.delete(1.0, "end")
        self.encounter_place.insert(1.0, self.encounter_text)

    def save_to_file(self):
        if self.encounter_text != 'Here will be written the generated encounter':
            if self.log_path == '':
                self.file_new()

            if self.log_path != '':
                self.log_path.write(f'{self.encounter_place.get("1.0",END)}\n')
                self.log_path.write('-----------------------------\n')
        else:
            messagebox.showinfo('No encounter loaded yet',
                                'Please generate encounter before saving it to the file')

    def add_encounter(self):
        # place for random encounter text
        self.encounter_place.grid(row=0, column=0, rowspan=2)
        self.encounter_place.configure(height=10, width=70)

        button = tk.Button(self.encounter, command=self.show_original, text='Show original encounter')
        button.grid(row=0, column=1)
        button.configure(width=20)

        button = tk.Button(self.encounter, command=self.save_to_file, text='Save encounter to file')
        button.grid(row=1, column=1)
        button.configure(width=20)

        self.encounter.grid(row=1, column=0, columnspan=2, sticky=tkinter.NSEW)
