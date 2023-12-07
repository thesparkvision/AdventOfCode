from enum import Enum

class HandRanks(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

card_ranks = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9 ,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

hand_identifiers = {
    '5': HandRanks.FIVE_OF_A_KIND,
    '41': HandRanks.FOUR_OF_A_KIND,
    '32': HandRanks.FULL_HOUSE,
    '311': HandRanks.THREE_OF_A_KIND,
    '221': HandRanks.TWO_PAIR,
    '2111': HandRanks.ONE_PAIR,
    '11111': HandRanks.HIGH_CARD
}

def find_hand_type(hand):
    hand_data = dict()
    for card in hand:
        hand_data[card] = hand_data.get(card, 0) + 1
    
    card_counts = [count for count in hand_data.values()]
    card_counts.sort(reverse=True)
    hand_identifier = ''.join(map(str,card_counts))

    hand_type =  hand_identifiers[hand_identifier]
    return hand_type

def sort_processed_data(data):
    return data['']

def get_total_winnings(processed_data):
    total_winnings = 0    
    for i in range(0, len(processed_data)):
        rank = i+1
        amount = processed_data[i]['amount']
        total_winnings += rank*amount
    return total_winnings

def process_input_data(input_data):
    processed_data = []
    for line in input_data:
        hand, bid_amount = line.strip().split()
        hand_type = find_hand_type(hand)
        processed_data.append({
            'hand': hand,
            'amount': int(bid_amount),
            'type': hand_type
        })
    return processed_data

def custom_key(item):
    enum_val = item['type'].value
    strength_tuple = tuple(card_ranks.get(char, 0) for char in item['hand'])
    return (enum_val, strength_tuple)

def find_total_winnings(input_data):
    print("Processing Input Data...")
    processed_data = process_input_data(input_data)

    print("Sorting Processed Data...")    
    sorted_data = sorted(processed_data, key=custom_key)

    print("Finding Total Winnings...")
    total_winnings = get_total_winnings(sorted_data)
    return total_winnings
    
def main() -> None:
    print("Starting Execution")
    
    lines = []

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        lines = [line for line in input_file]

    # lines = lines[:5]
    print(lines,end="\n\n")
    total_winnings = find_total_winnings(lines)
    
    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(total_winnings))

    print("Finished Execution")

main()