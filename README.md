
# Family Fight Simulation & Life Journey in Python

This project creatively simulates family dynamics and life experiences using Python's core object-oriented programming concepts such as 
**inheritance**, **polymorphism**, and **callback functions**.

---

## Features

1. **Family Fight Simulation** – Demonstrates polymorphism as each family member exhibits a unique "fighting style".
2. **Ordered Family List & Love Pairs** – Sorts and processes family relationships using list operations.
3. **Life Journey Simulation** – Emulates a mother's constant support through various career struggles using callback functions.

---

## Code Structure

### 1. Family Fight Simulation

class FamilyMembers:
    def fight():
        print("Fighting Style")

class Father():
    def fight(self):
        print("Shout")

class Mother():
    def fight(self):
        print("Logical Reasoning")

class Son():
    def fight(self):
        print("Ignore")

class Daughter():
    def fight(self):
        print("Silent Treatment")

FamilyMembers = [Father(), Mother(), Son(), Daughter()]

for member in FamilyMembers:
    member.fight()

````
**Polymorphism** is used here — all classes implement the `fight()` method differently.
---

### 2. List Ordering & Love Pairing

list_order = ["Son", "Father", "Mother", "Daughter", "GrandSon", "GrandFather", "Sister", "Brother", "GrandMother", "GrandDaughter"]

sorted_desc = sorted(list_order, reverse=True)
print(list_order[::-1])

love_pairs = [("Mother", "Son"), ("Father", "Daughter"), ("Brother", "Sister"), ("GrandFather", "GrandSon"), ("grandMother", "GrandDaughter")]

ordered_family = []

for first, second in love_pairs:
    if first in list_order and second in list_order:
        ordered_family.append(first)
        ordered_family.append(second)

print(ordered_family)

**Explanation**:

* The family list is reversed and sorted.
* Love/affection pairs are filtered and printed if both members are in the list.

### 3. Life Journey with Mother's Support

class Mother:
    def continues_love_and_support(self):
        print("Mother: Try next time")
    
    def happytears(self):
        print("Mother: I am so proud")

class Engineer:
    def struggle(self, callback):
        print("Son: trying lot..but Failed")
        callback()
        return False

class Artist:
    def struggle(self, callback):
        print("Son: Tried to be Artist..but Failed")
        callback()
        return False

class Entrepreneur:
    def struggle(self, callback):
        print("Son: Tried my best...But Succeeded!")
        return True

mother = Mother()
careers = [Engineer(), Artist(), Entrepreneur()]

for career in careers:
    if career.struggle(mother.continues_love_and_support):
        mother.happytears()
        break

**Explanation**:

* **Callback functions** are used to simulate emotional reactions.
* The mother supports the son no matter what — until he finally succeeds, and she expresses pride.


## Output Example

Shout
Logical Reasoning
Ignore
Silent Treatment
['GrandDaughter', 'GrandMother', 'Brother', ...]
['Mother', 'Son', 'Father', 'Daughter', ...]
Son: trying lot..but Failed
Mother: Try next time
Son: Tried to be Artist..but Failed
Mother: Try next time
Son: Tried my best...But Succeeded!
Mother: I am so proud


## Concepts Demonstrated

* Inheritance and Polymorphism
* List operations and filtering
* Callback functions
* Conditional logic and control flow
