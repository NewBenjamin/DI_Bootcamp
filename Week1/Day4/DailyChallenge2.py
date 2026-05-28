MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

matrix = []
lines = MATRIX_STR.strip().split('\n')
for line in lines:
    matrix.append(list(line))

decoded_message = ""
num_cols = len(matrix[0]) if matrix else 0

for col in range(num_cols):
    column_chars = []
    for row in range(len(matrix)):
        if col < len(matrix[row]):
            char = matrix[row][col]
            column_chars.append(char)
    
    for char in column_chars:
        if char.isalpha():
            if decoded_message and not decoded_message[-1].isspace():
                if column_chars[column_chars.index(char) - 1] and not column_chars[column_chars.index(char) - 1].isalpha():
                    decoded_message += " "
            decoded_message += char
        elif decoded_message and decoded_message[-1].isalpha():
            decoded_message += " "

print(decoded_message.strip())