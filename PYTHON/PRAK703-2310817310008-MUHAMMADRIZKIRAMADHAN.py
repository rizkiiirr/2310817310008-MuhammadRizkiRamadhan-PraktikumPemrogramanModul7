pertama, kedua = map(int, input().split())
baris1 = []
baris2 = []
if (pertama != kedua):
    print("Jumlah tidak sama")
else:
    input_baris1 = input().split()
    input_baris2 = input().split()
    for i in range(0,pertama):
        baris1.append(int(input_baris1[i]))
        baris2.append(int(input_baris2[i]))
    for i in range(pertama):
        print(baris1[i] * baris2[i], end=" ")
