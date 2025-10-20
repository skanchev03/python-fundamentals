fire_and_cell = input()
water = int(input())
fire = 0
effort = 0
fire_and_cell_list = fire_and_cell.split("#")
print("Cells:")

for i in range(len(fire_and_cell_list)):
        fire_value_pair = fire_and_cell_list[i].split(" = ")
        type_of_fire = fire_value_pair[0]
        value = fire_value_pair[1]

        if type_of_fire == "Low" and 1 <= int(value) <= 50 or type_of_fire == "Medium" and 51 <= int(value) <= 80 or type_of_fire == "High" and 81 <= int(value) <= 125:
            water -= int(value)
            fire += int(value)
            if water < 0:
                water += int(value)
                fire -= int(value)
                continue
            print(f" - {value}")
            effort += int(value) * 0.25

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")
