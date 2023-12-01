def get_calibration_value(line):
    numbers = []
    for letter in line:
        if ord(letter) >= ord('0') and ord(letter) <= ord('9'):
            numbers.append(letter)
    
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