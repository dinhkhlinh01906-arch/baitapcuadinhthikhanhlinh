import datetime

d = int(input("Ngày: "))
m = int(input("Tháng: "))
y = int(input("Năm: "))

ngay = datetime.date(y, m, d)

ngay_sau = ngay + datetime.timedelta(days=1)
ngay_truoc = ngay - datetime.timedelta(days=1)

print("Ngày kế tiếp:", ngay_sau)
print("Ngày trước đó:", ngay_truoc)