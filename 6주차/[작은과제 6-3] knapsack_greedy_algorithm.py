def get_optimal_value(capacity, weights, values, names):
    size = len(weights)
    vpw = [(values[i] / weights[i], weights[i], names[i]) for i in range(size)]
    densities = sorted(vpw, reverse = True)
    finalValue = 0
    for i, v in enumerate(densities):
        a = min(capacity, densities[i][1])
        finalValue += a * densities[i][0]
        print(densities[i][2], a, "gram is taken") 
        capacity -= a
    return finalValue

capacity = 170
values = [200000,650000,95000,570000,900000,450000,550000,370000,90000,730000]
weights = [25,35,23,20,10,15,20,12,30,25]
names = ["은", "금", "자수정", "오팔","다이아몬드","에메랄드","루비","사파이어","청동","아쿠아마린"]
opt_value = get_optimal_value(capacity, weights, values, names)
print("Value of the knapsack is", opt_value)
