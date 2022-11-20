N=[1,2,3,4,5,6,7,8,9,10]
A=[1,2,3,4,5,6,7]
B=[1,3,5,7,9]

P_of_A=round((len(A)/len(N)),2) #round(45456.5645,5)
P_of_B=round((len(B)/len(N)),2)

#let R.H.S
PA_PB = P_of_A * P_of_B

#R.H.S
A_intersection_B=[]
for i in range(0,len(A)):
    for j in range(0,len(B)):
         if(A[i]==B[j]):
            A_intersection_B.append(A[i])
P_intersection_AB=round((len(A_intersection_B)/len(N)),2)
print(PA_PB,"==",P_intersection_AB)
if(PA_PB == P_intersection_AB):
    print("Independent")
else:
    print("Not Independent")