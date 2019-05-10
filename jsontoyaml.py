import yaml

def main():
    """runtime code"""
    hitchiker = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},\
                 {"name": "Arthur Dent", "species": "Human"}]

    print(hitchiker)

    with open("yamlout.yml", 'w') as zfile:
        yaml.dump(hitchiker, zfile)

main()
