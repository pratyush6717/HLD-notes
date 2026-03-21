import os
import re

base_dir = r"c:\Users\praty\Coding\HLD-notes"
index_file = os.path.join(base_dir, "index.html")

with open(index_file, 'r', encoding='utf-8') as f:
    idx_content = f.read()

# We want to replace the single <ul> section with two sections.
# Let's find the <ul> block.
match = re.search(r'<ul>(.*?)</ul>', idx_content, re.DOTALL)
if match:
    hld_list = match.group(1)
    
    new_html_sections = f"""
        <h2 style="color: var(--color-text-main); font-size: 1.8rem; border-bottom: 2px solid var(--color-border-tertiary); padding-bottom: 8px; margin-top: 10px; margin-bottom: 20px;">High-Level Design (HLD)</h2>
        <ul style="margin-bottom: 40px;">
{hld_list}
        </ul>

        <h2 style="color: var(--color-text-main); font-size: 1.8rem; border-bottom: 2px solid var(--color-border-tertiary); padding-bottom: 8px; margin-bottom: 20px;">Low-Level Design (LLD)</h2>
        <ul>
            <li>
                <a href="LLD/1.What is LLD/what_is_lld_notes.html">
                    <span class="number">1</span> What is LLD
                </a>
            </li>
        </ul>
"""
    
    # We replace the original <ul>...</ul> with our two lists.
    new_idx_content = idx_content.replace(f"<ul>{hld_list}</ul>", new_html_sections)
    
    # Let's also update the subtitle slightly
    new_idx_content = new_idx_content.replace("Complete Collection of High-Level Design Concepts", "Complete Collection of System Design Concepts (HLD & LLD)")
    new_idx_content = new_idx_content.replace("HLD Notes Directory", "System Design Notes Directory")
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_idx_content)
    
    print("Successfully updated index.html with HLD and LLD sections.")
else:
    print("Could not find the ul block in index.html to replace.")
