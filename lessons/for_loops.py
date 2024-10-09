"""Practice of for loops"""

my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:
    new_list.append(elem)
print(new_list)

# pets example
pets: list[str] = ["Louie", "Bo", "Bear"]
output: str = "Good boy, "
for elem in pets:
    output += elem + "!"
    print(output)
    output = "Good boy, "
