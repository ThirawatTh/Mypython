print ("แจ้งผ่านคะแนน")
x = float(input("รับค่าคะแนน:"))
if x>= 80 and x<=100:
    print("เกรด___A___")
elif x>= 70 and x<=79:
    print("เกรด___B___")
elif x>= 60 and x<=69:
    print("เกรด___C___")
elif x>=  50 and x<=59:
    print("เกรด___D___")
elif x>= 0 and x<=49:
    print("เกรด___F___")
else:
    print("กรุณาป้อนข้อมูลใหม่ให้ถูกต้อง")
    