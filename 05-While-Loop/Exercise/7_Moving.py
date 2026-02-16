boxes_size = 0
free_width = int(input())
free_length = int(input())
free_height = int(input())
free_space = free_width * free_length * free_height
command = input()

while command != 'Done':
    number_of_boxes = int(command)
    boxes_size += number_of_boxes

    if boxes_size >= free_space:
        break

    command = input()

if boxes_size >= free_space:
    meters_needed = boxes_size - free_space
    print(f'No more free space! You need {meters_needed} Cubic meters more.')

elif command == 'Done' or free_space > boxes_size:
    meters_left = free_space - boxes_size
    print(f'{meters_left} Cubic meters left.')