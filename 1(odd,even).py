N=int(input("Enter an integer:"))
oddTotal=0
evenTotal=0
evenCount=0

for i in range (1,N+1):
    if i %2==0 :
        evenTotal=evenTotal + i
        evenCount=evenCount+1
        avg=evenTotal/evenCount
    else:
         oddTotal=oddTotal+i

print("the sum of odd numbers starting from 1 up to and including", N , "is:" , oddTotal)
print("the average of the even numbers starting from 1 up to and including" , N , "is:", avg)