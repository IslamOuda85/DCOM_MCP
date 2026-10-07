---
doc_type: scientific_content
course_id: data_communications
chapter: 8
chapter_id: data_communications_ch08
chapter_title: Switching
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_8/ch8.pdf
  pages: 207-234
assets_dir: assets
asset_counts:
  illustration: 28
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:27:03+00:00'
status: complete
---
# Chapter 8: Switching

## Chapter Objectives
> id: ch08-0 | src: book p.207 | kind: objectives

Switching is a topic that can be discussed at several layers. We have switching at the
physical layer, at the data-link layer, at the network layer, and even logically at the
application layer (message switching). We have decided to discuss the general idea
behind switching in this chapter, the last chapter related to the physical layer. We particularly discuss circuit-switching, which occurs at the physical layer. We introduce the
idea of packet-switching, which occurs at the data-link and network layers, but we
postpone the details of these topics until the appropriate chapters. Finally, we talk about
the physical structures of the switches and routers.
This chapter is divided into four sections:

- The first section introduces switching. It mentions three methods of switching: circuit switching, packet switching, and message switching. The section then defines
the switching methods that can occur in some layers of the Internet model.

- The second section discusses circuit-switched networks. It first defines three
phases in these types of networks. It then describes the efficiency of these networks. The section also discusses the delay in circuit-switched networks.

- The third section briefly discusses packet-switched networks. It first describes
datagram networks, listing their characteristics and advantages. The section then
describes virtual circuit networks, explaining their features and operations. We will
discuss packet-switched networks in more detail in Chapter 18.

- The last section discusses the structure of a switch. It first describes the structure of
a circuit switch. It then explains the structure of a packet switch.

## 8.1 INTRODUCTION
> id: ch08-8-1 | src: book 8.1; p.208 | kind: concept

A network is a set of connected devices. Whenever we have multiple devices, we have
the problem of how to connect them to make one-to-one communication possible. One
solution is to make a point-to-point connection between each pair of devices (a mesh
topology) or between a central device and every other device (a star topology). These
methods, however, are impractical and wasteful when applied to very large networks.
The number and length of the links require too much infrastructure to be cost-efficient,
and the majority of those links would be idle most of the time. Other topologies
employing multipoint connections, such as a bus, are ruled out because the distances
between devices and the total number of devices increase beyond the capacities of the
media and equipment.
A better solution is switching. A switched network consists of a series of interlinked
nodes, called switches. Switches are devices capable of creating temporary connections
between two or more devices linked to the switch. In a switched network, some of these
nodes are connected to the end systems (computers or telephones, for example). Others
are used only for routing. Figure 8.1 shows a switched network.

> **[ASSET ch08_ill_001]** Figure 8.1: Switched network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_001.png
> - src: book Figure 8.1; p.208
> - shows: Figure 8.1: Switched network. A mesh of intermediate switches connects end systems A through J; several alternative paths illustrate why a switched network avoids direct links between every pair.
> - structure: A mesh of intermediate switches connects end systems A through J; several alternative paths illustrate why a switched network avoids direct links between every pair.
> - text_in_image: B; C; D; E; A; F; II; III; I; IV; V; J; I; H; G
> - use_when: Teach ch08-8-1, interpret Figure 8.1, trace a switching path, or solve a linked practice question.
> - confidence: high

The end systems (communicating devices) are labeled A, B, C, D, and so on, and the
switches are labeled I, II, III, IV, and V. Each switch is connected to multiple links.

### 8.1.1 Three Methods of Switching
> id: ch08-8-1-1 | src: book 8.1.1; p.208 | kind: concept

Traditionally, three methods of switching have been discussed: circuit switching,
packet switching, and message switching. The first two are commonly used today.
The third has been phased out in general communications but still has networking
applications. Packet switching can further be divided into two subcategories—virtual-circuit approach and datagram approach—as shown in Figure 8.2. In this chapter, we
discuss only circuit switching and packet switching; message switching is more conceptual than practical.

> **[ASSET ch08_ill_002]** Figure 8.2: Taxonomy of switched networks
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_002.png
> - src: book Figure 8.2; p.209
> - shows: Figure 8.2: Taxonomy of switched networks. A taxonomy divides switching into circuit, packet, and message switching; packet switching divides into virtual-circuit and datagram approaches.
> - structure: A taxonomy divides switching into circuit, packet, and message switching; packet switching divides into virtual-circuit and datagram approaches.
> - text_in_image: Switching; Circuit switching; Packet switching; Message switching; Virtual-circuit; Datagram; approach; approach
> - use_when: Teach ch08-8-1-1, interpret Figure 8.2, trace a switching path, or solve a linked practice question.
> - confidence: high

### 8.1.2 Switching and TCP/IP Layers
> id: ch08-8-1-2 | src: book 8.1.2; p.209 | kind: concept

Switching can happen at several layers of the TCP/IP protocol suite.

#### Switching at Physical Layer
> id: ch08-8-1-2-switching-at-physical-layer | src: book p.209 | kind: concept

At the physical layer, we can have only circuit switching. There are no packets
exchanged at the physical layer. The switches at the physical layer allow signals to
travel in one path or another.

#### Switching at Data-Link Layer
> id: ch08-8-1-2-switching-at-data-link-layer | src: book p.209 | kind: concept

At the data-link layer, we can have packet switching. However, the term packet in this
case means frames or cells. Packet switching at the data-link layer is normally done
using a virtual-circuit approach.

#### Switching at Network Layer
> id: ch08-8-1-2-switching-at-network-layer | src: book p.209 | kind: concept

At the network layer, we can have packet switching. In this case, either a virtual-circuit
approach or a datagram approach can be used. Currently the Internet uses a datagram
approach, as we see in Chapter 18, but the tendency is to move to a virtual-circuit
approach.

#### Switching at Application Layer
> id: ch08-8-1-2-switching-at-application-layer | src: book p.209 | kind: concept

At the application layer, we can have only message switching. The communication at
the application layer occurs by exchanging messages. Conceptually, we can say that
communication using e-mail is a kind of message-switched communication, but we do
not see any network that actually can be called a message-switched network.

## 8.2 CIRCUIT-SWITCHED NETWORKS
> id: ch08-8-2 | src: book 8.2; p.209 | kind: concept

A circuit-switched network consists of a set of switches connected by physical links.
A connection between two stations is a dedicated path made of one or more links. However, each connection uses only one dedicated channel on each link. Each link is normally divided into n channels by using FDM or TDM, as discussed in Chapter 6.
A circuit-switched network is made of a set of switches connected
by physical links, in which each link is divided into n channels.

Figure 8.3 shows a trivial circuit-switched network with four switches and four
links. Each link is divided into n (n is 3 in the figure) channels by using FDM or TDM.

> **[ASSET ch08_ill_003]** Figure 8.3: A trivial circuit-switched network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_003.png
> - src: book Figure 8.3; p.210
> - shows: Figure 8.3: A trivial circuit-switched network. A circuit-switched network establishes one continuous path through four switches from end system A to M, with one of n link channels reserved on each hop.
> - structure: A circuit-switched network establishes one continuous path through four switches from end system A to M, with one of n link channels reserved on each hop.
> - text_in_image: I; II; One link, n channels; A; Path; M; IV; III
> - use_when: Teach ch08-8-2, interpret Figure 8.3, trace a switching path, or solve a linked practice question.
> - confidence: high

We have explicitly shown the multiplexing symbols to emphasize the division of
the link into channels even though multiplexing can be implicitly included in the switch
fabric.
The end systems, such as computers or telephones, are directly connected to a
switch. We have shown only two end systems for simplicity. When end system A needs
to communicate with end system M, system A needs to request a connection to M that
must be accepted by all switches as well as by M itself. This is called the setup phase;
a circuit (channel) is reserved on each link, and the combination of circuits or channels
defines the dedicated path. After the dedicated path made of connected circuits (channels)
is established, the data-transfer phase can take place. After all data have been transferred, the circuits are torn down.
We need to emphasize several points here:

- Circuit switching takes place at the physical layer.

- Before starting communication, the stations must make a reservation for the resources
to be used during the communication. These resources, such as channels (bandwidth
in FDM and time slots in TDM), switch buffers, switch processing time, and switch
input/output ports, must remain dedicated during the entire duration of data transfer
until the teardown phase.

- Data transferred between the two stations are not packetized (physical layer transfer
of the signal). The data are a continuous flow sent by the source station and received
by the destination station, although there may be periods of silence.
- There is no addressing involved during data transfer. The switches route the data
based on their occupied band (FDM) or time slot (TDM). Of course, there is end-to-end addressing used during the setup phase, as we will see shortly.

In circuit switching, the resources need to be reserved during the setup phase;
the resources remain dedicated for the entire duration of data transfer
until the teardown phase.

### Example 8.1
> id: ch08-example-8-1 | src: book Example 8.1 | kind: worked_example
As a trivial example, let us use a circuit-switched network to connect eight telephones in a small
area. Communication is through 4-kHz voice channels. We assume that each link uses FDM to
connect a maximum of two voice channels. The bandwidth of each link is then 8 kHz. Figure 8.4
shows the situation. Telephone 1 is connected to telephone 7; 2 to 5; 3 to 8; and 4 to 6. Of course
the situation may change when new connections are made. The switch controls the connections.

> **[ASSET ch08_ill_004]** Figure 8.4: Circuit-switched network used in Example 8.1
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_004.png
> - src: book Figure 8.4; p.211
> - shows: Figure 8.4: Circuit-switched network used in Example 8.1. Eight telephones connect through a circuit switch; paired calls occupy 4 kHz channels and shared links carry two channels over 8 kHz bands.
> - structure: Eight telephones connect through a circuit switch; paired calls occupy 4 kHz channels and shared links carry two channels over 8 kHz bands.
> - text_in_image: Circuit-switched network; 5; 1; 6; 0; 4; kHz; kHz; 2; 3; 0; 8; 7; kHz; kHz; 4; 0; 4; kHz; kHz; 8; 0; 4; kHz; kHz
> - use_when: Teach ch08-example-8-1, interpret Figure 8.4, trace a switching path, or solve a linked practice question.
> - confidence: high

### Example 8.2
> id: ch08-example-8-2 | src: book Example 8.2 | kind: worked_example
As another example, consider a circuit-switched network that connects computers in two remote
offices of a private company. The offices are connected using a T-1 line leased from a communication service provider. There are two 4 × 8 (4 inputs and 8 outputs) switches in this network. For
each switch, four output ports are folded into the input ports to allow communication between
computers in the same office. Four other output ports allow communication between the two
offices. Figure 8.5 shows the situation.

### 8.2.1 Three Phases
> id: ch08-8-2-1 | src: book 8.2.1; p.211 | kind: concept

The actual communication in a circuit-switched network requires three phases: connection setup, data transfer, and connection teardown.

#### Setup Phase
> id: ch08-8-2-1-setup-phase | src: book p.211 | kind: concept

Before the two parties (or multiple parties in a conference call) can communicate, a
dedicated circuit (combination of channels in links) needs to be established. The end systems are normally connected through dedicated lines to the switches, so connection setup

> **[ASSET ch08_ill_005]** Figure 8.5: Circuit-switched network used in Example 8.2
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_005.png
> - src: book Figure 8.5; p.212
> - shows: Figure 8.5: Circuit-switched network used in Example 8.2. Two office sites use 4-by-8 circuit switches with folded local paths and a 1.544 Mbps T-1 interoffice link.
> - structure: Two office sites use 4-by-8 circuit switches with folded local paths and a 1.544 Mbps T-1 interoffice link.
> - text_in_image: Circuit-switched network; 4 × 8; 4 × 8; switch; switch; T-1 line with; 1.544 Mbps
> - use_when: Teach ch08-example-8-2, interpret Figure 8.5, trace a switching path, or solve a linked practice question.
> - confidence: high

means creating dedicated channels between the switches. For example, in Figure 8.3,
when system A needs to connect to system M, it sends a setup request that includes the
address of system M, to switch I. Switch I finds a channel between itself and switch IV
that can be dedicated for this purpose. Switch I then sends the request to switch IV,
which finds a dedicated channel between itself and switch III. Switch III informs system M of system A’s intention at this time.
In the next step to making a connection, an acknowledgment from system M needs
to be sent in the opposite direction to system A. Only after system A receives this
acknowledgment is the connection established.
Note that end-to-end addressing is required for creating a connection between the
two end systems. These can be, for example, the addresses of the computers assigned
by the administrator in a TDM network, or telephone numbers in an FDM network.

#### Data-Transfer Phase
> id: ch08-8-2-1-data-transfer-phase | src: book p.212 | kind: concept

After the establishment of the dedicated circuit (channels), the two parties can transfer data.

#### Teardown Phase
> id: ch08-8-2-1-teardown-phase | src: book p.212 | kind: concept

When one of the parties needs to disconnect, a signal is sent to each switch to release
the resources.

### 8.2.2 Efficiency
> id: ch08-8-2-2 | src: book 8.2.2; p.212 | kind: concept

It can be argued that circuit-switched networks are not as efficient as the other two
types of networks because resources are allocated during the entire duration of the connection. These resources are unavailable to other connections. In a telephone network,
people normally terminate the communication when they have finished their conversation.
However, in computer networks, a computer can be connected to another computer
even if there is no activity for a long time. In this case, allowing resources to be dedicated
means that other connections are deprived.

### 8.2.3 Delay
> id: ch08-8-2-3 | src: book 8.2.3; p.213 | kind: concept

Although a circuit-switched network normally has low efficiency, the delay in this type
of network is minimal. During data transfer the data are not delayed at each switch; the
resources are allocated for the duration of the connection. Figure 8.6 shows the idea of
delay in a circuit-switched network when only two switches are involved.

> **[ASSET ch08_ill_006]** Figure 8.6: Delay in a circuit-switched network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_006.png
> - src: book Figure 8.6; p.213
> - shows: Figure 8.6: Delay in a circuit-switched network. A time-sequence diagram separates connection setup, continuous data transfer, and disconnect phases and shows their contributions to total circuit-switched delay.
> - structure: A time-sequence diagram separates connection setup, continuous data transfer, and disconnect phases and shows their contributions to total circuit-switched delay.
> - text_in_image: A; B; Connect; Total delay; Data transfer; Disconnect; Time; Time; Time; Time
> - use_when: Teach ch08-8-2-3, interpret Figure 8.6, trace a switching path, or solve a linked practice question.
> - confidence: high

As Figure 8.6 shows, there is no waiting time at each switch. The total delay is due
to the time needed to create the connection, transfer data, and disconnect the circuit. The
delay caused by the setup is the sum of four parts: the propagation time of the source
computer request (slope of the first gray box), the request signal transfer time (height of
the first gray box), the propagation time of the acknowledgment from the destination
computer (slope of the second gray box), and the signal transfer time of the acknowledgment (height of the second gray box). The delay due to data transfer is the sum of two
parts: the propagation time (slope of the colored box) and data transfer time (height of
the colored box), which can be very long. The third box shows the time needed to tear
down the circuit. We have shown the case in which the receiver requests disconnection,
which creates the maximum delay.

## 8.3 PACKET SWITCHING
> id: ch08-8-3 | src: book 8.3; p.213 | kind: concept

In data communications, we need to send messages from one end system to another. If
the message is going to pass through a packet-switched network, it needs to be
divided into packets of fixed or variable size. The size of the packet is determined by
the network and the governing protocol.
In packet switching, there is no resource allocation for a packet. This means that
there is no reserved bandwidth on the links, and there is no scheduled processing time
for each packet. Resources are allocated on demand. The allocation is done on a firstcome, first-served basis. When a switch receives a packet, no matter what the source or
destination is, the packet must wait if there are other packets being processed. As with
other systems in our daily life, this lack of reservation may create delay. For example, if
we do not have a reservation at a restaurant, we might have to wait.

In a packet-switched network, there is no resource reservation;
resources are allocated on demand.

We can have two types of packet-switched networks: datagram networks and virtual-circuit networks.

### 8.3.1 Datagram Networks
> id: ch08-8-3-1 | src: book 8.3.1; p.214 | kind: concept

In a datagram network, each packet is treated independently of all others. Even if a
packet is part of a multipacket transmission, the network treats it as though it existed
alone. Packets in this approach are referred to as datagrams.
Datagram switching is normally done at the network layer. We briefly discuss
datagram networks here as a comparison with circuit-switched and virtual-circuitswitched networks. In Chapter 18 of this text, we go into greater detail.
Figure 8.7 shows how the datagram approach is used to deliver four packets from
station A to station X. The switches in a datagram network are traditionally referred to
as routers. That is why we use a different symbol for the switches in the figure.

> **[ASSET ch08_ill_007]** Figure 8.7: A datagram network with four switches (routers)
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_007.png
> - src: book Figure 8.7; p.214
> - shows: Figure 8.7: A datagram network with four switches (routers). Four routers offer multiple paths between A and X; five labeled datagrams take different routes through the datagram network.
> - structure: Four routers offer multiple paths between A and X; five labeled datagrams take different routes through the datagram network.
> - text_in_image: Datagram network; A; 3; 1; 4; 3; 2; 1; 4; 1; 2; 3; 1; 4; X; 2; 3; 4; 1; 2
> - use_when: Teach ch08-8-3-1, interpret Figure 8.7, trace a switching path, or solve a linked practice question.
> - confidence: high

In this example, all four packets (or datagrams) belong to the same message, but
may travel different paths to reach their destination. This is so because the links may be
involved in carrying packets from other sources and do not have the necessary bandwidth
available to carry all the packets from A to X. This approach can cause the datagrams of
a transmission to arrive at their destination out of order with different delays between the
packets. Packets may also be lost or dropped because of a lack of resources. In most
protocols, it is the responsibility of an upper-layer protocol to reorder the datagrams or
ask for lost datagrams before passing them on to the application.
The datagram networks are sometimes referred to as connectionless networks. The
term connectionless here means that the switch (packet switch) does not keep information
about the connection state. There are no setup or teardown phases. Each packet is treated
the same by a switch regardless of its source or destination.

#### Routing Table
> id: ch08-8-3-1-routing-table | src: book p.215 | kind: concept

If there are no setup or teardown phases, how are the packets routed to their destinations
in a datagram network? In this type of network, each switch (or packet switch) has a routing table which is based on the destination address. The routing tables are dynamic and
are updated periodically. The destination addresses and the corresponding forwarding
output ports are recorded in the tables. This is different from the table of a circuit-switched network (discussed later) in which each entry is created when the setup phase
is completed and deleted when the teardown phase is over. Figure 8.8 shows the routing
table for a switch.

> **[ASSET ch08_ill_008]** Figure 8.8: Routing table in a datagram network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_008.png
> - src: book Figure 8.8; p.215
> - shows: Figure 8.8: Routing table in a datagram network. A datagram routing table maps destination addresses to output ports beside a four-port router.
> - structure: A datagram routing table maps destination addresses to output ports beside a four-port router.
> - text_in_image: Output; Destination; port; address; 1232; 1; 4150; 2; …; …; 9130; 3; 1; 4; 3; 2
> - use_when: Teach ch08-8-3-1-routing-table, interpret Figure 8.8, trace a switching path, or solve a linked practice question.
> - confidence: high

A switch in a datagram network uses a routing table that is based on the destination
address.

#### Destination Address
> id: ch08-8-3-1-destination-address | src: book p.215 | kind: concept

Every packet in a datagram network carries a header that contains, among other information, the destination address of the packet. When the switch receives the packet,
this destination address is examined; the routing table is consulted to find the corresponding port through which the packet should be forwarded. This address, unlike the
address in a virtual-circuit network, remains the same during the entire journey of the
packet.

The destination address in the header of a packet in a datagram network
remains the same during the entire journey of the packet.

#### Efficiency
> id: ch08-8-3-1-efficiency | src: book p.215 | kind: concept

The efficiency of a datagram network is better than that of a circuit-switched network; resources are allocated only when there are packets to be transferred. If a
source sends a packet and there is a delay of a few minutes before another packet can
be sent, the resources can be reallocated during these minutes for other packets from
other sources.

#### Delay
> id: ch08-8-3-1-delay | src: book p.216 | kind: concept

There may be greater delay in a datagram network than in a virtual-circuit network.
Although there are no setup and teardown phases, each packet may experience a wait at a
switch before it is forwarded. In addition, since not all packets in a message necessarily
travel through the same switches, the delay is not uniform for the packets of a message.
Figure 8.9 gives an example of delay in a datagram network for one packet.

> **[ASSET ch08_ill_009]** Figure 8.9: Delay in a datagram network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_009.png
> - src: book Figure 8.9; p.216
> - shows: Figure 8.9: Delay in a datagram network. A time-sequence diagram shows one packet crossing two routers with three transmission intervals, three propagation intervals, and two queueing waits.
> - structure: A time-sequence diagram shows one packet crossing two routers with three transmission intervals, three propagation intervals, and two queueing waits.
> - text_in_image: A; B; Transmission; time; Waiting; time; Total delay; Waiting; time; Time; Time; Time; Time
> - use_when: Teach ch08-8-3-1-delay, interpret Figure 8.9, trace a switching path, or solve a linked practice question.
> - confidence: high

The packet travels through two switches. There are three transmission times (3T),
three propagation delays (slopes 3τ of the lines), and two waiting times ($w_{1}$ + $w_{2}$). We
ignore the processing time in each switch. The total delay is

$$D_{\mathrm{total}}=3T+3\tau+w_1+w_2$$

### 8.3.2 Virtual-Circuit Networks
> id: ch08-8-3-2 | src: book 8.3.2; p.216 | kind: concept

A virtual-circuit network is a cross between a circuit-switched network and a datagram
network. It has some characteristics of both.

1. As in a circuit-switched network, there are setup and teardown phases in addition
to the data transfer phase.
2. Resources can be allocated during the setup phase, as in a circuit-switched network,
or on demand, as in a datagram network.
3. As in a datagram network, data are packetized and each packet carries an address in
the header. However, the address in the header has local jurisdiction (it defines what
the next switch should be and the channel on which the packet is being carried), not
end-to-end jurisdiction. The reader may ask how the intermediate switches know
where to send the packet if there is no final destination address carried by a packet.
The answer will be clear when we discuss virtual-circuit identifiers in the next section.
4. As in a circuit-switched network, all packets follow the same path established during
the connection.
5. A virtual-circuit network is normally implemented in the data-link layer, while a
circuit-switched network is implemented in the physical layer and a datagram network in the network layer. But this may change in the future.

Figure 8.10 is an example of a virtual-circuit network. The network has switches that
allow traffic from sources to destinations. A source or destination can be a computer,
packet switch, bridge, or any other device that connects other networks.

> **[ASSET ch08_ill_010]** Figure 8.10: Virtual-circuit network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_010.png
> - src: book Figure 8.10; p.217
> - shows: Figure 8.10: Virtual-circuit network. End systems A through D attach to a mesh of switches in a virtual-circuit network; an established path is selected through the mesh.
> - structure: End systems A through D attach to a mesh of switches in a virtual-circuit network; an established path is selected through the mesh.
> - text_in_image: C; End system; A; B; Switches; End system; End system; End system; D
> - use_when: Teach ch08-8-3-2, interpret Figure 8.10, trace a switching path, or solve a linked practice question.
> - confidence: high

#### Addressing
> id: ch08-8-3-2-addressing | src: book p.217 | kind: concept

In a virtual-circuit network, two types of addressing are involved: global and local
(virtual-circuit identifier).

#### Global Addressing
> id: ch08-8-3-2-global-addressing | src: book p.217 | kind: concept

A source or a destination needs to have a global address—an address that can be unique
in the scope of the network or internationally if the network is part of an international
network. However, we will see that a global address in virtual-circuit networks is used
only to create a virtual-circuit identifier, as discussed next.

#### Virtual-Circuit Identifier
> id: ch08-8-3-2-virtual-circuit-identifier | src: book p.217 | kind: concept

The identifier that is actually used for data transfer is called the virtual-circuit identifier
(VCI) or the label. A VCI, unlike a global address, is a small number that has only
switch scope; it is used by a frame between two switches. When a frame arrives at a
switch, it has a VCI; when it leaves, it has a different VCI. Figure 8.11 shows how the
VCI in a data frame changes from one switch to another. Note that a VCI does not need
to be a large number since each switch can use its own unique set of VCIs.

> **[ASSET ch08_ill_011]** Figure 8.11: Virtual-circuit identifier
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_011.png
> - src: book Figure 8.11; p.217
> - shows: Figure 8.11: Virtual-circuit identifier. A frame crosses a switch with VCI 14 and leaves with VCI 77, demonstrating that a virtual-circuit identifier has link-local scope.
> - structure: A frame crosses a switch with VCI 14 and leaves with VCI 77, demonstrating that a virtual-circuit identifier has link-local scope.
> - text_in_image: VCI; VCI; Data; 14; Data; 77
> - use_when: Teach ch08-8-3-2-virtual-circuit-identifier, interpret Figure 8.11, trace a switching path, or solve a linked practice question.
> - confidence: high

#### Three Phases
> id: ch08-8-3-2-three-phases | src: book p.218 | kind: concept

As in a circuit-switched network, a source and destination need to go through three
phases in a virtual-circuit network: setup, data transfer, and teardown. In the setup
phase, the source and destination use their global addresses to help switches make table
entries for the connection. In the teardown phase, the source and destination inform the
switches to delete the corresponding entry. Data transfer occurs between these two
phases. We first discuss the data-transfer phase, which is more straightforward; we then
talk about the setup and teardown phases.

#### Data-Transfer Phase
> id: ch08-8-3-2-data-transfer-phase | src: book p.218 | kind: concept

To transfer a frame from a source to its destination, all switches need to have a table
entry for this virtual circuit. The table, in its simplest form, has four columns. This
means that the switch holds four pieces of information for each virtual circuit that is
already set up. We show later how the switches make their table entries, but for the
moment we assume that each switch has a table with entries for all active virtual circuits. Figure 8.12 shows such a switch and its corresponding table.

> **[ASSET ch08_ill_012]** Figure 8.12: Switch and tables in a virtual-circuit network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_012.png
> - src: book Figure 8.12; p.218
> - shows: Figure 8.12: Switch and tables in a virtual-circuit network. A four-column switching table maps incoming port and VCI to outgoing port and VCI; example frames show 14 becoming 22 and 77 becoming 41.
> - structure: A four-column switching table maps incoming port and VCI to outgoing port and VCI; example frames show 14 becoming 22 and 77 becoming 41.
> - text_in_image: Incoming; Outgoing; Port; VCI; Port; VCI; 1; 14; 3; 22; 1; 77; 2; 41; Data; 77; Data; 14; Data; 22; 1; 3; 2; Data; 41
> - use_when: Teach ch08-8-3-2-data-transfer-phase, interpret Figure 8.12, trace a switching path, or solve a linked practice question.
> - confidence: high

Figure 8.12 shows a frame arriving at port 1 with a VCI of 14. When the frame
arrives, the switch looks in its table to find port 1 and a VCI of 14. When it is found, the
switch knows to change the VCI to 22 and send out the frame from port 3.
Figure 8.13 shows how a frame from source A reaches destination B and how its
VCI changes during the trip. Each switch changes the VCI and routes the frame.
The data-transfer phase is active until the source sends all its frames to the destination. The procedure at the switch is the same for each frame of a message. The process
creates a virtual circuit, not a real circuit, between the source and destination.

#### Setup Phase
> id: ch08-8-3-2-setup-phase | src: book p.218 | kind: concept

In the setup phase, a switch creates an entry for a virtual circuit. For example, suppose
source A needs to create a virtual circuit to B. Two steps are required: the setup request
and the acknowledgment.

> **[ASSET ch08_ill_013]** Figure 8.13: Source-to-destination data transfer in a virtual-circuit network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_013.png
> - src: book Figure 8.13; p.219
> - shows: Figure 8.13: Source-to-destination data transfer in a virtual-circuit network. Three switch tables trace a frame from A to B as its VCI changes from 14 to 66 to 22 to 77 across a WAN path.
> - structure: Three switch tables trace a frame from A to B as its VCI changes from 14 to 66 to 22 to 77 across a WAN path.
> - text_in_image: Incoming; Outgoing; Incoming; Outgoing; Port; VCI; Port; VCI; Port; VCI; Port; VCI; 1; 14; 3; 66; 2; 22; 3; 77; •••; •••; •••; •••; •••; •••; •••; •••; Data; 14; Data; 77; 2; 1; 1; 3; 3; B; 2; 22; A; 4; 4; Data; Data; 66; 1; 2; WAN; Incoming; Outgoing; Port; VCI; Port; VCI; 1; 66; 2; 22; •••; •••; •••; •••
> - use_when: Teach ch08-8-3-2-data-transfer-phase, interpret Figure 8.13, trace a switching path, or solve a linked practice question.
> - confidence: high

#### Setup Request
> id: ch08-8-3-2-setup-request | src: book p.219 | kind: concept

A setup request frame is sent from the source to the destination. Figure 8.14 shows
the process.

> **[ASSET ch08_ill_014]** Figure 8.14: Setup request in a virtual-circuit network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_014.png
> - src: book Figure 8.14; p.219
> - shows: Figure 8.14: Setup request in a virtual-circuit network. A setup request travels from A toward B; each switch allocates an outgoing VCI and creates its forward table entry.
> - structure: A setup request travels from A toward B; each switch allocates an outgoing VCI and creates its forward table entry.
> - text_in_image: Incoming; Outgoing; Incoming; Outgoing; Port; VCI; Port; VCI; Port; VCI; Port; VCI; 2; 22; 3; 1; 14; 3; VCI = 77; 3; 1; B; 3; A; 2; e; b; a; d; c; Switch 3; Switch 1; 1; 2; Switch 2; Incoming; Outgoing; Port; VCI; Port; VCI; 1; 66; 2
> - use_when: Teach ch08-8-3-2-setup-request, interpret Figure 8.14, trace a switching path, or solve a linked practice question.
> - confidence: high

a. Source A sends a setup frame to switch 1.
b. Switch 1 receives the setup request frame. It knows that a frame going from A to B
goes out through port 3. How the switch has obtained this information is a point
covered in future chapters. The switch, in the setup phase, acts as a packet switch;
it has a routing table which is different from the switching table. For the moment,
assume that it knows the output port. The switch creates an entry in its table for
this virtual circuit, but it is only able to fill three of the four columns. The switch
assigns the incoming port (1) and chooses an available incoming VCI (14) and the
outgoing port (3). It does not yet know the outgoing VCI, which will be found during the acknowledgment step. The switch then forwards the frame through port 3
to switch 2.
c. Switch 2 receives the setup request frame. The same events happen here as at
switch 1; three columns of the table are completed: in this case, incoming port (1),
incoming VCI (66), and outgoing port (2).
d. Switch 3 receives the setup request frame. Again, three columns are completed:
incoming port (2), incoming VCI (22), and outgoing port (3).
e. Destination B receives the setup frame, and if it is ready to receive frames from A,
it assigns a VCI to the incoming frames that come from A, in this case 77. This
VCI lets the destination know that the frames come from A, and not other sources.

#### Acknowledgment
> id: ch08-8-3-2-acknowledgment | src: book p.220 | kind: concept

A special frame, called the acknowledgment frame, completes the entries in the switching tables. Figure 8.15 shows the process.

> **[ASSET ch08_ill_015]** Figure 8.15: Setup acknowledgment in a virtual-circuit network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_015.png
> - src: book Figure 8.15; p.220
> - shows: Figure 8.15: Setup acknowledgment in a virtual-circuit network. The setup acknowledgment returns from B to A; reverse information completes the table entries needed for the virtual circuit.
> - structure: The setup acknowledgment returns from B to A; reverse information completes the table entries needed for the virtual circuit.
> - text_in_image: Incoming; Outgoing; Incoming; Outgoing; Port; VCI; Port; VCI; Port; VCI; Port; VCI; 1; 14; 3; 66; 2; 22; 3; 77; VCI = 77; VCI = 14; 1; 3; B; 3; A; 14; 77; 2; e; a; b; d; c; Switch 1; Switch 3; 22; 66; 1; 2; Switch 2; Incoming; Outgoing; Port; VCI; Port; VCI; 1; 66; 2; 22
> - use_when: Teach ch08-8-3-2-acknowledgment, interpret Figure 8.15, trace a switching path, or solve a linked practice question.
> - confidence: high

a. The destination sends an acknowledgment to switch 3. The acknowledgment carries
the global source and destination addresses so the switch knows which entry in the
table is to be completed. The frame also carries VCI 77, chosen by the destination as
the incoming VCI for frames from A. Switch 3 uses this VCI to complete the outgoing VCI column for this entry. Note that 77 is the incoming VCI for destination B,
but the outgoing VCI for switch 3.
b. Switch 3 sends an acknowledgment to switch 2 that contains its incoming VCI in the
table, chosen in the previous step. Switch 2 uses this as the outgoing VCI in the table.
c. Switch 2 sends an acknowledgment to switch 1 that contains its incoming VCI in the
table, chosen in the previous step. Switch 1 uses this as the outgoing VCI in the table.
d. Finally switch 1 sends an acknowledgment to source A that contains its incoming
VCI in the table, chosen in the previous step.
e. The source uses this as the outgoing VCI for the data frames to be sent to destination B.

#### Teardown Phase
> id: ch08-8-3-2-teardown-phase | src: book p.221 | kind: concept

In this phase, source A, after sending all frames to B, sends a special frame called a
teardown request. Destination B responds with a teardown confirmation frame. All
switches delete the corresponding entry from their tables.

#### Efficiency
> id: ch08-8-3-2-efficiency | src: book p.221 | kind: concept

As we said before, resource reservation in a virtual-circuit network can be made during
the setup or can be on demand during the data-transfer phase. In the first case, the delay
for each packet is the same; in the second case, each packet may encounter different
delays. There is one big advantage in a virtual-circuit network even if resource allocation
is on demand. The source can check the availability of the resources, without actually
reserving it. Consider a family that wants to dine at a restaurant. Although the restaurant
may not accept reservations (allocation of the tables is on demand), the family can call
and find out the waiting time. This can save the family time and effort.

In virtual-circuit switching, all packets belonging to the same source and destination
travel the same path, but the packets may arrive at the destination
with different delays if resource allocation is on demand.

#### Delay in Virtual-Circuit Networks
> id: ch08-8-3-2-delay-in-virtual-circuit-networks | src: book p.221 | kind: concept

In a virtual-circuit network, there is a one-time delay for setup and a one-time delay for
teardown. If resources are allocated during the setup phase, there is no wait time for
individual packets. Figure 8.16 shows the delay for a packet traveling through two
switches in a virtual-circuit network.

> **[ASSET ch08_ill_016]** Figure 8.16: Delay in a virtual-circuit network
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_016.png
> - src: book Figure 8.16; p.221
> - shows: Figure 8.16: Delay in a virtual-circuit network. A time-sequence diagram shows setup and teardown surrounding packet transmission through two switches in a virtual-circuit network.
> - structure: A time-sequence diagram shows setup and teardown surrounding packet transmission through two switches in a virtual-circuit network.
> - text_in_image: A; B; Setup; Total delay; Transmission; time; Teardown; Time; Time; Time; Time
> - use_when: Teach ch08-8-3-2-delay-in-virtual-circuit-networks, interpret Figure 8.16, trace a switching path, or solve a linked practice question.
> - confidence: high

The packet is traveling through two switches (routers). There are three transmission times (3T ), three propagation times (3τ), data transfer depicted by the sloping
lines, a setup delay (which includes transmission and propagation in two directions),
and a teardown delay (which includes transmission and propagation in one direction).
We ignore the processing time in each switch. The total delay time is

$$D_{\mathrm{total}}=3T+3\tau+D_{\mathrm{setup}}+D_{\mathrm{teardown}}$$

#### Circuit-Switched Technology in WANs
> id: ch08-8-3-2-circuit-switched-technology-in-wans | src: book p.222 | kind: concept

As we will see in Chapter 14, virtual-circuit networks are used in switched WANs such
as ATM networks. The data-link layer of these technologies is well suited to the virtual-circuit technology.

Switching at the data-link layer in a switched WAN is normally
implemented by using virtual-circuit techniques.

## 8.4 STRUCTURE OF A SWITCH
> id: ch08-8-4 | src: book 8.4; p.222 | kind: concept

We use switches in circuit-switched and packet-switched networks. In this section, we
discuss the structures of the switches used in each type of network.

### 8.4.1 Structure of Circuit Switches
> id: ch08-8-4-1 | src: book 8.4.1; p.222 | kind: concept

Circuit switching today can use either of two technologies: the space-division switch or
the time-division switch.

#### Space-Division Switch
> id: ch08-8-4-1-space-division-switch | src: book p.222 | kind: concept

In space-division switching, the paths in the circuit are separated from one another
spatially. This technology was originally designed for use in analog networks but is
used currently in both analog and digital networks. It has evolved through a long history
of many designs.

#### Crossbar Switch
> id: ch08-8-4-1-crossbar-switch | src: book p.222 | kind: concept

A crossbar switch connects n inputs to m outputs in a grid, using electronic microswitches (transistors) at each crosspoint (see Figure 8.17). The major limitation of this
design is the number of crosspoints required. To connect n inputs to m outputs using a

> **[ASSET ch08_ill_017]** Figure 8.17: Crossbar switch with three inputs and four outputs
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_017.png
> - src: book Figure 8.17; p.222
> - shows: Figure 8.17: Crossbar switch with three inputs and four outputs. A 3-input by 4-output crossbar grid marks controllable crosspoints and one selected input-to-output connection.
> - structure: A 3-input by 4-output crossbar grid marks controllable crosspoints and one selected input-to-output connection.
> - text_in_image: 1; To control station; 2; Crosspoint; 3; I; II; III; IV
> - use_when: Teach ch08-8-4-1-crossbar-switch, interpret Figure 8.17, trace a switching path, or solve a linked practice question.
> - confidence: high

crossbar switch requires n × m crosspoints. For example, to connect 1000 inputs to
1000 outputs requires a switch with 1,000,000 crosspoints. A crossbar switch [?] with
this number of crosspoints is impractical. Such a switch is also inefficient because statistics show that, in practice, fewer than 25 percent of the crosspoints are in use at any
given time. The rest are idle.

#### Multistage Switch
> id: ch08-8-4-1-multistage-switch | src: book p.223 | kind: concept

The solution to the limitations of the crossbar switch is the multistage switch, which
combines crossbar switches in several (normally three) stages, as shown in Figure 8.18.
In a single crossbar switch, only one row or column (one path) is active for any connection. So we need N × N crosspoints. If we can allow multiple paths inside the switch,
we can decrease the number of crosspoints. Each crosspoint in the middle stage can be
accessed by multiple crosspoints in the first or third stage.

> **[ASSET ch08_ill_018]** Figure 8.18: Multistage switch
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_018.png
> - src: book Figure 8.18; p.223
> - shows: Figure 8.18: Multistage switch. A general three-stage switch contains N/n first-stage n-by-k crossbars, k middle-stage N/n-by-N/n crossbars, and symmetric third-stage k-by-n crossbars.
> - structure: A general three-stage switch contains N/n first-stage n-by-k crossbars, k middle-stage N/n-by-N/n crossbars, and symmetric third-stage k-by-n crossbars.
> - text_in_image: N/n; N/n; k; Crossbars; Crossbars; Crossbars; n × k; k × n; n; n; …; …; N/n × N/n; …; …; …; k × n; n × k; n; n; …; …; N; N; …; …; …; …; N/n × N/n; …; …; k × n; n × k; n; n; …; …; Stage 1; Stage 2; Stage 3
> - use_when: Teach ch08-8-4-1-multistage-switch, interpret Figure 8.18, trace a switching path, or solve a linked practice question.
> - confidence: high

To design a three-stage switch, we follow these steps:
1. We divide the N input lines into groups, each of n lines. For each group, we use one
crossbar of size n × k, where k is the number of crossbars in the middle stage. In
other words, the first stage has N/n crossbars of n × k crosspoints.
2. We use k crossbars, each of size (N/n) × (N/n) in the middle stage.
3. We use N/n crossbars, each of size k × n at the third stage.
We can calculate the total number of crosspoints as follows:

$$C=2\left(\frac{N}{n}\right)(nk)+k\left(\frac{N}{n}\right)^2=2kN+k\left(\frac{N}{n}\right)^2$$

In a three-stage switch, the total number of crosspoints is\n\n$$C=2kN+k\left(\frac{N}{n}\right)^2$$
which is much smaller than the number of crosspoints in a single-stage switch ($N^{2}$).
##### Example 8.3
> id: ch08-example-8-3 | src: book Example 8.3 | kind: worked_example
Design a three-stage, 200 × 200 switch (N = 200) with k = 4 and n = 20.

**Solution**
In the first stage we have N/n or 10 crossbars, each of size 20 × 4. In the second stage, we have
4 crossbars, each of size 10 × 10. In the third stage, we have 10 crossbars, each of size 4 × 20.
The total number of crosspoints is $2kN+k(N/n)^2$, or 2000 crosspoints. This is 5 percent of the
number of crosspoints in a single-stage switch (200 × 200 = 40,000).

The multistage switch in Example 8.3 has one drawback—blocking during periods
of heavy traffic. The whole idea of multistage switching is to share the crosspoints in
the middle-stage crossbars. Sharing can cause a lack of availability if the resources are
limited and all users want a connection at the same time. Blocking refers to times when
one input cannot be connected to an output because there is no path available between
them—all the possible intermediate switches are occupied.
In a single-stage switch, blocking does not occur because every combination of
input and output has its own crosspoint; there is always a path. (Cases in which two
inputs are trying to contact the same output do not count. That path is not blocked; the
output is merely busy.) In the multistage switch described in Example 8.3, however,
only four of the first 20 inputs can use the switch at a time, only four of the second 20
inputs can use the switch at a time, and so on. The small number of crossbars at the
middle stage creates blocking.
In large systems, such as those having 10,000 inputs and outputs, the number of
stages can be increased to cut down on the number of crosspoints required. As the number of stages increases, however, possible blocking increases as well. Many people have
experienced blocking on public telephone systems in the wake of a natural disaster
when the calls being made to check on or reassure relatives far outnumber the regular
load of the system.
Clos investigated the condition of nonblocking in multistage switches and came up
with the following formula. In a nonblocking switch, the number of middle-stage
switches must be at least 2n – 1. In other words, we need to have k ≥ 2n – 1.
Note that the number of crosspoints is still smaller than that in a single-stage
switch. Now we need to minimize the number of crosspoints with a fixed N by using
the Clos criteria. We can take the derivative of the equation with respect to n (the only
variable) and find the value of n that makes the result zero. This n must be equal to or
greater than $\sqrt{N/2}$. In this case, the total number of crosspoints is greater than or equal
to 4N $[\sqrt{2N}-1]$. In other words, the minimum number of crosspoints according to the
Clos criteria is proportional to $N^{3/2}$.

According to Clos criterion:  n = $\sqrt{N/2}$   and     k ≥ 2n − 1
Total number of crosspoints  ≥ 4N [(2N)1/2 − 1]

##### Example 8.4
> id: ch08-example-8-4 | src: book Example 8.4 | kind: worked_example
Redesign the previous three-stage, 200 × 200 switch, using the Clos criteria with a minimum
number of crosspoints.
**Solution**
We let n = (200/2)1/2, or n = 10. We calculate k = 2n – 1 = 19. In the first stage, we have 200/10,
or 20, crossbars, each with 10 × 19 crosspoints. In the second stage, we have 19 crossbars,
each with 10 × 10 crosspoints. In the third stage, we have 20 crossbars each with 19 × 10
crosspoints. The total number of crosspoints is 20(10 × 19) + 19(10 × 10) + 20(19 × 10) =
9500. If we use a single-stage switch, we need 200 × 200 = 40,000 crosspoints. The number
of crosspoints in this three-stage switch is 24 percent that of a single-stage switch. More
points are needed than in Example 8.3 (5 percent). The extra crosspoints are needed to prevent blocking.

A multistage switch that uses the Clos criteria and a minimum number of crosspoints
still requires a huge number of crosspoints. For example, to have a 100,000 input/output
switch, we need something close to 200 million crosspoints (instead of 10 billion). This
means that if a telephone company needs to provide a switch to connect 100,000 telephones in a city, it needs 200 million crosspoints. The number can be reduced if we
accept blocking. Today, telephone companies use time-division switching or a combination of space- and time-division switches, as we will see shortly.

#### Time-Division Switch
> id: ch08-8-4-1-time-division-switch | src: book p.225 | kind: concept

Time-division switching uses time-division multiplexing (TDM) inside a switch. The
most popular technology is called the time-slot interchange (TSI).

#### Time-Slot Interchange
> id: ch08-8-4-1-time-slot-interchange | src: book p.225 | kind: concept

Figure 8.19 shows a system connecting four input lines to four output lines. Imagine
that each input line wants to send data to an output line according to the following pattern: (1 →3), (2 →4), (3 →1), and  (4 → 2), in which the arrow means “to.”

> **[ASSET ch08_ill_019]** Figure 8.19: Time-slot interchange
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_019.png
> - src: book Figure 8.19; p.225
> - shows: Figure 8.19: Time-slot interchange. A time-slot interchange switch writes four input slots to RAM sequentially and reads them in a control-memory-selected order to produce the permuted output slots.
> - structure: A time-slot interchange switch writes four input slots to RAM sequentially and reads them in a control-memory-selected order to produce the permuted output slots.
> - text_in_image: Time-division switch; Control unit; TSI; 3; 1; 2; 4; C; 3; 1; A; 1; 1; 2; 4; B; D; 2; 2; B A; D C; T; T; D C; B; D; D; A; C; A; 3; 3; M; M; Selectively; Sequentially; controlled; B; D; controlled; 4; 4; RAM
> - use_when: Teach ch08-8-4-1-time-slot-interchange, interpret Figure 8.19, trace a switching path, or solve a linked practice question.
> - confidence: high

The figure combines a TDM multiplexer, a TDM demultiplexer, and a TSI consisting of random access memory (RAM) with several memory locations. The size of each
location is the same as the size of a single time slot. The number of locations is the same
as the number of inputs (in most cases, the numbers of inputs and outputs are equal).
The RAM fills up with incoming data from time slots in the order received. Slots are
then sent out in an order based on the decisions of a control unit.

#### Time- and Space-Division Switch Combinations
> id: ch08-8-4-1-time-and-space-division-switch-combinations | src: book p.226 | kind: concept

When we compare space-division and time-division switching, some interesting facts
emerge. The advantage of space-division switching is that it is instantaneous. Its disadvantage is the number of crosspoints required to make space-division switching acceptable in
terms of blocking.
The advantage of time-division switching is that it needs no crosspoints. Its disadvantage, in the case of TSI, is that processing each connection creates delays. Each time
slot must be stored by the RAM, then retrieved and passed on.
In a third option, we combine space-division and time-division technologies to
take advantage of the best of both. Combining the two results in switches that are
optimized both physically (the number of crosspoints) and temporally (the amount
of delay). Multistage switches of this sort can be designed as time-space-time (TST)
switches.
Figure 8.20 shows a simple TST switch that consists of two time stages and one
space stage and has 12 inputs and 12 outputs. Instead of one time-division switch, it
divides the inputs into three groups (of four inputs each) and directs them to three time-slot interchanges. The result is that the average delay is one-third of what would result
from using one time-slot interchange to handle all 12 inputs.

> **[ASSET ch08_ill_020]** Figure 8.20: Time-space-time switch
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_020.png
> - src: book Figure 8.20; p.226
> - shows: Figure 8.20: Time-space-time switch. A time-space-time switch places TSI blocks before and after a middle crossbar, combining time-slot permutation with spatial path selection.
> - structure: A time-space-time switch places TSI blocks before and after a middle crossbar, combining time-slot permutation with spatial path selection.
> - text_in_image: TST; Time; Space; Time
> - use_when: Teach ch08-8-4-1-time-and-space-division-switch-combinations, interpret Figure 8.20, trace a switching path, or solve a linked practice question.
> - confidence: high

The last stage is a mirror image of the first stage. The middle stage is a space-division switch (crossbar) that connects the TSI groups to allow connectivity between
all possible input and output pairs (e.g., to connect input 3 of the first group to output 7
of the second group).

### 8.4.2 Structure of Packet Switches
> id: ch08-8-4-2 | src: book 8.4.2; p.226 | kind: concept

A switch used in a packet-switched network has a different structure from a switch used
in a circuit-switched network.We can say that a packet switch has four components:
input ports, output ports, the routing processor, and the switching fabric, as shown
in Figure 8.21.

> **[ASSET ch08_ill_021]** Figure 8.21: Packet switch components
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_021.png
> - src: book Figure 8.21; p.227
> - shows: Figure 8.21: Packet switch components. A packet switch contains input ports, output ports, a routing processor, and the central switching fabric that connects queued packets to selected outputs.
> - structure: A packet switch contains input ports, output ports, a routing processor, and the central switching fabric that connects queued packets to selected outputs.
> - text_in_image: Routing; processor; Input ports; Output ports; Port 1; Port 1; Port 2; Port 2; Switching fabric; • • •; • • •; Port N; Port N
> - use_when: Teach ch08-8-4-2, interpret Figure 8.21, trace a switching path, or solve a linked practice question.
> - confidence: high

#### Input Ports
> id: ch08-8-4-2-input-ports | src: book p.227 | kind: concept

An input port performs the physical and data-link functions of the packet switch. The
bits are constructed from the received signal. The packet is decapsulated from the frame.
Errors are detected and corrected. The packet is now ready to be routed by the network
layer. In addition to a physical-layer processor and a data-link processor, the input port
has buffers (queues) to hold the packet before it is directed to the switching fabric.
Figure 8.22 shows a schematic diagram of an input port.

> **[ASSET ch08_ill_022]** Figure 8.22: Input port
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_022.png
> - src: book Figure 8.22; p.227
> - shows: Figure 8.22: Input port. An input port pipeline applies physical-layer processing, data-link processing, and queueing before a packet enters the switching fabric.
> - structure: An input port pipeline applies physical-layer processing, data-link processing, and queueing before a packet enters the switching fabric.
> - text_in_image: Input port; Physical-layer; Data-link-layer; processor; processor; Queue
> - use_when: Teach ch08-8-4-2-input-ports, interpret Figure 8.22, trace a switching path, or solve a linked practice question.
> - confidence: high

#### Output Port
> id: ch08-8-4-2-output-port | src: book p.227 | kind: concept

The output port performs the same functions as the input port, but in the reverse order.
First the outgoing packets are queued, then the packet is encapsulated in a frame, and
finally the physical-layer functions are applied to the frame to create the signal to be
sent on the line. Figure 8.23 shows a schematic diagram of an output port.

> **[ASSET ch08_ill_023]** Figure 8.23: Output port
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_023.png
> - src: book Figure 8.23; p.227
> - shows: Figure 8.23: Output port. An output port pipeline queues packets from the fabric, performs data-link processing, and sends them through the physical layer.
> - structure: An output port pipeline queues packets from the fabric, performs data-link processing, and sends them through the physical layer.
> - text_in_image: Output port; Data-link-layer; Physical-layer; processor; processor; Queue
> - use_when: Teach ch08-8-4-2-output-port, interpret Figure 8.23, trace a switching path, or solve a linked practice question.
> - confidence: high

#### Routing Processor
> id: ch08-8-4-2-routing-processor | src: book p.228 | kind: concept

The routing processor performs the functions of the network layer. The destination
address is used to find the address of the next hop and, at the same time, the output port
number from which the packet is sent out. This activity is sometimes referred to as
table lookup because the routing processor searches the routing table. In the newer
packet switches, this function of the routing processor is being moved to the input ports
to facilitate and expedite the process.

#### Switching Fabrics
> id: ch08-8-4-2-switching-fabrics | src: book p.228 | kind: concept

The most difficult task in a packet switch is to move the packet from the input queue to
the output queue. The speed with which this is done affects the size of the input/output
queue and the overall delay in packet delivery. In the past, when a packet switch was
actually a dedicated computer, the memory of the computer or a bus was used as the
switching fabric. The input port stored the packet in memory; the output port retrieved
the packet from memory. Today, packet switches are specialized mechanisms that use a
variety of switching fabrics. We briefly discuss some of these fabrics here.

#### Crossbar Switch
> id: ch08-8-4-2-crossbar-switch | src: book p.228 | kind: concept

The simplest type of switching fabric is the crossbar switch, discussed in the previous
section.

#### Banyan Switch
> id: ch08-8-4-2-banyan-switch | src: book p.228 | kind: concept

A more realistic approach than the crossbar switch is the banyan switch (named after
the banyan tree). A banyan switch is a multistage switch with microswitches at each
stage that route the packets based on the output port represented as a binary string. For n
inputs and n outputs, we have $\log_2 n$ stages with n/2 microswitches at each stage. The first
stage routes the packet based on the high-order bit of the binary string. The second stage
routes the packet based on the second high-order bit, and so on. Figure 8.24 shows a banyan switch with eight inputs and eight outputs. The number of stages is $\log_2(8)$ = 3.

> **[ASSET ch08_ill_024]** Figure 8.24: A banyan switch
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_024.png
> - src: book Figure 8.24; p.228
> - shows: Figure 8.24: A banyan switch. An 8-by-8 banyan switch uses three stages; left, middle, and right destination bits control successive 2-by-2 microswitches.
> - structure: An 8-by-8 banyan switch uses three stages; left, middle, and right destination bits control successive 2-by-2 microswitches.
> - text_in_image: Left bit; Middle bit; Right bit; 0; 0; 0; 0; 0; A-1; B-1; C-1; 1; 1; 1; 1; 1; 0; 0; 0; 2; 2; A-2; B-2; C-2; 3; 3; 1; 1; 1; 0; 0; 0; 4; 4; A-3; B-3; C-3; 5; 5; 1; 1; 1; 0; 0; 0; 6; 6; A-4; B-4; C-4; 7; 7; 1; 1; 1
> - use_when: Teach ch08-8-4-2-banyan-switch, interpret Figure 8.24, trace a switching path, or solve a linked practice question.
> - confidence: high

Figure 8.25 shows the operation. In part a, a packet has arrived at input port 1 and
must go to output port 6 (110 in binary). The first microswitch (A-2) routes the packet

> **[ASSET ch08_ill_025]** Figure 8.25: Examples of routing in a banyan switch
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_025.png
> - src: book Figure 8.25; p.229
> - shows: Figure 8.25: Examples of routing in a banyan switch. Two banyan examples highlight the stage-by-stage routes for input 1 to output 6 (110) and input 5 to output 2 (010).
> - structure: Two banyan examples highlight the stage-by-stage routes for input 1 to output 6 (110) and input 5 to output 2 (010).
> - text_in_image: 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; A-1; B-1; C-1; A-1; B-1; C-1; 1; 1; 1; 1; 1; 1; 1; 1; 1; 1; 0; 0; 0; 0; 0; 0; 2; 2; 2; 2; A-2; B-2; C-2; A-2; B-2; C-2; 3; 3; 3; 3; 1; 1; 1; 1; 1; 1; 0; 0; 0; 0; 0; 0; 4; 4; 4; 4; A-3; B-3; C-3; A-3; B-3; C-3; 5; 5; 5; 5; 1; 1; 1; 1; 1; 1; 0; 0; 0; 0; 0; 0; 6; 6; 6; 6; A-4; B-4; C-4; A-4; B-4; C-4; 7; 7; 7; 7; 1; 1; 1; 1; 1; 1; a. Input 1 sending a cell to output 6 (110); b. Input 5 sending a cell to output 2 (010)
> - use_when: Teach ch08-8-4-2-banyan-switch, interpret Figure 8.25, trace a switching path, or solve a linked practice question.
> - confidence: high

based on the first bit (1), the second microswitch (B-4) routes the packet based on the
second bit (1), and the third microswitch (C-4) routes the packet based on the third bit (0).
In part b, a packet has arrived at input port 5 and must go to output port 2 (010 in
binary). The first microswitch (A-2) routes the packet based on the first bit (0), the second microswitch (B-2) routes the packet based on the second bit (1), and the third
microswitch (C-2) routes the packet based on the third bit (0).

#### Batcher-Banyan Switch
> id: ch08-8-4-2-batcher-banyan-switch | src: book p.229 | kind: concept

The problem with the banyan switch is the possibility of
internal collision even when two packets are not heading for the same output port. We
can solve this problem by sorting the arriving packets based on their destination port.
K. E. Batcher designed a switch that comes before the banyan switch and sorts the
incoming packets according to their final destinations. The combination is called the
Batcher-banyan switch. The sorting switch uses hardware merging techniques, but we
do not discuss the details here. Normally, another hardware module called a trap is
added between the Batcher switch and the banyan switch (see Figure 8.26) The trap
module prevents duplicate packets (the packets with the same output destination) from
passing to the banyan switch simultaneously. Only one packet for each destination is
allowed at each tick; if there is more than one, they wait for the next tick.

> **[ASSET ch08_ill_026]** Figure 8.26: Batcher-banyan switch
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_026.png
> - src: book Figure 8.26; p.229
> - shows: Figure 8.26: Batcher-banyan switch. A Batcher sorter and trap module precede an 8-by-8 banyan switch so packets are ordered by destination and duplicate simultaneous destinations are held back.
> - structure: A Batcher sorter and trap module precede an 8-by-8 banyan switch so packets are ordered by destination and duplicate simultaneous destinations are held back.
> - text_in_image: Banyan switch; 0; 0; 0; 0; 0; A-1; B-1; C-1; 1; 1; 1; 1; 1; 0; 0; 0; 2; 2; A-2; B-2; C-2; 3; 3; 1; 1; 1; Batcher; Trap; switch; module; 0; 0; 0; 4; 4; A-3; B-3; C-3; 5; 5; 1; 1; 1; 0; 0; 0; 6; 6; A-4; B-4; C-4; 7; 7; 1; 1; 1
> - use_when: Teach ch08-8-4-2-batcher-banyan-switch, interpret Figure 8.26, trace a switching path, or solve a linked practice question.
> - confidence: high

## 8.5 END-CHAPTER MATERIALS
> id: ch08-8-5 | src: book 8.5; p.230 | kind: concept

### 8.5.1 Recommended Reading
> id: ch08-8-5-1 | src: book 8.5.1; p.230 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [. . .] refer to the reference list at the end of the text.

#### Books
> id: ch08-8-5-1-books | src: book p.230 | kind: concept

Switching is discussed in [Sta04] and [GW04]. Circuit-switching is fully discussed in
[BEL01].

### 8.5.2 Key terms
> id: ch08-8-5-2 | src: book 8.5.2; p.230 | kind: concept

banyan switch
packet-switched network
Batcher-banyan switch
routing processor
blocking
setup phase
circuit switching
space-division switching
circuit-switched network
switch
crossbar switch
switching
crosspoint
switching fabric
data-transfer phase
table lookup
datagram
teardown phase
datagram network
time-division switching
end system
time-slot interchange (TSI)
input port
time-space-time (TST) switch
message switching
trap
multistage switch
virtual-circuit identifier (VCI)
output port
virtual-circuit network
packet switching

### 8.5.3 Summary
> id: ch08-8-5-3 | src: book 8.5.3; p.230 | kind: summary

A switched network consists of a series of interlinked nodes, called switches. Traditionally, three methods of switching have been important: circuit switching, packet switching, and message switching.
We can divide today’s networks into three broad categories: circuit-switched networks, packet-switched networks, and message-switched networks. Packet-switched
networks can also be divided into two subcategories: virtual-circuit networks and datagram networks. A circuit-switched network is made of a set of switches connected by
physical links, in which each link is divided into n channels. Circuit switching takes
place at the physical layer. In circuit switching, the resources need to be reserved during the setup phase; the resources remain dedicated for the entire duration of the data-transfer phase until the teardown phase.
In packet switching, there is no resource allocation for a packet. This means that
there is no reserved bandwidth on the links, and there is no scheduled processing time for
each packet. Resources are allocated on demand. In a datagram network, each packet is
treated independently of all others. Packets in this approach are referred to as datagrams.
There are no setup or teardown phases. A virtual-circuit network is a cross between a
circuit-switched network and a datagram network. It has some characteristics of both.
Circuit switching uses either of two technologies: the space-division switch or the time-division switch. A switch in a packet-switched network has a different structure from a
switch used in a circuit-switched network. We can say that a packet switch has four types
of components: input ports, output ports, a routing processor, and switching fabric.
