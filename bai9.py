so_dien = int(input("nhập số điện tiêu thụ (kwh)"))
sum = 0 
if so_dien <=50:
    sum += so_dien *1800
elif so_dien <= 100:
    sum += (so_dien-50)*2000 + 50*1800
else:
    sum += 50*1800 + 50*2000 +(so_dien-100)*2500

print(sum)