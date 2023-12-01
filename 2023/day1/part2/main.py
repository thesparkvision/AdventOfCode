number_words = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def check_if_number_word(index, line):
    ans = '-1'
    for word, number in number_words.items():
        word_slice = line[index: index + len(word)]
        if word_slice == word:
            ans = number
            break
    return ans

def get_calibration_value(line):
    numbers = []
    for index, letter in enumerate(line):
        if ord(letter) >= ord('0') and ord(letter) <= ord('9'):
            numbers.append(letter)
        else:
            number = check_if_number_word(index, line)
            if number!='-1':
                numbers.append(number)

    calibration_value = (numbers[0] + numbers[-1])
    return int(calibration_value)

def main():
    print("Starting Execution")
    final_sum = 0

    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            calibration_value = get_calibration_value(line)
            final_sum += calibration_value
            
    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(final_sum))

    print("Finished Execution")

main()