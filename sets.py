---
YamlDesc: CONTENT-ARTICLE
Title: python sets
MetaDescription: python sets, set operations, set functions example code, tutorials
MetaKeywords: python sets, set operations, set functions example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: sets
---

# Python Sets
* Sets are lists with no duplicate entries.
* Sets are unordered and are iterable with has no duplicate elements.
* Set are ideal over lists where there is a need to check for a spcific 
  element is a list of data.
* Set stores data as a hash table, hence its more efficient for searching 
  an element in it.
* There are Immutable and Mutable sets
* Below is a demonstration of a Mutable or changable set
>

## Creating a Set, Adding elements to a Set
```python
# Create a new set "S1"
set1 = {1,2,3,4}
print(set1)

# Create a SET "s1" from a LIST of STRING datatype elements
# Create a new set "S1"
set1 = {1,2,3,4}
s1 = set(["USA", "CHINA", "INDIA",])
print(s1)

# Add an element to a set using the ADD function
# Create a new set "S1"
set1 = {1,2,3,4}
s1.add("RUSSIA")
print(s1)
```python


## Frozen Sets or Immutable Sets
* Frozen sets cannot be changed, once created, they can only be read.
* Below is a demonstration of a Mutable or changable set.
```python
FS1 = frozenset([1,2,3])
print(FS1)

# The below commented code will result in error, As elements cannot be 
# added to FROZEN sets
# FS1.add(5)
```python


### Set Operations UNION
* Combine SETS with the UNION function
* This can be done using **UNION function** or the **| operator**
```python
# Combine SETS with the UNION function
S1 = {1,2,3}
S2 = {"A", "B", "C"}

# Create S3 by Merging set S2 with S1 using UNION function
S3 = S1.union(S2)
print(S3)

# Create S3 by Merging set S2 with S1 using | operator
S1 = {1,2,3}
S2 = {"A", "B", "C"}
S3 = S1 | S2
print(S3)
```python


### Set Operations INTERSECT
* Get common elements between TWO sets using the **INTERSECT function** 
```python
S11 = {1,2,3}
S12 = {1,4,5}
print(S11.intersection(S12))
```python


### Set Operations DIFFERENCE
* The **DIFFERENCE FUNCTION** gets the elements not in one over the another
* The **- operator** also supports this action.
```python
S11 = {1,2,3}
S12 = {1,4,5}
print(S11.difference(S12))
```python


### Set Operations Symmetric DIFFERENCE
* The **Symmetric DIFFERENCE** will get all differences between both sets
* This is done using the **^** operator
```python
SET1 = {0,1,2}
SET2 = {0,"A","B"}
print(SET1 ^ SET2)

```python


### Remove elements from SET
* **DISCARD FUNCTION**
* DISCARD FUNCTION is used to remove element from a SET.
* If element to be removed is not found no error is raised
>
* **REMOVE FUNCTION**
* REMOVE FUNCTION is used to remove element from a SET.
* If element to be removed is not found the **error is raised**
```python
A1 = {"a","b","c","d"}
A1.discard("a")
print(A1)

A1 = {"a","b","c","d"}
A1.remove("a")
print(A1)

# KeyError will be raised when REMOVE is used on 
# non exsistant element in set
# A1.remove("X") --> Will Cause Error (KeyError)
```python


### Set Operations CLEAR
* Remove elements from the SET
```python
S11 = {1,2,3}
print('Before Clear',S11)
S11.clear()
print('After Clear',S11)
```python

### Set Operations issubset()
* The **issubset()** checks if the input is a SubSet of the give set
* Returns TRUE or FALSE
```python
D1 = {1,2,3,4,5}
S1 = {2,3,4}
print(S1.issubset(D1))
```python


### Set Operations issuperset()
* The **issuperset()** checks if the input is a SuperSet of the give set
* Returns TRUE or FALSE
```python
D1 = {1,2,3,4,5}
S1 = {2,3,4}
print(D1.issuperset(S1))
```python


### Loop through SET elements
* Using the **FOR LOOP** to loop through SET elements
```python
# Create SET S1
S1 = {"A","B","C","D","E"}
for c in S1:
    print(c)
```python


### Using IF..ELSE with SET
* Common Mathemeatical operators such as >,<,>=,<= can be used with sets
```python

# Create 2 Sets
R1 = {1,2,3,4}
R2 = {2,3,4}

if R1 > R2:
    print("R1 Has more elements")

if R1 = R2:
    print("R1 Has equal elements")
else:
    print("R1 and R2 are notequal in element count")
```python
