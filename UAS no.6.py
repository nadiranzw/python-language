#Melanjutkan program UAS yang baru sedikit dikerjakan
#Menyunting fitur-fitur pada program sebelumnya
#menampung identitas mahasiswa ke dalam stack dan disimpan ke dalam pickle

import pickle

nama=[]
NIM=[]

nama.append('Budi')
nama.append('Andi')
nama.append('Eny')
NIM.append('H1A015001')
NIM.append('H1A015002')
NIM.append('H1A015003')


#menyalin data stack ke dalam file pickle
with open('Data.pkl', 'wb') as x:
    a=nama
    pickle.dump(a, x)
    b=NIM
    pickle.dump(b, x)

print("Daftar nama: \n", a)
print("\nDaftar NIM: \n", b)

def bacadata():
    #membaca data stack pada pickle
    with open('Data.pkl', 'rb') as x:
        a=pickle.load(x)
        print("\nDaftar nama: \n", a)
        b=pickle.load(x)
        print("\nDaftar NIM: \n", b)


#melakukan pengurutan data
def sorting():
    nama.sort()
    NIM.sort()
    print("\nSorting name: \n", nama)
    print("\nSorting NIM: \n", NIM)


#melakukan looping vertikal
def traversal():
    print("\nTraversal: ")
    for p in nama:
        print(p)
    for q in NIM:
        print(q)


#melakukan pencarian suatu nama pada stack nama
def searching1(nama, input1):
    found1=False
    for i in range(len(nama)):
        if nama[i]==input1:
            found1=True
    return found1
       

#melakukan pencarian suatu NIM pada stack NIM
def searching2(NIM, input2):
    found2=False
    for j in range(len(NIM)):
        if NIM[j]==input2:
            found2=True
    return found2


bacadata()
sorting()
traversal()

input1=input("\nMasukkan nama yang ingin dicari: ")
found1=searching1(nama, input1)
if found1:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")


input2=input("\nMasukkan NIM yang ingin dicari: ")
found2=searching2(NIM, input2)
if found2:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")