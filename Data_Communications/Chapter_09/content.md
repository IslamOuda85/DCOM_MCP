---
doc_type: scientific_content
course_id: data_communications
chapter: 9
chapter_id: data_communications_ch09
chapter_title: Introduction to Data-Link Layer
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_9/ch9.pdf
  pages: 235-256
assets_dir: assets
asset_counts:
  illustration: 16
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:32:00+00:00'
status: complete
---
# Chapter 9: Introduction to Data-Link Layer

## Chapter Objectives
> id: ch09-0 | src: book p.237 | kind: objectives

The TCP/IP protocol suite does not define any protocol in the data-link layer or
physical layer. These two layers are territories of networks that when connected
make up the Internet. These networks, wired or wireless, provide services to the upper
three layers of the TCP/IP suite. This may give us a clue that there are several standard
protocols in the market today. For this reason, we discuss the data-link layer in several
chapters. This chapter is an introduction that gives the general idea and common issues
in the data-link layer that relate to all networks.

- The first section introduces the data-link layer. It starts with defining the concept
of links and nodes. The section then lists and briefly describes the services provided by the data-link layer. It next defines two categories of links: point-to-point
and broadcast links. The section finally defines two sublayers at the data-link layer
that will be elaborated on in the next few chapters.

- The second section discusses link-layer addressing. It first explains the rationale
behind the existence of an addressing mechanism at the data-link layer. It then
describes three types of link-layer addresses to be found in some link-layer protocols. The section discusses the Address Resolution Protocol (ARP), which maps
the addresses at the network layer to addresses at the data-link layer. This protocol
helps a packet at the network layer find the link-layer address of the next node for
delivery of the frame that encapsulates the packet. To show how the network layer
helps us to find the data-link-layer addresses, a long example is included in this
section that shows what happens at each node when a packet is travelling through
the Internet.

## 9.1 INTRODUCTION
> id: ch09-9-1 | src: book 9.1; p.238 | kind: concept

The Internet is a combination of networks glued together by connecting devices (routers or switches). If a packet is to travel from a host to another host, it needs to pass
through these networks. Figure 9.1 shows the same scenario we discussed in Chapter 3,
but we are now interested in communication at the data-link layer. Communication at
the data-link layer is made up of five separate logical connections between the data-link
layers in the path.

> **[ASSET ch09_ill_001]** Figure 9.1: Communication at the data-link layer
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_001.png
> - src: book Figure 9.1; p.238
> - shows: Figure 9.1: Communication at the data-link layer. A layered Internet path connects an application on the source host to an application on the destination host through routers; network-layer communication is end to end while data-link communication is hop by hop.
> - structure: A layered Internet path connects an application on the source host to an application on the destination host through routers; network-layer communication is end to end while data-link communication is hop by hop.
> - text_in_image: Sky Research; Alice; Application; Alice; Transport; Network; Data-link; Physical; R2; Network; To other; Data-link; ISPs; Physical; R2; R1; R4; Network; To other; R3; R4; Data-link; ISPs; Physical; Switched; R5; WAN; Network; Data-link; National ISP; R5; Physical; ISP; R7; Network; To other; ISPs; Data-link; R6; R7; Physical; Legend; Point-to-point WAN; Bob; LAN switch; Application; Transport; WAN switch; Network; Data-link; Router; Bob; Physical; Scientific Books
> - use_when: Teach ch09-9-1, interpret Figure 9.1, trace address changes, or solve a linked practice question.
> - confidence: high

The data-link layer at Alice’s computer communicates with the data-link layer at router
R2. The data-link layer at router R2 communicates with the data-link layer at router R4,
and so on. Finally, the data-link layer at router R7 communicates with the data-link
layer at Bob’s computer. Only one data-link layer is involved at the source or the destination, but two data-link layers are involved at each router. The reason is that Alice’s
and Bob’s computers are each connected to a single network, but each router takes
input from one network and sends output to another network. Note that although
switches are also involved in the data-link-layer communication, for simplicity we have
not shown them in the figure.

### 9.1.1 Nodes and Links
> id: ch09-9-1-1 | src: book 9.1.1; p.239 | kind: concept

Communication at the data-link layer is node-to-node. A data unit from one point in the
Internet needs to pass through many networks (LANs and WANs) to reach another
point. Theses LANs and WANs are connected by routers. It is customary to refer to the
two end hosts and the routers as nodes and the networks in between as links. Figure 9.2
is a simple representation of links and nodes when the path of the data unit is only six
nodes.

> **[ASSET ch09_ill_002]** Figure 9.2: Nodes and Links
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_002.png
> - src: book Figure 9.2; p.239
> - shows: Figure 9.2: Nodes and Links. Two views identify nodes and links: LANs joined by routers form point-to-point Internet links, and an abstract chain alternates node and link symbols.
> - structure: Two views identify nodes and links: LANs joined by routers form point-to-point Internet links, and an abstract chain alternates node and link symbols.
> - text_in_image: Point-to-point; Point-to-point; network; network; LAN; LAN; LAN; a. A small part of the Internet; Link; Link; Link; Link; Link; Node; Node; Node; Node; Node; Node; b. Nodes and links
> - use_when: Teach ch09-9-1-1, interpret Figure 9.2, trace address changes, or solve a linked practice question.
> - confidence: high

The first node is the source host; the last node is the destination host. The other
four nodes are four routers. The first, the third, and the fifth links represent the three
LANs; the second and the fourth links represent the two WANs.

### 9.1.2 Services
> id: ch09-9-1-2 | src: book 9.1.2; p.239 | kind: concept

The data-link layer is located between the physical and the network layers. The data-link layer provides services to the network layer; it receives services from the physical
layer. Let us discuss services provided by the data-link layer.
The duty scope of the data-link layer is node-to-node. When a packet is travelling
in the Internet, the data-link layer of a node (host or router) is responsible for delivering
a datagram to the next node in the path. For this purpose, the data-link layer of the
sending node needs to encapsulate the datagram received from the network in a frame,
and the data-link layer of the receiving node needs to decapsulate the datagram from
the frame. In other words, the data-link layer of the source host needs only to
encapsulate, the data-link layer of the destination host needs to decapsulate, but each
intermediate node needs to both encapsulate and decapsulate. One may ask why we
need encapsulation and decapsulation at each intermediate node. The reason is that
each link may be using a different protocol with a different frame format. Even if one
link and the next are using the same protocol, encapsulation and decapsulation are
needed because the link-layer addresses are normally different. An analogy may help in
this case. Assume a person needs to travel from her home to her friend’s home in
another city. The traveller can use three transportation tools. She can take a taxi to go to
the train station in her own city, then travel on the train from her own city to the city
where her friend lives, and finally reach her friend’s home using another taxi. Here we
have a source node, a destination node, and two intermediate nodes. The traveller needs
to get into the taxi at the source node, get out of the taxi and get into the train at the first
intermediate node (train station in the city where she lives), get out of the train and get
into another taxi at the second intermediate node (train station in the city where her
friend lives), and finally get out of the taxi when she arrives at her destination. A kind
of encapsulation occurs at the source node, encapsulation and decapsulation occur at
the intermediate nodes, and decapsulation occurs at the destination node. Our traveller
is the same, but she uses three transporting tools to reach the destination.
Figure 9.3 shows the encapsulation and decapsulation at the data-link layer. For
simplicity, we have assumed that we have only one router between the source and destination. The datagram received by the data-link layer of the source host is encapsulated
in a frame. The frame is logically transported from the source host to the router. The
frame is decapsulated at the data-link layer of the router and encapsulated at another
frame. The new frame is logically transported from the router to the destination host.
Note that, although we have shown only two data-link layers at the router, the router
actually has three data-link layers because it is connected to three physical links.

> **[ASSET ch09_ill_003]** Figure 9.3: A communication with only three nodes
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_003.png
> - src: book Figure 9.3; p.240
> - shows: Figure 9.3: A communication with only three nodes. A datagram crosses three nodes using two different link types; each hop places the unchanged network-layer datagram inside a link-specific frame with its own data-link header.
> - structure: A datagram crosses three nodes using two different link types; each hop places the unchanged network-layer datagram inside a link-specific frame with its own data-link header.
> - text_in_image: Actual link; Data-link header; 2; Legend; Logical link; Datagram; Datagram; Datagram; Datagram; Datagram; 2; 2; Data link; Data link; Data link; Data link; Frame: type 1; Frame: type 2; Link: of type 1; Link: of type 2; Source; Destination; To another link
> - use_when: Teach ch09-9-1-2, interpret Figure 9.3, trace address changes, or solve a linked practice question.
> - confidence: high

With the contents of the above figure in mind, we can list the services provided by
a data-link layer as shown below.

#### Framing
> id: ch09-9-1-2-framing | src: book p.241 | kind: concept

Definitely, the first service provided by the data-link layer is framing. The data-link
layer at each node needs to encapsulate the datagram (packet received from the network
layer) in a frame before sending it to the next node. The node also needs to decapsulate
the datagram from the frame received on the logical channel. Although we have shown
only a header for a frame, we will see in future chapters that a frame may have both a
header and a trailer. Different data-link layers have different formats for framing.

A packet at the data-link layer is normally called a frame.

#### Flow Control
> id: ch09-9-1-2-flow-control | src: book p.241 | kind: concept

Whenever we have a producer and a consumer, we need to think about flow control. If
the producer produces items that cannot be consumed, accumulation of items occurs.
The sending data-link layer at the end of a link is a producer of frames; the receiving
data-link layer at the other end of a link is a consumer. If the rate of produced frames is
higher than the rate of consumed frames, frames at the receiving end need to be buffered while waiting to be consumed (processed). Definitely, we cannot have an unlimited buffer size at the receiving side. We have two choices. The first choice is to let the
receiving data-link layer drop the frames if its buffer is full. The second choice is to let
the receiving data-link layer send a feedback to the sending data-link layer to ask it to
stop or slow down. Different data-link-layer protocols use different strategies for flow
control. Since flow control also occurs at the transport layer, with a higher degree of
importance, we discuss this issue in Chapter 23 when we talk about the transport layer.

#### Error Control
> id: ch09-9-1-2-error-control | src: book p.241 | kind: concept

At the sending node, a frame in a data-link layer needs to be changed to bits, transformed to electromagnetic signals, and transmitted through the transmission media. At
the receiving node, electromagnetic signals are received, transformed to bits, and put
together to create a frame. Since electromagnetic signals are susceptible to error, a
frame is susceptible to error. The error needs first to be detected. After detection, it
needs to be either corrected at the receiver node or discarded and retransmitted by the
sending node. Since error detection and correction is an issue in every layer (node-to-node or host-to-host), we have dedicated all of Chapter 10 to this issue.

#### Congestion Control
> id: ch09-9-1-2-congestion-control | src: book p.241 | kind: concept

Although a link may be congested with frames, which may result in frame loss, most
data-link-layer protocols do not directly use a congestion control to alleviate congestion,
although some wide-area networks do. In general, congestion control is considered an
issue in the network layer or the transport layer because of its end-to-end nature. We will
discuss congestion control in the network layer and the transport layer in later chapters.

### 9.1.3 Two Categories of Links
> id: ch09-9-1-3 | src: book 9.1.3; p.241 | kind: concept

Although two nodes are physically connected by a transmission medium such as cable
or air, we need to remember that the data-link layer controls how the medium is used.
We can have a data-link layer that uses the whole capacity of the medium; we can also
have a data-link layer that uses only part of the capacity of the link. In other words, we
can have a point-to-point link or a broadcast link. In a point-to-point link, the link is
dedicated to the two devices; in a broadcast link, the link is shared between several
pairs of devices. For example, when two friends use the traditional home phones to
chat, they are using a point-to-point link; when the same two friends use their cellular
phones, they are using a broadcast link (the air is shared among many cell phone users).

### 9.1.4 Two Sublayers
> id: ch09-9-1-4 | src: book 9.1.4; p.242 | kind: concept

To better understand the functionality of and the services provided by the link layer, we
can divide the data-link layer into two sublayers: data link control (DLC) and media
access control (MAC). This is not unusual because, as we will see in later chapters, LAN
protocols actually use the same strategy. The data link control sublayer deals with all
issues common to both point-to-point and broadcast links; the media access control sublayer deals only with issues specific to broadcast links. In other words, we separate these
two types of links at the data-link layer, as shown in Figure 9.4.

> **[ASSET ch09_ill_004]** Figure 9.4: Dividing the data-link layer into two sublayers
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_004.png
> - src: book Figure 9.4; p.242
> - shows: Figure 9.4: Dividing the data-link layer into two sublayers. The data-link layer is split into data-link control and media-access control sublayers for a broadcast link, while a point-to-point link uses data-link control without shared-medium access.
> - structure: The data-link layer is split into data-link control and media-access control sublayers for a broadcast link, while a point-to-point link uses data-link control without shared-medium access.
> - text_in_image: Data-link layer; Data-link layer; Data link control sublayer; Data link control sublayer; Media access control sublayer; a. Data-link layer of a broadcast link; b. Data-link layer of a point-to-point link
> - use_when: Teach ch09-9-1-4, interpret Figure 9.4, trace address changes, or solve a linked practice question.
> - confidence: high

We discuss the DLC and MAC sublayers later, each in a separate chapter. In addition, we discuss the issue of error detection and correction, a duty of the data-link and
other layers, also in a separate chapter.

## 9.2 LINK-LAYER ADDRESSING
> id: ch09-9-2 | src: book 9.2; p.242 | kind: concept

The next issue we need to discuss about the data-link layer is the link-layer addresses.
In Chapter 18, we will discuss IP addresses as the identifiers at the network layer that
define the exact points in the Internet where the source and destination hosts are connected. However, in a connectionless internetwork such as the Internet we cannot make
a datagram reach its destination using only IP addresses. The reason is that each datagram in the Internet, from the same source host to the same destination host, may take a
different path. The source and destination IP addresses define the two ends but cannot
define which links the datagram should pass through.
We need to remember that the IP addresses in a datagram should not be changed. If
the destination IP address in a datagram changes, the packet never reaches its
destination; if the source IP address in a datagram changes, the destination host or a
router can never communicate with the source if a response needs to be sent back or an
error needs to be reported back to the source (see ICMP in Chapter 19).
The above discussion shows that we need another addressing mechanism in a connectionless internetwork: the link-layer addresses of the two nodes. A link-layer
address is sometimes called a link address, sometimes a physical address, and sometimes a MAC address. We use these terms interchangeably in this book.
Since a link is controlled at the data-link layer, the addresses need to belong to the
data-link layer. When a datagram passes from the network layer to the data-link layer,
the datagram will be encapsulated in a frame and two data-link addresses are added to
the frame header. These two addresses are changed every time the frame moves from
one link to another. Figure 9.5 demonstrates the concept in a small internet.

> **[ASSET ch09_ill_005]** Figure 9.5: IP addresses and link-layer addresses in a small internet
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_005.png
> - src: book Figure 9.5; p.243
> - shows: Figure 9.5: IP addresses and link-layer addresses in a small internet. Alice sends through routers R1 and R2 to Bob. IP source and destination remain N1 and N8, while each frame receives the local source and destination link addresses for its link.
> - structure: Alice sends through routers R1 and R2 to Bob. IP source and destination remain N1 and N8, while each frame receives the local source and destination link addresses for its link.
> - text_in_image: To another; link; N3 L3; Frame; Alice; N8; L2; L1; N1; Data; N2 L2; N4 L4; R1; N1 L1; Link 1; Data; Order of addresses; N: IP address; IP addresses: source-destination; Frame; N8; Legend; L: Link-layer address; Link-layer address: destination-source; N1; L4; Link 3; L5; N8 L8; R2; N7 L7; N5 L5; Link 2; N8; L8; L7; N1; Data; Bob; Frame; N6 L6; To another; network
> - use_when: Teach ch09-9-2, interpret Figure 9.5, trace address changes, or solve a linked practice question.
> - confidence: high

In the internet in Figure 9.5, we have three links and two routers. We also have
shown only two hosts: Alice (source) and Bob (destination). For each host, we have
shown two addresses, the IP addresses (N) and the link-layer addresses (L). Note
that a router has as many pairs of addresses as the number of links the router is connected to. We have shown three frames, one in each link. Each frame carries the
same datagram with the same source and destination addresses (N1 and N8), but the
link-layer addresses of the frame change from link to link. In link 1, the link-layer
addresses are $L_{1}$ and $L_{2}$. In link 2, they are $L_{4}$ and $L_{5}$. In link 3, they are $L_{7}$ and $L_{8}$.
Note that the IP addresses and the link-layer addresses are not in the same order. For
IP addresses, the source address comes before the destination address; for link-layer
addresses, the destination address comes before the source. The datagrams and
frames are designed in this way, and we follow the design. We may raise several
questions:

- If the IP address of a router does not appear in any datagram sent from a source to a
destination, why do we need to assign IP addresses to routers? The answer is that in
some protocols a router may act as a sender or receiver of a datagram. For example,
in routing protocols we will discuss in Chapters 20 and 21, a router is a sender or a
receiver of a message. The communications in these protocols are between routers.

- Why do we need more than one IP address in a router, one for each interface? The
answer is that an interface is a connection of a router to a link. We will see that an
IP address defines a point in the Internet at which a device is connected. A router
with n interfaces is connected to the Internet at n points. This is the situation of a
house at the corner of a street with two gates; each gate has the address related to
the corresponding street.

- How are the source and destination IP addresses in a packet determined? The
answer is that the host should know its own IP address, which becomes the source
IP address in the packet. As we will discuss in Chapter 26, the application layer
uses the services of DNS to find the destination address of the packet and passes it
to the network layer to be inserted in the packet.

- How are the source and destination link-layer addresses determined for each link?
Again, each hop (router or host) should know its own link-layer address, as we discuss later in the chapter. The destination link-layer address is determined by using
the Address Resolution Protocol, which we discuss shortly.

- What is the size of link-layer addresses? The answer is that it depends on the protocol
used by the link. Although we have only one IP protocol for the whole Internet, we
may be using different data-link protocols in different links. This means that we can
define the size of the address when we discuss different link-layer protocols.

### 9.2.1 Three Types of addresses
> id: ch09-9-2-1 | src: book 9.2.1; p.244 | kind: concept

Some link-layer protocols define three types of addresses: unicast, multicast, and
broadcast.

#### Unicast Address
> id: ch09-9-2-1-unicast-address | src: book p.244 | kind: concept

Each host or each interface of a router is assigned a unicast address. Unicasting means
one-to-one communication. A frame with a unicast address destination is destined only
for one entity in the link.

##### Example 9.1
> id: ch09-example-9-1 | src: book Example 9.1 | kind: worked_example
As we will see in Chapter 13, the unicast link-layer addresses in the most common LAN, Ethernet, are 48 bits (six bytes) that are presented as 12 hexadecimal digits separated by colons; for
example, the following is a link-layer address of a computer.

A3:34:45:11:92:F1

#### Multicast Address
> id: ch09-9-2-1-multicast-address | src: book p.244 | kind: concept

Some link-layer protocols define multicast addresses. Multicasting means one-to-many
communication. However, the jurisdiction is  local (inside the link).
##### Example 9.2
> id: ch09-example-9-2 | src: book Example 9.2 | kind: worked_example
As we will see in Chapter 13, the multicast link-layer addresses in the most common LAN,
Ethernet, are 48 bits (six bytes) that are presented as 12 hexadecimal digits separated by colons.
The second digit, however, needs to be an even number in hexadecimal. The following shows a
multicast address:

A2:34:45:11:92:F1

#### Broadcast Address
> id: ch09-9-2-1-broadcast-address | src: book p.245 | kind: concept

Some link-layer protocols define a broadcast address. Broadcasting means one-to-all
communication. A frame with a destination broadcast address is sent to all entities in
the link.

##### Example 9.3
> id: ch09-example-9-3 | src: book Example 9.3 | kind: worked_example
As we will see in Chapter 13, the broadcast link-layer addresses in the most common LAN,
Ethernet, are 48 bits, all 1s, that are presented as 12 hexadecimal digits separated by colons. The
following shows a broadcast address:

FF:FF:FF:FF:FF:FF

### 9.2.2 Address Resolution Protocol (ARP)
> id: ch09-9-2-2 | src: book 9.2.2; p.245 | kind: concept

Anytime a node has an IP datagram to send to another node in a link, it has the IP address
of the receiving node. The source host knows the IP address of the default router. Each
router except the last one in the path gets the IP address of the next router by using its forwarding table. The last router knows the IP address of the destination host. However, the
IP address of the next node is not helpful in moving a frame through a link; we need the
link-layer address of the next node. This is the time when the Address Resolution Protocol (ARP) becomes helpful. The ARP protocol is one of the auxiliary protocols defined
in the network layer, as shown in Figure 9.6. It belongs to the network layer, but we discuss it in this chapter because it maps an IP address to a logical-link address. ARP accepts
an IP address from the IP protocol, maps the address to the corresponding link-layer
address, and passes it to the data-link layer.

> **[ASSET ch09_ill_006]** Figure 9.6: Position of ARP in TCP/IP protocol suite
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_006.png
> - src: book Figure 9.6; p.245
> - shows: Figure 9.6: Position of ARP in TCP/IP protocol suite. ARP is positioned beside IP at the network/link boundary, mapping an IP address to a link-layer address while ICMP and IGMP remain above IP.
> - structure: ARP is positioned beside IP at the network/link boundary, mapping an IP address to a link-layer address while ICMP and IGMP remain above IP.
> - text_in_image: IP; ICMP; IGMP; address; Network; IP; layer; ARP; Link-layer; address
> - use_when: Teach ch09-9-2-2, interpret Figure 9.6, trace address changes, or solve a linked practice question.
> - confidence: high

Anytime a host or a router needs to find the link-layer address of another host or router
in its network, it sends an ARP request packet. The packet includes the link-layer and IP
addresses of the sender and the IP address of the receiver. Because the sender does not
know the link-layer address of the receiver, the query is broadcast over the link using the
link-layer broadcast address, which we discuss for each protocol later (see Figure 9.7).

> **[ASSET ch09_ill_007]** Figure 9.7: ARP operation
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_007.png
> - src: book Figure 9.7; p.246
> - shows: Figure 9.7: ARP operation. An ARP request is broadcast on a LAN asking for the hardware address that matches N2; system B returns a unicast reply containing L2.
> - structure: An ARP request is broadcast on a LAN asking for the hardware address that matches N2; system B returns a unicast reply containing L2.
> - text_in_image: LAN; System A; System B; N1 L1; N2 L2; Request; N3 L3; N4 L4; Request:; Looking for link-layer; address of a node with; IP address N2; a. ARP request is broadcast; LAN; System A; System B; N2 L2; N1 L1; Reply; N4 L4; N3 L3; Reply:; I am the node and my; link-layer address is; L2; b. ARP reply is unicast
> - use_when: Teach ch09-9-2-2, interpret Figure 9.7, trace address changes, or solve a linked practice question.
> - confidence: high

Every host or router on the network receives and processes the ARP request
packet, but only the intended recipient recognizes its IP address and sends back an ARP
response packet. The response packet contains the recipient’s IP and link-layer
addresses. The packet is unicast directly to the node that sent the request packet.
In Figure 9.7a, the system on the left (A) has a packet that needs to be delivered
to another system (B) with IP address N2. System A needs to pass the packet to its
data-link layer for the actual delivery, but it does not know the physical address of
the recipient. It uses the services of ARP by asking the ARP protocol to send a
broadcast ARP request packet to ask for the physical address of a system with an IP
address of N2.
This packet is received by every system on the physical network, but only system B
will answer it, as shown in Figure 9.7b. System B sends an ARP reply packet that
includes its physical address. Now system A can send all the packets it has for this destination using the physical address it received.

#### Caching
> id: ch09-9-2-2-caching | src: book p.247 | kind: concept

A question that is often asked is this: If system A can broadcast a frame to find the link-layer address of system B, why can’t system A send the datagram for system B using a
broadcast frame? In other words, instead of sending one broadcast frame (ARP
request), one unicast frame (ARP response), and another unicast frame (for sending the
datagram), system A can encapsulate the datagram and send it to the network. System B
receives it and keep it; other systems discard it.
To answer the question, we need to think about the efficiency. It is probable that
system A has more than one datagram to send to system B in a short period of time. For
example, if system B is supposed to receive a long e-mail or a long file, the data do not
fit in one datagram.
Let us assume that there are 20 systems connected to the network (link): system A,
system B, and 18 other systems. We also assume that system A has 10 datagrams to
send to system B in one second.
a. Without using ARP, system A needs to send 10 broadcast frames. Each of the
18 other systems need to receive the frames, decapsulate the frames, remove
the datagram and pass it to their network-layer to find out the datagrams do
not belong to them.This means processing and discarding 180 broadcast
frames.
b. Using ARP, system A needs to send only one broadcast frame. Each of the 18
other systems need to receive the frames, decapsulate the frames, remove the
ARP message and pass the message to their ARP protocol to find that the frame
must be discarded. This means processing and discarding only 18 (instead of
180) broadcast frames. After system B responds with its own data-link address,
system A can store the link-layer address in its cache memory. The rest of the
nine frames are only unicast. Since processing broadcast frames is expensive
(time consuming), the first method is preferable.

#### Packet Format
> id: ch09-9-2-2-packet-format | src: book p.247 | kind: concept

Figure 9.8 shows the format of an ARP packet. The names of the fields are selfexplanatory. The hardware type field defines the type of the link-layer protocol; Ethernet
is given the type 1. The protocol type field defines the network-layer protocol: IPv4 protocol is (0800)16. The source hardware and source protocol addresses are variable-length
fields defining the link-layer and network-layer addresses of the sender. The destination
hardware address and destination protocol address fields define the receiver link-layer
and network-layer addresses. An ARP packet is encapsulated directly into a data-link
frame. The frame needs to have a field to show that the payload belongs to the ARP and
not to the network-layer datagram.

##### Example 9.4
> id: ch09-example-9-4 | src: book Example 9.4 | kind: worked_example
A host with IP address N1 and MAC address L1 has a packet to send to another host with IP address
N2 and physical address L2 (which is unknown to the first host). The two hosts are on the same network. Figure 9.9 shows the ARP request and response messages.

> **[ASSET ch09_ill_008]** Figure 9.8: ARP packet
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_008.png
> - src: book Figure 9.8; p.248
> - shows: Figure 9.8: ARP packet. The ARP packet layout shows hardware/protocol types and lengths, request-or-reply operation, and variable-length sender and destination protocol and hardware address fields.
> - structure: The ARP packet layout shows hardware/protocol types and lengths, request-or-reply operation, and variable-length sender and destination protocol and hardware address fields.
> - text_in_image: 0; 8; 16; 31; Hardware: LAN or WAN protocol; Hardware Type; Protocol Type; Protocol: Network-layer protocol; Hardware; Protocol; Operation; length; length; Request:1, Reply:2; Source hardware address; Source protocol address; Destination hardware  address; (Empty in request); Destination protocol address
> - use_when: Teach ch09-9-2-2-packet-format, interpret Figure 9.8, trace address changes, or solve a linked practice question.
> - confidence: high

> **[ASSET ch09_ill_009]** Figure 9.9: Example 9.4
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_009.png
> - src: book Figure 9.9; p.248
> - shows: Figure 9.9: Example 9.4. Example 9.4 traces a broadcast ARP request from A and a unicast ARP reply from B, showing both ARP fields and enclosing frame addresses.
> - structure: Example 9.4 traces a broadcast ARP request from A and a unicast ARP reply from B, showing both ARP fields and enclosing frame addresses.
> - text_in_image: System A; System B; N2; N1; L1; L2 (Not known by A); 0x0001; 0x0800; 0x06; 0x04; 0x0001; ARP request; L1; N1; All 0s; N2; Multicast frame; From A to B; A; 1; Data; M; Destination; Source.; 0x0001; 0x0800; B: Broadcast address; 0x06; 0x04; 0x0002; L2; ARP reply; N2; L1; N2; Unicast frame; From B to A; A; B; 2; Data; Destination; Source
> - use_when: Teach ch09-example-9-4, interpret Figure 9.9, trace address changes, or solve a linked practice question.
> - confidence: high

### 9.2.3 An Example of Communication
> id: ch09-9-2-3 | src: book 9.2.3; p.248 | kind: concept

To show how communication is done at the data-link layer and how link-layer addresses
are found, let us go through a simple example. Assume Alice needs to send a datagram
to Bob, who is three nodes away in the Internet. How Alice finds the network-layer
address of Bob is what we discover in Chapter 26 when we discuss DNS. For the
moment, assume that Alice knows the network-layer (IP) address of Bob. In other
words, Alice’s host is given the data to be sent, the IP address of Bob, and the
IP address of Alice’s host (each host needs to know its IP address). Figure 9.10 shows
the part of the internet for our example.

> **[ASSET ch09_ill_010]** Figure 9.10: The internet for our example
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_010.png
> - src: book Figure 9.10; p.249
> - shows: Figure 9.10: The internet for our example. The chapter example topology connects Alice through R1, a point-to-point network, and R2 to Bob, with external links at both ends.
> - structure: The chapter example topology connects Alice through R1, a point-to-point network, and R2 to Bob, with external links at both ends.
> - text_in_image: To another; To another; link; link; Alice; Bob; Point-to-point network; R2; R1; Alice’s site; Bob’s site
> - use_when: Teach ch09-9-2-3, interpret Figure 9.10, trace address changes, or solve a linked practice question.
> - confidence: high

#### Activities at Alice’s Site
> id: ch09-9-2-3-activities-at-alice-s-site | src: book p.249 | kind: concept

We will use symbolic addresses to make the figures more readable. Figure 9.11 shows
what happens at Alice’s site.

> **[ASSET ch09_ill_011]** Figure 9.11: Flow of packets at Alice’s computer
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_011.png
> - src: book Figure 9.11; p.249
> - shows: Figure 9.11: Flow of packets at Alice’s computer. Alice combines forwarding-table lookup and ARP to choose R1, builds a datagram with N1-to-N8 addresses, wraps it in an L1-to-L2 frame, and transmits it.
> - structure: Alice combines forwarding-table lookup and ARP to choose R1, builds a datagram with N1-to-N8 addresses, wraps it in an L1-to-L2 frame, and transmits it.
> - text_in_image: Legend; Alice’s site; Bob’s site; N: Network-layer address; L: Link-layer address; NB; N1; N2; N3; N4; NA; LA; LB; L1; L2; L3; L4; R2; R1; Forwarding; Data; NA; NB; table; NB; N1; N1; ARP; ARP; Network layer; (Alice); (R1); L1; L1; L1; NA; Data; NB; Datagram; LA; Data-link layer; Note:; Data-link layer gets its own link-layer; NA; address (LA) here from its interface.; L1 LA; NB; Frame; Data; Physical layer; Signal; Flow of packets at Alice’s computer; To R1
> - use_when: Teach ch09-9-2-3-activities-at-alice-s-site, interpret Figure 9.11, trace address changes, or solve a linked practice question.
> - confidence: high

The network layer knows it’s given $N_{A}$, $N_{B}$, and the packet, but it needs to find the
link-layer address of the next node. The network layer consults its routing table and
tries to find which router is next (the default router in this case) for the destination $N_{B}$.
As we will discuss in Chapter 18, the routing table gives $N_{1}$, but the network layer
needs to find the link-layer address of router R1. It uses its ARP to find the link-layer
address $L_{1}$. The network layer can now pass the datagram with the link-layer address to
the data-link layer.
The data-link layer knows its own link-layer address, $L_{A}$. It creates the frame and
passes it to the physical layer, where the address is converted to signals and sent
through the media.

#### Activities at Router R1
> id: ch09-9-2-3-activities-at-router-r1 | src: book p.250 | kind: concept

Now let us see what happens at Router R1. Router R1, as we know, has only three
lower layers. The packet received needs to go up through these three layers and come
down. Figure 9.12 shows the activities.

> **[ASSET ch09_ill_012]** Figure 9.12: Flow of activities at router R1
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_012.png
> - src: book Figure 9.12; p.250
> - shows: Figure 9.12: Flow of activities at router R1. Router R1 removes Alice’s frame, routes the unchanged N1-to-N8 datagram, obtains the next-hop link address, creates a new frame for R2, and transmits it.
> - structure: Router R1 removes Alice’s frame, routes the unchanged N1-to-N8 datagram, obtains the next-hop link address, creates a new frame for R2, and transmits it.
> - text_in_image: Legend; Bob’s site; Alice’s site; N: Network-layer address; L: Link-layer address; NB; NA; N1; N2; N3; N4; LA; L1; L2; L3; L4; LB; R2; R1; Alice; Forwarding; table; N3; NB; N3; ARP; ARP; Network layer; (R2); (R1); L3; L3; L3; Datagram; NA; NB; Data; NA; NB; Data; L2; Data-link layer; Data-link layer; L1 LA; L3 L2; NA; NB; NA; NB; Data; Data; Frame; Frame; Physical layer; Physical layer; Signal; Signal; from Alice; Flow of packets at Router R1; To R2
> - use_when: Teach ch09-9-2-3-activities-at-router-r1, interpret Figure 9.12, trace address changes, or solve a linked practice question.
> - confidence: high

At arrival, the physical layer of the left link creates the frame and passes it to the
data-link layer. The data-link layer decapsulates the datagram and passes it to the network layer. The network layer examines the network-layer address of the datagram
and finds that the datagram needs to be delivered to the device with IP address $N_{B}$.
The network layer consults its routing table to find out which is the next node (router)
in the path to $N_{B}$. The forwarding table returns $N_{3}$. The IP address of router R2 is in
the same link with R1. The network layer now uses the ARP to find the link-layer
address of this router, which comes up as $L_{3}$. The network layer passes the datagram
and $L_{3}$ to the data-link layer belonging to the link at the right side. The link layer
encapsulates the datagram, adds L3 and L2 (its own link-layer address), and passes the
frame to the physical layer. The physical layer encodes the bits to signals and sends
them through the medium to R2.

#### Activities at Router R2
> id: ch09-9-2-3-activities-at-router-r2 | src: book p.251 | kind: concept

Activities at router R2 are almost the same as in R1, as shown in Figure 9.13.

> **[ASSET ch09_ill_013]** Figure 9.13: Activities at router R2.
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_013.png
> - src: book Figure 9.13; p.251
> - shows: Figure 9.13: Activities at router R2.. Router R2 removes R1’s frame, routes the unchanged datagram toward Bob, resolves Bob’s link address, and creates the final local frame.
> - structure: Router R2 removes R1’s frame, routes the unchanged datagram toward Bob, resolves Bob’s link address, and creates the final local frame.
> - text_in_image: Legend; Bob’s site; Alice’s site; N: Network-layer address; L: Link-layer address; NB; NA; N1; N2; N3; N4; Bob; LA; L1; L2; L3; L4; LB; R2; R1; Alice; Forwarding; table; NB; NB; NB; ARP; ARP; Network layer; (R2); (Bob); LB; LB; Datagram; NA; NB; LB; NA; NB; Data; Data; Data-link layer; Data-link layer; L4; LB; L4; L3 L2; NA; NB; NA; NB; Data; Data; Frame; Frame; Physical layer; Physical layer; Signal; Signal; from R1; Flow of packets at Router R2; To Bob
> - use_when: Teach ch09-9-2-3-activities-at-router-r2, interpret Figure 9.13, trace address changes, or solve a linked practice question.
> - confidence: high

#### Activities at Bob’s Site
> id: ch09-9-2-3-activities-at-bob-s-site | src: book p.251 | kind: concept

Now let us see what happens at Bob’s site. Figure 9.14 shows how the signals at
Bob’s site are changed to a message. At Bob’s site there are no more addresses or
mapping needed. The signal received from the link is changed to a frame. The frame
is passed to the data-link layer, which decapsulates the datagram and passes it to the
network layer. The network layer decapsulates the message and passes it to the
transport layer.

#### Changes in Addresses
> id: ch09-9-2-3-changes-in-addresses | src: book p.251 | kind: concept

This example shows that the source and destination network-layer addresses, NA and
NB, have not been changed during the whole journey. However, all four network-layer
addresses of routers R1 and R2 (N1, N2, N3, and N4) are needed to transfer a datagram
from Alice’s computer to Bob’s computer.

> **[ASSET ch09_ill_014]** Figure 9.14: Activities at Bob’s site
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_014.png
> - src: book Figure 9.14; p.252
> - shows: Figure 9.14: Activities at Bob’s site. Bob removes the final link-layer frame and passes the unchanged N1-to-N8 datagram upward through the network layer.
> - structure: Bob removes the final link-layer frame and passes the unchanged N1-to-N8 datagram upward through the network layer.
> - text_in_image: Legend; Bob’s site; Alice’s site; N: Network-layer address; L: Link-layer address; NB; NA; N1; N2; N3; N4; Bob; LA; L1; L2; L3; L4; LB; R2; R1; Alice; Network layer; Datagram; NA; NB; Data; Data-link layer; LB L4; Frame; NA; NB; Data; Physical layer; Signal; Flow of packets at Bob’s computer
> - use_when: Teach ch09-9-2-3-activities-at-bob-s-site, interpret Figure 9.14, trace address changes, or solve a linked practice question.
> - confidence: high

## 9.3 END-CHAPTER MATERIALS
> id: ch09-9-3 | src: book 9.3; p.252 | kind: concept

### 9.3.1 Recommended Reading
> id: ch09-9-3-1 | src: book 9.3.1; p.252 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets […] refer to the reference list at the end of the text.

#### Books
> id: ch09-9-3-1-books | src: book p.252 | kind: concept

Several books discuss link-layer issues. Among them we recommend [Ham 80], [Zar 02],
[Ror 96], [Tan 03], [GW 04], [For 03], [KMK 04], [Sta 04], [Kes 02], [PD 03], [Kei
02], [Spu 00], [KCK 98], [Sau 98], [Izz 00], [Per 00], and [WV 00].

### 9.3.2 Key Terms
> id: ch09-9-3-2 | src: book 9.3.2; p.252 | kind: concept

- Address Resolution Protocol (ARP)
- data link control (DLC)
- frame
- framing
- links
- media access control (MAC)
- nodes

### 9.3.3 Summary
> id: ch09-9-3-3 | src: book 9.3.3; p.252 | kind: summary

The Internet is made of many hosts, networks, and connecting devices such as routers.
The hosts and connecting devices are referred to as nodes; the networks are referred to
as links. A path in the Internet from a source host to a destination host is a set of nodes
and links through which a packet should travel.
The data-link layer is responsible for the creation and delivery of a frame to
another node, along the link. It is responsible for packetizing (framing), flow control,
error control, and congestion control along the link. Two data-link layers at the two
ends of a link coordinate to deliver a frame from one node to the next.
As with any delivery between a source and destination in which there are many
paths, we need two types of addressing. The end-to-end addressing defines the source
and destination; the link-layer addressing defines the addresses of the nodes that the
packet should pass through. To avoid including the link-layer addresses of all of these
nodes in the frame, the Address Resolution Protocol (ARP) was devised to map an IP
address to its corresponding link-layer address. When a packet is at one node ready to
be sent to the next, the forwarding table finds the IP address of the next node and ARP
find its link-layer address.
