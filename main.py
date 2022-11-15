# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def roll_dice(num_dice: int) -> list:
    roll_results = [random.randint(1, 6) for i in range(num_dice)]
    return roll_results


def parse_input(input_string: str) -> int:
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6")
        raise SystemExit(1)


def generate_dice_faces_diagram(dice_values):
    dice_faces = [DICE_ART[value] for value in dice_values]

    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")
    return "\n".join([diagram_header]+dice_faces_rows)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)
    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    print(f"\n{dice_face_diagram}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
