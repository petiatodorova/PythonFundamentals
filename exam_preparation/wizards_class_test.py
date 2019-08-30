class Wizard:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)


wizards_list = []

data = input()
wizards_names_list = []

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
            cur_wizard.health += health
            cur_wizard.damage += damage
    data = input()

data = input()

while not data == 'end':
    splitted_data = data.split(" <=> ")
    wizard_one_name = splitted_data[0]
    wizard_two_name = splitted_data[1]
    if not (wizard_one_name in wizards_names_list):
        print("Cannot place a fight with non-existing wizards!")
    elif not (wizard_two_name in wizards_names_list):
        print("Cannot place a fight with non-existing wizards!")
    elif ((wizard_one_name in wizards_names_list) and (wizard_two_name in wizards_names_list)):
        # FIGHT

        attacker_list = list(filter(lambda wiz: wiz.name == wizard_one_name, wizards_list))
        attacked_list = list(filter(lambda wiz: wiz.name == wizard_two_name, wizards_list))
        if len(attacker_list) > 0 and len(attacked_list) > 0:
            attacker = attacker_list[0]
            attacked = attacked_list[0]
            attacked.health -= attacker.damage
            attacker.health += 50
            if attacked.health <= 0:
                print(f"Fatality - {attacker.name} wins!")
                wizards_list.remove(attacked)
            else:
                print(f"Next time {attacked.name}!")
        else:
            print("Cannot place a fight with non-existing wizards!")
    data = input()

ordered_wizards = sorted(wizards_list, key=lambda wiz: (-wiz.health))
for wizard in ordered_wizards:
    print(f"Wizard: {wizard.name}. Health: {wizard.health}. Damage power: {wizard.damage}")