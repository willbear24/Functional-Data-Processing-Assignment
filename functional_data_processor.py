from functools import reduce

products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]

in_stock = [i for i in products if i["in_stock"] == True]

discounted_price = list(map(lambda p: {**p, "discounted_price": round(p["price"] * 0.9, 2)}, products))


sub_two_hundred = list(filter(lambda p: p["price"] <= 200 and p["in_stock"] == True, products))

sort_by_price = sorted(products, key=lambda p: p["price"])

total_stock_value = sum(p["price"] for p in products if p["in_stock"])

grouped = reduce(
    lambda acc, p: {**acc, p["category"]: acc.get(p["category"], []) + [p]},
    products,
    {}
)

print("-" * 50)
print(f"All products: {products}")
print("-" * 50)
print(f"In stock products: {in_stock}")
print("-" * 50)
print(f"Product list with discounted prices added: {discounted_price}")
print("-" * 50)
print(f"Products less than $200: {sub_two_hundred}")
print("-" * 50)
print(f"Productes sorted by price: {sort_by_price}")
print("-" * 50)
print(f"Total In Stock Value: ${total_stock_value}")
print("-" * 50)
print(f"Products sorted by group: {grouped}")
