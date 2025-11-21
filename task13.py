myCustomers = ["Raj","Ansh","dev","sanj","ayush"]
count = 0
for x in myCustomers:
    filename = f"file-0{count}.txt"
    with open(filename, 'w') as file:
        file.write(f"Hello, {x}!")
        count += 1
        
print("All files created successfully.")