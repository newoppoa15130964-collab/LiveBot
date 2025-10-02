!pip install rembg pillow

from rembg import remove
from PIL import Image
from google.colab import files

#อัปโหลดภาพ
uploaded = files.upload()

#ใช้ไฟล์แรกที่อัปโหลด
input_path = list(uploaded.keys())[0]
output_path = "output.png"

#เปิดภาพ
inp = Image.open(input_path)

#ลบพื้นหลัง
out = remove(inp)

#บันทึกภาพใหม่
out.save(output_path)
print("✅ ลบพื้นหลังเสร็จแล้ว ->", output_path)
