# Network and Host Logs Exercise
```python
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
<details><summary>Exercise Answers</summary>
<p>
1. The OS of this log is Linux (debial kernal).  UFW firewall generated this report.
</p>
<p>
2. The log is says that 2 outbound DHCP attempts occuring on ports 68/68 were blocked.
</p>
<p>
3.  This log is not indicative of anything malicious.
</p>

<br>

## Log 2
