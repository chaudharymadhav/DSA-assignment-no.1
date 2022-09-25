class Node:
    def __init__(self, name=None, age=None):
        self.prev = None
        self.next = None
        self.name = name
        self.age = age


class FamilyDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, name, age):
        node = Node(name, age)
        if self.head is None:  # no element present
            self.head = node
            self.tail = node
        else:  # we will be adding the element at the end if its not the first
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            node.prev = temp
            temp.next = node
            self.tail = node

n = int(input('Enter the number of family members you want to add in FAMILY_DLL-:'))
names = n * [None]
ages = n * [None]
for i in range(0, n):
    print('ENTER the name of family member number',i+1,'\b :-')
    names[i] = input()
    print('ENTER the age of family member',i+1,"-:")
    ages[i] = int(input())
for i in range(0, n):
    for j in range(0, n - i - 1):
        if ages[j] < ages[j + 1]:
            ages[j], ages[j + 1] = ages[j + 1], ages[j]
            names[j], names[j + 1] = names[j + 1], names[j]
Family_sequence = FamilyDLL()
for i in range(0, n):
    Family_sequence.insert(names[i], ages[i])
temp = Family_sequence.head
print("This is family sequence which represents first 2 names of parents(Father and Mother respectively )"
      "and last 2 names of children (elder and younger respectively) :-")
for i in range(0, n):  # printing the familytree
    print('|Name: ', temp.name, ' age: ', temp.age, '|  >>>  ', end='')
    temp = temp.next
# print('None')




