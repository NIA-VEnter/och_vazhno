arr_a = []
a = int(input())
a1 = a
len_a = len(str(a))
count_a = 0
final_int = 0

for i in range(len_a):
    arr_a.append(a1 % 10)
    a1 = a1 // 10

for i in arr_a:
    if i == 0:
        count_a += 1
        continue

    stepen = 2 ** count_a
    final_int = final_int + stepen
    count_a +=1
print(final_int)
