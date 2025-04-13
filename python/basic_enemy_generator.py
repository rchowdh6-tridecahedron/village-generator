import csv
import random

# Load the generated enemy names from the CSV
def load_enemy_names(filename):
    names = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            names.append(row[0])  # Assuming the names are in the first column
    return names

# Load the basic enemy data (health, stats, abilities, etc.)
def load_basic_enemies(filename):
    enemies = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            enemies.append({
                'enemy_type': row['enemy_type'],
                'health': int(row['health']),
                'strength': int(row['strength']),
                'agility': int(row['agility']),
                'constitution': int(row['constitution']),
                'intelligence': int(row['intelligence']),
                'wisdom': int(row['wisdom']),
                'perception': int(row['perception']),
                'abilities': row['abilities']
            })
    return enemies

# Generate enemies using random names from the enemy name list and basic enemy stats
def generate_enemies(names_file, basic_enemies_file, num_enemies, output_file):
    names = load_enemy_names(names_file)
    basic_enemies = load_basic_enemies(basic_enemies_file)

    enemies = []

    # Create the specified number of enemies
    for i in range(num_enemies):
        # Get a random enemy type from the basic_enemies list
        enemy_data = random.choice(basic_enemies)

        # Randomly assign a name from the generated names
        name = random.choice(names)

        # Create an enemy dictionary with the assigned name and basic enemy data
        enemy = {
            'enemy_name': name,
            'enemy_type': enemy_data['enemy_type'],
            'health': enemy_data['health'],
            'strength': enemy_data['strength'],
            'agility': enemy_data['agility'],
            'constitution': enemy_data['constitution'],
            'intelligence': enemy_data['intelligence'],
            'wisdom': enemy_data['wisdom'],
            'perception': enemy_data['perception'],
            'abilities': enemy_data['abilities']
        }
        enemies.append(enemy)

    # Write the generated enemies to a new CSV file
    with open(output_file, mode='w', newline='') as file:
        fieldnames = ['enemy_name', 'enemy_type', 'health', 'strength', 'agility', 'constitution', 'intelligence',
                      'wisdom', 'perception', 'abilities']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for enemy in enemies:
            writer.writerow(enemy)

# Example usage: Generate 20 enemies and save to a CSV file
generate_enemies('csvs/enemy_names.csv', 'csvs/basic_enemies.csv', 50, 'results/enemies.csv')
