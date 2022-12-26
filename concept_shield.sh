#!/bin/bash

# �]�m�n����ݤf
port=25596

# ���_�s�u���ɶ�(��)
block=30

# �w�q�C�j 5 �����@�� total packets received ���ƭ�
interval=5

# �w�q���`�ʥ]�ƶq
abnormal=100000

# �e�m�]�m�A���\�{���s�u���_�u
iptables -I INPUT -m state --state ESTABLISHED,RELATED -p tcp --dport $port -j ACCEPT

# ���o�ثe�� total packets received �ƭ�
# �p�G�z���t�ΤW�S�� netstat ���O�A�z�i�H��Ψ�L�����O�A�Ҧp ss �� ip
total=$(netstat -s | grep "total packets received" | awk '{print $1}')

# �C�j $interval ��A����@�� total packets received �ƭ�
while true; do
    # �ίv $interval ��
    sleep $interval

    # ���o�ثe�� total packets received �ƭ�
    # �p�G�z���t�ΤW�S�� netstat ���O�A�z�i�H��Ψ�L�����O�A�Ҧp ss �� ip
    current=$(netstat -s | grep "total packets received" | awk '{print $1}')

    # �p��۾F�⦸����������t��
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
        # ��X�۾F�⦸����������t��
        echo "pass $diff"

        # ��s total ����
        total=$current
    fi
done