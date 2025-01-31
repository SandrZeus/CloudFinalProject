def binary_to_ascii(binary_string):
    ascii_char = chr(int(binary_string, 2))
    
    return ascii_char

input_file_name = 'c:/Users/sandr/OneDrive/Desktop/task-6/TypeC'

with open(input_file_name, 'r') as file:
    binary_data = file.read().replace('\n', '')

binary_strings = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

ascii_text = ''.join([binary_to_ascii(binary_string) for binary_string in binary_strings])
print(ascii_text)
