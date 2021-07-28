#Program dibuat setelah UAS
#Membuat stack dengan operasi list
#Menambahkan fungsi untuk mencari sebuah nilai, mengurutkan nilai, dan melakukan traverse nilai

import pickle

#pembuatan stack dengan list
stack=[]

#menulis data stack ke dalam file pickle
with open('Data.pkl', 'wb') as y:
    for x in range (1, 6):
        stack.append(x)
    pickle.dump(stack, y)

print("Data stack1\t: ", stack)

def bacadata():
    #membaca data stack pada file pickle
    with open('Data.pkl', 'rb') as y:
        stack=pickle.load(y)
        print("Data stack2\t: ", stack)


#Mengurutkan nilai dalam stack
def sorting():
    stack.sort()
    print("Sorting\t\t: ", stack)


#Traversal nilai dalam stack
def traversal():
    print("Traversal\t: ")
    for x in stack:
        print(x)


#mencari nilai input pada stack
def searching(stack, s):
    found=False
    for i in range(len(stack)):
        if stack[i]==s:
            found=True
    return found


bacadata()
sorting()
traversal()

s=int(input("Masukkan nilai yang ingin dicari: "))
found=searching(stack, s)
if found:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")