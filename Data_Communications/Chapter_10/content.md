---
doc_type: scientific_content
course_id: data_communications
chapter: 10
chapter_id: data_communications_ch10
chapter_title: Error Detection and Correction
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_10/ch10.pdf
  pages: 257-292
assets_dir: assets
asset_counts:
  illustration: 23
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:42:37+00:00'
status: complete
---
# Chapter 10: Error Detection and Correction

## Chapter Objectives
> id: ch10-0 | src: book p.257 | kind: objectives

Networks must be able to transfer data from one device to another with acceptable accuracy. For most applications, a system must guarantee that the data received are identical to the data transmitted. Any time data are transmitted from one node to the next, they can become corrupted in passage. Many factors can alter one or more bits of a message. Some applications require a mechanism for detecting and correcting errors.

Some applications can tolerate a small level of error. For example, random errors in audio or video transmissions may be tolerable, but when we transfer text, we expect a very high level of accuracy. At the data-link layer, if a frame is corrupted between two nodes, it needs to be corrected before it continues its journey to other nodes. However, most link-layer protocols simply discard the frame and let upper-layer protocols handle retransmission. Some multimedia applications, however, try to correct the corrupted frame.

This chapter is organized around five main areas:
- The first section introduces types of errors, the concept of redundancy, and distinguishes between error detection and correction.
- The second section discusses block coding. It shows how errors can be detected using block coding and introduces the concept of Hamming distance.
- The third section discusses cyclic codes, focusing on the cyclic redundancy check (CRC) common in the data-link layer, its polynomial representation, and its hardware implementation.
- The fourth section discusses checksums, including one's complement calculation, the traditional Internet checksum, and alternative weighted algorithms.
- The fifth section discusses forward error correction (FEC) using Hamming distance, XOR operations, chunk interleaving, and packet compounding.

## 10.1 Introduction
> id: ch10-1 | src: book 10.1; p.258 | kind: concept

Let us first discuss some issues related, directly or indirectly, to error detection and correction.

### 10.1.1 Types of Errors
> id: ch10-1-1 | src: book 10.1.1; p.258 | kind: concept

Whenever bits flow from one point to another, they are subject to unpredictable changes because of interference. This interference can change the shape of the signal.

The term **single-bit error** means that only 1 bit of a given data unit (such as a byte, character, or packet) is changed from 1 to 0 or from 0 to 1.

The term **burst error** means that 2 or more bits in the data unit have changed from 1 to 0 or from 0 to 1. Figure 10.1 shows the effect of a single-bit and a burst error on a data unit.

> **[ASSET ch10_ill_001]** Figure 10.1: Single-bit and burst error
> - type: illustration
> - kind: waveform
> - file: assets/ch10_ill_001.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 2, 'label': 'Figure 10.1'}
> - shows: Figure 10.1: Single-bit and burst error. Two sent and received bit strings contrast one changed bit with an eight-bit burst span whose endpoints and internal corruptions are marked.
> - structure: Two sent and received bit strings contrast one changed bit with an eight-bit burst span whose endpoints and internal corruptions are marked.
> - text_in_image: Length of burst error (8 bits); 0 1 0 0 1 1 0 1 0 1 0 0 0 0 1 1; Sent; Sent; 0 0 0 0 0 0 1 0; Corrupted bit; Corrupted bits; 0 1 0 1 0 1 0 0 0 1 1 0 0 0 1 1; 0 0 0 0 1 0 1 0; Received; Received; a. Single-bit error; b. Burst error
> - use_when: Teach ch10-1-1, interpret Figure 10.1, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

A burst error is more likely to occur than a single-bit error because the duration of the noise signal is normally longer than the duration of 1 bit, which means that when noise affects data, it affects a set of bits. The number of bits affected depends on the data rate and duration of noise. For example, if we are sending data at 1 kbps, a noise of 1/100 second can affect 10 bits; if we are sending data at 1 Mbps, the same noise can affect 10,000 bits.

### 10.1.2 Redundancy
> id: ch10-1-2 | src: book 10.1.2; p.258 | kind: concept

The central concept in detecting or correcting errors is **redundancy**. To be able to detect or correct errors, we need to send some extra bits with our data. These redundant bits are added by the sender and removed by the receiver. Their presence allows the receiver to detect or correct corrupted bits.

### 10.1.3 Detection Versus Correction
> id: ch10-1-3 | src: book 10.1.3; pp.258-259 | kind: comparison

The correction of errors is more difficult than the detection.

In **error detection**, we are only looking to see if any error has occurred. The answer is a simple yes or no. We are not even interested in the number of corrupted bits. A single-bit error is the same for us as a burst error.

In **error correction**, we need to know the exact number of bits that are corrupted and, more importantly, their location in the message. The number of errors and the size of the message are important factors. If we need to correct a single error in an 8-bit data unit, we need to consider eight possible error locations; if we need to correct two errors in the same data unit, we need to consider 28 possible error combinations.

### 10.1.4 Coding
> id: ch10-1-4 | src: book 10.1.4; p.259 | kind: concept

Redundancy is achieved through various coding schemes. The sender adds redundant bits through a process that creates a relationship between the redundant bits and the actual data bits. The receiver checks the relationships between the two sets of bits to detect or correct errors.

The ratio of redundant bits to data bits and the robustness of the relationships are important factors in any coding scheme. There are two main categories of coding schemes:
- **Block coding**
- **Convolution coding**

In this chapter, we concentrate on block coding.

## 10.2 Block Coding
> id: ch10-2 | src: book 10.2; pp.259-264 | kind: concept

In block coding, we divide our message into blocks, each of $k$ bits, called **datawords**. We add $r$ redundant bits to each block to make the length $n = k + r$. The resulting $n$-bit blocks are called **codewords**.

With $k$ bits, we can create a combination of $2^k$ datawords; with $n$ bits, we can create a combination of $2^n$ codewords. Since $n > k$, the number of possible codewords is larger than the number of possible datawords:
$$2^n > 2^k$$

The block coding process is one-to-one; the same dataword is always encoded as the same codeword. This means that we have $2^n - 2^k$ codewords that are not used. These unused codewords are called invalid codewords.

### 10.2.1 Error Detection
> id: ch10-2-1 | src: book 10.2.1; pp.259-264 | kind: mechanism

How can errors be detected by using block coding? If the following two conditions are met, the receiver can detect a change in the original codeword:
1. The receiver has (or can find) a list of valid codewords.
2. The original codeword has changed to an invalid one.

Figure 10.2 shows the role of block coding in error detection.

> **[ASSET ch10_ill_002]** Figure 10.2: Process of error detection in block coding
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_002.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 4, 'label': 'Figure 10.2'}
> - shows: Figure 10.2: Process of error detection in block coding. A sender maps a k-bit dataword through a generator to an n-bit codeword; after an unreliable channel, a checker either extracts the dataword or discards the word.
> - structure: A sender maps a k-bit dataword through a generator to an n-bit codeword; after an unreliable channel, a checker either extracts the dataword or discards the word.
> - text_in_image: Sender; Receiver; Decoder; Encoder; k bits; k bits; Dataword; Dataword; Extract; Generator; Checker; Discard; Unreliable; transmission; n bits; Codeword; Codeword; n bits
> - use_when: Teach ch10-2-1, interpret Figure 10.2, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

The sender creates codewords out of datawords by using a generator. The codeword is sent over an unreliable channel where it may be corrupted. The receiver receives a codeword and passes it to a checker. If the codeword is valid, the checker extracts the dataword and accepts it; otherwise, the codeword is discarded.

#### Example 10.1
> id: ch10-example-10-1 | src: book Example 10.1; p.260 | kind: worked_example
Let us assume that $k = 2$ and $n = 3$. Table 10.1 shows the list of datawords and codewords. Later, we will see how to derive a codeword from a dataword.

**Table 10.1: A code for error detection in Example 10.1**

| Dataword | Codeword | Dataword | Codeword |
|---|---|---|---|
| 00 | 000 | 10 | 101 |
| 01 | 011 | 11 | 110 |

Assume the sender encodes the dataword 01 as 011 and sends it to the receiver. Consider the following cases:
1. The receiver receives 011. It is a valid codeword. The receiver accepts it and extracts the dataword 01.
2. The codeword is corrupted during transmission, and 111 is received (the leftmost bit is corrupted). The receiver discards 111 because it is not in the list of valid codewords.
3. The codeword is corrupted during transmission, and 000 is received (the rightmost two bits are corrupted). The receiver accepts it and extracts the dataword 00, which is wrong. The error is undetected.

> **Book note:** An error-detecting code can detect only the types of errors for which it is designed; other types of errors may remain undetected.

#### Hamming Distance
> id: ch10-2-1-hamming-distance | src: book 10.2.1; pp.260-261 | kind: formula
A central concept in coding is the **Hamming distance**. The Hamming distance between two words of the same size is the number of positions in which the corresponding bits differ. It is written as $d(x,y)$. The distance between the sent and received words equals the number of bits corrupted during transmission.

The distance is found by XORing the words and counting the 1s:
$$d(x,y)=\operatorname{weight}(x \oplus y)$$

#### Example 10.2
> id: ch10-example-10-2 | src: book Example 10.2; p.261 | kind: worked_example

For $000$ and $011$, $000 \oplus 011=011$, which has two 1s, so $d(000,011)=2$. For $10101$ and $11110$, the XOR result is $01011$, which has three 1s, so $d(10101,11110)=3$.

#### Minimum Hamming Distance for Error Detection
> id: ch10-2-1-minimum-hamming-distance | src: book 10.2.1; pp.261-262 | kind: formula
For a set of valid codewords, $d_{\min}$ is the smallest Hamming distance among every pair of distinct valid codewords. To guarantee detection of up to $s$ errors, valid codewords must be separated by at least:
$$d_{\min}=s+1$$

A code can sometimes detect more than $s$ errors, but only $s$ or fewer are guaranteed. Figure 10.3 shows every word produced by up to $s$ errors inside the radius-$s$ neighborhood of the sent word; another valid word must remain outside it.

> **[ASSET ch10_ill_003]** Figure 10.3: Geometric concept explaining dmin in error detection
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_003.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 6, 'label': 'Figure 10.3'}
> - shows: Figure 10.3: Geometric concept explaining dmin in error detection. A radius-s neighborhood around valid codeword x contains every word produced by up to s errors, while another valid word y lies beyond minimum distance d_min.
> - structure: A radius-s neighborhood around valid codeword x contains every word produced by up to s errors, while another valid word y lies beyond minimum distance d_min.
> - text_in_image: Legend; Any valid codeword; Radius s; y; x; Any corrupted codeword; with 1 to s errors; dmin > s
> - use_when: Teach ch10-2-1, interpret Figure 10.3, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

#### Example 10.3
> id: ch10-example-10-3 | src: book Example 10.3; p.261 | kind: worked_example

The code in Table 10.1 has $d_{\min}=2$, so it guarantees detection of one error. Two changed bits can transform one valid codeword into another and remain undetected.

#### Example 10.4
> id: ch10-example-10-4 | src: book Example 10.4; p.261 | kind: worked_example

A code with $d_{\min}=4$ guarantees detection of up to three errors because $s=d_{\min}-1=3$.

#### Linear Block Codes
> id: ch10-2-1-linear-block-codes | src: book 10.2.1; p.262 | kind: concept
Almost all block codes used today are **linear block codes**. In a linear block code, the XOR (addition modulo 2) of any two valid codewords is another valid codeword.

#### Example 10.5
> id: ch10-example-10-5 | src: book Example 10.5; p.262 | kind: worked_example

The code in Table 10.1 is linear: XORing any two codewords gives another valid codeword. For example, $011 \oplus 101=110$.

#### Minimum Distance for Linear Block Codes
> id: ch10-2-1-minimum-distance-linear | src: book 10.2.1; p.262 | kind: formula
For a linear block code, $d_{\min}$ equals the smallest number of 1s in any nonzero valid codeword:
$$d_{\min}=\min_{x\ne0}\operatorname{weight}(x)$$

#### Example 10.6
> id: ch10-example-10-6 | src: book Example 10.6; p.262 | kind: worked_example

For Table 10.1, each nonzero codeword has two 1s. Therefore, $d_{\min}=2$.

#### Parity-Check Code
> id: ch10-2-1-parity-check-code | src: book 10.2.1; pp.262-264 | kind: concept
The most familiar linear block code is the simple **parity-check code**. In this code, a $k$-bit dataword is augmented by $r = 1$ bit to form an $n$-bit codeword ($n = k + 1$). The extra bit, called the **parity bit**, is selected to make the total number of 1s in the codeword even (for even-parity schemes).

**Table 10.2: Simple parity-check code C(5, 4)**

| Dataword | Codeword | Dataword | Codeword |
|---|---|---|---|
| 0000 | 00000 | 1000 | 10001 |
| 0001 | 00011 | 1001 | 10010 |
| 0010 | 00101 | 1010 | 10100 |
| 0011 | 00110 | 1011 | 10111 |
| 0100 | 01001 | 1100 | 11000 |
| 0101 | 01010 | 1101 | 11011 |
| 0110 | 01100 | 1110 | 11101 |
| 0111 | 01111 | 1111 | 11110 |

Figure 10.4 shows the structure of an encoder and decoder for a simple parity-check code.

> **[ASSET ch10_ill_004]** Figure 10.4: Encoder and decoder for simple parity-check code
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_004.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 7, 'label': 'Figure 10.4'}
> - shows: Figure 10.4: Encoder and decoder for simple parity-check code. A four-bit dataword feeds an even-parity generator; the receiver recomputes a one-bit syndrome and accepts or discards the received dataword.
> - structure: A four-bit dataword feeds an even-parity generator; the receiver recomputes a one-bit syndrome and accepts or discards the received dataword.
> - text_in_image: Sender; Receiver; Dataword; Dataword; Decoder; Encoder; a3 a2 a1 a0; a3 a2 a1 a0; Accept; Discard; Decision; logic; Syndrome; s0; Checker; Generator; Unreliable; Parity bit; transmission; a3 a2 a1 a0 r0; b3 b2 b1 b0 q0; Codeword; Codeword
> - use_when: Teach ch10-2-1, interpret Figure 10.4, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

The calculation is performed in modular arithmetic. The encoder uses a generator that calculates the parity bit $r_0$:
$$r_0 = a_3 + a_2 + a_1 + a_0 \pmod 2$$

The receiver calculates a **syndrome** bit $s_0$:
$$s_0 = b_3 + b_2 + b_1 + b_0 + q_0 \pmod 2$$

If $s_0 = 0$, the received codeword is accepted (no detected error); if $s_0 = 1$, it is discarded. The simple parity-check code has $d_{\text{min}} = 2$, guaranteeing the detection of all single-bit errors. It also detects any odd number of errors.

#### Example 10.7
> id: ch10-example-10-7 | src: book Example 10.7; p.264 | kind: worked_example

Assume dataword `1011` is encoded as `10111`.

1. `10111` arrives unchanged: syndrome 0; dataword `1011` is created.
2. An error changes $a_1$, producing `10011`: syndrome 1; no dataword is created.
3. An error changes parity bit $r_0$, producing `10110`: syndrome 1; no dataword is created.
4. Errors change $r_0$ and $a_3$, producing `00110`: syndrome 0; the incorrect dataword `0011` is created. Two errors cancel in the parity check.
5. Errors change $a_3$, $a_2$, and $a_1$, producing `01011`: syndrome 1; no dataword is created. The parity check detects any odd number of errors.

## 10.3 Cyclic Codes
> id: ch10-3 | src: book 10.3; pp.264-277 | kind: concept

**Cyclic codes** are special linear block codes with one extra property: if a codeword is cyclically shifted (rotated), the resulting word is another codeword. For example, if 1011000 is a codeword and we cyclically shift it to the left, 0110001 is also a codeword.

### 10.3.1 CRC (Cyclic Redundancy Check)
> id: ch10-3-1 | src: book 10.3.1; pp.265-267 | kind: mechanism

A category of cyclic codes called the **cyclic redundancy check (CRC)** is used extensively in networks such as LANs and WANs. Table 10.3 shows an example of a CRC code $C(7, 4)$ with $d_{\text{min}} = 3$.

**Table 10.3: A CRC code with C(7, 4)**

| Dataword | Codeword | Dataword | Codeword |
|---|---|---|---|
| 0000 | 0000000 | 1000 | 1000101 |
| 0001 | 0001011 | 1001 | 1001110 |
| 0010 | 0010110 | 1010 | 1010011 |
| 0011 | 0011101 | 1011 | 1011000 |
| 0100 | 0100111 | 1100 | 1100010 |
| 0101 | 0101100 | 1101 | 1101001 |
| 0110 | 0110001 | 1110 | 1110100 |
| 0111 | 0111010 | 1111 | 1111111 |

Figure 10.5 shows the architecture for the CRC encoder and decoder.

> **[ASSET ch10_ill_005]** Figure 10.5: CRC encoder and decoder
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_005.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 9, 'label': 'Figure 10.5'}
> - shows: Figure 10.5: CRC encoder and decoder. A CRC sender divides an augmented dataword by a shared divisor and appends the remainder; the receiver divides the received codeword and tests the syndrome.
> - structure: A CRC sender divides an augmented dataword by a shared divisor and appends the remainder; the receiver divides the received codeword and tests the syndrome.
> - text_in_image: Sender; Receiver; Dataword; Dataword; Encoder; Decoder; a3 a2 a1 a0; a3 a2 a1 a0; Accept; 0 0 0; Discard; Decision; logic; Syndrome; s2; s1; s0; Divisor; Generator; Checker; d3 d2; d1; d0; Shared; Remainder; Unreliable; transmission; a3 a2 a1 a0 r2 r1 r0; b3 b2 b1 b0; q2 q1 q0; Codeword; Codeword
> - use_when: Teach ch10-3-1, interpret Figure 10.5, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

In the encoder, the dataword has $k$ bits (4 here); the codeword has $n$ bits (7 here). The size of the dataword is augmented by adding $n - k$ zeros to the right. The augmented dataword is divided by a predefined divisor of size $n - k + 1$ (4 bits here: 1011). The remainder of this modulo-2 binary division is the CRC check bits, appended to the dataword to form the codeword.

Figure 10.6 shows the step-by-step division process in the CRC encoder.

> **[ASSET ch10_ill_006]** Figure 10.6: Division in CRC encoder
> - type: illustration
> - kind: matrix_table
> - file: assets/ch10_ill_006.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 10, 'label': 'Figure 10.6'}
> - shows: Figure 10.6: Division in CRC encoder. Modulo-2 long division of augmented dataword 1001000 by divisor 1011 yields remainder 110 and codeword 1001110.
> - structure: Modulo-2 long division of augmented dataword 1001000 by divisor 1011 yields remainder 110 and codeword 1001110.
> - text_in_image: Dataword; 1; 0 0; 1; Encoding; Quotient; Discard; 1; 0 1; 0; Dividend; Divisor; 1; 0 1; 1; 1; 0 0; 1; 0 0 0; 1; 0 1; 1; Note:; Multiply: AND; 0; 1 0; 0; Subtract: XOR; Leftmost bit 0:; 0; 0 0; 0; use 0000 divisor; 1; 0 0; 0; 1; 0 1; 1; 0; 1 1; 0; Leftmost bit 0:; 0; 0 0; 0; use 0000 divisor; 1 1; 0; Remainder; 1; 0 0; 1; 1 1 0; Codeword; Dataword plus remainder
> - use_when: Teach ch10-3-1, interpret Figure 10.6, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

Figure 10.7 shows the division process in the CRC decoder for two cases: an uncorrupted codeword yielding syndrome 000 (accepted), and a corrupted codeword yielding a non-zero syndrome (discarded).

> **[ASSET ch10_ill_007]** Figure 10.7: Division in the CRC decoder for two cases
> - type: illustration
> - kind: matrix_table
> - file: assets/ch10_ill_007.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 11, 'label': 'Figure 10.7'}
> - shows: Figure 10.7: Division in the CRC decoder for two cases. Parallel modulo-2 divisions show an uncorrupted codeword producing syndrome 000 and acceptance, while a corrupted codeword produces syndrome 011 and rejection.
> - structure: Parallel modulo-2 divisions show an uncorrupted codeword producing syndrome 000 and acceptance, while a corrupted codeword produces syndrome 011 and rejection.
> - text_in_image: Uncorrupted; Corrupted; Codeword; Codeword; 1; 0 0; 1; 1 1 0; 1; 0 0; 0; 1 1 0; Decoder; Decoder; 1; 0 1; 0; 1; 0 1; 1; Codeword; Codeword; 1; 0 1; 1; 1; 0 0; 1; 1 1 0; 1; 0 1; 1; 1; 0 0; 0; 1 1 0; 1; 0 1; 1; 1; 0 1; 1; 0; 1 0; 1; 0; 1 1; 1; 0; 0 0; 0; 0; 0 0; 0; 1; 0 1; 1; 1; 1 1; 1; 1; 0 1; 1; 1; 0 1; 1; 0; 0 0; 0; 1; 0 0; 0; 0; 0 0; 0; 1; 0 1; 1; Zero; Non-Zero; Syndrome; Syndrome; 0 0; 0; 0 1; 1; Dataword; Dataword; 1; 0 0; 1; accepted; discarded
> - use_when: Teach ch10-3-1, interpret Figure 10.7, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

### 10.3.2 Polynomials
> id: ch10-3-2 | src: book 10.3.2; pp.267-269 | kind: formula

A pattern of 0s and 1s can be represented as a **polynomial** with coefficients of 0 and 1. The power of each term corresponds to the position of the bit, and the coefficient represents the bit value.

Figure 10.8 shows how a binary word is represented as a polynomial.

> **[ASSET ch10_ill_008]** Figure 10.8: A polynomial to represent a binary word
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_008.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 12, 'label': 'Figure 10.8'}
> - shows: Figure 10.8: A polynomial to represent a binary word. A seven-bit pattern 1000011 is expanded into coefficient-weighted powers and shortened to the polynomial x^6 + x + 1.
> - structure: A seven-bit pattern 1000011 is expanded into coefficient-weighted powers and shortened to the polynomial x^6 + x + 1.
> - text_in_image: a6; a5; a4; a3; a2; a1; a0; 1; 0; 0; 0; 0; 1; 1; 1; 0; 0; 0; 0; 1; 1; + x; +; 1; +; +; +; +; +; x6; +; 1x6; 0x5; 0x4; 0x3; 0x2; 1x1; 1x0; a. Binary pattern and polynomial; b. Short form
> - use_when: Teach ch10-3-2, interpret Figure 10.8, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

The degree of a polynomial is the highest power in the polynomial. For example, the degree of $x^6 + x + 1$ is 6.

Operations on polynomials follow modulo-2 arithmetic:
- **Addition and subtraction:** Both operations are identical and correspond to XORing the coefficients of identical powers.
- **Multiplication:** Accomplished by multiplying each term of one polynomial by each term of the other, summing identical powers modulo 2.
- **Division:** Modulo-2 division follows standard polynomial division, where subtraction of terms is replaced by XOR addition.
- **Shifting:** Shifting a binary pattern $k$ bits to the left corresponds to multiplying the polynomial by $x^k$.

### 10.3.3 Encoder Using Polynomials
> id: ch10-3-3 | src: book 10.3.3; pp.269-270 | kind: algorithm

We can express CRC encoding directly using polynomials. If the dataword is $d(x)$ and the divisor is the **generator polynomial** $g(x)$, the steps are:
1. Multiply the dataword polynomial $d(x)$ by $x^{n-k}$ to shift it by $n - k$ bits: $d(x) x^{n-k}$.
2. Divide $d(x) x^{n-k}$ by $g(x)$ using modulo-2 polynomial division:
   $$\frac{d(x) x^{n-k}}{g(x)} = q(x) + \frac{r(x)}{g(x)}$$
3. Add the remainder polynomial $r(x)$ to the shifted dataword polynomial to obtain the codeword polynomial $c(x)$:
   $$c(x) = d(x) x^{n-k} + r(x)$$

Figure 10.9 shows CRC encoding with polynomial division for dataword $x^3 + 1$ and generator $x^3 + x + 1$.

> **[ASSET ch10_ill_009]** Figure 10.9: CRC division using polynomials
> - type: illustration
> - kind: matrix_table
> - file: assets/ch10_ill_009.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 13, 'label': 'Figure 10.9'}
> - shows: Figure 10.9: CRC division using polynomials. Polynomial division of augmented dataword x^6 + x^3 by generator x^3 + x + 1 yields remainder x^2 + x and codeword x^6 + x^3 + x^2 + x.
> - structure: Polynomial division of augmented dataword x^6 + x^3 by generator x^3 + x + 1 yields remainder x^2 + x and codeword x^6 + x^3 + x^2 + x.
> - text_in_image: Dataword; x3 + 1; +; x; x3; Divisor; Dividend:; +; x6; x3; +; x +; 1; augmented; x3; dataword; +; +; x6; x3; x4; x4; +; +; x4; x2; x; +; x2; x; Remainder; Codeword; +; +; x; x2; x6; x3; Dataword Remainder
> - use_when: Teach ch10-3-3, interpret Figure 10.9, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

### 10.3.4 Analysis of Cyclic Codes
> id: ch10-3-4 | src: book 10.3.4; pp.270-274 | kind: algorithm

Let the sent codeword polynomial be $c(x)$. During transmission, noise adds an **error polynomial** $e(x)$, so the received polynomial is:
$$r(x) = c(x) + e(x)$$

The receiver divides $r(x)$ by $g(x)$. Since $c(x)$ is divisible by $g(x)$, the syndrome polynomial $s(x)$ is simply the remainder of dividing the error polynomial $e(x)$ by $g(x)$:
$$\frac{r(x)}{g(x)} = \frac{c(x)}{g(x)} + \frac{e(x)}{g(x)} \implies s(x) = \text{remainder}\left(\frac{e(x)}{g(x)}\right)$$

> **Book note:** In a cyclic code:
> 1. If $s(x) \ne 0$, one or more bits is corrupted.
> 2. If $s(x) = 0$, either:
>    a. No bit is corrupted, or
>    b. Some bits are corrupted, but the decoder failed to detect them.

An error goes undetected if and only if $e(x)$ is divisible by $g(x)$.

#### Single-Bit Error
> id: ch10-3-4-single-bit-error | src: book 10.3.4; p.271 | kind: concept
A single-bit error at position $i$ is represented by $e(x) = x^i$. If $g(x)$ has more than one term and the lowest term is $x^0 = 1$, then $g(x)$ cannot divide $x^i$, and all single-bit errors are caught.

> **Book note:** If the generator has more than one term and the coefficient of $x^0$ is 1, all single-bit errors can be caught.

#### Example 10.8
> id: ch10-example-10-8 | src: book Example 10.8; p.271 | kind: worked_example

Which generators guarantee detection of every single-bit error?

**a.** $g(x)=x+1$: every $x^i$ division leaves a remainder, so all single-bit errors are caught.

**b.** $g(x)=x^3$: an error at position $i\ge3$ is divisible by the generator and is missed; only positions below 3 are caught.

**c.** $g(x)=1$: every $x^i$ is divisible by the generator, so no single-bit error is caught; the generator is useless.

#### Two Isolated Single-Bit Errors
> id: ch10-3-4-two-isolated-single-bit-errors | src: book 10.3.4; pp.271-272 | kind: concept
Two isolated single-bit errors at positions $i$ and $j$ ($j > i$) are represented by:
$$e(x) = x^j + x^i = x^i (x^{j-i} + 1)$$

Figure 10.10 shows the representation of two isolated single-bit errors using polynomials.

> **[ASSET ch10_ill_010]** Figure 10.10: Representation of two isolated single-bit errors using polynomials
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_010.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 15, 'label': 'Figure 10.10'}
> - shows: Figure 10.10: Representation of two isolated single-bit errors using polynomials. A codeword axis marks two isolated errors at powers x^i and x^j; their separation is j minus i.
> - structure: A codeword axis marks two isolated errors at powers x^i and x^j; their separation is j minus i.
> - text_in_image: Difference: j – i; 0; 1; 0; 1; 1; 1; 0; 1; 0; 1; 0; 0; 0; 0; 1; 1; x0; xn–1; xj; xi
> - use_when: Teach ch10-3-4-two-isolated-single-bit-errors, interpret Figure 10.10, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

> **Book note:** If a generator cannot divide $x^t + 1$ ($t$ between 0 and $n - 1$), then all isolated double errors can be detected.

#### Example 10.9
> id: ch10-example-10-9 | src: book Example 10.9; p.272 | kind: worked_example

Assess the generators for two isolated single-bit errors.

**a.** $x+1$ misses any two adjacent errors.

**b.** $x^4+1$ misses two errors four positions apart.

**c.** $x^7+x^6+1$ is a good choice for this purpose.

**d.** $x^{15}+x^{14}+1$ detects two isolated errors separated by any distance below 32,768 bits.

#### Odd Numbers of Errors
> id: ch10-3-4-odd-numbers-of-errors | src: book 10.3.4; p.272 | kind: concept
> **Book note:** A generator that contains a factor of $x + 1$ can detect all odd-numbered errors.

Any polynomial with an odd number of terms has $e(1) = 1$. If $g(x)$ contains $x + 1$ as a factor, then $g(1) = 0$. Since zero cannot divide a non-zero value, $g(x)$ cannot divide $e(x)$, and all odd numbers of errors are detected.

#### Burst Errors
> id: ch10-3-4-burst-errors | src: book 10.3.4; pp.272-273 | kind: formula
A burst error of length $L$ can be written as $e(x) = x^i b(x)$, where $b(x)$ has degree $L - 1$.
> **Book note:**
> - All burst errors with $L \le r$ will be detected.
> - All burst errors with $L = r + 1$ will be detected with probability $1 - (1/2)^{r-1}$.
> - All burst errors with $L > r + 1$ will be detected with probability $1 - (1/2)^r$.

#### Example 10.10
> id: ch10-example-10-10 | src: book Example 10.10; p.273 | kind: worked_example

Compare three generators for burst-error detection.

**a.** $x^6+1$ detects every burst of length at most 6; about 3 in 100 length-7 bursts and 16 in 1000 bursts of length 8 or more are missed.

**b.** $x^{18}+x^7+x+1$ detects every burst of length at most 18; about 8 in one million length-19 bursts and 4 in one million bursts of length 20 or more are missed.

**c.** $x^{32}+x^{23}+x^7+1$ detects every burst of length at most 32; about 5 in ten billion length-33 bursts and 3 in ten billion bursts of length 34 or more are missed.

> **Book note:** A good polynomial generator

> **Book note:** A good polynomial generator needs to have the following characteristics:
> 1. It should have at least two terms.
> 2. The coefficient of the term $x^0$ should be 1.
> 3. It should not divide $x^t+1$ for $2\le t\le n-1$.
> 4. It should have the factor $x + 1$.

### 10.3.5 Advantages of Cyclic Codes
> id: ch10-3-5 | src: book 10.3.5; p.274 | kind: concept

Cyclic codes possess excellent performance in detecting single-bit errors, double errors, an odd number of errors, and burst errors. They can easily be implemented in hardware and software, and hardware implementations are extremely fast.

### 10.3.6 Other Cyclic Codes
> id: ch10-3-6 | src: book 10.3.6; pp.274-275 | kind: standard

Standard polynomials defined by international bodies are used in networking standards. Table 10.4 lists some of the most common standard polynomials.

**Table 10.4: Standard polynomials**

| Name | Polynomial | Bit Pattern | Used in |
|---|---|---|---|
| CRC-8 | $x^8 + x^2 + x + 1$ | `100000111` | ATM header |
| CRC-10 | $x^{10} + x^9 + x^5 + x^4 + x^2 + 1$ | `11000110101` | ATM AAL |
| CRC-16 | $x^{16} + x^{12} + x^5 + 1$ | `10001000000100001` | HDLC |
| CRC-32 | $x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1$ | `100000100110000010001110110110111` | LANs |

More advanced cyclic codes based on Galois fields include the Reed-Solomon codes used for both detection and correction.

### 10.3.7 Hardware Implementation
> id: ch10-3-7 | src: book 10.3.7; pp.275-277 | kind: mechanism

Cyclic codes can be implemented in hardware using shift registers and XOR gates.

Figure 10.11 shows the hardwired design of the divisor.

> **[ASSET ch10_ill_011]** Figure 10.11: Hardwired design of the divisor in CRC
> - type: illustration
> - kind: switch_fabric
> - file: assets/ch10_ill_011.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 19, 'label': 'Figure 10.11'}
> - shows: Figure 10.11: Hardwired design of the divisor in CRC. The fixed CRC divisor is represented as hardwired XOR inputs d2, d1, and d0, with the always-zero leading result omitted.
> - structure: The fixed CRC divisor is represented as hardwired XOR inputs d2, d1, and d0, with the always-zero leading result omitted.
> - text_in_image: Leftmost bit of the part; of the dividend involved; in XOR operation; d2; d1; d0; Broken line:; +; +; +; this bit is always 0; XOR; XOR; XOR
> - use_when: Teach ch10-3-7, interpret Figure 10.11, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

Figure 10.12 simulates the step-by-step division process using a hand-calculator style circuit across 7 time ticks.

> **[ASSET ch10_ill_012]** Figure 10.12: Simulation of division in CRC encoder
> - type: illustration
> - kind: matrix_table
> - file: assets/ch10_ill_012.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 20, 'label': 'Figure 10.12'}
> - shows: Figure 10.12: Simulation of division in CRC encoder. Seven clock snapshots trace CRC encoder register contents and XOR operations from augmented dataword input to the final three-bit remainder.
> - structure: Seven clock snapshots trace CRC encoder register contents and XOR operations from augmented dataword input to the final three-bit remainder.
> - text_in_image: Augmented dataword; 0; 0; 0; +; +; +; Time: 1; 0; 0; 1; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; +; +; +; Time: 2; 0; 1; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; +; +; +; Time: 3; 1; 0; 0; 1; 0; 0; 0; 0; 0; 1; 1; +; +; +; Time: 4; 0; 0; 1; 0; 0; 0; 1; 0; 0; 0; +; +; +; Time: 5; 0; 1; 1; 0; 0; 0; 0; 0; 0; 0; 1; 1; +; +; +; Time: 6; 1; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; +; +; +; 0; 1; Time: 7; 1; 1; 1; 0; 0; 1; 1; 0; Final remainder
> - use_when: Teach ch10-3-7, interpret Figure 10.12, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

Figure 10.13 shows the simplified encoder design using shift registers.

> **[ASSET ch10_ill_013]** Figure 10.13: The CRC encoder design using shift registers
> - type: illustration
> - kind: switch_fabric
> - file: assets/ch10_ill_013.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 21, 'label': 'Figure 10.13'}
> - shows: Figure 10.13: The CRC encoder design using shift registers. Three shift registers and two XOR taps implement the example CRC encoder for augmented dataword 1001000.
> - structure: Three shift registers and two XOR taps implement the example CRC encoder for augmented dataword 1001000.
> - text_in_image: Augmented dataword; +; +; 0; 0; 0; 1; 0; 0; 1; 0; 0; 0
> - use_when: Teach ch10-3-7, interpret Figure 10.13, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

Figure 10.14 shows the general architecture for an encoder and decoder with an arbitrary polynomial $g(x) = x^r + d_{r-1} x^{r-1} + \dots + d_1 x + 1$.

> **[ASSET ch10_ill_014]** Figure 10.14: General design of encoder and decoder of a CRC code
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_014.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 21, 'label': 'Figure 10.14'}
> - shows: Figure 10.14: General design of encoder and decoder of a CRC code. General r-stage shift-register diagrams show CRC encoding and syndrome calculation, with XOR taps present only for nonzero generator coefficients.
> - structure: General r-stage shift-register diagrams show CRC encoding and syndrome calculation, with XOR taps present only for nonzero generator coefficients.
> - text_in_image: d0; d1; dn–k–1; +; +; +; • • •; Dataword; rn–k–1; r1; r0; Note:; a. Encoder; The divisor line and XOR are; missing if the corresponding; bit in the divisor is 0.; d0; dn–k–1; d1; Received; +; +; +; • • •; codeword; sn–k–1; s1; s0; b. Decoder
> - use_when: Teach ch10-3-7, interpret Figure 10.14, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

## 10.4 Checksum
> id: ch10-4 | src: book 10.4; pp.277-282 | kind: concept

The **checksum** is an error-detecting technique applied primarily at the transport and network layers. Like linear block codes, it relies on redundancy.

### 10.4.1 Concept
> id: ch10-4-1 | src: book 10.4.1; pp.277-280 | kind: algorithm

The checksum uses one's complement arithmetic. In $n$-bit one's complement arithmetic, an unsigned number can range between 0 and $2^n - 1$. When adding numbers, any carry bit that goes beyond $n$ bits is wrapped around and added to the least significant bit.

#### Example 10.11
> id: ch10-example-10-11 | src: book Example 10.11; p.278 | kind: worked_example

A message contains five 4-bit numbers: $(7,11,12,0,6)$. Sending their ordinary sum would produce $(7,11,12,0,6,36)$. The receiver recomputes the sum and compares it with 36; a match is treated as no error. The drawback is that 36 needs six bits while each data item needs only four.

In $m$-bit one's-complement arithmetic, a value above $2^m-1$ is wrapped by adding its extra high-order bits to its $m$ low-order bits.

Figure 10.15 shows

Figure 10.15 shows the checksum concept at the sender and receiver.

> **[ASSET ch10_ill_015]** Figure 10.15: Checksum
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_015.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 22, 'label': 'Figure 10.15'}
> - shows: Figure 10.15: Checksum. Checksum generation appends an m-bit checksum to a message; the receiver recomputes the checksum and accepts only an all-zero result.
> - structure: Checksum generation appends an m-bit checksum to a message; the receiver recomputes the checksum and accepts only an all-zero result.
> - text_in_image: Sender; Receiver; Message; Message; m bits; m bits; m bits; m bits; m bits; m bits; All 0’s; [yes]; Discard; m bits; [no]; Generator; Checker; m bits; m bits; m bits; m bits; m bits; m bits; m bits; m bits; Message plus checksum; Message plus checksum
> - use_when: Teach ch10-4-1, interpret Figure 10.15, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

#### Example 10.12
> id: ch10-example-10-12 | src: book Example 10.12; p.279 | kind: worked_example

The ordinary sum 36 is $(100100)_2$. For a 4-bit sum, wrap the high bits into the low four bits: $(10)_2+(0100)_2=(0110)_2=6$. The sender can therefore send $(7,11,12,0,6,6)$, and the receiver accepts only when its one's-complement sum of the first five values is also 6.

#### Example 10.13
> id: ch10-example-10-13 | src: book Example 10.13; p.279 | kind: worked_example

Using Example 10.12, the sender obtains the wrapped sum 6 and complements it to form checksum $15-6=9$; `0110` and `1001` are complements. It sends $(7,11,12,0,6,9)$. With no corruption, the receiver's one's-complement sum is 15 and its complement is 0, so the data are accepted. Figure 10.16 traces the calculation.

> **[ASSET ch10_ill_016]** Figure 10.16: Example 10.13
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_016.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 23, 'label': 'Figure 10.16'}
> - shows: Figure 10.16: Example 10.13. Example 10.13 traces data values 7, 11, 12, 0, and 6: the sender produces checksum 9 and the receiver obtains calculated checksum 0.
> - structure: Example 10.13 traces data values 7, 11, 12, 0, and 6: the sender produces checksum 9 and the receiver obtains calculated checksum 0.
> - text_in_image: Sender; Receiver; 7; 7; 11; 11; 12; 12; 0; 0; 6; 6; 7, 11, 12, 0, 6, 9; Initialized checksum; Received Checksum; 0; 9; Packet; Sum (in one’s complement); Sum (in one’s complement); 6; 15; Actual checksum; Calculated Checksum; 9; 0
> - use_when: Teach ch10-4-1, interpret Figure 10.16, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

#### Internet Checksum
> id: ch10-4-1-internet-checksum | src: book 10.4.1; p.280 | kind: algorithm
Traditionally, the Internet has used a 16-bit checksum. The sender and receiver follow the five steps listed in Table 10.5.

**Table 10.5: Procedure to calculate the traditional checksum**

| Step | Sender | Receiver |
|---|---|---|
| 1 | The message is divided into 16-bit words. | The message and the checksum are received. |
| 2 | The value of the checksum word is initially set to zero. | The message is divided into 16-bit words. |
| 3 | All words are added using one's complement addition. | All words including the checksum are added using one's complement addition. |
| 4 | The sum is complemented and becomes the checksum. | The sum is complemented and becomes the new checksum. |
| 5 | The checksum is sent with the data. | If the value of the checksum is 0, the message is accepted; otherwise, it is rejected. |

Figure 10.17 shows the flowchart for the traditional checksum algorithm.

> **[ASSET ch10_ill_017]** Figure 10.17: Algorithm to calculate a traditional checksum
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_017.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 24, 'label': 'Figure 10.17'}
> - shows: Figure 10.17: Algorithm to calculate a traditional checksum. A flowchart accumulates 16-bit words, repeatedly folds a nonzero upper half into the lower half, complements the sum, and truncates to 16 bits.
> - structure: A flowchart accumulates 16-bit words, repeatedly folds a nonzero upper half into the lower half, complements the sum, and truncates to 16 bits.
> - text_in_image: Start; Sum =  0; More words?; [yes]; Sum = Sum + Next Word; [no]; Left(sum); is nonzero?; [yes]; Sum = Left(Sum) + Right(Sum); [no]; Notes:; a. Word and Checksum are each; Checksum = Complement (Sum); ; 16 bits, but Sum is 32 bits.; b. Left(Sum) can be found by shifting; ; Sum 16 bits to the right.; Checksum = truncate (Checksum); c. Right(Sum) can be found by; ; ANDing Sum with (0000FFFF)16 .; d. After Checksum is found, truncate; Stop; ; it to 16 bits.
> - use_when: Teach ch10-4-1, interpret Figure 10.17, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

### 10.4.2 Other Approaches to the Checksum
> id: ch10-4-2 | src: book 10.4.2; pp.280-282 | kind: algorithm

The traditional checksum has a weakness: if two words are swapped, or if one word is incremented while another is decremented by the same amount, the sum remains unchanged and the error is undetected. Alternative algorithms use weighted sums to preserve position information.

#### Fletcher Checksum
> id: ch10-4-2-fletcher-checksum | src: book 10.4.2; pp.281-282 | kind: algorithm
The **Fletcher checksum** computes two running sums ($L$ and $R$). Figure 10.18 shows the algorithm for an 8-bit Fletcher checksum over data octets producing a 16-bit checksum.

> **[ASSET ch10_ill_018]** Figure 10.18: Algorithm to calculate an 8-bit Fletcher checksum
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_018.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 26, 'label': 'Figure 10.18'}
> - shows: Figure 10.18: Algorithm to calculate an 8-bit Fletcher checksum. The Fletcher flowchart initializes L and R to zero, updates R then L modulo 256 for every octet, and concatenates them as a 16-bit checksum.
> - structure: The Fletcher flowchart initializes L and R to zero, updates R then L modulo 256 for every octet, and concatenates them as a 16-bit checksum.
> - text_in_image: Notes; Start; L : Left 8-bit checksum; R : Right 8-bit checksum; R = L = 0; Di: Next 8-bit data item; More data?; [yes]; R = (R + Di) mod 256; L = (L + R) mod 256; [no]; 16-bit; Checksum = L × 256 + R; R; L; checksum; Stop
> - use_when: Teach ch10-4-2, interpret Figure 10.18, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

#### Adler Checksum
> id: ch10-4-2-adler-checksum | src: book 10.4.2; p.282 | kind: algorithm
The **Adler-32 checksum** is a 32-bit checksum. It calculates two 16-bit sums modulo 65521 (the largest prime smaller than $2^{16}$). Figure 10.19 shows the algorithm.

> **[ASSET ch10_ill_019]** Figure 10.19: Algorithm to calculate an Adler checksum
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_019.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 26, 'label': 'Figure 10.19'}
> - shows: Figure 10.19: Algorithm to calculate an Adler checksum. The Adler flowchart initializes L to zero and R to one, updates R then L modulo 65,521 for every 16-bit item, and forms a 32-bit checksum.
> - structure: The Adler flowchart initializes L to zero and R to one, updates R then L modulo 65,521 for every 16-bit item, and forms a 32-bit checksum.
> - text_in_image: Start; Notes; L : Left 16-bit checksum; R : Right 16-bit checksum; R = 1    L = 0; Di: Next 16-bit data item; More data?; [yes]; R = (R + Di) mod 65,521; L = (L + R) mod 65,521; [no]; R; L; Checksum = L × 65,536 + R; 32-bit checksum; Stop
> - use_when: Teach ch10-4-2, interpret Figure 10.19, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

## 10.5 Forward Error Correction
> id: ch10-5 | src: book 10.5; pp.282-285 | kind: concept

**Forward Error Correction (FEC)** is a technique in which the receiver detects and automatically corrects transmission errors without requesting retransmission. FEC is essential in real-time applications (such as audio and video) or on simplex/deep-space channels where retransmission delay is unacceptable.

### 10.5.1 Using Hamming Distance
> id: ch10-5-1 | src: book 10.5.1; pp.282-283 | kind: mechanism

To guarantee the correction of up to $t$ errors, the minimum Hamming distance in a block code must satisfy:
$$d_{\text{min}} \ge 2t + 1$$

Figure 10.20 illustrates the geometric concept for error correction.

> **[ASSET ch10_ill_020]** Figure 10.20: Hamming distance for error correction
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_020.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 27, 'label': 'Figure 10.20'}
> - shows: Figure 10.20: Hamming distance for error correction. Disjoint radius-t territories around valid codewords x and y illustrate that their minimum distance must exceed 2t for unambiguous correction.
> - structure: Disjoint radius-t territories around valid codewords x and y illustrate that their minimum distance must exceed 2t for unambiguous correction.
> - text_in_image: Territory of y; Territory of x; Legend; y; Radius t; Radius t; Any valid codeword; x; Any corrupted codeword; with 1 to t errors; dmin > 2t
> - use_when: Teach ch10-5-1, interpret Figure 10.20, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

### 10.5.2 Using XOR
> id: ch10-5-2 | src: book 10.5.2; pp.283-284 | kind: mechanism

A simple FEC scheme adds a parity packet to a group of $N$ data packets. The parity packet $P$ is formed by XORing all $N$ data packets:
$$P = D_1 \oplus D_2 \oplus \dots \oplus D_N$$

If any one packet $D_i$ is lost, the receiver reconstructs it by XORing the remaining $N - 1$ packets and $P$:
$$D_i = D_1 \oplus \dots \oplus D_{i-1} \oplus D_{i+1} \oplus \dots \oplus D_N \oplus P$$

This scheme recovers from any single packet loss in the group.

### 10.5.3 Chunk Interleaving
> id: ch10-5-3 | src: book 10.5.3; p.284 | kind: mechanism

Burst errors often corrupt consecutive bytes or packets. In **chunk interleaving**, a message is organized into a matrix of rows and columns. Packets are loaded row by row but transmitted column by column.

Figure 10.21 shows how interleaving disperses errors across different packets.

> **[ASSET ch10_ill_021]** Figure 10.21: Interleaving
> - type: illustration
> - kind: architecture_block
> - file: assets/ch10_ill_021.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 28, 'label': 'Figure 10.21'}
> - shows: Figure 10.21: Interleaving. Five packets are filled row-wise with numbered chunks, transmitted column-wise, lose one packet, and are rebuilt with one missing chunk per reconstructed packet.
> - structure: Five packets are filled row-wise with numbered chunks, transmitted column-wise, lose one packet, and are rebuilt with one missing chunk per reconstructed packet.
> - text_in_image: 05; 04; 02; 01; 05; 04; 03; 02; 01; Packet 1; Packet 1; column by column; column by column; 10; 09; 07; 06; 10; 09; 08; 07; 06; Packet 2; Packet 2; Receiving; Sending; 15; 14; 12; 11; 15; 14; 13; 12; 11; Packet 3; Packet 3; 20; 19; 17; 16; 20; 19; 18; 17; 16; Packet 4; Packet 4; 25; 24; 22; 21; Packet 5; 25; 24; 23; 22; 21; Packet 5; a. Packet creation at sender; d. Packet recreation at receiver; Packet 5; Packet 4; Packet 3; Packet 2; Packet 1; 25; 20; 15; 10; 05; 24; 19; 14; 09; 04; 23; 18; 13; 08; 03; 22; 17; 12; 07; 02; 21; 16; 11; 06; 01; b. Packets sent; 25; 20; 15; 10; 05; 24; 19; 14; 09; 04; 22; 17; 12; 07; 02; 21; 16; 11; 06; 01; Lost; Packet 5; Packet 4; Packet 3; Packet 2; Packet 1; c. Packets received
> - use_when: Teach ch10-5-3, interpret Figure 10.21, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

### 10.5.4 Combining Hamming Distance and Interleaving
> id: ch10-5-4 | src: book 10.5.4; pp.284-285 | kind: mechanism

Hamming distance block coding and chunk interleaving can be combined into a two-dimensional error-correction scheme. Bytes are placed in a two-dimensional grid; parity or Hamming check bits are computed across both rows and columns. When a burst error occurs during transmission, column de-interleaving transforms the burst into isolated single-bit errors across different rows, which are corrected by the row codes.

### 10.5.5 Compounding High- and Low-Resolution Packets
> id: ch10-5-5 | src: book 10.5.5; p.285 | kind: mechanism

In multimedia streaming, another approach to FEC compounds high-resolution and low-resolution versions of data. Figure 10.22 shows this approach.

> **[ASSET ch10_ill_022]** Figure 10.22: Compounding high- and low-resolution packets
> - type: illustration
> - kind: flow
> - file: assets/ch10_ill_022.png
> - src: {'role': 'book', 'file': 'Slide/ch_10/ch10.pdf', 'page': 29, 'label': 'Figure 10.22'}
> - shows: Figure 10.22: Compounding high- and low-resolution packets. High-resolution packets are paired with the preceding packet’s low-resolution copy so one lost compound packet can be replaced at lower quality.
> - structure: High-resolution packets are paired with the preceding packet’s low-resolution copy so one lost compound packet can be replaced at lower quality.
> - text_in_image: Legend; High-resolution packet; Compound packet; Low-resolution packet; Empty packet; Creation of; P1-High; P2-High; P3-High; P4-High; P5-High; packets; Sending of; compound; P1-High; P1-L P2-High; P2-L P3-High; P3-L; P4-High; P4-L P5-High; packets; Packet 1; Packet 2; Packet 3; Packet 4; Packet 5; Packet 1; Packet 2; Packet 3; Packet 4; Packet 5; Receiving of; compound; P2-L P3-High; P1-High; P3-L P4-High; P4-L P5-High; Lost; packets; Recreation; P1-High; P2-L; P3-High; P4-High; P5-High; of packets
> - use_when: Teach ch10-5-5, interpret Figure 10.22, trace its calculation or data path, or solve a linked practice question.
> - confidence: high

## Chapter Summary
> id: ch10-summary | src: book 10.6.3; pp.286-287 | kind: summary

- Errors can be categorized as a single-bit error or a burst error. A single-bit error has only 1 bit corrupted; a burst error has 2 or more bits corrupted.
- Redundancy is the central concept in detecting or correcting errors. Extra bits are added to the data at the sender and checked at the receiver.
- In error detection, we are only interested in knowing whether any error has occurred. In error correction, we need to know the number of errors and their exact locations in the message.
- Forward error correction (FEC) is the process in which the receiver tries to guess the message by using redundant bits.
- In block coding, we divide our message into blocks of $k$ bits, called datawords. We add $r$ redundant bits to each block to make the length $n = k + r$. The resulting $n$-bit blocks are called codewords.
- The Hamming distance between two words of the same size is the number of differences between the corresponding bits.
- The minimum Hamming distance ($d_{\text{min}}$) is the smallest Hamming distance between all possible pairs in a set of words.
- To guarantee the detection of up to $s$ errors in all cases, the minimum Hamming distance in a block code must be $d_{\text{min}} = s + 1$.
- To guarantee correction of up to $t$ errors in all cases, the minimum Hamming distance in a block code must be $d_{\text{min}} = 2t + 1$.
- In a linear block code, the exclusive-OR (addition modulo-2) of two valid codewords creates another valid codeword.
- The most familiar linear block code is the simple parity-check code, which can detect all single-bit errors and any odd number of errors ($d_{\text{min}} = 2$).
- Cyclic codes are special linear block codes where a cyclic shift of a valid codeword produces another valid codeword.
- The cyclic redundancy check (CRC) is a popular cyclic code that can be analyzed using polynomials and implemented using shift registers.
- A good polynomial generator has at least two terms, an $x^0 = 1$ term, and contains $x + 1$ as a factor.
- A checksum is an error-detection technique based on one's complement addition of data words.
- Alternative checksum algorithms, such as Fletcher and Adler, use weighted sums to preserve position information.
