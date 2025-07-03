import os

# Folder name
folder = "python-everything_is_object"
os.makedirs(folder, exist_ok=True)

files_content = {
    "0-answer.txt": "type\n",
    "1-answer.txt": "id\n",
    "2-answer.txt": "No\n",
    "3-answer.txt": "Yes\n",
    "4-answer.txt": "Yes\n",
    "5-answer.txt": "No\n",
    "6-answer.txt": "True\n",
    "7-answer.txt": "True\n",
    "8-answer.txt": "True\n",
    "9-answer.txt": "True\n",
    "10-answer.txt": "True\n",
    "11-answer.txt": "False\n",
    "12-answer.txt": "True\n",
    "13-answer.txt": "True\n",
    "14-answer.txt": "[1, 2, 3, 4]\n",
    "15-answer.txt": "[1, 2, 3]\n",
    "16-answer.txt": "1\n",
    "17-answer.txt": "[1, 2, 3, 4]\n",
    "18-answer.txt": "[1, 2, 3]\n",
    "19-copy_list.py": "def copy_list(l):\n    return l[:]\n",
    "20-answer.txt": "Yes\n",
    "21-answer.txt": "Yes\n",
    "22-answer.txt": "No\n",
    "23-answer.txt": "Yes\n",
    "24-answer.txt": "True\n",
    "25-answer.txt": "True\n",
    "26-answer.txt": "True\n",
    "27-answer.txt": "No\n",
    "28-answer.txt": "Yes\n",
    "100-magic_string.py": (
        "def magic_string(l=[]):\n"
        "    l += [\"BestSchool\"]\n"
        "    return ', '.join(l)\n"
    ),
    "101-locked_class.py": (
        "class LockedClass:\n"
        "    __slots__ = ('first_name',)\n"
    ),
    "103-line1.txt": "1\n",
    "103-line2.txt": "0\n",
    "104-line1.txt": "1\n",
    "104-line2.txt": "0\n",
    "104-line3.txt": "No\n",
    "104-line4.txt": "No\n",
    "104-line5.txt": "1\n",
    "105-line1.txt": "104\n",
    "106-line1.txt": "1\n",
    "106-line2.txt": "0\n",
    "106-line3.txt": "No\n",
    "106-line4.txt": "No\n",
    "106-line5.txt": "1\n",
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"All files created in ./{folder}/\nNow zip the folder and upload as needed!")
