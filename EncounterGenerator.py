import pandas as pd
import random


class Generator:
    def __init__(self):
        # get hunting data
        df = pd.read_csv('Hunting.csv', sep=';')
        self.hunt = dict()
        for i in range(len(df)):
            place = df['Terrain'][i].split(', ')
            for j in place:
                if self.hunt.get(j) == None:
                    self.hunt.update({j: list()})
                self.hunt[j].append((df['Beast'][i], df['Size'][i], df['CR'][i]))
        # print(set(self.hunt))

        # get gathering data
        df = pd.read_csv('Ingredients.csv', sep=';', encoding="cp1250")
        self.gather = dict()
        for i in range(len(df)):
            place = df['Location'][i].split(', ')
            for j in place:
                if self.gather.get(j) == None:
                    self.gather.update({j: list()})
                self.gather[j].append((df['Herbs/Ingredients'][i], df['Rarity'][i], df['Ability'][i],
                                       df['Description'][i], df['Type'][i]))
        # print(set(self.gather))

        # get NPC data
        df = pd.read_csv('NPC.csv', sep=';')
        self.npc = dict()
        for i in range(len(df)):
            place = df['Terrain'][i].split(', ')
            for j in place:
                if self.npc.get(j) == None:
                    self.npc.update({j: list()})
                self.npc[j].append((df['Encounter'][i], df['Rarity'][i]))
        # print(set(self.npc))

        # # get combat data
        df = pd.read_csv('Combat.csv', sep=';', encoding="cp1250")
        self.fight = dict()
        for i in range(len(df)):
            place = df['Terrain'][i].split(', ')
            for j in place:
                if self.fight.get(j) == None:
                    self.fight.update({j: list()})
                self.fight[j].append((df['Herbs/Ingredients'][i], df['Rarity'][i], df['Ability'][i],
                                       df['Description'][i], df['Type'][i]))
        print(set(self.fight))

    def getEncounter(self, place, season, day, type, level):
        meeting = list()

        if type == 'Random':
            a = random.randint(1, 4)
            if a == 1:
                type = 'Fight'
            elif a == 2:
                type = 'Gathering resources'
            elif a == 3:
                type = 'Meeting'
            else:
                type = 'Hunting'

        if type == 'Fight':
            pass

        elif type == 'Gathering resources':
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
                            elif i[1] == 'Rare' and int(level)>10:
                                meeting.append((i[0], i[2], i[3]))
                                meeting.append((i[0], i[2], i[3]))
                            elif int(level)>15:
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
        elif type == 'Meeting':
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
        elif type == 'Hunting':
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

        return 'green'
        pass
