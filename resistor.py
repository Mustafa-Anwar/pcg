#This to make resistor  

#the lists
List = [] 
lis= []

def resistor_s(a, n):
    List.append(a) 
    if len(List) >= 1 :
        lis.append(List[n])
        b = sum(lis)
        return (sum(lis))

List2 = []
lis2 = []
R1, R2 = 0, 0


def resistor_p(a):
    List2.append(a)

    if len(List2) == 2:
        R1 = List2[0]
        R2 = List2[1]
        r = (R1 * R2) / (R1 + R2) 
        a = r
        return r
    elif len(List2) >= 3:
        print(List2)
        for i in range(len(List2)):
            lis2.append(1 / List2[i])
        r = 1 / sum(lis2)
        a = r
        return r
    

