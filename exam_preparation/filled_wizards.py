class Wizard:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)


wizards_list = []

data = input()

while not data == 'fight':
    splitted_data = data.split()

    wizards_names_list = list(map(lambda wiz: wiz.name, wizards_list))

    if splitted_data[0] == "new":
        name = splitted_data[1]
        health = int(splitted_data[2])
        damage = int(splitted_data[3])


        if not name in wizards_names_list:
            cur_wizard = Wizard(name=name, health=health, damage=damage)
            wizards_list.append(cur_wizard)
        else:
            print("Wizard already exists!")

    elif splitted_data[0] == "edit":
        name = splitted_data[1]
        health = int(splitted_data[2])
        damage = int(splitted_data[3])

        if not name in wizards_names_list:
            print("Wizard does not exist!")
        else:
            cur_wizard = list(filter(lambda wiz: wiz.name == name, wizards_list))[0]
            cur_wizard.health = health
            cur_wizard.damage = damage
    data = input()

for el in wizards_list:
    print(el.name)
    print(el.health)
    print(el.damage)
    print("*********")

