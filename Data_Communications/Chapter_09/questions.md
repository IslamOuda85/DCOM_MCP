---
doc_type: question_bank
course_id: data_communications
chapter: 9
chapter_id: data_communications_ch09
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 14
- id: Problems
  label: Problems
  count: 15
question_counts:
  Questions: 14
  Problems: 15
spec_version: 1.1-controller
generated_at: '2026-10-07T03:32:00+00:00'
status: complete
---
## Questions

### Q9-1
> id: ch09-q-q9-1 | type: review_question | group: Questions | ref_sections: [ch09-9-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

Distinguish between communication at the network layer and communication at the data-link layer.

### Q9-2
> id: ch09-q-q9-2 | type: review_question | group: Questions | ref_sections: [ch09-9-1-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

Distinguish between a point-to-point link and a broadcast link.

### Q9-3
> id: ch09-q-q9-3 | type: review_question | group: Questions | ref_sections: [ch09-9-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

Can two hosts in two different networks have the same link-layer address? Explain.

### Q9-4
> id: ch09-q-q9-4 | type: review_question | group: Questions | ref_sections: [ch09-9-2-2-packet-format] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

Is the size of the ARP packet fixed? Explain.

### Q9-5
> id: ch09-q-q9-5 | type: review_question | group: Questions | ref_sections: [ch09-9-2-2-packet-format] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

What is the size of an ARP packet when the protocol is IPv4 and the hardware is Ethernet?

### Q9-6
> id: ch09-q-q9-6 | type: review_question | group: Questions | ref_sections: [ch09-9-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

Assume we have an isolated link (not connected to any other link) such as a private network in a company. Do we still need addresses in both the network layer and the data-link layer? Explain.

### Q9-7
> id: ch09-q-q9-7 | type: review_question | group: Questions | ref_sections: [ch09-example-9-4] | has_figure: true | answer: null | figure_assets: [ch09_ill_009] | src: book p.253

In Figure 9.9, why is the destination hardware address all 0s in the ARP request message?

> [ASSET_REF ch09_ill_009] See the original figure and its description in assets/manifest.json.

### Q9-8
> id: ch09-q-q9-8 | type: review_question | group: Questions | ref_sections: [ch09-example-9-4] | has_figure: true | answer: null | figure_assets: [ch09_ill_009] | src: book p.253

In Figure 9.9, why is the destination hardware address of the frame from A to B a broadcast address?

> [ASSET_REF ch09_ill_009] See the original figure and its description in assets/manifest.json.

### Q9-9
> id: ch09-q-q9-9 | type: review_question | group: Questions | ref_sections: [ch09-example-9-4] | has_figure: true | answer: null | figure_assets: [ch09_ill_009] | src: book p.253

In Figure 9.9, how does system A know what the link-layer address of system B is when it receives the ARP reply?

> [ASSET_REF ch09_ill_009] See the original figure and its description in assets/manifest.json.

### Q9-10
> id: ch09-q-q9-10 | type: review_question | group: Questions | ref_sections: [ch09-9-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.253

When we talk about the broadcast address in a link, do we mean sending a message to all hosts and routers in the link or to all hosts and routers in the Internet? In other words, does a broadcast address have a local jurisdiction or a universal jurisdiction? Explain.

### Q9-11
> id: ch09-q-q9-11 | type: review_question | group: Questions | ref_sections: [ch09-9-2-2, ch09-9-2-2-caching] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

Why does a host or a router need to run the ARP program all of the time in the background?

### Q9-12
> id: ch09-q-q9-12 | type: review_question | group: Questions | ref_sections: [ch09-9-1-1, ch09-9-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

Why does a router normally have more than one interface?

### Q9-13
> id: ch09-q-q9-13 | type: review_question | group: Questions | ref_sections: [ch09-9-2-3-changes-in-addresses] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

Why is it better not to change an end-to-end address from the source to the destination?

### Q9-14
> id: ch09-q-q9-14 | type: review_question | group: Questions | ref_sections: [ch09-9-2, ch09-9-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

How many IP addresses and how many link-layer addresses should a router have when it is connected to five links?

## Problems

### P9-1
> id: ch09-q-p9-1 | type: problem | group: Problems | ref_sections: [ch09-9-1-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

Assume we have an internet (a private small internet) in which all hosts are connected in a mesh topology. Do we need routers in this internet? Explain.

### P9-2
> id: ch09-q-p9-2 | type: problem | group: Problems | ref_sections: [ch09-9-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

In the previous problem, do we need both network and data-link layers?

### P9-3
> id: ch09-q-p9-3 | type: problem | group: Problems | ref_sections: [ch09-9-1-1] | has_figure: true | answer: null | figure_assets: [ch09_ill_015] | src: book p.254

Explain why we do not need the router in Figure 9.15.

> **[ASSET ch09_ill_015]** Figure 9.15: Problem 9-3
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_015.png
> - src: book Figure 9.15; p.254
> - shows: Figure 9.15: Problem 9-3. Problem P9-3 shows two end systems connected through one router on a single continuous link, inviting the student to decide why the router is unnecessary.
> - structure: Problem P9-3 shows two end systems connected through one router on a single continuous link, inviting the student to decide why the router is unnecessary.
> - text_in_image: No text labels appear in the source figure.
> - use_when: Teach ch09-q-p9-3, interpret Figure 9.15, trace address changes, or solve a linked practice question.
> - confidence: high

### P9-4
> id: ch09-q-p9-4 | type: problem | group: Problems | ref_sections: [ch09-9-1-1] | has_figure: true | answer: null | figure_assets: [ch09_ill_016] | src: book p.254

Explain why we may need a router in Figure 9.16.

> **[ASSET ch09_ill_016]** Figure 9.16: Problem 9-4
> - type: illustration
> - kind: diagram
> - file: assets/ch09_ill_016.png
> - src: book Figure 9.16; p.254
> - shows: Figure 9.16: Problem 9-4. Problem P9-4 shows Alice and Bob on two separate site links joined by router R, inviting the student to explain why routing may be required.
> - structure: Problem P9-4 shows Alice and Bob on two separate site links joined by router R, inviting the student to explain why routing may be required.
> - text_in_image: Alice; Bob; R; Alice’s site; Bob’s site
> - use_when: Teach ch09-q-p9-4, interpret Figure 9.16, trace address changes, or solve a linked practice question.
> - confidence: high

### P9-5
> id: ch09-q-p9-5 | type: problem | group: Problems | ref_sections: [ch09-9-1-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

Is the current Internet using circuit-switching or packet-switching at the data-link layer? Explain.

### P9-6
> id: ch09-q-p9-6 | type: problem | group: Problems | ref_sections: [ch09-9-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

Assume Alice is travelling from 2020 Main Street in Los Angeles to 1432 American Boulevard in Chicago. If she is travelling by air from Los Angeles Airport to Chicago Airport,

**a.** find the end-to-end addresses in this scenario.

**b.** find the link-layer addresses in this scenario.

### P9-7
> id: ch09-q-p9-7 | type: problem | group: Problems | ref_sections: [ch09-9-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

In the previous problem, assume Alice cannot find a direct flight from Los Angeles to Chicago. If she needs to change flights in Denver,

**a.** find the end-to-end addresses in this scenario.

**b.** find the link-layer addresses in this scenario.

### P9-8
> id: ch09-q-p9-8 | type: problem | group: Problems | ref_sections: [ch09-9-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.254

When we send a letter using the services provided by the post office, do we use an end-to-end address? Does the post office necessarily use an end-to-end address to deliver the mail? Explain.

### P9-9
> id: ch09-q-p9-9 | type: problem | group: Problems | ref_sections: [ch09-9-2-3] | has_figure: true | answer: null | figure_assets: [ch09_ill_005] | src: book p.255

In Figure 9.5, assume Link 2 is broken. How can Alice communicate with Bob?

> [ASSET_REF ch09_ill_005] See the original figure and its description in assets/manifest.json.

### P9-10
> id: ch09-q-p9-10 | type: problem | group: Problems | ref_sections: [ch09-9-2-3, ch09-9-2-3-changes-in-addresses] | has_figure: true | answer: null | figure_assets: [ch09_ill_005] | src: book p.255

In Figure 9.5, show the process of frame change in routers R1 and R2.

> [ASSET_REF ch09_ill_005] See the original figure and its description in assets/manifest.json.

### P9-11
> id: ch09-q-p9-11 | type: problem | group: Problems | ref_sections: [ch09-9-2-2] | has_figure: true | answer: null | figure_assets: [ch09_ill_007] | src: book p.255

In Figure 9.7, assume system B is not running the ARP program. What would happen?

> [ASSET_REF ch09_ill_007] See the original figure and its description in assets/manifest.json.

### P9-12
> id: ch09-q-p9-12 | type: problem | group: Problems | ref_sections: [ch09-9-2-2-caching] | has_figure: true | answer: null | figure_assets: [ch09_ill_007] | src: book p.255

In Figure 9.7, do you think that system A should first check its cache for mapping from N2 to L2 before even broadcasting the ARP request?

> [ASSET_REF ch09_ill_007] See the original figure and its description in assets/manifest.json.

### P9-13
> id: ch09-q-p9-13 | type: problem | group: Problems | ref_sections: [ch09-9-2-2] | has_figure: true | answer: null | figure_assets: [ch09_ill_007] | src: book p.255

Assume the network in Figure 9.7 does not support broadcasting. What do you suggest for sending the ARP request in this network?

> [ASSET_REF ch09_ill_007] See the original figure and its description in assets/manifest.json.

### P9-14
> id: ch09-q-p9-14 | type: problem | group: Problems | ref_sections: [ch09-9-2-3-activities-at-alice-s-site, ch09-9-2-3-activities-at-router-r1, ch09-9-2-3-activities-at-router-r2] | has_figure: true | answer: null | figure_assets: [ch09_ill_011, ch09_ill_012, ch09_ill_013] | src: book p.255

In Figures 9.11 to 9.13, both the forwarding table and ARP are doing a kind of mapping. Show the difference between them by listing the input and output of mapping for a forwarding table and ARP.

> [ASSET_REF ch09_ill_011] See the original figure and its description in assets/manifest.json.

> [ASSET_REF ch09_ill_012] See the original figure and its description in assets/manifest.json.

> [ASSET_REF ch09_ill_013] See the original figure and its description in assets/manifest.json.

### P9-15
> id: ch09-q-p9-15 | type: problem | group: Problems | ref_sections: [ch09-9-1-1, ch09-9-2-2] | has_figure: true | answer: null | figure_assets: [ch09_ill_007] | src: book p.255

Figure 9.7 shows a system as either a host or a router. What would be the actual entity (host or router) of system A and B in each of the following cases:

**a.** If the link is the first one in the path?

**b.** If the link is the middle one in the path?

**c.** If the link is the last one in the path?

**d.** If there is only one link in the path (local communication)?

> [ASSET_REF ch09_ill_007] See the original figure and its description in assets/manifest.json.
