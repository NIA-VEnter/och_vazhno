def SS():
    arr_a = []
    a = input("num is")
    b = input("command is")
    try:
        a1 = int(a)
    except:
        a1 = 1
    len_a = len(a)
    count_a = 0
    final_int = 0



#from 2 to 10
    if b == "210":
        for i in range(len_a):
            arr_a.append(a1 % 10)
            a1 = a1 // 10



        for i in arr_a:
            if i == 0:
                count_a += 1
                continue



            stepen = 2 ** count_a
            ii = i * stepen
            final_int = final_int + ii
            count_a +=1





#from 8 to 10
    elif b == "810":
        for i in range(len_a):
            arr_a.append(a1 % 10)
            a1 = a1 // 10

        for i in arr_a:
            if i == 0:
                count_a += 1
                continue

            stepen = 8 ** count_a
            ii = i * stepen
            final_int = final_int + ii
            count_a += 1





#not done
    elif b == "1610":
        for i in range(len_a):
            arr_a.append(a1 % 10)
            a1 = a1 // 10

        for i in arr_a:
            if i == 0:
                count_a += 1
                continue

            stepen = 8 ** count_a
            ii = i * stepen
            final_int = final_int + ii
            count_a += 1








#from 10 to 2
    elif b == "102":
        while a1 != 0:
            arr_a.append(a1 % 2)
            a1 = a1 // 2


        arr_a1 = arr_a[::-1]
        arr_astr = [str(i) for i in arr_a1]


        arr_a1str = "".join(arr_astr)
        final_int = int(arr_a1str)



    # from 10 to 8
    elif b == "108":
        while a1 != 0:
            arr_a.append(a1 % 8)
            a1 = a1 // 8

        arr_a1 = arr_a[::-1]
        arr_astr = [str(i) for i in arr_a1]

        arr_a1str = "".join(arr_astr)
        final_int = int(arr_a1str)






    #NOT DONE
    elif b == "1016":
        while a1 != 0:
            arr_a.append(a1 % 8)
            a1 = a1 // 8


        arr_a1 = arr_a[::-1]
        arr_astr = [str(i) for i in arr_a1]


        arr_a1str = "".join(arr_astr)
        final_int = int(arr_a1str)










    print(final_int)


a = ""
while a != "end":
    SS()
    a = input("end")

