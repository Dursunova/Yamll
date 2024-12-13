import yaml


with open('pip.yaml', 'r') as file:
    data = yaml.safe_load(file)

for book in data['books']:
    if book['pages'] > 1000:
        print(f"Big book: {book['title']} from {book['library']}")
