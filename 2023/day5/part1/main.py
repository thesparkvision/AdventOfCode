class Solution:
    def __init__(self) -> None:
        self.seeds = []
        self.data_types = {
            'seed_to_soil_map': [],
            'soil_to_fertilizer_map': [],
            'fertilizer_to_water_map': [],
            'water_to_light_map': [],
            'light_to_temperature_map': [],
            'temperature_to_humidity_map': [],
            'humidity_to_location_map': []
        }

    def find_matching_destination(self, data_map, requested_no):
        for data in data_map:
            source_range, destination_range, range_length = data
            lowest_source_no = source_range
            highest_source_no = source_range + range_length - 1
            if requested_no >= lowest_source_no and requested_no <= highest_source_no:
                requested_no_relative_position = highest_source_no - requested_no
                highest_destionation_no = destination_range + range_length - 1
                matching_destination_no = highest_destionation_no - requested_no_relative_position
                return matching_destination_no
            
        return requested_no
    
    def find_location_numbers(self):
        print("Finding Location Numbers...")
        location_numbers = []

        for seed_no in self.seeds:
            soil_no = self.find_matching_destination(self.data_types['seed_to_soil_map'], seed_no)
            fertilizer_no = self.find_matching_destination(self.data_types['soil_to_fertilizer_map'], soil_no)
            water_no = self.find_matching_destination(self.data_types['fertilizer_to_water_map'], fertilizer_no)
            light_no = self.find_matching_destination(self.data_types['water_to_light_map'], water_no)
            temperature_no = self.find_matching_destination(self.data_types['light_to_temperature_map'], light_no)
            humidity_no = self.find_matching_destination(self.data_types['temperature_to_humidity_map'], temperature_no)
            location_no = self.find_matching_destination(self.data_types['humidity_to_location_map'], humidity_no)
            location_numbers.append(location_no)

        return location_numbers

    def extract_map_data(self, data_type, data):
        print(f"Extracting map data for {data_type}")
        data_map = self.data_types[data_type]
        splitted_data = data.strip().split("\n")
        
        for line in splitted_data:
            destination_range_no, source_range_no, range_length = map(int,line.strip().split())
            data_map.append((source_range_no, destination_range_no, range_length))

    def extract_seed_data(self, seed_data):
        print(f"Extracting seed data")
        self.seeds = [int(seed_no) for seed_no in seed_data.split()]

    def extract_data(self, input_data):
        segregated_info = input_data.split("\n\n")
        for info in segregated_info:
            data_type, data = info.split(":")
            data_type = data_type.replace("-","_").replace(" ", "_")
            
            if data_type == "seeds":
                self.extract_seed_data(data)
            elif data_type in self.data_types:
                self.extract_map_data(data_type, data)
            else:
                raise Exception(f"Invalid datatype detected: {data_type}")

def main():
    print("Starting Execution")
    
    input_data = None
    print("Reading Input File ...")
    with open("../input.txt", "r") as input_file:
        input_data = input_file.read()
    
    solution = Solution()
    solution.extract_data(input_data)
    location_numbers = solution.find_location_numbers()
    lowest_location_number = min(location_numbers)

    print("Writing Output File ...")
    with open("output.txt", "w") as output_file:
        output_file.write(str(lowest_location_number))

    print("Finished Execution")

main()