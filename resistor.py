#This to make resistor  

#the lists
List = [] 
lis= []

def resistor_s(a, n):
    List.append(a) 
    if len(List) >= 1 :
        lis.append(List[n])      
        return (sum(lis))

List2 = []
lis2 = []
R1, R2 = 0, 0

def resistor_p(a, n):
    List2.append(a)

    if len(List2) == 2:
        R1 = List2[0]
        R2 = List2[1]
        r = (R1 * R2) / (R1 + R2) 
        return r
    elif len(List2) >= 3:
        print(List2)
        for i in range(len(List2)):
            lis2.append(1 / List2[i])
        r = 1 / sum(lis2)
        return r

#test
#resistor_p(220,0)
#print(resistor_p(360,1))
#resistor_s(220,0)
#print(resistor_s(360,1))
