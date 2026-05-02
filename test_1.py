print("1st commit")
# Use end parameter to change what comes after each print statement
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')  # Use '-' instead of newline
    # Use sep parameter to specify separator between multiple arguments
print('cats', 'dogs', 'mice', sep=',')  # Comma-separated output
print('cats', 'dogs', 'mice', sep=',')  # Comma-separated output
# input() can display a prompt message directly
my_name = input('What is your name? ')  # Prompt and read in one call
print(f'Hi, {my_name}')  # f-string for string formatting

