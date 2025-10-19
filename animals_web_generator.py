import json


def load_data(file_path):
    """Loads JSON file"""
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")


def read_template(file_path):
    """Reads HTML template file"""
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal):
    """
    Converts a single animal dictionary into a structured HTML list item 
    with safety checks for missing fields.
    """
    output_html = ""

    output_html += "<li class='cards__item'>\n"

    name = animal.get("name")
    if name:
        output_html += f"<div class='card__title'>{name}</div>\n"

    output_html += "<p class='card__text'>\n"

    characteristics = animal.get("characteristics")
    if characteristics:

        diet = characteristics.get("diet")
        if diet:
            output_html += f"<strong>Diet:</strong> {diet}<br/>\n"

        animal_type = characteristics.get("type")
        if animal_type:
            output_html += f"<strong>Type:</strong> {animal_type}<br/>\n"

    locations = animal.get("locations")
    if locations and len(locations) > 0:
        output_html += f"<strong>Location:</strong> {locations[0]}<br/>\n"

    output_html += "</p>\n"
    output_html += "</li>\n"

    return output_html

# --------------------- MAIN EXECUTION ---------------------


# Load data and template
animals_data = load_data("animals_data.json")
template = read_template("animals_template.html")


# Generate final output string
animal_output_str = ""
for animal in animals_data:
    # This is the simplified, cleaner loop
    animal_output_str += serialize_animal(animal)


# Replace placeholder
FINAL_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"
final_html_content = template.replace(FINAL_PLACEHOLDER, animal_output_str)


# Write the new HTML content to a new file, animals.html
try:
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html_content)
except IOError as e:
    print(f"Error writing the file: {e}")
