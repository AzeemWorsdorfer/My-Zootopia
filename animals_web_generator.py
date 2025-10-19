import json


def load_data(file_path):
    """Loads JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


animal_output_str = ""
for animal in animals_data:
    animal_output_str += "<li class='cards__item'>\n"
    name = animal.get("name")
    animal_output_str += f"<div class='card__title'>{name}</div>\n"

    animal_output_str += "<p class='card__text'>\n"
    characteristics = animal.get("characteristics")
    if characteristics:

        diet = characteristics.get("diet")
        if diet:
            animal_output_str += f"<strong>Diet:</strong> {diet}<br/>\n"

        animal_type = characteristics.get("type")
        if animal_type:
            animal_output_str += f"<strong>Type:</strong> {animal_type}<br/>\n"

    locations = animal.get("locations")
    if locations and len(locations) > 0:
        animal_output_str += f"<strong>Location:</strong> {locations[0]}<br/>\n"
    animal_output_str += "</p>\n"
    animal_output_str += "</li>\n"


def read_template(file_path):
    """Reads HTML template file"""
    with open(file_path, "r") as handle:
        return handle.read()


template = read_template("animals_template.html")

final_html_content = template.replace(
    "__REPLACE_ANIMALS_INFO__", animal_output_str)

try:
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html_content)
except IOError as e:
    print(f"Error writing the file: {e}")
