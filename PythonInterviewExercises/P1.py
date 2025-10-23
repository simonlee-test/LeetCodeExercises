fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

randomDict : dict = {
    "F1" : "race", "Football" : "match", "Swimming" : "competition"
}

s : str = "F1"

if s in randomDict: #comparing with key value
    print("Yes") 

print(list(randomDict.keys()))
print(list(randomDict.values()))