age1 = {"まつだ": 20, "すずき": 29, "わたべ": 30, "やまだ": 25}
age2 = {"やまぐち": 15, "まつだ": 30, "いちかわ": 21}

keys_to_update = []
for i in list(age1.keys()):  # Create a list of keys to iterate over
    for j in age2:
        if i == j:  # Same key found
            keys_to_update.append(i)
            break

for key in keys_to_update:
    age1[key] = age2[key]

age1.update(age2)

print(age1)