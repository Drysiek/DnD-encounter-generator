import pandas as pd
import random
import os
import sys


def resource_path(relative_path):
    # function needed for auto-py-to-exe
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Generator:
    def __init__(self):
        # get hunting data
        df = pd.read_csv(resource_path('data/Hunting.csv'), sep=';')
        self.hunt = dict()
        for i in range(len(df)):
            place = df['Terrain'][i].split(', ')
            for j in place:
                if self.hunt.get(j) is None:
                    self.hunt.update({j: list()})
                self.hunt[j].append((df['Beast'][i], df['Size'][i], df['CR'][i]))

        # get gathering data
        df = pd.read_csv(resource_path('data/Ingredients.csv'), sep=';', encoding="cp1250")
        self.gather = dict()
        for i in range(len(df)):
            place = df['Location'][i].split(', ')
            for j in place:
                if self.gather.get(j) is None:
                    self.gather.update({j: list()})
                self.gather[j].append((df['Herbs/Ingredients'][i], df['Rarity'][i], df['Ability'][i],
                                       df['Description'][i], df['Type'][i]))

        # get NPC data
        df = pd.read_csv(resource_path('data/NPC.csv'), sep=';')
        self.npc = dict()
        for i in range(len(df)):
            place = df['Terrain'][i].split(', ')
            for j in place:
                if self.npc.get(j) is None:
                    self.npc.update({j: list()})
                self.npc[j].append((df['Encounter'][i], df['Rarity'][i]))

        # # get fight data
        df = pd.read_csv(resource_path('data/Combat.csv'), sep=';', encoding="cp1250")
        self.fight = dict()
        for i in range(len(df)):
            place = df['Terrain'][i].split(', ')
            for j in place:
                if self.fight.get(j) is None:
                    self.fight.update({j: list()})
                self.fight[j].append((df['Encounter'][i], df['Rarity'][i]))

    def get_encounter(self, place, season, day, encounter_type, level):
        # creating list of possible encounters
        meeting = list()

        # handling 'Random' encounter type
        if encounter_type == 'Random':
            a = random.randint(1, 4)
            if a == 1:
                encounter_type = 'Fight'
            elif a == 2:
                encounter_type = 'Gathering resources'
            elif a == 3:
                encounter_type = 'Meeting'
            else:
                encounter_type = 'Hunting'

        try:
            if encounter_type == 'Fight':
                for i in self.fight[place]:
                    if i[1] == 'common':
                        meeting.append(i[0])
                        meeting.append(i[0])
                        meeting.append(i[0])
                        meeting.append(i[0])
                    elif i[1] == 'uncommon':
                        meeting.append(i[0])
                        meeting.append(i[0])
                        meeting.append(i[0])
                    elif i[1] == 'rare' and int(level) > 10:
                        meeting.append(i[0])
                        meeting.append(i[0])
                    elif int(level) > 15:
                        meeting.append(i[0])
                    # print(random.choice(meeting))
                return random.choice(meeting)
            elif encounter_type == 'Gathering resources':
                for i in self.gather[place]:
                    if i[4] == 'Bug':
                        if day == 'Morning' or day == 'Night':
                            if season == 'Summer' or season == 'Fall':
                                if i[1] == 'Common':
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                elif i[1] == 'Uncommon':
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                elif i[1] == 'Rare' and int(level) > 10:
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                elif int(level) > 15:
                                    meeting.append((i[0], i[2], i[3]))
                            if i[1] == 'Common':
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif i[1] == 'Uncommon':
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif i[1] == 'Rare' and int(level) > 10:
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif int(level) > 15:
                                meeting.append((i[0], i[2], i[3]))
                    else:
                        if season != 'Winter':
                            if day == 'Afternoon' or day == 'Evening':
                                if i[1] == 'Common':
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                elif i[1] == 'Uncommon':
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                elif i[1] == 'Rare' and int(level) > 10:
                                    meeting.append((i[0], i[2], i[3]))
                                    meeting.append((i[0], i[2], i[3]))
                                elif int(level) > 15:
                                    meeting.append((i[0], i[2], i[3]))
                            if i[1] == 'Common':
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif i[1] == 'Uncommon':
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif i[1] == 'Rare' and int(level) > 10:
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif int(level) > 15:
                                meeting.append((i[0], i[2], i[3]))
                chosen = random.choice(meeting)
                # print(chosen)
                return f'{chosen[0]}\n{chosen[1]}\n{chosen[2]}'
            elif encounter_type == 'Meeting':
                for i in self.npc[place]:
                    if i[1] == 'common':
                        meeting.append(i[0])
                        meeting.append(i[0])
                        meeting.append(i[0])
                        meeting.append(i[0])
                    elif i[1] == 'uncommon':
                        meeting.append(i[0])
                        meeting.append(i[0])
                        meeting.append(i[0])
                    elif i[1] == 'rare' and int(level) > 10:
                        meeting.append(i[0])
                        meeting.append(i[0])
                    elif int(level) > 15:
                        meeting.append(i[0])
                # print(random.choice(meeting))
                return random.choice(meeting)
            elif encounter_type == 'Hunting':
                lvl = int(level)
                for i in self.hunt[place]:
                    if int(i[2])*4 <= lvl:
                        if season == 'Winter' and (i[1] == 'Tiny' or i[1] == 'Small'):
                            meeting.append((i[0], i[2]))
                            meeting.append((i[0], i[2]))
                        elif season == 'Winter' and i[1] == 'Medium':
                            meeting.append((i[0], i[2]))
                        elif season == 'Spring' and (i[1] == 'Huge' or i[1] == 'Large'):
                            meeting.append((i[0], i[2]))
                            meeting.append((i[0], i[2]))
                        elif season == 'Spring' and i[1] == 'Medium':
                            meeting.append((i[0], i[2]))
                        elif season == 'Summer' or season == 'Fall':
                            if day == 'Morning' or day == 'Night':
                                if i[1] == 'Tiny' or i[1] == 'Small':
                                    meeting.append((i[0], i[2]))
                                    meeting.append((i[0], i[2]))
                                    meeting.append((i[0], i[2]))
                                elif i[1] == 'Medium':
                                    meeting.append((i[0], i[2]))
                                    meeting.append((i[0], i[2]))
                                else:
                                    meeting.append((i[0], i[2]))
                            elif day == 'Afternoon':
                                if i[1] == 'Huge' or i[1] == 'Large' or i[1] == 'Medium':
                                    meeting.append((i[0], i[2]))
                                    meeting.append((i[0], i[2]))
                                else:
                                    meeting.append((i[0], i[2]))
                            else:
                                meeting.append((i[0], i[2]))
                choice = random.choice(meeting)
                if int(choice[1]) == 0:
                    return f'{choice[0]}*{2*random.randint(0, int(2*lvl))}'
                else:
                    return f'{choice[0]} CR:{choice[1]}'
        except IndexError:
            return 'No such encounter found'
