---
doc_type: question_bank
course_id: data_communications
chapter: 10
chapter_id: data_communications_ch10
textbook_edition: 5th
groups:
- id: Questions
  label: Questions
  count: 15
- id: Problems
  label: Problems
  count: 30
question_counts:
  Questions: 15
  Problems: 30
spec_version: 1.1-controller
generated_at: '2026-10-07T03:42:37+00:00'
status: complete
---
## Questions

### Q10-1
> id: ch10-q-q10-1 | type: review_question | group: Questions | ref_sections: [ch10-1-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

How does a single-bit error differ from a burst error?

### Q10-2
> id: ch10-q-q10-2 | type: review_question | group: Questions | ref_sections: [ch10-2-1-linear-block-codes] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

What is the definition of a linear block code?

### Q10-3
> id: ch10-q-q10-3 | type: review_question | group: Questions | ref_sections: [ch10-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

In a block code, a dataword is 20 bits and the corresponding codeword is 25 bits. What are the values of k, r, and n according to the definitions in the text? How many redundant bits are added to each dataword?

### Q10-4
> id: ch10-q-q10-4 | type: review_question | group: Questions | ref_sections: [ch10-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

In a codeword, we add two redundant bits to each 8-bit data word. Find the number of
**a.** valid codewords.

**b.** invalid codewords.

### Q10-5
> id: ch10-q-q10-5 | type: review_question | group: Questions | ref_sections: [ch10-2-1-minimum-hamming-distance] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

What is the minimum Hamming distance?

### Q10-6
> id: ch10-q-q10-6 | type: review_question | group: Questions | ref_sections: [ch10-2-1-minimum-hamming-distance] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

If we want to be able to detect two-bit errors, what should be the minimum Hamming distance?

### Q10-7
> id: ch10-q-q10-7 | type: review_question | group: Questions | ref_sections: [ch10-5-1, ch10-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

A category of error detecting (and correcting) code, called the Hamming code, is a code in which $d_{min}$ = 3. This code can detect up to two errors (or correct one single error). In this code, the values of n, k, and r are related as: n = $2^{r}$ − 1 and k = n − r. Find the number of bits in the dataword and the codewords if r is 3.

### Q10-8
> id: ch10-q-q10-8 | type: review_question | group: Questions | ref_sections: [ch10-3-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

In CRC, if the dataword is 5 bits and the codeword is 8 bits, how many 0s need to be added to the dataword to make the dividend? What is the size of the remainder? What is the size of the divisor?

### Q10-9
> id: ch10-q-q10-9 | type: review_question | group: Questions | ref_sections: [ch10-3-4-single-bit-error] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

In CRC, which of the following generators (divisors) guarantees the detection of a single bit error?
**a.** 101

**b.** 100

**c.** 1

### Q10-10
> id: ch10-q-q10-10 | type: review_question | group: Questions | ref_sections: [ch10-3-4-odd-numbers-of-errors] | has_figure: false | answer: null | figure_assets: [] | src: book p.287

In CRC, which of the following generators (divisors) guarantees the detection of an odd number of errors?
**a.** 10111

**b.** 101101

**c.** 111

### Q10-11
> id: ch10-q-q10-11 | type: review_question | group: Questions | ref_sections: [ch10-3-4-burst-errors] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

In CRC, we have chosen the generator 1100101. What is the probability of detecting a burst error of length
**a.** 5?

**b.** 7?

**c.** 10?

### Q10-12
> id: ch10-q-q10-12 | type: review_question | group: Questions | ref_sections: [ch10-4-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

Assume we are sending data items of 16-bit length. If two data items are swapped during transmission, can the traditional checksum detect this error? Explain.

### Q10-13
> id: ch10-q-q10-13 | type: review_question | group: Questions | ref_sections: [ch10-4-1-internet-checksum] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

Can the value of a traditional checksum be all 0s (in binary)? Defend your answer.

### Q10-14
> id: ch10-q-q10-14 | type: review_question | group: Questions | ref_sections: [ch10-4-2-fletcher-checksum] | has_figure: true | answer: null | figure_assets: [ch10_ill_018] | src: book p.288

Show how the Fletcher algorithm (Figure 10.18) attaches weights to the data items when calculating the checksum.

> [ASSET_REF ch10_ill_018] See the original figure and its description in assets/manifest.json.

### Q10-15
> id: ch10-q-q10-15 | type: review_question | group: Questions | ref_sections: [ch10-4-2-adler-checksum] | has_figure: true | answer: null | figure_assets: [ch10_ill_019] | src: book p.288

Show how the Adler algorithm (Figure 10.19) attaches weights to the data items when calculating the checksum.

> [ASSET_REF ch10_ill_019] See the original figure and its description in assets/manifest.json.

## Problems

### P10-1
> id: ch10-q-p10-1 | type: problem | group: Problems | ref_sections: [ch10-1-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

What is the maximum effect of a 2-ms burst of noise on data transmitted at the following rates?
**a.** 1500 bps

**b.** 12 kbps

**c.** 100 kbps

**d.** 100 Mbps

### P10-2
> id: ch10-q-p10-2 | type: problem | group: Problems | ref_sections: [ch10-1-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

Assume that the probability that a bit in a data unit is corrupted during transmission is p. Find the probability that x number of bits are corrupted in an n-bit data unit for each of the following cases.
**a.** n = 8, x = 1, p = 0.2

**b.** n = 16, x = 3, p = 0.3

**c.** n = 32, x = 10, p = 0.4

### P10-3
> id: ch10-q-p10-3 | type: problem | group: Problems | ref_sections: [ch10-2-1-hamming-distance] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

Exclusive-OR (XOR) is one of the most used operations in the calculation of codewords. Apply the exclusive-OR operation on the following pairs of patterns. Interpret the results.
**a.** (10001) ⊕ (10001)

**b.** (11100) ⊕ (00000)

**c.** (10011) ⊕ (11111)

### P10-4
> id: ch10-q-p10-4 | type: problem | group: Problems | ref_sections: [ch10-example-10-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

In Table 10.1, the sender sends dataword 10. A 3-bit burst error corrupts the codeword. Can the receiver detect the error? Defend your answer.

### P10-5
> id: ch10-q-p10-5 | type: problem | group: Problems | ref_sections: [ch10-2-1-parity-check-code] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

Using the code in Table 10.2, what is the dataword if each of the following codewords is received?
**a.** 01011

**b.** 11111

**c.** 00000

**d.** 11011

### P10-6
> id: ch10-q-p10-6 | type: problem | group: Problems | ref_sections: [ch10-2-1-linear-block-codes] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

Prove that the code represented by the following codewords is not linear. You need to find only one case that violates the linearity. {(00000), (01011), (10111), (11111)}

### P10-7
> id: ch10-q-p10-7 | type: problem | group: Problems | ref_sections: [ch10-2-1-hamming-distance] | has_figure: false | answer: null | figure_assets: [] | src: book p.288

What is the Hamming distance for each of the following codewords?
**a.** d (10000, 00000)

**b.** d (10101, 10000)

**c.** d (00000, 11111)

**d.** d (00000, 00000)

### P10-8
> id: ch10-q-p10-8 | type: problem | group: Problems | ref_sections: [ch10-3, ch10-3-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.289

Although it can be formally proved that the code in Table 10.3 is both linear and cyclic, use only two tests to partially prove the fact:
**a.** Test the cyclic property on codeword 0101100.

**b.** Test the linear property on codewords 0010110 and 1111111.

### P10-9
> id: ch10-q-p10-9 | type: problem | group: Problems | ref_sections: [ch10-3-6, ch10-3-4-burst-errors] | has_figure: false | answer: null | figure_assets: [] | src: book p.289

Referring to the CRC-8 in Table 10.4, answer the following questions:
**a.** Does it detect a single error? Defend your answer.

**b.** Does it detect a burst error of size 6? Defend your answer.

**c.** What is the probability of detecting a burst error of size 9?

**d.** What is the probability of detecting a burst error of size 15?

### P10-10
> id: ch10-q-p10-10 | type: problem | group: Problems | ref_sections: [ch10-2-1-parity-check-code] | has_figure: false | answer: null | figure_assets: [] | src: book p.289

Assuming even parity, find the parity bit for each of the following data units.
**a.** 1001011

**b.** 0001100

**c.** 1000000

**d.** 1110111

### P10-11
> id: ch10-q-p10-11 | type: problem | group: Problems | ref_sections: [ch10-2-1-parity-check-code] | has_figure: true | answer: null | figure_assets: [ch10_qf_001] | src: book p.289

A simple parity-check bit, which is normally added at the end of the word (changing a 7-bit ASCII character to a byte), cannot detect even numbers of errors. For example, two, four, six, or eight errors cannot be detected in this way. A better solution is to organize the characters in a table and create row and column parities. The bit in the row parity is sent with the byte, the column parity is sent as an extra byte (Figure 10.23). Show how the following errors can be detected:
**a.** An error at (R3, C3).

**b.** Two errors at (R3, C4) and (R3, C6).

**c.** Three errors at (R2, C4), (R2, C5), and (R3, C4).

**d.** Four errors at (R1, C2), (R1, C6), (R3, C2), and (R3, C6).

> **[ASSET ch10_qf_001]** Figure 10.23: P10-11
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_qf_001.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 33, 'label': 'Figure 10.23'}
> - shows: Figure 10.23: P10-11. Four row-and-column parity grids demonstrate one corrected error, two detected errors, three detected errors, and a four-corner pattern that remains undetected.
> - structure: Four row-and-column parity grids demonstrate one corrected error, two detected errors, three detected errors, and a four-corner pattern that remains undetected.
> - text_in_image: C1 C2 C3 C4 C5 C6; C7; C1 C2 C3 C4 C5 C6; C7; 1  1  0  0  1  1  1  1; 1  1  0  0  1  1  1  1; R1; R1; R2; 1  0  1  1  1  0  1  1; 1  0  1  1  1  0  1  1; R2; R3; 0  1  1  1  0  0  1  0; 0  1  1  0  0  1  1  0; R3; R4; 0  1  0  1  0  0  1  1; 0  1  0  1  0  0  1  1; R4; 0  1  0  1  0  1  0  1; 0  1  0  1  0  1  0  1; a. Detected and corrected; b. Detected; C1 C2 C3 C4 C5 C6; C7; C1 C2 C3 C4 C5 C6; C7; 1  1  0  0  1  1  1  1; 1  0  0  0  1  0  1  1; R1; R1; R2; R2; 1  0  1  0  0  0  1  1; 1  0  1  1  1  0  1  1; R3; R3; 0  1  1  0  0  0  1  0; 0  0  1  1  0  1  1  0; R4; 0  1  0  1  0  0  1  1; R4; 0  1  0  1  0  0  1  1; 0  1  0  1  0  1  0  1; 0  1  0  1  0  1  0  1; c. Detected; d. Not detected
> - use_when: Teach ch10-q-p10-11, interpret Figure 10.23, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

### P10-12
> id: ch10-q-p10-12 | type: problem | group: Problems | ref_sections: [ch10-3-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Given the dataword 101001111 and the divisor 10111, show the generation of the CRC codeword at the sender site (using binary division).

### P10-13
> id: ch10-q-p10-13 | type: problem | group: Problems | ref_sections: [ch10-3-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Apply the following operations on the corresponding polynomials:
**a.** ($x^{3}$ + $x^{2}$ + x + 1) + ($x^{4}$ + $x^{2}$ + x + 1)

**b.** ($x^{3}$ + $x^{2}$ + x + 1) − ($x^{4}$ + $x^{2}$ + x + 1)

**c.** ($x^{3}$ + $x^{2}$) × ($x^{4}$ + $x^{2}$ + x + 1)

**d.** ($x^{3}$ + $x^{2}$ + x + 1) / ($x^{2}$ + 1)

### P10-14
> id: ch10-q-p10-14 | type: problem | group: Problems | ref_sections: [ch10-3-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Answer the following questions:
**a.** What is the polynomial representation of 101110?

**b.** What is the result of shifting 101110 three bits to the left?

**c.** Repeat part b using polynomials.

**d.** What is the result of shifting 101110 four bits to the right?

**e.** Repeat part d using polynomials.

### P10-15
> id: ch10-q-p10-15 | type: problem | group: Problems | ref_sections: [ch10-3-4-single-bit-error] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Which of the following CRC generators guarantee the detection of a single bit error?
**a.** $x^{3}$ + x + 1

**b.** $x^{4}$ + $x^{2}$

**d.** $x^{2}$ + 1

**c.** 1

### P10-16
> id: ch10-q-p10-16 | type: problem | group: Problems | ref_sections: [ch10-3-6, ch10-3-4-burst-errors] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Referring to the CRC-8 polynomial in Table 10.4, answer the following questions:
**a.** Does it detect a single error? Defend your answer.

**b.** Does it detect a burst error of size 6? Defend your answer.

**c.** What is the probability of detecting a burst error of size 9?

**d.** What is the probability of detecting a burst error of size 15?

### P10-17
> id: ch10-q-p10-17 | type: problem | group: Problems | ref_sections: [ch10-3-6, ch10-3-4-burst-errors] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Referring to the CRC-32 polynomial in Table 10.4, answer the following questions:
**a.** Does it detect a single error? Defend your answer.

**b.** Does it detect a burst error of size 16? Defend your answer.

**c.** What is the probability of detecting a burst error of size 33?

**d.** What is the probability of detecting a burst error of size 55?

### P10-18
> id: ch10-q-p10-18 | type: problem | group: Problems | ref_sections: [ch10-4-1-internet-checksum] | has_figure: true | answer: null | figure_assets: [ch10_ill_017] | src: book p.290

Assume a packet is made only of four 16-bit words $\mathrm{(A7A2)}_{16}$, $\mathrm{(CABF)}_{16}$, $\mathrm{(903A)}_{16}$, and $\mathrm{(A123)}_{16}$. Manually simulate the algorithm in Figure 10.17 to find the checksum.

> [ASSET_REF ch10_ill_017] See the original figure and its description in assets/manifest.json.

### P10-19
> id: ch10-q-p10-19 | type: problem | group: Problems | ref_sections: [ch10-4-1-internet-checksum] | has_figure: false | answer: null | figure_assets: [] | src: book p.290

Traditional checksum calculation needs to be done in one’s complement arithmetic. Computers and calculators today are designed to do calculations in two’s complement arithmetic. One way to calculate the traditional checksum is to add the numbers in two’s complement arithmetic, find the quotient and remainder of dividing the result by $2^{16}$, and add the quotient and the remainder to get the sum in one’s complement. The checksum can be found by subtracting the sum from $2^{16}$ − 1. Use the above method to find the checksum of the following four numbers: 43,689, 64,463, 45,112, and 59,683.

### P10-20
> id: ch10-q-p10-20 | type: problem | group: Problems | ref_sections: [ch10-4-1-internet-checksum] | has_figure: false | answer: null | figure_assets: [] | src: book p.291

This problem shows a special case in checksum handling. A sender has two data items to send: $\mathrm{(4567)}_{16}$ and $\mathrm{(BA98)}_{16}$. What is the value of the checksum?

### P10-21
> id: ch10-q-p10-21 | type: problem | group: Problems | ref_sections: [ch10-4-2-fletcher-checksum] | has_figure: true | answer: null | figure_assets: [ch10_ill_018] | src: book p.291

Manually simulate the Fletcher algorithm (Figure 10.18) to calculate the checksum of the following bytes: $\mathrm{(2B)}_{16}$, $\mathrm{(3F)}_{16}$, $\mathrm{(6A)}_{16}$, and $\mathrm{(AF)}_{16}$. Also show that the result is a weighted checksum.

> [ASSET_REF ch10_ill_018] See the original figure and its description in assets/manifest.json.

### P10-22
> id: ch10-q-p10-22 | type: problem | group: Problems | ref_sections: [ch10-4-2-adler-checksum] | has_figure: true | answer: null | figure_assets: [ch10_ill_019] | src: book p.291

Manually simulate the Adler algorithm (Figure 10.19) to calculate the checksum of the following words: $\mathrm{(FBFF)}_{16}$ and $\mathrm{(EFAA)}_{16}$. Also show that the result is a weighted checksum.

> [ASSET_REF ch10_ill_019] See the original figure and its description in assets/manifest.json.

### P10-23
> id: ch10-q-p10-23 | type: problem | group: Problems | ref_sections: [ch10-4-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.291

One of the examples of a weighted checksum is the ISBN-10 code we see printed on the back cover of some books. In ISBN-10, there are 9 decimal digits that define the country, the publisher, and the book. The tenth (rightmost) digit is a checksum digit. The code $D_1D_2\dots D_9C$ satisfies
$$[10D_1+9D_2+8D_3+\dots+2D_9+C]\bmod 11=0.$$
The weights are 10, 9, ..., 1. If the calculated value for C is 10, one uses the letter X instead. By replacing each weight w with its complement in modulo 11 arithmetic (11 − w), it can be shown that the check digit can be calculated as shown below. The check digit can be calculated as
$$C=[D_1+2D_2+3D_3+\dots+9D_9]\bmod 11.$$
Calculate the check digit for ISBN-10: 0-07-296775-C.

### P10-24
> id: ch10-q-p10-24 | type: problem | group: Problems | ref_sections: [ch10-4-2] | has_figure: false | answer: null | figure_assets: [] | src: book p.291

An ISBN-13 code, a new version of ISBN-10, is another example of a weighted checksum with 13 digits, in which there are 12 decimal digits defining the book and the last digit is the checksum digit. The code $D_1D_2\dots D_{12}C$ satisfies
$$[D_1+3D_2+D_3+\dots+3D_{12}+C]\bmod 10=0.$$
The weights alternate between 1 and 3. Using the above description, calculate the check digit for ISBN-13: 978-0-07-296775-C.

### P10-25
> id: ch10-q-p10-25 | type: problem | group: Problems | ref_sections: [ch10-5-3] | has_figure: false | answer: null | figure_assets: [] | src: book p.291

In the interleaving approach to FEC, assume each packet contains 10 samples from a sampled piece of music. Instead of loading the first packet with the first 10 samples, the second packet with the second 10 samples, and so on, the sender loads the first packet with the odd-numbered samples of the first 20 samples, the second packet with the even-numbered samples of the first 20 samples, and so on. The receiver reorders the samples and plays them. Now assume that the third packet is lost in transmission. What will be missed at the receiver site?

### P10-26
> id: ch10-q-p10-26 | type: problem | group: Problems | ref_sections: [ch10-5-1, ch10-example-10-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.292

Assume we want to send a dataword of two bits using FEC based on the Hamming distance. Show how the following list of datawords/codewords can automatically correct up to a one-bit error in transmission. 00 → 00000 01→ 01011 10 → 10101 11 → 11110

### P10-27
> id: ch10-q-p10-27 | type: problem | group: Problems | ref_sections: [ch10-5-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.292

Assume we need to create codewords that can automatically correct a one-bit error. What should the number of redundant bits (r) be, given the number of bits in the dataword (k)? Remember that the codeword needs to be n = k + r bits, called C(n, k). After finding the relationship, find the number of bits in r if k is 1, 2, 5, 50, or 1000.

### P10-28
> id: ch10-q-p10-28 | type: problem | group: Problems | ref_sections: [ch10-5-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.292

In the previous problem we tried to find the number of bits to be added to a dataword to correct a single-bit error. If we need to correct more than one bit, the number of redundant bits increases. What should the number of redundant bits (r) be to automatically correct one or two bits (not necessarily contiguous) in a dataword of size k? After finding the relationship, find the number of bits in r if k is 1, 2, 5, 50, or 1000.

### P10-29
> id: ch10-q-p10-29 | type: problem | group: Problems | ref_sections: [ch10-5-1] | has_figure: false | answer: null | figure_assets: [] | src: book p.292

Using the ideas in the previous two problems, we can create a general formula for correcting any number of errors (m) in a codeword of size (n). Develop such a formula. Use the combination of n objects taking x objects at a time.

### P10-30
> id: ch10-q-p10-30 | type: problem | group: Problems | ref_sections: [ch10-5-5] | has_figure: true | answer: null | figure_assets: [ch10_ill_022] | src: book p.292

In Figure 10.22, assume we have 100 packets. We have created two sets of packets with high and low resolutions. Each high-resolution packet carries on average 700 bits. Each low-resolution packet carries on average 400 bits. How many extra bits are we sending in this scheme for the sake of FEC? What is the percentage of overhead?

> [ASSET_REF ch10_ill_022] See the original figure and its description in assets/manifest.json.
