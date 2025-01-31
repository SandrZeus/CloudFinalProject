import os

folder_path = 'c:/Users/sandr/OneDrive/Desktop/task-6/Type A'

try:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                equations = file.readlines()

            results = []
            for equation in equations:
                equation = equation.strip()
                if equation:
                    operands = equation.split()
                    result = eval(' '.join(operands))
                    results.append(result)

            print(f"Results for '{filename}':")
            for result in results:
                print(result)
            print()

except FileNotFoundError:
    print(f"Folder '{folder_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
