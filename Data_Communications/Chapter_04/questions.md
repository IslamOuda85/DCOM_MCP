---
doc_type: question_bank
course_id: data_communications
chapter: 4
chapter_id: data_communications_ch04
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 12
- id: Problems
  label: Problems
  count: 20
question_counts:
  Questions: 12
  Problems: 20
spec_version: 1.1-controller
generated_at: '2026-10-07T03:03:01+00:00'
status: complete
---
## Questions

### Q4-1
> id: ch04-q-q4-1 | type: review_question | group: Questions | ref_sections: [ch04-4-1] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

List three techniques of digital-to-digital conversion.

### Q4-2
> id: ch04-q-q4-2 | type: review_question | group: Questions | ref_sections: [ch04-4-1-1-signal-element-versus-data-element] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Distinguish between a signal element and a data element.

### Q4-3
> id: ch04-q-q4-3 | type: review_question | group: Questions | ref_sections: [ch04-4-1-1-data-rate-versus-signal-rate] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Distinguish between data rate and signal rate.

### Q4-4
> id: ch04-q-q4-4 | type: review_question | group: Questions | ref_sections: [ch04-4-1-1-baseline-wandering] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Define baseline wandering and its effect on digital transmission.

### Q4-5
> id: ch04-q-q4-5 | type: review_question | group: Questions | ref_sections: [ch04-4-1-1-dc-components] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Define a DC component and its effect on digital transmission.

### Q4-6
> id: ch04-q-q4-6 | type: review_question | group: Questions | ref_sections: [ch04-4-1-1-self-synchronization] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Define the characteristics of a self-synchronizing signal.

### Q4-7
> id: ch04-q-q4-7 | type: review_question | group: Questions | ref_sections: [ch04-4-1-2] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

List five line coding schemes discussed in this book.

### Q4-8
> id: ch04-q-q4-8 | type: review_question | group: Questions | ref_sections: [ch04-4-1-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Define block coding and give its purpose.

### Q4-9
> id: ch04-q-q4-9 | type: review_question | group: Questions | ref_sections: [ch04-4-1-4] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Define scrambling and give its purpose.

### Q4-10
> id: ch04-q-q4-10 | type: review_question | group: Questions | ref_sections: [ch04-4-2-1, ch04-4-2-2] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

Compare and contrast PCM and DM.

### Q4-11
> id: ch04-q-q4-11 | type: review_question | group: Questions | ref_sections: [ch04-4-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

What are the differences between parallel and serial transmission?

### Q4-12
> id: ch04-q-q4-12 | type: review_question | group: Questions | ref_sections: [ch04-4-3-2] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

List three different techniques in serial transmission and explain the differences.

## Problems

### P4-1
> id: ch04-q-p4-1 | type: problem | group: Problems | ref_sections: [ch04-4-1-1-signal-element-versus-data-element, ch04-4-1-1-data-rate-versus-signal-rate] | has_figure: true | answer: null | figure_assets: [ch04_ill_002] | src: book PDF pp.37

Calculate the value of the signal rate for each case in Figure 4.2 if the data rate is 1 Mbps and c = 1/2.

> [ASSET_REF ch04_ill_002] See the original figure and its description in assets/manifest.json.

### P4-2
> id: ch04-q-p4-2 | type: problem | group: Problems | ref_sections: [ch04-4-1-1-self-synchronization] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37

In a digital transmission, the sender clock is 0.2 percent faster than the receiver clock. How many extra bits per second does the sender send if the data rate is 1 Mbps?

### P4-3
> id: ch04-q-p4-3 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-nrz-non-return-to-zero, ch04-4-1-2-summary-of-line-coding-schemes] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.37,38

Draw the graph of the NRZ-L scheme using each of the following data streams, assuming that the last signal level has been positive. From the graphs, guess the bandwidth for this scheme using the average number of changes in the signal level. Compare your guess with the corresponding entry in Table 4.1.

**a.** 00000000

**b.** 11111111

**c.** 01010101

**d.** 00110011

### P4-4
> id: ch04-q-p4-4 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-non-return-to-zero-nrz, ch04-4-1-2-summary-of-line-coding-schemes] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.38

Repeat Problem P4-3 for the NRZ-I scheme.

### P4-5
> id: ch04-q-p4-5 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-biphase-manchester-and-differential-manchester, ch04-4-1-2-summary-of-line-coding-schemes] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.38

Repeat Problem P4-3 for the Manchester scheme.

### P4-6
> id: ch04-q-p4-6 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-biphase-manchester-and-differential-manchester, ch04-4-1-2-summary-of-line-coding-schemes] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.38

Repeat Problem P4-3 for the differential Manchester scheme.

### P4-7
> id: ch04-q-p4-7 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-2b1q, ch04-4-1-2-summary-of-line-coding-schemes] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.38

Repeat Problem P4-3 for the 2B1Q scheme, but use the following data streams.

**a.** 0000000000000000

**b.** 1111111111111111

**c.** 0101010101010101

**d.** 0011001100110011

### P4-8
> id: ch04-q-p4-8 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-multitransition-mlt-3, ch04-4-1-2-summary-of-line-coding-schemes] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.38

Repeat Problem P4-3 for the MLT-3 scheme, but use the following data streams.

**a.** 00000000

**b.** 11111111

**c.** 01010101

**d.** 00011000

### P4-9
> id: ch04-q-p4-9 | type: problem | group: Problems | ref_sections: [ch04-4-1-2] | has_figure: true | answer: null | figure_assets: [ch04_ill_036] | src: book PDF pp.38

Find the 8-bit data stream for each case depicted in Figure 4.36.

> **[ASSET ch04_ill_036]** Figure 4.36: Problem P4-9
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_036.png
> - src: book Figure 4.36; p.132
> - shows: Figure 4.36: Problem P4-9. Three waveform panels for Problem P4-9 show NRZ-I, differential Manchester, and AMI signals on aligned bit intervals so the student can decode the corresponding eight-bit streams.
> - structure: Three waveform panels for Problem P4-9 show NRZ-I, differential Manchester, and AMI signals on aligned bit intervals so the student can decode the corresponding eight-bit streams.
> - text_in_image: Time; a. NRZ-I; Time; b. differential Manchester; Time; c. AMI
> - use_when: Teach ch04-q-p4-9, interpret Figure 4.36, or solve a linked practice question.
> - confidence: high

### P4-10
> id: ch04-q-p4-10 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-non-return-to-zero-nrz] | has_figure: true | answer: null | figure_assets: [ch04_ill_006] | src: book PDF pp.38

An NRZ-I signal has a data rate of 100 Kbps. Using Figure 4.6, calculate the value of the normalized energy (P) for frequencies at 0 Hz, 50 KHz, and 100 KHz.

> [ASSET_REF ch04_ill_006] See the original figure and its description in assets/manifest.json.

### P4-11
> id: ch04-q-p4-11 | type: problem | group: Problems | ref_sections: [ch04-4-1-2-biphase-manchester-and-differential-manchester] | has_figure: true | answer: null | figure_assets: [ch04_ill_008] | src: book PDF pp.39

A Manchester signal has a data rate of 100 Kbps. Using Figure 4.8, calculate the value of the normalized energy (P) for frequencies at 0 Hz, 50 KHz, 100 KHz.

> [ASSET_REF ch04_ill_008] See the original figure and its description in assets/manifest.json.

### P4-12
> id: ch04-q-p4-12 | type: problem | group: Problems | ref_sections: [ch04-4-1-3-4b-5b] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

The input stream to a 4B/5B block encoder is 0100 0000 0000 0000 0000 0001 Answer the following questions:

**a.** What is the output stream?

**b.** What is the length of the longest consecutive sequence of 0s in the input?

**c.** What is the length of the longest consecutive sequence of 0s in the output?

### P4-13
> id: ch04-q-p4-13 | type: problem | group: Problems | ref_sections: [ch04-4-1-3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

How many invalid (unused) code sequences can we have in 5B/6B encoding? How many in 3B/4B encoding?

### P4-14
> id: ch04-q-p4-14 | type: problem | group: Problems | ref_sections: [ch04-4-1-4-b8zs, ch04-4-1-4-hdb3] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

What is the result of scrambling the sequence 11100000000000 using each of the following scrambling techniques? Assume that the last non-zero signal level has been positive.

**a.** B8ZS

**b.** HDB3 (The number of nonzero pulses is odd after the last substitution.)

### P4-15
> id: ch04-q-p4-15 | type: problem | group: Problems | ref_sections: [ch04-4-2-1-sampling-rate] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

What is the Nyquist sampling rate for each of the following signals?

**a.** A low-pass signal with bandwidth of 200 KHz?

**b.** A band-pass signal with bandwidth of 200 KHz if the lowest frequency is 100 KHz?

### P4-16
> id: ch04-q-p4-16 | type: problem | group: Problems | ref_sections: [ch04-4-2-1-sampling-rate, ch04-4-2-1-quantization-error, ch04-4-2-1-pcm-bandwidth] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

We have sampled a low-pass signal with a bandwidth of 200 KHz using 1024 levels of quantization.

**a.** Calculate the bit rate of the digitized signal.

**b.** Calculate the SNRdB for this signal.

**c.** Calculate the PCM bandwidth of this signal.

### P4-17
> id: ch04-q-p4-17 | type: problem | group: Problems | ref_sections: [ch04-4-2-1-maximum-data-rate-of-a-channel] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

What is the maximum data rate of a channel with a bandwidth of 200 KHz if we use four levels of digital signaling.

### P4-18
> id: ch04-q-p4-18 | type: problem | group: Problems | ref_sections: [ch04-4-2-1-quantization-error] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

An analog signal has a bandwidth of 20 KHz. If we sample this signal and send it through a 30 Kbps channel, what is the SNRdB?

### P4-19
> id: ch04-q-p4-19 | type: problem | group: Problems | ref_sections: [ch04-4-1-2] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

We have a baseband channel with a 1-MHz bandwidth. What is the data rate for this channel if we use each of the following line coding schemes?

**a.** NRZ-L

**b.** Manchester

**c.** MLT-3

**d.** 2B1Q

### P4-20
> id: ch04-q-p4-20 | type: problem | group: Problems | ref_sections: [ch04-4-3-2-asynchronous-transmission, ch04-4-3-2-synchronous-transmission] | has_figure: false | answer: null | figure_assets: [] | src: book PDF pp.39

We want to transmit 1000 characters with each character encoded as 8 bits.

**a.** Find the number of transmitted bits for synchronous transmission.

**b.** Find the number of transmitted bits for asynchronous transmission.

**c.** Find the redundancy percent in each case.
