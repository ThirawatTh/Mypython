#ฟังก์ชั้นหาพื้นที่สามเหลี่ยม = 1/2*ฐ*ส
def triangle(base, height):
    area = 1/2*base*height
   #print("พื้นที่สามเหลี่ยม %.3f" % area)
    return area

#triangle(2,3)
#triangle(5,10)
#triangle(7,3)
b = int(input("ค่าฐาน:"))
h = int(input("ค่าสูง:"))
print("พื้นที่สามเหลี่ยม %.3f" % triangle(b,h))