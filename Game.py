import random
import json
import os
import time

SCORE_FILE = "scores.json"

LEVELS = {
    "1": ("Easy", 50, 10),
    "2": ("Medium", 100, 7),
    "3": ("Hard", 200, 5),
}

def load_scores():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE) as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def choose_level():
    print("\nLevel chuno:")
    for key, (name, mx, att) in LEVELS.items():
        print(f"{key}. {name} (1-{mx}, {att} attempts)")
    while True:
        choice = input("Choice: ").strip()
        if choice in LEVELS:
            return LEVELS[choice]
        print("Sirf 1, 2 ya 3 likho!")

def hint(diff, max_num):
    if diff <= max_num * 0.05:
        return "🔥 Bahut garam!"
    elif diff <= max_num * 0.15:
        return "♨️ Garam"
    elif diff <= max_num * 0.30:
        return "🌤️ Thanda"
    return "🧊 Bahut thanda!"

def play(name):
    level, max_num, max_attempts = choose_level()
    number = random.randint(1, max_num)
    attempts = 0
    start = time.time()

    print(f"\n{name}, 1 se {max_num} ke beech guess karo!")
    print(f"Attempts: {max_attempts}\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess ({max_attempts - attempts} bache): "))
        except ValueError:
            print("Number likho! ❌")
            continue

        if not 1 <= guess <= max_num:
            print(f"1 se {max_num} ke beech likho!")
            continue

        attempts += 1

        if guess == number:
            secs = round(time.time() - start, 1)
            points = (max_attempts - attempts + 1) * 100 - int(secs)
            points = max(points, 10)
            print(f"\n🎉 Sahi! {attempts} attempts, {secs} sec")
            print(f"⭐ Points: {points}")
            return level, points

        direction = "Thoda bada 🔼" if guess < number else "Thoda chhota 🔽"
        print(f"{direction} | {hint(abs(guess - number), max_num)}")

    print(f"\n😢 Game over! Number tha {number}")
    return level, 0

def show_leaderboard(scores):
    if not scores:
        return
    print("\n🏆 Leaderboard")
    top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (player, pts) in enumerate(top, 1):
        print(f"{i}. {player} - {pts}")

def main():
    print("🎮 Number Guessing Game")
    name = input("Tumhara naam: ").strip().title() or "Player"
    scores = load_scores()

    while True:
        level, points = play(name)
        if points > scores.get(name, 0):
            scores[name] = points
            save_scores(scores)
            print("🔥 Naya personal best!")
        show_leaderboard(scores)

        if input("\nDobara? (y/n): ").lower() != "y":
            print(f"Thanks {name}! 👋")
            break

if __name__ == "__main__":
    main()
