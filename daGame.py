from random import randint as rnd


def procesar():
    command = input(": ").split()
    action_word = command[0]
    if action_word in action_dict:
        action = action_dict[action_word]
        if len(command) == 2:
            print(action(command[1]))
        elif command[0] == 'exit':
            print(action('Bye bye'))
        elif len(command) == 1:
            print(action())
    else:
        print("Unknown action {}".format(action_word))
        return


class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 12
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""
        if 12 >= self.health >= 9:
            return self._desc
        elif 8 >= self.health >= 5:
            health_line = "It has a wound on its knee."
        elif 4 >= self.health >= 1:
            health_line = "Its left arm has been cut off!"
        elif self.health == 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Human(GameObject):
    def __init__(self, name):
        self.class_name = "human"
        self.health = 10
        self._desc = "You know humans"
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""
        if 8 <= self.health <= 10:
            return self._desc
        elif 5 <= self.health <= 7:
            health_line = "He has some cuts"
        elif 1 <= self.health <= 4:
            health_line = "His right leg is gone!"
        elif self.health == 0:
            health_line = "He is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Elf(GameObject):
    def __init__(self, name):
        self.class_name = "elf"
        self.health = 15
        self._desc = "Melancholic and mystic creatures. Usually shines."
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""
        if 12 <= self.health <= 15:
            return self._desc
        elif 8 <= self.health <= 11:
            health_line = "He is not shining any more."
        elif 4 <= self.health <= 7:
            health_line = "He is bleeding a lot... in blue!"
        elif 1 <= self.health <= 3:
            health_line = "He has not hands. He can't use his bow."
        elif self.health == 0:
            health_line = "He is dead (Oddly he's shining again)."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        damage = rnd(0, 3)
        if damage == 3:
            msg = "Super critical hit.\n"
        elif damage == 2:
            msg = "Critical hit.\n"
        elif damage == 0:
            msg = "You missed. "
        else:
            msg = ""

        if type(thing) == Goblin:
            if thing.health == 0:
                return "It is dead. You can't hit it any more."
            thing.health -= damage
            if thing.health <= 0:
                thing.health = 0
                msg += "You killed the {}! ".format(thing.class_name)
            elif damage == 0:
                pass
            else:
                msg += "You hit the {}. ".format(thing.class_name)
            msg += "Health = " + str(thing.health)

        elif type(thing) == Human:
            if thing.health == 0:
                return "It is dead. You can't hit him any more."
            thing.health -= damage
            if thing.health <= 0:
                thing.health = 0
                msg += "You killed the {}! . ".format(thing.class_name)
            elif damage == 0:
                pass
            else:
                msg += "You hit the {}. ".format(thing.class_name)
            msg += "Health = " + str(thing.health)

        elif type(thing) == Elf:
            if thing.health == 0:
                return "It is dead. You can't hit him any more."
            thing.health -= damage
            if thing.health <= 0:
                thing.health = 0
                msg += "You killed the {}! . ".format(thing.class_name)
            elif damage == 0:
                pass
            else:
                msg += "You hit the {}. ".format(thing.class_name)
            msg += "Health = " + str(thing.health)
            
        else:
            msg = "There is no {} here.".format(thing.class_name)
        return msg
    else:
        return "There is no {} here. Create one first if you dare.".format(noun)


def new(noun):
    if noun in race_dict:
        race = race_dict[noun]
        race = race("")
        return "New character created. " + "Health = " + str(race.health)
    else:
        return "You can not create a {}.".format(noun)


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


def dice():
    return "Your roll is " + str(rnd(1,6))


action_dict = {"examine": examine, "hit": hit, "new": new, "exit": quit, "roll": dice}
race_dict = {"goblin": Goblin, "human": Human, "elf": Elf}
justOnce = 1
while True:
    intro = "daGame".center(80, '*')
    intro += """
    Este es un juego para competir con tus amigos. Cada quien elige un
    personaje, se tira el dado para ver quién golpea primero, el primero que
    mate al otro gana :D
    Instrucciones:
    1.- Crear un nuevo personaje (new 'personaje') que puede ser
        un goblin/human/elf (como máximo puede haber 3 jugadores a la vez).
        En cualquier momento puedes crear un personaje nuevo, esto resetea sus
        stats (no se pueden tener dos personajes del mismo tipo).
    2.- Examinar un personaje (examine 'personaje') para ver su
        estatus.
    3.- Golpear un personaje (hit 'personaje') solo por diversión.
    4.- Tirar el dado (roll).
    5.- Salir (exit)."""
    while justOnce:
        print(intro)
        justOnce -= 1
    procesar()
