import re

def find_scratchcard_points(scratchcards):
    scratchcard_points = list()    
    
    for scratchcard in scratchcards:
        _, scratchcard_info = scratchcard.split(":")
        winning_numbers, owned_numbers = scratchcard_info.split("|")
        
        winning_numbers = re.split('\s+', winning_numbers.strip())
        winning_numbers = set(map(int, winning_numbers))
        
        owned_numbers = re.split('\s+', owned_numbers.strip())
        owned_numbers = set(map(int, owned_numbers))
        
        matched_numbers = winning_numbers & owned_numbers
        matched_numbers_count = len(matched_numbers)
        scratchcard_point = 0 if matched_numbers_count == 0 else 2**(matched_numbers_count-1)
        
        scratchcard_points.append(scratchcard_point)

    return scratchcard_points

def main():
    print("Starting Execution")
    
    lines = []

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
            
    scratchcard_points = find_scratchcard_points(lines)
    scratchcard_points_sums = sum(scratchcard_points)

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(scratchcard_points_sums))

    print("Finished Execution")

main()