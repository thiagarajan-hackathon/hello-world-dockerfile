import time

print("Dockerfile: Hello world !!")
end_time = time.time() + 5 * 60 * 60  # 5 hours

while time.time() < end_time:
    time.sleep(60)
