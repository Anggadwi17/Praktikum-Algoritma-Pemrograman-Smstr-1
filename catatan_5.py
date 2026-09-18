#Program 5.1 For

# Perulangan (loop) 
 
from ast import Pass


angka = 1 
print(angka) 
angka = angka + 1 
print(angka) 
angka = angka + 1 
print(angka) 
 
# for kondisi: 
# aksi 
 
#dengan list 
angka2 = [0,1,2,3,4] # ini adalah list 
print(angka2) 
 
for i in angka2: 
 print(f"i sekarang → {i}") #print(f) -> kombinasi text dan variabel 
print("akhiri dari program\n") 
 
#dengan range 
angka3 = range(5) 
 
for i in angka3: 
  print(f"i sekarang → {i}") 
print("akhiri dari program\n")
# Perulangan (loop) 
 
angka = 1 
print(angka) 
angka = angka + 1 
print(angka) 
angka = angka + 1 
print(angka) 
 
# for kondisi: 
# aksi 
 
#dengan list 
angka2 = [0,1,2,3,4] # ini adalah list 
print(angka2) 
 
for i in angka2: 
 print(f"i sekarang → {i}") #print(f) -> kombinasi text dan variabel 
print("akhiri dari program\n") 
 
#dengan range 
angka3 = range(5) 
 
for i in angka3: 
  print(f"i sekarang → {i}") 
print("akhiri dari program\n")


#Program 5.2 While Loop

# while loop 
 
#while kondisi: 
# aksi ini 
# aksi itu 
 
 
print("===contoh 1===")
 
angka = 10 
while angka > 5: 
 print("ipin lari ipin!!!") 
 
print("===contoh 2===")
 
angka = 0 
print(f"angka sekarang → {angka}") 
 
while angka < 5: 
 angka += 1 
 #angka = angka + 1 
 print(f"angka sekarang → {angka}") 
 print("ipin lari ipin") 
 
print("program berakhir, ipin sudah jauh")


#Program 5.3  Continue and Pass

# continue, pass, break 
 
#pass → dia berfungsi sebagai dummy, tidak akan dieksekusi 
 
angka = 0 
 
while angka < 5: 
 angka = angka + 1 
  
 if(angka == 3): 
  pass # ini tidak akan dieksekusi 
 print(angka) 
 
#continue 
 
angka = 0 
print(f"angka sekarang → {angka}") 
 
while angka < 5: 
 angka = angka + 1 
 print(f"angka sekarang → {angka}") # aksi 1 
 
 if(angka == 3): 
  print("nice") 
  continue # akan membuat loop meloncat ke step selanjutnya 
 print("whasssup") # aksi 2 
 
print("Pinish")


#Program 5.4  break 

# break 
 
angka = 0 
print(f"angka sekarang → {angka}") 
 
while angka <5:
    angka = angka + 1 
    print(f"angka sekarang → {angka}") # aksi 1 
     
    if(angka == 3): 
     print("nice") 
     break # akan membuat loop berhenti 
    print("whasssup") # aksi 2


#Program 5.5  Latihan perulangan 


#latihan membuat segitiga 
# 1. Menggunakan for 
sisi = 4 
count = 1 
for i in range(sisi): 
  print("*" * count) 
count += 1  
# 2. Menggunakan while 
sisi = 4 
count = 1 
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break