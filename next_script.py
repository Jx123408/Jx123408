import time
import sys

message = "こんにちは"

for char in message:
    print(char, end='', flush=True)
    time.sleep(0.3)  # 0.3秒ごとに1文字表示

print()  # 改行
