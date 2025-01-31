import os

folder_path = 'c:/Users/sandr/OneDrive/Desktop/task-6/Type B'

try:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            reversed_lines = []
            for line in lines:
                words = line.split()
                reversed_words = [word[::-1] for word in words]
                reversed_line = ' '.join(reversed_words)
                reversed_lines.append(reversed_line)

            print(f"Reversed words in '{filename}':")
            for reversed_line in reversed_lines:
                print(reversed_line)
            print()

except FileNotFoundError:
    print(f"Folder '{folder_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
