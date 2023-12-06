def is_winning_race_possible(boat_speed, remaining_race_time, record_distance) -> bool:
    total_distance_traversed = boat_speed * remaining_race_time
    return total_distance_traversed > record_distance

def find_no_of_ways_to_win_race(race_time, record_distance) -> int:
    no_of_ways = 0
    
    for boat_charging_time in range(1, race_time):
        boat_speed = boat_charging_time
        race_time_left = race_time - boat_charging_time

        if is_winning_race_possible(
            boat_speed,
            race_time_left,
            record_distance
        ):
            no_of_ways += 1

    return no_of_ways

def find_no_of_winning_ways_data(times_data, distances_data) -> list[int]:
    print("Finding no. of ways to win the race for the data....")
    no_of_winning_ways_data = []

    no_of_races = len(times_data)

    for race_no in range(0, no_of_races):
        race_time = times_data[race_no]
        record_distance = distances_data[race_no]
        
        print(f"Finding no. of ways to win race {race_no}")
        no_of_ways_to_win_race = find_no_of_ways_to_win_race(race_time, record_distance)
        no_of_winning_ways_data.append(no_of_ways_to_win_race)

    return no_of_winning_ways_data

def main() -> None:
    print("Starting Execution")
    
    lines = []

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        lines = [line.strip().split(":")[1] for line in input_file]
            
    single_race_time = "".join(lines[0].split())
    single_race_record_distance = "".join(lines[1].split())

    times = [int(single_race_time)]
    distances = [int(single_race_record_distance)]

    no_of_winning_ways_data = find_no_of_winning_ways_data(
        times,
        distances
    )
    
    product = 1
    for no_of_winning_ways in no_of_winning_ways_data:
        product *= no_of_winning_ways

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(product))

    print("Finished Execution")

main()