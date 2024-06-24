def bmi_(h,w):
    c = (h/100)**2
    b = w/c
    return b

def bmi (n):

    if n< 18.50:
        print("น้ำหนักน้อย/ผอม")
    elif n >=18.50 and n <=22.90 :
        e = ("---ปกติสุขภาพดี---")
    elif n >=23 and n <=24.90 :
        e = ("---ท้วม/โรคอ้วนระดับ 1 ---")
    elif n >=25 and n <=29.90 :
        e = ("---อ้วน/โรคอ้วนระดับ 2---")
    elif n >=30 :
        e = ("---อ้วนมาก/โรคอ้วนระดับ 3---")
    
    return e

z = float(input("น้ำหนักตัว(kg): "))
x = float(input("ส่วนสูง(m): "))
n = bmi_(x,z)
bmi1 = bmi(n)

print("ค่าดัชนีมวลกายอยู่ในกณฑ์ , bmi1")
print("ค่าดัชนีมวลกายคือ %.3f" %n)
