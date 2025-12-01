from datetime import datetime, timedelta

def run():
    student_id = "1121404"
    name = "陳宥丞"

    now = datetime.utcnow() + timedelta(hours=8)
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"學號：{student_id}, 姓名：{name}, 執行時間：{now}")

if __name__ == "__main__":
    run()
