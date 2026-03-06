import datetime

d = int(input("Ngày: "))
m = int(input("Tháng: "))
y = int(input("Năm: "))

ngay = datetime.date(y, m, d)

print("Đây là ngày thứ", ngay.timetuple().tm_yday, "trong năm")