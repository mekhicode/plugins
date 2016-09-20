
sudo apt-get install bind9

sudo vi /etc/bind/named.conf
```
include "/etc/bind/named.conf.example.com";
```

sudo vi /etc/bind/named.conf.example.com
```
zone "example.com" {
        type master;
        file "/etc/bind/db.example.com";
};
```

sudo vi /etc/bind/db.example.com
```
$TTL 86400
$ORIGIN example.com.
@ IN  SOA ns1.example.org root (
    2013031901  ;serial
    12h         ;refresh
    7200        ;retry
    604800      ;expire 
    86400       ;mininum
    )
@ IN  NS  ns1.example.org.
@ IN  NS  ns2.example.org.
@ IN  A   114.80.252.13
www IN  A   114.80.252.13
redmine IN  A   114.80.252.13
gitlab IN  A   114.80.252.13
```

sudo rndc reload

