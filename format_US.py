import re

US_file = open("US.txt", "r")
US_str = US_file.read()
US_lst = list(US_str)

for i in range(0, len(US_lst)):
    if US_lst[i] == "|":
	US_lst[i] = ","


new_h_atk_str = "".join(US_lst)
print(new_h_atk_str)
