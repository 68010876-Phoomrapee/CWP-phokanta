def average(class_scores):
    return sum(class_scores.values()) / len(class_scores)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
    # 18 + 15 + 8 + 9 = 50
    # 50 / 4 = 12.5
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
    # 17 + 15 + 8 + 13 = 53
    # 53 / 4 = 13.25
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")