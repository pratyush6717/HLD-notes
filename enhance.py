import os
import glob
import re
from pathlib import Path

base_dir = r"c:\Users\praty\Coding\HLD-notes"
html_files = [str(p) for p in Path(base_dir).rglob("*.html")]

wrapper_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HLD Note</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
            --color-background-primary: #0f172a;
            --color-background-secondary: #1e293b;
            --color-text-primary: #f8fafc;
            --color-text-secondary: #cbd5e1;
            --color-text-tertiary: #94a3b8;
            --color-border-primary: #3b82f6;
            --color-border-secondary: #334155;
            --color-border-tertiary: #475569;
        }

        @media (prefers-color-scheme: light) {
            :root {
                --color-background-primary: #f8fafc;
                --color-background-secondary: #ffffff;
                --color-text-primary: #0f172a;
                --color-text-secondary: #475569;
                --color-text-tertiary: #64748b;
                --color-border-primary: #2563eb;
                --color-border-secondary: #cbd5e1;
                --color-border-tertiary: #e2e8f0;
            }
        }

        body {
            font-family: var(--font-sans) !important;
            background-color: var(--color-background-primary) !important;
            color: var(--color-text-primary) !important;
            margin: 0 !important;
            padding: 2rem 1rem !important;
            line-height: 1.6 !important;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            max-width: 900px !important;
            margin: 0 auto !important;
            background: transparent !important;
        }
        
        /* Modern aesthetic enhancements */
        .box, .card, .sub-panel, .cap-card, .scenario-box, .highlight, .pain, .cure, .insight-box, .path-box, .decision-card {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        }

        .box:hover, .cap-card:hover, .scenario-box:hover, .decision-card:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
        }

        button, .nav-btn, .sub-btn {
            box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
            touch-action: manipulation;
        }
        
        button:hover, .nav-btn:hover, .sub-btn:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }

        .section-title {
            color: var(--color-border-primary) !important;
            font-weight: 600 !important;
            letter-spacing: 0.1em !important;
        }
        
        .box-title, .cap-card-title {
            font-weight: 600 !important;
            letter-spacing: -0.01em !important;
        }
        
        .compare-table th {
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
            background-color: var(--color-background-secondary) !important;
        }

        /* Back Button Style */
        .back-btn {
            display: inline-flex;
            align-items: center;
            text-decoration: none;
            color: var(--color-text-primary);
            font-weight: 500;
            font-size: 14px;
            padding: 8px 16px;
            background: var(--color-background-secondary);
            border-radius: 8px;
            border: 1px solid var(--color-border-tertiary);
            transition: all 0.2s;
            margin-bottom: 2rem;
        }
        .back-btn:hover {
            border-color: var(--color-border-primary);
            color: var(--color-border-primary);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            body {
                padding: 1rem 0.5rem !important;
            }
            .grid, .grid-3, .two-col, .path-diagram, .decision-strip {
                display: flex !important;
                flex-direction: column !important;
                gap: 1rem !important;
            }
            .sub-nav, .nav {
                justify-content: center !important;
                gap: 0.5rem !important;
            }
            .compare-table {
                display: block !important;
                width: 100% !important;
                overflow-x: auto !important;
                -webkit-overflow-scrolling: touch;
            }
            .box, .cap-card, .scenario-box, .decision-card {
                width: 100% !important;
                box-sizing: border-box !important;
            }
            .flow-row, .node-row {
                flex-wrap: wrap !important;
                justify-content: center !important;
            }
        }
    </style>
</head>
<body>
<div class="container" style="padding: 0 !important; max-width: 900px; margin: 0 auto; text-align: left;">
    <a href="../index.html" class="back-btn">
        &larr; Back to Index
    </a>
</div>
"""

wrapper_end = """
</body>
</html>
"""

count = 0
for filepath in html_files:
    if "index.html" in filepath and Path(filepath).parent == Path(base_dir):
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    # Extract original content
    # If the file was already wrapped in our previous step, unwrap it
    match = re.search(r'&larr; Back to Index\s*</a>\s*</div>(.*)</body>', text, re.DOTALL)
    if match:
        original_content = match.group(1).lstrip()
    else:
        # If it wasn't wrapped for some reason, use the whole text
        original_content = text
        # If there's an existing DOCTYPE or <html>, it might break compilation, but our previous run already caught these.
        # Just in case:
        original_content = re.sub(r'<!DOCTYPE html>', '', original_content, flags=re.IGNORECASE)
        original_content = re.sub(r'<html.*?>', '', original_content, flags=re.IGNORECASE|re.DOTALL)
        original_content = re.sub(r'</html>.*', '', original_content, flags=re.IGNORECASE|re.DOTALL)
        original_content = re.sub(r'<body.*?>', '', original_content, flags=re.IGNORECASE|re.DOTALL)
        original_content = re.sub(r'</body>', '', original_content, flags=re.IGNORECASE)
        original_content = re.sub(r'<head>.*?</head>', '', original_content, flags=re.IGNORECASE|re.DOTALL)

    original_content = original_content.strip()

    with open(filepath, 'w', encoding='utf-8') as f:
        dir_name = Path(filepath).parent.name
        pretty_title = dir_name.replace('_', ' ').title()
        
        rel_base = os.path.relpath(base_dir, start=os.path.dirname(filepath)).replace('\\', '/')
        back_href = f"{rel_base}/index.html"
        html_start = wrapper_start.replace("<title>HLD Note</title>", f"<title>{pretty_title} - HLD Note</title>")
        html_start = html_start.replace('href="../index.html"', f'href="{back_href}"')
        
        f.write(html_start + "\n" + original_content + "\n" + wrapper_end)
        count += 1

print(f"Processed {len(html_files)} files. Updated {count} files for mobile responsiveness successfully.")
