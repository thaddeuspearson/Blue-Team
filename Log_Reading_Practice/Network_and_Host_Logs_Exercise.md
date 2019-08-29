# Network and Host Logs Exercise
```python
# psedocode directions (will not run)

def identify(exercise_list):

    questions_complete = False


    for exercise in exercise_list:

        if exercise == exercise_list[len(exercise_list - 1)]:

            questions_complete = True

            return "I'm Finished!!!"
        
exercises = [

    "1. Identify the OS && network device that generated the following logs",

    "2. What is each log saying?",

    "3. Which logs are normal vs malicious?"

]

identify(exercises)   
```
<br>

## Log 1
```
Aug  5 15:12:48 debian kernel: [ 2816.454036] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=63825 DF PROTO=TCP SPT=48824 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0
Aug  5 15:12:49 debian kernel: [ 2818.245909] [UFW AUDIT] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55611 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:12:49 debian kernel: [ 2818.245918] [UFW BLOCK] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55611 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:13:08 debian kernel: [ 2836.585918] [UFW AUDIT] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55976 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:13:08 debian kernel: [ 2836.585926] [UFW BLOCK] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55976 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:13:10 debian kernel: [ 2838.795866] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=26332 DF PROTO=TCP SPT=48852 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0
Aug  5 15:13:10 debian kernel: [ 2838.886422] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=60755 DF PROTO=TCP SPT=48854 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 15:13:10 debian kernel: [ 2838.887038] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=32790 DF PROTO=TCP SPT=48856 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0 
```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Linux (debial kernal).  UFW firewall generated this report.
</p>
<p>
2. The log is says that 2 outbound DHCP attempts occuring on ports 68/68 were blocked.
</p>
<p>
3.  This log is not indicative of anything malicious.
</p>
</details>
<br>

## Log 2

```
Aug  5 16:27:23 debian kernel: [ 3535.868836] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=36914 DF PROTO=TCP SPT=45734 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:23 debian kernel: [ 3535.868842] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=36914 DF PROTO=TCP SPT=45734 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:31 debian kernel: [ 3544.237326] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=55203 DF PROTO=TCP SPT=45736 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:31 debian kernel: [ 3544.237332] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=55203 DF PROTO=TCP SPT=45736 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:57 debian kernel: [ 3570.390818] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=45455 DF PROTO=TCP SPT=45742 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:57 debian kernel: [ 3570.390826] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=45455 DF PROTO=TCP SPT=45742 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:28:12 debian kernel: [ 3584.699296] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=742 DF PROTO=TCP SPT=45744 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:28:12 debian kernel: [ 3584.699304] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=742 DF PROTO=TCP SPT=45744 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
```

<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Linux (debial kernal).  UFW firewall generated this report.
</p>
<p>
2. The log is says that outbound TCP traffic on port 1337 was blocked 4 times.
</p>
<p>
3.  This log is slightly indicative of malicious behavior, as the port 1337 is being used.
</p>
</details>
<br>

## Log 3

```
2019-08-05 16:42:33 ALLOW UDP 192.168.56.7 224.0.0.251 5353 5353 0 - - - - - - - SEND
2019-08-05 16:42:33 ALLOW UDP 192.168.56.7 192.168.56.255 137 137 0 - - - - - - - SEND
2019-08-05 16:42:39 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:40 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:41 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:42 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:47 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:48 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:49 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:50 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:51 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:52 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:43:01 ALLOW ICMP ::1 ff02::16 - - 0 - - - - 143 0 - SEND
2019-08-05 16:43:01 ALLOW 2 127.0.0.1 224.0.0.22 - - 0 - - - - - - - SEND
2019-08-05 16:43:01 ALLOW UDP 127.0.0.1 239.255.255.250 63778 1900 0 - - - - - - - SEND
2019-08-05 16:43:01 ALLOW UDP 127.0.0.1 239.255.255.250 63778 1900 0 - - - - - - - RECEIVE
2019-08-05 16:43:16 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:17 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:18 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:19 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Windows.  The Windows Defender Firewall generated this report.
</p>
<p>
2. The log is says 4 outbound pings to destination ip 192.168.56.2 were allowed, 6 ping attempts from 192.168.56.3 to the local machine were blocked, and 4 pings to destination ip 192.168.56.103 were allowed. 
</p>
<p>
3.  This log does not indicate any malicious behavior.
</p>
</details>

# Detection Alerts

![pi-hole](https://raw.githubusercontent.com/thaddeuspearson/Blue-Team/master/photos_and_screenshots/pi_hole.png)pi_hole


