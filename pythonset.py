#Lectures by Ravula Govardhan - #Subscribe and hit #bell.
#------------------------------------------------------------
#python set operations
#we'll use the setA and setB for our illustration
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}

#union operations
print(setA)
print(setB)
print(len(setA))
print(len(setB))

print(setA | setB)

#python set example using the union() method
print(setA.union(setB))
print(len(setA.union(setB)))

print(setB.union(setA))
print(len(setB.union(setA)))

#---------------------------------------------
#intersection operation
#python intersection example using the & operator 
print(setA)
print(len(setA))

print(setB)
print(len(setB))

print(setA & setB)

#python set example using the intersection method 
print(setA.intersection(setB))
print(len(setA.intersection(setB)))

print(setB.intersection(setA))
print(len(setB.intersection(setA)))

#-------------------------------------------
#difference operation
#python set's difference operation 
print(setA - setB)
print(len(setA - setB))

print(setB - setA)
print(len(setB - setA))

#python set's difference operation using the difference() method
print(setA.difference(setB))
print(len(setA.difference(setB)))

print(setB.difference(setA))
print(len(setB.difference(setA)))

#-------------------------------------
#symmetric difference
#python set example using the caret (^) operator
print(setA ^ setB)
print(len(setA ^ setB))

print(setB ^ setA)
print(len(setB ^ setA))

#python set example using the symmetric_difference() method
print(setA.symmetric_difference(setB))
print(len(setA.symmetric_difference(setB)))

print(setB.symmetric_difference(setA))
print(len(setB.symmetric_difference(setA)))