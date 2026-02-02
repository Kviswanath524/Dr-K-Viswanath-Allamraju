'''file1 = open("D:\\IARE\\EPS.txt")
read_content = file1.read()
print(read_content)'''

'''file_path = r"D:\\IARE\\EPS.txt"  
with open(file_path, "r") as file:
    file_contents = file.read()  
print(file_contents)'''

'''with open(r'D:\IARE\EPS.txt', 'w') as file2:
    file2.write('Programming is Fun.\n')
    file2.write('Programiz for beginners\n')'''

'''file_path = r"D:\\IARE\\EPS.txt"  
with open(file_path, "w") as file:
    file.write("Hello, this is a new text file!\n")
    file.write("This line will be written in the file.\n")'''
'''import os

folder_path = r"D:\IARE\EPS3"
file_path = os.path.join(folder_path, "New.txt")

# Ensure the folder exists
os.makedirs(folder_path, exist_ok=True)

# Create the file
with open(file_path, "w") as file:
    file.write("This file was created successfully!\n")

print("File and folder created successfully!")'''

