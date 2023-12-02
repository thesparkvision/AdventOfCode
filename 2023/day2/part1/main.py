def is_valid_game(game_cube_subsets, BLUE_BAG_CONFIG):
    game_cube_subsets = game_cube_subsets.strip().split(";")

    for game_cube_subset in game_cube_subsets:
        game_cubes = game_cube_subset.strip().split(",")
        for game_cube in game_cubes:
            game_cube_count, game_cube_name = game_cube.strip().split(" ")
            if int(game_cube_count) > BLUE_BAG_CONFIG[game_cube_name]:
                return False
    return True

def find_valid_game_ids(game_lines, BLUE_BAG_CONFIG):
    valid_games = []

    for game_line in game_lines:
        game_name, game_cube_subsets = game_line.split(":")
        if is_valid_game(game_cube_subsets, BLUE_BAG_CONFIG):
            _, game_id = game_name.split(" ")
            game_id = int(game_id)
            valid_games.append(game_id)
    print(valid_games, "debug")
    return valid_games

def main():
    print("Starting Execution")
    
    game_lines = []
    BLUE_BAG_CONFIG = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        game_lines = [line for line in input_file]
            
    valid_game_ids = find_valid_game_ids(game_lines, BLUE_BAG_CONFIG)
    valid_game_ids_sum = sum(valid_game_ids)

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(valid_game_ids_sum))

    print("Finished Execution")

main()