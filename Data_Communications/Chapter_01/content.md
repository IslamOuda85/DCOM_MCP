---
doc_type: scientific_content
course_id: data_communications
chapter: 1
chapter_id: data_communications_ch01
chapter_title: Introduction
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_1/ch1.pdf
  pages: 1-30
assets_dir: assets
asset_counts:
  illustration: 17
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-06T21:41:30+00:00'
status: complete
---
# Chapter 1: Introduction

## Chapter Objectives
> id: ch01-0 | src: book p.3 | kind: objectives

Data communications and networking have changed the way we do business and the
way we live. Business decisions have to be made ever more quickly, and the decision makers require immediate access to accurate information. Why wait a week for
that report from Europe to arrive by mail when it could appear almost instantaneously
through computer networks? Businesses today rely on computer networks and internetworks.
Data communication and networking have found their way not only through business and personal communication, they have found many applications in political and
social issues. People have found how to communicate with other people in the world to
express their social and political opinions and problems. Communities in the world are
not isolated anymore.
But before we ask how quickly we can get hooked up, we need to know how networks operate, what types of technologies are available, and which design best fills
which set of needs.
This chapter paves the way for the rest of the  book. It is divided into five sections.

- The first section introduces data communications and defines their components
and the types of data exchanged. It also shows how different types of data are represented and how data is flowed through the network.

- The second section introduces networks and defines their criteria and structures. It
introduces four different network topologies that are encountered throughout the
book.

- The third section discusses different types of networks: LANs, WANs, and internetworks (internets). It also introduces the Internet, the largest internet in the
world. The concept of switching is also introduced in this section to show how
small networks can be combined to create larger ones.

- The fourth section covers a brief history of the Internet. The section is divided into
three eras: early history, the birth of the Internet, and the issues related to the Internet today. This section can be skipped if the reader is familiar with this history.

- The fifth section covers standards and standards organizations. The section covers
Internet standards and Internet administration. We refer to these standards and
organizations throughout the book.

## 1.1 DATA COMMUNICATIONS
> id: ch01-1-1 | src: book 1.1; p.4 | kind: concept

When we communicate, we are sharing information. This sharing can be local or
remote. Between individuals, local communication usually occurs face to face, while
remote communication takes place over distance. The term telecommunication, which
includes telephony, telegraphy, and television, means communication at a distance (tele
is Greek for “far”). The word data refers to information presented in whatever form is
agreed upon by the parties creating and using the data.
Data communications are the exchange of data between two devices via some
form of transmission medium such as a wire cable. For data communications to occur,
the communicating devices must be part of a communication system made up of a combination of hardware (physical equipment) and software (programs). The effectiveness
of a data communications system depends on four fundamental characteristics: delivery, accuracy, timeliness, and jitter.
1. Delivery. The system must deliver data to the correct destination. Data must be
received by the intended device or user and only by that device or user.
2. Accuracy. The system must deliver the data accurately. Data that have been
altered in transmission and left uncorrected are unusable.
3. Timeliness. The system must deliver data in a timely manner. Data delivered late are
useless. In the case of video and audio, timely delivery means delivering data as
they are produced, in the same order that they are produced, and without significant delay. This kind of delivery is called real-time transmission.
4. Jitter. Jitter refers to the variation in the packet arrival time. It is the uneven delay in
the delivery of audio or video packets. For example, let us assume that video packets
are sent every 30 ms. If some of the packets arrive with 30-ms delay and others with
40-ms delay, an uneven quality in the video is the result.

### 1.1.1 Components
> id: ch01-1-1-1 | src: book 1.1.1; p.4 | kind: concept

A data communications system has five components (see Figure 1.1).

> **[ASSET ch01_ill_001]** Figure 1.1: Five components of data communication
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_001.png
> - src: book Figure 1.1; p.4
> - shows: Figure 1.1: Five components of data communication. Sender at left and receiver at right share a transmission medium. A message arrow points left to right. Each endpoint has a protocol rule list (Rule 1, Rule 2, through Rule n); the five components are message, sender, receiver, medium, and protocol.
> - structure: Sender at left and receiver at right share a transmission medium. A message arrow points left to right. Each endpoint has a protocol rule list (Rule 1, Rule 2, through Rule n); the five components are message, sender, receiver, medium, and protocol.
> - text_in_image: Rule 1:; Rule 1:; Rule 2:; Rule 2:; Protocol; Protocol; ...; ...; Rule n:; Rule n:; Message; Sender; Receiver; Transmission medium
> - use_when: Teach ch01-1-1-1, explain Figure 1.1, or solve its linked practice questions.
> - confidence: high

1. Message. The message is the information (data) to be communicated. Popular
forms of information include text, numbers, pictures, audio, and video.
2. Sender. The sender is the device that sends the data message. It can be a computer, workstation, telephone handset, video camera, and so on.
3. Receiver. The receiver is the device that receives the message. It can be a computer, workstation, telephone handset, television, and so on.
4. Transmission medium. The transmission medium is the physical path by which
a message travels from sender to receiver. Some examples of transmission media
include twisted-pair wire, coaxial cable, fiber-optic cable, and radio waves.
5. Protocol. A protocol is a set of rules that govern data communications. It represents an agreement between the communicating devices. Without a protocol, two
devices may be connected but not communicating, just as a person speaking French
cannot be understood by a person who speaks only Japanese.

### 1.1.2 Data Representation
> id: ch01-1-1-2 | src: book 1.1.2; p.5 | kind: concept

Information today comes in different forms such as text, numbers, images, audio, and
video.

#### Text
> id: ch01-1-1-2-text | src: book 1.1.2; p.5 | kind: concept

In data communications, text is represented as a bit pattern, a sequence of bits (0s or
1s). Different sets of bit patterns have been designed to represent text symbols. Each set
is called a code, and the process of representing symbols is called coding. Today, the
prevalent coding system is called Unicode, which uses 32 bits to represent a symbol or
character used in any language in the world. The American Standard Code for Information Interchange (ASCII), developed some decades ago in the United States, now
constitutes the first 127 characters in Unicode and is also referred to as Basic Latin.
Appendix A includes part of the Unicode.

#### Numbers
> id: ch01-1-1-2-numbers | src: book 1.1.2; p.5 | kind: concept

Numbers are also represented by bit patterns. However, a code such as ASCII is not used
to represent numbers; the number is directly converted to a binary number to simplify
mathematical operations. Appendix B discusses several different numbering systems.

#### Images
> id: ch01-1-1-2-images | src: book 1.1.2; p.5 | kind: concept

Images are also represented by bit patterns. In its simplest form, an image is composed
of a matrix of pixels (picture elements), where each pixel is a small dot. The size of the
pixel depends on the resolution. For example, an image can be divided into 1000 pixels
or 10,000 pixels. In the second case, there is a better representation of the image (better
resolution), but more memory is needed to store the image.
After an image is divided into pixels, each pixel is assigned a bit pattern. The size
and the value of the pattern depend on the image. For an image made of only blackand-white dots (e.g., a chessboard), a 1-bit pattern is enough to represent a pixel.
If an image is not made of pure white and pure black pixels, we can increase the
size of the bit pattern to include gray scale. For example, to show four levels of gray
scale, we can use 2-bit patterns. A black pixel can be represented by 00, a dark gray
pixel by 01, a light gray pixel by 10, and a white pixel by 11.
There are several methods to represent color images. One method is called RGB,
so called because each color is made of a combination of three primary colors: red,
green, and blue. The intensity of each color is measured, and a bit pattern is assigned to
it. Another method is called YCM, in which a color is made of a combination of three
other primary colors: yellow, cyan, and magenta.

#### Audio
> id: ch01-1-1-2-audio | src: book 1.1.2; p.5 | kind: concept

Audio refers to the recording or broadcasting of sound or music. Audio is by nature
different from text, numbers, or images. It is continuous, not discrete. Even when we
use a microphone to change voice or music to an electric signal, we create a continuous
signal. We will learn more about audio in Chapter 26.

#### Video
> id: ch01-1-1-2-video | src: book 1.1.2; p.5 | kind: concept

Video refers to the recording or broadcasting of a picture or movie. Video can either be
produced as a continuous entity (e.g., by a TV camera), or it can be a combination of
images, each a discrete entity, arranged to convey the idea of motion. We will learn
more about video in Chapter 26.

### 1.1.3 Data Flow
> id: ch01-1-1-3 | src: book 1.1.3; p.6 | kind: concept

Communication between two devices can be simplex, half-duplex, or full-duplex as
shown in Figure 1.2.

> **[ASSET ch01_ill_002]** Figure 1.2: Data flow (simplex, half-duplex, and full-duplex)
> - type: illustration
> - kind: flow
> - file: assets/ch01_ill_002.png
> - src: book Figure 1.2; p.6
> - shows: Figure 1.2: Data flow (simplex, half-duplex, and full-duplex). Three panels: (a) simplex has one rightward data arrow from mainframe to monitor; (b) half-duplex has a rightward arrow at time 1 and a leftward arrow at time 2; (c) full-duplex has opposing data arrows available all the time.
> - structure: Three panels: (a) simplex has one rightward data arrow from mainframe to monitor; (b) half-duplex has a rightward arrow at time 1 and a leftward arrow at time 2; (c) full-duplex has opposing data arrows available all the time.
> - text_in_image: Direction of data; a. Simplex; Mainframe; Monitor; Direction of data at time 1; Direction of data at time 2; b. Half-duplex; Direction of data all the time; c. Full-duplex
> - use_when: Teach ch01-1-1-3, explain Figure 1.2, or solve its linked practice questions.
> - confidence: high

#### Simplex
> id: ch01-1-1-3-simplex | src: book 1.1.3; p.6 | kind: concept

In simplex mode, the communication is unidirectional, as on a one-way street. Only one
of the two devices on a link can transmit; the other can only receive (see Figure 1.2a).
Keyboards and traditional monitors are examples of simplex devices. The keyboard can only introduce input; the monitor can only accept output. The simplex mode
can use the entire capacity of the channel to send data in one direction.

#### Half-Duplex
> id: ch01-1-1-3-half-duplex | src: book 1.1.3; p.6 | kind: concept

In half-duplex mode, each station can both transmit and receive, but not at the same time.
When one device is sending, the other can only receive, and vice versa (see Figure 1.2b).
The half-duplex mode is like a one-lane road with traffic allowed in both directions. When cars are traveling in one direction, cars going the other way must wait. In a
half-duplex transmission, the entire capacity of a channel is taken over by whichever of
the two devices is transmitting at the time. Walkie-talkies and CB (citizens band) radios
are both half-duplex systems.
The half-duplex mode is used in cases where there is no need for communication
in both directions at the same time; the entire capacity of the channel can be utilized for
each direction.

#### Full-Duplex
> id: ch01-1-1-3-full-duplex | src: book 1.1.3; p.6 | kind: concept

In full-duplex mode (also called duplex), both stations can transmit and receive simultaneously (see Figure 1.2c).
The full-duplex mode is like a two-way street with traffic flowing in both directions at the same time. In full-duplex mode, signals going in one direction share the
capacity of the link with signals going in the other direction. This sharing can occur in
two ways: Either the link must contain two physically separate transmission paths, one
for sending and the other for receiving; or the capacity of the channel is divided
between signals traveling in both directions.
One common example of full-duplex communication is the telephone network.
When two people are communicating by a telephone line, both can talk and listen at the
same time.
The full-duplex mode is used when communication in both directions is required
all the time. The capacity of the channel, however, must be divided between the two
directions.

## 1.2 NETWORKS
> id: ch01-1-2 | src: book 1.2; p.7 | kind: concept

A network is the interconnection of a set of devices capable of communication. In this
definition, a device can be a host (or an end system as it is sometimes called) such as a
large computer, desktop, laptop, workstation, cellular phone, or security system. A
device in this definition can also be a connecting device such as a router, which connects the network to other networks, a switch, which connects devices together, a
modem (modulator-demodulator), which changes the form of data, and so on. These
devices in a network are connected using wired or wireless transmission media such as
cable or air. When we connect two computers at home using a plug-and-play router, we
have created a network, although very small.

### 1.2.1 Network Criteria
> id: ch01-1-2-1 | src: book 1.2.1; p.7 | kind: concept

A network must be able to meet a certain number of criteria. The most important of
these are performance, reliability, and security.

#### Performance
> id: ch01-1-2-1-performance | src: book 1.2.1; p.7 | kind: concept

Performance can be measured in many ways, including transit time and response time.
Transit time is the amount of time required for a message to travel from one device to
another. Response time is the elapsed time between an inquiry and a response. The performance of a network depends on a number of factors, including the number of users,
the type of transmission medium, the capabilities of the connected hardware, and the
efficiency of the software.
Performance is often evaluated by two networking metrics: throughput and delay.
We often need more throughput and less delay. However, these two criteria are often
contradictory. If we try to send more data to the network, we may increase throughput
but we increase the delay because of traffic congestion in the network.

#### Reliability
> id: ch01-1-2-1-reliability | src: book 1.2.1; p.7 | kind: concept

In addition to accuracy of delivery, network reliability is measured by the frequency of
failure, the time it takes a link to recover from a failure, and the network’s robustness in
a catastrophe.

#### Security
> id: ch01-1-2-1-security | src: book 1.2.1; p.7 | kind: concept

Network security issues include protecting data from unauthorized access, protecting
data from damage and development, and implementing policies and procedures for
recovery from breaches and data losses.

### 1.2.2 Physical Structures
> id: ch01-1-2-2 | src: book 1.2.2; p.8 | kind: concept

Before discussing networks, we need to define some network attributes.

#### Type of Connection
> id: ch01-1-2-2-type-of-connection | src: book 1.2.2; p.8 | kind: concept

A network is two or more devices connected through links. A link is a communications
pathway that transfers data from one device to another. For visualization purposes, it is
simplest to imagine any link as a line drawn between two points. For communication to
occur, two devices must be connected in some way to the same link at the same time.
There are two possible types of connections: point-to-point and multipoint.

#### Point-to-Point
> id: ch01-1-2-2-point-to-point | src: book 1.2.2; p.8 | kind: concept

A point-to-point connection provides a dedicated link between two devices. The
entire capacity of the link is reserved for transmission between those two devices. Most
point-to-point connections use an actual length of wire or cable to connect the two
ends, but other options, such as microwave or satellite links, are also possible (see
Figure 1.3a). When we change television channels by infrared remote control, we are
establishing a point-to-point connection between the remote control and the television’s
control system.

#### Multipoint
> id: ch01-1-2-2-multipoint | src: book 1.2.2; p.8 | kind: concept

A multipoint (also called multidrop) connection is one in which more than two specific devices share a single link (see Figure 1.3b).

> **[ASSET ch01_ill_003]** Figure 1.3: Types of connections: point-to-point and multipoint
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_003.png
> - src: book Figure 1.3; p.9
> - shows: Figure 1.3: Types of connections: point-to-point and multipoint. Panel (a) connects exactly two laptops with one dedicated link. Panel (b) connects a mainframe and multiple computers to the same horizontal shared link.
> - structure: Panel (a) connects exactly two laptops with one dedicated link. Panel (b) connects a mainframe and multiple computers to the same horizontal shared link.
> - text_in_image: Link; a. Point-to-point; Link; Mainframe; b. Multipoint
> - use_when: Teach ch01-1-2-2-multipoint, explain Figure 1.3, or solve its linked practice questions.
> - confidence: high

In a multipoint environment, the capacity of the channel is shared, either spatially
or temporally. If several devices can use the link simultaneously, it is a spatially shared
connection. If users must take turns, it is a timeshared connection.

#### Physical Topology
> id: ch01-1-2-2-physical-topology | src: book 1.2.2; p.8 | kind: concept

The term physical topology refers to the way in which a network is laid out physically.
Two or more devices connect to a link; two or more links form a topology. The topology
of a network is the geometric representation of the relationship of all the links and
linking devices (usually called nodes) to one another. There are four basic topologies
possible: mesh, star, bus, and ring.

#### Mesh Topology
> id: ch01-1-2-2-mesh-topology | src: book 1.2.2; p.8 | kind: concept

In a mesh topology, every device has a dedicated point-to-point link to every other
device. The term dedicated means that the link carries traffic only between the two
devices it connects. To find the number of physical links in a fully connected mesh network with n nodes, we first consider that each node must be connected to every other
node. Node 1 must be connected to $n-1$ nodes, node 2 must be connected to $n-1$
nodes, and finally node n must be connected to $n-1$ nodes. We need $n(n-1)$ physical
links. However, if each physical link allows communication in both directions (duplex
mode), we can divide the number of links by 2. In other words, we can say that in a mesh
topology, we need  $n(n-1)/2$  duplex-mode links.  To accommodate that many links,
every device on the network must have $n-1$ input/output (I/O) ports (see Figure 1.4) to
be connected to the other $n-1$ stations.
A mesh offers several advantages over other network topologies. First, the use of
dedicated links guarantees that each connection can carry its own data load, thus eliminating the traffic problems that can occur when links must be shared by multiple
devices. Second, a mesh topology is robust. If one link becomes unusable, it does not
incapacitate the entire system. Third, there is the advantage of privacy or security. When
every message travels along a dedicated line, only the intended recipient sees it. Physical
boundaries prevent other users from gaining access to messages. Finally, point-to-point
links make fault identification and fault isolation easy. Traffic can be routed to avoid
links with suspected problems. This facility enables the network manager to discover the
precise location of the fault and aids in finding its cause and solution.

> **[ASSET ch01_ill_004]** Figure 1.4: A fully connected mesh topology (five devices)
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_004.png
> - src: book Figure 1.4; p.10
> - shows: Figure 1.4: A fully connected mesh topology (five devices). Five computers form a complete mesh. Every computer has a direct link to the other four; the diagram explicitly labels n = 5 and 10 links.
> - structure: Five computers form a complete mesh. Every computer has a direct link to the other four; the diagram explicitly labels n = 5 and 10 links.
> - text_in_image: n = 5; 10 links.
> - use_when: Teach ch01-1-2-2-mesh-topology, explain Figure 1.4, or solve its linked practice questions.
> - confidence: high

The main disadvantages of a mesh are related to the amount of cabling and the
number of I/O ports required. First, because every device must be connected to every
other device, installation and reconnection are difficult. Second, the sheer bulk of the
wiring can be greater than the available space (in walls, ceilings, or floors) can accommodate. Finally, the hardware required to connect each link (I/O ports and cable) can be
prohibitively expensive. For these reasons a mesh topology is usually implemented in a
limited fashion, for example, as a backbone connecting the main computers of a hybrid
network that can include several other topologies.
One practical example of a mesh topology is the connection of telephone regional
offices in which each regional office needs to be connected to every other regional
office.

#### Star Topology
> id: ch01-1-2-2-star-topology | src: book 1.2.2; p.8 | kind: concept

In a star topology, each device has a dedicated point-to-point link only to a central controller, usually called a hub. The devices are not directly linked to one another. Unlike a
mesh topology, a star topology does not allow direct traffic between devices. The controller acts as an exchange: If one device wants to send data to another, it sends the
data to the controller, which then relays the data to the other connected device (see
Figure 1.5) .

> **[ASSET ch01_ill_005]** Figure 1.5: A star topology connecting four stations
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_005.png
> - src: book Figure 1.5; p.10
> - shows: Figure 1.5: A star topology connecting four stations. A central hub has four separate spokes, each ending at one station. There are no direct station-to-station links.
> - structure: A central hub has four separate spokes, each ending at one station. There are no direct station-to-station links.
> - text_in_image: Hub
> - use_when: Teach ch01-1-2-2-star-topology, explain Figure 1.5, or solve its linked practice questions.
> - confidence: high

A star topology is less expensive than a mesh topology. In a star, each device needs
only one link and one I/O port to connect it to any number of others. This factor also
makes it easy to install and reconfigure. Far less cabling needs to be housed, and
additions, moves, and deletions involve only one connection: between that device and
the hub.
Other advantages include robustness. If one link fails, only that link is affected. All
other links remain active. This factor also lends itself to easy fault identification and
fault isolation. As long as the hub is working, it can be used to monitor link problems
and bypass defective links.
One big disadvantage of a star topology is the dependency of the whole topology
on one single point, the hub. If the hub goes down, the whole system is dead.
Although a star requires far less cable than a mesh, each node must be linked to a
central hub. For this reason, often more cabling is required in a star than in some other
topologies (such as ring or bus).
The star topology is used in local-area networks (LANs), as we will see in Chapter 13.
High-speed LANs often use a star topology with a central hub.

#### Bus Topology
> id: ch01-1-2-2-bus-topology | src: book 1.2.2; p.8 | kind: concept

The preceding examples all describe point-to-point connections. A bus topology, on the
other hand, is multipoint. One long cable acts as a backbone to link all the devices in a
network (see Figure 1.6).

> **[ASSET ch01_ill_006]** Figure 1.6: A bus topology connecting three stations
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_006.png
> - src: book Figure 1.6; p.11
> - shows: Figure 1.6: A bus topology connecting three stations. One horizontal bus cable terminates at a cable end on each side. Three stations connect to the bus through separate drop lines and taps.
> - structure: One horizontal bus cable terminates at a cable end on each side. Three stations connect to the bus through separate drop lines and taps.
> - text_in_image: Drop line; Drop line; Drop line; Cable end; Cable end; Tap; Tap; Tap
> - use_when: Teach ch01-1-2-2-bus-topology, explain Figure 1.6, or solve its linked practice questions.
> - confidence: high

Nodes are connected to the bus cable by drop lines and taps. A drop line is a connection running between the device and the main cable. A tap is a connector that either
splices into the main cable or punctures the sheathing of a cable to create a contact with
the metallic core. As a signal travels along the backbone, some of its energy is transformed into heat. Therefore, it becomes weaker and weaker as it travels farther and farther. For this reason there is a limit on the number of taps a bus can support and on the
distance between those taps.
Advantages of a bus topology include ease of installation. Backbone cable can be
laid along the most efficient path, then connected to the nodes by drop lines of various
lengths. In this way, a bus uses less cabling than mesh or star topologies. In a star, for
example, four network devices in the same room require four lengths of cable reaching
all the way to the hub. In a bus, this redundancy is eliminated. Only the backbone cable
stretches through the entire facility. Each drop line has to reach only as far as the nearest point on the backbone.
Disadvantages include difficult reconnection and fault isolation. A bus is usually
designed to be optimally efficient at installation. It can therefore be difficult to add new
devices. Signal reflection at the taps can cause degradation in quality. This degradation
can be controlled by limiting the number and spacing of devices connected to a given
length of cable. Adding new devices may therefore require modification or replacement
of the backbone.
In addition, a fault or break in the bus cable stops all transmission, even between
devices on the same side of the problem. The damaged area reflects signals back in the
direction of origin, creating noise in both directions.
Bus topology was the one of the first topologies used in the design of early local-area networks. Traditional Ethernet LANs can use a bus topology, but they are less popular now for reasons we will discuss in Chapter 13.

#### Ring Topology
> id: ch01-1-2-2-ring-topology | src: book 1.2.2; p.8 | kind: concept

In a ring topology, each device has a dedicated point-to-point connection with only the
two devices on either side of it. A signal is passed along the ring in one direction, from
device to device, until it reaches its destination. Each device in the ring incorporates a
repeater. When a device receives a signal intended for another device, its repeater
regenerates the bits and passes them along (see Figure 1.7).

> **[ASSET ch01_ill_007]** Figure 1.7: A ring topology connecting six stations
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_007.png
> - src: book Figure 1.7; p.12
> - shows: Figure 1.7: A ring topology connecting six stations. Six stations attach through six repeaters placed around one closed ring. Each repeater connects to its two neighboring repeaters.
> - structure: Six stations attach through six repeaters placed around one closed ring. Each repeater connects to its two neighboring repeaters.
> - text_in_image: Repeater; Repeater; Repeater; Repeater; Repeater; Repeater
> - use_when: Teach ch01-1-2-2-ring-topology, explain Figure 1.7, or solve its linked practice questions.
> - confidence: high

A ring is relatively easy to install and reconfigure. Each device is linked to only its
immediate neighbors (either physically or logically). To add or delete a device requires
changing only two connections. The only constraints are media and traffic considerations (maximum ring length and number of devices). In addition, fault isolation is simplified. Generally, in a ring a signal is circulating at all times. If one device does not
receive a signal within a specified period, it can issue an alarm. The alarm alerts the
network operator to the problem and its location.
However, unidirectional traffic can be a disadvantage. In a simple ring, a break in
the ring (such as a disabled station) can disable the entire network. This weakness can
be solved by using a dual ring or a switch capable of closing off the break.
Ring topology was prevalent when IBM introduced its local-area network, Token
Ring. Today, the need for higher-speed LANs has made this topology less popular.

## 1.3 NETWORK TYPES
> id: ch01-1-3 | src: book 1.3; p.13 | kind: concept

After defining networks in the previous section and discussing their physical structures,
we need to discuss different types of networks we encounter in the world today. The criteria of distinguishing one type of network from another is difficult and sometimes confusing. We use a few criteria such as size, geographical coverage, and ownership to make this
distinction. After discussing two types of networks, LANs and WANs, we define switching, which is used to connect networks to form an  internetwork (a network of networks).

### 1.3.1 Local Area Network
> id: ch01-1-3-1 | src: book 1.3.1; p.13 | kind: concept

A local area network (LAN) is usually privately owned and connects some hosts in a
single office, building, or campus. Depending on the needs of an organization, a LAN
can be as simple as two PCs and a printer in someone’s home office, or it can extend
throughout a company and include audio and video devices. Each host in a LAN has an
identifier, an address, that uniquely defines the host in the LAN. A packet sent by a host
to another host carries both the source host’s and the destination host’s addresses.
In the past, all hosts in a network were connected through a common cable, which
meant that a packet sent from one host to another was received by all hosts. The intended
recipient kept the packet; the others dropped the packet. Today, most LANs use a smart
connecting switch, which is able to recognize the destination address of the packet and
guide the packet to its destination without sending it to all other hosts. The switch alleviates the traffic in the LAN and allows more than one pair to communicate with each
other at the same time if there is no common source and destination among them. Note
that the above definition of a LAN does not define the minimum or maximum number of
hosts in a LAN. Figure 1.8 shows a LAN using either a common cable or a switch.

> **[ASSET ch01_ill_008]** Figure 1.8: An isolated LAN in the past and today
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_008.png
> - src: book Figure 1.8; p.13
> - shows: Figure 1.8: An isolated LAN in the past and today. Panel (a) places eight hosts, Host 1 through Host 8, along one common cable with taps and cable ends. Panel (b) connects the same eight host labels separately to one switch. The legend identifies hosts, a switch, a cable tap, a cable end, the common cable, and an individual connection.
> - structure: Panel (a) places eight hosts, Host 1 through Host 8, along one common cable with taps and cable ends. Panel (b) connects the same eight host labels separately to one switch. The legend identifies hosts, a switch, a cable tap, a cable end, the common cable, and an individual connection.
> - text_in_image: Host 1; Host 2; Host 3; Host 4; Host 5; Host 6; Host 7; Host 8; a. LAN with a common cable (past); Legend; Host 1; Host 2; Host 3; Host 4; A host (of any type); A switch; A cable tap; A cable end; Switch; The common cable; A connection; Host 5; Host 6; Host 7; Host 8; b. LAN with a switch (today)
> - use_when: Teach ch01-1-3-1, explain Figure 1.8, or solve its linked practice questions.
> - confidence: high

LANs are discussed in more detail in Part III of the book.

When LANs were used in isolation (which is rare today), they were designed to allow
resources to be shared between the hosts. As we will see shortly, LANs today are connected
to each other and to WANs (discussed next) to create communication at a wider level.

### 1.3.2 Wide Area Network
> id: ch01-1-3-2 | src: book 1.3.2; p.14 | kind: concept

A wide area network (WAN) is also an interconnection of devices capable of communication. However, there are some differences between a LAN and a WAN. A LAN is normally
limited in size, spanning an office, a building, or a campus; a WAN has a wider geographical span, spanning a town, a state, a country, or even the world. A LAN interconnects hosts;
a WAN interconnects connecting devices such as switches, routers, or modems. A LAN is
normally privately owned by the organization that uses it; a WAN is normally created and
run by communication companies and leased by an organization that uses it. We see two
distinct examples of WANs today: point-to-point WANs and switched WANs.

#### Point-to-Point WAN
> id: ch01-1-3-2-point-to-point-wan | src: book 1.3.2; p.14 | kind: concept

A point-to-point WAN is a network that connects two communicating devices through a transmission media (cable or air). We will see examples of these WANs when we discuss how to
connect the networks to one another. Figure 1.9 shows an example of a point-to-point WAN.

> **[ASSET ch01_ill_009]** Figure 1.9: A point-to-point WAN
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_009.png
> - src: book Figure 1.9; p.14
> - shows: Figure 1.9: A point-to-point WAN. Two connecting devices are joined by a single connecting medium, with each device leading outward to another network. The legend distinguishes the connecting device from the medium.
> - structure: Two connecting devices are joined by a single connecting medium, with each device leading outward to another network. The legend distinguishes the connecting device from the medium.
> - text_in_image: A connecting device; Legend; Connecting medium; To another; To another; network; network
> - use_when: Teach ch01-1-3-2-point-to-point-wan, explain Figure 1.9, or solve its linked practice questions.
> - confidence: high

#### Switched WAN
> id: ch01-1-3-2-switched-wan | src: book 1.3.2; p.14 | kind: concept

A switched WAN is a network with more than two ends. A switched WAN, as we will
see shortly, is used in the backbone of global communication today. We can say that a
switched WAN is a combination of several point-to-point WANs that are connected by
switches. Figure 1.10 shows an example of a switched WAN.

> **[ASSET ch01_ill_010]** Figure 1.10: A switched WAN
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_010.png
> - src: book Figure 1.10; p.14
> - shows: Figure 1.10: A switched WAN. Four switches form a rectangular switched WAN with horizontal and vertical connecting media. Each switch also has an outward link labeled To another network. The legend identifies a switch and a connecting medium.
> - structure: Four switches form a rectangular switched WAN with horizontal and vertical connecting media. Each switch also has an outward link labeled To another network. The legend identifies a switch and a connecting medium.
> - text_in_image: To another; To another; network; network; To another; To another; Legend; network; network; A switch; Connecting medium; To another; To another; network; network; To another; To another; network; network
> - use_when: Teach ch01-1-3-2-switched-wan, explain Figure 1.10, or solve its linked practice questions.
> - confidence: high

WANs are discussed in more detail in Part II of the book.

#### Internetwork
> id: ch01-1-3-2-internetwork | src: book 1.3.2; p.14 | kind: concept

Today, it is very rare to see a LAN or a WAN in isolation; they are connected to one
another. When two or more networks are connected, they make an internetwork, or
internet. As an example, assume that an organization has two offices, one on the east
coast and the other on the west coast. Each office has a LAN that allows all employees in
the office to communicate with each other. To make the communication between employees at different offices possible, the management leases a point-to-point dedicated WAN
from a service provider, such as a telephone company, and connects the two LANs. Now
the company has an internetwork, or a private internet (with lowercase i). Communication
between offices is now possible. Figure 1.11 shows this internet.

> **[ASSET ch01_ill_011]** Figure 1.11: An internetwork made of two LANs and one point-to-point WAN
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_011.png
> - src: book Figure 1.11; p.15
> - shows: Figure 1.11: An internetwork made of two LANs and one point-to-point WAN. A west-coast office LAN connects to router R1. A point-to-point WAN connects R1 to R2. Router R2 connects to an east-coast office LAN; the two LANs and the WAN form one internetwork.
> - structure: A west-coast office LAN connects to router R1. A point-to-point WAN connects R1 to R2. Router R2 connects to an east-coast office LAN; the two LANs and the WAN form one internetwork.
> - text_in_image: Point-to-point; R1; R2; WAN; Router; Router; LAN; LAN; West coast office; East coast office
> - use_when: Teach ch01-1-3-2-internetwork, explain Figure 1.11, or solve its linked practice questions.
> - confidence: high

When a host in the west coast office sends a message to another host in the same
office, the router blocks the message, but the switch directs the message to the destination.
On the other hand, when a host on the west coast sends a message to a host on the east
coast, router R1 routes the packet to router R2, and the packet reaches the destination.
Figure 1.12 (see next page) shows another internet with several LANs and WANs
connected. One of the WANs is a switched WAN with four switches.

### 1.3.3 Switching
> id: ch01-1-3-3 | src: book 1.3.3; p.15 | kind: concept

An internet is a switched network in which a switch connects at least two links
together. A switch needs to forward data from a network to another network when
required. The two most common types of switched networks are circuit-switched and
packet-switched networks. We discuss both next.

#### Circuit-Switched Network
> id: ch01-1-3-3-circuit-switched-network | src: book 1.3.3; p.15 | kind: concept

In a circuit-switched network, a dedicated connection, called a circuit, is always
available between the two end systems; the switch can only make it active or inactive.
Figure 1.13 shows a very simple switched network that connects four telephones to
each end. We have used telephone sets instead of computers as an end system because
circuit switching was very common in telephone networks in the past, although part of
the telephone network today is a packet-switched network.
In Figure 1.13, the four telephones at each side are connected to a switch. The
switch connects a telephone set at one side to a telephone set at the other side. The thick

> **[ASSET ch01_ill_012]** Figure 1.12: A heterogeneous network made of four WANs and three LANs
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_012.png
> - src: book Figure 1.12; p.16
> - shows: Figure 1.12: A heterogeneous network made of four WANs and three LANs. A heterogeneous internetwork combines four WANs and three LANs. A resident reaches a switched WAN through two modems and a point-to-point WAN. Routers connect the switched WAN to two further point-to-point WANs leading to LANs. LANs contain a switch and hosts.
> - structure: A heterogeneous internetwork combines four WANs and three LANs. A resident reaches a switched WAN through two modems and a point-to-point WAN. Routers connect the switched WAN to two further point-to-point WANs leading to LANs. LANs contain a switch and hosts.
> - text_in_image: Point-to-point; Modem; Modem; WAN; Resident; Switched WAN; Router; Point-to-point; WAN; Router; Router; Point-to-point; WAN; LAN; Router; LAN
> - use_when: Teach ch01-1-3-3-circuit-switched-network, explain Figure 1.12, or solve its linked practice questions.
> - confidence: high

> **[ASSET ch01_ill_013]** Figure 1.13: A circuit-switched network
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_013.png
> - src: book Figure 1.13; p.16
> - shows: Figure 1.13: A circuit-switched network. Four telephone endpoints on each side connect to a local switch over low-capacity lines. The two switches are joined by one high-capacity line. The legend distinguishes thin low-capacity from thick high-capacity lines.
> - structure: Four telephone endpoints on each side connect to a local switch over low-capacity lines. The two switches are joined by one high-capacity line. The legend distinguishes thin low-capacity from thick high-capacity lines.
> - text_in_image: Low-capacity line; High-capacity line; Switch; Switch
> - use_when: Teach ch01-1-3-3-circuit-switched-network, explain Figure 1.13, or solve its linked practice questions.
> - confidence: high

line connecting two switches is a high-capacity communication line that can handle
four voice communications at the same time; the capacity can be shared between all
pairs of telephone sets. The switches used in this example have forwarding tasks but no
storing capability.
Let us look at two cases. In the first case, all telephone sets are busy; four people at
one site are talking with four people at the other site; the capacity of the thick line is
fully used. In the second case, only one telephone set at one side is connected to a telephone set at the other side; only one-fourth of the capacity of the thick line is used. This
means that a circuit-switched network is efficient only when it is working at its full
capacity; most of the time, it is inefficient because it is working at partial capacity. The
reason that we need to make the capacity of the thick line four times the capacity of
each voice line is that we do not want communication to fail when all telephone sets at
one side want to be connected with all telephone sets at the other side.

#### Packet-Switched Network
> id: ch01-1-3-3-packet-switched-network | src: book 1.3.3; p.15 | kind: concept

In a computer network, the communication between the two ends is done in blocks of
data called packets. In other words, instead of the continuous communication we see
between two telephone sets when they are being used, we see the exchange of individual data packets between the two computers. This allows us to make the switches function for both storing and forwarding because a packet is an independent entity that can
be stored and sent later. Figure 1.14 shows a small packet-switched network that connects four computers at one site to four computers at the other site.

> **[ASSET ch01_ill_014]** Figure 1.14: A packet-switched network
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_014.png
> - src: book Figure 1.14; p.17
> - shows: Figure 1.14: A packet-switched network. Four computer endpoints on each side connect to a router through low-capacity links. A high-capacity link joins the routers. Queues and opposing packet arrows illustrate traffic buffered and forwarded through the routers.
> - structure: Four computer endpoints on each side connect to a router through low-capacity links. A high-capacity link joins the routers. Queues and opposing packet arrows illustrate traffic buffered and forwarded through the routers.
> - text_in_image: Low-capacity line; High-capacity line; Queue; Queue; Router; Router
> - use_when: Teach ch01-1-3-3-packet-switched-network, explain Figure 1.14, or solve its linked practice questions.
> - confidence: high

A router in a packet-switched network has a queue that can store and forward the
packet. Now assume that the capacity of the thick line is only twice the capacity of the
data line connecting the computers to the routers. If only two computers (one at each
site) need to communicate with each other, there is no waiting for the packets.
However, if packets arrive at one router when the thick line is already working at its full
capacity, the packets should be stored and forwarded in the order they arrived. The two
simple examples show that a packet-switched network is more efficient than a circuit-switched network, but the packets may encounter some delays.
In this book, we mostly discuss packet-switched networks. In Chapter 18, we discuss
packet-switched networks in more detail and discuss the performance of these networks.

### 1.3.4 The Internet
> id: ch01-1-3-4 | src: book 1.3.4; p.17 | kind: concept

As we discussed before, an internet (note the lowercase i) is two or more networks that
can communicate with each other. The most notable internet is called the Internet
(uppercase I ), and is composed of thousands of interconnected networks. Figure 1.15
shows a conceptual (not geographical) view of the Internet.
The figure shows the Internet as several backbones, provider networks, and customer networks. At the top level, the backbones are large networks owned by some
communication companies such as Sprint, Verizon (MCI), AT&T, and NTT. The backbone networks are connected through some complex switching systems, called peering
points. At the second level, there are smaller networks, called provider networks, that
use the services of the backbones for a fee. The provider networks are connected to
backbones and sometimes to other provider networks. The customer networks are

> **[ASSET ch01_ill_015]** Figure 1.15: The Internet today
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_015.png
> - src: book Figure 1.15; p.18
> - shows: Figure 1.15: The Internet today. Customer networks connect to provider networks. Multiple provider networks connect to overlapping backbone networks in the center. Peering points appear to the left and right of the backbone group; repeated customer and provider groups illustrate the larger Internet hierarchy.
> - structure: Customer networks connect to provider networks. Multiple provider networks connect to overlapping backbone networks in the center. Peering points appear to the left and right of the backbone group; repeated customer and provider groups illustrate the larger Internet hierarchy.
> - text_in_image: Customer; Customer; Customer; Customer; network; network; network; network; Provider; Provider; network; network; Peering; point; Peering; point; Backbones; Provider; Provider; Provider; network; network; network; Customer; Customer; Customer; Customer; Customer; Customer; network; network; network; network; network; network
> - use_when: Teach ch01-1-3-4, explain Figure 1.15, or solve its linked practice questions.
> - confidence: high

networks at the edge of the Internet that actually use the services provided by the Internet. They pay fees to provider networks for receiving services.
Backbones and provider networks are also called Internet Service Providers
(ISPs). The backbones are often referred to as international ISPs; the provider networks are often referred to as national or regional ISPs.

### 1.3.5 Accessing the Internet
> id: ch01-1-3-5 | src: book 1.3.5; p.18 | kind: concept

The Internet today is an internetwork that allows any user to become part of it. The
user, however, needs to be physically connected to an ISP. The physical connection is
normally done through a point-to-point WAN. In this section, we briefly describe
how this can happen, but we postpone the technical details of the connection until
Chapters 14 and 16.

#### Using Telephone Networks
> id: ch01-1-3-5-using-telephone-networks | src: book 1.3.5; p.18 | kind: concept

Today most residences and small businesses have telephone service, which means
they are connected to a telephone network. Since most telephone networks have
already connected themselves to the Internet, one option for residences and small
businesses to connect to the Internet is to change the voice line between the residence
or business and the telephone center to a point-to-point WAN. This can be done in
two ways.

- Dial-up service. The first solution is to add to the telephone line a modem that
converts data to voice. The software installed on the computer dials the ISP and
imitates making a telephone connection. Unfortunately, the dial-up service is
very slow, and when the line is used for Internet connection, it cannot be used for
telephone (voice) connection. It is only useful for small residences. We discuss
dial-up service in Chapter 14.

- DSL Service. Since the advent of the Internet, some telephone companies have
upgraded their telephone lines to provide higher speed Internet services to residences or small businesses. The DSL service also allows the line to be used simultaneously for voice and data communication. We discuss DSL in Chapter 14.

#### Using Cable Networks
> id: ch01-1-3-5-using-cable-networks | src: book 1.3.5; p.18 | kind: concept

More and more residents over the last two decades have begun using cable TV services
instead of antennas to receive TV broadcasting. The cable companies have been
upgrading their cable networks and connecting to the Internet. A residence or a small
business can be connected to the Internet by using this service. It provides a higher
speed connection, but the speed varies depending on the number of neighbors that use
the same cable. We discuss the cable networks in Chapter 14.

#### Using Wireless Networks
> id: ch01-1-3-5-using-wireless-networks | src: book 1.3.5; p.18 | kind: concept

Wireless connectivity has recently become increasingly popular. A household or a
small business can use a combination of wireless and wired connections to access the
Internet. With the growing wireless WAN access, a household or a small business can
be connected to the Internet through a wireless WAN. We discuss wireless access in
Chapter 16.

#### Direct Connection to the Internet
> id: ch01-1-3-5-direct-connection-to-the-internet | src: book 1.3.5; p.18 | kind: concept

A large organization or a large corporation can itself become a local ISP and be connected to the Internet. This can be done if the organization or the corporation leases a
high-speed WAN from a carrier provider and connects itself to a regional ISP. For
example, a large university with several campuses can create an internetwork and then
connect the internetwork to the Internet.

## 1.4 INTERNET HISTORY
> id: ch01-1-4 | src: book 1.4; p.19 | kind: concept

Now that we have given an overview of the Internet, let us give a brief history of the
Internet. This brief history makes it clear how the Internet has evolved from a private
network to a global one in less than 40 years.

### 1.4.1 Early History
> id: ch01-1-4-1 | src: book 1.4.1; p.19 | kind: concept

There were some communication networks, such as telegraph and telephone networks,
before 1960. These networks were suitable for constant-rate communication at that time,
which means that after a connection was made between two users, the encoded message
(telegraphy) or voice (telephony) could be exchanged. A computer network, on the other
hand, should be able to handle bursty data, which means data received at variable rates at
different times. The world needed to wait for the packet-switched network to be invented.

#### Birth of Packet-Switched Networks
> id: ch01-1-4-1-birth-of-packet-switched-networks | src: book 1.4.1; p.19 | kind: concept

The theory of packet switching for bursty traffic was first presented by Leonard
Kleinrock in 1961 at MIT. At the same time, two other researchers, Paul Baran at Rand
Institute and Donald Davies at National Physical Laboratory in England, published
some papers about packet-switched networks.

#### ARPANET
> id: ch01-1-4-1-arpanet | src: book 1.4.1; p.19 | kind: concept

In the mid-1960s, mainframe computers in research organizations were stand-alone
devices. Computers from different manufacturers were unable to communicate with
one another. The Advanced Research Projects Agency (ARPA) in the Department of
Defense (DOD) was interested in finding a way to connect computers so that the
researchers they funded could share their findings, thereby reducing costs and eliminating duplication of effort.
In 1967, at an Association for Computing Machinery (ACM) meeting, ARPA presented its ideas for the Advanced Research Projects Agency Network (ARPANET),
a small network of connected computers. The idea was that each host computer (not
necessarily from the same manufacturer) would be attached to a specialized computer,
called an interface message processor (IMP). The IMPs, in turn, would be connected to
each other. Each IMP had to be able to communicate with other IMPs as well as with its
own attached host.
By 1969, ARPANET was a reality. Four nodes, at the University of California at
Los Angeles (UCLA), the University of California at Santa Barbara (UCSB), Stanford
Research Institute (SRI), and the University of Utah, were connected via the IMPs to
form a network. Software called the Network Control Protocol (NCP) provided communication between the hosts.

### 1.4.2 Birth of the Internet
> id: ch01-1-4-2 | src: book 1.4.2; p.20 | kind: concept

In 1972, Vint Cerf and Bob Kahn, both of whom were part of the core ARPANET
group, collaborated on what they called the Internetting Project. They wanted to link
dissimilar networks so that a host on one network could communicate with a host on
another. There were many problems to overcome: diverse packet sizes, diverse interfaces, and diverse transmission rates, as well as differing reliability requirements. Cerf
and Kahn devised the idea of a device called a gateway to serve as the intermediary
hardware to transfer data from one network to another.

#### TCP/IP
> id: ch01-1-4-2-tcp-ip | src: book 1.4.2; p.20 | kind: concept

Cerf and Kahn’s landmark 1973 paper outlined the protocols to achieve end-to-end
delivery of data. This was a new version of NCP. This paper on transmission control
protocol (TCP) included concepts such as encapsulation, the datagram, and the functions of a gateway. A radical idea was the transfer of responsibility for error correction
from the IMP to the host machine. This ARPA Internet now became the focus of the
communication effort. Around this time, responsibility for the ARPANET was handed
over to the Defense Communication Agency (DCA).
In October 1977, an internet consisting of three different networks (ARPANET,
packet radio, and packet satellite) was successfully demonstrated. Communication
between networks was now possible.
Shortly thereafter, authorities made a decision to split TCP into two protocols: Transmission Control Protocol (TCP) and Internet Protocol (IP). IP would handle datagram
routing while TCP would be responsible for higher level functions such as segmentation,
reassembly, and error detection. The new combination became known as TCP/IP.
In 1981, under a Defence Department contract, UC Berkeley modified the UNIX
operating system to include TCP/IP. This inclusion of network software along with a
popular operating system did much for the popularity of internetworking. The open
(non-manufacturer-specific) implementation of the Berkeley UNIX gave every manufacturer a working code base on which they could build their products.
In 1983, authorities abolished the original ARPANET protocols, and TCP/IP
became the official protocol for the ARPANET. Those who wanted to use the Internet
to access a computer on a different network had to be running TCP/IP.

#### MILNET
> id: ch01-1-4-2-milnet | src: book 1.4.2; p.20 | kind: concept

In 1983, ARPANET split into two networks: Military Network (MILNET) for military
users and ARPANET for nonmilitary users.

#### CSNET
> id: ch01-1-4-2-csnet | src: book 1.4.2; p.20 | kind: concept

Another milestone in Internet history was the creation of CSNET in 1981. Computer
Science Network (CSNET) was a network sponsored by the National Science Foundation (NSF). The network was conceived by universities that were ineligible to join
ARPANET due to an absence of ties to the Department of Defense. CSNET was a less
expensive network; there were no redundant links and the transmission rate was slower.
By the mid-1980s, most U.S. universities with computer science departments were
part of CSNET. Other institutions and companies were also forming their own networks and using TCP/IP to interconnect. The term Internet, originally associated with
government-funded connected networks, now referred to the connected networks using
TCP/IP protocols.

#### NSFNET
> id: ch01-1-4-2-nsfnet | src: book 1.4.2; p.20 | kind: concept

With the success of CSNET, the NSF in 1986 sponsored the National Science Foundation Network (NSFNET), a backbone that connected five supercomputer centers
located throughout the United States. Community networks were allowed access to this
backbone, a T-1 line (see Chapter 6) with a 1.544-Mbps data rate, thus providing connectivity throughout the United States. In 1990, ARPANET was officially retired and
replaced by NSFNET. In 1995, NSFNET reverted back to its original concept of a
research network.

#### ANSNET
> id: ch01-1-4-2-ansnet | src: book 1.4.2; p.20 | kind: concept

In 1991, the U.S. government decided that NSFNET was not capable of supporting the
rapidly increasing Internet traffic. Three companies, IBM, Merit, and Verizon, filled the
void by forming a nonprofit organization called Advanced Network & Services (ANS)
to build a new, high-speed Internet backbone called Advanced Network Services
Network (ANSNET).

### 1.4.3 Internet Today
> id: ch01-1-4-3 | src: book 1.4.3; p.22 | kind: concept

Today, we witness a rapid growth both in the infrastructure and new applications. The
Internet today is a set of pier networks that provide services to the whole world. What
has made the Internet so popular is the invention of new applications.

#### World Wide Web
> id: ch01-1-4-3-world-wide-web | src: book 1.4.3; p.22 | kind: concept

The 1990s saw the explosion of Internet applications due to the emergence of the World
Wide Web (WWW). The Web was invented at CERN by Tim Berners-Lee. This invention has added the commercial applications to the Internet.

#### Multimedia
> id: ch01-1-4-3-multimedia | src: book 1.4.3; p.22 | kind: concept

Recent developments in the multimedia applications such as voice over IP (telephony),
video over IP (Skype), view sharing (YouTube), and television over IP (PPLive) has
increased the number of users and the amount of time each user spends on the network.
We discuss multimedia in Chapter 28.

#### Peer-to-Peer Applications
> id: ch01-1-4-3-peer-to-peer-applications | src: book 1.4.3; p.22 | kind: concept

Peer-to-peer networking is also a new area of communication with a lot of potential.
We introduce some peer-to-peer applications in Chapter 29.

## 1.5 STANDARDS AND ADMINISTRATION
> id: ch01-1-5 | src: book 1.5; p.22 | kind: concept

In the discussion of the Internet and its protocol, we often see a reference to a standard
or an administration entity. In this section, we introduce these standards and administration entities for those readers that are not familiar with them; the section can be
skipped if the reader is familiar with them.

### 1.5.1 Internet Standards
> id: ch01-1-5-1 | src: book 1.5.1; p.22 | kind: concept

An Internet standard is a thoroughly tested specification that is useful to and adhered to
by those who work with the Internet. It is a formalized regulation that must be followed.
There is a strict procedure by which a specification attains Internet standard status. A specification begins as an Internet draft. An Internet draft is a working document (a work in
progress) with no official status and a six-month lifetime. Upon recommendation from the
Internet authorities, a draft may be published as a Request for Comment (RFC). Each
RFC is edited, assigned a number, and made available to all interested parties. RFCs go
through maturity levels and are categorized according to their requirement level.

#### Maturity Levels
> id: ch01-1-5-1-maturity-levels | src: book 1.5.1; p.22 | kind: concept

An RFC, during its lifetime, falls into one of six maturity levels: proposed standard, draft
standard, Internet standard, historic, experimental, and informational (see  Figure 1.16).

- Proposed Standard. A proposed standard is a specification that is stable, well
understood, and of sufficient interest to the Internet community. At this level, the
specification is usually tested and implemented by several different groups.

> **[ASSET ch01_ill_016]** Figure 1.16: Maturity levels of an RFC
> - type: illustration
> - kind: flow
> - file: assets/ch01_ill_016.png
> - src: book Figure 1.16; p.23
> - shows: Figure 1.16: Maturity levels of an RFC. Internet draft is at the top. A central downward progression passes through proposed standard, draft standard, and Internet standard, with labels Six months and two tries and Four months and two tries. Experimental and informational branches appear on the sides, and historic is at the bottom. This is the maturity model shown in the 2013 textbook.
> - structure: Internet draft is at the top. A central downward progression passes through proposed standard, draft standard, and Internet standard, with labels Six months and two tries and Four months and two tries. Experimental and informational branches appear on the sides, and historic is at the bottom. This is the maturity model shown in the 2013 textbook.
> - text_in_image: Internet draft; Proposed standard; Experimental; Informational; Six months and two tries; Draft standard; Four months and two tries; Internet standard; Historic
> - use_when: Teach ch01-1-5-1-maturity-levels, explain Figure 1.16, or solve its linked practice questions.
> - confidence: high

- Draft Standard. A proposed standard is elevated to draft standard status after at
least two successful independent and interoperable implementations. Barring difficulties, a draft standard, with modifications if specific problems are encountered,
normally becomes an Internet standard.

- Internet Standard. A draft standard reaches Internet standard status after demonstrations of successful implementation.

- Historic. The historic RFCs are significant from a historical perspective. They
either have been superseded by later specifications or have never passed the necessary maturity levels to become an Internet standard.

- Experimental. An RFC classified as experimental describes work related to an
experimental situation that does not affect the operation of the Internet. Such an
RFC should not be implemented in any functional Internet service.

- Informational. An RFC classified as informational contains general, historical, or
tutorial information related to the Internet. It is usually written by someone in a
non-Internet organization, such as a vendor.

#### Requirement Levels
> id: ch01-1-5-1-requirement-levels | src: book 1.5.1; p.22 | kind: concept

RFCs are classified into five requirement levels: required, recommended, elective, limited use, and not recommended.

- Required. An RFC is labeled required if it must be implemented by all Internet
systems to achieve minimum conformance. For example, IP and ICMP (Chapter 19)
are required protocols.

- Recommended. An RFC labeled recommended is not required for minimum
conformance; it is recommended because of its usefulness. For example, FTP
(Chapter 26) and TELNET (Chapter 26) are recommended protocols.

- Elective. An RFC labeled elective is not required and not recommended. However,
a system can use it for its own benefit.
- Limited Use. An RFC labeled limited use should be used only in limited situations.
Most of the experimental RFCs fall under this category.

- Not Recommended. An RFC labeled not recommended is inappropriate for general use. Normally a historic (deprecated) RFC may fall under this category.

RFCs can be found at http://www.rfc-editor.org.

### 1.5.2 Internet Administration
> id: ch01-1-5-2 | src: book 1.5.2; p.24 | kind: concept

The Internet, with its roots primarily in the research domain, has evolved and gained
a broader user base with significant commercial activity. Various groups that coordinate
Internet issues have guided this growth and development. Appendix G gives the addresses,
e-mail addresses, and telephone numbers for some of these groups. Figure 1.17
shows the general organization of Internet administration.

> **[ASSET ch01_ill_017]** Figure 1.17: Internet administration
> - type: illustration
> - kind: architecture_block
> - file: assets/ch01_ill_017.png
> - src: book Figure 1.17; p.24
> - shows: Figure 1.17: Internet administration. ISOC is above IAB. IAB branches to IRTF on the left and IETF on the right. IRTF contains IRSG above research groups (RG). IETF contains IESG above areas, which in turn contain working groups (WG). Ellipses indicate additional groups and areas.
> - structure: ISOC is above IAB. IAB branches to IRTF on the left and IETF on the right. IRTF contains IRSG above research groups (RG). IETF contains IESG above areas, which in turn contain working groups (WG). Ellipses indicate additional groups and areas.
> - text_in_image: ISOC; IAB; IRTF; IETF; IRSG; IESG; Area; Area; RG; RG; WG; WG; WG; WG; RG; RG
> - use_when: Teach ch01-1-5-2, explain Figure 1.17, or solve its linked practice questions.
> - confidence: high

#### ISOC
> id: ch01-1-5-2-isoc | src: book 1.5.2; p.24 | kind: concept

The Internet Society (ISOC) is an international, nonprofit organization formed in
1992 to provide support for the Internet standards process. ISOC accomplishes this
through maintaining and supporting other Internet administrative bodies such as IAB,
IETF, IRTF, and IANA (see the following sections). ISOC also promotes research and
other scholarly activities relating to the Internet.

#### IAB
> id: ch01-1-5-2-iab | src: book 1.5.2; p.24 | kind: concept

The Internet Architecture Board (IAB) is the technical advisor to the ISOC. The
main purposes of the IAB are to oversee the continuing development of the TCP/IP
Protocol Suite and to serve in a technical advisory capacity to research members of the
Internet community. IAB accomplishes this through its two primary components, the
Internet Engineering Task Force (IETF) and the Internet Research Task Force (IRTF).
Another responsibility of the IAB is the editorial management of the RFCs, described
earlier. IAB is also the external liaison between the Internet and other standards organizations and forums.

#### IETF
> id: ch01-1-5-2-ietf | src: book 1.5.2; p.24 | kind: concept

The Internet Engineering Task Force (IETF) is a forum of working groups managed
by the Internet Engineering Steering Group (IESG). IETF is responsible for identifying
operational problems and proposing solutions to these problems. IETF also develops
and reviews specifications intended as Internet standards. The working groups are collected into areas, and each area concentrates on a specific topic. Currently nine areas
have been defined. The areas include applications, protocols, routing, network management next generation (IPng), and security.

#### IRTF
> id: ch01-1-5-2-irtf | src: book 1.5.2; p.24 | kind: concept

The Internet Research Task Force (IRTF) is a forum of working groups managed by
the Internet Research Steering Group (IRSG). IRTF focuses on long-term research topics related to Internet protocols, applications, architecture, and technology.

## 1.6 END-CHAPTER MATERIALS
> id: ch01-1-6 | src: book 1.6; p.25 | kind: concept

### 1.6.1 Recommended Reading
> id: ch01-1-6-1 | src: book 1.6.1; p.25 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items enclosed in brackets [. . .] refer to the reference list at the end of the book.
#### Books
> id: ch01-1-6-1-books | src: book 1.6.1; p.25 | kind: concept
The introductory materials covered in this chapter can be found in [Sta04] and [PD03].
[Tan03] also discusses standardization.

### 1.6.2 Key Terms
> id: ch01-1-6-2 | src: book 1.6.2; p.25 | kind: concept

- Advanced Network Services Network (ANSNET)
- Advanced Research Projects Agency (ARPA)
- Advanced Research Projects Agency Network (ARPANET)
- American Standard Code for Information Interchange (ASCII)
- audio
- backbone
- Basic Latin
- bus topology
- circuit-switched network
- code
- Computer Science Network (CSNET)
- data
- data communications
- delay
- full-duplex mode
- half-duplex mode
- hub
- image
- internet
- Internet
- Internet Architecture Board (IAB)
- Internet draft
- Internet Engineering Task Force (IETF)
- Internet Research Task Force (IRTF)
- Internet Service Provider (ISP)
- Internet Society (ISOC)
- Internet standard
- internetwork
- local area network (LAN)
- mesh topology
- message
- Military Network (MILNET)
- multipoint or multidrop connection
- National Science Foundation Network (NSFNET)
- network
- node
- packet
- packet-switched network
- performance
- physical topology
- point-to-point connection
- protocol
- Request for Comment (RFC)
- RGB
- ring topology
- simplex mode
- star topology
- switched network
- TCP/IP protocol suite
- telecommunication
- throughput
- Transmission Control Protocol/ Internet Protocol (TCP/IP)
- transmission medium
- Unicode
- video
- wide area network (WAN)
- YCM

### 1.6.3 Summary
> id: ch01-1-6-3 | src: book 1.6.3; p.26 | kind: concept

Data communications are the transfer of data from one device to another via some form
of transmission medium. A data communications system must transmit data to the correct
destination in an accurate and timely manner. The five components that make up a data
communications system are the message, sender, receiver, medium, and protocol. Text,
numbers, images, audio, and video are different forms of information. Data flow between
two devices can occur in one of three ways: simplex, half-duplex, or full-duplex.
A network is a set of communication devices connected by media links. In a point-to-point connection, two and only two devices are connected by a dedicated link. In a
multipoint connection, three or more devices share a link. Topology refers to the physical
or logical arrangement of a network. Devices may be arranged in a mesh, star, bus, or
ring topology.
A network can be categorized as a local area network or a wide area network. A
LAN is a data communication system within a building, plant, or campus, or between
nearby buildings. A WAN is a data communication system spanning states, countries,
or the whole world. An internet is a network of networks. The Internet is a collection of
many separate networks.
The Internet history started with the theory of packet switching for bursty traffic.
The history continued when The ARPA was interested in finding a way to connect
computers so that the researchers they funded could share their findings, resulting in
the creation of ARPANET. The Internet was born when Cerf and Kahn devised the idea
of a device called a gateway to serve as the intermediary hardware to transfer data from
one network to another. The TCP/IP protocol suite paved the way for creation of
today’s Internet. The invention of WWW, the use of multimedia, and peer-to-peer communication helps the growth of the Internet.
An Internet standard is a thoroughly tested specification. An Internet draft is a
working document with no official status and a six-month lifetime. A draft may be
published as a Request for Comment (RFC). RFCs go through maturity levels and are
categorized according to their requirement level. The Internet administration has

evolved with the Internet. ISOC promotes research and activities. IAB is the technical
advisor to the ISOC. IETF is a forum of working groups responsible for operational
problems. IRTF is a forum of working groups focusing on long-term research topics.

## 1.7 PRACTICE SET
> id: ch01-1-7 | src: book 1.7; p.27 | kind: concept

### 1.7.1 Quizzes
> id: ch01-1-7-1 | src: book 1.7.1; p.27 | kind: concept

A set of interactive quizzes for this chapter can be found on the book website. It is
strongly recommended that the student take the quizzes to check his/her understanding
of the materials before continuing with the practice set.

## 1.8 SIMULATION EXPERIMENTS
> id: ch01-1-8 | src: book 1.8; p.28 | kind: concept

### 1.8.1 Applets
> id: ch01-1-8-1 | src: book 1.8.1; p.28 | kind: concept

One of the ways to show the network protocols in action or visually see the solution to
some examples is through the use of interactive animation. We have created some Java
applets to show some of the main concepts discussed in this chapter. It is strongly recommended that the students activate these applets on the book website and carefully
examine the protocols in action. However, note that applets have been created only for
some chapters, not all (see the book website).

### 1.8.2 Lab Assignments
> id: ch01-1-8-2 | src: book 1.8.2; p.28 | kind: concept

Experiments with networks and network equipment can be done using at least two
methods. In the first method, we can create an isolated networking laboratory and use

networking hardware and software to simulate the topics discussed in each chapter. We
can create an internet and send and receive packets from any host to another. The flow
of packets can be observed and the performance can be measured. Although the first
method is more effective and more instructional, it is expensive to implement and not
all institutions are ready to invest in such an exclusive laboratory.
In the second method, we can use the Internet, the largest network in the world, as
our virtual laboratory. We can send and receive packets using the Internet. The existence of some free-downloadable software allows us to capture and examine the packets exchanged. We can analyze the packets to see how theoretical aspects of networking
are put into action. Although the second method may not be as effective as the first
method, in that we cannot control and change the packet routes to see how the Internet
behaves, the method is much cheaper to implement. It does not need a physical networking lab; it can be implemented using our desktop or laptop. The required software
is also free to download.
There are many programs and utilities available for Windows and UNIX operating
systems that allow us to sniff, capture, trace, and analyze packets that are exchanged
between our computer and the Internet. Some of these, such as Wireshark and PingPlotter, have graphical user interface (GUI); others, such as traceroute, nslookup, dig,
ipconfig, and ifconfig, are network administration command-line utilities. Any of these
programs and utilities can be a valuable debugging tool for network administrators and
educational tool for computer network students.
In this book, we mostly use Wireshark for lab assignments, although we occasionally use other tools. It captures live packet data from a network interface and displays
them with detailed protocol information. Wireshark, however, is a passive analyzer. It
only “measures” things from the network without manipulating them; it doesn’t send
packets on the network or perform other active operations. Wireshark is not an intrusion detection tool either. It does not give warning about any network intrusion. It,
nevertheless, can help network administrators or network security engineers to figure
out what is going on inside a network and to troubleshoot network problems. In addition to being an indispensable tool for network administrators and security engineers,
Wireshark is a valuable tool for protocol developers, who may use it to debug protocol
implementations, and a great educational tool for computer networking students who
can use it to see details of protocol operations in real time. However, note that we can
use lab assignments only with a few chapters.
Lab1-1. In this lab assignment we learn how to download and install Wireshark. The
instructions for downloading and installing the software are posted on the
book website in the lab section for Chapter 1. In this document, we also discuss the general idea behind the software, the format of its window, and how
to use it. The full study of this lab prepares the student to use Wireshark in the
lab assignments for other chapters.
