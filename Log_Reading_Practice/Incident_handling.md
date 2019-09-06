# Incident Handling Exercise

### Scenerio
<p>
Your network consists of a DMZ hosting basic services such as DNS, HTTP, FTP, and SSH, along with a user subnet. Network traffic is being captured on your router's DMZ interface doing full packet capture on the traffic going into and out of your DMZ subnet.  There is a firewall on your network's inbound link and the firewall rules are included in your file set.
</p>
<p>
You recently joined your orginization's incident handling team.  One of the network system administrators has noted anomalous traffic on the internal web server and has identified it as a "network event."  You are on call and need to do an initial analysis of the data to determine whether the event should be classified as a "network incident." Assuming an incident has occurred, you will also be asked to make recommendations to your organization for mitigating this incident and for improving the security of your network.
</p>

### Network Topology Map

![Network_topology](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/Incident_Handling_Network_Topology.png?raw=true)


#### 1. What tools will you use to analyze the network trafﬁc and log ﬁles for this network event? List the tools (VMs and software) that you will use during your investigation and what each will be used for. (You will likely update this list as you go through the lab.)
<p>
For this exercise, I will use Kali Linux as the operating system.  I will use Wireshark to analyze the network traffic.
</p>

<br>

#### 2. What is the IP address of the host in the 172.16.2.0/24 subnet that accessed our DNS server?

<p>
The IP address of the host is 172.16.2.58
</p>

<br>

#### 3. What are the ﬁrst three requests made from that host to our DNS server?

![dns_&&_src](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/dns_&&_src_ip.png?raw=true)

<br>

#### 4. What information has the external host determined about our network that he/she might use during subsequent penetration attempts?

<p>
The external host has successfully received a DNS zone transfer.  This has enumerated the ip addresses and DNS records of all of the ip addresses located on our DMZ network.  This will enable the host to do more accurate network scanning.
</p>

![AXFR_evidence](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/AXFR_evidence.png?raw=true)

<br>

#### 5.  What is unusual about this interaction between an (external) Internet host and our DNS server?

<p>
What is unusual is that the zone transfer succeeded.  This should only be reserved for exchanges inbetween DNS servers. Users should not be able to receive a DNS zone transfer.
</p> 

<br>

#### 6. Which hosts were scanned?

<p>
4 hosts were scanned.  10.10.4.1, 10.10.4.12, 10.10.4.16, 10.10.4.251
</p>

![hosts_scanned](https://github.com/thaddeuspearson/Blue-Team/blob/master/photos_and_screenshots/Scanned_Hosts.png?raw=true)

#### 7. The attacker scanned the same group of ports on each server. Which ports did the attacker include in his/her scan of these hosts?

<p>
Ports scanned were 20, 21, 22, 25, 80, 443
</p>

![ports_scanned]()
<br>