import psutil
import time
import requests

url = "https://discord.com/api/webhooks/1056935826635894944/GtC84sSwQwofdjXg1C7KSrZUMxOzkekgf5ctnEwcFnfme59HX_uFUGAwkbeK9xwvaL8N"

cpu_usage_threshold = 90
ram_usage_threshold = 90
disk_usage_threshold = 90

cpu_usage_count = 0
ram_usage_count = 0
disk_usage_count = 0

def get_cpu_usage():
    return psutil.cpu_percent()

def get_ram_usage():
    ram_stats = psutil.virtual_memory()
    ram_total = ram_stats.total
    ram_used = ram_stats.used
    ram_usage_percent = (ram_used / ram_total) * 100
    return ram_usage_percent

def get_disk_usage():
    disk_stats = psutil.disk_usage('/')
    disk_total = disk_stats.total
    disk_used = disk_stats.used
    disk_usage_percent = (disk_used / disk_total) * 100
    return disk_usage_percent

while True:

    def webhook():
        data = {
            "content": warn,
            "username": "通知"
        }
        result = requests.post(url, json=data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()
    disk_usage = get_disk_usage()

    if cpu_usage > cpu_usage_threshold:
        cpu_usage_count += 1
        if cpu_usage_count >= 3:
            print("警告：CPU 使用率連續 3 次超過 90%！")
            cpu_usage_count = 0
            warn = f"警告：硬碟使用率連續 3 次超過 90%！，當前值 {cpu_usage}%"
            webhook()
    else:
        cpu_usage_count = 0

    if ram_usage > ram_usage_threshold:
        ram_usage_count += 1
        if ram_usage_count >= 3:
            print("警告：RAM 使用率連續 3 次超過 90%！")
            ram_usage_count = 0
            warn = f"警告：RAM 使用率連續 3 次超過 90%！，當前值 {ram_usage}%"
            webhook()

    else:
        ram_usage_count = 0

    if disk_usage > disk_usage_threshold:
        disk_usage_count += 1
        if disk_usage_count >= 3:
            print("警告：硬碟使用率連續 3 次超過 90%！")
            disk_usage_count = 0
            warn = f"警告：硬碟使用率連續 3 次超過 90%！，當前值 {disk_usage}%"
            webhook()
    else:
        disk_usage_count = 0

    print(f"CPU 使用率：{cpu_usage:.2f}%")
    print(f"RAM 使用率：{ram_usage:.2f}%")
    print(f"硬碟使用率：{disk_usage:.2f}%")

    time.sleep(3)
