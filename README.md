# Wake on Magic Packet

**This script will wake my iMac, so that I can then SSH into it. Wake on LAN doesn't work with ssh, 
hence the need for this script.**


## What is a Magic Packet?

> Magic Packet causes the network card to awaken the computer when it receives a magic packet.
> A packet is considered "magic" when it contains FF FF FF FF FF FF (six instances of the largest possible byte value) 
> followed by sixteen instances of the card's six-byte MAC address.
> That sequence can appear anywhere within the frame, so the packet can be sent over any higher-level protocol. 
> Usually, UDP is used, but sometimes raw frames with EtherType 0x0842 are used.
(Source: [Wikipedia](https://en.wikipedia.org/wiki/Wake-on-LAN#Magic_packet).)

## Usage:

1: Change the value of `mac_adress` to the mac address of the target.

2: `python womp.py`

