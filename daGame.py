from random import randint as rnd


def procesar():
    command = input(": ").split()
    action_word = command[0]
    if action_word in action_dict:
        action = action_dict[action_word]
        if command[0] != 'exit':
            print(action(command[1]))
        else:
            print(action('Bye bye'))
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
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        health_line = ""
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
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


action_dict = {"examine": examine, "hit": hit, "new": new, "exit": quit}
race_dict = {"goblin": Goblin, "human": Human}
justOnce = 1
while True:
    intro = "daGame".center(80, '*')
    intro += """
    Este es un juego de prueba en el que tu puedes hacer solo tres cosas: 
    1.- Crear un nuevo personaje (new 'personaje') que puede ser
        un goblin o un human (puedes tener hasta dos personajes a la vez).
        En cualquier momento puedes crear un personaje nuevo, esto resetea sus
        stats (no se pueden tener dos personajes del mismo tipo).
    2.- Examinar un personaje (examine 'personaje') para ver su
        estatus.
    3.- Golpear un personaje (hit 'personaje') solo por diversión.
    Para salir sólo escribe exit."""
    while justOnce:
        print(intro)
        justOnce -= 1
    procesar()
