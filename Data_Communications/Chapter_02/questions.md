---
doc_type: question_bank
course_id: data_communications
chapter: 2
chapter_id: data_communications_ch02
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 15
- id: Problems
  label: Problems
  count: 15
question_counts:
  Questions: 15
  Problems: 15
spec_version: 1.1-controller
generated_at: '2026-10-06T21:45:17+00:00'
status: complete
---
## Questions

### Q2-1
> id: ch02-q-q2-1 | type: review_question | group: Questions | ref_sections: [ch02-2-1-2-first-principle] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

What is the first principle we discussed in this chapter for protocol layering that needs to be followed to make the communication bidirectional?

### Q2-2
> id: ch02-q-q2-2 | type: review_question | group: Questions | ref_sections: [ch02-2-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

Which layers of the TCP/IP protocol suite are involved in a link-layer switch?

### Q2-3
> id: ch02-q-q2-3 | type: review_question | group: Questions | ref_sections: [ch02-2-2-1, ch02-2-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

A router connects three links (networks). How many of each of the following layers can the router be involved with?

**a.** physical layer

**b.** data-link layer

**c.** network layer

### Q2-4
> id: ch02-q-q2-4 | type: review_question | group: Questions | ref_sections: [ch02-2-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

In the TCP/IP protocol suite, what are the identical objects at the sender and the receiver sites when we think about the logical connection at the application layer?

### Q2-5
> id: ch02-q-q2-5 | type: review_question | group: Questions | ref_sections: [ch02-2-2-2, ch02-2-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

A host communicates with another host using the TCP/IP protocol suite. What is the unit of data sent or received at each of the following layers?

**a.** application layer

**b.** network layer

**c.** data-link layer

### Q2-6
> id: ch02-q-q2-6 | type: review_question | group: Questions | ref_sections: [ch02-2-2-4] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

Which of the following data units is encapsulated in a frame?

**a.** a user datagram

**b.** a datagram

**c.** a segment

### Q2-7
> id: ch02-q-q2-7 | type: review_question | group: Questions | ref_sections: [ch02-2-2-3-transport-layer, ch02-2-2-4] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

Which of the following data units is decapsulated from a user datagram?

**a.** a datagram

**b.** a segment

**c.** a message

### Q2-8
> id: ch02-q-q2-8 | type: review_question | group: Questions | ref_sections: [ch02-2-2-3-transport-layer, ch02-2-2-4] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

Which of the following data units has an application-layer message plus the header from layer 4?

**a.** a frame

**b.** a user datagram

**c.** a bit

### Q2-9
> id: ch02-q-q2-9 | type: review_question | group: Questions | ref_sections: [ch02-2-2-3-application-layer] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

List some application-layer protocols mentioned in this chapter.

### Q2-10
> id: ch02-q-q2-10 | type: review_question | group: Questions | ref_sections: [ch02-2-2-3-transport-layer] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

If a port number is 16 bits (2 bytes), what is the minimum header size at the transport layer of the TCP/IP protocol suite?

### Q2-11
> id: ch02-q-q2-11 | type: review_question | group: Questions | ref_sections: [ch02-2-2-5] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.17

What are the types of addresses (identifiers) used in each of the following layers?

**a.** application layer

**b.** network layer

**c.** data-link layer

### Q2-12
> id: ch02-q-q2-12 | type: review_question | group: Questions | ref_sections: [ch02-2-2-6] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

When we say that the transport layer multiplexes and demultiplexes application-layer messages, do we mean that a transport-layer protocol can combine several messages from the application layer in one packet? Explain.

### Q2-13
> id: ch02-q-q2-13 | type: review_question | group: Questions | ref_sections: [ch02-2-2-6] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Can you explain why we did not mention multiplexing/demultiplexing services for the application layer?

### Q2-14
> id: ch02-q-q2-14 | type: review_question | group: Questions | ref_sections: [ch02-2-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Assume we want to connect two isolated hosts together to let each host communicate with the other. Do we need a link-layer switch between the two? Explain.

### Q2-15
> id: ch02-q-q2-15 | type: review_question | group: Questions | ref_sections: [ch02-2-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

If there is a single path between the source host and the destination host, do we need a router between the two hosts?

## Problems

### P2-1
> id: ch02-q-p2-1 | type: problem | group: Problems | ref_sections: [ch02-2-1-1-second-scenario] | has_figure: true | answer: null | figure_assets: [ch02_ill_002] | src: book PDF pp.18

Answer the following questions about Figure 2.2 when the communication is from Maria to Ann:

**a.** What is the service provided by layer 1 to layer 2 at Maria’s site?

**b.** What is the service provided by layer 1 to layer 2 at Ann’s site?

> [ASSET_REF ch02_ill_002] See the original figure and its description in assets/manifest.json.

### P2-2
> id: ch02-q-p2-2 | type: problem | group: Problems | ref_sections: [ch02-2-1-1-second-scenario] | has_figure: true | answer: null | figure_assets: [ch02_ill_002] | src: book PDF pp.18

Answer the following questions about Figure 2.2 when the communication is from Maria to Ann:

**a.** What is the service provided by layer 2 to layer 3 at Maria’s site?

**b.** What is the service provided by layer 2 to layer 3 at Ann’s site?

> [ASSET_REF ch02_ill_002] See the original figure and its description in assets/manifest.json.

### P2-3
> id: ch02-q-p2-3 | type: problem | group: Problems | ref_sections: [ch02-2-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Assume that the number of hosts connected to the Internet at year 2010 is five hundred million. If the number of hosts increases only 20 percent per year, what is the number of hosts in year 2020?

### P2-4
> id: ch02-q-p2-4 | type: problem | group: Problems | ref_sections: [ch02-2-2-4] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Assume a system uses five protocol layers. If the application program creates a message of 100 bytes and each layer (including the fifth and the first) adds a header of 10 bytes to the data unit, what is the efficiency (the ratio of application-layer bytes to the number of bytes transmitted) of the system?

### P2-5
> id: ch02-q-p2-5 | type: problem | group: Problems | ref_sections: [ch02-2-2-2, ch02-2-2-3-network-layer] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Assume we have created a packet-switched internet. Using the TCP/IP protocol suite, we need to transfer a huge file. What are the advantage and disadvantage of sending large packets?

### P2-6
> id: ch02-q-p2-6 | type: problem | group: Problems | ref_sections: [ch02-2-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Match the following to one or more layers of the TCP/IP protocol suite:

**a.** route determination

**b.** connection to transmission media

**c.** providing services for the end user

### P2-7
> id: ch02-q-p2-7 | type: problem | group: Problems | ref_sections: [ch02-2-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.18

Match the following to one or more layers of the TCP/IP protocol suite:

**a.** creating user datagrams

**b.** responsibility for handling frames between adjacent nodes

**c.** transforming bits to electromagnetic signals

### P2-8
> id: ch02-q-p2-8 | type: problem | group: Problems | ref_sections: [ch02-2-2-6] | has_figure: true | answer: null | figure_assets: [ch02_ill_010] | src: book PDF pp.18

In Figure 2.10, when the IP protocol decapsulates the transport-layer packet, how does it know to which upper-layer protocol (UDP or TCP) the packet should be delivered?

> [ASSET_REF ch02_ill_010] See the original figure and its description in assets/manifest.json.

### P2-9
> id: ch02-q-p2-9 | type: problem | group: Problems | ref_sections: [ch02-2-2-6] | has_figure: true | answer: null | figure_assets: [ch02_ill_010] | src: book PDF pp.18,19

Assume a private internet uses three different protocols at the data-link layer (L1, L2, and L3). Redraw Figure 2.10 with this assumption. Can we say that, in the data-link layer, we have demultiplexing at the source node and multiplexing at the destination node?

> [ASSET_REF ch02_ill_010] See the original figure and its description in assets/manifest.json.

### P2-10
> id: ch02-q-p2-10 | type: problem | group: Problems | ref_sections: [ch02-2-2-1, ch02-2-2-3-application-layer] | has_figure: true | answer: null | figure_assets: [ch02_ill_004] | src: book PDF pp.19

Assume that a private internet requires that the messages at the application layer be encrypted and decrypted for security purposes. If we need to add some information about the encryption/decryption process (such as the algorithms used in the process), does it mean that we are adding one layer to the TCP/IP protocol suite? Redraw the TCP/IP layers (Figure 2.4 part b) if you think so.

> [ASSET_REF ch02_ill_004] See the original figure and its description in assets/manifest.json.

### P2-11
> id: ch02-q-p2-11 | type: problem | group: Problems | ref_sections: [ch02-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.19

Protocol layering can be found in many aspects of our lives such as air travelling. Imagine you make a round-trip to spend some time on vacation at a resort. You need to go through some processes at your city airport before flying. You also need to go through some processes when you arrive at the resort airport. Show the protocol layering for the round trip using some layers such as baggage checking/claiming, boarding/unboarding, takeoff/landing.

### P2-12
> id: ch02-q-p2-12 | type: problem | group: Problems | ref_sections: [ch02-2-3-1] | has_figure: true | answer: null | figure_assets: [ch02_ill_004] | src: book PDF pp.19

The presentation of data is becoming more and more important in today’s Internet. Some people argue that the TCP/IP protocol suite needs to add a new layer to take care of the presentation of data. If this new layer is added in the future, where should its position be in the suite? Redraw Figure 2.4 to include this layer.

> [ASSET_REF ch02_ill_004] See the original figure and its description in assets/manifest.json.

### P2-13
> id: ch02-q-p2-13 | type: problem | group: Problems | ref_sections: [ch02-2-2-3-data-link-layer, ch02-2-2-3-physical-layer] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.19

In an internet, we change the LAN technology to a new one. Which layers in the TCP/IP protocol suite need to be changed?

### P2-14
> id: ch02-q-p2-14 | type: problem | group: Problems | ref_sections: [ch02-2-2-3-transport-layer, ch02-2-2-3-application-layer] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.19

Assume that an application-layer protocol is written to use the services of UDP. Can the application-layer protocol uses the services of TCP without change?

### P2-15
> id: ch02-q-p2-15 | type: problem | group: Problems | ref_sections: [ch02-2-2-1] | has_figure: true | answer: null | figure_assets: [ch01_ill_011] | src: book PDF pp.19

Using the internet in Figure 1.11 (Chapter 1) in the text, show the layers of the TCP/IP protocol suite and the flow of data when two hosts, one on the west coast and the other on the east coast, exchange messages.

> [ASSET_REF ch01_ill_011] Cross-chapter reference to the reviewed source Figure 1.11.
