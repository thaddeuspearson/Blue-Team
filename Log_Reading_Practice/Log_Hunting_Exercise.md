# Log Hunting Exercises
```python
# psedocode directions (will not run)

def identify(exercise_dct):

    exercises_complete = False


    for exercise in exercise_dct:

        do(exercise)

        if exercise == exercise_dct[len(exercise_dct)]:

            exercises_complete = True

            return "I'm Finished!!!"

```

<br>

## Network Logs

```python        
exercises = {

    1: "Identify the OS && network device that generated the following logs",

    2: "What is each log saying?",

    3: "Which logs are normal vs malicious?"

}

identify(exercises)   
```

<br>

### Log 1
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
3. This log is not indicative of anything malicious.
</p>
</details>
<br>

### Log 2

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
3. This log is slightly indicative of malicious behavior, as the port 1337 is being used.
</p>
</details>
<br>

### Log 3

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
3. This log does not indicate any malicious behavior.
</p>
</details>

<br>

## Host Logs

```python
exercises = {

    1: "Identify the OS && application(s) that generated the following logs",

    2: "What is each log saying?",

    3: "Which logs are normal vs malicious?",

    4: "Who are the actors (hostnames, usernames, IPs)?" 

}

identify(exercises)   

```
<br>

### Log 1

```
Aug  5 14:09:20 debian sudo:   debian : TTY=pts/0 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  5 14:09:20 debian sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Aug  5 14:09:20 debian su: (to root) debian on pts/0
Aug  5 14:09:20 debian su: pam_unix(su:session): session opened for user root by (uid=0)
Aug  5 14:09:22 debian su: pam_unix(su:session): session closed for user root
Aug  5 14:09:22 debian sudo: pam_unix(sudo:session): session closed for user root
Aug  5 14:09:23 debian sudo:   debian : TTY=pts/0 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  5 14:09:23 debian sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Aug  5 14:09:23 debian su: (to root) debian on pts/0
Aug  5 14:09:23 debian su: pam_unix(su:session): session opened for user root by (uid=0)
Aug  5 14:09:41 debian su: pam_unix(su:session): session closed for user root
Aug  5 14:09:41 debian sudo: pam_unix(sudo:session): session closed for user root
Aug  5 14:09:43 debian sudo:   debian : TTY=pts/0 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  5 14:09:43 debian sudo: pam_unix(sudo:session): session opened for user root by (uid=0)

```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Debian Linux.  The auth.log in /var/log/auth.log generated this report.
</p>
<p>
2. The log is says the user root successfully ran a sudo command in the /home/debian directory, and successfully became su, 4 times 
</p>
<p>
3. While certainly strange, considering the user already had root access, this log does not inherently indicate any malicious behavior.
</p>
<p>
4. The actor in this log is the user root.
</details>

<br>

### Log 2

```
Aug  6 02:52:28 debian sudo:   debian : 3 incorrect password attempts ; TTY=pts/2 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  6 02:52:31 debian sudo: pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/2 ruser=debian rhost=  user=debian
Aug  6 02:52:42 debian sudo:   debian : 3 incorrect password attempts ; TTY=pts/2 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/su
Aug  6 03:14:30 debian sudo: pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/6 ruser=debian rhost=  user=debian
Aug  6 03:14:50 debian sudo:   debian : 3 incorrect password attempts ; TTY=pts/6 ; PWD=/home/debian ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow

```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Debian Linux.  The auth.log in /var/log/auth.log generated this report.
</p>
<p>
2. The log is says the user root unsuccessfully ran a sudo command in the /home/debian directory 3 times. Twice to become su, and once to attempt to read the /etc/shadow file. 
</p>
<p>
3. This log contains some suspicious behavior. Multiple incorrect password attempts by themselves do not necessarily indicate malicious behavior, but trying to read the etc/shadow file, where user password hashes are stored is highly suspect.  What is slightly strange is that this user is already root. This would indicate that this particular log was most likely non-malicious activity generated for exercise purposes.
</p>
<p>
4. The actor in this log attempted to login as the remote user debian, which is a root user account.
</details>

<br>

### Log 3

```
Aug  6 03:11:13 debian sshd[1421]: Accepted password for debian from 192.168.56.3 port 53358 ssh2
Aug  6 03:11:13 debian sshd[1421]: pam_unix(sshd:session): session opened for user debian by (uid=0)
Aug  6 03:11:13 debian systemd-logind[412]: New session 4 of user debian.
Aug  6 03:11:16 debian sshd[1427]: Received disconnect from 192.168.56.3 port 53358:11: disconnected by user
Aug  6 03:11:16 debian sshd[1427]: Disconnected from user debian 192.168.56.3 port 53358
Aug  6 03:11:16 debian sshd[1421]: pam_unix(sshd:session): session closed for user debian
Aug  6 03:11:16 debian systemd-logind[412]: Session 4 logged out. Waiting for processes to exit.
Aug  6 03:11:16 debian systemd-logind[412]: Removed session 4.
Aug  6 03:11:22 debian sshd[1432]: Accepted password for debian from 192.168.56.3 port 53360 ssh2
Aug  6 03:11:22 debian sshd[1432]: pam_unix(sshd:session): session opened for user debian by (uid=0)
Aug  6 03:11:22 debian systemd-logind[412]: New session 5 of user debian.

```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Debian Linux.  The auth.log in /var/log/auth.log generated this report.
</p>
<p>
2. The log is says two successfully executed ssh commands from 192.168.56.3 occured on two different ports, port 53358 and port 53360, approximately 10 seconds between each other, as user debian. 
</p>
<p>
3. There is nothing inherently suspicious about this behavior, however it is important to note that ssh must be properly hardened to guard against unauthorized remote logins. One of the best ways to do this is with authentication keys and to disable remote root login.
</p>
<p>
4. The actor in this log is the ip addess 192.168.56.3. The remote user was loged in as debian, which is a root user account.  Since this ip is a private address, this SSH session was executed from the local network.
</details>

<br>

### Log 4

```
Aug  6 02:54:16 debian sshd[1278]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  6 02:54:18 debian sshd[1278]: Failed password for root from 192.168.56.3 port 53312 ssh2
Aug  6 02:54:23 debian sshd[1278]: Failed password for root from 192.168.56.3 port 53312 ssh2
Aug  6 02:54:29 debian sshd[1278]: Failed password for root from 192.168.56.3 port 53312 ssh2
Aug  6 02:54:31 debian sshd[1278]: Connection closed by authenticating user root 192.168.56.3 port 53312 [preauth]
Aug  6 02:54:31 debian sshd[1278]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  6 02:54:37 debian sshd[1280]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  6 02:54:39 debian sshd[1280]: Failed password for root from 192.168.56.3 port 53314 ssh2
Aug  6 02:54:42 debian sshd[1280]: Failed password for root from 192.168.56.3 port 53314 ssh2
Aug  6 02:54:47 debian sshd[1280]: Failed password for root from 192.168.56.3 port 53314 ssh2
Aug  6 02:54:47 debian sshd[1280]: Connection closed by authenticating user root 192.168.56.3 port 53314 [preauth]
Aug  6 02:54:47 debian sshd[1280]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root

```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Debian Linux.  The auth.log in /var/log/auth.log generated this report.
</p>
<p>
2. The log says two instances of unsuccessfully executed ssh commands trying to login as the remote user debian occurred from 192.168.56.3, on ports 53312 and 53314.  The password was entered incorrectly three times in each instance. 
</p>
<p>
3. There is nothing inherently suspicious about this behavior, as it is possible that the user has forgotten their password.  However, this isworth keeping an eye on, if more instances like this are occuring, as it might indicate that a relatively unskilled unauthorized individual on the local network is trying to access an account they should not be trying to access.
</p>
<p>
4. The actor in this log is the ip addess 192.168.56.3.  Since this ip is a private address, this SSH session was executed from the local network.
</details>

<br>

### Log 5

```
Aug  5 14:30:19 debian sshd[2251]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2252]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2259]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2257]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2255]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2254]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2258]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2261]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2256]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:19 debian sshd[2260]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.56.3  user=root
Aug  5 14:30:20 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:20 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:20 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:20 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:20 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:20 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:20 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:20 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:20 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:20 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:22 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:23 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:23 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:23 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:23 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:23 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:23 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:23 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:23 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:23 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:25 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:25 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:25 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:26 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:26 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:26 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:26 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:26 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:26 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:26 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:28 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:28 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:28 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:28 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:28 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:28 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:28 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:28 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:28 debian sshd[2258]: Failed password for root from 192.168.56.3 port 48810 ssh2
Aug  5 14:30:28 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2
Aug  5 14:30:31 debian sshd[2251]: Failed password for root from 192.168.56.3 port 48798 ssh2
Aug  5 14:30:31 debian sshd[2252]: Failed password for root from 192.168.56.3 port 48800 ssh2
Aug  5 14:30:31 debian sshd[2259]: Failed password for root from 192.168.56.3 port 48812 ssh2
Aug  5 14:30:31 debian sshd[2257]: Failed password for root from 192.168.56.3 port 48808 ssh2
Aug  5 14:30:31 debian sshd[2255]: Failed password for root from 192.168.56.3 port 48804 ssh2
Aug  5 14:30:31 debian sshd[2256]: Failed password for root from 192.168.56.3 port 48806 ssh2
Aug  5 14:30:31 debian sshd[2254]: Failed password for root from 192.168.56.3 port 48802 ssh2
Aug  5 14:30:32 debian sshd[2261]: Failed password for root from 192.168.56.3 port 48816 ssh2
Aug  5 14:30:32 debian sshd[2260]: Failed password for root from 192.168.56.3 port 48814 ssh2

```
<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. The OS of this log is Debian Linux.  The auth.log in /var/log/auth.log generated this report.
</p>
<p>
2. The log says several instances of unsuccessfully executed ssh commands, trying to login as the remote user debian, occurred from 192.168.56.3, on ports 48798, 48800, 48802, 48804, 48806 48808, 48810, 48812, 48814, and 48816. The password was entered incorrectly in each instance. 
</p>
<p>
3. There is a high probability that this log indicates malicious activity. The time stamps of each attempt are occuring in intervals less than a second. The ports that are attempting to connect are evenly spaced apart and occur in periods of 10. This ismost likely indicative of a brute force attempt, with 10 threads attempting to guess the password for the ssh service.
</p>
<p>
4. The actor in this log is the ip addess 192.168.56.3.  Since this ip is a private address, these SSH login attempts were executed from the local network.
</details>

<br>






# Detection Alerts

<br>


## DNS

```python

exercises = {

    1: "Evaluate the screenshot",

    2: "What domains were blocked by the firewall?",

    3: "Are the domains potentially malicious?",

    4: "What is the likely reason the domains were blocked?"

}

identify(exercises)
```
<br>

![pi-hole](https://raw.githubusercontent.com/thaddeuspearson/Blue-Team/master/photos_and_screenshots/pi_hole.png)

<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. This log file came from the application Pi-hole (https://pi-hole.net).  It is an ad-blocking DNS server typically run on a rasberry pi.
</p>
<p>
2. Pi-hole has been set to blacklist v10.events.data.microsoft.com and settings-win.data.microsoft.com. 
</p>
<p>
3. The domains that have been blacklisted are not inherently malicious. v10.events.data.microsoft.com is a windows 10 service associated with Diagnostic Data, and settings-win.data.microsoft.com is used for Windows apps to dynamically update their configuration.
</p>
<p>
4. The likely reason that these domains were blocked is that these services are on the gravity script in Pi-hole.  The gravity script retrives blocklists, and consolidates them into one unique list for the DNS to use.
</p>
</details>

<br>

## AntiVirus

```python

exercises = {

    1: "Which application generated the below detection alerts?",

    2: "Are the detected actions benign or malicious?",

    3: "Are all the quarantined items in image 2 malicious?"

}

identify(exercises)
```
<br>

### Image 1

![anti_virus_1](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/antivirus_1.png?raw=true)

<br>

### Image 2

![anti_virus_2](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/antivirus_2.png?raw=true)

<br>


#### SHA256 hash for `payload4.exe` and `payload5.exe`:
```
886943cb62c287b4bcf77372227875e10cf87b6e76eaa046b5a54547db13d5f9
```
<br>

<details><summary><b>Exercise Answers</b></summary>
<br>
<p>
1. This log file came from the application AVG (https://avg.com).  This is an anti-virus application.
</p>
<p>
2. The detected actions are malicious in nature.  The application notepad.exe has been quarantined because it was infected with malware.  The threat name of the malware is Win32:TrojanX-gen [Trj].  It is considered a low level threat.
</p>
<p>
3. It is highly likely that all of the quarentined items in image 2 are malicious.  Upon checking virus total, 21 engines have detected this files SHA256 hash to be associated with malware.

![virus_total](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/virus_total_payload4.png?raw=true)

Furthermore, the file locations the other quarantined file was found at a suspicious location, `C:\Users\root\AppData\Local\Temp\p.ps1`.  It would be highly unusual for a power shell to be running from a temporary file location.
</p>
</details>