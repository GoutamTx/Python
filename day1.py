''' Non local keyword is a keyword used for referring any variable to it's nearest scope 
(basically to refer a variable in nested function from the parent function)'''

'''LIST'''     # ordered,mutable,dupicate allowed,heterogenous

list1=["black","red","white","blue"]
print(len(list1)) #length
print(list1[1])  #accesing_element
list1.insert(2,"pink")
print(list1)  #inserting
list1.append("peach")
list2=["navy","cyan"]
list1.extend(list2)
print(list1)
list1.sort()
print(list1)
list1.append("red")
print(list1.count("red")) # counting a specified element
list1.pop()
list1.clear() # clear the list
del list1 # deletes the list(structure also)
# print(list1)  raises an error as there is nothing as list1

''' TUPLES '''     # ordered,immutable,dupicate allowed,heterogenous

tup=("black","red","white","blue","cyan")
print(len(tup))
print(tup[-1])
if "black" in tup:
    print("present")
# cannot add or remove items directly (first make it a list than back a tuple)
y=list(tup)
y.remove("black")
tup=tuple(y)

(apple,banana,*orange)=tup  # * is to unpack all the remaining values in the last object

print(orange)
x=tup.index("cyan")
print(x)
del tup


''' SETS'''    # unordered,unique,mutable

se={"black","pink","red","cyan"}
print(len(se))
for x in se:                                # cannot access element through index
    print(x)
print("black" in se)

se.add("blue")
se1={"apple","orange"}
se.update(se1)
print(se)
se.remove("apple")                     # if item is not present in the set REMOVE  will raise an error
print(se)

se.discard("phone")                    # DISCARD doesn't raise any error even if element is not present
print(se)

a=se.pop()                             # remove any random element
print(a)
se.clear()
print(se)
del se


m={"a","b","c",1,2}
n={1,2,3}
o=m.union(n)                                     # any data type can be unioned with sets
o=m | n                                  # only sets can be unioned
print(o)

m.update(n)
print(m)
o=m.intersection(n)                     # & can also be used instead of intersection
print(o)

o.clear()
o=m.difference(n)

print(o)



