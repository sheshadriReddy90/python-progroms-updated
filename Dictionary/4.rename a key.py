fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}
key=input()
new_key=input()
fruit_items=list(fruits.items())
fruit_items_copy=fruit_items.copy()
fruits_count=len(fruit_items)

for i in range(fruits_count):
    if fruit_items[i][0]==key:
        upadated_tuple=(new_key,fruit_items[i][1])
        fruit_items_copy[i]=upadated_tuple
print(fruit_items_copy)         