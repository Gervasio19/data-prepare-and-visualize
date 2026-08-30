import json

with open('Project1_OnlineRetail_Student_Lessons1-3.ipynb') as f:
    data = json.load(f)

new_source = [
    "# G1\n",
    "display(retail_clean[retail_clean['Country'].isin(['France', 'Germany', 'Spain'])])\n",
    "\n",
    "# G2\n",
    "display(retail_clean[(retail_clean['Country'] == 'United Kingdom') & (retail_clean['TotalAmount'] >= 500)])\n",
    "\n",
    "# G3\n",
    "display(retail_clean[(retail_clean['Quantity'] > 100) & (retail_clean['Price'] > 10)])\n",
    "\n",
    "# G4\n",
    "display(retail_clean.iloc[:10, :4])\n",
    "\n",
    "# G5\n",
    "display(retail_clean.loc[retail_clean['TotalAmount'] >= 200, ['Invoice', 'StockCode', 'Quantity', 'Price', 'TotalAmount']])\n"
]

data['cells'][29]['source'] = new_source

with open('Project1_OnlineRetail_Student_Lessons1-3.ipynb', 'w') as f:
    json.dump(data, f, indent=1)

print("Part G completed.")
