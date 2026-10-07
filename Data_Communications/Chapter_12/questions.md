---
doc_type: question_bank
course_id: data_communications
chapter: 12
chapter_id: data_communications_ch12
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 24
- id: Problems
  label: Problems
  count: 25
question_counts:
  Questions: 24
  Problems: 25
spec_version: 1.1-controller
generated_at: '2026-10-07T03:48:17+00:00'
status: complete
---
## Questions

### Q12-1
> id: ch12-q-q12-1 | type: review_question | group: Questions | ref_sections: [ch12-0, ch12-12-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

Which of the following is a random-access protocol?
**a.** CSMA/CD

**b.** Polling

**c.** TDMA

### Q12-2
> id: ch12-q-q12-2 | type: review_question | group: Questions | ref_sections: [ch12-0, ch12-12-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

Which of the following is a controlled-access protocol?
**a.** Token-passing

**b.** Polling

**c.** FDMA

### Q12-3
> id: ch12-q-q12-3 | type: review_question | group: Questions | ref_sections: [ch12-0, ch12-12-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

Which of the following is a channelization protocol?
**a.** ALOHA

**b.** Token-passing

**c.** CDMA

### Q12-4
> id: ch12-q-q12-4 | type: review_question | group: Questions | ref_sections: [ch12-12-1-1-vulnerable-time] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

Stations in a pure Aloha network send frames of size 1000 bits at the rate of 1 Mbps. What is the vulnerable time for this network?

### Q12-5
> id: ch12-q-q12-5 | type: review_question | group: Questions | ref_sections: [ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

Stations in an slotted Aloha network send frames of size 1000 bits at the rate of 1 Mbps. What is the vulnerable time for this network?

### Q12-6
> id: ch12-q-q12-6 | type: review_question | group: Questions | ref_sections: [ch12-12-1-1-pure-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

In a pure Aloha network with G = 1/2, how is the throughput affected in each of the following cases?
**a.** G is increased to 1.

**b.** G is decreased to 1/4.

### Q12-7
> id: ch12-q-q12-7 | type: review_question | group: Questions | ref_sections: [ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.354

In a slotted Aloha network with G = 1/2, how is the throughput affected in each of the following cases?
**a.** G is increased to 1.

**b.** G is decreased to 1/4.

### Q12-8
> id: ch12-q-q12-8 | type: review_question | group: Questions | ref_sections: [ch12-12-1-1-pure-aloha] | has_figure: true | answer: null | figure_assets: [ch12_ill_003] | src: book p.355

To understand the uses of K in Figure 12.3, find the probability that a station can send immediately in each of the following cases:
**a.** After one failure.

**b.** After three failures.

> [ASSET_REF ch12_ill_003] See the original figure and its description in assets/manifest.json.

### Q12-9
> id: ch12-q-q12-9 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-procedure] | has_figure: true | answer: null | figure_assets: [ch12_ill_013] | src: book p.355

To understand the uses of K in Figure 12.13, find the probability that a station can send immediately in each of the following cases:
**a.** After one failure.

**b.** After four failures.

> [ASSET_REF ch12_ill_013] See the original figure and its description in assets/manifest.json.

### Q12-10
> id: ch12-q-q12-10 | type: review_question | group: Questions | ref_sections: [ch12-12-1-4] | has_figure: true | answer: null | figure_assets: [ch12_ill_015] | src: book p.355

To understand the uses of K in Figure 12.15, find the probability that a station can send immediately in each of the following cases:
**a.** After two failures.

**b.** After five failures.

> [ASSET_REF ch12_ill_015] See the original figure and its description in assets/manifest.json.

### Q12-11
> id: ch12-q-q12-11 | type: review_question | group: Questions | ref_sections: [ch12-12-1-1-pure-aloha] | has_figure: true | answer: null | figure_assets: [ch12_ill_003] | src: book p.355

Based on Figure 12.3, how do we interpret success in an Aloha network?

> [ASSET_REF ch12_ill_003] See the original figure and its description in assets/manifest.json.

### Q12-12
> id: ch12-q-q12-12 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-procedure] | has_figure: true | answer: null | figure_assets: [ch12_ill_013] | src: book p.355

Based on Figure 12.13, how do we interpret success in a CSMA/CD network?

> [ASSET_REF ch12_ill_013] See the original figure and its description in assets/manifest.json.

### Q12-13
> id: ch12-q-q12-13 | type: review_question | group: Questions | ref_sections: [ch12-12-1-4] | has_figure: true | answer: null | figure_assets: [ch12_ill_015] | src: book p.355

Based on Figure 12.15, how do we interpret success in a CSMA/CA network?

> [ASSET_REF ch12_ill_015] See the original figure and its description in assets/manifest.json.

### Q12-14
> id: ch12-q-q12-14 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-minimum-frame-size] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Assume the propagation delay in a broadcast network is 5 μs and the frame transmission time is 10 μs.
**a.** How long does it take for the first bit to reach the destination?

**b.** How long does it take for the last bit to reach the destination after the first bit has arrived?

**c.** How long is the network involved with this frame (vulnerable to collision)?

### Q12-15
> id: ch12-q-q12-15 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-minimum-frame-size] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Assume the propagation delay in a broadcast network is 3 μs and the frame transmission time is 5 μs. Can the collision be detected no matter where it occurs?

### Q12-16
> id: ch12-q-q12-16 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-minimum-frame-size] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Assume the propagation delay in a broadcast network is 6 μs and the frame transmission time is 4 μs. Can the collision be detected no matter where it occurs?

### Q12-17
> id: ch12-q-q12-17 | type: review_question | group: Questions | ref_sections: [ch12-12-1, ch12-12-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Explain why collision is an issue in random access protocols but not in controlled access protocols.

### Q12-18
> id: ch12-q-q12-18 | type: review_question | group: Questions | ref_sections: [ch12-12-1, ch12-12-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Explain why collision is an issue in random access protocols but not in channelization protocols.

### Q12-19
> id: ch12-q-q12-19 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-minimum-frame-size] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Assume the propagation delay in a broadcast network is 5 μs and the frame transmission time is 10 μs.
**a.** How long does it take for the first bit to reach the destination?

**b.** How long does it take for the last bit to reach the destination after the first bit has arrived?

**c.** How long is the network involved with this frame (vulnerable to collision)?

### Q12-20
> id: ch12-q-q12-20 | type: review_question | group: Questions | ref_sections: [ch12-12-1-3-minimum-frame-size] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

Assume the propagation delay in a broadcast network is 12 μs and the frame transmission time is 8 μs.
**a.** How long does it take for the first bit to reach the destination?

**b.** How long does it take for the last bit to reach the destination after the first bit has arrived?

**c.** How long is the network involved with this frame (vulnerable to collision)?

### Q12-21
> id: ch12-q-q12-21 | type: review_question | group: Questions | ref_sections: [ch12-12-1-4] | has_figure: false | answer: null | figure_assets: [] | src: book p.355

List some strategies in CSMA/CA that are used to avoid collision.

### Q12-22
> id: ch12-q-q12-22 | type: review_question | group: Questions | ref_sections: [ch12-12-1-4-frame-exchange-time-line] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

In a wireless LAN, station A is assigned IFS = 5 milliseconds and station B is assigned IFS = 7 milliseconds. Which station has a higher priority? Explain.

### Q12-23
> id: ch12-q-q12-23 | type: review_question | group: Questions | ref_sections: [ch12-12-1-4] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

There is no acknowledgment mechanism in CSMA/CD, but we need this mechanism in CSMA/CA. Explain the reason.

### Q12-24
> id: ch12-q-q12-24 | type: review_question | group: Questions | ref_sections: [ch12-12-1-4-network-allocation-vector] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

What is the purpose of NAV in CSMA/CA?

## Problems

### P12-1
> id: ch12-q-p12-1 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

To formulate the performance of a multiple-access network, we need a mathematical model. When the number of stations in a network is very large, the Poisson distribution, $p[x]=e^{-\lambda}\lambda^x/x!$, is used. In this formula, p[x] is the probability of generating x number of frames in a period of time and λ is the average number of generated frames during the same period of time. Using the Poisson distribution:
**a.** Find the probability that a pure Aloha network generates x number of frames during the vulnerable time. Note that the vulnerable time for this network is two times the frame transmission time ($T_{fr}$).

**b.** Find the probability that a slotted Aloha network generates x number of frames during the vulnerable time. Note that the vulnerable time for this network is equal to the frame transmission time ($T_{fr}$).

### P12-2
> id: ch12-q-p12-2 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

In the previous problem, we used the Poisson distribution to find the probability of generating x number of frames, in a certain period of time, in a pure or slotted Aloha network as $p[x]=e^{-\lambda}\lambda^x/x!$. In this problem, we want to find the probability that a frame in such a network reaches its destination without colliding with other frames. For this purpose, it is simpler to think that we have G stations, each sending an average of one frame during the frame transmission time (instead of having N frames, each sending an average of G/N frames during the same time). Then, the probability of success for a station is the probability that no other station sends a frame during the vulnerable time.
**a.** Find the probability that a station in a pure Aloha network can successfully send a frame during a vulnerable time.

**b.** Find the probability that a station in a slotted Aloha network can successfully send a frame during a vulnerable time.

### P12-3
> id: ch12-q-p12-3 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

In the previous problem, we found that the probability of a station (in a Gstation network) successfully sending a frame in a vulnerable time is $P=e^{-2G}$ for pure ALOHA and $P=e^{-G}$ for a slotted Aloha network. In this problem, we want to find the throughput of these networks, which is the probability that any station (out of G stations) can successfully send a frame during the vulnerable time.
**a.** Find the throughput of a pure Aloha network.

**b.** Find the throughput of a slotted ALOHA network.

### P12-4
> id: ch12-q-p12-4 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.356

In the previous problem, we showed that the throughput is $S=Ge^{-2G}$ for pure ALOHA and $S=Ge^{-G}$ for slotted ALOHA. In this problem, we want to find the value of G in each network that makes the throughput maximum and find the value of the maximum throughput. This can be done if we find the derivative of S with respect to G and set the derivative to zero.
**a.** Find the value of G that makes the throughput maximum, and find the value of the maximum throughput for a pure Aloha network.

**b.** Find the value of G that makes the throughput maximum, and find the value of the maximum throughput for a slotted Aloha network.

### P12-5
> id: ch12-q-p12-5 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.357

A multiple access network with a large number of stations can be analyzed using the Poisson distribution. When there is a limited number of stations in a network, we need to use another approach for this analysis. In a network with N stations, we assume that each station has a frame to send during the frame transmission time ($T_{fr}$) with probability p. In such a network, a station is successful in sending its frame if the station has a frame to send during the vulnerable time and no other station has a frame to send during this period of time.
**a.** Find the probability that a station in a pure Aloha network can successfully send a frame during the vulnerable time.

**b.** Find the probability that a station in a slotted Aloha network can successfully send a frame during the vulnerable time.

### P12-6
> id: ch12-q-p12-6 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.357

In the previous problem, we found the probability of success for a station to send a frame successfully during the vulnerable time. The throughput of a network with a limited number of stations is the probability that any station (out of N stations) can send a frame successfully. In other words, the throughput is the sum of N success probabilities.
**a.** Find the throughput of a pure Aloha network.

**b.** Find the throughput of a slotted Aloha network.

### P12-7
> id: ch12-q-p12-7 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.357

In the previous problem, we found the throughputs of a pure and a slotted Aloha network as $S=Np(1-p)^{2(N-1)}$ and $S=Np(1-p)^{N-1}$ respectively. In this problem we want to find the maximum throughput with respect to p.
**a.** Find the value of p that maximizes the throughput of a pure Aloha network, and calculate the maximum throughput when N is a very large number.

**b.** Find the value of p that maximizes the throughput of a slotted Aloha network, and calculate the maximum throughput when N is a very large number.

### P12-8
> id: ch12-q-p12-8 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.357

There are only three active stations in a slotted Aloha network: A, B, and C. Each station generates a frame in a time slot with the corresponding probabilities $p_{A}$ = 0.2, $p_{B}$ = 0.3, and $p_{C}$ = 0.4 respectively.
**a.** What is the throughput of each station?

**b.** What is the throughput of the network?

### P12-9
> id: ch12-q-p12-9 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.357

There are only three active stations in a slotted Aloha network: A, B, and C. Each station generates a frame in a time slot with the corresponding probabilities $p_{A}$ = 0.2, $p_{B}$ = 0.3, and $p_{C}$ = 0.4 respectively.
**a.** What is the probability that any station can send a frame in the first slot?

**b.** What is the probability that station A can successfully send a frame for the first time in the second slot?

**c.** What is the probability that station C can successfully send a frame for the first time in the third slot?

### P12-10
> id: ch12-q-p12-10 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput, ch12-12-1-1-slotted-aloha-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

A slotted Aloha network is working with maximum throughput.
**a.** What is the probability that a slot is empty?

**b.** How many slots, n, on average, should pass before getting an empty slot?

### P12-11
> id: ch12-q-p12-11 | type: problem | group: Problems | ref_sections: [ch12-12-1-2-vulnerable-time] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

One of the useful parameters in a LAN is the number of bits that can fit in one meter of the medium (nb/m). Find the value of nb/m if the data rate is 100 Mbps and the medium propagation speed is 2 × $10^{8}$ m/s.

### P12-12
> id: ch12-q-p12-12 | type: problem | group: Problems | ref_sections: [ch12-12-1-2-vulnerable-time] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

Another useful parameter in a LAN is the bit length of the medium ($L_{b}$), which defines the number of bits that the medium can hold at any time. Find the bit length of a LAN if the data rate is 100 Mbps and the medium length in meters ($L_{m}$) for a communication between two stations is 200 m. Assume the propagation speed in the medium is 2 × $10^{8}$ m/s.

### P12-13
> id: ch12-q-p12-13 | type: problem | group: Problems | ref_sections: [ch12-12-1-2-vulnerable-time] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

We have defined the parameter a as the number of frames that can fit the medium between two stations, or a = ($T_{p}$)/($T_{fr}$). Another way to define this parameter is a = $L_{b}$/$F_{b}$, in which $L_{b}$ is the bit length of the medium and $F_{b}$ is the frame length of the medium. Show that the two definitions are equivalent.

### P12-14
> id: ch12-q-p12-14 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

In a bus CSMA/CD network with a data rate of 10 Mbps, a collision occurs 20 μs after the first bit of the frame leaves the sending station. What should the length of the frame be so that the sender can detect the collision?

### P12-15
> id: ch12-q-p12-15 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

Assume that there are only two stations, A and B, in a bus CSMA/CD network. The distance between the two stations is 2000 m and the propagation speed is 2 × $10^{8}$m/s. If station A starts transmitting at time t1:
**a.** Does the protocol allow station B to start transmitting at time $t_{1}$ + 8 μs? If the answer is yes, what will happen?

**b.** Does the protocol allow station B to start transmitting at time $t_{1}$ + 11 μs? If the answer is yes, what will happen?

### P12-16
> id: ch12-q-p12-16 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: true | answer: null | figure_assets: [ch12_ill_013] | src: book p.358

There are only two stations, A and B, in a bus 1-persistence CSMA/CD network with $T_{p}$ = 25.6 μs and $T_{fr}$ = 51.2 μs. Station A has a frame to send to station B. The frame is unsuccessful two times and succeeds on the third try. Draw a time line diagram for this problem. Assume that the R is 1 and 2 respectively and ignore the time for sending a jamming signal (see Figure 12.13).

> [ASSET_REF ch12_ill_013] See the original figure and its description in assets/manifest.json.

### P12-17
> id: ch12-q-p12-17 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: false | answer: null | figure_assets: [] | src: book p.358

To understand why we need to have a minimum frame size $T_{fr}$ = 2 × $T_{p}$ in a CSMA/CD network, assume we have a bus network with only two stations, A and B, in which $T_{fr}$ = 40 μs and $T_{p}$ = 25 μs. Station A starts sending a frame at time t = 0.0 μs and station B starts sending a frame at t = 23.0 μs. Answer the following questions:
**a.** Do frames collide?

**b.** If the answer to part a is yes, does station A detect collision?

**c.** If the answer to part a is yes, does station B detect collision?

### P12-18
> id: ch12-q-p12-18 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: false | answer: null | figure_assets: [] | src: book p.359

In a bus 1-persistence CSMA/CD with $T_{p}$ = 50 μs and $T_{fr}$ = 120 μs, there are two stations, A and B. Both stations start sending frames to each other at the same time. Since the frames collide, each station tries to retransmit. Station A comes out with R = 0 and station B with R = 1. Ignore any other delay including the delay for sending jamming signals. Do the frames collide again? Draw a time-line diagram to prove your claim. Does the generation of a random number help avoid collision in this case?

### P12-19
> id: ch12-q-p12-19 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: true | answer: null | figure_assets: [ch12_ill_013] | src: book p.359

The random variable R (Figure 12.13) is designed to give stations different delays when a collision has occurred. To alleviate the collision, we expect that different stations generate different values of R. To show the point, find the probability that the value of R is the same for two stations after
**a.** the first collision.

**b.** the second collision.

> [ASSET_REF ch12_ill_013] See the original figure and its description in assets/manifest.json.

### P12-20
> id: ch12-q-p12-20 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: true | answer: null | figure_assets: [ch12_ill_030] | src: book p.359

Assume we have a slotted CSMA/CD network. Each station in this network uses a contention period, in which the station contends for access to the shared channel before being able to send a frame. We assume that the contention period is made of contention slots. At the beginning of each slot, the station senses the channel. If the channel is free, the station sends its frame; if the channel is busy, the station refrains from sending and waits until the beginning of the next slot. In other words, the station waits, on average, for k slots before sending its frame, as shown in Figure 12.30. Note that the channel is either in the contention state, the transmitting state, or the idle state (when no station has a frame to send). However, if N is a very large number, the idle state actually disappears.
**a.** What is the probability of a free slot ($P_{free}$) if the number of stations is N and each station has a frame to send with probability p?

**b.** What is the maximum of this probability when N is a very large number?

**c.** What is the probability that the jth slot is free?

**d.** What is the average number of slots, k, that a station should wait before getting a free slot?

**e.** What is the value of k when N (the number of stations) is very large?

> **[ASSET ch12_ill_030]** Figure 12.30: Problem P12-20
> - type: illustration
> - kind: diagram
> - file: assets/ch12_ill_030.png
> - src: book Figure 12.30; p.359
> - shows: Figure 12.30: Problem P12-20. A time line for Problem P12-20 alternates contention slots, busy frame intervals, and an idle interval.
> - structure: A time line for Problem P12-20 alternates contention slots, busy frame intervals, and an idle interval.
> - text_in_image: Busy; Busy; Busy; Idle; Time; Contention; Contention; Contention
> - use_when: Teach ch12-q-p12-20, compare MAC behavior, trace the timing or signal calculation, or solve a linked practice question.
> - confidence: high

### P12-21
> id: ch12-q-p12-21 | type: problem | group: Problems | ref_sections: [ch12-12-1-3-minimum-frame-size, ch12-12-1-3-procedure] | has_figure: false | answer: null | figure_assets: [] | src: book p.359

Although the throughput calculation of a CSMA/CD is really involved, we can calculate the maximum throughput of a slotted CSMA/CD with the specification we described in the previous problem. We found that the average number of contention slots a station needs to wait is k = e slots. With this assumption, the throughput of a slotted CSMA/CD is S = ($T_{fr}$)/(time the channel is busy for a frame) The time the channel is busy for a frame is the time to wait for a free slot plus the time to transmit the frame plus the propagation delay to receive the good news about the lack of collision. Assume the duration of a contention slot is 2 × ($T_{p}$) and a = ($T_{p}$)/($T_{fr}$). Note that the parameter a is the number of frames that occupy the transmission media. Find the throughput of a slotted CSMA/CD in terms of the parameter a.

### P12-22
> id: ch12-q-p12-22 | type: problem | group: Problems | ref_sections: [ch12-12-1-1-pure-throughput] | has_figure: false | answer: null | figure_assets: [] | src: book p.360

We have a pure ALOHA network with a data rate of 10 Mbps. What is the maximum number of 1000-bit frames that can be successfully sent by this network?

### P12-23
> id: ch12-q-p12-23 | type: problem | group: Problems | ref_sections: [ch12-12-3-3-chips] | has_figure: false | answer: null | figure_assets: [] | src: book p.360

Check to see if the following set of chips can belong to an orthogonal system. [+1, +1] [+1, −1] and

### P12-24
> id: ch12-q-p12-24 | type: problem | group: Problems | ref_sections: [ch12-12-3-3-chips] | has_figure: false | answer: null | figure_assets: [] | src: book p.360

Check to see if the following set of chips can belong to an orthogonal system. [+1, +1, +1, +1] , [+1, −1, −1, +1] , [−1, +1, +1, −1] , [+1, −1, −1, +1]

### P12-25
> id: ch12-q-p12-25 | type: problem | group: Problems | ref_sections: [ch12-12-3-3-sequence-generation, ch12-12-3-3-encoding-and-decoding] | has_figure: true | answer: null | figure_assets: [ch12_ill_029] | src: book p.360

Alice and Bob are experimenting with CDMA using a $W_{2}$ Walsh table (see Figure 12.29). Alice uses the code [+1, +1] and Bob uses the code [+1, −1]. Assume that they simultaneously send a hexadecimal digit to each other. Alice sends (6)16 and Bob sends (B)16. Show how they can detect what the other person has sent.

> [ASSET_REF ch12_ill_029] See the original figure and its description in assets/manifest.json.
