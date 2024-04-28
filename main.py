import json

# Initialize a dictionary to store data
data_dict = {}

# Open the text file
with open('result.txt', 'r') as file:
    # Read each line
    for line in file:
        # Split the line by commas
        parts = line.strip().split(',')
        
        # Initialize a dictionary to store key-value pairs for this line
        line_data = {}
        
        # Iterate over parts and split each part by colon to get key-value pairs
        for part in parts:
            key, value = part.split(':', 1)
            # Remove any leading or trailing whitespace
            key = key.strip()
            value = value.strip()
            # Remove single quotes around the values
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            # Add key-value pair to line_data dictionary

            ################################# my-custom-code-goes here #################################
            custom_key = 'path'
            custom_value = f"/config/recordings/{line_data.get('callName')}"
            line_data[custom_key] = custom_value

            line_data[key] = value
        
        # Extract the value of callName
        call_name = line_data.get('callName')
        if call_name:
            # Add the line_data dictionary to the data_dict with callName as key
            data_dict[call_name] = line_data

# Write data_dict to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("JSON file 'output.json' has been generated.")
