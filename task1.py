my_poly = {0: -10, 2: 3, 4: 1}

def evaluate_polynomial(poly_dict, x):
    result = 0
    for key, value in poly_dict.items():
        result += value * (x ** key)
    return result
print(evaluate_polynomial(my_poly, 2))
print(evaluate_polynomial(my_poly, -1.5))