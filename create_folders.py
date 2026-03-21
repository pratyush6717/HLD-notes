import os
import re

raw_data = """4. Strategy Design Pattern (Behavioral Pattern)
7min
Play
5. Observer Pattern (Behavioral Pattern)
18min
Play
6. Decorator Design Pattern (Structural Design Pattern)
17min
Play
7. Factory & Abstract Factory pattern (Creational Design Pattern)
25min
Play
8. Design Parking Lot (English Dubbed)
58min
Play
9. Design Tic-Tac-Toe Game
25min
Play
10. LLD of Elevator System
1hr 27min
Play
11. LLD of Car Rental System
54min
Play
12. Chain Of Responsibility Design Pattern (Behavioral Design Pattern)
12min
Play
13. LLD of Snake n Ladder Game
51min
Play
14. Proxy Design Pattern (Structural Pattern)
9min
Play
15. LLD of BookMyShow | Design Movie Ticket Booking App
46min
Play
16. Null Object Design Pattern (Behavioral Pattern)
9min
Play
17. State Design Pattern (Behavioral) | Design Vending Machine
31min
Play
18. LLD of ATM
45min
Play
19. Composite Pattern (Structural Design Pattern)
21min
Play
20. Adapter Pattern (Structural Design Pattern)
17min
Play
21. LLD of Splitwise
50min
Play
22. Builder Design Pattern (Creational Design Pattern)
27min
Play
23. LLD of Cricbuzz
39min
Play
24. Facade Design Pattern (Structural Design Pattern)
23min
Play
25. Bridge Design Pattern (Structural Design Pattern)
19min
Play
26. LLD of Inventory Management System
39min
Play
27. Flyweight Design Pattern (Structural Design Pattern)
31min
Play
28. Command Design Pattern (Behavioral Design Pattern)
18min
Play
29. Iterator Design Pattern (Behavioral Design Pattern)
18min
Play
30. Mediator Design Pattern (Behavioral Design Pattern)
20min
Play
31. LLD of Apply Coupons on Shopping Cart Products
19min
Play
32. Visitor Design Pattern (Behavioral Design Pattern)
33min
Play
33. MVC Design Pattern
15min
Play
34. Memento Design Pattern (Behavioral Design Pattern)
15min
Play
35. Template Method Design Pattern (Behavioral Design Pattern)
13min
Play
36. Interpreter Pattern (Behavioral Design Pattern)
17min
Play
37. LLD of Payment Gateway
47min
Play
38. Object Pool Design Pattern (Creational Design Pattern)"""

lines = raw_data.split('\n')
folders = []

for line in lines:
    line = line.strip()
    if re.match(r'^\d+\.', line):
        # Remove characters not allowed in Windows folder names e.g. |, ?, <, >, *, ", \
        folder_name = re.sub(r'[<>:"/\\|?*]', '', line)
        folders.append(folder_name)

base_lld_dir = r"c:\Users\praty\Coding\HLD-notes\LLD"
os.makedirs(base_lld_dir, exist_ok=True)

created_count = 0
for folder in folders:
    folder_path = os.path.join(base_lld_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    notes_file = os.path.join(folder_path, "notes")
    if not os.path.exists(notes_file):
        with open(notes_file, 'w', encoding='utf-8') as f:
            pass # Just create an empty file
        created_count += 1

print(f"Successfully processed {len(folders)} folders and created {created_count} empty 'notes' files.")
