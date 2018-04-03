#This to make resistor
List = [[0,0]]
NewList = []
a = 0
lis=[]
def resistor_s(a, n): 

    List.append(a) 
    if len(List) >= 1:
        print(List)
        lis.append(List[n])      
        print ("it's : ",sum(lis))
    
resistor(480, 1)
resistor(300, 2)
resistor(220, 3)
