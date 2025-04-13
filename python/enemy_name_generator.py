import random
import csv

# List of first and second syllables for enemy names
first_syllables = ["Gr", "Zik", "Sn", "Kr", "Vok", "Bl", "Rog", "Tuk", "Wag", "Gur"]
second_syllables = ["nik", "gar", "zak", "kug", "tok", "krak", "zog", "dok", "gash", "blin"]

# Vowels to use for inserting between syllables
vowels = ['a', 'e', 'i', 'o', 'u']

# Function to generate a random enemy name
def generate_enemy_name():
    first = random.choice(first_syllables)
    second = random.choice(second_syllables)
    
    # Check if the name might need a vowel inserted for pronounceability
    if first[-1] in "bcdfghjklmnpqrstvwxyz" and second[0] in "bcdfghjklmnpqrstvwxyz":
        # If both syllables end and start with consonants, insert a vowel
        vowel = random.choice(vowels)
        name = first + vowel + second
    else:
        name = first + second

    return name

# Generate a list of enemy names
enemy_names = [generate_enemy_name() for _ in range(300)]

# Write the generated names to a CSV file
with open('csvs/enemy_names.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Enemy Name"])  # Write the header
    for name in enemy_names:
        writer.writerow([name])

# Output the names to verify
for name in enemy_names:
    print(name)
