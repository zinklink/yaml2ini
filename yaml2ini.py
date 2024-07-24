from configparser import ConfigParser

# pip install pyyaml
import yaml


def yaml_to_ini(yaml_file, ini_file):
    # 讀取YAML文件
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # 創建ConfigParser對象
    config = ConfigParser()

    # 將YAML數據轉換為INI格式
    for section, values in yaml_data.items():
        config.add_section(section)
        for key, value in values.items():
            config.set(section, key, str(value))

    # 將INI數據寫入文件
    with open(ini_file, 'w') as file:
        config.write(file)


if __name__ == "__main__":
    yaml_file = 'passwd.yml'
    ini_file = 'output.ini'
    yaml_to_ini(yaml_file, ini_file)
    yaml_to_ini(yaml_file, ini_file)
    yaml_to_ini(yaml_file, ini_file)
