import csv
import random
import re

# ---------- Utility ----------
def load_csv(filepath):
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def draw_random_items(items, count):
    if count >= len(items):
        return random.sample(items, len(items))  # Shuffle all if asking for more than available
    return random.sample(items, count)

# ---------- Villager Deck ----------
def build_villager_deck(filepath, count):
    villagers = load_csv(filepath)
    selected = draw_random_items(villagers, count)
    selected.sort(key=lambda v: v['class'])  # Optional: Sort alphabetically by class
    print(f"\n🧑‍🌾 Villager Deck ({len(selected)} cards):")
    for v in selected:
        print(f"- {v['name']} ({v['class']}) | HP: {v['health']} | "
              f"STR: {v['strength']} AGI: {v['agility']} CON: {v['constitution']} "
              f"INT: {v['intelligence']} WIS: {v['wisdom']} PER: {v['perception']} | Fit: {v['class']}")
    return selected

# ---------- Enemy Deck ----------
def build_enemy_deck(filepath, count):
    enemies = load_csv(filepath)
    selected = draw_random_items(enemies, count)
    print(f"\n👹 Enemy Deck ({len(selected)} cards):")
    for e in selected:
        print(f"- {e['enemy_name']} ({e['enemy_type']}) | HP: {e['health']} | "
              f"STR: {e['strength']} AGI: {e['agility']} CON: {e['constitution']} "
              f"INT: {e['intelligence']} WIS: {e['wisdom']} PER: {e['perception']} | Abilities: {e['abilities']}")
    return selected

# ---------- Boss Deck ----------
def build_boss_deck(filepath, count):
    bosses = load_csv(filepath)
    selected = draw_random_items(bosses, count)
    print(f"\n👑 Boss Deck ({len(selected)} cards):")
    for b in selected:
        print(f"- {b['name']} ({b['race']} {b['class']}) | HP: {b['health']} | "
              f"STR: {b['strength']} AGI: {b['agility']} CON: {b['constitution']} "
              f"INT: {b['intelligence']} WIS: {b['wisdom']} PER: {b['perception']} | Abilities: {b['abilities']}")
    return selected

# ---------- Weapons Deck ----------
def build_weapon_deck(filepath, count):
    weapons = load_csv(filepath)
    selected = draw_random_items(weapons, count)
    print(f"\n🗡️ Weapon Deck ({len(selected)} cards):")
    for w in selected:
        alt = f" | Alt: {w['alt_dice']} ({w['alt_damage_type']})" if w['alt_dice'] else ""
        special = f" | Special: {w['Special']}" if w['Special'] else ""
        print(f"- {w['name']} ({w['attribute']} | {w['dice']} {w['damage_type']}{alt}{special})")
    return selected

# ---------- Basic Encounter Deck ----------
def build_basic_encounter_deck(filepath, count):
    encounters = load_csv(filepath)
    selected = draw_random_items(encounters, count)
    print(f"\n📜 Basic Encounter Deck ({len(selected)} cards):")
    for e in selected:
        print(f"- {e['title']}: {e['enemy_rule']} | Twists: {e['plot_twists']}")
    return selected

# ---------- Twist Deck ----------
def build_twist_deck(filepath, count):
    twists = load_csv(filepath)
    selected = draw_random_items(twists, count)
    print(f"\n🌀 Twist Deck ({len(selected)} cards):")
    for t in selected:
        print(f"- {t['title']}: {t['description']}")
    return selected

# ---------- Final Encounter Deck ----------
def build_final_encounter_deck(filepath, count):
    final_encounters = load_csv(filepath)
    selected = draw_random_items(final_encounters, count)
    print(f"\n🔥 Final Encounter Deck ({len(selected)} cards):")
    for f in selected:
        print(f"- {f['title']}: {f['enemy_rule']} | Twists: {f['plot_twists']}")
    return selected

# ---------- PRINT CARD -----------------
def print_card(card, deck_type):
    if deck_type == 'villager':
        print(f"- {card['name']} ({card['class']}) | HP: {card['health']} | "
              f"STR:{card['strength']} AGI:{card['agility']} CON:{card['constitution']} "
              f"INT:{card['intelligence']} WIS:{card['wisdom']} PER:{card['perception']} | Fit: {card['class']}")
    elif deck_type == 'enemy':
        print(f"- {card['enemy_name']} ({card['enemy_type']}) | HP: {card['health']} | "
              f"STR:{card['strength']} AGI:{card['agility']} CON:{card['constitution']} "
              f"INT:{card['intelligence']} WIS:{card['wisdom']} PER:{card['perception']} | Abilities: {card['abilities']}")
    elif deck_type == 'boss':
        print(f"- {card['name']} ({card['race']} {card['class']}) | HP: {card['health']} | "
              f"STR:{card['strength']} AGI:{card['agility']} CON:{card['constitution']} "
              f"INT:{card['intelligence']} WIS:{card['wisdom']} PER:{card['perception']} | Abilities: {card['abilities']}")
    elif deck_type == 'weapon':
        print(f"- {card['name']} | {card['attribute']} | {card['dice']} {card['damage_type']}"
              f"{' | Alt: ' + card['alt_dice'] + ' ' + card['alt_damage_type'] if card['alt_dice'] else ''}"
              f"{' | ' + card['Special'] if card['Special'] else ''}")
    elif deck_type == 'basic_encounter':
        print(f"- {card['title']} | Rule: {card['enemy_rule']} | Twists: {card['plot_twists']}")
    elif deck_type == 'twist':
        print(f"- {card['title']} | Description: {card['description']}")
    elif deck_type == 'final_encounter':
        print(f"- {card['title']} | Rule: {card['enemy_rule']} | Twists: {card['plot_twists']}")
    else:
        print(f"- Unknown card type: {deck_type}")

# ----- Dice Parser ---------
def parse_dice(dice_str):
    match = re.fullmatch(r'(\d+)d(\d+)', dice_str)
    if not match:
        return None
    count, sides = map(int, match.groups())
    return sum(random.randint(1, sides) for _ in range(count))


# ---------- Main ----------
def main():
    print("📦 Deck Builder - Village Defense")

    # Paths to your CSVs
    villager_file = 'results/villagers.csv'
    enemy_file = 'results/enemies.csv'
    boss_file = 'csvs/bosses.csv'
    weapons_file = 'csvs/weapons.csv'
    basic_encounters_file = 'csvs/basic_encounters.csv'
    twists_file = 'csvs/twists.csv'
    final_encounters_file = 'csvs/final_encounters.csv'

    try:
        v_count = int(input("How many villagers to include? "))
        e_count = int(input("How many enemies to include? "))
        b_count = int(input("How many bosses to include? "))
        w_count = int(input("How many weapons to include? "))
        be_count = int(input("How many basic encounters to include? "))
        t_count = int(input("How many twists to include? "))
        fe_count = int(input("How many final encounters to include? "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    villager_deck = build_villager_deck(villager_file, v_count)
    enemy_deck = build_enemy_deck(enemy_file, e_count)
    boss_deck = build_boss_deck(boss_file, b_count)
    weapon_deck = build_weapon_deck(weapons_file, w_count)
    basic_encounter_deck = build_basic_encounter_deck(basic_encounters_file, be_count)
    twist_deck = build_twist_deck(twists_file, t_count)
    final_encounter_deck = build_final_encounter_deck(final_encounters_file, fe_count)
    
    deck_state = {
        'villager': villager_deck,
        'enemy': enemy_deck,
        'boss': boss_deck,
        'weapon': weapon_deck,
        'basic_encounter': basic_encounter_deck,
        'twist': twist_deck,
        'final_encounter': final_encounter_deck
    }

    print("\n✅ All decks loaded. Type 'help' for commands.\n")

    while True:
        cmd = input(">> ").strip().lower()

        if cmd in ['exit', 'quit']:
            print("👋 Exiting game.")
            break

        elif cmd == 'help':
            print("""
🎮 Commands:
  draw [deck]              - Draw one card from the specified deck
  view [deck]              - View all cards remaining in the deck
  reshuffle [deck]         - Reshuffle the deck (refill from CSV)
  decks                    - List all available decks
  quit / exit              - Exit the program
""")
        elif cmd.startswith("draw "):
            parts = cmd.split()
            if len(parts) == 2:
                deck_name = parts[1]
                draw_count = 1
            elif len(parts) == 3:
                deck_name = parts[1]
                dice_or_number = parts[2]
                if dice_or_number.isdigit():
                    draw_count = int(dice_or_number)
                else:
                    draw_count = parse_dice(dice_or_number)
                    if draw_count is None:
                        print(f"❌ Invalid dice notation: '{dice_or_number}'")
                        continue
            else:
                print("❌ Usage: draw [deck] [number|XdY]")
                continue

            if deck_name not in deck_state:
                print(f"❌ Deck '{deck_name}' not found.")
                continue

            deck = deck_state[deck_name]
            if not deck:
                print(f"⚠️ Deck '{deck_name}' is empty.")
                continue

            draw_count = min(draw_count, len(deck))
            print(f"🎴 Drawing {draw_count} from '{deck_name}':")
            for _ in range(draw_count):
                card = deck.pop(0)
                print_card(card, deck_name)
        elif cmd.startswith("view "):
            parts = cmd.split(maxsplit=1)
            if len(parts) != 2:
                print("❌ Usage: view [deck]")
                continue

            deck_name = parts[1]
            if deck_name not in deck_state:
                print(f"❌ Deck '{deck_name}' not found.")
                continue

            deck = deck_state[deck_name]
            print(f"🔎 {deck_name} ({len(deck)} cards remaining):")
            if not deck:
                print("⚠️ Deck is empty.")
            for card in deck:
                print_card(card, deck_name)
        elif cmd.startswith("reshuffle "):
            _, deck_name = cmd.split(maxsplit=1)
            if deck_name == 'villager':
                deck_state['villager'] = build_villager_deck(villager_file, v_count)
            elif deck_name == 'enemy':
                deck_state['enemy'] = build_enemy_deck(enemy_file, e_count)
            elif deck_name == 'boss':
                deck_state['boss'] = build_boss_deck(boss_file, b_count)
            elif deck_name == 'weapon':
                deck_state['weapon'] = build_weapon_deck(weapons_file, w_count)
            elif deck_name == 'basic_encounter':
                deck_state['basic_encounter'] = build_basic_encounter_deck(basic_encounters_file, be_count)
            elif deck_name == 'twist':
                deck_state['twist'] = build_twist_deck(twists_file, t_count)
            elif deck_name == 'final_encounter':
                deck_state['final_encounter'] = build_final_encounter_deck(final_encounters_file, fe_count)
            else:
                print("❌ Unknown deck.")
                continue
            print(f"🔁 Reshuffled {deck_name}.")

        elif cmd == "decks":
            print("📦 Available decks:")
            for name in deck_state:
                print(f" - {name} ({len(deck_state[name])} remaining)")

        else:
            print("❓ Unknown command. Type 'help' for available options.")
    
    

if __name__ == "__main__":
    main()
