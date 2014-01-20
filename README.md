What
====

Monitors traffic passing through a machine, taking actions as desired.

How
===

```
sudo apt-get install python-pypcap python-dpkt
sudo ./nethogg.py
```

I suspect pypcap is faster, but it's pretty trivial to switch to pcapy if you prefer.

Why
===

To catch bandwidth hoggers in the London Hackspace network.

Also http://en.wikipedia.org/wiki/Nidhogg.

