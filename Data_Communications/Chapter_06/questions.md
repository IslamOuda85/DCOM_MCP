---
doc_type: question_bank
course_id: data_communications
chapter: 6
chapter_id: data_communications_ch06
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 12
- id: Problems
  label: Problems
  count: 18
question_counts:
  Questions: 12
  Problems: 18
spec_version: 1.1-controller
generated_at: '2026-10-07T03:15:22+00:00'
status: complete
---
## Questions

### Q6-1
> id: ch06-q-q6-1 | type: review_question | group: Questions | ref_sections: [ch06-6-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

Describe the goals of multiplexing.

### Q6-2
> id: ch06-q-q6-2 | type: review_question | group: Questions | ref_sections: [ch06-6-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

List three main multiplexing techniques mentioned in this chapter.

### Q6-3
> id: ch06-q-q6-3 | type: review_question | group: Questions | ref_sections: [ch06-6-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

Distinguish between a link and a channel in multiplexing.

### Q6-4
> id: ch06-q-q6-4 | type: review_question | group: Questions | ref_sections: [ch06-6-1-1, ch06-6-1-2, ch06-6-1-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

Which of the three multiplexing techniques is (are) used to combine analog signals? Which of the three multiplexing techniques is (are) used to combine digital signals?

### Q6-5
> id: ch06-q-q6-5 | type: review_question | group: Questions | ref_sections: [ch06-6-1-1-the-analog-carrier-system] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

Define the analog hierarchy used by telephone companies and list different levels of the hierarchy.

### Q6-6
> id: ch06-q-q6-6 | type: review_question | group: Questions | ref_sections: [ch06-6-1-3-digital-signal-service] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

Define the digital hierarchy used by telephone companies and list different levels of the hierarchy.

### Q6-7
> id: ch06-q-q6-7 | type: review_question | group: Questions | ref_sections: [ch06-6-1-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.181

Which of the three multiplexing techniques is common for fiber-optic links? Explain the reason.

### Q6-8
> id: ch06-q-q6-8 | type: review_question | group: Questions | ref_sections: [ch06-6-1-3-multilevel-multiplexing, ch06-6-1-3-multiple-slot-allocation, ch06-6-1-3-pulse-stuffing] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Distinguish between multilevel TDM, multiple-slot TDM, and pulse-stuffed TDM.

### Q6-9
> id: ch06-q-q6-9 | type: review_question | group: Questions | ref_sections: [ch06-6-1-3-synchronous-tdm, ch06-6-1-3-statistical-time-division-multiplexing] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Distinguish between synchronous and statistical TDM.

### Q6-10
> id: ch06-q-q6-10 | type: review_question | group: Questions | ref_sections: [ch06-6-2, ch06-6-2-1, ch06-6-2-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Define spread spectrum and its goal. List the two spread spectrum techniques discussed in this chapter.

### Q6-11
> id: ch06-q-q6-11 | type: review_question | group: Questions | ref_sections: [ch06-6-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Define FHSS and explain how it achieves bandwidth spreading.

### Q6-12
> id: ch06-q-q6-12 | type: review_question | group: Questions | ref_sections: [ch06-6-2-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Define DSSS and explain how it achieves bandwidth spreading.

## Problems

### P6-1
> id: ch06-q-p6-1 | type: problem | group: Problems | ref_sections: [ch06-6-1-1, ch06-example-6-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Assume that a voice channel occupies a bandwidth of 4 kHz. We need to multiplex 10 voice channels with guard bands of 500 Hz using FDM. Calculate the required bandwidth.

### P6-2
> id: ch06-q-p6-2 | type: problem | group: Problems | ref_sections: [ch06-6-1-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

We need to transmit 100 digitized voice channels using a passband channel of 20 kHz. What should be the ratio of bits/Hz if we use no guard band?

### P6-3
> id: ch06-q-p6-3 | type: problem | group: Problems | ref_sections: [ch06-6-1-1-the-analog-carrier-system] | has_figure: true | answer: null | figure_assets: [ch06_ill_009] | src: book p.182

In the analog hierarchy of Figure 6.9, find the overhead (extra bandwidth for guard band or control) in each hierarchy level (group, supergroup, master group, and jumbo group).

> [ASSET_REF ch06_ill_009] See the original figure and its description in assets/manifest.json.

### P6-4
> id: ch06-q-p6-4 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-time-slots-and-frames, ch06-6-1-3-frame-synchronizing] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

We need to use synchronous TDM and combine 20 digital sources, each of 100 Kbps. Each output slot carries 1 bit from each digital source, but one extra bit is added to each frame for synchronization. Answer the following questions:

**a.** What is the size of an output frame in bits?

**b.** What is the output frame rate?

**c.** What is the duration of an output frame?

**d.** What is the output data rate?

**e.** What is the efficiency of the system (ratio of useful bits to the total bits)?

### P6-5
> id: ch06-q-p6-5 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-time-slots-and-frames, ch06-6-1-3-frame-synchronizing] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Repeat Problem 6-4 if each output slot carries 2 bits from each source.

### P6-6
> id: ch06-q-p6-6 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-statistical-time-division-multiplexing, ch06-6-1-3-addressing, ch06-6-1-3-slot-size] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

We have 14 sources, each creating 500 8-bit characters per second. Since only some of these sources are active at any moment, we use statistical TDM to combine these sources using character interleaving. Each frame carries 6 slots at a time, but we need to add 4-bit addresses to each slot. Answer the following questions:

**a.** What is the size of an output frame in bits?

**b.** What is the output frame rate?

**c.** What is the duration of an output frame?

**d.** What is the output data rate?

### P6-7
> id: ch06-q-p6-7 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-multilevel-multiplexing] | has_figure: false | answer: null | figure_assets: [] | src: book p.182

Ten sources, six with a bit rate of 200 kbps and four with a bit rate of 400 kbps, are to be combined using multilevel TDM with no synchronizing bits. Answer the following questions about the final stage of the multiplexing:

**a.** What is the size of a frame in bits?

**b.** What is the frame rate?

**c.** What is the duration of a frame?

**d.** What is the data rate?

### P6-8
> id: ch06-q-p6-8 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-multiple-slot-allocation] | has_figure: false | answer: null | figure_assets: [] | src: book p.183

Four channels, two with a bit rate of 200 kbps and two with a bit rate of 150 kbps, are to be multiplexed using multiple-slot TDM with no synchronization bits. Answer the following questions:

**a.** What is the size of a frame in bits?

**b.** What is the frame rate?

**c.** What is the duration of a frame?

**d.** What is the data rate?

### P6-9
> id: ch06-q-p6-9 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-pulse-stuffing] | has_figure: false | answer: null | figure_assets: [] | src: book p.183

Two channels, one with a bit rate of 190 kbps and another with a bit rate of 180 kbps, are to be multiplexed using pulse-stuffing TDM with no synchronization bits. Answer the following questions:

**a.** What is the size of a frame in bits?

**b.** What is the frame rate?

**c.** What is the duration of a frame?

**d.** What is the data rate?

### P6-10
> id: ch06-q-p6-10 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-the-t-1-frame] | has_figure: false | answer: null | figure_assets: [] | src: book p.183

Answer the following questions about a T-1 line:

**a.** What is the duration of a frame?

**b.** What is the overhead (number of extra bits per second)?

### P6-11
> id: ch06-q-p6-11 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-synchronous-tdm, ch06-6-1-3-empty-slots] | has_figure: false | answer: null | figure_assets: [] | src: book p.183

Show the contents of the five output frames for a synchronous TDM multiplexer that combines four sources sending the following characters. Note that the characters are sent in the same order that they are typed. The third source is silent.

**a.** Source 1 message: HELLO

**b.** Source 2 message: HI

**c.** Source 3 message:

**d.** Source 4 message: BYE

### P6-12
> id: ch06-q-p6-12 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-time-slots-and-frames, ch06-6-1-3-frame-synchronizing] | has_figure: true | answer: null | figure_assets: [ch06_ill_034] | src: book p.183

Figure 6.34 shows a multiplexer in a synchronous TDM system. Each output slot is only 10 bits long (3 bits taken from each input plus 1 framing bit). What is the output stream? The bits arrive at the multiplexer as shown by the arrows.

> **[ASSET ch06_ill_034]** Figure 6.34: Problem P6-12
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_034.png
> - src: book Figure 6.34; p.183
> - shows: Figure 6.34: Problem P6-12. Problem P6-12 supplies three input bit streams entering a synchronous TDM multiplexer; arrows mark the next bits and the output frame has ten bits including one framing bit.
> - structure: Problem P6-12 supplies three input bit streams entering a synchronous TDM multiplexer; arrows mark the next bits and the output frame has ten bits including one framing bit.
> - text_in_image: 1 0 1 1 1 0 1 1 1 1 0 1; Frame of 10 bits; 1 1 1 1 1 1 1 0 0 0 0; TDM; 1 0 1 0 0 0 0 0 0 1 1 1 1
> - use_when: Teach ch06-q-p6-12, interpret Figure 6.34, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

### P6-13
> id: ch06-q-p6-13 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-time-slots-and-frames] | has_figure: true | answer: null | figure_assets: [ch06_ill_035] | src: book p.183

Figure 6.35 shows a demultiplexer in a synchronous TDM. If the input slot is 16 bits long (no framing bits), what is the bit stream in each output? The bits arrive at the demultiplexer as shown by the arrows.

> **[ASSET ch06_ill_035]** Figure 6.35: Problem P6-13
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_035.png
> - src: book Figure 6.35; p.184
> - shows: Figure 6.35: Problem P6-13. Problem P6-13 supplies three consecutive 16-bit slots entering a synchronous TDM demultiplexer; the task is to route each slot to its output stream in arrival order.
> - structure: Problem P6-13 supplies three consecutive 16-bit slots entering a synchronous TDM demultiplexer; the task is to route each slot to its output stream in arrival order.
> - text_in_image: 1 0 1 0 0 0 0 0; 1 0 1 0 1 0 1 0 1 0 1 0 0 0 0 1; 0 1 1 1 0 0 0 0 0 1 1 1 1 0 0 0; TDM
> - use_when: Teach ch06-q-p6-13, interpret Figure 6.35, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

### P6-14
> id: ch06-q-p6-14 | type: problem | group: Problems | ref_sections: [ch06-6-1-3-digital-signal-service] | has_figure: true | answer: null | figure_assets: [ch06_ill_023] | src: book p.184

Answer the following questions about the digital hierarchy in Figure 6.23:

**a.** What is the overhead (number of extra bits) in the DS-1 service?

**b.** What is the overhead (number of extra bits) in the DS-2 service?

**c.** What is the overhead (number of extra bits) in the DS-3 service?

**d.** What is the overhead (number of extra bits) in the DS-4 service?

> [ASSET_REF ch06_ill_023] See the original figure and its description in assets/manifest.json.

### P6-15
> id: ch06-q-p6-15 | type: problem | group: Problems | ref_sections: [ch06-6-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.184

What is the minimum number of bits in a PN sequence if we use FHSS with a channel bandwidth of B = 4 kHz and Bss = 100 kHz?

### P6-16
> id: ch06-q-p6-16 | type: problem | group: Problems | ref_sections: [ch06-6-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.184

An FHSS system uses a 4-bit PN sequence. If the bit rate of the PN is 64 bits per second, answer the following questions:

**a.** What is the total number of possible channels?

**b.** What is the time needed to finish a complete cycle of PN?

### P6-17
> id: ch06-q-p6-17 | type: problem | group: Problems | ref_sections: [ch06-6-2-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.184

A pseudorandom number generator uses the following formula to create a random series:

$$N_{i+1}=(5+7N_i)\bmod 17-1$$

Here, $N_i$ is the current random number and $N_{i+1}$ is the next random number. The term $\bmod$ gives the remainder after division by 17. Show the sequence created by this generator for use in spread spectrum.

### P6-18
> id: ch06-q-p6-18 | type: problem | group: Problems | ref_sections: [ch06-6-2-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.184

We have a digital medium with a data rate of 10 Mbps. How many 64-kbps voice channels can be carried by this medium if we use DSSS with the Barker sequence?
