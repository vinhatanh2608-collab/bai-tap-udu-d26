diem_trung_binh = float(input())

if diem_trung_binh < 0 or diem_trung_binh > 10:
    print("lỗi")
elif diem_trung_binh < 5:
    print("Yếu")
elif diem_trung_binh <= 6.4:
    print("Trung bình")
elif diem_trung_binh <= 7.9:
    print("Khá")
else:
    print("giỏi")