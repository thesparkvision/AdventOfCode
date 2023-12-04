def find_scratchcard_counts(scratchcards):
    total_scratchcard_types = len(scratchcards)
    scratchcard_counts = [1 for _ in range(total_scratchcard_types)]    
    
    for scratchcard in scratchcards:
        scratchcard_name, scratchcard_info = scratchcard.split(":")

        _, scratchcard_id = scratchcard_name.split()
        scratchcard_id = int(scratchcard_id) - 1

        winning_numbers, owned_numbers = scratchcard_info.split("|")
        winning_numbers = set(map(int, winning_numbers.strip().split()))
        owned_numbers = set(map(int, owned_numbers.strip().split()))
        
        matched_numbers = winning_numbers & owned_numbers
        matched_numbers_count = len(matched_numbers)
        
        current_scratchcard_count = scratchcard_counts[scratchcard_id]

        if matched_numbers_count == 0:
            continue

        next_scratchcard_id = scratchcard_id + 1
        last_scratchcard_id = scratchcard_id + matched_numbers_count

        while next_scratchcard_id <= last_scratchcard_id:
            if next_scratchcard_id == total_scratchcard_types:
                break
            scratchcard_counts[next_scratchcard_id] += current_scratchcard_count
            next_scratchcard_id += 1
    
    return scratchcard_counts

def main():
    print("Starting Execution")
    
    lines = []

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]


    scratchcard_counts = find_scratchcard_counts(lines)
    scratchcard_counts_sum = sum(scratchcard_counts)

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(scratchcard_counts_sum))

    print("Finished Execution")

main()