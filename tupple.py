tuple_1=("OJJ","OKK","aaa","ASD","ytrt")
y=list(tuple_1)
y.append("NAA")
b=tuple(y)
print(b)

#unpasck tuple Data
tuple_1=("OJJ","OKK","aaa","ASD","ytrt")
(a,*b)=tuple_1
print(b)

#Tuple loop
tup_12=(1,2,3,4,5,6,7,0,0,0,8,9,0)
for i in range(len(tup_12)):
    print(i)

    print("Tupple method")
    ik=tup_12.count(0)
    print(ik)

print("method")
print(tup_12.index(0))