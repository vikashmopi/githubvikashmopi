#name="123 sd d34 5 65 6436  3452 dsad46 5 62 wer6 45 5 66"

#write a function and also write a testcase 

#output : listformat only unique value,sort by asc to des []

#print(name.isdigit())
def get_unique_numbers(name):
    numbers = []

    for value in name.split():
        if value.isdigit():
            numbers.append(int(value))

    return sorted(set(numbers))

name = "123 sd d34 5 65 6436 3452 dsad46 5 62 wer6 45 5 66"

result = get_unique_numbers(name)

print(result)
