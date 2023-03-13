def greedy_algorithm(list1):

    maxlen = len(list1)
    temp1 = list()
    temp2 = list()
    temp3 = list()
    temp4 = list()
    temp5 = list()
    temp6 = list()
    temp7 = list()
    for i in range(0,maxlen):
        temp1.append(list1[i])
    for d in range(0,maxlen):
        j = d +1
        if j < maxlen:
            temp3.append(temp1[j])
        temp2.append(temp1[d])
    for n in range(0, maxlen):
        o = n + 1
        p = n + 2
        if o < maxlen:

            if len(list1[n]) >= len(list1[n+1]):
                maxlen2 = len(list1[n])
            elif len(list1[n]) < len(list1[n+1]):
                maxlen2 = len(list1[n+1])
        if p < maxlen:
            if maxlen2 < len(list1[n+2]):
                maxlen2 = len(list1[n+2])




    for f in range(0, maxlen-1):
        temp2.append(temp3[f])
    for g in range(0, maxlen):
        temp4.append(temp2[g])
        s = g + maxlen
        if s < 2*maxlen -1 :
            temp4.append(temp2[s])
    for k in range(0, (2*maxlen -1)):
        w = k +1
        if w < 2*maxlen -1:
            if temp4[k][0:] != temp4[k+1][::-1]:
                temp5.append(temp4[k][0:])
            elif temp4[k][0:] == temp4[k+1][::-1]:
                temp5.append(temp4[k][0:])
    for l in range(0, ((2 * maxlen)- 2)):
        w = l + 1

        for m in range(0,maxlen2):
            u = m+1
            x = m-1
            z = -(u+1)
            f = -(u-1)
            if w < ((2 * maxlen) - 2) and u < (maxlen2+2):

                if -(maxlen2+1) <z < (maxlen2+2) and -(maxlen2+1)< x < (maxlen2+2) and -(maxlen2+1)<f <(maxlen2+2):
                    if temp5[l][m] != temp5[w][-(u)]:
                        if temp5[l] != temp5[w]:
                            if temp5[l][u] == temp5[w][z] or temp5[l][x] == temp5[w][f]:
                                temp6.append(temp5[l][m])
                                print('aaa')
                        # temp6.append(temp5[w][-u])

                elif temp5[l][m] == temp5[w][-(u)]:
                    if temp5[l] != temp5[w]:
                        temp6.append(temp5[l][m])
                        temp6.append(temp5[w][-u+1])
                        print('bbb')

    print(temp1)
    print(temp2)
    print(temp3)
    print(temp4)
    print(temp5)
    print(temp6)
    print('maxlen2: ', maxlen2)
    print('maxlen: ', maxlen)
    t = ''.join(temp6)
    print('shortest_superstrings: ', t)

print(greedy_algorithm(['UV', 'VW', 'XY', 'YZ', 'Zd']))

