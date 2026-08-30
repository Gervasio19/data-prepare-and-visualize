import json

with open('Project1_OnlineRetail_Student_Lessons1-3.ipynb') as f:
    data = json.load(f)

for i, cell in enumerate(data['cells']):
    if cell['cell_type'] == 'markdown':
        src = "".join(cell['source']).strip().split('\n')[0]
        if 'Part G' in src:
            print(f"Cell {i}: {src}")
    elif cell['cell_type'] == 'code':
        # check around Part G
        pass
