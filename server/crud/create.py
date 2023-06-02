import json
import os

def main(new_item):
    def read_json_file(filename):
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump([], file)  # Create an empty JSON list
            return []
        with open(filename, "r") as file:
            data = json.load(file)
        return data

    def write_json_file(data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def create(data, item):
        data.append(item)
        return data

    filename = "data.json"
    data = read_json_file(filename)
    data = create(data, new_item)
    write_json_file(data, filename)