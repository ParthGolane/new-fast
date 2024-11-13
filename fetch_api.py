import requests


BASE_URL = "http://127.0.0.1:8000"
student_id = 2


response = requests.get(f"{BASE_URL}/students/{student_id}")


if response.status_code == 200:
    student_data = response.json()
    print("Student Data:", student_data)
else:
    print("Error:", response.status_code, response.json().get("detail"))
