import json


def load_data(file_path):
    """Loads JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


def get_animal_info():
    for animal in animals_data:
        name = animal.get("name")
        if name:
            print(f"Name: {name}")

        characteristics = animal.get("characteristics")
        if characteristics:

            diet = characteristics.get("diet")
            if diet:
                print(f"Diet: {diet}")

            animal_type = characteristics.get("type")
            if animal_type:
                print(f"Type: {animal_type}")

        locations = animal.get("locations")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")
        print()


get_animal_info()
