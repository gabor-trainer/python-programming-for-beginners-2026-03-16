def get_result_text(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


prices = [100, 250, 50, 300, 75]
person = {"name": "Alice", "age": 30, "city": "New York"}


discounted = []
for price in prices:
    discounted.append(price * 0.9)


discounted = [price * 0.9 for price in prices]

x = [v for k, v in person.items()]


scores = [85, 42, 91, 67, 55, 78, 95, 38]
passing = [score for score in scores if score >= 60]
print(passing)
print(discounted)


scores = [85, 42, 91, 67, 55, 78, 95, 38]
labels = [get_result_text(score) for score in scores]

labels = []
for score in scores:
    labels.append("Pass" if score >= 60 else "Fail")
print(labels)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
flat = [value for row in matrix for value in row]

result = [[v*2 for v in row] for row in matrix]
print(result)
# print(flat)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] *= 2

result = []
for row in matrix:
    result_row = []
    for value in row:
        result_row.append(value * 2)
    result.append(result_row)        


products = ["Apples", "Bananas", "Cherries"]
prices = [25, 15, 40]

x = zip(products, prices)

catalog = {product: price for product, price in zip(products, prices)}
print(catalog)
