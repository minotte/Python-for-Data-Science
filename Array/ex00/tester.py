from give_bmi import give_bmi, apply_limit


print("test 1:")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("test 2:")
try:
    height = [2.71, "sju"]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

except Exception as e:
    print("Error:", e)

print("test 3:")
try:
    height = [2.71, 1.15]
    weight = [165.3, -38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit([1, -1, 8], 26))

except Exception as e:
    print("Error:", e)

print("test 4:")
try:
    height = [2.71, 1.15]
    weight = [165.3, 38.4, 54]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(-1, 26))

except Exception as e:
    print("Error:", e)
