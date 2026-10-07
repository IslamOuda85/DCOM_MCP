---
doc_type: scientific_content
course_id: data_communications
chapter: 2
chapter_id: data_communications_ch02
chapter_title: Network Models
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_2/ch2.pdf
  pages: 31-50
assets_dir: assets
asset_counts:
  illustration: 12
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-06T21:45:17+00:00'
status: complete
---
# Chapter 2: Network Models

## Chapter Objectives
> id: ch02-0 | src: book p.31 | kind: objectives

The second chapter is a preparation for the rest of the book. The next five parts of the
book is devoted to one of the layers in the TCP/IP protocol suite. In this chapter,
we first discuss the idea of network models in general and the TCP/IP protocol suite in
particular.
Two models have been devised to define computer network operations: the TCP/IP
protocol suite and the OSI model. In this chapter, we first discuss a general subject, protocol
layering, which is used in both models. We then concentrate on the TCP/IP protocol suite,
on which the book is based. The OSI model is briefly discuss for comparison with the
TCP/IP protocol suite.

- The first section introduces the concept of protocol layering using two scenarios.
The section also discusses the two principles upon which the protocol layering is
based. The first principle dictates that each layer needs to have two opposite tasks.
The second principle dictates that the corresponding layers should be identical.
The section ends with a brief discussion of logical connection between two identical layers in protocol layering. Throughout the book, we need to distinguish
between logical and physical connections.

- The second section discusses the five layers of the TCP/IP protocol suite. We show
how packets in each of the five layers (physical, data-link, network, transport, and
application) are named. We also mention the addressing mechanism used in each
layer. Each layer of the TCP/IP protocol suite is a subject of a part of the book. In
other words, each layer is discussed in several chapters; this section is just an introduction and preparation.

- The third section gives a brief discussion of the OSI model. This model was never
implemented in practice, but a brief discussion of the model and its comparison
with the TCP/IP protocol suite may be useful to better understand the TCP/IP protocol suite. In this section we also give a brief reason for the OSI model’s lack of
success.

## 2.1 PROTOCOL LAYERING
> id: ch02-2-1 | src: book 2.1; p.32 | kind: concept

We defined the term protocol in Chapter 1. In data communication and networking, a
protocol defines the rules that both the sender and receiver and all intermediate devices
need to follow to be able to communicate effectively. When communication is simple,
we may need only one simple protocol; when the communication is complex, we may
need to divide the task between different layers, in which case we need a protocol at
each layer, or protocol layering.

### 2.1.1 Scenarios
> id: ch02-2-1-1 | src: book 2.1.1; p.32 | kind: concept

Let us develop two simple scenarios to better understand the need for protocol layering.

#### First Scenario
> id: ch02-2-1-1-first-scenario | src: book p.32 | kind: concept

In the first scenario, communication is so simple that it can occur in only one layer.
Assume Maria and Ann are neighbors with a lot of common ideas. Communication
between Maria and Ann takes place in one layer, face to face, in the same language, as
shown in Figure 2.1.

> **[ASSET ch02_ill_001]** Figure 2.1: A single-layer protocol
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_001.png
> - src: book Figure 2.1; p.32
> - shows: Figure 2.1: A single-layer protocol. Maria and Ann each have one Layer 1 Listen/Talk block. A shared Air path connects the blocks; upward arrows indicate the physical sound path at each endpoint.
> - structure: Maria and Ann each have one Layer 1 Listen/Talk block. A shared Air path connects the blocks; upward arrows indicate the physical sound path at each endpoint.
> - text_in_image: Maria; Ann; Layer 1; Layer 1; Listen/Talk; Listen/Talk; Air
> - use_when: Teach ch02-2-1-1-first-scenario, explain Figure 2.1, or solve a linked practice question.
> - confidence: high

Even in this simple scenario, we can see that a set of rules needs to be followed.
First, Maria and Ann know that they should greet each other when they meet. Second,
they know that they should confine their vocabulary to the level of their friendship.
Third, each party knows that she should refrain from speaking when the other party
is speaking. Fourth, each party knows that the conversation should be a dialog, not a
monolog: both should have the opportunity to talk about the issue. Fifth, they should
exchange some nice words when they leave.
We can see that the protocol used by Maria and Ann is different from the communication between a professor and the students in a lecture hall. The communication in
the second case is mostly monolog; the professor talks most of the time unless a student
has a question, a situation in which the protocol dictates that she should raise her hand
and wait for permission to speak. In this case, the communication is normally very formal and limited to the subject being taught.

#### Second Scenario
> id: ch02-2-1-1-second-scenario | src: book p.32 | kind: concept

In the second scenario, we assume that Ann is offered a higher-level position in her
company, but needs to move to another branch located in a city very far from Maria.
The two friends still want to continue their communication and exchange ideas because
they have come up with an innovative project to start a new business when they both
retire. They decide to continue their conversation using regular mail through the post
office. However, they do not want their ideas to be revealed by other people if the letters are intercepted. They agree on an encryption/decryption technique. The sender of
the letter encrypts it to make it unreadable by an intruder; the receiver of the letter
decrypts it to get the original letter. We discuss the encryption/decryption methods in
Chapter 31, but for the moment we assume that Maria and Ann use one technique that
makes it hard to decrypt the letter if one does not have the key for doing so. Now we
can say that the communication between Maria and Ann takes place in three layers, as
shown in Figure 2.2. We assume that Ann and Maria each have three machines (or
robots) that can perform the task at each layer.

> **[ASSET ch02_ill_002]** Figure 2.2: A three-layer protocol
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_002.png
> - src: book Figure 2.2; p.33
> - shows: Figure 2.2: A three-layer protocol. Maria and Ann each have three stacked peer functions: Layer 3 Listen/Talk handles plaintext, Layer 2 Encrypt/Decrypt transforms plaintext and ciphertext, and Layer 1 Send/receive mail handles mail. Horizontal double arrows label identical peer objects; the bottom physical route passes through two postal endpoints and a postal carrier facility.
> - structure: Maria and Ann each have three stacked peer functions: Layer 3 Listen/Talk handles plaintext, Layer 2 Encrypt/Decrypt transforms plaintext and ciphertext, and Layer 1 Send/receive mail handles mail. Horizontal double arrows label identical peer objects; the bottom physical route passes through two postal endpoints and a postal carrier facility.
> - text_in_image: Maria; Ann; Layer 3; Listen/Talk; Listen/Talk; Layer 3; Identical objects; Plaintext; Plaintext; Layer 2; Layer 2; Encrypt/Decrypt; Encrypt/Decrypt; Identical objects; Ciphertext; Ciphertext; Send mail/; Send mail/; Layer 1; Layer 1; receive mail; receive mail; Identical objects; Mail; Mail; US Post; US Post; Postal carrier facility
> - use_when: Teach ch02-2-1-1-second-scenario, explain Figure 2.2, or solve a linked practice question.
> - confidence: high

##### Layered Message Flow
> id: ch02-2-1-1-second-scenario-message-flow | src: book pp.33–34 | kind: mechanism

Let us assume that Maria sends the first letter to Ann. Maria talks to the machine at
the third layer as though the machine is Ann and is listening to her. The third layer
machine listens to what Maria says and creates the plaintext (a letter in English), which
is passed to the second layer machine. The second layer machine takes the plaintext,
encrypts it, and creates the ciphertext, which is passed to the first layer machine. The
first layer machine, presumably a robot, takes the ciphertext, puts it in an envelope,
adds the sender and receiver addresses, and mails it.
At Ann’s side, the first layer machine picks up the letter from Ann’s mail box, recognizing the letter from Maria by the sender address. The machine takes out the ciphertext from the envelope and delivers it to the second layer machine. The second layer
machine decrypts the message, creates the plaintext, and passes the plaintext to the
third-layer machine. The third layer machine takes the plaintext and reads it as though
Maria is speaking.
##### Benefits and Tradeoffs of Protocol Layering
> id: ch02-2-1-1-second-scenario-benefits | src: book p.34 | kind: concept

Protocol layering enables us to divide a complex task into several smaller and simpler tasks. For example, in Figure 2.2, we could have used only one machine to do the
job of all three machines. However, if Maria and Ann decide that the encryption/
decryption done by the machine is not enough to protect their secrecy, they would have
to change the whole machine. In the present situation, they need to change only the second layer machine; the other two can remain the same. This is referred to as modularity.
Modularity in this case means independent layers. A layer (module) can be defined as a
black box with inputs and outputs, without concern about how inputs are changed to
outputs. If two machines provide the same outputs when given the same inputs, they
can replace each other. For example, Ann and Maria can buy the second layer machine
from two different manufacturers. As long as the two machines create the same ciphertext from the same plaintext and vice versa, they do the job.
One of the advantages of protocol layering is that it allows us to separate the
services from the implementation. A layer needs to be able to receive a set of services from the lower layer and to give the services to the upper layer; we don’t care
about how the layer is implemented. For example, Maria may decide not to buy the
machine (robot) for the first layer; she can do the job herself. As long as Maria can
do the tasks provided by the first layer, in both directions, the communication
system works.
Another advantage of protocol layering, which cannot be seen in our simple examples but reveals itself when we discuss protocol layering in the Internet, is that communication does not always use only two end systems; there are intermediate systems that
need only some layers, but not all layers. If we did not use protocol layering, we would
have to make each intermediate system as complex as the end systems, which makes
the whole system more expensive.
Is there any disadvantage to protocol layering? One can argue that having a single
layer makes the job easier. There is no need for each layer to provide a service to the
upper layer and give service to the lower layer. For example, Ann and Maria could find
or build one machine that could do all three tasks. However,  as mentioned above, if one
day they found that their code was broken, each would have to replace the whole
machine with a new one instead of just changing the machine in the second layer.

### 2.1.2 Principles of Protocol Layering
> id: ch02-2-1-2 | src: book 2.1.2; p.34 | kind: concept

Let us discuss two principles of protocol layering.

#### First Principle
> id: ch02-2-1-2-first-principle | src: book p.34 | kind: concept

The first principle dictates that if we want bidirectional communication, we need to
make each layer so that it is able to perform two opposite tasks, one in each direction.
For example, the third layer task is to listen (in one direction) and talk (in the other
direction). The second layer needs to be able to encrypt and decrypt. The first layer
needs to send and receive mail.

#### Second Principle
> id: ch02-2-1-2-second-principle | src: book p.34 | kind: concept

The second principle that we need to follow in protocol layering is that the two
objects under each layer at both sites should be identical. For example, the object
under layer 3 at both sites should be a plaintext letter. The object under layer 2 at
both sites should be a ciphertext letter. The object under layer 1 at both sites should
be a piece of mail.

### 2.1.3 Logical Connections
> id: ch02-2-1-3 | src: book 2.1.3; p.35 | kind: concept

After following the above two principles, we can think about logical connection
between each layer as shown in Figure 2.3. This means that we have layer-to-layer
communication. Maria and Ann can think that there is a logical (imaginary) connection
at each layer through which they can send the object created from that layer. We will
see that the concept of logical connection will help us better understand the task of layering we encounter in data communication and networking.

> **[ASSET ch02_ill_003]** Figure 2.3: Logical connection between peer layers
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_003.png
> - src: book Figure 2.3; p.35
> - shows: Figure 2.3: Logical connection between peer layers. The same three peer layers appear at Maria and Ann. Dotted bidirectional arrows show logical peer connections for plaintext at Layer 3, ciphertext at Layer 2, and mail at Layer 1; the actual transfer still traverses the stack.
> - structure: The same three peer layers appear at Maria and Ann. Dotted bidirectional arrows show logical peer connections for plaintext at Layer 3, ciphertext at Layer 2, and mail at Layer 1; the actual transfer still traverses the stack.
> - text_in_image: Maria; Ann; Layer 3; Layer 3; Listen/Talk; Talk/Listen; Logical connection; Plaintext; Plaintext; Layer 2; Layer 2; Encrypt/Decrypt; Encrypt/Decrypt; Logical connection; Ciphertext; Ciphertext; Send mail/; Send mail/; Layer 1; Layer 1; receive mail; receive mail; Logical connection; Mail; Mail
> - use_when: Teach ch02-2-1-3, explain Figure 2.3, or solve a linked practice question.
> - confidence: high

## 2.2 TCP/IP PROTOCOL SUITE
> id: ch02-2-2 | src: book 2.2; p.35 | kind: concept

Now that we know about the concept of protocol layering and the logical communication between layers in our second scenario, we can introduce the TCP/IP (Transmission
Control Protocol/Internet Protocol). TCP/IP is a protocol suite (a set of protocols organized in different layers) used in the Internet today. It is a hierarchical protocol made up
of interactive modules, each of which provides a specific functionality. The term hierarchical means that each upper level protocol is supported by the services provided by
one or more lower level protocols. The original TCP/IP protocol suite was defined as
four software layers built upon the hardware. Today, however, TCP/IP is thought of as a
five-layer model. Figure 2.4 shows both configurations.

### 2.2.1 Layered Architecture
> id: ch02-2-2-1 | src: book 2.2.1; p.35 | kind: concept

To show how the layers in the TCP/IP protocol suite are involved in communication
between two hosts, we assume that we want to use the suite in a small internet made up
of three LANs (links), each with a link-layer switch. We also assume that the links are
connected by one router, as shown in Figure 2.5.

> **[ASSET ch02_ill_004]** Figure 2.4: Layers in the TCP/IP protocol suite
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_004.png
> - src: book Figure 2.4; p.36
> - shows: Figure 2.4: Layers in the TCP/IP protocol suite. Two vertical comparisons show the original four-layer TCP/IP model and the five-layer model used by the book. Original Application maps to Layer 5 Application, Transport to Layer 4 Transport, Internet to Layer 3 Network, and Network Interface plus Hardware Devices to Layer 2 Data link plus Layer 1 Physical.
> - structure: Two vertical comparisons show the original four-layer TCP/IP model and the five-layer model used by the book. Original Application maps to Layer 5 Application, Transport to Layer 4 Transport, Internet to Layer 3 Network, and Network Interface plus Hardware Devices to Layer 2 Data link plus Layer 1 Physical.
> - text_in_image: Application; Application; Layer 5; Layer 4; Transport; Transport; Internet; Network; Layer 3; Network Interface; Data link; Layer 2; Layer 1; Physical; Hardware Devices; a. Original layers; b. Layers used in this book
> - use_when: Teach ch02-2-2-1, explain Figure 2.4, or solve a linked practice question.
> - confidence: high

> **[ASSET ch02_ill_005]** Figure 2.5: Communication through an internet
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_005.png
> - src: book Figure 2.5; p.36
> - shows: Figure 2.5: Communication through an internet. Source A and destination B each contain all five TCP/IP layers. Two link-layer switches contain only data-link and physical layers. The router contains network, data-link, and physical functions for each connected link. The lower topology shows A through Link 1, a router, and Link 2 to B, with a third link to C.
> - structure: Source A and destination B each contain all five TCP/IP layers. Two link-layer switches contain only data-link and physical layers. The router contains network, data-link, and physical functions for each connected link. The lower topology shows A through Link 1, a router, and Link 2 to B, with a third link to C.
> - text_in_image: Source (A); Destination (B); Application; Application; Transport; Transport; Router; Network; Network; Network; Switch; Switch; Data link; Data link; Data link; Data link; Data link; Data link; Physical; Physical; Physical; Physical; Physical; Physical; Communication from A to B; Router; A; B; Link 1; Link 2; Link 3; C
> - use_when: Teach ch02-2-2-1, explain Figure 2.5, or solve a linked practice question.
> - confidence: high

Let us assume that computer A communicates with computer B. As the figure
shows, we have five communicating devices in this communication: source host
(computer A), the link-layer switch in link 1, the router, the link-layer switch in link 2,
and the destination host (computer B). Each device is involved with a set of layers
depending on the role of the device in the internet. The two hosts are involved in all five
layers; the source host needs to create a message in the application layer and send it
down the layers so that it is physically sent to the destination host. The destination host
needs to receive the communication at the physical layer and then deliver it through the
other layers to the application layer.
The router is involved in only three layers; there is no transport or application layer
in a router as long as the router is used only for routing. Although a router is always
involved in one network layer, it is involved in n combinations of link and physical layers in which n is the number of links the router is connected to. The reason is that each
link may use its own data-link or physical protocol. For example, in the above figure, the
router is involved in three links, but the message sent from source A to destination B is
involved in two links. Each link may be using different link-layer and physical-layer
protocols; the router needs to receive a packet from link 1 based on one pair of protocols and deliver it to link 2 based on another pair of protocols.
A link-layer switch in a link, however, is involved only in two layers, data-link and
physical. Although each switch in the above figure has two different connections, the
connections are in the same link, which uses only one set of protocols. This means that,
unlike a router, a link-layer switch is involved only in one data-link and one physical
layer.

### 2.2.2 Layers in the TCP/IP Protocol Suite
> id: ch02-2-2-2 | src: book 2.2.2; p.37 | kind: concept

After the above introduction, we briefly discuss the functions and duties of layers in
the TCP/IP protocol suite. Each layer is discussed in detail in the next five parts of
the book. To better understand the duties of each layer, we need to think about the
logical connections between layers. Figure 2.6 shows logical connections in our simple internet.

> **[ASSET ch02_ill_006]** Figure 2.6: Logical connections between layers of the TCP/IP protocol suite
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_006.png
> - src: book Figure 2.6; p.37
> - shows: Figure 2.6: Logical connections between layers of the TCP/IP protocol suite. Source and destination hosts contain all five layers, the router has network and lower layers, and switches have data-link and physical layers. Horizontal dashed lines show application, transport, and network logical connections end to end, while data-link and physical logical connections operate hop by hop.
> - structure: Source and destination hosts contain all five layers, the router has network and lower layers, and switches have data-link and physical layers. Horizontal dashed lines show application, transport, and network logical connections end to end, while data-link and physical logical connections operate hop by hop.
> - text_in_image: Source; Destination; host; host; Logical connections; Application; Application; Transport; Transport; Network; Network; Data link; Data link; Physical; Physical; Switch; Router; Switch; LAN; LAN; Router; Link 1; Link 2; Source; Destination; To link 3; host; host
> - use_when: Teach ch02-2-2-2, explain Figure 2.6, or solve a linked practice question.
> - confidence: high

Using logical connections makes it easier for us to think about the duty of each
layer. As the figure shows, the duty of the application, transport, and network layers is
end-to-end. However, the duty of the data-link and physical layers is hop-to-hop, in
which a hop is a host or router. In other words, the domain of duty of the top three
layers is the internet, and the domain of duty of the two lower layers is the link.
Another way of thinking of the logical connections is to think about the data unit
created from each layer. In the top three layers, the data unit (packets) should not be
changed by any router or link-layer switch. In the bottom two layers, the packet created
by the host is changed only by the routers, not by the link-layer switches.
Figure 2.7 shows the second principle discussed previously for protocol layering.
We show the identical objects below each layer related to each device.

> **[ASSET ch02_ill_007]** Figure 2.7: Identical objects in the TCP/IP protocol suite
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_007.png
> - src: book Figure 2.7; p.38
> - shows: Figure 2.7: Identical objects in the TCP/IP protocol suite. Source host, router, and destination host are aligned by layers. Dashed paths label identical objects: messages and transport packets are end to end, datagrams remain identical across both router sides, while frames and bits are identical only within each link. A note explains that switches are omitted because they do not change objects.
> - structure: Source host, router, and destination host are aligned by layers. Dashed paths label identical objects: messages and transport packets are end to end, datagrams remain identical across both router sides, while frames and bits are identical only within each link. A note explains that switches are omitted because they do not change objects.
> - text_in_image: Notes: We have not shown switches because they don’t change objects.; Application; Application; Identical objects (messages); Transport; Transport; Identical objects (segments or user datagrams); Network; Network; Identical objects (datagrams); Identical objects (datagrams); Data link; Data link; Identical objects (frames); Identical objects (frames); Physical; Physical; Identical objects (bits); Identical objects (bits)
> - use_when: Teach ch02-2-2-2, explain Figure 2.7, or solve a linked practice question.
> - confidence: high

Note that, although the logical connection at the network layer is between the two
hosts, we can only say that identical objects exist between two hops in this case because
a router may fragment the packet at the network layer and send more packets than
received (see fragmentation in Chapter 19). Note that the link between two hops does
not change the object.

### 2.2.3 Description of Each Layer
> id: ch02-2-2-3 | src: book 2.2.3; p.38 | kind: concept

After understanding the concept of logical communication, we are ready to briefly discuss the duty of each layer. Our discussion in this chapter will be very brief, but we
come back to the duty of each layer in next five parts of the book.

#### Physical Layer
> id: ch02-2-2-3-physical-layer | src: book p.38 | kind: concept

We can say that the physical layer is responsible for carrying individual bits in a frame
across the link. Although the physical layer is the lowest level in the TCP/IP protocol
suite, the communication between two devices at the physical layer is still a logical
communication because there is another, hidden layer, the transmission media, under
the physical layer. Two devices are connected by a transmission medium (cable or air).
We need to know that the transmission medium does not carry bits; it carries electrical
or optical signals. So the bits received in a frame from the data-link layer are transformed and sent through the transmission media, but we can think that the logical unit
between two physical layers in two devices is a bit. There are several protocols that
transform a bit to a signal. We discuss them in Part II when we discuss the physical
layer and the transmission media.

#### Data-link Layer
> id: ch02-2-2-3-data-link-layer | src: book p.39 | kind: concept

We have seen that an internet is made up of several links (LANs and WANs) connected
by routers. There may be several overlapping sets of links that a datagram can travel
from the host to the destination. The routers are responsible for choosing the best links.
However, when the next link to travel is determined by the router, the data-link layer is
responsible for taking the datagram and moving it across the link. The link can be a
wired LAN with a link-layer switch, a wireless LAN, a wired WAN, or a wireless
WAN. We can also have different protocols used with any link type. In each case, the
data-link layer is responsible for moving the packet through the link.
TCP/IP does not define any specific protocol for the data-link layer. It supports all
the standard and proprietary protocols. Any protocol that can take the datagram and
carry it through the link suffices for the network layer. The data-link layer takes a datagram and encapsulates it in a packet called a frame.
Each link-layer protocol may provide a different service. Some link-layer protocols provide complete error detection and correction, some provide only error correction. We discuss wired links in Chapters 13 and 14 and wireless links in Chapters 15
and 16.

#### Network Layer
> id: ch02-2-2-3-network-layer | src: book p.39 | kind: concept

The network layer is responsible for creating a connection between the source computer
and the destination computer. The communication at the network layer is host-to-host.
However, since there can be several routers from the source to the destination, the routers
in the path are responsible for choosing the best route for each packet. We can say that the
network layer is responsible for host-to-host communication and routing the packet
through possible routes. Again, we may ask ourselves why we need the network layer. We
could have added the routing duty to the transport layer and dropped this layer. One reason,
as we said before, is the separation of different tasks between different layers. The second
reason is that the routers do not need the application and transport layers. Separating the
tasks allows us to use fewer protocols on the routers.
The network layer in the Internet includes the main protocol, Internet Protocol
(IP), that defines the format of the packet, called a datagram at the network layer. IP
also defines the format and the structure of addresses used in this layer. IP is also
responsible for routing a packet from its source to its destination, which is achieved by
each router forwarding the datagram to the next router in its path.
IP is a connectionless protocol that provides no flow control, no error control, and
no congestion control services. This means that if any of theses services is required for
an application, the application should rely only on the transport-layer protocol. The network layer also includes unicast (one-to-one) and multicast (one-to-many) routing protocols. A routing protocol does not take part in routing (it is the responsibility of IP),
but it creates forwarding tables for routers to help them in the routing process.
The network layer also has some auxiliary protocols that help IP in its delivery and
routing tasks. The Internet Control Message Protocol (ICMP) helps IP to report some
problems when routing a packet. The Internet Group Management Protocol (IGMP) is
another protocol that helps IP in multitasking. The Dynamic Host Configuration Protocol (DHCP) helps IP to get the network-layer address for a host. The Address Resolution Protocol (ARP) is a protocol that helps IP to find the link-layer address of a host or
a router when its network-layer address is given. ARP is discussed in Chapter 9, ICMP
in Chapter 19, and IGMP in Chapter 21.

#### Transport Layer
> id: ch02-2-2-3-transport-layer | src: book p.40 | kind: concept

The logical connection at the transport layer is also end-to-end. The transport layer at the
source host gets the message from the application layer, encapsulates it in a transport-layer packet (called a segment or a user datagram in different protocols) and sends it,
through the logical (imaginary) connection, to the transport layer at the destination host.
In other words, the transport layer is responsible for giving services to the application
layer: to get a message from an application program running on the source host and
deliver it to the corresponding application program on the destination host. We may ask
why we need an end-to-end transport layer when we already have an end-to-end application layer. The reason is the separation of tasks and duties, which we discussed earlier.
The transport layer should be independent of the application layer. In addition, we will
see that we have more than one protocol in the transport layer, which means that each
application program can use the protocol that best matches its requirement.
As we said, there are a few transport-layer protocols in the Internet, each designed
for some specific task. The main protocol, Transmission Control Protocol (TCP), is a
connection-oriented protocol that first establishes a logical connection between transport layers at two hosts before transferring data. It creates a logical pipe between two
TCPs for transferring a stream of bytes. TCP provides flow control (matching the sending data rate of the source host with the receiving data rate of the destination host to
prevent overwhelming the destination), error control (to guarantee that the segments
arrive at the destination without error and resending the corrupted ones), and congestion control to reduce the loss of segments due to congestion in the network. The other
common protocol, User Datagram Protocol (UDP), is a connectionless protocol that
transmits user datagrams without first creating a logical connection. In UDP, each user
datagram is an independent entity without being related to the previous or the next one
(the meaning of the term connectionless). UDP is a simple protocol that does not provide flow, error, or congestion control. Its simplicity, which means small overhead, is
attractive to an application program that needs to send short messages and cannot
afford the retransmission of the packets involved in TCP, when a packet is corrupted or
lost. A new protocol, Stream Control Transmission Protocol (SCTP) is designed to
respond to new applications that are emerging in the multimedia. We will discuss UDP,
TCP, and SCTP in Chapter 24.

#### Application Layer
> id: ch02-2-2-3-application-layer | src: book p.40 | kind: concept

As Figure 2.6 shows, the logical connection between the two application layers is end-to-end. The two application layers exchange messages between each other as though
there were a bridge between the two layers. However, we should know that the communication is done through all the layers.
Communication at the application layer is between two processes (two programs
running at this layer). To communicate, a process sends a request to the other process
and receives a response. Process-to-process communication is the duty of the application layer. The application layer in the Internet includes many predefined protocols, but
a user can also create a pair of processes to be run at the two hosts. In Chapter 25, we
explore this situation.
The Hypertext Transfer Protocol (HTTP) is a vehicle for accessing the World
Wide Web (WWW). The Simple Mail Transfer Protocol (SMTP) is the main protocol
used in electronic mail (e-mail) service. The File Transfer Protocol (FTP) is used for
transferring files from one host to another. The Terminal Network (TELNET) and
Secure Shell (SSH) are used for accessing a site remotely. The Simple Network Management Protocol (SNMP) is used by an administrator to manage the Internet at global
and local levels. The Domain Name System (DNS) is used by other protocols to find
the network-layer address of a computer. The Internet Group Management Protocol
(IGMP) is used to collect membership in a group. We discuss most of these protocols in
Chapter 26 and some in other chapters.

### 2.2.4 Encapsulation and Decapsulation
> id: ch02-2-2-4 | src: book 2.2.4; p.41 | kind: concept

One of the important concepts in protocol layering in the Internet is encapsulation/
decapsulation. Figure 2.8 shows this concept for the small internet in Figure 2.5.

> **[ASSET ch02_ill_008]** Figure 2.8: Encapsulation/Decapsulation
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_008.png
> - src: book Figure 2.8; p.41
> - shows: Figure 2.8: Encapsulation/Decapsulation. Source host, router, and destination host show encapsulation and decapsulation. At the source, transport header 4, network header 3, and data-link header 2 are added around the message. The router removes and replaces link-layer framing while forwarding the network packet. The destination removes headers 2, 3, and 4 to recover the message.
> - structure: Source host, router, and destination host show encapsulation and decapsulation. At the source, transport header 4, network header 3, and data-link header 2 are added around the message. The router removes and replaces link-layer framing while forwarding the network packet. The destination removes headers 2, 3, and 4 to recover the message.
> - text_in_image: 4; Header at transport layer; Encapsulate; 3; Header at network layer; Legend; 2; Decapsulate; Header at data-link layer; Destination host; Source host; Application; Application; Message; Message; Router; Transport; Transport; 4; Message; 4; Message; Network; Network; 3; 4; Message; 3; 4; Message; 3; 4; Message; 3; 4; Message; Data link; Data link; 2; 3; 4; Message; 2; 3; 4; Message; 2; 3; 4; Message; 2; 3; 4; Message; Physical; Physical
> - use_when: Teach ch02-2-2-4, explain Figure 2.8, or solve a linked practice question.
> - confidence: high

We have not shown the layers for the link-layer switches because no encapsulation/
decapsulation occurs in this device. In Figure 2.8, we show the encapsulation in the
source host, decapsulation in the destination host, and encapsulation and decapsulation
in the router.

#### Encapsulation at the Source Host
> id: ch02-2-2-4-encapsulation-at-the-source-host | src: book p.41 | kind: concept

At the source, we have only encapsulation.
1. At the application layer, the data to be exchanged is referred to as a message. A
message normally does not contain any header or trailer, but if it does, we refer to
the whole as the message. The message is passed to the transport layer.
2. The transport layer takes the message as the payload, the load that the transport
layer should take care of. It adds the transport layer header to the payload, which
contains the identifiers of the source and destination application programs that
want to communicate plus some more information that is needed for the end-to-end delivery of the message, such as information needed for flow, error control, or
congestion control. The result is the transport-layer packet, which is called the segment (in TCP) and the user datagram (in UDP). The transport layer then passes the
packet to the network layer.
3. The network layer takes the transport-layer packet as data or payload and adds its
own header to the payload. The header contains the addresses of the source and
destination hosts and some more information used for error checking of the header,
fragmentation information, and so on. The result is the network-layer packet,
called a datagram. The network layer then passes the packet to the data-link layer.
4. The data-link layer takes the network-layer packet as data or payload and adds its
own header, which contains the link-layer addresses of the host or the next hop (the
router). The result is the link-layer packet, which is called a frame. The frame is
passed to the physical layer for transmission.

#### Decapsulation and Encapsulation at the Router
> id: ch02-2-2-4-decapsulation-and-encapsulation-at-the-router | src: book p.42 | kind: concept

At the router, we have both decapsulation and encapsulation because the router is connected to two or more links.
1. After the set of bits are delivered to the data-link layer, this layer decapsulates the
datagram from the frame and passes it to the network layer.
2. The network layer only inspects the source and destination addresses in the datagram
header and consults its forwarding table to find the next hop to which the datagram is to
be delivered. The contents of the datagram should not be changed by the network layer
in the router unless there is a need to fragment the datagram if it is too big to be passed
through the next link. The datagram is then passed to the data-link layer of the next link.
3. The data-link layer of the next link encapsulates the datagram in a frame and
passes it to the physical layer for transmission.

#### Decapsulation at the Destination Host
> id: ch02-2-2-4-decapsulation-at-the-destination-host | src: book p.42 | kind: concept

At the destination host, each layer only decapsulates the packet received, removes the
payload, and delivers the payload to the next-higher layer protocol until the message
reaches the application layer. It is necessary to say that decapsulation in the host
involves error checking.

### 2.2.5 Addressing
> id: ch02-2-2-5 | src: book 2.2.5; p.42 | kind: concept

It is worth mentioning another concept related to protocol layering in the Internet,
addressing. As we discussed before, we have logical communication between pairs of
layers in this model. Any communication that involves two parties needs two addresses:
source address and destination address. Although it looks as if we need five pairs of
addresses, one pair per layer, we normally have only four because the physical layer does
not need addresses; the unit of data exchange at the physical layer is a bit, which definitely cannot have an address. Figure 2.9 shows the addressing at each layer.
As the figure shows, there is a relationship between the layer, the address used in
that layer, and the packet name at that layer. At the application layer, we normally use
names to define the site that provides services, such as someorg.com, or the e-mail

> **[ASSET ch02_ill_009]** Figure 2.9: Addressing in the TCP/IP protocol suite
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_009.png
> - src: book Figure 2.9; p.43
> - shows: Figure 2.9: Addressing in the TCP/IP protocol suite. A three-column mapping relates packet names to layers and address types: Message/Application/Names; Segment or User datagram/Transport/Port numbers; Datagram/Network/Logical addresses; Frame/Data-link/Link-layer addresses; Bits/Physical with no address type.
> - structure: A three-column mapping relates packet names to layers and address types: Message/Application/Names; Segment or User datagram/Transport/Port numbers; Datagram/Network/Logical addresses; Frame/Data-link/Link-layer addresses; Bits/Physical with no address type.
> - text_in_image: Packet names; Layers; Addresses; Message; Application layer; Names; Segment / User datagram; Transport layer; Port numbers; Datagram; Network layer; Logical addresses; Frame; Data-link layer; Link-layer addresses; Bits; Physical layer
> - use_when: Teach ch02-2-2-5, explain Figure 2.9, or solve a linked practice question.
> - confidence: high

address, such as somebody@coldmail.com. At the transport layer, addresses are called
port numbers, and these define the application-layer programs at the source and
destination. Port numbers are local addresses that distinguish between several programs
running at the same time. At the network-layer, the addresses are global, with the whole
Internet as the scope. A network-layer address uniquely defines the connection of a
device to the Internet. The link-layer addresses, sometimes called MAC addresses, are
locally defined addresses, each of which defines a specific host or router in a network
(LAN or WAN). We will come back to these addresses in future chapters.

### 2.2.6 Multiplexing and Demultiplexing
> id: ch02-2-2-6 | src: book 2.2.6; p.43 | kind: concept

Since the TCP/IP protocol suite uses several protocols at some layers, we can say that we
have multiplexing at the source and demultiplexing at the destination. Multiplexing in this
case means that a protocol at a layer can encapsulate a packet from several next-higher
layer protocols (one at a time); demultiplexing means that a protocol can decapsulate and
deliver a packet to several next-higher layer protocols (one at a time). Figure 2.10 shows
the concept of multiplexing and demultiplexing at the three upper layers.

> **[ASSET ch02_ill_010]** Figure 2.10: Multiplexing and demultiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_010.png
> - src: book Figure 2.10; p.43
> - shows: Figure 2.10: Multiplexing and demultiplexing. At the source, FTP and HTTP feed TCP while DNS and SNMP feed UDP; TCP and UDP multiplex into IP. At the destination, IP demultiplexes to TCP or UDP and then to the appropriate application protocol. Ellipses indicate additional protocols.
> - structure: At the source, FTP and HTTP feed TCP while DNS and SNMP feed UDP; TCP and UDP multiplex into IP. At the destination, IP demultiplexes to TCP or UDP and then to the appropriate application protocol. Ellipses indicate additional protocols.
> - text_in_image: FTP; HTTP; DNS; SNMP; FTP; HTTP; DNS; SNMP; TCP; UDP; TCP; UDP; IP; IP; a. Multiplexing at source; b. Demultiplexing at destination
> - use_when: Teach ch02-2-2-6, explain Figure 2.10, or solve a linked practice question.
> - confidence: high

To be able to multiplex and demultiplex, a protocol needs to have a field in its
header to identify to which protocol the encapsulated packets belong. At the transport
layer, either UDP or TCP can accept a message from several application-layer
protocols. At the network layer, IP can accept a segment from TCP or a user datagram
from UDP. IP can also accept a packet from other protocols such as ICMP, IGMP, and
so on. At the data-link layer, a frame may carry the payload coming from IP or other
protocols such as ARP (see Chapter 9).

## 2.3 THE OSI MODEL
> id: ch02-2-3 | src: book 2.3; p.44 | kind: concept

Although, when speaking of the Internet, everyone talks about the TCP/IP protocol
suite, this suite is not the only suite of protocols defined. Established in 1947, the
International Organization for Standardization (ISO) is a multinational body
dedicated to worldwide agreement on international standards. Almost three-fourths of
the countries in the world are represented in the ISO. An ISO standard that covers all
aspects of network communications is the Open Systems Interconnection (OSI)
model. It was first introduced in the late 1970s.

ISO is the organization; OSI is the model.

An open system is a set of protocols that allows any two different systems to communicate regardless of their underlying architecture. The purpose of the OSI model is
to show how to facilitate communication between different systems without requiring
changes to the logic of the underlying hardware and software. The OSI model is not a
protocol; it is a model for understanding and designing a network architecture that is
flexible, robust, and interoperable. The OSI model was intended to be the basis for the
creation of the protocols in the OSI stack.
The OSI model is a layered framework for the design of network systems that
allows communication between all types of computer systems. It consists of seven separate but related layers, each of which defines a part of the process of moving information
across a network (see Figure 2.11).

> **[ASSET ch02_ill_011]** Figure 2.11: The OSI model
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_011.png
> - src: book Figure 2.11; p.44
> - shows: Figure 2.11: The OSI model. Seven stacked OSI layers are numbered from Layer 7 Application at the top through Presentation, Session, Transport, Network, Data link, to Layer 1 Physical at the bottom.
> - structure: Seven stacked OSI layers are numbered from Layer 7 Application at the top through Presentation, Session, Transport, Network, Data link, to Layer 1 Physical at the bottom.
> - text_in_image: Layer 7; Application; Layer 6; Presentation; Layer 5; Session; Layer 4; Transport; Layer 3; Network; Layer 2; Data link; Layer 1; Physical
> - use_when: Teach ch02-2-3, explain Figure 2.11, or solve a linked practice question.
> - confidence: high

### 2.3.1 OSI versus TCP/IP
> id: ch02-2-3-1 | src: book 2.3.1; p.45 | kind: concept

When we compare the two models, we find that two layers, session and presentation,
are missing from the TCP/IP protocol suite. These two layers were not added to the
TCP/IP protocol suite after the publication of the OSI model. The application layer in
the suite is usually considered to be the combination of three layers in the OSI model,
as shown in Figure 2.12.

> **[ASSET ch02_ill_012]** Figure 2.12: TCP/IP and OSI model
> - type: illustration
> - kind: diagram
> - file: assets/ch02_ill_012.png
> - src: book Figure 2.12; p.45
> - shows: Figure 2.12: TCP/IP and OSI model. The OSI stack is compared with TCP/IP. OSI Application, Presentation, and Session correspond to TCP/IP Application; OSI Transport corresponds to TCP/IP Transport; Network to Network; Data link to Data link; and Physical to Physical. Braces identify several application protocols, several transport protocols, IP plus helper protocols, and underlying LAN/WAN technology.
> - structure: The OSI stack is compared with TCP/IP. OSI Application, Presentation, and Session correspond to TCP/IP Application; OSI Transport corresponds to TCP/IP Transport; Network to Network; Data link to Data link; and Physical to Physical. Braces identify several application protocols, several transport protocols, IP plus helper protocols, and underlying LAN/WAN technology.
> - text_in_image: Application; Several application; Presentation; Application; protocols; Session; Several transport; Transport; Transport; protocols; Internet Protocol; Network; Network; and some helping; protocols; Data link; Data link; Underlying; LAN and WAN; technology; Physical; Physical; TCP/IP Protocol Suite; OSI Model
> - use_when: Teach ch02-2-3-1, explain Figure 2.12, or solve a linked practice question.
> - confidence: high

Two reasons were mentioned for this decision. First, TCP/IP has more than one
transport-layer protocol. Some of the functionalities of the session layer are available
in some of the transport-layer protocols. Second, the application layer is not only
one piece of software. Many applications can be developed at this layer. If some of
the functionalities mentioned in the session and presentation layers are needed for
a particular application, they can be included in the development of that piece of
software.

### 2.3.2 Lack of OSI Model’s Success
> id: ch02-2-3-2 | src: book 2.3.2; p.45 | kind: concept

The OSI model appeared after the TCP/IP protocol suite. Most experts were at first
excited and thought that the TCP/IP protocol would be fully replaced by the OSI
model. This did not happen for several reasons, but we describe only three, which are
agreed upon by all experts in the field. First, OSI was completed when TCP/IP was
fully in place and a lot of time and money had been spent on the suite; changing it
would cost a lot. Second, some layers in the OSI model were never fully defined. For
example, although the services provided by the presentation and the session layers
were listed in the document, actual protocols for these two layers were not fully
defined, nor were they fully described, and the corresponding software was not fully
developed. Third, when OSI was implemented by an organization in a different
application, it did not show a high enough level of performance to entice the Internet
authority to switch from the TCP/IP protocol suite to the OSI model.

## 2.4 END-CHAPTER MATERIALS
> id: ch02-2-4 | src: book 2.4; p.46 | kind: concept

### 2.4.1 Recommended Reading
> id: ch02-2-4-1 | src: book 2.4.1; p.46 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books, and RFCs. The items enclosed in brackets refer to the reference list at the end of
the book.

#### Books and Papers
> id: ch02-2-4-1-books-and-papers | src: book p.46 | kind: concept

Several books and papers give a thorough coverage about the materials discussed in this
chapter: [Seg 98], [Lei et al. 98], [Kle 04], [Cer 89], and [Jen et al. 86].

#### RFCs
> id: ch02-2-4-1-rfcs | src: book p.46 | kind: concept

Two RFCs in particular discuss the TCP/IP suite: RFC 791 (IP) and RFC 817 (TCP). In
future chapters we list different RFCs related to each protocol in each layer.

### 2.4.2 Key Terms
> id: ch02-2-4-2 | src: book 2.4.2; p.46 | kind: concept

- International Organization for Standardization (ISO)
- Open Systems Interconnection (OSI) model
- protocol layering

### 2.4.3 Summary
> id: ch02-2-4-3 | src: book 2.4.3; p.46 | kind: summary

A protocol is a set of rules that governs communication. In protocol layering, we need
to follow two principles to provide bidirectional communication. First, each layer needs
to perform two opposite tasks. Second, two objects under each layer at both sides
should be identical. In a protocol layering, we need to distinguish between a logical
connection and a physical connection. Two protocols at the same layer can have a logical connection; a physical connection is only possible through the physical layers.
TCP/IP is a hierarchical protocol suite made of five layers: physical, data link, network, transport, and application. The physical layer coordinates the functions required
to transmit a bit stream over a physical medium. The data-link layer is responsible for
delivering data units from one station to the next without errors. The network layer is
responsible for the source-to-destination delivery of a packet across multiple network
links. The transport layer is responsible for the process-to-process delivery of the entire
message. The application layer enables the users to access the network.
Four levels of addresses are used in an internet following the TCP/IP protocols: physical (link) addresses, logical (IP) addresses, port addresses, and specific addresses. The
physical address, also known as the link address, is the address of a node as defined by
its LAN or WAN. The IP address uniquely defines a host on the Internet. The port
address identifies a process on a host. A specific address is a user-friendly address.
Another model that defines protocol layering is the Open Systems Interconnection
(OSI) model. Two layers in the OSI model, session and presentation, are missing from
the TCP/IP protocol suite. These two layers were not added to the TCP/IP protocol
suite after the publication of the OSI model. The application layer in the suite is usually
considered to be the combination of three layers in the OSI model. The OSI model did
not replace the TCP/IP protocol suite because it was completed when TCP/IP was fully
in place and because some layers in the OSI model were never fully defined.
