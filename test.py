from rembg import remove
from PIL import Image

input_path = "3fbe8fc2ae1413a698fcbaa93629f793.jpg"
output_path = "output.png"

เปิดภาพ
inp = Image.open(input_path)

ลบพื้นหลัง
out = remove(inp)

บันทึกไฟล์ใหม่
out.save(output_path)
print("✅ ลบพื้นหลังเสร็จแล้ว ->", output_path)
