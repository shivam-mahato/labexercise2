# 3.N studentstake K apples and distribute them amongeach student evenly.
# The remaining parts remain in the basket.
# How many apples will eachsingle student get?
# How many apples will remain in the basket?The program read the numbers N and K.


N = int(input("enter the number of students:"))
K = int(input("enter the number of apples"))

D = K//N
B = K%N

print(f"each student get {D} apples")
print(f"the remainig apples are{B}")
