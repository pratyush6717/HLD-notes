import os
import glob
import re
from pathlib import Path

base_dir = r"c:\Users\praty\Coding\HLD-notes"
index_file = os.path.join(base_dir, "index.html")

# Fix index.html
if os.path.exists(index_file):
    with open(index_file, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    # Replace href="1.Network..." to href="HLD/1.Network..."
    new_idx_content = re.sub(r'href="(\d+\.[^"]+)"', r'href="HLD/\1"', idx_content)
    
    if new_idx_content != idx_content:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_idx_content)
        print("Updated index.html links to point to HLD/ directory.")

# Fix back buttons in the notes
note_files = glob.glob(os.path.join(base_dir, "HLD", "*", "*.html"))
count = 0
for filepath in note_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    old_back_link = 'href="../index.html"'
    new_back_link = 'href="../../index.html"'
    if old_back_link in content:
        content = content.replace(old_back_link, new_back_link)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated back links in {count} note files.")
