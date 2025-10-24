import json


def load_data(file_path):
    """Loads JSON file safely with utf-8 encoding"""
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


def read_template(file_path):
    """Reads HTML template file"""
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return ""


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

    output_html += "<div class='card__text'>\n"
    output_html += "<ul class='animal__characteristics'>\n"

    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    if diet:
        output_html += f"<li><strong>Diet:</strong> {diet}</li>\n"

    animal_type = characteristics.get("type")
    if animal_type:
        output_html += f"<li><strong>Type:</strong> {animal_type}</li>\n"

    locations = animal.get("locations")
    if locations:
        output_html += f"<li><strong>Location:</strong> {locations[0]}</li>\n"

    output_html += "</ul>\n"
    output_html += "</div>\n"
    output_html += "</li>\n"

    return output_html


# Entry point for script execution
def main():
    # Load data and template
    animals_data = load_data("animals_data.json")
    template = read_template("animals_template.html")

    if not animals_data or not template:
        print("Missing data or template, aborting.")
        return

    # Generate final output string
    animal_output_str = ""
    for animal in animals_data:
        animal_output_str += serialize_animal(animal)

    # Replace placeholder
    FINAL_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"
    final_html_content = template.replace(FINAL_PLACEHOLDER, animal_output_str)

    # Write the new HTML content to a new file, animals.html
    try:
        with open("animals.html", "w", encoding="utf-8") as file:
            file.write(final_html_content)
        print("animals.html generated successfully!")
    except IOError as e:
        print(f"Error writing the file: {e}")


if __name__ == "__main__":
    main()
