
# 1. Family Fight Simulation with Inheritance & Polymorphism

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


# 3. 


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



## 5.3:

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
        print("Son: Tried to be Artsit..but Failed ")
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
