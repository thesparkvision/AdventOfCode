from copy import deepcopy
from itertools import accumulate

CUBE_COLOR_DICT = {
    "blue": 1,
    "red": 1,
    "green": 1
}

def find_minimum_set_cubes(game_cube_subsets):
    game_cube_subsets = game_cube_subsets.strip().split(";")
    minimum_set_cubes = deepcopy(CUBE_COLOR_DICT)

    for game_cube_subset in game_cube_subsets:
        game_cubes = game_cube_subset.strip().split(",")
        for game_cube in game_cubes:
            game_cube_count, game_cube_name = game_cube.strip().split(" ")
            if int(game_cube_count) > minimum_set_cubes[game_cube_name]:
                minimum_set_cubes[game_cube_name] = int(game_cube_count)
    
    return minimum_set_cubes

def find_game_power(minimum_set_cubes):
    game_power = 1
    for cube_count in minimum_set_cubes.values():
        game_power *= cube_count
    return game_power

def find_game_powers(game_lines):
    game_powers = []

    for game_line in game_lines:
        game_name, game_cube_subsets = game_line.split(":")
        minimum_set_cubes = find_minimum_set_cubes(game_cube_subsets)
        game_power = find_game_power(minimum_set_cubes)
        game_powers.append(game_power)

    return game_powers

def main():
    print("Starting Execution")
    
    game_lines = []

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        game_lines = [line for line in input_file]
            
    game_powers = find_game_powers(game_lines)
    game_powers_sums = sum(game_powers)

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(game_powers_sums))

    print("Finished Execution")

main()