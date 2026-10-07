---
doc_type: scientific_content
course_id: data_communications
chapter: 12
chapter_id: data_communications_ch12
chapter_title: Media Access Control (MAC)
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_12/ch12.pdf
  pages: 325-360
assets_dir: assets
asset_counts:
  illustration: 30
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:48:17+00:00'
status: complete
---
# Chapter 12: Media Access Control (MAC)

## Chapter Objectives
> id: ch12-0 | src: book p.325 | kind: objectives

When nodes or stations are connected and use a common link, called a multipoint or
broadcast link, we need a multiple-access protocol to coordinate access to the link.
The problem of controlling the access to the medium is similar to the rules of speaking in
an assembly. The procedures guarantee that the right to speak is upheld and ensure that
two people do not speak at the same time, do not interrupt each other, do not monopolize
the discussion, and so on.  Many protocols have been devised to handle access to a shared
link. All of these protocols belong to a sublayer in the data-link layer called media access
control (MAC). We categorize them into three groups, as shown in Figure 12.1.

> **[ASSET ch12_ill_001]** Figure 12.1: Taxonomy of multiple-access protocols
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_001.png
> - src: book Figure 12.1; p.325
> - shows: Figure 12.1: Taxonomy of multiple-access protocols. A taxonomy tree divides multiple-access protocols into random access, controlled access, and channelization, with the protocols in each family listed below.
> - structure: A taxonomy tree divides multiple-access protocols into random access, controlled access, and channelization, with the protocols in each family listed below.
> - text_in_image: Multiple-access; protocols; Random-access; Controlled-access; Channelization; protocols; protocols; protocols; ALOHA; Reservation; FDMA; CSMA; Polling; TDMA; CSMA/CD; CDMA; Token passing; CSMA/CA
> - use_when: Teach ch12-0, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

This chapter is divided into three sections:

- The first section discusses random-access protocols. Four protocols, ALOHA,
CSMA, CSMA/CD, and CSMA/CA,  are described in this section. These protocols
are mostly used in LANs and WANs, which we discuss in future chapters.

- The second section discusses controlled-access protocols. Three protocols, reservation, polling, and token-passing, are described in this section. Some of these protocols are used in LANs, but others have some historical value.

- The third section discusses channelization protocols. Three protocols, FDMA,
TDMA, and CDMA are described in this section. These protocols are used in cellular telephony, which we discuss in Chapter 16.

## 12.1 RANDOM ACCESS
> id: ch12-12-1 | src: book 12.1; p.326 | kind: concept

In random-access or contention methods, no station is superior to another station and
none is assigned control over another. At each instance, a station that has data to send
uses a procedure defined by the protocol to make a decision on whether or not to send.
This decision depends on the state of the medium (idle or busy). In other words, each
station can transmit when it desires on the condition that it follows the predefined procedure, including testing the state of the medium.
Two features give this method its name. First, there is no scheduled time for a
station to transmit. Transmission is random among the stations. That is why these
methods are called random access. Second, no rules specify which station should send
next. Stations compete with one another to access the medium. That is why these methods are also called contention methods.
In a random-access method, each station has the right to the medium without being
controlled by any other station. However, if more than one station tries to send, there is
an access conflict—collision—and the frames will be either destroyed or modified. To
avoid access conflict or to resolve it when it happens, each station follows a procedure
that answers the following questions:

- When can the station access the medium?
- What can the station do if the medium is busy?
- How can the station determine the success or failure of the transmission?
- What can the station do if there is an access conflict?

The random-access methods we study in this chapter have evolved from a very
interesting protocol known as ALOHA, which used a very simple procedure called multiple access (MA). The method was improved with the addition of a procedure that
forces the station to sense the medium before transmitting. This was called carrier
sense multiple access (CSMA). This method later evolved into two parallel methods:
carrier sense multiple access with collision detection (CSMA/CD), which tells the station
what to do when a collision is detected, and carrier sense multiple access with collision
avoidance (CSMA/CA), which tries to avoid the collision.

### 12.1.1 ALOHA
> id: ch12-12-1-1 | src: book 12.1.1; p.326 | kind: concept

ALOHA, the earliest random access method, was developed at the University of Hawaii
in early 1970. It was designed for a radio (wireless) LAN, but it can be used on any
shared medium.
It is obvious that there are potential collisions in this arrangement. The medium is
shared between the stations. When a station sends data, another station may attempt to
do so at the same time. The data from the two stations collide and become garbled.

#### Pure ALOHA
> id: ch12-12-1-1-pure-aloha | src: book p.326 | kind: concept

The original ALOHA protocol is called pure ALOHA. This is a simple but elegant protocol. The idea is that each station sends a frame whenever it has a frame to send (multiple access). However, since there is only one channel to share, there is the possibility
of collision between frames from different stations. Figure 12.2 shows an example of
frame collisions in pure ALOHA.

> **[ASSET ch12_ill_002]** Figure 12.2: Frames in a pure ALOHA network
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_002.png
> - src: book Figure 12.2; p.327
> - shows: Figure 12.2: Frames in a pure ALOHA network. Four station timelines show unslotted frames, with shaded overlap regions marking two pure-ALOHA collisions.
> - structure: Four station timelines show unslotted frames, with shaded overlap regions marking two pure-ALOHA collisions.
> - text_in_image: Station 1; Station 2; Station 3; Station 4; Time; Collision; Collision; duration; duration
> - use_when: Teach ch12-12-1-1-pure-aloha, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

There are four stations (unrealistic assumption) that contend with one another for
access to the shared channel. The figure shows that each station sends two frames; there
are a total of eight frames on the shared medium. Some of these frames collide because
multiple frames are in contention for the shared channel. Figure 12.2 shows that only
two frames survive: one frame from station 1 and one frame from station 3. We need to
mention that even if one bit of a frame coexists on the channel with one bit from
another frame, there is a collision and both will be destroyed. It is obvious that we need
to resend the frames that have been destroyed during transmission.
The pure ALOHA protocol relies on acknowledgments from the receiver. When a
station sends a frame, it expects the receiver to send an acknowledgment. If the
acknowledgment does not arrive after a time-out period, the station assumes that the
frame (or the acknowledgment) has been destroyed and resends the frame.
A collision involves two or more stations. If all these stations try to resend their
frames after the time-out, the frames will collide again. Pure ALOHA dictates that
when the time-out period passes, each station waits a random amount of time before
resending its frame. The randomness will help avoid more collisions. We call this time
the backoff time $T_{B}$.
Pure ALOHA has a second method to prevent congesting the channel with retransmitted frames. After a maximum number of retransmission attempts $K_{max}$, a station
must give up and try later. Figure 12.3 shows the procedure for pure ALOHA based on
the above strategy.
The time-out period is equal to the maximum possible round-trip propagation delay,
which is twice the amount of time required to send a frame between the two most widely
separated stations (2 × $T_{p}$). The backoff time $T_{B}$ is a random value that normally depends
on K (the number of attempted unsuccessful transmissions). The formula for $T_{B}$ depends
on the implementation. One common formula is the binary exponential backoff. In this
method, for each retransmission, a multiplier R = 0 to $2^{K}$ − 1 is randomly chosen and multiplied by $T_{p}$ (maximum propagation time) or $T_{fr}$(the average time required to send out a
frame) to find $T_{B}$. Note that in this procedure, the range of the random numbers increases
after each collision. The value of $K_{max}$ is usually chosen as 15.

> **[ASSET ch12_ill_003]** Figure 12.3: Procedure for pure ALOHA protocol
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_003.png
> - src: book Figure 12.3; p.328
> - shows: Figure 12.3: Procedure for pure ALOHA protocol. The pure-ALOHA flowchart initializes attempt count K, sends, waits for an acknowledgment, and uses exponential random backoff before retry or abort.
> - structure: The pure-ALOHA flowchart initializes attempt count K, sends, waits for an acknowledgment, and uses exponential random backoff before retry or abort.
> - text_in_image: Station has; Legend; a frame to send; K : Number of attempts; K = 0; Tp: Maximum propagation time; Tfr: Average transmission time; TB: (Backoff time): R × Tp or R × Tfr; R : (Random number): 0 to 2K – 1; Send the; Wait TB; frame; Wait; Choose; (2 × Tp); R; [false]; ACK; K > Kmax; received?; K = K + 1; [false]; [true]; [true]; Success; Abort
> - use_when: Teach ch12-12-1-1-pure-aloha, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

##### Example 12.1
> id: ch12-example-12-1 | src: book Example 12.1; p.328 | kind: worked_example
The stations on a wireless ALOHA network are a maximum of 600 km apart. If we assume that
signals propagate at 3 × $10^{8}$ m/s, we find $T_{p}$ = (600 × $10^{3}$) / (3 × $10^{8}$) = 2 ms. For K = 2, the range
of R is {0, 1, 2, 3}. This means that $T_{B}$ can be 0, 2, 4, or 6 ms, based on the outcome of the random variable R.

#### Vulnerable time
> id: ch12-12-1-1-vulnerable-time | src: book p.328 | kind: concept

Let us find the vulnerable time, the length of time in which there is a possibility of collision. We assume that the stations send fixed-length frames with each frame taking $T_{fr}$ seconds to send. Figure 12.4 shows the vulnerable time for station B.

> **[ASSET ch12_ill_004]** Figure 12.4: Vulnerable time for pure ALOHA protocol
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_004.png
> - src: book Figure 12.4; p.328
> - shows: Figure 12.4: Vulnerable time for pure ALOHA protocol. Three frames centered around B show that any start within one frame time before or after B overlaps it, giving a vulnerable interval of 2T_fr.
> - structure: Three frames centered around B show that any start within one frame time before or after B overlaps it, giving a vulnerable interval of 2T_fr.
> - text_in_image: A’s end; B’s end; collides with; collides with; B’s beginning; C’s beginning; A; B; C; Time; t + Tfr; t; t – Tfr; Vulnerable time = 2 × Tfr
> - use_when: Teach ch12-12-1-1-vulnerable-time, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

Station B starts to send a frame at time t. Now imagine station A has started to send
its frame after t − $T_{fr}$. This leads to a collision between the frames from station B and
station A. On the other hand, suppose that station C starts to send a frame before time
t + $T_{fr}$. Here, there is also a collision between frames from station B and station C.
Looking at Figure 12.4, we see that the vulnerable time during which a collision
may occur in pure ALOHA is 2 times the frame transmission time.

Pure ALOHA vulnerable time = 2 × $T_{fr}$

##### Example 12.2
> id: ch12-example-12-2 | src: book Example 12.2; p.329 | kind: worked_example
A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps. What is the
requirement to make this frame collision-free?

**Solution**
Average frame transmission time $T_{fr}$ is 200 bits/200 kbps or 1 ms. The vulnerable time is 2 × 1 ms =
2 ms. This means no station should send later than 1 ms before this station starts transmission and
no station should start sending during the period (1 ms) that this station is sending.

#### Throughput
> id: ch12-12-1-1-pure-throughput | src: book p.329 | kind: concept

Let us call G the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully transmitted frames for pure ALOHA is $S=Ge^{-2G}$. The maximum throughput $S_{max}$ is 0.184,
for G = 1/2. (We can find it by setting the derivative of S with respect to G to 0; see Exercises.) In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these frames
reach their destination successfully. We expect G = 1/2 to produce the maximum throughput because the vulnerable time is 2 times the frame transmission time. Therefore, if a
station generates only one frame in this vulnerable time (and no other stations generate a
frame during this time), the frame will reach its destination successfully.

The throughput for pure ALOHA is $S=Ge^{-2G}$.
The maximum throughput is $S_{\max}=1/(2e)\approx0.184$ at $G=1/2$.

##### Example 12.3
> id: ch12-example-12-3 | src: book Example 12.3; p.329 | kind: worked_example
A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps. What is the
throughput if the system (all stations together) produces
a. 1000 frames per second?
b. 500 frames per second?
c. 250 frames per second?

**Solution**
The frame transmission time is 200/200 kbps or 1 ms.
a. If the system creates 1000 frames per second, or 1 frame per millisecond, then G = 1. In
this case $S=Ge^{-2G}$ = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive.
b. If the system creates 500 frames per second, or 1/2 frames per millisecond, then G = 1/2.
In this case $S=Ge^{-2G}$ = 0.184 (18.4 percent). This means that the throughput is 500 ×
0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that this is the
maximum throughput case, percentagewise.
c. If the system creates 250 frames per second, or 1/4 frames per millisecond, then G = 1/4.
In this case $S=Ge^{-2G}$ = 0.152 (15.2 percent). This means that the throughput is
250 × 0.152 = 38. Only 38 frames out of 250 will probably survive.

#### Slotted ALOHA
> id: ch12-12-1-1-slotted-aloha | src: book p.330 | kind: concept

Pure ALOHA has a vulnerable time of 2 × $T_{fr}$. This is so because there is no rule that
defines when the station can send. A station may send soon after another station has
started or just before another station has finished. Slotted ALOHA was invented to
improve the efficiency of pure ALOHA.
In slotted ALOHA we divide the time into slots of $T_{fr}$ seconds and force the station to send only at the beginning of the time slot. Figure 12.5 shows an example of
frame collisions in slotted ALOHA.

> **[ASSET ch12_ill_005]** Figure 12.5: Frames in a slotted ALOHA network
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_005.png
> - src: book Figure 12.5; p.330
> - shows: Figure 12.5: Frames in a slotted ALOHA network. Four station timelines aligned to slots show collisions only when frames begin in the same slot.
> - structure: Four station timelines aligned to slots show collisions only when frames begin in the same slot.
> - text_in_image: Collision; Collision; duration; duration; Station 1; Station 2; Station 3; Station 4; Time; Slot 1; Slot 2; Slot 3; Slot 4; Slot 5; Slot 6
> - use_when: Teach ch12-12-1-1-slotted-aloha, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

Because a station is allowed to send only at the beginning of the synchronized time
slot, if a station misses this moment, it must wait until the beginning of the next time
slot. This means that the station which started at the beginning of this slot has already
finished sending its frame. Of course, there is still the possibility of collision if two
stations try to send at the beginning of the same time slot. However, the vulnerable time
is now reduced to one-half, equal to $T_{fr}$. Figure 12.6 shows the situation.

> **[ASSET ch12_ill_006]** Figure 12.6: Vulnerable time for slotted ALOHA protocol
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_006.png
> - src: book Figure 12.6; p.330
> - shows: Figure 12.6: Vulnerable time for slotted ALOHA protocol. Frames B and C share one slot, illustrating the slotted-ALOHA vulnerable interval T_fr.
> - structure: Frames B and C share one slot, illustrating the slotted-ALOHA vulnerable interval T_fr.
> - text_in_image: B collides with C; A; B; C; Time; t + Tfr; t – Tfr; t; Vulnerable time = Tfr
> - use_when: Teach ch12-12-1-1-slotted-aloha-throughput, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

Slotted ALOHA vulnerable time = $T_{fr}$

#### Throughput
> id: ch12-12-1-1-slotted-aloha-throughput | src: book p.331 | kind: concept

It can be proven that the average number of successful transmissions for slotted ALOHA is
$S=Ge^{-G}$. The maximum throughput $S_{max}$ is 0.368, when G = 1. In other words, if one
frame is generated during one frame transmission time, then 36.8 percent of these frames
reach their destination successfully. We expect G = 1 to produce maximum throughput
because the vulnerable time is equal to the frame transmission time. Therefore, if a station
generates only one frame in this vulnerable time (and no other station generates a frame
during this time), the frame will reach its destination successfully.

The throughput for slotted ALOHA is $S=Ge^{-G}$.
The maximum throughput is $S_{\max}=1/e\approx0.368$ at $G=1$.

##### Example 12.4
> id: ch12-example-12-4 | src: book Example 12.4; p.331 | kind: worked_example
A slotted ALOHA network transmits 200-bit frames using a shared channel with a 200-kbps
bandwidth. Find the throughput if the system (all stations together) produces
a. 1000 frames per second.
b. 500 frames per second.
c. 250 frames per second.

**Solution**
This situation is similar to the previous exercise except that the network is using slotted ALOHA
instead of pure ALOHA. The frame transmission time is 200/200 kbps or 1 ms.
a. In this case G is 1. So $S=Ge^{-G}$ = 0.368 (36.8 percent). This means that the throughput
is 1000 × 0.368 = 368 frames. Only 368 out of 1000 frames will probably survive. Note
that this is the maximum throughput case, percentagewise.
b. Here G is 1/2. In this case $S=Ge^{-G}$ = 0.303 (30.3 percent). This means that the
throughput is 500 × 0.303 ≈ 151. Only 151 frames out of 500 will probably survive.
c. Now G is 1/4. In this case $S=Ge^{-G}$ = 0.195 (19.5 percent). This means that the
throughput is 250 × 0.195 = 49. Only 49 frames out of 250 will probably survive.

### 12.1.2 CSMA
> id: ch12-12-1-2 | src: book 12.1.2; p.331 | kind: concept

To minimize the chance of collision and, therefore, increase the performance, the
CSMA method was developed. The chance of collision can be reduced if a station
senses the medium before trying to use it. Carrier sense multiple access (CSMA)
requires that each station first listen to the medium (or check the state of the medium)
before sending. In other words, CSMA is based on the principle “sense before transmit”
or “listen before talk.”
CSMA can reduce the possibility of collision, but it cannot eliminate it. The reason
for this is shown in Figure 12.7, a space and time model of a CSMA network. Stations
are connected to a shared channel (usually a dedicated medium).
The possibility of collision still exists because of propagation delay; when a station
sends a frame, it still takes time (although very short) for the first bit to reach every station
and for every station to sense it. In other words, a station may sense the medium and find
it idle, only because the first bit sent by another station has not yet been received.

> **[ASSET ch12_ill_007]** Figure 12.7: Space/time model of a collision in CSMA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_007.png
> - src: book Figure 12.7; p.332
> - shows: Figure 12.7: Space/time model of a collision in CSMA. A space-time diagram shows B and C sensing idle at different times because of propagation delay, then creating an overlap region.
> - structure: A space-time diagram shows B and C sensing idle at different times because of propagation delay, then creating an overlap region.
> - text_in_image: B starts; C starts; at time t1; at time t2; A; B; C; D; t1; t2; Area where; B’s signal exists; Area where; both signals exist; Area where; C’s signal exists; Time; Time
> - use_when: Teach ch12-12-1-2, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

At time $t_{1}$, station B senses the medium and finds it idle, so it sends a frame. At
time $t_{2}$ ($t_{2}$ > $t_{1}$), station C senses the medium and finds it idle because, at this time, the
first bits from station B have not reached station C. Station C also sends a frame. The
two signals collide and both frames are destroyed.

#### Vulnerable Time
> id: ch12-12-1-2-vulnerable-time | src: book p.332 | kind: concept

The vulnerable time for CSMA is the propagation time $T_{p}$. This is the time needed for
a signal to propagate from one end of the medium to the other. When a station sends a
frame and any other station tries to send a frame during this time, a collision will result.
But if the first bit of the frame reaches the end of the medium, every station will already
have heard the bit and will refrain from sending. Figure 12.8 shows the worst case. The
leftmost station, A, sends a frame at time $t_{1}$, which reaches the rightmost station, D, at
time $t_{1}$ + $T_{p}$. The gray area shows the vulnerable area in time and space.

> **[ASSET ch12_ill_008]** Figure 12.8: Vulnerable time in CSMA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_008.png
> - src: book Figure 12.8; p.332
> - shows: Figure 12.8: Vulnerable time in CSMA. Signals propagate from four stations across a bus; sensing points and the shaded wedge identify the CSMA vulnerable propagation interval.
> - structure: Signals propagate from four stations across a bus; sensing points and the shaded wedge identify the CSMA vulnerable propagation interval.
> - text_in_image: A; B; C; D; D senses; B senses; C senses; here; here; here; t1; Vulnerable time; =; propagation time; Frame propagation; Time; Time
> - use_when: Teach ch12-12-1-2-vulnerable-time, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

#### Persistence Methods
> id: ch12-12-1-2-persistence-methods | src: book p.333 | kind: concept

What should a station do if the channel is busy? What should a station do if the channel
is idle? Three methods have been devised to answer these questions: the 1-persistent
method, the nonpersistent method, and the p-persistent method. Figure 12.9 shows
the behavior of three persistence methods when a station finds a channel busy.

> **[ASSET ch12_ill_009]** Figure 12.9: Behavior of three persistence methods
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_009.png
> - src: book Figure 12.9; p.333
> - shows: Figure 12.9: Behavior of three persistence methods. Timelines compare 1-persistent, nonpersistent, and p-persistent behavior while a channel alternates between busy and idle.
> - structure: Timelines compare 1-persistent, nonpersistent, and p-persistent behavior while a channel alternates between busy and idle.
> - text_in_image: Transmit; Transmit; Sense; Sense; Continuously sense; Wait; Wait; Time; Time; Busy; Busy; a. 1-Persistent; b. Nonpersistent; Send if; Send if; Send if; R < p.; R < p.; R < p.; Wait a time slot; Wait a backoff; Wait a time slot; Continuously sense; otherwise; time; otherwise; Time; Busy; Busy; c. p-Persistent
> - use_when: Teach ch12-12-1-2-persistence-methods, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

Figure 12.10 shows the flow diagrams for these methods.

#### 1-Persistent
> id: ch12-12-1-2-1-persistent | src: book p.333 | kind: concept

The 1-persistent method is simple and straightforward. In this method, after the station
finds the line idle, it sends its frame immediately (with probability 1). This method has
the highest chance of collision because two or more stations may find the line idle and
send their frames immediately. We will see later that Ethernet uses this method.

#### Nonpersistent
> id: ch12-12-1-2-nonpersistent | src: book p.333 | kind: concept

In the nonpersistent method, a station that has a frame to send senses the line. If the line
is idle, it sends immediately. If the line is not idle, it waits a random amount of time and
then senses the line again. The nonpersistent approach reduces the chance of collision
because it is unlikely that two or more stations will wait the same amount of time and
retry to send simultaneously. However, this method reduces the efficiency of the network because the medium remains idle when there may be stations with frames to send.

p-Persistent
The p-persistent method is used if the channel has time slots with a slot duration equal
to or greater than the maximum propagation time. The p-persistent approach combines
the advantages of the other two strategies. It reduces the chance of collision and
improves efficiency. In this method, after the station finds the line idle it follows these
steps:
1. With probability p, the station sends its frame.

> **[ASSET ch12_ill_010]** Figure 12.10: Flow diagram for three persistence methods
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_010.png
> - src: book Figure 12.10; p.334
> - shows: Figure 12.10: Flow diagram for three persistence methods. Three flowcharts specify the sensing, waiting, probability, and transmission decisions for 1-persistent, nonpersistent, and p-persistent CSMA.
> - structure: Three flowcharts specify the sensing, waiting, probability, and transmission decisions for 1-persistent, nonpersistent, and p-persistent CSMA.
> - text_in_image: Channel; Channel; [true]; [true]; busy?; busy?; Wait; randomly; [false]; [false]; Station; Station; can transmit.; can transmit.; a. 1-Persistent; b. Nonpersistent; Channel; [true]; busy?; [false]; Generate a; random number; (R = 0 to 1); Channel; [false]; R ≤ p; [false]; busy?; Wait; a slot; [true]; [true]; Use backoff process; Station; as though collision occurred.; can transmit.; c. p-Persistent
> - use_when: Teach ch12-12-1-2-persistence-methods, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

2. With probability q = 1 − p, the station waits for the beginning of the next time slot
and checks the line again.
a. If the line is idle, it goes to step 1.
b. If the line is busy, it acts as though a collision has occurred and uses the backoff procedure.

### 12.1.3 CSMA/CD
> id: ch12-12-1-3 | src: book 12.1.3; p.334 | kind: concept

The CSMA method does not specify the procedure following a collision. Carrier sense
multiple access with collision detection (CSMA/CD) augments the algorithm to
handle the collision.
In this method, a station monitors the medium after it sends a frame to see if the
transmission was successful. If so, the station is finished. If, however, there is a collision, the frame is sent again.
To better understand CSMA/CD, let us look at the first bits transmitted by the two
stations involved in the collision. Although each station continues to send bits in the
frame until it detects the collision, we show what happens as the first bits collide. In
Figure 12.11, stations A and C are involved in the collision.

> **[ASSET ch12_ill_011]** Figure 12.11: Collision of the first bits in CSMA/CD
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_011.png
> - src: book Figure 12.11; p.335
> - shows: Figure 12.11: Collision of the first bits in CSMA/CD. A space-time plot shows the first bits from A and C colliding before either station detects the other transmission.
> - structure: A space-time plot shows the first bits from A and C colliding before either station detects the other transmission.
> - text_in_image: A; B; C; D; t1; First bit of A; t2; Transmission; Transmission; time; t3; time; First bit of C; C’s collision; t4; A’s collision; detection and; detection; abortion; and abortion; Collision; Time; Time; occurs
> - use_when: Teach ch12-12-1-3, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

At time $t_{1}$, station A has executed its persistence procedure and starts sending
the bits of its frame. At time $t_{2}$, station C has not yet sensed the first bit sent by
A. Station C executes its persistence procedure and starts sending the bits in its
frame, which propagate both to the left and to the right. The collision occurs sometime after time $t_{2}$. Station C detects a collision at time $t_{3}$ when it receives the first
bit of A’s frame. Station C immediately (or after a short time, but we assume immediately) aborts transmission. Station A detects collision at time $t_{4}$ when it receives
the first bit of C’s frame; it also immediately aborts transmission. Looking at the
figure, we see that A transmits for the duration $t_{4}$ − $t_{1}$; C transmits for the duration
$t_{3}$ − $t_{2}$.
Now that we know the time durations for the two transmissions, we can show a
more complete graph in Figure 12.12.

> **[ASSET ch12_ill_012]** Figure 12.12: Collision and abortion in CSMA/CD
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_012.png
> - src: book Figure 12.12; p.335
> - shows: Figure 12.12: Collision and abortion in CSMA/CD. After collision, A and C continue briefly, detect the collision at different times, and abort their partial frames.
> - structure: After collision, A and C continue briefly, detect the collision at different times, and abort their partial frames.
> - text_in_image: A; B; C; D; Collision; occurs; t1; t2; Transmission; Transmission; Part of A’s frame; time; t3; time; Part of C’s frame; t4; A detects; collision and; aborts; C detects; collision; Time; Time; and aborts
> - use_when: Teach ch12-12-1-3, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

#### Minimum Frame Size
> id: ch12-12-1-3-minimum-frame-size | src: book p.335 | kind: concept

For CSMA/CD to work, we need a restriction on the frame size. Before sending the last
bit of the frame, the sending station must detect a collision, if any, and abort the transmission. This is so because the station, once the entire frame is sent, does not keep a copy of
the frame and does not monitor the line for collision detection. Therefore, the frame transmission time $T_{fr}$ must be at least two times the maximum propagation time $T_{p}$. To understand the reason, let us think about the worst-case scenario. If the two stations involved in
a collision are the maximum distance apart, the signal from the first takes time $T_{p}$ to reach
the second, and the effect of the collision takes another time $T_{P}$ to reach the first. So the
requirement is that the first station must still be transmitting after $2T_{p}$.

##### Example 12.5
> id: ch12-example-12-5 | src: book Example 12.5; p.336 | kind: worked_example
A network using CSMA/CD has a bandwidth of 10 Mbps. If the maximum propagation time
(including the delays in the devices and ignoring the time needed to send a jamming signal, as we
see later) is 25.6 μs, what is the minimum size of the frame?

**Solution**
The minimum frame transmission time is $T_{fr}$ = 2 × $T_{p}$ = 51.2 μs. This means, in the worst case, a
station needs to transmit for a period of 51.2 μs to detect the collision. The minimum size of the
frame is 10 Mbps × 51.2 μs = 512 bits or 64 bytes. This is actually the minimum size of the frame
for Standard Ethernet, as we will see later in the chapter.

#### Procedure
> id: ch12-12-1-3-procedure | src: book p.336 | kind: concept

Now let us look at the flow diagram for CSMA/CD in Figure 12.13. It is similar to the
one for the ALOHA protocol, but there are differences.

> **[ASSET ch12_ill_013]** Figure 12.13: Flow diagram for the CSMA/CD
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_013.png
> - src: book Figure 12.13; p.336
> - shows: Figure 12.13: Flow diagram for the CSMA/CD. The CSMA/CD flowchart combines persistence, simultaneous transmit-and-listen behavior, collision detection, jamming, and binary exponential backoff.
> - structure: The CSMA/CD flowchart combines persistence, simultaneous transmit-and-listen behavior, collision detection, jamming, and binary exponential backoff.
> - text_in_image: Station has; a frame to send; K = 0; Legend; Tfr: Frame average transmission; time; Wait TB; K : Number of attempts; Apply one of the; R  : (random number): 0 to 2K _ 1; persistence methods; seconds; TB: (Backoff time) = R × Tfr; Create random; Done or; [false]; Transmit; number R; collision?; and receive; [true]; [true]; Send a; Collision; K < 15 ?; [true]; jamming; K = K + 1; detected?; signal; [false]; [false]; Abort; Success
> - use_when: Teach ch12-12-1-3-procedure, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

The first difference is the addition of the persistence process. We need to sense the
channel before we start sending the frame by using one of the persistence processes we
discussed previously (nonpersistent, 1-persistent, or p-persistent). The corresponding
box can be replaced by one of the persistence processes shown in Figure 12.10.
The second difference is the frame transmission. In ALOHA, we first transmit
the entire frame and then wait for an acknowledgment. In CSMA/CD, transmission
and collision detection are continuous processes. We do not send the entire frame and
then look for a collision. The station transmits and receives continuously and simultaneously (using two different ports or a bidirectional port). We use a loop to show that
transmission is a continuous process. We constantly monitor in order to detect one of
two conditions: either transmission is finished or a collision is detected. Either event
stops transmission. When we come out of the loop, if a collision has not been
detected, it means that transmission is complete; the entire frame is transmitted.
Otherwise, a collision has occurred.
The third difference is the sending of a short jamming signal to make sure that all
other stations become aware of the collision.

#### Energy Level
> id: ch12-12-1-3-energy-level | src: book p.337 | kind: concept

We can say that the level of energy in a channel can have three values: zero, normal,
and abnormal. At the zero level, the channel is idle. At the normal level, a station has
successfully captured the channel and is sending its frame. At the abnormal level, there
is a collision and the level of the energy is twice the normal level. A station that has a
frame to send or is sending a frame needs to monitor the energy level to determine if the
channel is idle, busy, or in collision mode. Figure 12.14 shows the situation.

> **[ASSET ch12_ill_014]** Figure 12.14: Energy level during transmission, idleness, or collision
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_014.png
> - src: book Figure 12.14; p.337
> - shows: Figure 12.14: Energy level during transmission, idleness, or collision. Energy over time distinguishes a normal transmission level, zero-energy idle interval, and abnormal collision level.
> - structure: Energy over time distinguishes a normal transmission level, zero-energy idle interval, and abnormal collision level.
> - text_in_image: Energy; Collision; Time; Frame transmission; Frame transmission; Idle
> - use_when: Teach ch12-12-1-3-energy-level, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

#### Throughput
> id: ch12-12-1-3-throughput | src: book p.337 | kind: concept

The throughput of CSMA/CD is greater than that of pure or slotted ALOHA. The maximum throughput occurs at a different value of G and is based on the persistence
method and the value of p in the p-persistent approach. For the 1-persistent method, the
maximum throughput is around 50 percent when G = 1. For the nonpersistent method,
the maximum throughput can go up to 90 percent when G is between 3 and 8.

#### Traditional Ethernet
> id: ch12-12-1-3-traditional-ethernet | src: book p.337 | kind: concept

One of the LAN protocols that used CSMA/CD is the traditional Ethernet with the data
rate of 10 Mbps. We discuss the Ethernet LANs in Chapter 13, but it is good to know
that the traditional Ethernet was a broadcast LAN that used the 1-persistence method to
control access to the common media. Later versions of Ethernet try to move from
CSMA/CD access methods for the reason that we discuss in Chapter 13.

### 12.1.4 CSMA/CA
> id: ch12-12-1-4 | src: book 12.1.4; p.338 | kind: concept

Carrier sense multiple access with collision avoidance (CSMA/CA) was invented
for wireless networks. Collisions are avoided through the use of CSMA/CA’s three
strategies: the interframe space, the contention window, and acknowledgments, as
shown in Figure 12.15. We discuss RTS and CTS frames later.

> **[ASSET ch12_ill_015]** Figure 12.15: Flow diagram of CSMA/CA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_015.png
> - src: book Figure 12.15; p.338
> - shows: Figure 12.15: Flow diagram of CSMA/CA. The CSMA/CA flowchart uses IFS, a contention window, acknowledgments, timeout, and exponential backoff because wireless stations cannot reliably detect collisions.
> - structure: The CSMA/CA flowchart uses IFS, a contention window, acknowledgments, timeout, and exponential backoff because wireless stations cannot reliably detect collisions.
> - text_in_image: Station has; a frame to send; K = 0; Legend; K: Number of attempts; TB: Backoff time; Channel free?; IFS: Interframe Space; [false]; [true]; RTS: Request to send; Carrier sense; CTS: Clear to send; Wait IFS; Choose a random number; Contention; R between 0 and 2K − 1; window; and use the Rth slot; Send RTS; Wait TB; seconds; Set a timer; CTS received; [false]; before time-out?; [true]; Wait IFS; Send; Transmission; the frame; Set a timer; [true]; ACK received; K < limit ?; [false]; before time-out?; K = K + 1; [true]; [false]; Abort; Success
> - use_when: Teach ch12-12-1-4, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

- Interframe Space (IFS). First, collisions are avoided by deferring transmission even
if the channel is found idle. When an idle channel is found, the station does not send
immediately. It waits for a period of time called the interframe space or IFS. Even
though the channel may appear idle when it is sensed, a distant station may have
already started transmitting. The distant station’s signal has not yet reached this
station. The IFS time allows the front of the transmitted signal by the distant station to
reach this station. After waiting an IFS time, if the channel is still idle, the station can
send, but it still needs to wait a time equal to the contention window (described next).
The IFS variable can also be used to prioritize stations or frame types. For example, a
station that is assigned a shorter IFS has a higher priority.

- Contention Window. The contention window is an amount of time divided into
slots. A station that is ready to send chooses a random number of slots as its wait
time. The number of slots in the window changes according to the binary exponential backoff strategy. This means that it is set to one slot the first time and then doubles each time the station cannot detect an idle channel after the IFS time. This is
very similar to the p-persistent method except that a random outcome defines the
number of slots taken by the waiting station. One interesting point about the contention window is that the station needs to sense the channel after each time slot.
However, if the station finds the channel busy, it does not restart the process; it just
stops the timer and restarts it when the channel is sensed as idle. This gives priority
to the station with the longest waiting time. See Figure 12.16.

> **[ASSET ch12_ill_016]** Figure 12.16: Contention window
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_016.png
> - src: book Figure 12.16; p.339
> - shows: Figure 12.16: Contention window. A time axis expands the contention window after a failed attempt and shows a randomly selected slot following IFS.
> - structure: A time axis expands the contention window after a failed attempt and shows a randomly selected slot following IFS.
> - text_in_image: Size:; Found; binary exponential; idle; Continuously sense; IFS; Contention window; Time; Busy
> - use_when: Teach ch12-12-1-4-frame-exchange-time-line, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

- Acknowledgment. With all these precautions, there still may be a collision resulting
in destroyed data. In addition, the data may be corrupted during the transmission.
The positive acknowledgment and the time-out timer can help guarantee that the
receiver has received the frame.

#### Frame Exchange Time Line
> id: ch12-12-1-4-frame-exchange-time-line | src: book p.339 | kind: concept

Figure 12.17 shows the exchange of data and control frames in time.
1. Before sending a frame, the source station senses the medium by checking the
energy level at the carrier frequency.
a. The channel uses a persistence strategy with backoff until the channel is idle.
b. After the station is found to be idle, the station waits for a period of time called
the DCF interframe space (DIFS); then the station sends a control frame called
the request to send (RTS).
2. After receiving the RTS and waiting a period of time called the short interframe
space (SIFS), the destination station sends a control frame, called the clear to
send (CTS), to the source station. This control frame indicates that the destination
station is ready to receive data.

> **[ASSET ch12_ill_017]** Figure 12.17: CSMA/CA and NAV
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_017.png
> - src: book Figure 12.17; p.340
> - shows: Figure 12.17: CSMA/CA and NAV. RTS, CTS, data, and ACK timelines show SIFS/DIFS spacing and how other stations set their network allocation vectors.
> - structure: RTS, CTS, data, and ACK timelines show SIFS/DIFS spacing and how other stations set their network allocation vectors.
> - text_in_image: All other stations; Source; Destination; A; B; C; D; • • •; DIFS; RTS; SIFS; CTS; CTS; SIFS; NAV; Data; SIFS; ACK; ACK; Time; Time; Time; Time
> - use_when: Teach ch12-12-1-4-network-allocation-vector, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

3. The source station sends data after waiting an amount of time equal to SIFS.
4. The destination station, after waiting an amount of time equal to SIFS, sends an
acknowledgment to show that the frame has been received. Acknowledgment is
needed in this protocol because the station does not have any means to check for
the successful arrival of its data at the destination. On the other hand, the lack of
collision in CSMA/CD is a kind of indication to the source that data have
arrived.

#### Network Allocation Vector
> id: ch12-12-1-4-network-allocation-vector | src: book p.340 | kind: concept

How do other stations defer sending their data if one station acquires access? In other
words, how is the collision avoidance aspect of this protocol accomplished? The key is
a feature called NAV.
When a station sends an RTS frame, it includes the duration of time that it needs to
occupy the channel. The stations that are affected by this transmission create a timer
called a network allocation vector (NAV) that shows how much time must pass before
these stations are allowed to check the channel for idleness. Each time a station
accesses the system and sends an RTS frame, other stations start their NAV. In other
words, each station, before sensing the physical medium to see if it is idle, first checks
its NAV to see if it has expired. Figure 12.17 shows the idea of NAV.

#### Collision During Handshaking
> id: ch12-12-1-4-collision-during-handshaking | src: book p.340 | kind: concept

What happens if there is a collision during the time when RTS or CTS control frames
are in transition, often called the handshaking period? Two or more stations may try to
send RTS frames at the same time. These control frames may collide. However,
because there is no mechanism for collision detection, the sender assumes there has
been a collision if it has not received a CTS frame from the receiver. The backoff strategy is employed, and the sender tries again.

#### Hidden-Station Problem
> id: ch12-12-1-4-hidden-station-problem | src: book p.341 | kind: concept

The solution to the hidden station problem is the use of the handshake frames (RTS and
CTS).  Figure 12.17 also shows that the RTS message from B reaches A, but not C.
However, because both B and C are within the range of A, the CTS message, which
contains the duration of data transmission from B to A, reaches C. Station C knows that
some hidden station is using the channel and refrains from transmitting until that duration is over.

#### CSMA/CA and Wireless Networks
> id: ch12-12-1-4-csma-ca-and-wireless-networks | src: book p.341 | kind: concept

CSMA/CA was mostly intended for use in wireless networks. The procedure described
above, however, is not sophisticated enough to handle some particular issues related to
wireless networks, such as hidden terminals or exposed terminals. We will see how
these issues are solved by augmenting the above protocol with handshaking features.
The use of CSMA/CA in wireless networks will be discussed in Chapter 15.

## 12.2 CONTROLLED ACCESS
> id: ch12-12-2 | src: book 12.2; p.341 | kind: concept

In controlled access, the stations consult one another to find which station has the right
to send. A station cannot send unless it has been authorized by other stations. We discuss three controlled-access methods.

### 12.2.1 Reservation
> id: ch12-12-2-1 | src: book 12.2.1; p.341 | kind: concept

In the reservation method, a station needs to make a reservation before sending data.
Time is divided into intervals. In each interval, a reservation frame precedes the data
frames sent in that interval.
If there are N stations in the system, there are exactly N reservation minislots in the
reservation frame. Each minislot belongs to a station. When a station needs to send a
data frame, it makes a reservation in its own minislot. The stations that have made reservations can send their data frames after the reservation frame.
Figure 12.18 shows a situation with five stations and a five-minislot reservation
frame. In the first interval, only stations 1, 3, and 4 have made reservations. In the second interval, only station 1 has made a reservation.

> **[ASSET ch12_ill_018]** Figure 12.18: Reservation access method
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_018.png
> - src: book Figure 12.18; p.341
> - shows: Figure 12.18: Reservation access method. Reservation mini-slots precede data frames; stations announce their intended transmissions before sending in reservation order.
> - structure: Reservation mini-slots precede data frames; stations announce their intended transmissions before sending in reservation order.
> - text_in_image: Direction of packet movement; 5; 4; 3; 2; 1; 5; 4; 3; 2; 1; 5; 4; 3; 2; 1; Data; Data; Data; Data; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 1; 1; 0; 1; station 1; station 4; station 3; station 1; Reservation; frame
> - use_when: Teach ch12-12-2-1, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

### 12.2.2 Polling
> id: ch12-12-2-2 | src: book 12.2.2; p.342 | kind: concept

Polling works with topologies in which one device is designated as a primary station and
the other devices are secondary stations. All data exchanges must be made through the
primary device even when the ultimate destination is a secondary device. The primary
device controls the link; the secondary devices follow its instructions. It is up to the primary device to determine which device is allowed to use the channel at a given time. The
primary device, therefore, is always the initiator of a session (see Figure 12.19). This
method uses poll and select functions to prevent collisions. However, the drawback is if
the primary station fails, the system goes down.

> **[ASSET ch12_ill_019]** Figure 12.19: Select and poll functions in polling-access method
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_019.png
> - src: book Figure 12.19; p.342
> - shows: Figure 12.19: Select and poll functions in polling-access method. Select and poll exchanges show a primary station granting a secondary permission to receive or to transmit.
> - structure: Select and poll exchanges show a primary station granting a secondary permission to receive or to transmit.
> - text_in_image: A; A; B; B; Primary; Primary; 1; SEL; 1; Poll; 2; 2; ACK; NAK; 3; Data; 3; 4; Poll; ACK; 4; Data; Select; 5; ACK; Poll
> - use_when: Teach ch12-12-2-2, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

#### Select
> id: ch12-12-2-2-select | src: book p.342 | kind: concept

The select function is used whenever the primary device has something to send.
Remember that the primary controls the link. If the primary is neither sending nor
receiving data, it knows the link is available. If it has something to send, the primary
device sends it. What it does not know, however, is whether the target device is prepared to receive. So the primary must alert the secondary to the upcoming transmission
and wait for an acknowledgment of the secondary’s ready status. Before sending data,
the primary creates and transmits a select (SEL) frame, one field of which includes the
address of the intended secondary.

#### Poll
> id: ch12-12-2-2-poll | src: book p.342 | kind: concept

The poll function is used by the primary device to solicit transmissions from the secondary devices. When the primary is ready to receive data, it must ask (poll) each
device in turn if it has anything to send. When the first secondary is approached, it
responds either with a NAK frame if it has nothing to send or with data (in the form of
a data frame) if it does. If the response is negative (a NAK frame), then the primary
polls the next secondary in the same manner until it finds one with data to send. When
the response is positive (a data frame), the primary reads the frame and returns an
acknowledgment (ACK frame), verifying its receipt.

### 12.2.3 Token Passing
> id: ch12-12-2-3 | src: book 12.2.3; p.343 | kind: concept

In the token-passing method, the stations in a network are organized in a logical ring.
In other words, for each station, there is a predecessor and a successor. The predecessor is the station which is logically before the station in the ring; the successor is the
station which is after the station in the ring. The current station is the one that is
accessing the channel now. The right to this access has been passed from the predecessor to the current station. The right will be passed to the successor when the current
station has no more data to send.
But how is the right to access the channel passed from one station to another? In
this method, a special packet called a token circulates through the ring. The possession
of the token gives the station the right to access the channel and send its data. When a
station has some data to send, it waits until it receives the token from its predecessor. It
then holds the token and sends its data. When the station has no more data to send, it
releases the token, passing it to the next logical station in the ring. The station cannot
send data until it receives the token again in the next round. In this process, when a station receives the token and has no data to send, it just passes the data to the next station.
Token management is needed for this access method. Stations must be limited in the
time they can have possession of the token. The token must be monitored to ensure it has
not been lost or destroyed. For example, if a station that is holding the token fails, the token
will disappear from the network. Another function of token management is to assign priorities to the stations and to the types of data being transmitted. And finally, token management is needed to make low-priority stations release the token to high-priority stations.

#### Logical Ring
> id: ch12-12-2-3-logical-ring | src: book p.343 | kind: concept

In a token-passing network, stations do not have to be physically connected in a ring;
the ring can be a logical one. Figure 12.20 shows four different physical topologies that
can create a logical ring.

> **[ASSET ch12_ill_020]** Figure 12.20: Logical ring and physical topology in token-passing access method
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_020.png
> - src: book Figure 12.20; p.343
> - shows: Figure 12.20: Logical ring and physical topology in token-passing access method. Physical ring, dual ring, bus ring, and star ring topologies are annotated with the logical token path.
> - structure: Physical ring, dual ring, bus ring, and star ring topologies are annotated with the logical token path.
> - text_in_image: 1; 2; 1; 2; 3; 4; 3; 4; a. Physical ring; b. Dual ring; 1; 2; 1; 2; 3; 4; 3; 4; c. Bus ring; d. Star ring
> - use_when: Teach ch12-12-2-3-logical-ring, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

In the physical ring topology, when a station sends the token to its successor, the
token cannot be seen by other stations; the successor is the next one in line. This
means that the token does not have to have the address of the next successor. The problem with this topology is that if one of the links—the medium between two adjacent
stations—fails, the whole system fails.
The dual ring topology uses a second (auxiliary) ring which operates in the reverse
direction compared with the main ring. The second ring is for emergencies only (such
as a spare tire for a car). If one of the links in the main ring fails, the system automatically combines the two rings to form a temporary ring. After the failed link is restored,
the auxiliary ring becomes idle again. Note that for this topology to work, each station
needs to have two transmitter ports and two receiver ports. The high-speed Token Ring
networks called FDDI (Fiber Distributed Data Interface) and CDDI (Copper Distributed Data Interface) use this topology.
In the bus ring topology, also called a token bus, the stations are connected to a single cable called a bus. They, however, make a logical ring, because each station knows
the address of its successor (and also predecessor for token management purposes).
When a station has finished sending its data, it releases the token and inserts the address
of its successor in the token. Only the station with the address matching the destination
address of the token gets the token to access the shared media. The Token Bus LAN,
standardized by IEEE, uses this topology.
In a star ring topology, the physical topology is a star. There is a hub, however, that
acts as the connector. The wiring inside the hub makes the ring; the stations are connected to this ring through the two wire connections. This topology makes the network
less prone to failure because if a link goes down, it will be bypassed by the hub and the
rest of the stations can operate. Also adding and removing stations from the ring is easier.
This topology is still used in the Token Ring LAN designed by IBM.

## 12.3 CHANNELIZATION
> id: ch12-12-3 | src: book 12.3; p.344 | kind: concept

Channelization (or channel partition, as it is sometimes called) is a multiple-access
method in which the available bandwidth of a link is shared in time, frequency, or
through code, among different stations. In this section, we discuss three channelization
protocols: FDMA, TDMA, and CDMA.

We see the application of all these methods in Chapter 16
when we discuss cellular phone systems.

### 12.3.1 FDMA
> id: ch12-12-3-1 | src: book 12.3.1; p.344 | kind: concept

In frequency-division multiple access (FDMA), the available bandwidth is divided
into frequency bands. Each station is allocated a band to send its data. In other words,
each band is reserved for a specific station, and it belongs to the station all the time.
Each station also uses a bandpass filter to confine the transmitter frequencies. To prevent
station interferences, the allocated bands are separated from one another by small
guard bands. Figure 12.21 shows the idea of FDMA.

> **[ASSET ch12_ill_021]** Figure 12.21: Frequency-division multiple access (FDMA)
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_021.png
> - src: book Figure 12.21; p.345
> - shows: Figure 12.21: Frequency-division multiple access (FDMA). Four stations occupy separate frequency bands in a common FDMA channel while one station is silent.
> - structure: Four stations occupy separate frequency bands in a common FDMA channel while one station is silent.
> - text_in_image: Data; Data; f; f; Station 2; Station 1; • • •; • • •; t; t; f; Common; • • •; channel; t; f; f; Station 3; Station 4; • • •; • • •; t; t; Data; Silent
> - use_when: Teach ch12-12-3-1, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

In FDMA, the available bandwidth of the common channel
is divided into bands that are separated by guard bands.

FDMA specifies a predetermined frequency band for the entire period of communication. This means that stream data (a continuous flow of data that may not be packetized) can easily be used with FDMA. We will see in Chapter 16 how this feature can
be used in cellular telephone systems.
We need to emphasize that although FDMA and frequency-division multiplexing
(FDM) conceptually seem similar, there are differences between them. FDM, as we
saw in Chapter 6, is a physical layer technique that combines the loads from lowbandwidth channels and transmits them by using a high-bandwidth channel. The channels that are combined are low-pass. The multiplexer modulates the signals, combines
them, and creates a bandpass signal. The bandwidth of each channel is shifted by the
multiplexer.
FDMA, on the other hand, is an access method in the data-link layer. The data-link layer in each station tells its physical layer to make a bandpass signal from the
data passed to it. The signal must be created in the allocated band. There is no physical multiplexer at the physical layer. The signals created at each station are automatically  bandpass-filtered. They are mixed when they are sent to the common
channel.

### 12.3.2 TDMA
> id: ch12-12-3-2 | src: book 12.3.2; p.346 | kind: concept

In time-division multiple access (TDMA), the stations share the bandwidth of the
channel in time. Each station is allocated a time slot during which it can send data.
Each station transmits its data in its assigned time slot. Figure 12.22 shows the idea
behind TDMA.

> **[ASSET ch12_ill_022]** Figure 12.22: Time-division multiple access (TDMA)
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_022.png
> - src: book Figure 12.22; p.346
> - shows: Figure 12.22: Time-division multiple access (TDMA). Four stations occupy repeating time slots in a common TDMA channel while one station is silent.
> - structure: Four stations occupy repeating time slots in a common TDMA channel while one station is silent.
> - text_in_image: Data; Data; f; f; Station 2; Station 1; • • •; • • •; t; t; f; Common; channel; • • •; t; f; f; Station 3; Station 4; • • •; • • •; t; t; Data; Silent
> - use_when: Teach ch12-12-3-2, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

The main problem with TDMA lies in achieving synchronization between the different
stations. Each station needs to know the beginning of its slot and the location of its slot.
This may be difficult because of propagation delays introduced in the system if the stations are spread over a large area. To compensate for the delays, we can insert guard
times. Synchronization is normally accomplished by having some synchronization bits
(normally referred to as preamble bits) at the beginning of each slot.

In TDMA, the bandwidth is just one channel that is
timeshared  between different stations.

We also need to emphasize that although TDMA and time-division multiplexing
(TDM) conceptually seem the same, there are differences between them. TDM, as we
saw in Chapter 6, is a physical layer technique that combines the data from slower
channels and transmits them by using a faster channel. The process uses a physical
multiplexer that interleaves data units from each channel.
TDMA, on the other hand, is an access method in the data-link layer. The data-link
layer in each station tells its physical layer to use the allocated time slot. There is no
physical multiplexer at the physical layer.

### 12.3.3 CDMA
> id: ch12-12-3-3 | src: book 12.3.3; p.347 | kind: concept

Code-division multiple access (CDMA) was conceived several decades ago. Recent
advances in electronic technology have finally made its implementation possible.
CDMA differs from FDMA in that only one channel occupies the entire bandwidth of
the link. It differs from TDMA in that all stations can send data simultaneously; there is
no timesharing.

In CDMA, one channel carries all transmissions simultaneously.

#### Analogy
> id: ch12-12-3-3-analogy | src: book p.347 | kind: concept

Let us first give an analogy. CDMA simply means communication with different codes.
For example, in a large room with many people, two people can talk privately in English if nobody else understands English. Another two people can talk in Chinese if they
are the only ones who understand Chinese, and so on. In other words, the common
channel, the space of the room in this case, can easily allow communication between
several couples, but in different languages (codes).

#### Idea
> id: ch12-12-3-3-idea | src: book p.347 | kind: concept

Let us assume we have four stations, 1, 2, 3, and 4, connected to the same channel. The
data from station 1 are $d_{1}$, from station 2 are $d_{2}$, and so on. The code assigned to the
first station is $c_{1}$, to the second is $c_{2}$, and so on. We assume that the assigned codes have
two properties.

1. If we multiply each code by another, we get 0.
2. If we multiply each code by itself, we get 4 (the number of stations).

With these two properties in mind, let us see how the above four stations can send data
using the same common channel, as shown in Figure 12.23.
Station 1 multiplies (a special kind of multiplication, as we will see) its data by its
code to get $d_{1}$ ⋅ $c_{1}$. Station 2 multiplies its data by its code to get $d_{2}$ ⋅ $c_{2}$, and so on. The
data that go on the channel are the sum of all these terms, as shown in the box. Any
station that wants to receive data from one of the other three multiplies the data on the
channel by the code of the sender. For example, suppose stations 1 and 2 are talking to
each other. Station 2 wants to hear what station 1 is saying. It multiplies the data on the
channel by $c_{1}$, the code of station 1.
Because ($c_{1}$ ⋅ $c_{1}$) is 4, but ($c_{2}$ ⋅ $c_{1}$), ($c_{3}$ ⋅ $c_{1}$), and ($c_{4}$ ⋅ $c_{1}$) are all 0s, station 2 divides
the result by 4 to get the data from station 1.

#### Chips
> id: ch12-12-3-3-chips | src: book p.347 | kind: concept

CDMA is based on coding theory. Each station is assigned a code, which is a sequence
of numbers called chips, as shown in Figure 12.24. The codes are for the previous
example.
Later in this chapter we show how we chose these sequences. For now, we need to
know that we did not choose the sequences randomly; they were carefully selected.
They are called orthogonal sequences and have the following properties:

> **[ASSET ch12_ill_023]** Figure 12.23: Simple idea of communication with code
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_023.png
> - src: book Figure 12.23; p.348
> - shows: Figure 12.23: Simple idea of communication with code. Four stations multiply data by distinct codes and their coded signals add on the shared channel.
> - structure: Four stations multiply data by distinct codes and their coded signals add on the shared channel.
> - text_in_image: Data; Data; d1; d2; Station 1; Station 2; d1 · c1; d2 · c2; Common; Data; d1 · c1; d2 · c2; d3 · c3; d4 · c4; +; +; +; channel; d3 · c3; d4 · c4; Station 4; Station 3; d3; d4; Data
> - use_when: Teach ch12-12-3-3-idea, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

data = ($d_{1}$ ⋅ $c_{1}$ + $d_{2}$ ⋅ $c_{2}$ + $d_{3}$ ⋅ $c_{3}$ + $d_{4}$ ⋅ $c_{4}$) ⋅ $c_{1}$
= $d_{1}$ ⋅ $c_{1}$ ⋅ $c_{1}$ + $d_{2}$ ⋅ $c_{2}$ ⋅ $c_{1}$ + $d_{3}$ ⋅ $c_{3}$ ⋅ $c_{1}$ + $d_{4}$ ⋅ $c_{4}$ ⋅ $c_{1}$ = 4 × $d_{1}$

> **[ASSET ch12_ill_024]** Figure 12.24: Chip sequences
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_024.png
> - src: book Figure 12.24; p.348
> - shows: Figure 12.24: Chip sequences. Four mutually orthogonal length-four chip sequences C1 through C4 are listed.
> - structure: Four mutually orthogonal length-four chip sequences C1 through C4 are listed.
> - text_in_image: C1; C2; C3; C4; [+1   +1   +1   +1]; [+1   –1   +1  –1]; [+1   +1   –1   –1]; [+1   –1   –1   +1]
> - use_when: Teach ch12-12-3-3-chips, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

1. Each sequence is made of N elements, where N is the number of stations.
2. If we multiply a sequence by a number, every element in the sequence is multiplied
by that element. This is called multiplication of a sequence by a scalar. For example,

2 • [+1 +1 −1 −1] = [+2 +2 −2 −2]

3. If we multiply two equal sequences, element by element, and add the results, we
get N, where N is the number of elements in each sequence. This is called the inner
product of two equal sequences. For example,

[+1 +1 −1 −1] • [+1 +1 −1 −1] = 1 + 1 + 1 + 1 = 4

4. If we multiply two different sequences, element by element, and add the results,
we get 0. This is called the inner product of two different sequences. For example,

[+1 +1 −1 −1] • [+1 +1 +1 +1] = 1 + 1 − 1 − 1 = 0
5. Adding two sequences means adding the corresponding elements. The result is
another sequence. For example,

[+1 +1 −1 −1] + [+1 +1 +1 +1] = [+2 +2  0  0]

#### Data Representation
> id: ch12-12-3-3-data-representation | src: book p.349 | kind: concept

We follow these rules for encoding: If a station needs to send a 0 bit, it encodes it as −1;
if it needs to send a 1 bit, it encodes it as +1. When a station is idle, it sends no signal,
which is interpreted as a 0. These are shown in Figure 12.25.

> **[ASSET ch12_ill_025]** Figure 12.25: Data representation in CDMA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_025.png
> - src: book Figure 12.25; p.349
> - shows: Figure 12.25: Data representation in CDMA. CDMA maps bit 0 to minus one, bit 1 to plus one, and silence to zero before code multiplication.
> - structure: CDMA maps bit 0 to minus one, bit 1 to plus one, and silence to zero before code multiplication.
> - text_in_image: Data bit 0                  –1; Data bit 1                  +1; Silence                   0
> - use_when: Teach ch12-12-3-3-data-representation, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

#### Encoding and Decoding
> id: ch12-12-3-3-encoding-and-decoding | src: book p.349 | kind: concept

As a simple example, we show how four stations share the link during a 1-bit interval.
The procedure can easily be repeated for additional intervals. We assume that stations 1
and 2 are sending a 0 bit and channel 4 is sending a 1 bit. Station 3 is silent. The data at
the sender site are translated to −1, −1, 0, and +1. Each station multiplies the corresponding number by its chip (its orthogonal sequence), which is unique for each station. The
result is a new sequence which is sent to the channel. For simplicity, we assume that all
stations send the resulting sequences at the same time. The sequence on the channel is
the sum of all four sequences as defined before. Figure 12.26 shows the situation.
Now imagine that station 3, which we said is silent, is listening to station 2. Station 3
multiplies the total data on the channel by the code for station 2, which is [+1  −1  +1 −1],
to get

[−1 −1 −3 +1] • [+1 −1 +1 −1] = −4/4 = −1    →  bit 1

#### Signal Level
> id: ch12-12-3-3-signal-level | src: book p.349 | kind: concept

The process can be better understood if we show the digital signal produced by each
station and the data recovered at the destination (see Figure 12.27). The figure shows
the corresponding signals for each station (using NRZ-L for simplicity) and the signal
that is on the common channel.
Figure 12.28 shows how station 3 can detect the data sent by station 2 by using the
code for station 2. The total data on the channel are multiplied (inner product operation) by the signal representing station 2 chip code to get a new signal. The station then
integrates and adds the area under the signal, to get the value −4, which is divided by 4
and interpreted as bit 0.

#### Sequence Generation
> id: ch12-12-3-3-sequence-generation | src: book p.349 | kind: concept

To generate chip sequences, we use a Walsh table, which is a two-dimensional table with
an equal number of rows and columns, as shown in Figure 12.29.

> **[ASSET ch12_ill_026]** Figure 12.26: Sharing channel in CDMA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_026.png
> - src: book Figure 12.26; p.350
> - shows: Figure 12.26: Sharing channel in CDMA. A four-station CDMA example multiplies each station symbol by its chip code and sums the resulting sequences on the shared channel.
> - structure: A four-station CDMA example multiplies each station symbol by its chip code and sums the resulting sequences on the shared channel.
> - text_in_image: Bit 0; Bit 0; –1; –1; C2; C1; Station 1; Station 2; [+1  +1   +1  –1]; [+1  +1   +1  +1]; d1 · c1; d2 · c2; [–1  –1   –1  –1]; [–1  –1   –1  +1]; Common; Data; [–1  –1  –3   +1]; channel; [0     0     0     0]; [+1  –1   –1  +1]; C4; d3 · c3; d4 · c4; C3; [+1 –1 –1 +1]; [+1  +1   –1  –1]; Station 3; Station 4; +1; 0; Silent; Bit 1
> - use_when: Teach ch12-12-3-3-encoding-and-decoding, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

> **[ASSET ch12_ill_027]** Figure 12.27: Digital signal created by four stations in CDMA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_027.png
> - src: book Figure 12.27; p.350
> - shows: Figure 12.27: Digital signal created by four stations in CDMA. Four station waveforms and the composite channel waveform show the chip-by-chip sum for a specific data combination.
> - structure: Four station waveforms and the composite channel waveform show the chip-by-chip sum for a specific data combination.
> - text_in_image: Bit 0; Bit 0; [–1  +1  –1 +1]; [–1  –1 –1 –1]; Station 1; Station 2; Bit 1; Silent; [+1  –1  –1 +1]; [0    0    0    0]; Station 4; Station 3; Data on the channel
> - use_when: Teach ch12-12-3-3-signal-level, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

In the Walsh table, each row is a sequence of chips. $W_{1}$for a one-chip sequence has
one row and one column. We can choose −1 or +1 for the chip for this trivial table (we
chose +1). According to Walsh, if we know the table for N sequences $W_{N}$, we can create
the table for 2N sequences $W_{2}$N, as shown in Figure 12.29. The $W_{N}$ with the overbar $W_{N}$
stands for the complement of $W_{N}$, where each +1 is changed to −1 and vice versa.
Figure 12.29 also shows how we can create $W_{2}$ and $W_{4}$ from $W_{1}$. After we select $W_{1}$, $W_{2}$
can be made from four $W_{1}$s, with the last one the complement of $W_{1}$. After $W_{2}$ is generated, $W_{4}$ can be made of four $W_{2}$s, with the last one the complement of $W_{2}$. Of course,
$W_{8}$ is composed of four $W_{4}$s, and so on. Note that after $W_{N}$ is made, each station is
assigned a chip corresponding to a row.

> **[ASSET ch12_ill_028]** Figure 12.28: Decoding of the composite signal for one in CDMA
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_028.png
> - src: book Figure 12.28; p.351
> - shows: Figure 12.28: Decoding of the composite signal for one in CDMA. The receiver multiplies the composite signal by station 2’s code, sums the products, divides by four, and recovers bit 0.
> - structure: The receiver multiplies the composite signal by station 2’s code, sums the products, divides by four, and recovers bit 0.
> - text_in_image: Station 2’s code; [+1  –1   +1  –1]; Data on the channel; Summing the values; Inner product result; –4; –4; –4/4; –1; Bit 0
> - use_when: Teach ch12-12-3-3-encoding-and-decoding, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

> **[ASSET ch12_ill_029]** Figure 12.29: General rule and examples of creating Walsh tables
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_029.png
> - src: book Figure 12.29; p.351
> - shows: Figure 12.29: General rule and examples of creating Walsh tables. Walsh matrix recursion and the generated W2 and W4 tables show how orthogonal chip sets double in size.
> - structure: Walsh matrix recursion and the generated W2 and W4 tables show how orthogonal chip sets double in size.
> - text_in_image: +1; +1; +1; +1; +1; –1; +1; –1; +1; +1; W4  =; W2  =; WN; WN; +1; +1; +1; –1; –1; –1; +1; W1  =; W2N  =; WN; WN; +1; –1; –1; +1; a. Two basic rules; b. Generation of W2 and W4
> - use_when: Teach ch12-12-3-3-sequence-generation, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

Something we need to emphasize is that the number of sequences, N, needs to be a
power of 2. In other words, we need to have N = $2^{m}$.

The number of sequences in a Walsh table needs to be N = $2^{m}$.

##### Example 12.6
> id: ch12-example-12-6 | src: book Example 12.6; p.351 | kind: worked_example
Find the chips for a network with
a. Two stations
b. Four stations

**Solution**
We can use the rows of $W_{2}$ and $W_{4}$ in Figure 12.29:
a. For a two-station network, we have [+1 +1] and [+1 −1].
b. For a four-station network we have [+1 +1 +1 +1], [+1 −1 +1 −1], [+1 +1 −1 −1], and
[+1 −1 −1 +1].
##### Example 12.7
> id: ch12-example-12-7 | src: book Example 12.7; p.352 | kind: worked_example
What is the number of sequences if we have 90 stations in our network?

**Solution**
The number of sequences needs to be $2^{m}$. We need to choose m = 7 and N = $2^{7}$ or 128. We can
then use 90 of the sequences as the chips.

##### Example 12.8
> id: ch12-example-12-8 | src: book Example 12.8; p.352 | kind: worked_example
Prove that a receiving station can get the data sent by a specific sender if it multiplies the entire
data on the channel by the sender’s chip code and then divides it by the number of stations.

**Solution**
Let us prove this for the first station, using our previous four-station example. We can say that the
data on the channel D = ($d_{1}$ ⋅ $c_{1}$ + $d_{2}$ ⋅ $c_{2}$ + $d_{3}$ ⋅ $c_{3}$+ $d_{4}$ ⋅ $c_{4}$). The receiver that wants to get the data
sent by station 1 multiplies these data by $c_{1}$.

$$
D\cdot c_1=(d_1c_1+d_2c_2+d_3c_3+d_4c_4)\cdot c_1
=d_1N+d_2(0)+d_3(0)+d_4(0)=d_1N.
$$

When we divide the result by N, we get $d_{1}$.

## 12.4 END-CHAPTER MATERIALS
> id: ch12-12-4 | src: book 12.4; p.352 | kind: concept

### 12.4.1 Recommended Reading
> id: ch12-12-4-1 | src: book 12.4.1; p.352 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books and RFCs. The items in brackets […] refer to the reference list at the end of the
text.

#### Books
> id: ch12-12-4-1-books | src: book p.352 | kind: concept

Several excellent books discuss link-layer issues. Among them we recommend [Ham 80],
[Zar 02], [Ror 96], [Tan 03], [GW 04], [For 03], [KMK 04], [Sta 04], [Kes 02],
[PD 03], [Kei 02], [Spu 00], [KCK 98], [Sau 98], [Izz 00], [Per 00], and [WV 00].

#### RFCs
> id: ch12-12-4-1-rfcs | src: book p.352 | kind: concept

A discussion of the use of the checksum in the Internet can be found in RFC 1141.

### 12.4.2 Key Terms
> id: ch12-12-4-2 | src: book 12.4.2; p.353 | kind: concept

- 1-persistent method
- ALOHA
- binary exponential backoff
- carrier sense multiple access (CSMA)
- carrier sense multiple access with collision
- avoidance (CSMA/CA)
- carrier sense multiple access with collision
- detection (CSMA/CD)
- channelization
- code-division multiple access (CDMA)
- collision
- contention
- contention window
- controlled access
- DCF interframe space (DIFS)
- frequency-division multiple access (FDMA)
- inner product
- interface space (IFS)
- jamming signal
- media access control (MAC)
- multiple access (MA)
- network allocation vector (NAV)
- nonpersistent method
- orthogonal sequence
- p-persistent method
- polling
- primary station
- propagation time
- pure ALOHA
- random access
- reservation
- secondary station
- short interframe space (SIFS)
- slotted ALOHA
- time-division multiple access (TDMA)
- token
- token passing
- vulnerable time
- Walsh table

### 12.4.3 Summary
> id: ch12-12-4-3 | src: book 12.4.3; p.353 | kind: summary

Many formal protocols have been devised to handle access to a shared link. We categorize them into three groups: random access protocols, controlled access protocols, and
channelization protocols.
In random access or contention methods, no station is superior to another station
and none is assigned the control over another.  ALOHA allows multiple access (MA) to
the shared medium.There are potential collisions in this arrangement. To minimize the
chance of collision and, therefore, increase the performance, the CSMA method was
developed. The chance of collision can be reduced if a station senses the medium
before trying to use it. Carrier sense multiple access (CSMA) requires that each station
first listen to the medium before sending. Carrier sense multiple access with collision
detection (CSMA/CD) augments the CSMA algorithm to handle collision. In this
method, a station monitors the medium after it sends a frame to see if the transmission
was successful. If so, the station is finished. If, however, there is a collision, the frame
is sent again. To avoid collisions on wireless networks, carrier sense multiple access with
collision avoidance (CSMA/CA) was invented. Collisions are avoided through the use
of three strategies: the interframe space, the contention window, and acknowledgments.
In controlled access, the stations consult one another to find which station has the
right to send. A station cannot send unless it has been authorized by other stations. We
discussed three popular controlled-access methods: reservation, polling, and token
passing. In the reservation access method, a station needs to make a reservation before
sending data. Time is divided into intervals. In each interval, a reservation frame precedes the data frames sent in that interval. In the polling method, all data exchanges
must be made through the primary device even when the ultimate destination is a secondary device. The primary device controls the link; the secondary devices follow its
instructions. In the token-passing method, the stations in a network are organized in a
logical ring. Each station has a predecessor and a successor. A special packet called a
token circulates through the ring.
Channelization is a multiple-access method in which the available bandwidth of a
link is shared in time, frequency, or through code, between different stations. We discussed three channelization protocols: FDMA, TDMA, and CDMA. In frequency-division multiple access (FDMA), the available bandwidth is divided into frequency
bands. Each station is allocated a band to send its data. In other words, each band is
reserved for a specific station, and it belongs to the station all the time. In time-division
multiple access (TDMA), the stations share the bandwidth of the channel in time. Each
station is allocated a time slot during which it can send data. Each station transmits its
data in its assigned time slot. In code-division multiple access (CDMA), the stations use
different codes to achieve multiple access. CDMA is based on coding theory and uses
sequences of numbers called chips. The sequences are generated using orthogonal
codes such as the Walsh tables.
