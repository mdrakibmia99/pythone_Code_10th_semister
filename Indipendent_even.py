N=[1,2,3,4,5,6,7,8,9,10]
A=[1,2,3,4,5,6]
B=[2,4,6,8,10]

P_of_A=round((len(A)/len(N)),2)
P_of_B=round((len(B)/len(N)),2)

#let R.H.S
PA_PB = P_of_A * P_of_B

#L.H.S
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