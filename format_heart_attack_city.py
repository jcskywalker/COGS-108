import re

h_atk_cty_file = open("heart_attack_city.txt", "r")
h_atk_str = h_atk_cty_file.read()
h_atk_lst = list(h_atk_str)
matches = re.finditer(" [0-9]+\. ", h_atk_str)
for m in matches:
    # print(h_atk_lst[m.start():m.end()])
    h_atk_lst[m.start()] = "\n"

for i in range(0, len(h_atk_lst)):
    if h_atk_lst[i] == " ":
	h_atk_lst[i] = ","


new_h_atk_str = "".join(h_atk_lst)
print(new_h_atk_str)
