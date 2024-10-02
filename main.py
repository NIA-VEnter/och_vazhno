def SS(a, b):
    arr_a = []
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





    #from 10 to 16
    elif b == "1016":
        while a1 != 0:
            arr_a.append(a1 % 16)
            a1 = a1 // 16

        arr_a1 = arr_a[::-1]
        arr_a2 = []

        for i in arr_a1:
            if i == 10:
                arr_a2.append('A')
                continue

            elif i == 11:
                arr_a2.append('B')
                continue

            elif i == 12:
                arr_a2.append('C')
                continue

            elif i == 13:
                arr_a2.append('D')
                continue

            elif i == 14:
                arr_a2.append('E')
                continue

            elif i == 15:
                arr_a2.append('F')
                continue

            arr_a2.append(str(i))

        final_int = "".join(arr_a2)














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






    #FROM 16 TO 10
    elif b == "1610":
        for i in range(len_a):
            last_char = a[-1]
            a = a[:-1]

            if last_char == 'A':
                arr_a.append(10)

            elif last_char == 'B':
                arr_a.append(11)

            elif last_char == 'C':
                arr_a.append(12)

            elif last_char == 'D':
                arr_a.append(13)

            elif last_char == 'E':
                arr_a.append(14)

            elif last_char == 'F':
                arr_a.append(15)

            else:
                arr_a.append(int(last_char))



        for i in arr_a:
            if i == 0:
                count_a += 1
                continue

            stepen = 16 ** count_a
            ii = i * stepen
            final_int = final_int + ii
            count_a += 1









    print(final_int)


a = ""
while a != "end":
    a1 = input('num is ')
    b = input('command is ')
    SS(a1,b)
    a = input("end")

