import time
import psutil
import requests
from datetime import datetime


# 設定流量限制(Mbps為單位)
limit = 100

# discord webhook link
webhook_url = ""

while True:
    # 取得目前的流入流量與封包量
    traffic_bytes = psutil.net_io_counters().bytes_recv
    packets1 = psutil.net_io_counters().packets_recv
    time.sleep(1)
    traffic_bytes2 = psutil.net_io_counters().bytes_recv
    packets2 = psutil.net_io_counters().packets_recv
    packets = (packets2 - packets1)
    traffic = (traffic_bytes2 - traffic_bytes) * 8 / 1000 / 1000
    if traffic > limit:
        if traffic > 1000:
            traffic = traffic / 1000
            data = {
                "content": f":warning: [{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] 流量: {traffic} Gbps, 封包: {packets} 個",
                "username": "Network Alert"
            }
            requests.post(webhook_url, json=data)
        elif traffic > 100:
             data = {
                 "content": f":warning: [{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] 流量: {traffic} Mbps, 封包: {packets} 個",
                 "username": "Network Alert"
             }
             requests.post(webhook_url, json=data)

    # 冷卻時間(60秒)
    time.sleep(60)