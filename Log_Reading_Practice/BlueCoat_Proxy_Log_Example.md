# BlueCoat Proxy Log Example

The following logs were pulled from:
http://log-sharing.dreamhosters.com/bluecoat_proxy_big.zip
**This file is huge, do not 'cat' in the terminal.  Use tail -n300**

<br>

```
2005-05-04 17:16:08 1 45.14.4.61 304 TCP_HIT 207 431 GET http hg.travelocity.com.edgesuite.net /graphics/tvly_mc_125x25.gif - - DIRECT 80.67.66.62 image/gif "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)" PROXIED Travel - 192.16.170.42 SG-HTTP-Service - none -

2005-05-04 17:16:08 154 45.14.4.127 200 TCP_NC_MISS 2973 720 GET http images.google.com /images ?q=tbn:-dEjG3JAHxgJ:www.kevcom.com/images/linux/linux.logo.2yp.jpg - DIRECT images.google.com image/jpeg "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312" PROXIED Hacking/Proxy%20Avoidance - 192.16.170.42 SG-HTTP-Service - none -

2005-05-04 17:16:08 18 45.23.4.216 304 TCP_RESCAN_HIT 422 405 GET http twinpeaksweather.com /java-sys/Dgclock.class - - DIRECT 66.235.216.135 application/octet-stream "Mozilla/4.0 (Windows 2000 5.0) Java/1.5.0_02" PROXIED News/Media - 192.16.170.42 SG-HTTP-Service - none -
```

## BlueCoat Proxy Log Syntax

```
<date> <time> <time-taken> <c-ip> <sc-status> <s-action> <sc-bytes> <cs-bytes> <cs-method> <cs-uri-scheme> <cs-host> <cs-uri-path> <cs-uri-query> <cs-username> <s-hierarchy> <s-supplier-name> <content-type> <cs-useragent> <sc-filter-result> <sc-filter-category> <x-virus-id> <s-ip> <s-sitename> <x-virus-details> <x-icap-error-code> <x-icap-error-details>
```

<br>
The first log indicates that at 17:16:08 on 2005-05-04(YYYY-MM-DD), a client at ip 45.14.4.61, with a Windows NT 5.1 MSIE 6.0 user-agent was redirected (status code 304) to a cached resource from hg.travelocity.com.edgesuite.net/graphics/tvly_mc_123x25.gif, which is a image/gif file. This request was proxied by 192.16.170.42 and filtered as Travel. The TCP_HIT indicated that a valid copy of the requested object was in the cache.

<br>

```
2005-05-04 17:16:08 1 45.14.4.61 304 TCP_HIT 207 431 GET http hg.travelocity.com.edgesuite.net /graphics/tvly_mc_125x25.gif - - DIRECT 80.67.66.62 image/gif "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)" PROXIED Travel - 192.16.170.42 SG-HTTP-Service - none -
```

<br>

The second log indicated that at 17:16:08 on 2005-05-04(YYYY-MM-DD), a client at ip 45.14.4.127, with a Macintosh OS X Safari user-agent made a GET request for an image at http://images.google.com/images?q=tbn:-dEjG3JAHxgJ:www.kevcom.com/images/linux/linux.logo.2yp.jpg. This request was proxied by 192.16.170.42 and filtered as Hacking/Proxy%20Avoidance.  The TCP_NC_MISS indicated that the object returned from the origin server was nonchacheable.
<br>

```
2005-05-04 17:16:08 154 45.14.4.127 200 TCP_NC_MISS 2973 720 GET http images.google.com /images ?q=tbn:-dEjG3JAHxgJ:www.kevcom.com/images/linux/linux.logo.2yp.jpg - DIRECT images.google.com image/jpeg "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312" PROXIED Hacking/Proxy%20Avoidance - 192.16.170.42 SG-HTTP-Service - none -
```

<br>

The third log indicated that at 17:16:08 on 2005-05-04(YYYY-MM-DD), a client at ip 45.23.4.216 with a Windows 2000 user-agent made a GET request for a web application at http://twinpeaksweather.com/java-sys/Dgclock.class.  This request was proxied by 192.16.170.42 and filtered as SG-HTTP-Service.  The TCP_RESCAN_HIT indicated that the requested object was found in the cache but was rescanned because the virus-scanner-tag-id in the object was different from the current scanner tag.

<br>

```
2005-05-04 17:16:08 18 45.23.4.216 304 TCP_RESCAN_HIT 422 405 GET http twinpeaksweather.com /java-sys/Dgclock.class - - DIRECT 66.235.216.135 application/octet-stream "Mozilla/4.0 (Windows 2000 5.0) Java/1.5.0_02" PROXIED News/Media - 192.16.170.42 SG-HTTP-Service - none -
```
