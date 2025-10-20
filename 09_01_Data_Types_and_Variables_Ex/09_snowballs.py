number_of_snowballs = int(input())
best_value = 0
best_weight = 0
best_time = 0
best_quality = 0

for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight // time) ** quality

    if value > best_value:
        best_value = value
        best_weight = weight
        best_time = time
        best_quality = quality

print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")
