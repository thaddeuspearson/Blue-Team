# AWS Flow Log Example

![AWS Log File](https://media.amazonwebservices.com/blog/2015/flow_see_a_stream_2.png)

### AWS Flow Log Syntax

```
<version> <account-id> <interface-id> <srcaddr> <dstaddr> <srcport> <dstport> <protocol> <packets> <bytes> <start> <end> <action> <log-status>
```

### Examples
```
2 123456789010 eni-abc123de 172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK
```
SSH (destination port 22, TCP protocol 6) traffic from 172.31.16.139 to network interface eni-abc123de in account number 123456789010 was accepted  
<br>
<br>
```
2 123456789010 eni-abc123de 172.31.9.69 172.31.9.12 49761 3389 6 20 4249 1418530010 1418530070 REJECT OK
```
RDP (destination port 3389, TCP protocol 6) traffic from 172.31.9.69 to network interface eni-abc123de  in account number 123456789010 was rejected



```
2 123456789010 eni-1a2b3c4d - - - - - - - 1431280876 1431280934 - NODATA

2 123456789010 eni-4b118871 - - - - - - - 1431280876 1431280934 - SKIPDATA
```
Two examples are when no data or skipped data is recorded from the capture session:

2 123456789010 eni-1235b8ca 203.0.113.12 172.31.16.139 0 0 1 4 336 1432917027 1432917142 ACCEPT OK
2 123456789010 eni-1235b8ca 172.31.16.139 203.0.113.12 0 0 1 4 336 1432917094 1432917142 REJECT OK
2 123456789010 eni-f41c42bf 2001:db8:1234:a100:8d6e:3477:df66:f105 2001:db8:1234:a102:3304:8879:34cf:4071 34892 22 6 54 8855 1477913708 1477913820 ACCEPT OK

```

