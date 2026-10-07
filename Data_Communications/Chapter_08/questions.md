---
doc_type: question_bank
course_id: data_communications
chapter: 8
chapter_id: data_communications_ch08
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 10
- id: Problems
  label: Problems
  count: 16
question_counts:
  Questions: 10
  Problems: 16
spec_version: 1.1-controller
generated_at: '2026-10-07T03:27:03+00:00'
status: complete
---
## Questions

### Q8-1
> id: ch08-q-q8-1 | type: review_question | group: Questions | ref_sections: [ch08-8-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

Describe the need for switching and define a switch.

### Q8-2
> id: ch08-q-q8-2 | type: review_question | group: Questions | ref_sections: [ch08-8-1-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

List the three traditional switching methods. Which are the most common today?

### Q8-3
> id: ch08-q-q8-3 | type: review_question | group: Questions | ref_sections: [ch08-8-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

What are the two approaches to packet switching?

### Q8-4
> id: ch08-q-q8-4 | type: review_question | group: Questions | ref_sections: [ch08-8-2, ch08-8-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

Compare and contrast a circuit-switched network and a packet-switched network.

### Q8-5
> id: ch08-q-q8-5 | type: review_question | group: Questions | ref_sections: [ch08-8-3-1-destination-address, ch08-8-3-1-routing-table] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

What is the role of the address field in a packet traveling through a datagram network?

### Q8-6
> id: ch08-q-q8-6 | type: review_question | group: Questions | ref_sections: [ch08-8-3-2-virtual-circuit-identifier] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

What is the role of the address field in a packet traveling through a virtual-circuit network?

### Q8-7
> id: ch08-q-q8-7 | type: review_question | group: Questions | ref_sections: [ch08-8-4-1-space-division-switch, ch08-8-4-1-time-division-switch] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

Compare space-division and time-division switches.

### Q8-8
> id: ch08-q-q8-8 | type: review_question | group: Questions | ref_sections: [ch08-8-4-1-time-slot-interchange] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

What is TSI and what is its role in time-division switching?

### Q8-9
> id: ch08-q-q8-9 | type: review_question | group: Questions | ref_sections: [ch08-8-4-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

Compare and contrast the two major categories of circuit switches.

### Q8-10
> id: ch08-q-q8-10 | type: review_question | group: Questions | ref_sections: [ch08-8-4-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

List four major components of a packet switch and their functions.

## Problems

### P8-1
> id: ch08-q-p8-1 | type: problem | group: Problems | ref_sections: [ch08-8-2-1, ch08-8-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.231

A path in a digital circuit-switched network has a data rate of 1 Mbps. The exchange of 1000 bits is required for the setup and teardown phases. The distance between two parties is 5000 km. Answer the following questions if the propagation speed is 2 × $10^{8}$ m/s:

**a.** What is the total delay if 1000 bits of data are exchanged during the data-transfer phase?

**b.** What is the total delay if 100,000 bits of data are exchanged during the data-transfer phase?

**c.** What is the total delay if 1,000,000 bits of data are exchanged during the data-transfer phase?

**d.** Find the delay per 1000 bits of data for each of the above cases and compare them. What can you infer?

### P8-2
> id: ch08-q-p8-2 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-delay] | has_figure: false | answer: null | figure_assets: [] | src: book p.232

Five equal-size datagrams belonging to the same message leave for the destination one after another. However, they travel through different paths as shown in Table 8.1.

**Table 8.1: Datagram paths used in Problem P8-2**

| Datagram | Path Length | Visited Switches |
| --- | --- | --- |
| 1 | 3200 km | 1, 3, 5 |
| 2 | 11,700 km | 1, 2, 5 |
| 3 | 12,200 km | 1, 2, 3, 5 |
| 4 | 10,200 km | 1, 4, 5 |
| 5 | 10,700 km | 1, 4, 3, 5 |
### P8-3
> id: ch08-q-p8-3 | type: problem | group: Problems | ref_sections: [ch08-8-2-1, ch08-8-3-1, ch08-8-3-2-three-phases] | has_figure: false | answer: null | figure_assets: [] | src: book p.232

Transmission of information in any network involves end-to-end addressing and sometimes local addressing (such as VCI). Table 8.2 shows the types of networks and the addressing mechanism used in each of them. Table 8.2 P8-3 Network Setup Data Transfer Teardown Circuit-switched End-to-end End-to-end Datagram End-to-end Virtual-circuit End-to-end Local End-to-end Answer the following questions:

**a.** Why does a circuit-switched network need end-to-end addressing during the setup and teardown phases? Why are no addresses needed during the data transfer phase for this type of network?

**b.** Why does a datagram network need only end-to-end addressing during the data transfer phase, but no addressing during the setup and teardown phases?

**c.** Why does a virtual-circuit network need addresses during all three phases?


**Table 8.2: Addressing by network phase**

| Network | Setup | Data Transfer | Teardown |
| --- | --- | --- | --- |
| Circuit-switched | End-to-end |  | End-to-end |
| Datagram |  | End-to-end |  |
| Virtual-circuit | End-to-end | Local | End-to-end |
### P8-4
> id: ch08-q-p8-4 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-routing-table, ch08-8-3-2-data-transfer-phase] | has_figure: false | answer: null | figure_assets: [] | src: book p.232

We mentioned that two types of networks, datagram and virtual-circuit, need a routing or switching table to find the output port from which the information belonging to a destination should be sent out, but a circuit-switched network has no need for such a table. Give the reason for this difference.

### P8-5
> id: ch08-q-p8-5 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-routing-table, ch08-8-3-2-three-phases] | has_figure: false | answer: null | figure_assets: [] | src: book p.233

An entry in the switching table of a virtual-circuit network is normally created during the setup phase and deleted during the teardown phase. In other words, the entries in this type of network reflect the current connections, the activity in the network. In contrast, the entries in a routing table of a datagram network do not depend on the current connections; they show the configuration of the network and how any packet should be routed to a final destination. The entries may remain the same even if there is no activity in the network. The routing tables, however, are updated if there are changes in the network. Can you explain the reason for these two different characteristics? Can we say that a virtual-circuit is a connection-oriented network and a datagram network is a connectionless network because of the above characteristics?

### P8-6
> id: ch08-q-p8-6 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-routing-table, ch08-8-3-2-data-transfer-phase] | has_figure: false | answer: null | figure_assets: [] | src: book p.233

The minimum number of columns in a datagram network is two; the minimum number of columns in a virtual-circuit network is four. Can you explain the reason? Is the difference related to the type of addresses carried in the packets of each network?

### P8-7
> id: ch08-q-p8-7 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-routing-table] | has_figure: true | answer: null | figure_assets: [ch08_ill_027] | src: book p.233

Figure 8.27 shows a switch (router) in a datagram network. Find the output port for packets with the following destination addresses:

**a.** Packet 1: 7176

**b.** Packet 2: 1233

**c.** Packet 3: 8766

**d.** Packet 4: 9144

> **[ASSET ch08_ill_027]** Figure 8.27: Problem P8-7
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_027.png
> - src: book Figure 8.27; p.233
> - shows: Figure 8.27: Problem P8-7. Problem P8-7 pairs a destination-to-port routing table with a four-port router for four lookup exercises.
> - structure: Problem P8-7 pairs a destination-to-port routing table with a four-port router for four lookup exercises.
> - text_in_image: Output; Destination; port; address; 1233; 3; 1456; 2; 1; 4; 3255; 1; 4470; 4; 7176; 2; 3; 2; 8766; 3; 9144; 2
> - use_when: Teach ch08-q-p8-7, interpret Figure 8.27, trace a switching path, or solve a linked practice question.
> - confidence: high

### P8-8
> id: ch08-q-p8-8 | type: problem | group: Problems | ref_sections: [ch08-8-3-2-data-transfer-phase] | has_figure: true | answer: null | figure_assets: [ch08_ill_028] | src: book p.233

Figure 8.28 shows a switch in a virtual-circuit network. Find the output port and the output VCI for packets with the following input port and input VCI addresses:

**a.** Packet 1: 3, 78

**b.** Packet 2: 2, 92

**c.** Packet 3: 4, 56

**d.** Packet 4: 2, 71

> **[ASSET ch08_ill_028]** Figure 8.28: Problem P8-8
> - type: illustration
> - kind: diagram
> - file: assets/ch08_ill_028.png
> - src: book Figure 8.28; p.233
> - shows: Figure 8.28: Problem P8-8. Problem P8-8 pairs an incoming-port/VCI to outgoing-port/VCI switching table with a four-port virtual-circuit switch.
> - structure: Problem P8-8 pairs an incoming-port/VCI to outgoing-port/VCI switching table with a four-port virtual-circuit switch.
> - text_in_image: Incoming; Outgoing; Port; Port; VCI; VCI; 1; 14; 3; 22; 1; 4; 2; 71; 4; 41; 2; 92; 1; 45; 3; 58; 2; 43; 3; 2; 3; 78; 2; 70; 4; 56; 3; 11
> - use_when: Teach ch08-q-p8-8, interpret Figure 8.28, trace a switching path, or solve a linked practice question.
> - confidence: high

### P8-9
> id: ch08-q-p8-9 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-routing-table, ch08-8-3-2-data-transfer-phase] | has_figure: false | answer: null | figure_assets: [] | src: book p.233

Answer the following questions:

**a.** Can a routing table in a datagram network have two entries with the same destination address? Explain.

**b.** Can a switching table in a virtual-circuit network have two entries with the same input port number? With the same output port number? With the same incoming VCIs? With the same outgoing VCIs? With the same incoming values (port, VCI)? With the same outgoing values (port, VCI)?

### P8-10
> id: ch08-q-p8-10 | type: problem | group: Problems | ref_sections: [ch08-8-3-1-routing-table, ch08-8-3-2-data-transfer-phase] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

It is obvious that a router or a switch needs to search to find information in the corresponding table. The searching in a routing table for a datagram network is based on the destination address; the searching in a switching table in a virtual-circuit network is based on the combination of incoming port and incoming VCI. Explain the reason and define how these tables must be ordered (sorted) based on these values.
### P8-11
> id: ch08-q-p8-11 | type: problem | group: Problems | ref_sections: [ch08-8-4-1-crossbar-switch] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

Consider an $n \times k$ crossbar switch with $n$ inputs and $k$ outputs.

**a.** Can we say that the switch acts as a multiplexer if $n>k$?

**b.** Can we say that the switch acts as a demultiplexer if $n<k$?
### P8-12
> id: ch08-q-p8-12 | type: problem | group: Problems | ref_sections: [ch08-8-4-1-multistage-switch] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

We need a three-stage space-division switch with $N=100$. We use 10 crossbars at the first and third stages and 4 crossbars at the middle stage.

**a.** Draw the configuration diagram.

**b.** Calculate the total number of crosspoints.

**c.** Find the possible number of simultaneous connections.

**d.** Find the possible number of simultaneous connections if we use a single crossbar ($100 \times 100$).

**e.** Find the blocking factor, the ratio of the number of connections in part c and in part d.
### P8-13
> id: ch08-q-p8-13 | type: problem | group: Problems | ref_sections: [ch08-8-4-1-multistage-switch] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

Repeat Problem P8-12 if we use 6 crossbars at the middle stage.
### P8-14
> id: ch08-q-p8-14 | type: problem | group: Problems | ref_sections: [ch08-8-4-1-multistage-switch] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

Redesign the configuration of Problem P8-12 using the Clos criteria.
### P8-15
> id: ch08-q-p8-15 | type: problem | group: Problems | ref_sections: [ch08-8-4-1-crossbar-switch, ch08-8-4-1-multistage-switch] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

We need to have a space-division switch with 1000 inputs and outputs. What is the total number of crosspoints in each of the following cases?

**a.** Using a single crossbar.

**b.** Using a multistage switch based on the Clos criteria.
### P8-16
> id: ch08-q-p8-16 | type: problem | group: Problems | ref_sections: [ch08-8-4-1-time-and-space-division-switch-combinations] | has_figure: false | answer: null | figure_assets: [] | src: book p.234

We need a three-stage time-space-time switch with $N=100$. We use 10 TSIs at the first and third stages and 4 crossbars at the middle stage.

**a.** Draw the configuration diagram.

**b.** Calculate the total number of crosspoints.

**c.** Calculate the total number of memory locations we need for the TSIs.
