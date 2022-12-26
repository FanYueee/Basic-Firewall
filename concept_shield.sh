#!/bin/bash

# 砞竚璶北狠
port=25596

# い耞硈絬丁()
block=30

# ﹚竡–筳 5 ъΩ total packets received 计
interval=5

# ﹚竡钵盽计秖
abnormal=100000

# 玡竚砞竚す砛瞷Τ硈絬ぃ耞絬
iptables -I INPUT -m state --state ESTABLISHED,RELATED -p tcp --dport $port -j ACCEPT

# 眔ヘ玡 total packets received 计
# 狦眤╰参⊿Τ netstat 眤эノㄤㄒ ss ┪ ip
total=$(netstat -s | grep "total packets received" | awk '{print $1}')

# –筳 $interval ъΩ total packets received 计
while true; do
    # 何痸 $interval 
    sleep $interval

    # 眔ヘ玡 total packets received 计
    # 狦眤╰参⊿Τ netstat 眤эノㄤㄒ ss ┪ ip
    current=$(netstat -s | grep "total packets received" | awk '{print $1}')

    # 璸衡綟ㄢΩъぇ丁畉钵
    diff=$(($current - $total))

    if [ $diff -gt $abnormal ]
    then
        total=$current
        sleep 5
        echo "fail $diff"
        iptables -A INPUT -p tcp --dport $port -j DROP
        sleep $block
        iptables -D INPUT -p tcp --dport $port -j DROP
    else 
        # 块綟ㄢΩъぇ丁畉钵
        echo "pass $diff"

        # 穝 total 
        total=$current
    fi
done