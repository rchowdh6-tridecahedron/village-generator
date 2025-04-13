import csv
import random

# Load names from a CSV file
def load_names(filename):
    names = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row[0])  # Assuming the names are in the first column
    return names

# Load classes from a CSV file
def load_classes(filename):
    classes = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create a dictionary for each class: name, weight, and other info
            classes.append({
                'name': row['class_name'],
                'weight': int(row['weight']),
                'strength': int(row['strength']),
                'agility': int(row['agility']),
                'constitution': int(row['constitution']),
                'intelligence': int(row['intelligence']),
                'wisdom': int(row['wisdom']),
                'perception': int(row['perception']),
                'base_health': int(row['base_health']),
            })
    return classes

# Generate a villager
def generate_villager(names, class_info):
    name = random.choice(names)
    
    # Calculate attributes based on class
    attributes = {
        'strength': random.randint(-1, 1) + class_info['strength'],
        'agility': random.randint(-1, 1) + class_info['agility'],
        'constitution': random.randint(-1, 1) + class_info['constitution'],
        'intelligence': random.randint(-1, 1) + class_info['intelligence'],
        'wisdom': random.randint(-1, 1) + class_info['wisdom'],
        'perception': random.randint(-1, 1) + class_info['perception'],
    }

    # Calculate health
    health = random.randint(8, 10) + class_info['base_health']  # base health range 8-10, with class bonus

    # Create a villager dictionary
    villager = {
        'name': name,
        'class': class_info['name'],
        'strength': attributes['strength'],
        'agility': attributes['agility'],
        'constitution': attributes['constitution'],
        'intelligence': attributes['intelligence'],
        'wisdom': attributes['wisdom'],
        'perception': attributes['perception'],
        'health': health,
    }
    return villager

# Generate a list of villagers and save it to a CSV
def generate_villagers(names_file, classes_file, num_villagers, output_file):
    names = load_names(names_file)
    classes = load_classes(classes_file)

    villagers = []

    # Step 1: Ensure at least one villager of each class
    for class_info in classes:
        name = random.choice(names)
        villager = generate_villager([name], class_info)  # Generate one villager for each class
        villagers.append(villager)

    # Step 2: Generate remaining villagers, weighted by class
    remaining_villagers = num_villagers - len(classes)
    
    # If there are more villagers to generate than classes, generate them randomly with weighted chances
    for _ in range(remaining_villagers):
        class_info = random.choices(classes, weights=[cls['weight'] for cls in classes])[0]
        villager = generate_villager(names, class_info)
        villagers.append(villager)

    # Step 3: Sort the villagers by their class name in alphabetical order
    villagers_sorted = sorted(villagers, key=lambda x: x['class'])

    # Write villagers to CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=villagers_sorted[0].keys())
        writer.writeheader()
        for villager in villagers_sorted:
            writer.writerow(villager)

# Example usage:
generate_villagers('csvs/names.csv', 'csvs/classes.csv', 50, 'results/villagers.csv')
