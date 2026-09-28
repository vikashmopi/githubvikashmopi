def unique_value(name): # "ab1 cd3 ,b2 1e4 41,ab" ,[1,2,3,4]
    numbers=[]#[1,1,4,4,1]
    for item in name.replace("/"," ").split():#"ab1 cd3 b2 1e4 41 ab",["ab1","ab",cd3","b2","1e4","41","ab"]
        print("item:",item)
        if item.isdigit():
            numbers.append(int(item))
            break

        for char in item: #"41"  ,"1"
            print("char:",char)
            digit=""#
            if char.isdigit():#true,true
                digit=digit+char #digit=""+"1"
            if digit:#1
               numbers.append(int(digit))
               print("number:",numbers)
    return sorted(set(numbers))

result=input("enter the value:")
print(unique_value(result))


            