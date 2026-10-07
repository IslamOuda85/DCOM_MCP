---
doc_type: scientific_content
course_id: data_communications
chapter: 4
chapter_id: data_communications_ch04
chapter_title: Digital Transmission
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_4/ch4.pdf
  pages: 95-134
assets_dir: assets
asset_counts:
  illustration: 36
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:03:01+00:00'
status: complete
---
# Chapter 4: Digital Transmission

## Chapter Objectives
> id: ch04-0 | src: book p.95 | kind: objectives

Acomputer network is designed to send information from one point to another. This
information needs to be converted to either a digital signal or an analog signal for
transmission. In this chapter, we discuss the first choice, conversion to digital signals;
in Chapter 5, we discuss the second choice, conversion to analog signals.
We discussed the advantages and disadvantages of digital transmission over analog
transmission in Chapter 3. In this chapter, we show the schemes and techniques that
we use to transmit data digitally. First, we discuss digital-to-digital conversion techniques, methods which convert digital data to digital signals. Second, we discuss analogto-digital conversion techniques, methods which change an analog signal to a digital
signal. Finally, we discuss transmission modes. We have divided this chapter into three
sections:

- The first section discusses digital-to-digital conversion. Line coding is used to convert digital data to a digital signal. Several common schemes are discussed. The
section also describes block coding, which is used to create redundancy in the digital data before they are encoded as a digital signal. Redundancy is used as an
inherent error detecting tool. The last topic in this section discusses scrambling, a
technique used for digital-to-digital conversion in long-distance transmission.

- The second section discusses analog-to-digital conversion. Pulse code modulation
is described as the main method used to sample an analog signal. Delta modulation
is used to improve the efficiency of the pulse code modulation.

- The third section discusses transmission modes. When we want to transmit data
digitally, we need to think about parallel or serial transmission. In parallel transmission, we send multiple bits at a time; in serial transmission, we send one bit at a
time.

## 4.1 DIGITAL-TO-DIGITAL CONVERSION
> id: ch04-4-1 | src: book 4.1; p.96 | kind: concept

In Chapter 3, we discussed data and signals. We said that data can be either digital or
analog. We also said that signals that represent data can also be digital or analog. In this
section, we see how we can represent digital data by using digital signals. The conversion involves three techniques: line coding, block coding, and scrambling. Line coding
is always needed; block coding and scrambling may or may not be needed.

### 4.1.1 Line Coding
> id: ch04-4-1-1 | src: book 4.1.1; p.96 | kind: concept

Line coding is the process of converting digital data to digital signals. We assume that
data, in the form of text, numbers, graphical images, audio, or video, are stored in computer memory as sequences of bits (see Chapter 1). Line coding converts a sequence of
bits to a digital signal. At the sender, digital data are encoded into a digital signal; at the
receiver, the digital data are recreated by decoding the digital signal. Figure 4.1 shows
the process.

> **[ASSET ch04_ill_001]** Figure 4.1: Line coding and decoding
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_001.png
> - src: book Figure 4.1; p.96
> - shows: Figure 4.1: Line coding and decoding. Digital bits enter an encoder, cross a link as a digital waveform, and enter a decoder that recovers the same digital bits. Sender and receiver blocks mark the endpoints.
> - structure: Digital bits enter an encoder, cross a link as a digital waveform, and enter a decoder that recovers the same digital bits. Sender and receiver blocks mark the endpoints.
> - text_in_image: Sender; Receiver; Digital data; Digital data; Digital signal; 0 1 0 1  …  1 0 1; 0 1 0 1  …  1 0 1; • • •; Link; Encoder; Decoder
> - use_when: Teach ch04-4-1-1, interpret Figure 4.1, or solve a linked practice question.
> - confidence: high

#### Characteristics
> id: ch04-4-1-1-characteristics | src: book p.96 | kind: concept

Before discussing different line coding schemes, we address their common characteristics.

#### Signal Element Versus Data Element
> id: ch04-4-1-1-signal-element-versus-data-element | src: book p.96 | kind: concept

Let us distinguish between a data element and a signal element. In data communications, our goal is to send data elements. A data element is the smallest entity that can
represent a piece of information: this is the bit. In digital data communications, a signal
element carries data elements. A signal element is the shortest unit (timewise) of a digital signal. In other words, data elements are what we need to send; signal elements are
what we can send. Data elements are being carried; signal elements are the carriers.
We define a ratio r which is the number of data elements carried by each signal element. Figure 4.2 shows several situations with different values of r.
In part a of the figure, one data element is carried by one signal element (r = 1). In
part b of the figure, we need two signal elements (two transitions) to carry each data
element ($r=1/2$). We will see later that the extra signal element is needed to guarantee
synchronization. In part c of the figure, a signal element carries two data elements (r = 2).

> **[ASSET ch04_ill_002]** Figure 4.2: Signal element versus data element
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_002.png
> - src: book Figure 4.2; p.97
> - shows: Figure 4.2: Signal element versus data element. Four panels compare the ratio r of data elements to signal elements: one-to-one, one data element over two signal elements, two data elements in one signal element, and four data elements over three signal elements.
> - structure: Four panels compare the ratio r of data elements to signal elements: one-to-one, one data element over two signal elements, two data elements in one signal element, and four data elements over three signal elements.
> - text_in_image: 1 data element; 1 data element; 1; 0; 1; 1; 0; 1; 1 signal; 2 signal; element; elements; a. One data element per one signal; b. One data element per two signal; elements   r =   1; element (r = 1); 2; 2 data elements; 4 data elements; 11; 01; 11; 1101; 1 signal; 3 signal; element; elements; c. Two data elements per one signal; d. Four data elements per three signal; elements   r = 4; element (r = 2); 3
> - use_when: Teach ch04-4-1-1-signal-element-versus-data-element, interpret Figure 4.2, or solve a linked practice question.
> - confidence: high

Finally, in part d, a group of 4 bits is being carried by a group of three signal elements
(r = 4/3). For every line coding scheme we discuss, we will give the value of r.
An analogy may help here. Suppose each data element is a person who needs to be
carried from one place to another. We can think of a signal element as a vehicle that can
carry people. When r = 1, it means each person is driving a vehicle. When r > 1, it
means more than one person is travelling in a vehicle (a carpool, for example). We can
also have the case where one person is driving a car and a trailer (r = 1/2).

#### Data Rate Versus Signal Rate
> id: ch04-4-1-1-data-rate-versus-signal-rate | src: book p.97 | kind: concept

The data rate defines the number of data elements (bits) sent in 1s. The unit is bits per
second (bps). The signal rate is the number of signal elements sent in 1s. The unit is
the baud. There are several common terminologies used in the literature. The data rate
is sometimes called the bit rate; the signal rate is sometimes called the pulse rate, the
modulation rate, or the baud rate.
One goal in data communications is to increase the data rate while decreasing the
signal rate. Increasing the data rate increases the speed of transmission; decreasing the
signal rate decreases the bandwidth requirement. In our vehicle-people analogy, we
need to carry more people in fewer vehicles to prevent traffic jams. We have a limited
bandwidth in our transportation system.
We now need to consider the relationship between data rate (N) and signal rate (S)

$$S = \frac{N}{r}$$

in which r has been previously defined. This relationship, of course, depends on the
value of r. It also depends on the data pattern. If we have a data pattern of all 1s or all
0s, the signal rate may be different from a data pattern of alternating 0s and 1s. To
derive a formula for the relationship, we need to define three cases: the worst, best, and
average. The worst case is when we need the maximum signal rate; the best case is
when we need the minimum. In data communications, we are usually interested in the
average case. We can formulate the relationship between data rate and signal rate as

$$S_{\mathrm{ave}} = cN\left(\frac{1}{r}\right)\ \text{baud}$$
baud

where N is the data rate (bps); c is the case factor, which varies for each case; S is the
number of signal elements per second; and r is the previously defined factor.

##### Example 4.1
> id: ch04-example-4-1 | src: book Example 4.1 | kind: worked_example
A signal is carrying data in which one data element is encoded as one signal element (r = 1). If
the bit rate is 100 kbps, what is the average value of the baud rate if c is between 0 and 1?

**Solution**
We assume that the average value of c is 1/2. The baud rate is then

$$S = cN\left(\frac{1}{r}\right)=\frac{1}{2}(100{,}000)(1)=50{,}000\ \text{baud}=50\ \text{kbaud}$$

#### Bandwidth
> id: ch04-4-1-1-bandwidth | src: book p.98 | kind: concept

We discussed in Chapter 3 that a digital signal that carries information is nonperiodic.
We also showed that the bandwidth of a nonperiodic signal is continuous with an infinite range. However, most digital signals we encounter in real life have a bandwidth
with finite values. In other words, the bandwidth is theoretically infinite, but many of
the components have such a small amplitude that they can be ignored. The effective
bandwidth is finite. From now on, when we talk about the bandwidth of a digital signal,
we need to remember that we are talking about this effective bandwidth.

Although the actual bandwidth of a digital signal is infinite,
the effective bandwidth is finite.

We can say that the baud rate, not the bit rate, determines the required bandwidth
for a digital signal. If we use the transportation analogy, the number of vehicles, not the
number of people being carried, affects the traffic. More changes in the signal mean
injecting more frequencies into the signal. (Recall that frequency means change and
change means frequency.) The bandwidth reflects the range of frequencies we need.
There is a relationship between the baud rate (signal rate) and the bandwidth. Bandwidth is a complex idea. When we talk about the bandwidth, we normally define a
range of frequencies. We need to know where this range is located as well as the values
of the lowest and the highest frequencies. In addition, the amplitude (if not the phase)
of each component is an important issue. In other words, we need more information
about the bandwidth than just its value; we need a diagram of the bandwidth. We will
show the bandwidth for most schemes we discuss in the chapter. For the moment, we
can say that the bandwidth (range of frequencies) is proportional to the signal rate
(baud rate). The minimum bandwidth can be given as

$$B_{\min} = cN\left(\frac{1}{r}\right)$$
We can solve for the maximum data rate if the bandwidth of the channel is given.

$$N_{\max} = \frac{1}{c}Br$$

##### Example 4.2
> id: ch04-example-4-2 | src: book Example 4.2 | kind: worked_example
The maximum data rate of a channel (see Chapter 3) is Nmax = 2 × B × log2 L (defined by the
Nyquist formula). Does this agree with the previous formula for $N_{max}$?

**Solution**
A signal with L levels actually can carry log2 L bits per level. If each level corresponds to one signal element and we assume the average case (c = 1/2), then we have
$$N_{\max} = \frac{1}{c}Br = 2B\log_2 L$$

#### Baseline Wandering
> id: ch04-4-1-1-baseline-wandering | src: book p.99 | kind: concept

In decoding a digital signal, the receiver calculates a running average of the received
signal power. This average is called the baseline. The incoming signal power is evaluated
against this baseline to determine the value of the data element. A long string of 0s or 1s
can cause a drift in the baseline (baseline wandering) and make it difficult for the receiver
to decode correctly. A good line coding scheme needs to prevent baseline wandering.

#### DC Components
> id: ch04-4-1-1-dc-components | src: book p.99 | kind: concept

When the voltage level in a digital signal is constant for a while, the spectrum creates very low frequencies (results of Fourier analysis). These frequencies around
zero, called DC (direct-current) components, present problems for a system that cannot pass low frequencies or a system that uses electrical coupling (via a transformer). We can say that DC component means 0/1 parity that can cause base-line
wondering. For example, a telephone line cannot pass frequencies below 200 Hz.
Also a long-distance link may use one or more transformers to isolate different parts
of the line electrically. For these systems, we need a scheme with no DC component.

#### Self-synchronization
> id: ch04-4-1-1-self-synchronization | src: book p.99 | kind: concept

To correctly interpret the signals received from the sender, the receiver’s bit intervals
must correspond exactly to the sender’s bit intervals. If the receiver clock is faster or
slower, the bit intervals are not matched and the receiver might misinterpret the signals.
Figure 4.3 shows a situation in which the receiver has a shorter bit duration. The sender
sends 10110001, while the receiver receives 110111000011.
A self-synchronizing digital signal includes timing information in the data being
transmitted. This can be achieved if there are transitions in the signal that alert the
receiver to the beginning, middle, or end of the pulse. If the receiver’s clock is out of
synchronization, these points can reset the clock.

##### Example 4.3
> id: ch04-example-4-3 | src: book Example 4.3 | kind: worked_example
In a digital transmission, the receiver clock is 0.1 percent faster than the sender clock. How many
extra bits per second does the receiver receive if the data rate is 1 kbps? How many if the data
rate is 1 Mbps?

**Solution**
At 1 kbps, the receiver receives 1001 bps instead of 1000 bps.

> **[ASSET ch04_ill_003]** Figure 4.3: Effect of lack of synchronization
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_003.png
> - src: book Figure 4.3; p.100
> - shows: Figure 4.3: Effect of lack of synchronization. Two time plots compare the sent sequence with a receiver using the wrong clock. Misaligned sampling boundaries turn eight sent bits into twelve interpreted bits.
> - structure: Two time plots compare the sent sequence with a receiver using the wrong clock. Misaligned sampling boundaries turn eight sent bits into twelve interpreted bits.
> - text_in_image: 1; 0; 1; 1; 0; 0; 0; 1; • • •; Time; a. Sent; 1; 1; 0; 1; 1; 1; 0; 0; 0; 0; 1; 1; • • •; Time; b. Received
> - use_when: Teach ch04-example-4-3, interpret Figure 4.3, or solve a linked practice question.
> - confidence: high

→
→
1000 bits sent
1001 bits received
1 extra bps

At 1 Mbps, the receiver receives 1,001,000 bps instead of 1,000,000 bps.
→
→
1,000,000 bits sent
1,001,000 bits received
1000 extra bps

#### Built-in Error Detection
> id: ch04-4-1-1-built-in-error-detection | src: book p.100 | kind: concept

It is desirable to have a built-in error-detecting capability in the generated code to
detect some or all of the errors that occurred during transmission. Some encoding
schemes that we will discuss have this capability to some extent.

#### Immunity to Noise and Interference
> id: ch04-4-1-1-immunity-to-noise-and-interference | src: book p.100 | kind: concept

Another desirable code characteristic is a code that is immune to noise and other interferences. Some encoding schemes that we will discuss have this capability.

#### Complexity
> id: ch04-4-1-1-complexity | src: book p.100 | kind: concept

A complex scheme is more costly to implement than a simple one. For example, a
scheme that uses four signal levels is more difficult to interpret than one that uses only
two levels.

### 4.1.2 Line Coding Schemes
> id: ch04-4-1-2 | src: book 4.1.2; p.100 | kind: concept

We can roughly divide line coding schemes into five broad categories, as shown in
Figure 4.4.
There are several schemes in each category. We need to be familiar with all
schemes discussed in this section to understand the rest of the book. This section can be
used as a reference for schemes encountered later.

#### Unipolar Scheme
> id: ch04-4-1-2-unipolar-scheme | src: book p.100 | kind: concept

In a unipolar scheme, all the signal levels are on one side of the time axis, either above
or below.

> **[ASSET ch04_ill_004]** Figure 4.4: Line coding schemes
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_004.png
> - src: book Figure 4.4; p.101
> - shows: Figure 4.4: Line coding schemes. A classification tree branches from line coding to unipolar, polar, bipolar, multilevel, and multitransition families, with the named schemes listed beside each branch.
> - structure: A classification tree branches from line coding to unipolar, polar, bipolar, multilevel, and multitransition families, with the named schemes listed beside each branch.
> - text_in_image: Unipolar; NRZ; NRZ, RZ, and biphase (Manchester,; Polar; and differential Manchester); Line coding; Bipolar; AMI and pseudoternary; Multilevel; 2B/1Q,  8B/6T, and 4D-PAM5; Multitransition; MLT-3
> - use_when: Teach ch04-4-1-2-unipolar-scheme, interpret Figure 4.4, or solve a linked practice question.
> - confidence: high

#### NRZ (Non-Return-to-Zero)
> id: ch04-4-1-2-nrz-non-return-to-zero | src: book p.101 | kind: concept

Traditionally, a unipolar scheme was designed as a non-return-to-zero (NRZ) scheme
in which the positive voltage defines bit 1 and the zero voltage defines bit 0. It is called
NRZ because the signal does not return to zero at the middle of the bit. Figure 4.5
shows a unipolar NRZ scheme.

> **[ASSET ch04_ill_005]** Figure 4.5: Unipolar NRZ scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_005.png
> - src: book Figure 4.5; p.101
> - shows: Figure 4.5: Unipolar NRZ scheme. A unipolar NRZ waveform uses zero and positive voltage V for the shown bit pattern; an inset gives the normalized power expression.
> - structure: A unipolar NRZ waveform uses zero and positive voltage V for the shown bit pattern; an inset gives the normalized power expression.
> - text_in_image: Amplitude; 1; 0; 1; 1; 0; V; 1; 1; 1; V 2 +     (0)2 =     V 2; 2; 2; 2; 0; Normalized power; Time
> - use_when: Teach ch04-4-1-2-nrz-non-return-to-zero, interpret Figure 4.5, or solve a linked practice question.
> - confidence: high

Compared with its polar counterpart (see the next section), this scheme is very
costly. As we will see shortly, the normalized power (the power needed to send 1 bit per
unit line resistance) is double that for polar NRZ. For this reason, this scheme is normally not used in data communications today.

#### Polar Schemes
> id: ch04-4-1-2-polar-schemes | src: book p.101 | kind: concept

In polar schemes, the voltages are on both sides of the time axis. For example, the voltage level for 0 can be positive and the voltage level for 1 can be negative.

#### Non-Return-to-Zero (NRZ)
> id: ch04-4-1-2-non-return-to-zero-nrz | src: book p.101 | kind: concept

In polar NRZ encoding, we use two levels of voltage amplitude. We can have two versions of polar NRZ: NRZ-L and NRZ-I, as shown in Figure 4.6. The figure also shows
the value of r, the average baud rate, and the bandwidth. In the first variation, NRZ-L
(NRZ-Level), the level of the voltage determines the value of the bit. In the second
variation, NRZ-I (NRZ-Invert), the change or lack of change in the level of the voltage
determines the value of the bit. If there is no change, the bit is 0; if there is a change, the
bit is 1.

> **[ASSET ch04_ill_006]** Figure 4.6: Polar NRZ-L and NRZ-I schemes
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_006.png
> - src: book Figure 4.6; p.102
> - shows: Figure 4.6: Polar NRZ-L and NRZ-I schemes. NRZ-L and NRZ-I waveforms encode the same bit stream. NRZ-L maps levels to bits; NRZ-I uses an inversion for bit 1. A normalized power spectrum marks average signal rate N/2 and bandwidth versus f/N.
> - structure: NRZ-L and NRZ-I waveforms encode the same bit stream. NRZ-L maps levels to bits; NRZ-I uses an inversion for bit 1. A normalized power spectrum marks average signal rate N/2 and bandwidth versus f/N.
> - text_in_image: 0; 1; 0; 0; 1; 1; 1; 0; Save = N/2; r = 1; NRZ-L; P; Time; 1; Bandwidth; NRZ-I; 0.5; Time; 0; f /N; 0; 1; 2; No inversion: Next bit is 0; Inversion: Next bit is 1
> - use_when: Teach ch04-4-1-2-non-return-to-zero-nrz, interpret Figure 4.6, or solve a linked practice question.
> - confidence: high

In NRZ-L the level of the voltage determines the value of the bit. In NRZ-I
the inversion or the lack of inversion determines the value of the bit.

Let us compare these two schemes based on the criteria we previously defined.
Although baseline wandering is a problem for both variations, it is twice as severe in
NRZ-L. If there is a long sequence of 0s or 1s in NRZ-L, the average signal power
becomes skewed. The receiver might have difficulty discerning the bit value. In NRZ-I
this problem occurs only for a long sequence of 0s. If somehow we can eliminate the
long sequence of 0s, we can avoid baseline wandering. We will see shortly how this can
be done.
The synchronization problem (sender and receiver clocks are not synchronized)
also exists in both schemes. Again, this problem is more serious in NRZ-L than in
NRZ-I. While a long sequence of 0s can cause a problem in both schemes, a long
sequence of 1s affects only NRZ-L.
Another problem with NRZ-L occurs when there is a sudden change of polarity in
the system. For example, if twisted-pair cable is the medium, a change in the polarity of
the wire results in all 0s interpreted as 1s and all 1s interpreted as 0s. NRZ-I does not
have this problem. Both schemes have an average signal rate of N/2 Bd.

NRZ-L and NRZ-I both have an average signal rate of N/2 Bd.

Let us discuss the bandwidth. Figure 4.6 also shows the normalized bandwidth for
both variations. The vertical axis shows the power density (the power for each 1 Hz of
bandwidth); the horizontal axis shows the frequency. The bandwidth reveals a very
serious problem for this type of encoding. The value of the power density is very high
around frequencies close to zero. This means that there are DC components that carry a
high level of energy. As a matter of fact, most of the energy is concentrated in frequencies between 0 and N/2. This means that although the average of the signal rate is N/2,
the energy is not distributed evenly between the two halves.

NRZ-L and NRZ-I both have a DC component problem.
##### Example 4.4
> id: ch04-example-4-4 | src: book Example 4.4 | kind: worked_example
A system is using NRZ-I to transfer 10-Mbps data. What are the average signal rate and minimum bandwidth?

**Solution**
The average signal rate is S = N/2 = 500 kbaud. The minimum bandwidth for this average baud
rate is $B_{min}$ = S = 500 kHz.

#### Return-to-Zero (RZ)
> id: ch04-4-1-2-return-to-zero-rz | src: book p.103 | kind: concept

The main problem with NRZ encoding occurs when the sender and receiver clocks are
not synchronized. The receiver does not know when one bit has ended and the next bit
is starting. One solution is the return-to-zero (RZ) scheme, which uses three values:
positive, negative, and zero. In RZ, the signal changes not between bits but during the
bit. In Figure 4.7 we see that the signal goes to 0 in the middle of each bit. It remains
there until the beginning of the next bit. The main disadvantage of RZ encoding is that
it requires two signal changes to encode a bit and therefore occupies greater bandwidth.
The same problem we mentioned, a sudden change of polarity  resulting in all 0s interpreted as 1s and all 1s interpreted as 0s, still exists here, but  there is no DC component
problem. Another problem is the complexity: RZ uses three levels of voltage, which is
more complex to create and discern. As a result of all these deficiencies, the scheme is
not used today. Instead, it has been replaced by the better-performing Manchester and
differential Manchester schemes (discussed next).

> **[ASSET ch04_ill_007]** Figure 4.7: Polar RZ scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_007.png
> - src: book Figure 4.7; p.103
> - shows: Figure 4.7: Polar RZ scheme. Polar RZ returns to zero in every bit interval and uses positive, zero, and negative levels. The adjacent spectrum indicates r = 1/2, average signal rate N, and its wider bandwidth.
> - structure: Polar RZ returns to zero in every bit interval and uses positive, zero, and negative levels. The adjacent spectrum indicates r = 1/2, average signal rate N, and its wider bandwidth.
> - text_in_image: 1; Save = N; r =; 2; Amplitude; P; 0; 1; 0; 0; 1; Bandwidth; 1; 0.5; Time; 0; 0; 1; 2; f/N
> - use_when: Teach ch04-4-1-2-return-to-zero-rz, interpret Figure 4.7, or solve a linked practice question.
> - confidence: high

#### Biphase: Manchester and Differential Manchester
> id: ch04-4-1-2-biphase-manchester-and-differential-manchester | src: book p.103 | kind: concept

The idea of RZ (transition at the middle of the bit) and the idea of NRZ-L are combined
into the Manchester scheme. In Manchester encoding, the duration of the bit is divided
into two halves. The voltage remains at one level during the first half and moves to the
other level in the second half. The transition at the middle of the bit provides synchronization. Differential Manchester, on the other hand, combines the ideas of RZ and
NRZ-I. There is always a transition at the middle of the bit, but the bit values are determined at the beginning of the bit. If the next bit is 0, there is a transition; if the next bit
is 1, there is none. Figure 4.8 shows both Manchester and differential Manchester
encoding.
The Manchester scheme overcomes several problems associated with NRZ-L, and
differential Manchester overcomes several problems associated with NRZ-I. First, there

> **[ASSET ch04_ill_008]** Figure 4.8: Polar biphase: Manchester and differential Manchester schemes
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_008.png
> - src: book Figure 4.8; p.104
> - shows: Figure 4.8: Polar biphase: Manchester and differential Manchester schemes. Manchester and differential Manchester waveforms encode the same bits. Manchester uses a mid-bit transition; differential Manchester also uses presence or absence of a transition at the interval start. Their spectrum marks average signal rate N.
> - structure: Manchester and differential Manchester waveforms encode the same bits. Manchester uses a mid-bit transition; differential Manchester also uses presence or absence of a transition at the interval start. Their spectrum marks average signal rate N.
> - text_in_image: 0 is; 1 is; 0; 1; 0; 0; 1; 1; 1; Save = N; r =; 2; Manchester; P; Time; 1; Bandwidth; 0.5; 0; Differential; 0; 1; 2; f/N; Manchester; Time; No inversion: Next bit is 1; Inversion: Next bit is 0
> - use_when: Teach ch04-4-1-2-biphase-manchester-and-differential-manchester, interpret Figure 4.8, or solve a linked practice question.
> - confidence: high

In Manchester and differential Manchester encoding, the transition
at the middle of the bit is used for synchronization.

is no baseline wandering. There is no DC component because each bit has a positive and
negative voltage contribution. The only drawback is the signal rate. The signal rate for
Manchester and differential Manchester is double that for NRZ. The reason is that there
is always one transition at the middle of the bit and maybe one transition at the end of
each bit. Figure 4.8 shows both Manchester and differential Manchester encoding
schemes. Note that Manchester and differential Manchester schemes are also called
biphase schemes.

The minimum bandwidth of Manchester and differential Manchester
is 2 times that of NRZ.

#### Bipolar Schemes
> id: ch04-4-1-2-bipolar-schemes | src: book p.104 | kind: concept

In bipolar encoding (sometimes called multilevel binary), there are three voltage levels: positive, negative, and zero. The voltage level for one data element is at zero, while
the voltage level for the other element alternates between positive and negative.

In bipolar encoding, we use three levels: positive, zero, and negative.

#### AMI and Pseudoternary
> id: ch04-4-1-2-ami-and-pseudoternary | src: book p.104 | kind: concept

Figure 4.9 shows two variations of bipolar encoding: AMI and pseudoternary. A common bipolar encoding scheme is called bipolar alternate mark inversion (AMI). In
the term alternate mark inversion, the word mark comes from telegraphy and means 1.
So AMI means alternate 1 inversion. A neutral zero voltage represents binary 0. Binary
1s are represented by alternating positive and negative voltages. A variation of AMI
encoding is called pseudoternary in which the 1 bit is encoded as a zero voltage and
the 0 bit is encoded as alternating positive and negative voltages.

> **[ASSET ch04_ill_009]** Figure 4.9: Bipolar schemes: AMI and pseudoternary
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_009.png
> - src: book Figure 4.9; p.105
> - shows: Figure 4.9: Bipolar schemes: AMI and pseudoternary. AMI and pseudoternary waveforms alternate nonzero polarities. AMI assigns alternating nonzero pulses to 1s; pseudoternary assigns them to 0s. The spectrum marks average signal rate N/2.
> - structure: AMI and pseudoternary waveforms alternate nonzero polarities. AMI assigns alternating nonzero pulses to 1s; pseudoternary assigns them to 0s. The spectrum marks average signal rate N/2.
> - text_in_image: Amplitude; 1; Save =   N; r = 1; 2; 0; 1; 0; 0; 1; 0; P; AMI; Bandwidth; Time; 1; 0.5; Pseudoternary; 0; Time; f/N; 0; 1; 2
> - use_when: Teach ch04-4-1-2-ami-and-pseudoternary, interpret Figure 4.9, or solve a linked practice question.
> - confidence: high

The bipolar scheme was developed as an alternative to NRZ. The bipolar scheme
has the same signal rate as NRZ, but there is no DC component. The NRZ scheme has
most of its energy concentrated near zero frequency, which makes it unsuitable for
transmission over channels with poor performance around this frequency. The concentration of the energy in bipolar encoding is around frequency N/2. Figure 4.9 shows the
typical energy concentration for a bipolar scheme.
One may ask why we do not have a DC component in bipolar encoding. We can
answer this question by using the Fourier transform, but we can also think about it intuitively. If we have a long sequence of 1s, the voltage level alternates between positive
and negative; it is not constant. Therefore, there is no DC component. For a long
sequence of 0s, the voltage remains constant, but its amplitude is zero, which is the
same as having no DC component. In other words, a sequence that creates a constant
zero voltage does not have a DC component.
AMI is commonly used for long-distance communication, but it has a synchronization problem when a long sequence of 0s is present in the data. Later in the chapter, we
will see how a scrambling technique can solve this problem.

#### Multilevel Schemes
> id: ch04-4-1-2-multilevel-schemes | src: book p.105 | kind: concept

The desire to increase the data rate or decrease the required bandwidth has resulted in
the creation of many schemes. The goal is to increase the number of bits per baud by
encoding a pattern of m data elements into a pattern of n signal elements. We only have
two types of data elements (0s and 1s), which means that a group of m data elements
can produce a combination of $2^{m}$ data patterns. We can have different types of signal
elements by allowing different signal levels. If we have L different levels, then we can
produce $L^{n}$ combinations of signal patterns. If $2^{m}$ = $L^{n}$, then each data pattern is
encoded into one signal pattern. If $2^{m}$ < $L^{n}$, data patterns occupy only a subset of signal
patterns. The subset can be carefully designed to prevent baseline wandering, to provide synchronization, and to detect errors that occurred during data transmission. Data
encoding is not possible if $2^{m}$ > $L^{n}$ because some of the data patterns cannot be
encoded.
The code designers have classified these types of coding as mBnL, where m is the
length of the binary pattern, B means binary data, n is the length of the signal pattern,
and L is the number of levels in the signaling. A letter is often used in place of L: B
(binary) for L = 2, T (ternary) for L = 3, and Q (quaternary) for L = 4. Note that the first
two letters define the data pattern, and the second two define the signal pattern.

In mBnL schemes, a pattern of m data elements is encoded as a pattern of n signal
elements in which $2^{m}$ ≤ $L^{n}$.

#### 2B1Q
> id: ch04-4-1-2-2b1q | src: book p.106 | kind: concept

The first mBnL scheme we discuss, two binary, one quaternary (2B1Q), uses data
patterns of size 2 and encodes the 2-bit patterns as one signal element belonging to a
four-level signal. In this type of encoding m = 2, n = 1, and L = 4 (quaternary). Figure 4.10
shows an example of a 2B1Q signal.

> **[ASSET ch04_ill_010]** Figure 4.10: Multilevel: 2B1Q scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_010.png
> - src: book Figure 4.10; p.106
> - shows: Figure 4.10: Multilevel: 2B1Q scheme. The 2B1Q mapping table assigns dibits 00, 01, 10, and 11 to four amplitudes. A waveform encodes paired bits, and the spectrum marks r = 2 and average signal rate N/4.
> - structure: The 2B1Q mapping table assigns dibits 00, 01, 10, and 11 to four amplitudes. A waveform encodes paired bits, and the spectrum marks r = 2 and average signal rate N/4.
> - text_in_image: Rules:; 00; –3; 01; –1; 10; +3; 11; +1; Save = N/4; r = 2; 11; 00; 01; 11; 10; +3; P; +1; 1; Bandwidth; Time; –1; 0.5; 0; –3; f/N; 0; 1/2; 1; 2; Assuming positive original level
> - use_when: Teach ch04-4-1-2-2b1q, interpret Figure 4.10, or solve a linked practice question.
> - confidence: high

The average signal rate of 2B1Q is S = N/4. This means that using 2B1Q, we can
send data 2 times faster than by using NRZ-L. However, 2B1Q uses four different signal levels, which means the receiver has to discern four different thresholds. The
reduced bandwidth comes with a price. There are no redundant signal patterns in this
scheme because $2^{2}$ = $4^{1}$.
The 2B1Q scheme is used in DSL (Digital Subscriber Line) technology to provide
a high-speed connection to the Internet by using subscriber telephone lines (see
Chapter 14).

#### 8B6T
> id: ch04-4-1-2-8b6t | src: book p.106 | kind: concept

A very interesting scheme is eight binary, six ternary (8B6T). This code is used with
100BASE-4T cable, as we will see in Chapter 13. The idea is to encode a pattern of
8 bits as a pattern of six signal elements, where the signal has three levels (ternary). In
this type of scheme, we can have $2^{8}$ = 256 different data patterns and $3^{6}$ = 729 different

signal patterns. The mapping table is shown in Appendix F. There are 729 − 256 = 473
redundant signal elements that provide synchronization and error detection. Part of the
redundancy is also used to provide DC balance. Each signal pattern has a weight of 0 or
+1 DC values. This means that there is no pattern with the weight −1. To make the
whole stream DC-balanced, the sender keeps track of the weight. If two groups of
weight 1 are encountered one after another, the first one is sent as is, while the next one is
totally inverted to give a weight of  −1.
Figure 4.11 shows an example of three data patterns encoded as three signal patterns. The three possible signal levels are represented as −, 0, and +. The first 8-bit
pattern 00010001 is encoded as the signal pattern − 0 − 0 + + with weight 0; the second 8-bit pattern 01010011 is encoded as − + − + + 0 with weight +1. The third 8-bit
pattern 01010000 should be encoded as + − − + 0 + with weight +1. To create DC
balance, the sender inverts the actual signal. The receiver can easily recognize that
this is an inverted pattern because the weight is −1. The pattern is inverted before
decoding.

> **[ASSET ch04_ill_011]** Figure 4.11: Multilevel: 8B6T scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_011.png
> - src: book Figure 4.11; p.107
> - shows: Figure 4.11: Multilevel: 8B6T scheme. The 8B6T waveform maps successive 8-bit groups to six ternary signal elements at +V, 0, or −V; two example input groups and their ternary outputs are shown.
> - structure: The 8B6T waveform maps successive 8-bit groups to six ternary signal elements at +V, 0, or −V; two example input groups and their ternary outputs are shown.
> - text_in_image: 01010000; 00010001; 01010011; +V; Inverted; pattern; 0; Time; –V; – 0 – 0 + +; – + – + + 0; + – – + 0 +
> - use_when: Teach ch04-4-1-2-8b6t, interpret Figure 4.11, or solve a linked practice question.
> - confidence: high

The average signal rate is theoretically $S_{\mathrm{ave}}=(1/2)N(6/8)$; in practice
the minimum bandwidth is very close to 6N/8.

#### 4D-PAM5
> id: ch04-4-1-2-4d-pam5 | src: book p.107 | kind: concept

The last signaling scheme we discuss in this category is called four-dimensional five-level pulse amplitude modulation (4D-PAM5). The 4D means that data is sent over four
wires at the same time. It uses five voltage levels, such as −2, −1, 0, 1, and 2. However, one
level, level 0, is used only for forward error detection (discussed in Chapter 10). If we
assume that the code is just one-dimensional, the four levels create something similar to
8B4Q. In other words, an 8-bit word is translated to a signal element of four different levels.
The worst signal rate for this imaginary one-dimensional version is N × 4/8, or N/2.
The technique is designed to send data over four channels (four wires). This means
the signal rate can be reduced to N/8, a significant achievement. All 8 bits can be fed
into a wire simultaneously and sent by using one signal element. The point here is that
the four signal elements comprising one signal group are sent simultaneously in a four-dimensional setting. Figure 4.12 shows the imaginary one-dimensional and the actual
four-dimensional implementation. Gigabit LANs (see Chapter 13) use this technique to
send 1-Gbps data over four copper cables that can handle 125 Mbaud. This scheme has
a lot of redundancy in the signal pattern because $2^{8}$ data patterns are matched to $4^{4}$ =
256 signal patterns. The extra signal patterns can be used for other purposes such as
error detection.

> **[ASSET ch04_ill_012]** Figure 4.12: Multilevel: 4D-PAM5 scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_012.png
> - src: book Figure 4.12; p.108
> - shows: Figure 4.12: Multilevel: 4D-PAM5 scheme. A 4D-PAM5 encoder distributes eight incoming bits over four wires. Each wire carries a 250-Mbps five-level symbol stream, yielding four parallel 125-MBd paths.
> - structure: A 4D-PAM5 encoder distributes eight incoming bits over four wires. Each wire carries a 250-Mbps five-level symbol stream, yielding four parallel 125-MBd paths.
> - text_in_image: 1 Gbps; 00011110; 250 Mbps; Wire 1 (125 MBd); 250 Mbps; Wire 2 (125 MBd); +2; +1; 250 Mbps; Wire 3 (125 MBd); –1; –2; 250 Mbps; Wire 4 (125 MBd)
> - use_when: Teach ch04-4-1-2-4d-pam5, interpret Figure 4.12, or solve a linked practice question.
> - confidence: high

#### Multitransition: MLT-3
> id: ch04-4-1-2-multitransition-mlt-3 | src: book p.108 | kind: concept

NRZ-I and differential Manchester are classified as differential encoding but use two
transition rules to encode binary data (no inversion, inversion). If we have a signal with
more than two levels, we can design a differential encoding scheme with more than two
transition rules. MLT-3 is one of them. The multiline transmission, three-level (MLT-3)
scheme uses three levels (+V, 0, and −V) and three transition rules to move between the
levels.
1. If the next bit is 0, there is no transition.
2. If the next bit is 1 and the current level is not 0, the next level is 0.
3. If the next bit is 1 and the current level is 0, the next level is the opposite of the last
nonzero level.
The behavior of MLT-3 can best be described by the state diagram shown in Figure 4.13.
The three voltage levels (−V, 0, and +V) are shown by three states (ovals). The transition
from one state (level) to another is shown by the connecting lines. Figure 4.13 also shows
two examples of an MLT-3 signal.
One might wonder why we need to use MLT-3, a scheme that maps one bit to one
signal element. The signal rate is the same as that for NRZ-I, but with greater complexity (three levels and complex transition rules). It turns out that the shape of the signal in
this scheme helps to reduce the required bandwidth. Let us look at the worst-case scenario, a sequence of 1s. In this case, the signal element pattern +V 0 −V 0 is repeated
every 4 bits. A nonperiodic signal has changed to a periodic signal with the period
equal to 4 times the bit duration. This worst-case situation can be simulated as an analog signal with a frequency one-fourth of the bit rate. In other words, the signal rate for
MLT-3 is one-fourth the bit rate. This makes MLT-3 a suitable choice when we need to
send 100 Mbps on a copper wire that cannot support more than 32 MHz (frequencies
above this level create electromagnetic emissions). MLT-3 and LANs are discussed in
Chapter 13.

> **[ASSET ch04_ill_013]** Figure 4.13: Multitransition: MLT-3 scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_013.png
> - src: book Figure 4.13; p.109
> - shows: Figure 4.13: Multitransition: MLT-3 scheme. MLT-3 cycles through +V, 0, −V, and 0 only when the next bit is 1; bit 0 holds the current level. Typical and worst-case waveforms accompany a state-transition diagram.
> - structure: MLT-3 cycles through +V, 0, −V, and 0 only when the next bit is 1; bit 0 holds the current level. Typical and worst-case waveforms accompany a state-transition diagram.
> - text_in_image: 0; 1; 0; 1; 1; 0; 1; 1; +V; 0V; Next bit: 0; Time; –V; Next bit: 1; Next bit: 1; 0; a. Typical case; Next bit: 1; +V; –V; 1; 1; 1; 1; 1; 1; 1; 1; Last; Last; non-zero; non-zero; +V; Next bit: 0; Next bit: 0; level: –V; level: +V; 0V; c. Transition states; Time; –V; b. Worst case
> - use_when: Teach ch04-4-1-2-multitransition-mlt-3, interpret Figure 4.13, or solve a linked practice question.
> - confidence: high

#### Summary of Line Coding Schemes
> id: ch04-4-1-2-summary-of-line-coding-schemes | src: book p.109 | kind: concept

We summarize in Table 4.1 the characteristics of the different schemes discussed.

**Table 4.1: Summary of line-coding schemes**

| Category | Scheme | Bandwidth (average) | Characteristics |
| --- | --- | --- | --- |
| Unipolar | NRZ | B = N/2 | Costly, no self-synchronization if long 0s or 1s, DC |
| Polar | NRZ-L | B = N/2 | No self-synchronization if long 0s or 1s, DC |
|  | NRZ-I | B = N/2 | No self-synchronization for long 0s, DC |
|  | Biphase | B = N | Self-synchronization, no DC, high bandwidth |
| Bipolar | AMI | B = N/2 | No self-synchronization for long 0s, DC |
| Multilevel | 2B1Q | B = N/4 | No self-synchronization for long same double bits |
|  | 8B6T | B = 3N/4 | Self-synchronization, no DC |
|  | 4D-PAM5 | B = N/8 | Self-synchronization, no DC |
| Multitransition | MLT-3 | B = N/3 | No self-synchronization for long 0s |

Bandwidth

(average)

Costly, no self-synchronization if long 0s or
1s, DC

No self-synchronization for long same double
bits

### 4.1.3 Block Coding
> id: ch04-4-1-3 | src: book 4.1.3; p.109 | kind: concept

We need redundancy to ensure synchronization and to provide some kind of inherent
error detecting. Block coding can give us this redundancy and improve the performance of line coding. In general, block coding changes a block of m bits into a block
of n bits, where n is larger than m. Block coding is referred to as an mB/nB encoding
technique.

Block coding is normally referred to as mB/nB coding;
it replaces each m-bit group with an n-bit group.
The slash in block encoding (for example, 4B/5B) distinguishes block encoding
from multilevel encoding (for example, 8B6T), which is written without a slash. Block
coding normally involves three steps: division, substitution, and combination. In the
division step, a sequence of bits is divided into groups of m bits. For example, in 4B/5B
encoding, the original bit sequence is divided into 4-bit groups. The heart of block coding is the substitution step. In this step, we substitute an m-bit group with an n-bit
group. For example, in 4B/5B encoding we substitute a 4-bit group with a 5-bit group.
Finally, the n-bit groups are combined to form a stream. The new stream has more bits
than the original bits. Figure 4.14 shows the procedure.

> **[ASSET ch04_ill_014]** Figure 4.14: Block coding concept
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_014.png
> - src: book Figure 4.14; p.110
> - shows: Figure 4.14: Block coding concept. An mB/nB block coder divides an input stream into m-bit groups, substitutes each with an n-bit code, and recombines the n-bit groups into a longer output stream.
> - structure: An mB/nB block coder divides an input stream into m-bit groups, substitutes each with an n-bit code, and recombines the n-bit groups into a longer output stream.
> - text_in_image: Division of a stream into m-bit groups; m bits; m bits; m bits; …; …; …; 1 1 0; 1; 0 0 0; 1; • • •; 0 1 0; 1; mB-to-nB; substitution; …; …; …; 0 1 0; 1 0 1; 0 0 0; 0 0 1; 0 1 1; 1 1 1; • • •; n bits; n bits; n bits; Combining n-bit groups into a stream
> - use_when: Teach ch04-4-1-3, interpret Figure 4.14, or solve a linked practice question.
> - confidence: high

#### 4B/5B
> id: ch04-4-1-3-4b-5b | src: book p.110 | kind: concept

The four binary/five binary (4B/5B) coding scheme was designed to be used in combination with NRZ-I. Recall that NRZ-I has a good signal rate, one-half that of the
biphase, but it has a synchronization problem. A long sequence of 0s can make the
receiver clock lose synchronization. One solution is to change the bit stream, prior to
encoding with NRZ-I, so that it does not have a long stream of 0s. The 4B/5B scheme
achieves this goal. The block-coded stream does not have more that three consecutive
0s, as we will see later. At the receiver, the NRZ-I encoded digital signal is first
decoded into a stream of bits and then decoded to remove the redundancy. Figure 4.15
shows the idea.

> **[ASSET ch04_ill_015]** Figure 4.15: Using block coding 4B/5B with NRZ-I line coding scheme
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_015.png
> - src: book Figure 4.15; p.110
> - shows: Figure 4.15: Using block coding 4B/5B with NRZ-I line coding scheme. A 4B/5B encoder precedes NRZ-I encoding at the sender; the receiver applies NRZ-I decoding and then 4B/5B decoding to recover the original data.
> - structure: A 4B/5B encoder precedes NRZ-I encoding at the sender; the receiver applies NRZ-I decoding and then 4B/5B decoding to recover the original data.
> - text_in_image: Sender; Receiver; Digital signal; Link; 4B/5B; NRZ-I; NRZ-I; 4B/5B; encoding; encoding; decoding; decoding
> - use_when: Teach ch04-4-1-3-4b-5b, interpret Figure 4.15, or solve a linked practice question.
> - confidence: high

In 4B/5B, the 5-bit output that replaces the 4-bit input has no more than one leading
zero (left bit) and no more than two trailing zeros (right bits). So when different groups
are combined to make a new sequence, there are never more than three consecutive 0s.
(Note that NRZ-I has no problem with sequences of 1s.) Table 4.2 shows the corresponding pairs used in 4B/5B encoding. Note that the first two columns pair a 4-bit
group with a 5-bit group. A group of 4 bits can have only 16 different combinations
while a group of 5 bits can have 32 different combinations. This means that there are 16
groups that are not used for 4B/5B encoding. Some of these unused groups are used for
control purposes; the others are not used at all. The latter provide a kind of error detection. If a 5-bit group arrives that belongs to the unused portion of the table, the receiver
knows that there is an error in the transmission.

**Table 4.2: 4B/5B mapping codes**

| Data Sequence | Encoded Sequence | Control Sequence | Encoded Sequence |
| --- | --- | --- | --- |
| 0000 | 11110 | Q (Quiet) | 00000 |
| 0001 | 01001 | I (Idle) | 11111 |
| 0010 | 10100 | H (Halt) | 00100 |
| 0011 | 10101 | J (Start delimiter) | 11000 |
| 0100 | 01010 | K (Start delimiter) | 10001 |
| 0101 | 01011 | T (End delimiter) | 01101 |
| 0110 | 01110 | S (Set) | 11001 |
| 0111 | 01111 | R (Reset) | 00111 |
| 1000 | 10010 |  |  |
| 1001 | 10011 |  |  |
| 1010 | 10110 |  |  |
| 1011 | 10111 |  |  |
| 1100 | 11010 |  |  |
| 1101 | 11011 |  |  |
| 1110 | 11100 |  |  |
| 1111 | 11101 |  |  |

Figure 4.16 shows an example of substitution in 4B/5B coding. 4B/5B encoding
solves the problem of synchronization and overcomes one of the deficiencies of NRZ-I.
However, we need to remember that it increases the signal rate of NRZ-I. The redundant bits add 20 percent more baud. Still, the result is less than the biphase scheme
which has a signal rate of 2 times that of NRZ-I. However, 4B/5B block encoding does
not solve the DC component problem of NRZ-I. If a DC component is unacceptable, we
need to use biphase or bipolar encoding.

##### Example 4.5
> id: ch04-example-4-5 | src: book Example 4.5 | kind: worked_example
We need to send data at a 1-Mbps rate. What is the minimum required bandwidth, using a combination of 4B/5B and NRZ-I or Manchester coding?

**Solution**
First 4B/5B block coding increases the bit rate to 1.25 Mbps. The minimum bandwidth using
NRZ-I is N/2 or 625 kHz. The Manchester scheme needs a minimum bandwidth of 1 MHz. The

> **[ASSET ch04_ill_016]** Figure 4.16: Substitution in 4B/5B block coding
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_016.png
> - src: book Figure 4.16; p.112
> - shows: Figure 4.16: Substitution in 4B/5B block coding. Four-bit blocks such as 1111 and 0001 map to five-bit blocks such as 11111 and 11001; branching lines illustrate substitution from the 4-bit set to the 5-bit set.
> - structure: Four-bit blocks such as 1111 and 0001 map to five-bit blocks such as 11111 and 11001; branching lines illustrate substitution from the 4-bit set to the 5-bit set.
> - text_in_image: 4-bit blocks; 1 1 1 1; 0 0 0 1; 0 0 0 0; • • •; 1 1 1 1 1; 1 1 1 1 0; 1 1 1 0 1; 0 1 0 0 1; 0 0 0 0 0; • • •; • • •; 5-bit blocks
> - use_when: Teach ch04-example-4-5, interpret Figure 4.16, or solve a linked practice question.
> - confidence: high

first choice needs a lower bandwidth, but has a DC component problem; the second choice needs
a higher bandwidth, but does not have a DC component problem.

#### 8B/10B
> id: ch04-4-1-3-8b-10b | src: book p.112 | kind: concept

The eight binary/ten binary (8B/10B) encoding is similar to 4B/5B encoding except
that a group of 8 bits of data is now substituted by a 10-bit code. It provides greater
error detection capability than 4B/5B. The 8B/10B block coding is actually a combination of 5B/6B and 3B/4B encoding, as shown in Figure 4.17.

> **[ASSET ch04_ill_017]** Figure 4.17: 8B/10B block encoding
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_017.png
> - src: book Figure 4.17; p.112
> - shows: Figure 4.17: 8B/10B block encoding. An 8B/10B encoder combines a 5B/6B encoder, a 3B/4B encoder, and a disparity controller to turn each 8-bit block into a balanced 10-bit block.
> - structure: An 8B/10B encoder combines a 5B/6B encoder, a 3B/4B encoder, and a disparity controller to turn each 8-bit block into a balanced 10-bit block.
> - text_in_image: 5B/6B encoding; 10-bit block; 8-bit block; Disparity; controller; 3B/4B encoding; 8B/10B encoder
> - use_when: Teach ch04-4-1-3-8b-10b, interpret Figure 4.17, or solve a linked practice question.
> - confidence: high

The five most significant bits of a 10-bit block are fed into the 5B/6B encoder; the
three least significant bits are fed into a 3B/4B encoder. The split is done to simplify the
mapping table. To prevent a long run of consecutive 0s or 1s, the code uses a disparity
controller which keeps track of excess 0s over 1s (or 1s over 0s). If the bits in the current block create a disparity that contributes to the previous disparity (either direction),
then each bit in the code is complemented (a 0 is changed to a 1 and a 1 is changed to a 0).
The coding has $2^{10}$ − $2^{8}$ = 768 redundant groups that can be used for disparity checking
and error detection. In general, the technique is superior to 4B/5B because of better
built-in error-checking capability and better synchronization.

### 4.1.4 Scrambling
> id: ch04-4-1-4 | src: book 4.1.4; p.113 | kind: concept

Biphase schemes that are suitable for dedicated links between stations in a LAN are not
suitable for long-distance communication because of their wide bandwidth requirement.
The combination of block coding and NRZ line coding is not suitable for long-distance
encoding either, because of the DC component. Bipolar AMI encoding, on the other
hand, has a narrow bandwidth and does not create a DC component. However, a long
sequence of 0s upsets the synchronization. If we can find a way to avoid a long sequence
of 0s in the original stream, we can use bipolar AMI for long distances. We are looking
for a technique that does not increase the number of bits and does provide synchronization. We are looking for a solution that substitutes long zero-level pulses with a combination of other levels to provide synchronization. One solution is called scrambling. We
modify part of the AMI rule to include scrambling, as shown in Figure 4.18. Note that
scrambling, as opposed to block coding, is done at the same time as encoding. The
system needs to insert the required pulses based on the defined scrambling rules. Two
common scrambling techniques are B8ZS and HDB3.

> **[ASSET ch04_ill_018]** Figure 4.18: AMI used with scrambling
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_018.png
> - src: book Figure 4.18; p.113
> - shows: Figure 4.18: AMI used with scrambling. A sender modifies an AMI waveform when a violated all-zero run appears; the receiver detects the deliberate violations and decodes the modified AMI stream.
> - structure: A sender modifies an AMI waveform when a violated all-zero run appears; the receiver detects the deliberate violations and decodes the modified AMI stream.
> - text_in_image: Sender; Receiver; Violated digital signal; Modified AMI; Modified AMI; decoding; encoding
> - use_when: Teach ch04-4-1-4, interpret Figure 4.18, or solve a linked practice question.
> - confidence: high

#### B8ZS
> id: ch04-4-1-4-b8zs | src: book p.113 | kind: concept

Bipolar with 8-zero substitution (B8ZS) is commonly used in North America. In
this technique, eight consecutive zero-level voltages are replaced by the sequence
000VB0VB. The V in the sequence denotes violation; this is a nonzero voltage that
breaks an AMI rule of encoding (opposite polarity from the previous). The B in the
sequence denotes bipolar, which means a nonzero level voltage in accordance with the
AMI rule. There are two cases, as shown in Figure 4.19.

> **[ASSET ch04_ill_019]** Figure 4.19: Two cases of B8ZS scrambling technique
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_019.png
> - src: book Figure 4.19; p.113
> - shows: Figure 4.19: Two cases of B8ZS scrambling technique. Two B8ZS panels show eight-zero substitution after a positive previous pulse and after a negative previous pulse. B and V markers distinguish balancing and deliberate violation pulses.
> - structure: Two B8ZS panels show eight-zero substitution after a positive previous pulse and after a negative previous pulse. B and V markers distinguish balancing and deliberate violation pulses.
> - text_in_image: 1; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; V; B; B; V; 0; 0; 0; 0; 0; 0; 0; 0; V; B; B; V; a. Previous level is positive.; b. Previous level is negative.
> - use_when: Teach ch04-4-1-4-b8zs, interpret Figure 4.19, or solve a linked practice question.
> - confidence: high

Note that the scrambling in this case does not change the bit rate. Also, the technique balances the positive and negative voltage levels (two positives and two negatives), which means that the DC balance is maintained. Note that the substitution may
change the polarity of a 1 because, after the substitution, AMI needs to follow its rules.

B8ZS substitutes eight consecutive zeros with 000VB0VB.

One more point is worth mentioning. The letter V (violation) or B (bipolar) here is
relative. The V means the same polarity as the polarity of the previous nonzero pulse;
B means the polarity opposite to the polarity of the previous nonzero pulse.

#### HDB3
> id: ch04-4-1-4-hdb3 | src: book p.114 | kind: concept

High-density bipolar 3-zero (HDB3) is commonly used outside of North America. In
this technique, which is more conservative than B8ZS, four consecutive zero-level voltages are replaced with a sequence of 000V or B00V. The reason for two different substitutions is to maintain the even number of nonzero pulses after each substitution. The
two rules can be stated as follows:
1. If the number of nonzero pulses after the last substitution is odd, the substitution
pattern will be 000V, which makes the total number of nonzero pulses even.
2. If the number of nonzero pulses after the last substitution is even, the substitution
pattern will be B00V, which makes the total number of nonzero pulses even.
Figure 4.20 shows an example.

> **[ASSET ch04_ill_020]** Figure 4.20: Different situations in HDB3 scrambling technique
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_020.png
> - src: book Figure 4.20; p.114
> - shows: Figure 4.20: Different situations in HDB3 scrambling technique. Three HDB3 panels show four-zero substitution for even and odd counts of nonzero pulses and for the next alternating case. B and V pulses preserve AMI polarity rules while inserting violations.
> - structure: Three HDB3 panels show four-zero substitution for even and odd counts of nonzero pulses and for the next alternating case. B and V pulses preserve AMI polarity rules while inserting violations.
> - text_in_image: First; Second; Third; substitution; substitution; substitution; 1; 1; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; B; B; V; V; 0; 0; 0; 0; 0; 0; 0; V; Even; Even Odd; Even; Even
> - use_when: Teach ch04-4-1-4-hdb3, interpret Figure 4.20, or solve a linked practice question.
> - confidence: high

There are several points we need to mention here. First, before the first substitution, the number of nonzero pulses is even, so the first substitution is B00V. After this
substitution, the polarity of the 1 bit is changed because the AMI scheme, after each
substitution, must follow its own rule. After this bit, we need another substitution,
which is 000V because we have only one nonzero pulse (odd) after the last substitution.
The third substitution is B00V because there are no nonzero pulses after the second
substitution (even).

HDB3 substitutes four consecutive zeros with 000V or B00V depending
on the number of nonzero pulses after the last substitution.

## 4.2 ANALOG-TO-DIGITAL CONVERSION
> id: ch04-4-2 | src: book 4.2; p.115 | kind: concept

The techniques described in Section  4.1 convert digital data to digital signals. Sometimes, however, we have an analog signal such as one created by a microphone or camera. We have seen in Chapter 3 that a digital signal is superior to an analog signal. The
tendency today is to change an analog signal to digital data. In this section we describe
two techniques, pulse code modulation and delta modulation. After the digital data are
created (digitization), we can use one of the techniques described in Section 4.1 to convert the digital data to a digital signal.

### 4.2.1 Pulse Code Modulation (PCM)
> id: ch04-4-2-1 | src: book 4.2.1; p.115 | kind: concept

The most common technique to change an analog signal to digital data (digitization) is
called pulse code modulation (PCM). A PCM encoder has three processes, as shown in
Figure 4.21.

> **[ASSET ch04_ill_021]** Figure 4.21: Components of PCM encoder
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_021.png
> - src: book Figure 4.21; p.115
> - shows: Figure 4.21: Components of PCM encoder. A PCM encoder takes an analog signal through sampling, quantizing, and encoding. Insets show the PAM samples and quantized levels; the output is a digital bit stream.
> - structure: A PCM encoder takes an analog signal through sampling, quantizing, and encoding. Insets show the PAM samples and quantized levels; the output is a digital bit stream.
> - text_in_image: Quantized signal; PCM encoder; 1 1 … 1 1 0 0; Sampling; Encoding; Quantizing; Digital data; Analog signal; PAM signal
> - use_when: Teach ch04-4-2-1, interpret Figure 4.21, or solve a linked practice question.
> - confidence: high

1. The analog signal is sampled.
2. The sampled signal is quantized.
3. The quantized values are encoded as streams of bits.

#### Sampling
> id: ch04-4-2-1-sampling | src: book p.115 | kind: concept

The first step in PCM is sampling. The analog signal is sampled every $T_{s}$ s, where $T_{s}$ is
the sample interval or period. The inverse of the sampling interval is called the sampling rate or sampling frequency and denoted by $f_{s}$, where $f_s=1/T_s$. There are three
sampling methods—ideal, natural, and flat-top—as shown in Figure 4.22.
In ideal sampling, pulses from the analog signal are sampled. This is an ideal sampling method and cannot be easily implemented. In natural sampling, a high-speed
switch is turned on for only the small period of time when the sampling occurs. The
result is a sequence of samples that retains the shape of the analog signal. The most

> **[ASSET ch04_ill_022]** Figure 4.22: Three different sampling methods for PCM
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_022.png
> - src: book Figure 4.22; p.116
> - shows: Figure 4.22: Three different sampling methods for PCM. Three aligned time plots compare ideal point sampling, natural pulse sampling, and flat-top sample-and-hold sampling of the same analog waveform.
> - structure: Three aligned time plots compare ideal point sampling, natural pulse sampling, and flat-top sample-and-hold sampling of the same analog waveform.
> - text_in_image: Amplitude; Amplitude; Amplitude; Analog signal; Analog signal; Analog signal; Time; Time; Time; Ts; a. Ideal sampling; b. Natural sampling; c. Flat-top sampling
> - use_when: Teach ch04-4-2-1-sampling, interpret Figure 4.22, or solve a linked practice question.
> - confidence: high

common sampling method, called sample and hold, however, creates flat-top samples
by using a circuit.
The sampling process is sometimes referred to as pulse amplitude modulation
(PAM). We need to remember, however, that the result is still an analog signal with
nonintegral values.

#### Sampling Rate
> id: ch04-4-2-1-sampling-rate | src: book p.116 | kind: concept

One important consideration is the sampling rate or frequency. What are the restrictions
on $T_{s}$? This question was elegantly answered by Nyquist. According to the Nyquist theorem, to reproduce the original analog signal, one necessary condition is that the sampling rate be at least twice the highest frequency in the original signal.

According to the Nyquist theorem, the sampling rate must be
at least 2 times the highest frequency contained in the signal.

We need to elaborate on the theorem at this point. First, we can sample a signal
only if the signal is band-limited. In other words, a signal with an infinite bandwidth
cannot be sampled. Second, the sampling rate must be at least 2 times the highest frequency, not the bandwidth. If the analog signal is low-pass, the bandwidth and the
highest frequency are the same value. If the analog signal is bandpass, the bandwidth
value is lower than the value of the maximum frequency. Figure 4.23 shows the value
of the sampling rate for two types of signals.

##### Example 4.6
> id: ch04-example-4-6 | src: book Example 4.6 | kind: worked_example
For an intuitive example of the Nyquist theorem, let us sample a simple sine wave at three sampling rates: $f_{s}$ = 4f (2 times the Nyquist rate), $f_{s}$ = 2f (Nyquist rate), and $f_{s}$ = f (one-half the
Nyquist rate). Figure 4.24 shows the sampling and the subsequent recovery of the signal.
It can be seen that sampling at the Nyquist rate can create a good approximation of the original sine wave (part a). Oversampling in part b can also create the same approximation, but it is
redundant and unnecessary. Sampling below the Nyquist rate (part c) does not produce a signal
that looks like the original sine wave.

##### Example 4.7
> id: ch04-example-4-7 | src: book Example 4.7 | kind: worked_example
As an interesting example, let us see what happens if we sample a periodic event such as the revolution of a hand of a clock. The second hand of a clock has a period of 60 s. According to the

> **[ASSET ch04_ill_023]** Figure 4.23: Nyquist sampling rate for low-pass and bandpass signals
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_023.png
> - src: book Figure 4.23; p.117
> - shows: Figure 4.23: Nyquist sampling rate for low-pass and bandpass signals. Frequency plots show a low-pass signal spanning zero to fmax and a bandpass signal spanning fmin to fmax. Both annotate the Nyquist rate as twice fmax.
> - structure: Frequency plots show a low-pass signal spanning zero to fmax and a bandpass signal spanning fmin to fmax. Both annotate the Nyquist rate as twice fmax.
> - text_in_image: Amplitude; Nyquist rate = 2 ×  fmax; Low-pass signal; Frequency; fmin; fmax; Amplitude; Nyquist rate = 2  ×  fmax; Bandpass signal; 0; fmin; fmax; Frequency
> - use_when: Teach ch04-example-4-7, interpret Figure 4.23, or solve a linked practice question.
> - confidence: high

> **[ASSET ch04_ill_024]** Figure 4.24: Recovery of a sampled sine wave for different sampling rates
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_024.png
> - src: book Figure 4.24; p.117
> - shows: Figure 4.24: Recovery of a sampled sine wave for different sampling rates. Three panels sample and reconstruct a sine wave at fs = 2f, fs = 4f, and fs = f, showing Nyquist-rate sampling, oversampling, and an incorrect undersampled reconstruction.
> - structure: Three panels sample and reconstruct a sine wave at fs = 2f, fs = 4f, and fs = f, showing Nyquist-rate sampling, oversampling, and an incorrect undersampled reconstruction.
> - text_in_image: a. Nyquist rate sampling: fs = 2 f; b. Oversampling: fs = 4 f; c. Undersampling: fs =  f
> - use_when: Teach ch04-example-4-7, interpret Figure 4.24, or solve a linked practice question.
> - confidence: high

According to the Nyquist theorem, we need to sample the hand (take and send a picture) every 30 s ($T_s=T/2$ or $f_s=2f$). In Figure 4.25a, the sample points, in order, are 12, 6, 12, 6, 12, and 6. The receiver of the
samples cannot tell if the clock is moving forward or backward. In part b, we sample at double
the Nyquist rate (every 15 s). The sample points, in order, are 12, 3, 6, 9, and 12. The clock is
moving forward. In part c, we sample below the Nyquist rate ($T_s=3T/4$ or $f_s=4f/3$). The sample

> **[ASSET ch04_ill_025]** Figure 4.25: Sampling of a clock with only one hand
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_025.png
> - src: book Figure 4.25; p.118
> - shows: Figure 4.25: Sampling of a clock with only one hand. Clock-face sequences compare sampling at the Nyquist rate, oversampling, and undersampling. The observed samples can imply forward, ambiguous, or backward motion.
> - structure: Clock-face sequences compare sampling at the Nyquist rate, oversampling, and undersampling. The observed samples can imply forward, ambiguous, or backward motion.
> - text_in_image: Samples can mean that; 12; 12; 12; 12; 12; the clock is moving; either forward or; 9; 3; 9; 3; 9; 3; 9; 3; 9; 3; backward.; 6; 6; 6; 6; 6; (12-6-12-6-12); 1; a. Sampling at Nyquist rate: Ts = T; 2; 12; 12; 12; 12; 12; Samples show clock; is moving forward.; 9; 3; 9; 3; 9; 3; 9; 3; 9; 3; (12-3-6-9-12); 6; 6; 6; 6; 6; 1; b. Oversampling (above Nyquist rate): Ts =   T; 4; 12; 12; 12; 12; 12; Samples show clock; 9; 3; 9; 3; 9; 3; 9; 3; 9; 3; is moving backward.; (12-9-6-3-12); 6; 6; 6; 6; 6; c. Undersampling (below Nyquist rate): Ts = T 3; 4
> - use_when: Teach ch04-example-4-7, interpret Figure 4.25, or solve a linked practice question.
> - confidence: high

points, in order, are 12, 9, 6, 3, and 12. Although the clock is moving forward, the receiver thinks
that the clock is moving backward.

##### Example 4.8
> id: ch04-example-4-8 | src: book Example 4.8 | kind: worked_example
An example related to Example 4.7 is the seemingly backward rotation of the wheels of a forwardmoving car in a movie. This can be explained by undersampling. A movie is filmed at 24 frames
per second. If a wheel is rotating more than 12 times per second, the undersampling creates the
impression of a backward rotation.

##### Example 4.9
> id: ch04-example-4-9 | src: book Example 4.9 | kind: worked_example
Telephone companies digitize voice by assuming a maximum frequency of 4000 Hz. The sampling rate therefore is 8000 samples per second.

##### Example 4.10
> id: ch04-example-4-10 | src: book Example 4.10 | kind: worked_example
A complex low-pass signal has a bandwidth of 200 kHz. What is the minimum sampling rate for
this signal?

**Solution**
The bandwidth of a low-pass signal is between 0 and f, where f is the maximum frequency in the
signal. Therefore, we can sample this signal at 2 times the highest frequency (200 kHz). The sampling rate is therefore 400,000 samples per second.
##### Example 4.11
> id: ch04-example-4-11 | src: book Example 4.11 | kind: worked_example
A complex bandpass signal has a bandwidth of 200 kHz. What is the minimum sampling rate for
this signal?

**Solution**
We cannot find the minimum sampling rate in this case because we do not know where the bandwidth starts or ends. We do not know the maximum frequency in the signal.

#### Quantization
> id: ch04-4-2-1-quantization | src: book p.119 | kind: concept

The result of sampling is a series of pulses with amplitude values between the maximum and minimum amplitudes of the signal. The set of amplitudes can be infinite with
nonintegral values between the two limits. These values cannot be used in the encoding
process. The following are the steps in quantization:
1. We assume that the original analog signal has instantaneous amplitudes between
$V_{min}$ and $V_{max}$.
2. We divide the range into L zones, each of height Δ (delta).

$$\Delta = \frac{V_{\max}-V_{\min}}{L}$$

3. We assign quantized values of 0 to L − 1 to the midpoint of each zone.
4. We approximate the value of the sample amplitude to the quantized values.
As a simple example, assume that we have a sampled signal and the sample amplitudes
are between −20 and +20 V. We decide to have eight levels (L = 8). This means that
Δ = 5 V. Figure 4.26 shows this example.
We have shown only nine samples using ideal sampling (for simplicity). The
value at the top of each sample in the graph shows the actual amplitude. In the chart,
the first row is the normalized value for each sample (actual amplitude/Δ). The quantization process selects the quantization value from the middle of each zone. This
means that the normalized quantized values (second row) are different from the normalized amplitudes. The difference is called the normalized error (third row). The
fourth row is the quantization code for each sample based on the quantization levels
at the left of the graph. The encoded words (fifth row) are the final products of the
conversion.

#### Quantization Levels
> id: ch04-4-2-1-quantization-levels | src: book p.119 | kind: concept

In the previous example, we showed eight quantization levels. The choice of L, the
number of levels, depends on the range of the amplitudes of the analog signal and how
accurately we need to recover the signal. If the amplitude of a signal fluctuates between
two values only, we need only two levels; if the signal, like voice, has many amplitude
values, we need more quantization levels. In audio digitizing, L is normally chosen to
be 256; in video it is normally thousands. Choosing lower values of L increases the
quantization error if there is a lot of fluctuation in the signal.

#### Quantization Error
> id: ch04-4-2-1-quantization-error | src: book p.119 | kind: concept

One important issue is the error created in the quantization process. (Later, we will see
how this affects high-speed modems.) Quantization is an approximation process. The

> **[ASSET ch04_ill_026]** Figure 4.26: Quantization and encoding of a sampled signal
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_026.png
> - src: book Figure 4.26; p.120
> - shows: Figure 4.26: Quantization and encoding of a sampled signal. A quantization graph assigns nine PAM samples to eight zones around multiples of Δ. A table records normalized PAM values, quantized values, errors, decimal codes, and three-bit encoded words for every sample.
> - structure: A quantization graph assigns nine PAM samples to eight zones around multiples of Δ. A table records normalized PAM values, quantized values, errors, decimal codes, and three-bit encoded words for every sample.
> - text_in_image: Quantization; Normalized; codes; amplitude; 4D; 19.7; 7; 16.2; 3D; 6; 11.0; 2D; 5; 7.5; D; 4; 0; 3; Time; –5.5; –D; –6.0; –6.1; 2; –9.4; –2D; –11.3; 1; –3D; 0; –4D; Normalized; –1.22; 1.50; 3.24; 3.94; 2.20; –1.10; –2.26; –1.88; –1.20; PAM values; Normalized; –1.50; 1.50; 3.50; 3.50; 2.50; –1.50; –2.50; –1.50; –1.50; quantized values; Normalized; –0.38; 0; +0.26; –0.44; +0.30; –0.40; –0.24; +0.38; –0.30; error; Quantization code; 2; 5; 7; 7; 6; 2; 1; 2; 2; Encoded words; 010; 101; 111; 111; 110; 010; 001; 010; 010
> - use_when: Teach ch04-4-2-1-quantization-error, interpret Figure 4.26, or solve a linked practice question.
> - confidence: high

input values to the quantizer are the real values; the output values are the approximated
values. The output values are chosen to be the middle value in the zone. If the input
value is also at the middle of the zone, there is no quantization error; otherwise, there is
an error. In the previous example, the normalized amplitude of the third sample is 3.24,
but the normalized quantized value is 3.50. This means that there is an error of +0.26.
The value of the error for any sample is less than  Δ/2. In other words, we have  −Δ/2 ≤
error ≤ Δ/2.
The quantization error changes the signal-to-noise ratio of the signal, which in turn
reduces the upper limit capacity according to Shannon.
It can be proven that the contribution of the quantization error to the $SNR_{dB}$ of
the signal depends on the number of quantization levels L, or the bits per sample $n_{b}$, as
shown in the following formula:

$$\mathrm{SNR}_{\mathrm{dB}} = 6.02n_b + 1.76\ \mathrm{dB}$$

##### Example 4.12
> id: ch04-example-4-12 | src: book Example 4.12 | kind: worked_example
What is the $SNR_{dB}$ in the example of Figure 4.26?

**Solution**
We can use the formula to find the quantization. We have eight levels and 3 bits per sample, so
$SNR_{dB}$ = 6.02(3) + 1.76 = 19.82 dB. Increasing the number of levels increases the SNR.
##### Example 4.13
> id: ch04-example-4-13 | src: book Example 4.13 | kind: worked_example
A telephone subscriber line must have an $SNR_{dB}$ above 40. What is the minimum number of bits
per sample?

**Solution**
We can calculate the number of bits as
$$\mathrm{SNR}_{\mathrm{dB}} = 6.02n_b + 1.76 = 40 \;\Rightarrow\; n_b = 6.35$$

Telephone companies usually assign 7 or 8 bits per sample.

#### Uniform Versus Nonuniform Quantization
> id: ch04-4-2-1-uniform-versus-nonuniform-quantization | src: book p.121 | kind: concept

For many applications, the distribution of the instantaneous amplitudes in the analog
signal is not uniform. Changes in amplitude often occur more frequently in the lower
amplitudes than in the higher ones. For these types of applications it is better to use
nonuniform zones. In other words, the height of Δ is not fixed; it is greater near the
lower amplitudes and less near the higher amplitudes. Nonuniform quantization can
also be achieved by using a process called companding and expanding. The signal is
companded at the sender before conversion; it is expanded at the receiver after conversion. Companding means reducing the instantaneous voltage amplitude for large values; expanding is the opposite process. Companding gives greater weight to strong
signals and less weight to weak ones. It has been proved that nonuniform quantization
effectively reduces the $SNR_{dB}$ of quantization.

#### Encoding
> id: ch04-4-2-1-encoding | src: book p.121 | kind: concept

The last step in PCM is encoding. After each sample is quantized and the number of
bits per sample is decided, each sample can be changed to an $n_{b}$-bit code word. In Figure 4.26 the encoded words are shown in the last row. A quantization code of 2 is
encoded as 010; 5 is encoded as 101; and so on. Note that the number of bits for each
sample is determined from the number of quantization levels. If the number of quantization levels is L, the number of bits is $n_b=\log_2L$. In our example L is 8 and $n_{b}$ is
therefore 3. The bit rate can be found from the formula

$$N = f_s n_b$$

##### Example 4.14
> id: ch04-example-4-14 | src: book Example 4.14 | kind: worked_example
We want to digitize the human voice. What is the bit rate, assuming 8 bits per sample?

**Solution**
The human voice normally contains frequencies from 0 to 4000 Hz. So the sampling rate and bit
rate are calculated as follows:

Sampling rate = 4000 × 2 = 8000 samples/s
Bit rate = 8000 × 8 = 64,000 bps = 64 kbps

#### Original Signal Recovery
> id: ch04-4-2-1-original-signal-recovery | src: book p.121 | kind: concept

The recovery of the original signal requires the PCM decoder. The decoder first uses
circuitry to convert the code words into a pulse that holds the amplitude until the next
pulse. After the staircase signal is completed, it is passed through a low-pass filter to
smooth the staircase signal into an analog signal. The filter has the same cutoff frequency as the original signal at the sender. If the signal has been sampled at (or
greater than) the Nyquist sampling rate and if there are enough quantization levels,
the original signal will be recreated. Note that the maximum and minimum values of
the original signal can be achieved by using amplification. Figure 4.27 shows the
simplified process.

> **[ASSET ch04_ill_027]** Figure 4.27: Components of a PCM decoder
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_027.png
> - src: book Figure 4.27; p.122
> - shows: Figure 4.27: Components of a PCM decoder. A PCM decoder converts digital code words into held staircase samples, then passes them through a low-pass filter to reconstruct a smooth analog waveform.
> - structure: A PCM decoder converts digital code words into held staircase samples, then passes them through a low-pass filter to reconstruct a smooth analog waveform.
> - text_in_image: Amplitude; Time; PCM decoder; Amplitude; Analog signal; Make and; Low-pass; 1 1 … 1 1 0 0; connect; Time; filter; samples; Digital data
> - use_when: Teach ch04-4-2-1-original-signal-recovery, interpret Figure 4.27, or solve a linked practice question.
> - confidence: high

#### PCM Bandwidth
> id: ch04-4-2-1-pcm-bandwidth | src: book p.122 | kind: concept

Suppose we are given the bandwidth of a low-pass analog signal. If we then digitize the
signal, what is the new minimum bandwidth of the channel that can pass this digitized
signal? We have said that the minimum bandwidth of a line-encoded signal is $B_{min}$ = c ×
N × (1/r). We substitute the value of N in this formula:
$$B_{\min}=cN\left(\frac{1}{r}\right)=cn_bf_s\left(\frac{1}{r}\right)=cn_b(2B_{\mathrm{analog}})\left(\frac{1}{r}\right)$$

When 1/r = 1 (for a NRZ or bipolar signal) and c = (1/2) (the average situation), the
minimum bandwidth is

$$B_{\min}=n_bB_{\mathrm{analog}}$$

This means the minimum bandwidth of the digital signal is $n_{b}$ times greater than the
bandwidth of the analog signal. This is the price we pay for digitization.

##### Example 4.15
> id: ch04-example-4-15 | src: book Example 4.15 | kind: worked_example
We have a low-pass analog signal of 4 kHz. If we send the analog signal, we need a channel with
a minimum bandwidth of 4 kHz. If we digitize the signal and send 8 bits per sample, we need a
channel with a minimum bandwidth of 8 × 4 kHz = 32 kHz.

#### Maximum Data Rate of a Channel
> id: ch04-4-2-1-maximum-data-rate-of-a-channel | src: book p.123 | kind: concept

In Chapter 3, we discussed the Nyquist theorem, which gives the data rate of a channel
as Nmax = 2 × B × log2 L. We can deduce this rate from the Nyquist sampling theorem
by using the following arguments.
1. We assume that the available channel is low-pass with bandwidth B.
2. We assume that the digital signal we want to send has L levels, where each level is
a signal element. This means r = 1/log2 L.
3. We first pass the digital signal through a low-pass filter to cut off the frequencies
above B Hz.
4. We treat the resulting signal as an analog signal and sample it at 2 × B samples per
second and quantize it using L levels. Additional quantization levels are useless
because the signal originally had L levels.
5. The resulting bit rate is N = fs × nb = 2 × B × log2 L. This is the maximum
bandwidth.

$$N_{\max}=2B\log_2L\ \mathrm{bps}$$

#### Minimum Required Bandwidth
> id: ch04-4-2-1-minimum-required-bandwidth | src: book p.123 | kind: concept

The previous argument can give us the minimum bandwidth if the data rate and the
number of signal levels are fixed. We can say

$$B_{\min}=\frac{N}{2\log_2L}\ \mathrm{Hz}$$

### 4.2.2 Delta Modulation (DM)
> id: ch04-4-2-2 | src: book 4.2.2; p.123 | kind: concept

PCM is a very complex technique. Other techniques have been developed to reduce the
complexity of PCM. The simplest is delta modulation. PCM finds the value of the signal amplitude for each sample; DM finds the change from the previous sample. Figure 4.28 shows the process. Note that there are no code words here; bits are sent one
after another.

> **[ASSET ch04_ill_028]** Figure 4.28: The process of delta modulation
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_028.png
> - src: book Figure 4.28; p.123
> - shows: Figure 4.28: The process of delta modulation. An analog curve is approximated by a staircase with step size d and interval T. Each upward or downward step produces the displayed 1 or 0 in the generated bit stream.
> - structure: An analog curve is approximated by a staircase with step size d and interval T. Each upward or downward step produces the displayed 1 or 0 in the generated bit stream.
> - text_in_image: Amplitude; T; d; Time; Generated; 0; 1; 1; 1; 1; 1; 1; 0; 0; 0; 0; 0; 0; 1; 1; binary data
> - use_when: Teach ch04-4-2-2, interpret Figure 4.28, or solve a linked practice question.
> - confidence: high

#### Modulator
> id: ch04-4-2-2-modulator | src: book p.124 | kind: concept

The modulator is used at the sender site to create a stream of bits from an analog signal.
The process records the small positive or negative changes, called delta δ. If the delta is
positive, the process records a 1; if it is negative, the process records a 0. However, the
process needs a base against which the analog signal is compared. The modulator
builds a second signal that resembles a staircase. Finding the change is then reduced to
comparing the input signal with the gradually made staircase signal. Figure 4.29 shows
a diagram of the process.

> **[ASSET ch04_ill_029]** Figure 4.29: Delta modulation components
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_029.png
> - src: book Figure 4.29; p.124
> - shows: Figure 4.29: Delta modulation components. A delta modulator compares the analog input with delayed staircase feedback. A comparator drives both the digital output and a staircase maker; a delay unit feeds the next comparison.
> - structure: A delta modulator compares the analog input with delayed staircase feedback. A comparator drives both the digital output and a staircase maker; a delay unit feeds the next comparison.
> - text_in_image: DM modulator; 1 1 … 1 1 0 0; Comparator; Digital data; Analog signal; Delay unit; Staircase maker
> - use_when: Teach ch04-4-2-2-modulator, interpret Figure 4.29, or solve a linked practice question.
> - confidence: high

The modulator, at each sampling interval, compares the value of the analog signal
with the last value of the staircase signal. If the amplitude of the analog signal is
larger, the next bit in the digital data is 1; otherwise, it is 0. The output of the comparator, however, also makes the staircase itself. If the next bit is 1, the staircase maker
moves the last point of the staircase signal δ up; if the next bit is 0, it moves it δ down.
Note that we need a delay unit to hold the staircase function for a period between two
comparisons.

#### Demodulator
> id: ch04-4-2-2-demodulator | src: book p.124 | kind: concept

The demodulator takes the digital data and, using the staircase maker and the
delay unit, creates the analog signal. The created analog signal, however, needs to
pass through a low-pass filter for smoothing. Figure 4.30 shows the schematic
diagram.

#### Adaptive DM
> id: ch04-4-2-2-adaptive-dm | src: book p.124 | kind: concept

A better performance can be achieved if the value of δ is not fixed. In adaptive
delta modulation, the value of δ changes according to the amplitude of the analog
signal.

#### Quantization Error
> id: ch04-4-2-2-quantization-error | src: book p.124 | kind: concept

It is obvious that DM is not perfect. Quantization error is always introduced in the process. The quantization error of DM, however, is much less than that for PCM.

> **[ASSET ch04_ill_030]** Figure 4.30: Delta demodulation components
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_030.png
> - src: book Figure 4.30; p.125
> - shows: Figure 4.30: Delta demodulation components. A delta demodulator sends received bits through a staircase maker and delay feedback loop, then smooths the staircase with a low-pass filter to recover the analog signal.
> - structure: A delta demodulator sends received bits through a staircase maker and delay feedback loop, then smooths the staircase with a low-pass filter to recover the analog signal.
> - text_in_image: DM demodulator; Staircase; maker; 1 1 … 1 1 0 0; Digital data; Low-pass; Analog signal; filter; Delay unit
> - use_when: Teach ch04-4-2-2-quantization-error, interpret Figure 4.30, or solve a linked practice question.
> - confidence: high

## 4.3 TRANSMISSION MODES
> id: ch04-4-3 | src: book 4.3; p.125 | kind: concept

Of primary concern when we are considering the transmission of data from one device
to another is the wiring, and of primary concern when we are considering the wiring is
the data stream. Do we send 1 bit at a time; or do we group bits into larger groups and,
if so, how? The transmission of binary data across a link can be accomplished in either
parallel or serial mode. In parallel mode, multiple bits are sent with each clock tick.
In serial mode, 1 bit is sent with each clock tick. While there is only one way to send
parallel data, there are three subclasses of serial transmission: asynchronous, synchronous, and isochronous (see Figure 4.31).

> **[ASSET ch04_ill_031]** Figure 4.31: Data transmission and modes
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_031.png
> - src: book Figure 4.31; p.125
> - shows: Figure 4.31: Data transmission and modes. A hierarchy divides data transmission into parallel and serial; serial divides further into asynchronous, synchronous, and isochronous modes.
> - structure: A hierarchy divides data transmission into parallel and serial; serial divides further into asynchronous, synchronous, and isochronous modes.
> - text_in_image: Data transmission; Parallel; Serial; Asynchronous; Synchronous; Isochronous
> - use_when: Teach ch04-4-3, interpret Figure 4.31, or solve a linked practice question.
> - confidence: high

### 4.3.1 Parallel Transmission
> id: ch04-4-3-1 | src: book 4.3.1; p.125 | kind: concept

Binary data, consisting of 1s and 0s, may be organized into groups of n bits each.
Computers produce and consume data in groups of bits much as we conceive of and use
spoken language in the form of words rather than letters. By grouping, we can send
data n bits at a time instead of 1. This is called parallel transmission.
The mechanism for parallel transmission is a conceptually simple one: Use n wires
to send n bits at one time. That way each bit has its own wire, and all n bits of one
group can be transmitted with each clock tick from one device to another. Figure 4.32
shows how parallel transmission works for n = 8. Typically, the eight wires are bundled
in a cable with a connector at each end.

> **[ASSET ch04_ill_032]** Figure 4.32: Parallel transmission
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_032.png
> - src: book Figure 4.32; p.126
> - shows: Figure 4.32: Parallel transmission. Eight bits leave the sender at the same time over eight separate lines and reach the receiver in parallel; a curved boundary labels one wire pod containing eight lines.
> - structure: Eight bits leave the sender at the same time over eight separate lines and reach the receiver in parallel; a curved boundary labels one wire pod containing eight lines.
> - text_in_image: The 8 bits; are sent; together; 0; 1; 1; 0; 0; 0; 1; 0; We need; Sender; Receiver; eight lines
> - use_when: Teach ch04-4-3-1, interpret Figure 4.32, or solve a linked practice question.
> - confidence: high

The advantage of parallel transmission is speed. All else being equal, parallel
transmission can increase the transfer speed by a factor of n over serial transmission.
But there is a significant disadvantage: cost. Parallel transmission requires n communication lines (wires in the example) just to transmit the data stream. Because this is
expensive, parallel transmission is usually limited to short distances.

### 4.3.2 Serial Transmission
> id: ch04-4-3-2 | src: book 4.3.2; p.126 | kind: concept

In serial transmission one bit follows another, so we need only one communication channel rather than n to transmit data between two communicating devices (see
Figure 4.33).

> **[ASSET ch04_ill_033]** Figure 4.33: Serial transmission
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_033.png
> - src: book Figure 4.33; p.126
> - shows: Figure 4.33: Serial transmission. A parallel-to-serial converter emits eight bits one after another on one line; a serial-to-parallel converter restores the group at the receiver.
> - structure: A parallel-to-serial converter emits eight bits one after another on one line; a serial-to-parallel converter restores the group at the receiver.
> - text_in_image: The 8 bits are sent; 0; 0; one after another.; 1; 1; 1; 1; 0; 1; 1; 0; 0; 0; 1; 0; 0; 0; We need only; 0; 0; one line (wire).; 0; 0; 1; 1; Parallel/serial; Serial/parallel; 0; 0; converter; converter; Sender; Receiver
> - use_when: Teach ch04-4-3-2, interpret Figure 4.33, or solve a linked practice question.
> - confidence: high

The advantage of serial over parallel transmission is that with only one communication channel, serial transmission reduces the cost of transmission over parallel by
roughly a factor of n.
Since communication within devices is parallel, conversion devices are required at
the interface between the sender and the line (parallel-to-serial) and between the line
and the receiver (serial-to-parallel).
Serial transmission occurs in one of three ways: asynchronous, synchronous, and
isochronous.

#### Asynchronous Transmission
> id: ch04-4-3-2-asynchronous-transmission | src: book p.127 | kind: concept

Asynchronous transmission is so named because the timing of a signal is unimportant.
Instead, information is received and translated by agreed upon patterns. As long as
those patterns are followed, the receiving device can retrieve the information without
regard to the rhythm in which it is sent. Patterns are based on grouping the bit stream
into bytes. Each group, usually 8 bits, is sent along the link as a unit. The sending system handles each group independently, relaying it to the link whenever ready, without
regard to a timer.
Without synchronization, the receiver cannot use timing to predict when the next
group will arrive. To alert the receiver to the arrival of a new group, therefore, an extra
bit is added to the beginning of each byte. This bit, usually a 0, is called the start bit.
To let the receiver know that the byte is finished, 1 or more additional bits are appended
to the end of the byte. These bits, usually 1s, are called stop bits. By this method, each
byte is increased in size to at least 10 bits, of which 8 bits is information and 2 bits or
more are signals to the receiver. In addition, the transmission of each byte may then be
followed by a gap of varying duration. This gap can be represented either by an idle
channel or by a stream of additional stop bits.

In asynchronous transmission, we send 1 start bit (0) at the beginning and 1 or more
stop bits (1s) at the end of each byte. There may be a gap between bytes.

The start and stop bits and the gap alert the receiver to the beginning and end of
each byte and allow it to synchronize with the data stream. This mechanism is called
asynchronous because, at the byte level, the sender and receiver do not have to be synchronized. But within each byte, the receiver must still be synchronized with the
incoming bit stream. That is, some synchronization is required, but only for the duration of a single byte. The receiving device resynchronizes at the onset of each new byte.
When the receiver detects a start bit, it sets a timer and begins counting bits as they
come in. After n bits, the receiver looks for a stop bit. As soon as it detects the stop bit,
it waits until it detects the next start bit.

Asynchronous here means “asynchronous at the byte level,”
but the bits are still synchronized; their durations are the same.

Figure 4.34 is a schematic illustration of asynchronous transmission. In this example, the start bits are 0s, the stop bits are 1s, and the gap is represented by an idle line
rather than by additional stop bits.
The addition of stop and start bits and the insertion of gaps into the bit stream
make asynchronous transmission slower than forms of transmission that can operate

> **[ASSET ch04_ill_034]** Figure 4.34: Asynchronous transmission
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_034.png
> - src: book Figure 4.34; p.128
> - shows: Figure 4.34: Asynchronous transmission. An asynchronous bit stream frames each data unit with a start bit and stop bits. Gaps of arbitrary length separate the units, and an arrow shows the direction of flow.
> - structure: An asynchronous bit stream frames each data unit with a start bit and stop bits. Gaps of arbitrary length separate the units, and an arrow shows the direction of flow.
> - text_in_image: Direction of flow; Stop bit; Start bit; Sender; Receiver; Data; 1; 11111011; 0; 01101; 0; 1; 11111011; 0; 1; 00010111; 0; 1; 11; Gaps between; data units
> - use_when: Teach ch04-4-3-2-asynchronous-transmission, interpret Figure 4.34, or solve a linked practice question.
> - confidence: high

without the addition of control information. But it is cheap and effective, two advantages that make it an attractive choice for situations such as low-speed communication.
For example, the connection of a keyboard to a computer is a natural application for
asynchronous transmission. A user types only one character at a time, types extremely
slowly in data processing terms, and leaves unpredictable gaps of time between
characters.

#### Synchronous Transmission
> id: ch04-4-3-2-synchronous-transmission | src: book p.128 | kind: concept

In synchronous transmission, the bit stream is combined into longer “frames,” which
may contain multiple bytes. Each byte, however, is introduced onto the transmission
link without a gap between it and the next one. It is left to the receiver to separate the
bit stream into bytes for decoding purposes. In other words, data are transmitted as an
unbroken string of 1s and 0s, and the receiver separates that string into the bytes, or
characters, it needs to reconstruct the information.

In synchronous transmission, we send bits one after another without start or stop
bits or gaps. It is the responsibility of the receiver to group the bits.

Figure 4.35 gives a schematic illustration of synchronous transmission. We have
drawn in the divisions between bytes. In reality, those divisions do not exist; the
sender puts its data onto the line as one long string. If the sender wishes to send data
in separate bursts, the gaps between bursts must be filled with a special sequence of 0s
and 1s that means idle. The receiver counts the bits as they arrive and groups them in
8-bit units.
Without gaps and start and stop bits, there is no built-in mechanism to help the
receiving device adjust its bit synchronization midstream. Timing becomes very important, therefore, because the accuracy of the received information is completely dependent on the ability of the receiving device to keep an accurate count of the bits as they
come in.

> **[ASSET ch04_ill_035]** Figure 4.35: Synchronous transmission
> - type: illustration
> - kind: diagram
> - file: assets/ch04_ill_035.png
> - src: book Figure 4.35; p.129
> - shows: Figure 4.35: Synchronous transmission. A synchronous transmission sends a continuous stream organized into frames, with no gaps between data units inside a frame; sender, receiver, frame boundaries, and flow direction are shown.
> - structure: A synchronous transmission sends a continuous stream organized into frames, with no gaps between data units inside a frame; sender, receiver, frame boundaries, and flow direction are shown.
> - text_in_image: Direction of flow; Frame; Frame; Frame; 11110011; 11111011; 11110110; 11110111; • • •; 11110111; Sender; Receiver
> - use_when: Teach ch04-4-3-2-synchronous-transmission, interpret Figure 4.35, or solve a linked practice question.
> - confidence: high

The advantage of synchronous transmission is speed. With no extra bits or gaps to
introduce at the sending end and remove at the receiving end, and, by extension, with
fewer bits to move across the link, synchronous transmission is faster than asynchronous transmission. For this reason, it is more useful for high-speed applications such as
the transmission of data from one computer to another. Byte synchronization is accomplished in the data-link layer.
We need to emphasize one point here. Although there is no gap between characters
in synchronous serial transmission, there may be uneven gaps between frames.

#### Isochronous
> id: ch04-4-3-2-isochronous | src: book p.129 | kind: concept

In real-time audio and video, in which uneven delays between frames are not acceptable, synchronous transmission fails. For example, TV images are broadcast at the rate
of 30 images per second; they must be viewed at the same rate. If each image is sent by
using one or more frames, there should be no delays between frames. For this type of
application, synchronization between characters is not enough; the entire stream of bits
must be synchronized. The isochronous transmission guarantees that the data arrive at
a fixed rate.

## 4.4 END-CHAPTER MATERIALS
> id: ch04-4-4 | src: book 4.4; p.129 | kind: concept

### 4.4.1 Recommended Reading
> id: ch04-4-4-1 | src: book 4.4.1; p.129 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets […] refer to the reference list at the end of the text.

#### Books
> id: ch04-4-4-1-books | src: book p.129 | kind: concept

Digital to digital conversion is discussed in [Pea92], [Cou01], and [Sta04]. Sampling
is discussed in [Pea92], [Cou01], and [Sta04]. [Hsu03] gives a good mathematical
approach to modulation and sampling. More advanced materials can be found in
[Ber96].

### 4.4.2 Key Terms
> id: ch04-4-4-2 | src: book 4.4.2; p.130 | kind: concept

- adaptive delta modulation
- alternate mark inversion (AMI)
- analog-to-digital conversion
- asynchronous transmission
- baseline
- baseline wandering
- baud rate
- biphase
- bipolar
- bipolar with 8-zero substitution (B8ZS)
- bit rate
- block coding
- companding and expanding
- data element
- data rate
- DC component
- delta modulation (DM)
- differential Manchester
- digital-to-digital conversion
- digitization
- eight binary/ten binary (8B/10B)
- eight-binary, six-ternary (8B6T)
- four binary/five binary (4B/5B)
- four dimensional, five-level pulse amplitude
- modulation (4D-PAM5)
- high-density bipolar 3-zero (HDB3)
- isochronous transmission
- line coding
- Manchester
- modulation rate
- multilevel binary
- multiline transmission, three-level (MLT-3)
- non-return-to-zero (NRZ)
- non-return-to-zero, invert (NRZ-I)
- non-return-to-zero, level (NRZ-L)
- Nyquist theorem
- parallel transmission
- polar
- pseudoternary
- pulse amplitude modulation (PAM)
- pulse code modulation (PCM)
- pulse rate
- quantization
- quantization error
- return-to-zero (RZ)
- sample and hold
- sampling
- sampling rate
- scrambling
- self-synchronizing
- serial transmission
- signal element
- signal rate
- start bit
- stop bit
- synchronous transmission
- transmission mode
- two-binary, one quaternary (2B1Q)
- unipolar

### 4.4.3 Summary
> id: ch04-4-4-3 | src: book 4.4.3; p.130 | kind: summary

Digital-to-digital conversion involves three techniques: line coding, block coding, and
scrambling. Line coding is the process of converting digital data to a digital signal. We
can roughly divide line coding schemes into five broad categories: unipolar, polar,
bipolar, multilevel, and multitransition. Block coding provides redundancy to ensure
synchronization and inherent error detection. Block coding is normally referred to as
mB/nB coding; it replaces each m-bit group with an n-bit group. Scrambling provides
synchronization without increasing the number of bits. Two common scrambling techniques are B8ZS and HDB3.
The most common technique to change an analog signal to digital data (digitization) is called pulse code modulation (PCM). The first step in PCM is sampling. The
analog signal is sampled every $T_{s}$ second, where $T_{s}$ is the sample interval or period. The
inverse of the sampling interval is called the sampling rate or sampling frequency and
denoted by $f_{s}$, where $f_s=1/T_s$. There are three sampling methods—ideal, natural, and
flat-top. According to the Nyquist theorem, to reproduce the original analog signal, one
necessary condition is that the sampling rate be at least twice the highest frequency in
the original signal. Other sampling techniques have been developed to reduce the complexity of PCM. The simplest is delta modulation. PCM finds the value of the signal
amplitude for each sample; DM finds the change from the previous sample.
While there is only one way to send parallel data, there are three subclasses of
serial transmission: asynchronous, synchronous, and isochronous. In asynchronous
transmission, we send 1 start bit (0) at the beginning and 1 or more stop bits (1s) at the
end of each byte. In synchronous transmission, we send bits one after another without
start or stop bits or gaps. It is the responsibility of the receiver to group the bits. The
isochronous mode provides synchronization for the entire stream of bits. In other
words, it guarantees that the data arrive at a fixed rate.
