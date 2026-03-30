import os

INPUT="/Users/oksanaafanaseva/Desktop/python-for-big-data-and-data-science-1/project_template/data/input.txt"
def read_data():
    data = []
    if not os.path.exists(INPUT):
        print(f"File not found: {INPUT}")
        return []
    with open(INPUT, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 4:
                surname = parts[0]
                name = parts[1]
                age = int(parts[2])
                year = int(parts[3])
                data.append((surname, name, age, year))
    return data
