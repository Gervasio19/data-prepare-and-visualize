import json

with open('Project1_OnlineRetail_Student_Lessons1-3.ipynb') as f:
    data = json.load(f)

for i in range(25, 35):
    if i < len(data['cells']):
        cell = data['cells'][i]
        src = "".join(cell['source']).strip()
        print(f"--- Cell {i} ({cell['cell_type']}) ---")
        print(src[:200])
        print("...")
