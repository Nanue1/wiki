<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Threat Intelligence</a>
<ul>
<li><a href="#sec-1-1">1.1. data source introduction</a></li>
</ul>
</li>
</ul>
</div>
</div>


+HTML\_HEAD: <script type="text/javascript" src="<http://www.pirilampo.org/styles/lib/js/jquery.stickytableheaders.min.js>"></script>

# Threat Intelligence<a id="sec-1" name="sec-1"></a>

## data source introduction<a id="sec-1-1" name="sec-1-1"></a>

### DONE reputation.alienvault.com<a id="sec-1-1-1" name="sec-1-1-1"></a>

-   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-14 Fri 15:45]</span></span>

<p class="verse">
[alienvault-labs](https://www.alienvault.com/who-we-are/alienvault-labs) 实验室每天扫描获取全球的威胁与漏洞,付费产品每三十分钟更新一次数据<br  />
产品提供14天免费试用<br  />
Unified Security Management™ Simplifies Security in the Cloud & On-Premises<br  />
AlienVault unifies all of your essential security tools in one location and combines them with real-time threat intelligence.<br  />
sum: 31978<br  />
</p>

<p class="verse">
tags: scanner spam malware/suspicious<br  />
confidence ：7<br  />
source url : <https://reputation.alienvault.com/reputation.data><br  />
total : 0<br  />
cycle : 1 day<br  />
incremental : 0 /day<br  />
</p>

### DONE osint.bambenekconsulting.com<a id="sec-1-1-2" name="sec-1-1-2"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-03 Mon 16:49]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-06-30 Fri 16:26]</span></span>

数据源爬取规则过老，需要修改规则或者重写爬虫

目前库内只有7w

<http://osint.bambenekconsulting.com/feeds/>

sum: 865311
C&C

1.  <http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist.txt>

2.  <http://osint.bambenekconsulting.com/feeds/c2-dommasterlist.txt>
    -   tags: dga
    -   confidence ：9
    -   source url : <http://osint.bambenekconsulting.com/feeds/dga-feed.txt>
    -   total : 2000
    -   cycle : 1 day
    -   incremental : - /day

### DONE blocklist.de<a id="sec-1-1-3" name="sec-1-1-3"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-06-30 Fri 14:33]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-06-29 Thu 14:07]</span></span>

数据源提供 botnet scanner  spam 数据

扫描数据扫描端口

数据源提供更新时间属性

<https://lists.blocklist.de/lists/> 目录下所有数据
sum : 68711

1.  scanner

    -   tags: scanner
    -   confidence ：7
    -   source url : 
        1.  <http://lists.blocklist.de/lists/ssh.txt>
        2.  <http://lists.blocklist.de/lists/mail.txt>
        3.  <http://lists.blocklist.de/lists/apache.txt>
        4.  <http://lists.blocklist.de/lists/imap.txt>
        5.  <http://lists.blocklist.de/lists/ftp.txt>
        6.  <http://lists.blocklist.de/lists/sip.txt>
        7.  <http://lists.blocklist.de/lists/bruteforcelogin.txt>
    -   total : -
    -   cycle : 1 day
    -   incremental : - /day

2.  botnet

    -   tags: scanner
    -   confidence ：7
    -   source url : <http://lists.blocklist.de/lists/bots.txt>
    -   total : -
    -   cycle : 1 day
    -   incremental : - /day
    
        {
        "_id" : ObjectId("593be9071d41c83f53a07bd4"),
        "confidence" : 7,
        "count" : 1,
        "description" : "",
        "group" : "everyone",
        "indicator" : "5.189.168.152",
        "lasttime" : "",
        "provider" : "blocklist.de",
        "rdata" : "",
        "tags" : "scanner",
        "tlp" : "green"
        }

### DONE emergingthreats.net<a id="sec-1-1-4" name="sec-1-1-4"></a>

-   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-06-29 Thu 13:32]</span></span>

sum: 1289

1.  compromised-ips

    -   tags: botnet,C&C
    -   confidence ：8
    -   source url :
        
        <p class="verse">
        <https://rules.emergingthreats.net/blockrules/compromised-ips.txt>,<br  />
        <https://rules.emergingthreats.net/blockrules/emerging-compromised.rules>,<br  />
        <https://rules.emergingthreats.net/blockrules/emerging-botcc.excluded>,<br  />
        <https://rules.emergingthreats.net/blockrules/emerging-compromised.suricata.rules>,<br  />
        <https://rules.emergingthreats.net/blockrules/emerging-compromised.suricata.rules><br  />
        <https://rules.emergingthreats.net/blockrules/emerging-botcc.suricata.rules>,<br  />
        <https://rules.emergingthreats.net/blockrules/emerging-botcc.rules><br  />
        <https://rules.emergingthreats.net/blockrules/emerging-botcc.portgrouped.rules>,<br  />
        <https://rules.emergingthreats.net/blockrules/emerging-botcc.portgrouped.suricata.rules>,<br  />
        </p>
    -   total : 1254
    -   cycle : 1 day
    -   incremental :  /day

### DONE netlab.360.com<a id="sec-1-1-5" name="sec-1-1-5"></a>

-   State "DONE"       from "UNDO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-04 Tue 11:17]</span></span>
-   State "UNDO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-06-30 Fri 16:02]</span></span>

Domain generation algorithms (DGA)

这个实验室提供的 dga ek 域名生产算法产生的域名已经是失效的

1.  exploit malware

    -   tags:exploit malware
    -   confidence ：7
    -   source url :<http://data.netlab.360.com/feeds/ek/magnitude.txt>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

2.  dga

    -   tags:dga
    -   confidence ：7
    -   source url :
    
    <p class="verse">
    ek<br  />
    <http://data.netlab.360.com/feeds/ek/magnitude.txt><br  />
    dga<br  />
    <http://data.netlab.360.com/feeds/dga/bamital.txt><br  />
    <http://data.netlab.360.com/feeds/dga/banjori.txt><br  />
    <http://data.netlab.360.com/feeds/dga/banjori.txt><br  />
    <http://data.netlab.360.com/feeds/dga/chinad.txt><br  />
    <http://data.netlab.360.com/feeds/dga/conficker.txt><br  />
    <http://data.netlab.360.com/feeds/dga/cryptolocker.txt><br  />
    <http://data.netlab.360.com/feeds/dga/dircrypt.txt><br  />
    <http://data.netlab.360.com/feeds/dga/dyre.txt><br  />
    <http://data.netlab.360.com/feeds/dga/fobber.txt><br  />
    <http://data.netlab.360.com/feeds/dga/gameover.txt><br  />
    <http://data.netlab.360.com/feeds/dga/gspy.txt><br  />
    <http://data.netlab.360.com/feeds/dga/locky.txt><br  />
    <http://data.netlab.360.com/feeds/dga/madmax.txt><br  />
    <http://data.netlab.360.com/feeds/dga/mirai.txt><br  />
    <http://data.netlab.360.com/feeds/dga/murofet.txt><br  />
    <http://data.netlab.360.com/feeds/dga/necurs.txt><br  />
    <http://data.netlab.360.com/feeds/dga/nymaim.txt><br  />
    <http://data.netlab.360.com/feeds/dga/proslikefan.txt><br  />
    <http://data.netlab.360.com/feeds/dga/pykspa.txt><br  />
    <http://data.netlab.360.com/feeds/dga/qadars.txt><br  />
    <http://data.netlab.360.com/feeds/dga/ranbyus.txt><br  />
    <http://data.netlab.360.com/feeds/dga/rovnix.txt><br  />
    <http://data.netlab.360.com/feeds/dga/shifu.txt><br  />
    <http://data.netlab.360.com/feeds/dga/simda.txt><br  />
    <http://data.netlab.360.com/feeds/dga/suppobox.txt><br  />
    <http://data.netlab.360.com/feeds/dga/symmi.txt><br  />
    <http://data.netlab.360.com/feeds/dga/tempedreve.txt><br  />
    <http://data.netlab.360.com/feeds/dga/tinba.txt><br  />
    <http://data.netlab.360.com/feeds/dga/tofsee.txt><br  />
    <http://data.netlab.360.com/feeds/dga/vawtrak.txt><br  />
    <http://data.netlab.360.com/feeds/dga/vidro.txt><br  />
    </p>
    
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### DONE abuse.ch<a id="sec-1-1-6" name="sec-1-1-6"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-12 Wed 17:19]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-05 Wed 12:04]</span></span>

sum :16810

1.  DONE sslbl.abuse.ch

    -   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-06 Thu 16:13]</span></span>
              15 分钟更新一次 botnet malware C&C
    -   tags: botnet
    -   confidence ：10
    -   source url :
        1.  <https://sslbl.abuse.ch/blacklist/sslblacklist.csv>   C&C  sha1
        2.  <https://sslbl.abuse.ch/blacklist/sslipblacklist.csv> C&C  ip
        3.  <https://sslbl.abuse.ch/blacklist/sslipblacklist_aggressive.csv> C&C ip
        4.  <https://sslbl.abuse.ch/blacklist/dyre_sslipblacklist.csv>  C&C ip
        5.  <https://sslbl.abuse.ch/blacklist/dyre_sslblacklist.csv>  C&C sha1
    -   total :2384
    -   cycle : 1 day
    -   incremental :  /day

2.  DONE zeustracker.abuse.ch

    -   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-12 Wed 16:34]</span></span>
    -   tags: botnet
    -   confidence ：9
    -   source url :
    
    <p class="verse">
    <https://zeustracker.abuse.ch/blocklist.php?download=baddomains>   domain  C&C<br  />
    <https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist> domain C&C<br  />
    <br  />
    <https://zeustracker.abuse.ch/blocklist.php?download=badips>   ip C&C<br  />
    <http://zeustracker.abuse.ch/blocklist.php?download=ipblocklist> ip C&C<br  />
    <br  />
    <https://zeustracker.abuse.ch/blocklist.php?download=compromised> url Botnets<br  />
    <br  />
    <https://zeustracker.abuse.ch/removals.php> domain C&C<br  />
    </p>
    
    -   total : 673
    -   cycle : 1 day
    -   incremental :  /day

3.  DONE feodotracker.abuse.ch

    -   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-12 Wed 16:58]</span></span>
    
    sum : 903
    -   tags: botnet
    -   confidence ：6-8
    -   source url :
    
    <p class="verse">
    1. <https://feodotracker.abuse.ch/blocklist/?download=domainblocklist> 8 domain<br  />
    2. <https://feodotracker.abuse.ch/blocklist/?download=ipblocklist>  6 ip<br  />
    </p>
    
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

4.  DONE ransomware.abuse.ch

    -   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-12 Wed 17:19]</span></span>
    -   tags:botnet
    -   confidence ：9
    -   source url :
        
        <http://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt>
        
        <http://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt>,
        
        <http://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt>,
        
        <http://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt>,
    
    -   total :12850
    -   cycle : 1 day
    -   incremental :  /day

### DONE antispam.imp.ch<a id="sec-1-1-7" name="sec-1-1-7"></a>

-   State "DONE"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-06-28 Wed 10:38]</span></span>

imp.ch 的反垃圾邮件 共享feed项目,声称每15分钟更新一次

但已经停止更新了。
-   tags: Spam Sources
-   confidence ：9
-   source url :<http://antispam.imp.ch/spamlist>
-   total : 943
-   cycle : 15 minutes
-   incremental : 0/day

### DONE alexa.com<a id="sec-1-1-8" name="sec-1-1-8"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-19 Wed 15:38]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-14 Fri 19:54]</span></span>

亚马逊的alexa提供站点排名

sum：1529

1.  top-1000

    -   tags: whitelist
    -   confidence ：5
    -   source url : <http://s3.amazonaws.com/alexa-static/top-1m.csv.zip>
    -   total : 1529
    -   cycle : 1 day
    -   incremental : 100+ /day
    
        {
        "_id" : ObjectId("593ba272256c1046ad056f91"),
        "confidence" : 5,
        "count" : 1,
        "description" : "alexa #972",//站点排名
        "group" : "everyone",
        "indicator" : "11st.co.kr", //域名信息
        "lasttime" : "",
        "provider" : "alexa.com",
        "rdata" : "",
        "tags" : "whitelist",
        "tlp" : "green"
        }

### DONE public-dns.info<a id="sec-1-1-9" name="sec-1-1-9"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-20 Thu 14:16]</span></span>
-   tags: whitelist
-   confidence ：5  
    
    <https://public-dns.info/nameservers-all.txt>

### DONE umbrella.cisco.com<a id="sec-1-1-10" name="sec-1-1-10"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-24 Mon 17:12]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-17 Mon 10:16]</span></span>

一级域名

sum：1134

1.  top-1000

    -   tags: whitelist
    -   confidence ：5
    -   source url : <http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip>
    -   total : 1134
    -   cycle : 1 day
    -   incremental : 100+ /day
    
        {
        "_id" : ObjectId("593be90a1d41c83fa8a07c1b"),
        "confidence" : 5,
        "count" : 1,
        "description" : "cisco umbrella #401",
        "group" : "everyone",
        "indicator" : "t.co",
        "lasttime" : "",
        "provider" : "umbrella.cisco.com",
        "rdata" : "",
        "tags" : "whitelist",
        "tlp" : "green"
        }

### DONE danger.rulez.sk<a id="sec-1-1-11" name="sec-1-1-11"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 11:12]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-17 Mon 10:16]</span></span>
         sum : 1254

1.  scanner

    -   tags: scanner
    -   confidence ：9
    -   source url :<http://danger.rulez.sk/projects/bruteforceblocker/blist.php>
    -   total : 1254
    -   cycle : 1 day
    -   incremental :  /day

### DONE csirtg.io<a id="sec-1-1-12" name="sec-1-1-12"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 13:48]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-17 Mon 10:16]</span></span>

Unsolicited Commercial Email(UCE)商业垃圾邮件

<https://csirtg.io/users/csirtgadgets/feeds/uce-urls>

feed有限制250条 需要继续观察数据量
sum: 1037

1.  scanner

    -   tags: scanner
    -   confidence ：9
    -   source url : <https://csirtg.io/api/users/csirtgadgets/feeds/port-scanners.csv>
    -   total : -
    -   cycle : 1 day
    -   incremental :  /day

2.  uce

    -   tags: spam
    -   confidence ：9
    -   source url : 
        1.  <https://csirtg.io/api/users/csirtgadgets/feeds/uce-urls.csv>
        2.  <https://csirtg.io/api/users/csirtgadgets/feeds/uce-email-addresses.csv>
        3.  <https://csirtg.io/api/users/csirtgadgets/feeds/uce-ip.csv>
    -   total : -
    -   cycle : 1 day
    -   incremental :  /day

3.  darknet

    -   tags: darknet
    -   confidence ：9
    -   source url :<https://csirtg.io/api/users/wes/feeds/darknet.csv>
    -   total : -
    -   cycle : 1 day
    -   incremental :  /day

### DONE dataplane.org<a id="sec-1-1-13" name="sec-1-1-13"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-07 Mon 14:08]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 13:48]</span></span>

sum : 46710

1.  scanner

    -   tags: scanner
    -   confidence ：9
    -   source url :
        1.  <https://dataplane.org/sshclient.txt>
        2.  <https://dataplane.org/sshpwauth.txt>
        3.  <https://dataplane.org/sipquery.txt>
        4.  <https://dataplane.org/sipinvitation.txt>
        5.  <https://dataplane.org/sipregistration.txt>
    -   total : 1254
    -   cycle : 1 day
    -   incremental :  /day

### DONE malc0de.com<a id="sec-1-1-14" name="sec-1-1-14"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-07 Mon 15:18]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 13:48]</span></span>

提取代码出现问题

sum : 0

1.  malware

    -   tags: malware
    -   confidence ：9
    -   source url :<http://malc0de.com/rss/>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### UNDO mirc.com<a id="sec-1-1-15" name="sec-1-1-15"></a>

-   State "UNDO"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-07 Mon 15:43]</span></span>
          提供了几十个irc聊天服务器的域名地址,而且是2016年就停止更新了
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 13:48]</span></span>

sum : 191

1.  domains

    -   tags: whitelist
    -   confidence ：8
    -   source url :<http://www.mirc.com/servers.ini>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### DONE nothink.org<a id="sec-1-1-16" name="sec-1-1-16"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-07 Mon 15:52]</span></span>
-   State "TODO"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 13:49]</span></span>

1.  scanner

    -   tags:exploit malware
    -   confidence ：7
    -   source url :<http://www.nothink.org/blacklist/blacklist_ssh_day.txt>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### DONE openphish.com<a id="sec-1-1-17" name="sec-1-1-17"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-07 Mon 15:59]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-07-25 Tue 13:49]</span></span>

1.  phishing

    -   tags:phishing
    -   confidence ：9
    -   source url :<https://openphish.com/feed.txt>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### DONE vxvazlt.net<a id="sec-1-1-18" name="sec-1-1-18"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-23 Wed 17:36]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-08-21 Mon 16:16]</span></span>
-   source url :
    1.<http://vxvault.net/URL_List.php>
-   data\_type：2
-   indicator: url
-   confidence ：10
-   alive: False
-   source: phishtank.com
-   tag:7
-   description:none
-   updated\_time:"none"
-   created\_time:当前时间(2017-06-30T14:22:44)

### DONE spamhaus.org<a id="sec-1-1-19" name="sec-1-1-19"></a>

-   State "DONE"       from "SOMEDAY"    <span class="timestamp-wrapper"><span class="timestamp">[2017-09-25 Mon 14:33]</span></span>

需要代理 asn数据待入
-   State "TODO"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-23 Wed 12:17]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-08-21 Mon 16:16]</span></span>
-   source url :
    1.  <http://www.spamhaus.org/drop/drop.txt>
    2.  <http://www.spamhaus.org/drop/edrop.txt>
    3.  <https://www.spamhaus.org/drop/asndrop.txt>
-   indicator: IP
-   confidence ：9
-   data\_type：0
-   alive: False
-   source:www.spamhaus.org
-   tag:3
-   description:'none'
-   updated\_time:'none'
-   created\_time:当前时间(2017-06-30T14:22:44)

### DONE phishtank.com<a id="sec-1-1-20" name="sec-1-1-20"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-09-25 Mon 14:32]</span></span>

实习生doning
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-08-21 Mon 16:16]</span></span>
-   source url :
    1.  <http://data.phishtank.com/data/%7Btoken%7D/online-valid.json.gz>
-   data\_type：2
-   indicator: url
-   confidence ：9
-   alive: true
-   source: phishtank.com
-   tag:8
-   description:none
-   updated\_time:数据源提供时间(2017-06-30T14:22:44)
-   created\_time:当前时间(2017-06-30T14:22:44)

### DONE dragonresearchgroup.org<a id="sec-1-1-21" name="sec-1-1-21"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-09-25 Mon 14:32]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-09-04 Mon 11:00]</span></span>
    -   tags: scanner
    -   confidence ：9
    -   source url :
        1.  <http://dragonresearchgroup.org/insight/sshpwauth.txt>
        2.  <http://dragonresearchgroup.org/insight/http-report.txt>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### DONE watcherlab.com<a id="sec-1-1-22" name="sec-1-1-22"></a>

-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-10-10 Tue 17:44]</span></span>
-   State "TODO"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2017-10-10 Tue 17:27]</span></span>
-   State "DONE"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2017-10-10 Tue 17:27]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-09-04 Mon 11:00]</span></span>

1.  cc

    -   tags: cc
    -   confidence ：9
    -   source url :<http://feed.watcherlab.com/>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### TODO isc.sans.edu<a id="sec-1-1-23" name="sec-1-1-23"></a>

需要代理 
-   State "TODO"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-24 Thu 09:51]</span></span>
-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-24 Thu 09:51]</span></span>
-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-08-21 Mon 16:16]</span></span>
-   source url :
    1.  <https://isc.sans.edu/feeds/suspiciousdomains_Low.txt>
    2.  <https://isc.sans.edu/feeds/suspiciousdomains_High.txt>
    3.  <https://isc.sans.edu/feeds/suspiciousdomains_Medium.txt>
    4.  <https://isc.sans.edu/feeds/block.txt>
-   data\_type：0
-   indicator: url
-   confidence ：9
-   alive: true
-   source: phishtank.com
-   tag:8
-   description:none
-   updated\_time:数据源提供时间(2017-06-30T14:22:44)
-   created\_time:当前时间(2017-06-30T14:22:44)

1.  scanner

    -   tags: scanner
    -   confidence ：7-9
    -   source url :
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### TODO packetmail.net<a id="sec-1-1-24" name="sec-1-1-24"></a>

代理问题
-   State "TODO"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2017-09-04 Mon 10:58]</span></span>
-   State "DONE"       from "TODO"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-24 Thu 09:51]</span></span>
-   State "TODO"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2017-08-15 Tue 09:57]</span></span>
-   source url :
    1.  <https://www.packetmail.net/iprep.txt>
    2.  <https://www.packetmail.net/iprep_mail.txt>
    3.  <https://www.packetmail.net/iprep_ramnode.txt>
-   indicator: IP
-   confidence ：8
-   data\_type：0
-   alive: true
-   source: packetmail.net
-   tag:5
-   description:none
-   updated\_time:数据源提供时间(2017-06-30T14:22:44)
-   created\_time:当前时间(2017-06-30T14:22:44)

### TODO otx.alienvault.com<a id="sec-1-1-25" name="sec-1-1-25"></a>

-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-10-10 Tue 15:22]</span></span>

1.  otx

    -   tags: DDos ,C&C,Malware,Proxy,Phishing,Scanner,suspicious
    -   confidence ：5
    -   source url :
        1.  <https://sslbl.abuse.ch/blacklist/sslipblacklist.csv>
        2.  <https://sslbl.abuse.ch/blacklist/dyre_sslipblacklist.csv>
        3.  <https://sslbl.abuse.ch/blacklist/sslblacklist.csv>
    -   total :
    -   cycle : 1 day
    -   incremental :  /day

### TODO malwaredomainlist.com<a id="sec-1-1-26" name="sec-1-1-26"></a>

-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-09-25 Mon 14:35]</span></span>

### badips.com<a id="sec-1-1-27" name="sec-1-1-27"></a>

source url : 1.<https://www.badips.com/get/list/any/2?age=7d>
data\_type: 0
indicator: ip
tags: scanners
source: badips.com

### raw.githubusercontent.com<a id="sec-1-1-28" name="sec-1-1-28"></a>

source url: 
1.<https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_1d.ipset>
2.<https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset>
data\_type:0
indicator:ip
tags:
source: raw.githubusercontent.com

### cinsscore.com<a id="sec-1-1-29" name="sec-1-1-29"></a>

source url: 1.<http://cinsscore.com/list/ci-badguys.txt>
data\_type:0
indicator: ip
tags: scanner
source: cinsscore.com

### cybercrime-tracker.net<a id="sec-1-1-30" name="sec-1-1-30"></a>

source url: 1.<http://cybercrime-tracker.net/ccam.php>
data\_type: 1
indicator: domain
tags:
source: cybercrime-tracker.net
注：数据既有ip又有domain

### dataplane.org<a id="sec-1-1-31" name="sec-1-1-31"></a>

source url: 1.<https://dataplane.org/dnsrd.txt>
          2.<https://dataplane.org/dnsrd.txt>
          3.<https://dataplane.org/dnsversion.txt>
          4.<https://dataplane.org/vncrfb.txt>
 data\_type: 0
 indicator: ip
 tags: scanner
 confidence：9
 source: dataplane.org

### blocklist.greensnow.co<a id="sec-1-1-32" name="sec-1-1-32"></a>

source url: 1.<http://blocklist.greensnow.co/greensnow.txt>
data\_type:0
indicator: ip
tags: scanner
source: blocklist.greensnow.co

### malwaredomainlist.com<a id="sec-1-1-33" name="sec-1-1-33"></a>

source url: 1.<http://www.malwaredomainlist.com/hostslist/ip.txt>
data\_type:0
indicator: ip
tags: scanner
source: malwaredomainlist.com

### maxmind.com<a id="sec-1-1-34" name="sec-1-1-34"></a>

source url: 1.<https://www.maxmind.com/en/high-risk-ip-sample-list>
data\_type:0
indicator: ip
tags: 
source: www.maxmind.com

### rutgers.edu<a id="sec-1-1-35" name="sec-1-1-35"></a>

source url: 1.<https://report.cs.rutgers.edu/DROP/attackers>
data\_type:0
indicator: ip
tags: scanner
source: rutgers.edu

### 统计表<a id="sec-1-1-36" name="sec-1-1-36"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="left" />

<col  class="right" />

<col  class="right" />

<col  class="right" />

<col  class="left" />

<col  class="right" />

<col  class="left" />

<col  class="right" />

<col  class="right" />

<col  class="left" />

<col  class="right" />

<col  class="left" />

<col  class="left" />

<col  class="left" />

<col  class="left" />

<col  class="right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="left">&#xa0;</th>
<th scope="col" class="right">scanner</th>
<th scope="col" class="right">spam</th>
<th scope="col" class="right">botnet</th>
<th scope="col" class="left">c&c</th>
<th scope="col" class="right">malware</th>
<th scope="col" class="left">phishing</th>
<th scope="col" class="right">whitelist</th>
<th scope="col" class="right">darknet</th>
<th scope="col" class="left">ddos</th>
<th scope="col" class="right">exploit</th>
<th scope="col" class="left">honeypot</th>
<th scope="col" class="left">hijacked</th>
<th scope="col" class="left">suspicious</th>
<th scope="col" class="left">data-type</th>
<th scope="col" class="right">sum</th>
</tr>
</thead>

<tbody>
<tr>
<td class="left">alexa.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">5</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">DOMAIN</td>
<td class="right">1529</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">reputation.alienvault.com</td>
<td class="right">7</td>
<td class="right">6</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">6</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">31978</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">osint.bambenekconsulting.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">9</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">865311</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">blocklist.de</td>
<td class="right">7</td>
<td class="right">&#xa0;</td>
<td class="right">7</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">68711</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">umbrella.cisco.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">5</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">DOMAIN</td>
<td class="right">1134</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">csirtg.io</td>
<td class="right">9</td>
<td class="right">9</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">9</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP,URL,</td>
<td class="right">1037</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">danger.rulez.sk</td>
<td class="right">9</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">1254</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">dataplane.org</td>
<td class="right">9</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">46710</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">emergingthreats.net</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">8</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">1289</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">abuse.ch</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">8-10</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">URL ,IP ,MD5</td>
<td class="right">16810</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">malc0de.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">9</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">URL,IP,MD5</td>
<td class="right">0</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">mirc.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">8</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">URL</td>
<td class="right">191</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">netlab.360.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">7</td>
<td class="left">&#xa0;</td>
<td class="right">7</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">7</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP,URL,DOMAIN,MD5</td>
<td class="right">889955</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">nothink.org</td>
<td class="right">7</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">193</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">openphish.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">9</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">URL</td>
<td class="right">5352</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">packetmail.net</td>
<td class="right">8</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">8</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">16424</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">phishtank.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">9</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">27128</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">isc.sans.edu</td>
<td class="right">8</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">7-9</td>
<td class="left">IP</td>
<td class="right">0</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">spamhaus.org</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">9</td>
<td class="left">&#xa0;</td>
<td class="left">ASN,IPv6,Network</td>
<td class="right">1241</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">vxvault.net</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">9</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">196</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">otx.alienvault.com</td>
<td class="right">5</td>
<td class="right">5</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">5</td>
<td class="left">5</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">5</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">5</td>
<td class="left">IP,URL,MD5</td>
<td class="right">0</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">antispam.imp.ch</td>
<td class="right">&#xa0;</td>
<td class="right">9</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">0</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">dragonresearchgroup.org</td>
<td class="right">9</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">0</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">watcherlab.com</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">9</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">IP</td>
<td class="right">0</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="left">sum</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="left">&#xa0;</td>
<td class="right">1976443</td>
</tr>
</tbody>
</table>

### base info<a id="sec-1-1-37" name="sec-1-1-37"></a>

-   data-type
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="left" />
    
    <col  class="right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="left">ip</td>
    <td class="right">0</td>
    </tr>
    
    
    <tr>
    <td class="left">domain</td>
    <td class="right">1</td>
    </tr>
    
    
    <tr>
    <td class="left">url</td>
    <td class="right">2</td>
    </tr>
    
    
    <tr>
    <td class="left">md5</td>
    <td class="right">3</td>
    </tr>
    
    
    <tr>
    <td class="left">sha256</td>
    <td class="right">4</td>
    </tr>
    
    
    <tr>
    <td class="left">sha1</td>
    <td class="right">5</td>
    </tr>
    </tbody>
    </table>
-   tags 标签说明
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="right" />
    
    <col  class="left" />
    
    <col  class="left" />
    </colgroup>
    <tbody>
    <tr>
    <td class="right">0</td>
    <td class="left">Suspicious</td>
    <td class="left">可疑的</td>
    </tr>
    
    
    <tr>
    <td class="right">1</td>
    <td class="left">DDos</td>
    <td class="left">DDos攻击</td>
    </tr>
    
    
    <tr>
    <td class="right">2</td>
    <td class="left">Exploits</td>
    <td class="left">漏洞攻击</td>
    </tr>
    
    
    <tr>
    <td class="right">3</td>
    <td class="left">Spam Sources</td>
    <td class="left">垃圾邮件</td>
    </tr>
    
    
    <tr>
    <td class="right">4</td>
    <td class="left">Web  Attacks</td>
    <td class="left">Web攻击</td>
    </tr>
    
    
    <tr>
    <td class="right">5</td>
    <td class="left">Scanners</td>
    <td class="left">扫描源</td>
    </tr>
    
    
    <tr>
    <td class="right">6</td>
    <td class="left">Botnets</td>
    <td class="left">僵尸网络被控端</td>
    </tr>
    
    
    <tr>
    <td class="right">7</td>
    <td class="left">Malware</td>
    <td class="left">恶意软件</td>
    </tr>
    
    
    <tr>
    <td class="right">8</td>
    <td class="left">Phishing</td>
    <td class="left">钓鱼</td>
    </tr>
    
    
    <tr>
    <td class="right">9</td>
    <td class="left">Proxy</td>
    <td class="left">代理</td>
    </tr>
    
    
    <tr>
    <td class="right">10</td>
    <td class="left">C&C</td>
    <td class="left">僵尸网络控制端</td>
    </tr>
    
    
    <tr>
    <td class="right">11</td>
    <td class="left">Whitelist</td>
    <td class="left">白名单</td>
    </tr>
    
    
    <tr>
    <td class="right">12</td>
    <td class="left">Honeypot</td>
    <td class="left">蜜罐</td>
    </tr>
    
    
    <tr>
    <td class="right">13</td>
    <td class="left">DGA</td>
    <td class="left">域名随机生成</td>
    </tr>
    </tbody>
    </table>
-   confidence  数据源的可信度
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="left" />
    
    <col  class="left" />
    </colgroup>
    <tbody>
    <tr>
    <td class="left">(9-10)</td>
    <td class="left">Certain</td>
    </tr>
    
    
    <tr>
    <td class="left">(7-8)</td>
    <td class="left">Very Confident</td>
    </tr>
    
    
    <tr>
    <td class="left">(6-7)</td>
    <td class="left">Somewhat Confident</td>
    </tr>
    
    
    <tr>
    <td class="left">(5-6)</td>
    <td class="left">Not Confident</td>
    </tr>
    
    
    <tr>
    <td class="left">(5)</td>
    <td class="left">"50/50 shot"</td>
    </tr>
    
    
    <tr>
    <td class="left">(0-4)</td>
    <td class="left">Informational Data</td>
    </tr>
    </tbody>
    </table>
-   统计表
    
    ![img](//7xpyfe.com1.z0.glb.clouddn.com/blog/20170616/135122999.png)
-   数据库内存储格式
    -   录入机制:
        同一数据源来的数据，威胁类型不变时，
        
        只更新该类型记录更新时间,created\_time不会变化
        
        当indicator 和 tag都变化的时候，才会录入一条新的数据
    -   更新机制
        每天通过created\_time获取新怎么的数据
    
        {
           "indicator":"1.180.74.58",
           "data_type":0,
           "confidence":7,
           "alive":true/false,
           "updated_time":"2017-06-30T14:22:44"/"none",
           "source":"blocklist.de",
           "tag":5,
           "created_time":"2017-06-30T14:22:44"
           "description":""
        }

### TODO other source<a id="sec-1-1-38" name="sec-1-1-38"></a>

-   State "TODO"       from ""           <span class="timestamp-wrapper"><span class="timestamp">[2017-06-16 Fri 13:11]</span></span>
-   spamhaustech
    <https://www.spamhaustech.com/protecting-mail-streams/>
-   abusix
    <https://www.abusix.com/>
-   apwg.org
    <https://apwg.org/>
    2003年创建的国际跨行业情报联盟 出网络钓鱼的报告可供下载
    
    没找到feed源
    
    提供数据分享的方式 <https://sourceforge.net/projects/ecrisp-x/>
-   <http://txt.proxyspy.net/proxy.txt>
           <http://www.malwareurl.com>
           <http://www.malwaredomainlist.com/mdl.php>

<<<<<<< HEAD

`=====`

>>>>>>> f346d7973f1c8caefbad2f6e1e86f0546df81356