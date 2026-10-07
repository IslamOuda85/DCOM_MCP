---
doc_type: question_bank
course_id: data_communications
chapter: 5
chapter_id: data_communications_ch05
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 10
- id: Problems
  label: Problems
  count: 12
question_counts:
  Questions: 10
  Problems: 12
spec_version: 1.1-controller
generated_at: '2026-10-07T03:08:10+00:00'
status: complete
---
## Questions

### Q5-1
> id: ch05-q-q5-1 | type: review_question | group: Questions | ref_sections: [ch05-0] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Define analog transmission.

### Q5-2
> id: ch05-q-q5-2 | type: review_question | group: Questions | ref_sections: [ch05-5-1-1-carrier-signal] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Define carrier signal and explain its role in analog transmission.

### Q5-3
> id: ch05-q-q5-3 | type: review_question | group: Questions | ref_sections: [ch05-5-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Define digital-to-analog conversion.

### Q5-4
> id: ch05-q-q5-4 | type: review_question | group: Questions | ref_sections: [ch05-5-1-2, ch05-5-1-3, ch05-5-1-4, ch05-5-1-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Which characteristics of an analog signal are changed to represent the digital signal in each of the following digital-to-analog conversions?

**a.** ASK

**b.** FSK

**c.** PSK

**d.** QAM

### Q5-5
> id: ch05-q-q5-5 | type: review_question | group: Questions | ref_sections: [ch05-5-1-2, ch05-5-1-4-binary-psk-bpsk] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Which of the four digital-to-analog conversion techniques (ASK, FSK, PSK or QAM) is the most susceptible to noise? Defend your answer.

### Q5-6
> id: ch05-q-q5-6 | type: review_question | group: Questions | ref_sections: [ch05-5-1-4-constellation-diagram] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Define constellation diagram and explain its role in analog transmission.

### Q5-7
> id: ch05-q-q5-7 | type: review_question | group: Questions | ref_sections: [ch05-5-1-4-constellation-diagram] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

What are the two components of a signal when the signal is represented on a constellation diagram? Which component is shown on the horizontal axis? Which is shown on the vertical axis?

### Q5-8
> id: ch05-q-q5-8 | type: review_question | group: Questions | ref_sections: [ch05-5-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Define analog-to-analog conversion.

### Q5-9
> id: ch05-q-q5-9 | type: review_question | group: Questions | ref_sections: [ch05-5-2-1, ch05-5-2-2, ch05-5-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Which characteristics of an analog signal are changed to represent the lowpass analog signal in each of the following analog-to-analog conversions?

**a.** AM

**b.** FM

**c.** PM

### Q5-10
> id: ch05-q-q5-10 | type: review_question | group: Questions | ref_sections: [ch05-5-2-1, ch05-5-2-2, ch05-5-2-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.152

Which of the three analog-to-analog conversion techniques (AM, FM, or PM) is the most susceptible to noise? Defend your answer.

## Problems

### P5-1
> id: ch05-q-p5-1 | type: problem | group: Problems | ref_sections: [ch05-5-1-1-data-rate-versus-signal-rate, ch05-5-1-2, ch05-5-1-3, ch05-5-1-4-quadrature-psk-qpsk, ch05-5-1-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

Calculate the baud rate for the given bit rate and type of modulation.

**a.** 2000 bps, FSK

**b.** 4000 bps, ASK

**c.** 6000 bps, QPSK

**d.** 36,000 bps, 64-QAM

### P5-2
> id: ch05-q-p5-2 | type: problem | group: Problems | ref_sections: [ch05-5-1-1-data-rate-versus-signal-rate, ch05-5-1-2, ch05-5-1-3, ch05-5-1-4-binary-psk-bpsk, ch05-5-1-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

Calculate the bit rate for the given baud rate and type of modulation.

**a.** 1000 baud, FSK

**b.** 1000 baud, ASK

**c.** 1000 baud, BPSK

**d.** 1000 baud, 16-QAM

### P5-3
> id: ch05-q-p5-3 | type: problem | group: Problems | ref_sections: [ch05-5-1-1-data-rate-versus-signal-rate, ch05-5-1-2-multilevel-ask, ch05-5-1-3-multilevel-fsk, ch05-5-1-4, ch05-5-1-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

What is the number of bits per baud for the following techniques?

**a.** ASK with four different amplitudes

**b.** FSK with eight different frequencies

**c.** PSK with four different phases

**d.** QAM with a constellation of 128 points

### P5-4
> id: ch05-q-p5-4 | type: problem | group: Problems | ref_sections: [ch05-5-1-4-constellation-diagram, ch05-5-1-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

Draw the constellation diagram for the following:

**a.** ASK, with peak amplitude values of 1 and 3

**b.** BPSK, with a peak amplitude value of 2

**c.** QPSK, with a peak amplitude value of 3

**d.** 8-QAM with two different peak amplitude values, 1 and 3, and four different phases

### P5-5
> id: ch05-q-p5-5 | type: problem | group: Problems | ref_sections: [ch05-5-1-4-constellation-diagram, ch05-5-1-5] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

Draw the constellation diagram for the following cases. Find the peak amplitude value for each case and define the type of modulation (ASK, FSK, PSK, or QAM). The numbers in parentheses define the values of I and Q respectively.

**a.** Two points at (2, 0) and (3, 0)

**b.** Two points at (3, 0) and (−3, 0)

**c.** Four points at (2, 2), (−2, 2), (−2, −2), and (2, −2)

**d.** Two points at (0, 2) and (0, −2)

### P5-6
> id: ch05-q-p5-6 | type: problem | group: Problems | ref_sections: [ch05-5-1-1-data-rate-versus-signal-rate, ch05-5-1-4-constellation-diagram] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

How many bits per baud can we send in each of the following cases if the signal constellation has one of the following number of points?

**a.** 2

**b.** 4

**c.** 16

**d.** 1024

### P5-7
> id: ch05-q-p5-7 | type: problem | group: Problems | ref_sections: [ch05-5-1-2-bandwidth-for-ask, ch05-5-1-3-bandwidth-for-bfsk, ch05-5-1-4-bandwidth, ch05-5-1-5-bandwidth-for-qam] | has_figure: false | answer: null | figure_assets: [] | src: book p.153

What is the required bandwidth for the following cases if we need to send 4000 bps? Let d = 1.

**a.** ASK

**b.** FSK with 2Δf = 4 kHz

**c.** QPSK

**d.** 16-QAM

### P5-8
> id: ch05-q-p5-8 | type: problem | group: Problems | ref_sections: [ch05-5-1-2-bandwidth-for-ask, ch05-5-1-4-bandwidth, ch05-5-1-5-bandwidth-for-qam] | has_figure: false | answer: null | figure_assets: [] | src: book p.154

The telephone line has 4 kHz bandwidth. What is the maximum number of bits we can send using each of the following techniques? Let d = 0.

**a.** ASK

**b.** QPSK

**c.** 16-QAM

**d.** 64-QAM

### P5-9
> id: ch05-q-p5-9 | type: problem | group: Problems | ref_sections: [ch05-5-1-1-data-rate-versus-signal-rate, ch05-5-1-5-bandwidth-for-qam] | has_figure: false | answer: null | figure_assets: [] | src: book p.154

A corporation has a medium with a 1-MHz bandwidth (lowpass). The corporation needs to create 10 separate independent channels each capable of sending at least 10 Mbps. The company has decided to use QAM technology. What is the minimum number of bits per baud for each channel? What is the number of points in the constellation diagram for each channel? Let d = 0.

### P5-10
> id: ch05-q-p5-10 | type: problem | group: Problems | ref_sections: [ch05-5-1-1-data-rate-versus-signal-rate, ch05-5-1-5-bandwidth-for-qam] | has_figure: false | answer: null | figure_assets: [] | src: book p.154

A cable company uses one of the cable TV channels (with a bandwidth of 6 MHz) to provide digital communication for each resident. What is the available data rate for each resident if the company uses a 64-QAM technique?

### P5-11
> id: ch05-q-p5-11 | type: problem | group: Problems | ref_sections: [ch05-5-2-1-am-bandwidth, ch05-5-2-2-fm-bandwidth, ch05-5-2-3-pm-bandwidth] | has_figure: false | answer: null | figure_assets: [] | src: book p.154

Find the bandwidth for the following situations if we need to modulate a 5-kHz voice.

**a.** AM

**b.** FM ($\beta=5$)

**c.** PM ($\beta=1$)
### P5-12
> id: ch05-q-p5-12 | type: problem | group: Problems | ref_sections: [ch05-5-2-1-standard-bandwidth-allocation-for-am-radio, ch05-5-2-2-standard-bandwidth-allocation-for-fm-radio] | has_figure: false | answer: null | figure_assets: [] | src: book p.154

Find the total number of channels in the corresponding band allocated by FCC.

**a.** AM

**b.** FM
