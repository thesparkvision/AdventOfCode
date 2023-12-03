def is_valid_cell(i, j, length, height):
    return  0 <= i < height and 0 <= j < length

def is_cell_number(i, j, engine_schematic):
    return ord('0') <= ord(engine_schematic[i][j]) <= ord('9')

def construct_neighbour_coordinates(i,j):
    top_left = i-1, j-1
    top_center = i-1, j
    top_right = i-1, j+1
    center_left = i, j-1
    center_right = i, j+1
    bottom_left = i+1, j-1
    bottom_center = i+1, j
    bottom_right = i+1, j+1

    return [
        top_left,
        top_center,
        top_right,
        center_left,
        center_right,
        bottom_left,
        bottom_center,
        bottom_right
    ]

def find_complete_part_number(ni, nj, engine_schematic):
    complete_part_number = ""
    complete_part_number += engine_schematic[ni][nj]
    rel_left = nj - 1
    rel_right = nj + 1
    length = len(engine_schematic[ni])

    while rel_left >= 0:
        if is_cell_number(ni, rel_left, engine_schematic):
            complete_part_number = engine_schematic[ni][rel_left] + complete_part_number
        else:
            break
        rel_left -= 1

    while rel_right < length:
        if is_cell_number(ni, rel_right, engine_schematic):
            complete_part_number += engine_schematic[ni][rel_right]
        else:
            break
        rel_right += 1

    complete_part_number = int(complete_part_number)
    return complete_part_number

def find_part_numbers(engine_schematic):
    part_numbers = list()    
    height = len(engine_schematic)
    length = len(engine_schematic[0])

    for i in range(0, height):
        for j in range(0, length):

            cell_val = engine_schematic[i][j]
            if is_cell_number(i,j, engine_schematic) or cell_val == '.':
                continue

            neighbouring_coordinates = construct_neighbour_coordinates(i, j)
            found_part_numbers = set()
            for neighbouring_coordinate in neighbouring_coordinates:
                ni, nj = neighbouring_coordinate 
                
                if (
                    is_valid_cell(ni, nj, length, height) and 
                    is_cell_number(ni, nj, engine_schematic)
                ):
                    part_number = find_complete_part_number(ni, nj, engine_schematic)
                    if part_number not in found_part_numbers:
                        part_numbers.append(part_number)
                        found_part_numbers.add(part_number)

    return part_numbers

def main():
    print("Starting Execution")
    
    lines = []

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
            
    part_numbers = find_part_numbers(lines)
    part_numbers_sums = sum(part_numbers)

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(part_numbers_sums))

    print("Finished Execution")

main()