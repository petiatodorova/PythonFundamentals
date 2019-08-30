width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
count_boxes = 0

while True:
    input_command = input()
    if input_command == "Done":
        print(f'{volume} Cubic meters left.')
        break

    volume -= int(input_command)
    if volume < 0:
        print(f'No more free space! You need {abs(volume)} Cubic meters more.')
        break

