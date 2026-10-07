---
doc_type: question_bank
course_id: data_communications
chapter: 13
chapter_id: data_communications_ch13
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 10
- id: Problems
  label: Problems
  count: 11
question_counts:
  Questions: 10
  Problems: 11
spec_version: 1.1-controller
generated_at: '2026-10-07T03:54:04+00:00'
status: complete
---
## Questions

### Q13-1
> id: ch13-q-q13-1 | type: review_question | group: Questions | ref_sections: [ch13-13-2-6-no-need-for-csma-cd] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

Why is there no need for CSMA/CD on a full-duplex Ethernet LAN?

### Q13-2
> id: ch13-q-q13-2 | type: review_question | group: Questions | ref_sections: [ch13-13-1-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

Compare the data rates for Standard Ethernet, Fast Ethernet, Gigabit Ethernet, and 10 Gigabit Ethernet.

### Q13-3
> id: ch13-q-q13-3 | type: review_question | group: Questions | ref_sections: [ch13-13-2-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

What are the common Standard Ethernet implementations?

### Q13-4
> id: ch13-q-q13-4 | type: review_question | group: Questions | ref_sections: [ch13-13-3-2-summary] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

What are the common Fast Ethernet implementations?

### Q13-5
> id: ch13-q-q13-5 | type: review_question | group: Questions | ref_sections: [ch13-13-4-2-implementation-summary] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

What are the common Gigabit Ethernet implementations?

### Q13-6
> id: ch13-q-q13-6 | type: review_question | group: Questions | ref_sections: [ch13-13-5-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

What are the common 10 Gigabit implementations?

### Q13-7
> id: ch13-q-q13-7 | type: review_question | group: Questions | ref_sections: [ch13-13-2-1-frame-format] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

How is the preamble field different from the SFD field?

### Q13-8
> id: ch13-q-q13-8 | type: review_question | group: Questions | ref_sections: [ch13-13-2-2-unicast-multicast-and-broadcast-addresses] | has_figure: false | answer: null | figure_assets: [] | src: book p.384

What is the difference between unicast, multicast, and broadcast addresses?

### Q13-9
> id: ch13-q-q13-9 | type: review_question | group: Questions | ref_sections: [ch13-13-2-6-bridged-ethernet, ch13-13-2-6-separating-collision-domains] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

What are the advantages of dividing an Ethernet LAN with a bridge?

### Q13-10
> id: ch13-q-q13-10 | type: review_question | group: Questions | ref_sections: [ch13-13-2-6-switched-ethernet] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

What is the relationship between a switch and a bridge?

## Problems

### P13-1
> id: ch13-q-p13-1 | type: problem | group: Problems | ref_sections: [ch13-13-2-2-transmission-of-address-bits] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

What is the hexadecimal equivalent of the following Ethernet address? 01011010 00010001 01010101 00011000 10101010 00001111

### P13-2
> id: ch13-q-p13-2 | type: problem | group: Problems | ref_sections: [ch13-13-2-2-transmission-of-address-bits] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

How does the Ethernet address 1A:2B:3C:4D:5E:6F appear on the line in binary?

### P13-3
> id: ch13-q-p13-3 | type: problem | group: Problems | ref_sections: [ch13-13-2-2-unicast-multicast-and-broadcast-addresses] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

If an Ethernet destination address is 07:01:02:03:04:05, what is the type of the address (unicast, multicast, or broadcast)?

### P13-4
> id: ch13-q-p13-4 | type: problem | group: Problems | ref_sections: [ch13-13-2-1-frame-length] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

An Ethernet MAC sublayer receives 42 bytes of data from the upper layer. How many bytes of padding must be added to the data?

### P13-5
> id: ch13-q-p13-5 | type: problem | group: Problems | ref_sections: [ch13-13-2-1-frame-format, ch13-13-2-1-frame-length] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

What is the ratio of useful data to the entire packet for the smallest Ethernet frame?

### P13-6
> id: ch13-q-p13-6 | type: problem | group: Problems | ref_sections: [ch13-13-2-5-10base5-thick-ethernet] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

Suppose the length of a 10Base5 cable is 2500 m. If the speed of propagation in a thick coaxial cable is 200,000,000 m/s, how long does it take for a bit to travel from the beginning to the end of the network? Assume there is a 10 μs delay in the equipment.

### P13-7
> id: ch13-q-p13-7 | type: problem | group: Problems | ref_sections: [ch13-13-1-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

Suppose you are to design a LAN for a company that has 100 employees, each given a desktop computer attached to the LAN. What should be the data rate of the LAN if the typical use of the LAN is shown below:
**a.** Each employee needs to retrieve a file of average size of 10 megabytes in a second. An employee may do this on average 10 times during the eight-hour working time.

**b.** Each employee needs to access the Internet at 250 Kbps. This can happen for 10 employees simultaneously.

**c.** Each employee may receive 10 e-mails per hour with an average size of 100 kilobytes. Half of the employees may receive e-mails simultaneously.

### P13-8
> id: ch13-q-p13-8 | type: problem | group: Problems | ref_sections: [ch13-13-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

In a Standard Ethernet LAN, the average size of a frame is 1000 bytes. If a noise of 2 ms occurs on the LAN, how many frames are destroyed?

### P13-9
> id: ch13-q-p13-9 | type: problem | group: Problems | ref_sections: [ch13-13-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

Repeat Problem P13-8 for a Fast Ethernet LAN.

### P13-10
> id: ch13-q-p13-10 | type: problem | group: Problems | ref_sections: [ch13-13-4] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

Repeat Problem P13-8 for a Gigabit Ethernet LAN.

### P13-11
> id: ch13-q-p13-11 | type: problem | group: Problems | ref_sections: [ch13-13-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.385

Repeat Problem P13-8 for a 10 Gigabit Ethernet LAN.
