downloaded = 0
cost = 0
income = 0
liste = [100, 42, 26, 19, 15, 12, 10, 9, 8, 7, 6]
index = 0
for i in range(50):
    liste.append(5)
for i in range(200):
    liste.append(2)

active_user = 0
ad_ratio = 0.138
while (cost < income):
    cost += 40000
    downloaded += 114285.7
    active_user = downloaded * liste[index] / 100
    income += active_user * ad_ratio
    index += 1

print(index+1)
