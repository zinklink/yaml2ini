import sys
from configparser import ConfigParser

# pip install pyyaml
import yaml


def yaml_to_ini(yaml_file, ini_file):

    # Read the YAML file
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Create a ConfigParse object
    config = ConfigParser()

    # Convert YAML format data to INI format.
    for section, values in yaml_data.items():
        config.add_section(section)
        for key, value in values.items():
            config.set(section, key, str(value))

    with open(ini_file, 'w') as file:
        config.write(file)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        yaml_file = sys.argv[1]
        ini_file = sys.argv[2]
        yaml_to_ini(yaml_file, ini_file)
