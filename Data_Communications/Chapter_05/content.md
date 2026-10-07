---
doc_type: scientific_content
course_id: data_communications
chapter: 5
chapter_id: data_communications_ch05
chapter_title: Analog Transmission
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_5/ch5.pdf
  pages: 135-154
assets_dir: assets
asset_counts:
  illustration: 20
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:08:10+00:00'
status: complete
---
# Chapter 5: Analog Transmission

## Chapter Objectives
> id: ch05-0 | src: book p.135 | kind: objectives

In Chapter 3, we discussed the advantages and disadvantages of digital and analog
transmission. We saw that while digital transmission is very desirable, a low-pass
channel is needed. We also saw that analog transmission is the only choice if we have a
bandpass channel. Digital transmission was discussed in Chapter 4; we discuss analog
transmission in this chapter.
Converting digital data to a bandpass analog signal is traditionally called digital-to-analog conversion. Converting a low-pass analog signal to a bandpass analog signal
is traditionally called analog-to-analog conversion. In this chapter, we discuss these two
types of conversions in two sections:

- The first section discusses digital-to-analog conversion. The section shows how we
can change digital data to an analog signal when a band-pass channel is available.
The first method described is called amplitude shift keying (ASK), in which the
amplitude of a carrier is changed using the digital data. The second method
described is called frequency shift keying (FSK), in which the frequency of a carrier is changed using the digital data. The third method described is called phase
shift keying (PSK), in which the phase of a carrier signal is changed to represent
digital data. The fourth method described is called quadrature amplitude modulation (QAM), in which both amplitude and phase of a carrier signal are changed to
represent digital data.

- The second section discusses analog-to-analog conversion. The section shows how
we can change an analog signal to a new analog signal with a smaller bandwidth.
The conversion is used when only a band-pass channel is available. The first
method is called amplitude modulation (AM), in which the amplitude of a carrier
is changed based on the changes in the original analog signal. The second method
is called frequency modulation (FM), in which the phase of a carrier is changed
based on the changes in the original analog signal. The third method is called
phase modulation (PM), in which the phase of a carrier signal is changed to show
the changes in the original signal.

## 5.1 DIGITAL-TO-ANALOG CONVERSION
> id: ch05-5-1 | src: book 5.1; p.136 | kind: concept

Digital-to-analog conversion is the process of changing one of the characteristics of
an analog signal based on the information in digital data. Figure 5.1 shows the relationship between the digital information, the digital-to-analog modulating process,
and the resultant analog signal.

> **[ASSET ch05_ill_001]** Figure 5.1: Digital-to-analog conversion
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_001.png
> - src: book Figure 5.1; p.136
> - shows: Figure 5.1: Digital-to-analog conversion. A left-to-right communication path sends digital data into a modulator, carries the resulting analog signal across the link, and uses a demodulator to recover digital data at the receiver.
> - structure: A left-to-right communication path sends digital data into a modulator, carries the resulting analog signal across the link, and uses a demodulator to recover digital data at the receiver.
> - text_in_image: Sender; Receiver; Analog signal; Digital data; Digital data; 0 1 0 1  …  1 0 1; 0 1 0 1  …  1 0 1; Link; Modulator; Demodulator
> - use_when: Teach ch05-5-1, interpret Figure 5.1, compare modulation methods, or support a linked practice question.
> - confidence: high

As discussed in Chapter 3, a sine wave is defined by three characteristics: amplitude, frequency, and phase. When we vary any one of these characteristics, we create a
different version of that wave. So, by changing one characteristic of a simple electric
signal, we can use it to represent digital data. Any of the three characteristics can be
altered in this way, giving us at least three mechanisms for modulating digital data into
an analog signal: amplitude shift keying (ASK), frequency shift keying (FSK), and
phase shift keying (PSK). In addition, there is a fourth (and better) mechanism that
combines changing both the amplitude and phase, called quadrature amplitude modulation (QAM). QAM is the most efficient of these options and is the mechanism commonly used today (see Figure 5.2).

> **[ASSET ch05_ill_002]** Figure 5.2: Types of digital-to-analog conversion
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_002.png
> - src: book Figure 5.2; p.136
> - shows: Figure 5.2: Types of digital-to-analog conversion. A classification tree branches digital-to-analog conversion into ASK, FSK, PSK, and QAM, with each abbreviation attached to its full modulation name.
> - structure: A classification tree branches digital-to-analog conversion into ASK, FSK, PSK, and QAM, with each abbreviation attached to its full modulation name.
> - text_in_image: Digital-to-analog; conversion; Amplitude shift keying; Frequency shift keying; Phase shift keying; (ASK); (FSK); (PSK); Quadrature amplitude modulation; (QAM)
> - use_when: Teach ch05-5-1, interpret Figure 5.2, compare modulation methods, or support a linked practice question.
> - confidence: high

### 5.1.1 Aspects of Digital-to-Analog Conversion
> id: ch05-5-1-1 | src: book 5.1.1; p.137 | kind: concept

Before we discuss specific methods of digital-to-analog modulation, two basic issues
must be reviewed: bit and baud rates and the carrier signal.

#### Data Element Versus Signal Element
> id: ch05-5-1-1-data-element-versus-signal-element | src: book p.137 | kind: concept

In Chapter 4, we discussed the concept of the data element versus the signal element.
We defined a data element as the smallest piece of information to be exchanged, the bit.
We also defined a signal element as the smallest unit of a signal that is constant.
Although we continue to use the same terms in this chapter, we will see that the nature
of the signal element is a little bit different in analog transmission.

#### Data Rate Versus Signal Rate
> id: ch05-5-1-1-data-rate-versus-signal-rate | src: book p.137 | kind: concept

We can define the data rate (bit rate) and the signal rate (baud rate) as we did for digital
transmission. The relationship between them is

$$S = N\left(\frac{1}{r}\right)\ \text{baud}$$

where N is the data rate (bps) and r is the number of data elements carried in one signal
element. The value of r in analog transmission is $r = \log_2 L$, where L is the number of
different signal elements. The same nomenclature is used to simplify the comparisons.

Bit rate is the number of bits per second. Baud rate is the number of signal
elements per second. In the analog transmission of digital data,
the baud rate is less than or equal to the bit rate.

The same analogy we used in Chapter 4 for bit rate and baud rate applies here. In
transportation, a baud is analogous to a vehicle, and a bit is analogous to a passenger.
We need to maximize the number of people per car to reduce the traffic.

##### Example 5.1
> id: ch05-example-5-1 | src: book Example 5.1 | kind: worked_example
An analog signal carries 4 bits per signal element. If 1000 signal elements are sent per second,
find the bit rate.

**Solution**
In this case, r = 4, S = 1000, and N is unknown. We can find the value of N from
$$S = N\left(\frac{1}{r}\right) \quad\text{or}\quad N = Sr = 1000(4) = 4000\ \text{bps}$$

##### Example 5.2
> id: ch05-example-5-2 | src: book Example 5.2 | kind: worked_example
An analog signal has a bit rate of 8000 bps and a baud rate of 1000 baud. How many data elements
are carried by each signal element? How many signal elements do we need?

**Solution**
In this example, S = 1000, N = 8000, and r and L are unknown. We first find the value of r and
then the value of L.
$$S = N\left(\frac{1}{r}\right) \;\Rightarrow\; r = \frac{N}{S} = \frac{8000}{1000} = 8\ \text{bits/baud}$$\n\n$$r = \log_2 L \;\Rightarrow\; L = 2^r = 2^8 = 256$$

#### Bandwidth
> id: ch05-5-1-1-bandwidth | src: book p.138 | kind: concept

The required bandwidth for analog transmission of digital data is proportional to the
signal rate except for FSK, in which the difference between the carrier signals needs to
be added. We discuss the bandwidth for each technique.

#### Carrier Signal
> id: ch05-5-1-1-carrier-signal | src: book p.138 | kind: concept

In analog transmission, the sending device produces a high-frequency signal that acts
as a base for the information signal. This base signal is called the carrier signal or carrier frequency. The receiving device is tuned to the frequency of the carrier signal that it
expects from the sender. Digital information then changes the carrier signal by modifying one or more of its characteristics (amplitude, frequency, or phase). This kind of
modification is called modulation (shift keying).

### 5.1.2 Amplitude Shift Keying
> id: ch05-5-1-2 | src: book 5.1.2; p.138 | kind: concept

In amplitude shift keying, the amplitude of the carrier signal is varied to create signal
elements. Both frequency and phase remain constant while the amplitude changes.

#### Binary ASK (BASK)
> id: ch05-5-1-2-binary-ask-bask | src: book p.138 | kind: concept

Although we can have several levels (kinds) of signal elements, each with a different
amplitude, ASK is normally implemented using only two levels. This is referred to as
binary amplitude shift keying or on-off keying (OOK). The peak amplitude of one signal
level is 0; the other is the same as the amplitude of the carrier frequency. Figure 5.3
gives a conceptual view of binary ASK.

> **[ASSET ch05_ill_003]** Figure 5.3: Binary amplitude shift keying
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_003.png
> - src: book Figure 5.3; p.138
> - shows: Figure 5.3: Binary amplitude shift keying. Aligned panels show the input bits, the on-off keyed carrier, five one-second signal elements, and the centered frequency spectrum. The annotations connect r = 1, S = N, and B = (1 + d)S.
> - structure: Aligned panels show the input bits, the on-off keyed carrier, five one-second signal elements, and the centered frequency spectrum. The annotations connect r = 1, S = N, and B = (1 + d)S.
> - text_in_image: Amplitude; Bit rate: 5; 1; 0; 1; 1; 0; r = 1; B = (1 + d)S; S = N; Bandwidth; Time; 1 signal; 1 signal; 1 signal; 1 signal; 1 signal; element; element; element; element; element; 0; 1 s; 0; fc; Baud rate: 5
> - use_when: Teach ch05-5-1-2-binary-ask-bask, interpret Figure 5.3, compare modulation methods, or support a linked practice question.
> - confidence: high

#### Bandwidth for ASK
> id: ch05-5-1-2-bandwidth-for-ask | src: book p.138 | kind: concept

Figure 5.3 also shows the bandwidth for ASK. Although the carrier signal is only one
simple sine wave, the process of modulation produces a nonperiodic composite signal.
This signal, as was discussed in Chapter 3, has a continuous set of frequencies. As we
expect, the bandwidth is proportional to the signal rate (baud rate). However, there is
normally another factor involved, called d, which depends on the modulation and filtering process. The value of d is between 0 and 1. This means that the bandwidth can be
expressed as shown, where S is the signal rate and the B is the bandwidth.

$$B = (1+d)S$$
The formula shows that the required bandwidth has a minimum value of S and a
maximum value of 2S. The most important point here is the location of the bandwidth. The middle of the bandwidth is where $f_{c}$, the carrier frequency, is located. This
means if we have a bandpass channel available, we can choose our $f_{c}$ so that the modulated signal occupies that bandwidth. This is in fact the most important advantage of
digital-to-analog conversion. We can shift the resulting bandwidth to match what is
available.

#### Implementation
> id: ch05-5-1-2-implementation | src: book p.139 | kind: concept

The complete discussion of ASK implementation is beyond the scope of this book.
However, the simple ideas behind the implementation may help us to better understand
the concept itself. Figure 5.4 shows how we can simply implement binary ASK.

> **[ASSET ch05_ill_004]** Figure 5.4: Implementation of binary ASK
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_004.png
> - src: book Figure 5.4; p.139
> - shows: Figure 5.4: Implementation of binary ASK. A unipolar NRZ bit stream and a carrier oscillator feed a multiplier. The output preserves the carrier for bit 1 and suppresses it for bit 0, producing binary ASK.
> - structure: A unipolar NRZ bit stream and a carrier oscillator feed a multiplier. The output preserves the carrier for bit 1 and suppresses it for bit 0, producing binary ASK.
> - text_in_image: 1; 0; 1; 1; 0; Multiplier; Carrier signal; fc; Modulated signal; Oscillator
> - use_when: Teach ch05-5-1-2-implementation, interpret Figure 5.4, compare modulation methods, or support a linked practice question.
> - confidence: high

If digital data are presented as a unipolar NRZ (see Chapter 4) digital signal with a
high voltage of 1 V and a low voltage of 0 V, the implementation can achieved by
multiplying the NRZ digital signal by the carrier signal coming from an oscillator.
When the amplitude of the NRZ signal is 1, the amplitude of the carrier frequency is
held; when the amplitude of the NRZ signal is 0, the amplitude of the carrier frequency
is zero.

##### Example 5.3
> id: ch05-example-5-3 | src: book Example 5.3 | kind: worked_example
We have an available bandwidth of 100 kHz which spans from 200 to 300 kHz. What are the carrier frequency and the bit rate if we modulated our data by using ASK with d = 1?

**Solution**
The middle of the bandwidth is located at 250 kHz. This means that our carrier frequency can be
at $f_{c}$ = 250 kHz. We can use the formula for bandwidth to find the bit rate (with d = 1 and r = 1).
$$B=(1+d)S=2N\left(\frac{1}{r}\right)=2N=100\ \text{kHz}\;\Rightarrow\;N=50\ \text{kbps}$$

##### Example 5.4
> id: ch05-example-5-4 | src: book Example 5.4 | kind: worked_example
In data communications, we normally use full-duplex links with communication in both directions. We need to divide the bandwidth into two with two carrier frequencies, as shown in
Figure 5.5. The figure shows the positions of two carrier frequencies and the bandwidths. The
available bandwidth for each direction is now 50 kHz, which leaves us with a data rate of 25 kbps
in each direction.

> **[ASSET ch05_ill_005]** Figure 5.5: Bandwidth of full-duplex ASK used in Example 5.4
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_005.png
> - src: book Figure 5.5; p.140
> - shows: Figure 5.5: Bandwidth of full-duplex ASK used in Example 5.4. The 200-to-300 kHz channel is divided into two 50 kHz bands centered at 225 and 275 kHz, supporting simultaneous ASK transmission in opposite directions.
> - structure: The 200-to-300 kHz channel is divided into two 50 kHz bands centered at 225 and 275 kHz, supporting simultaneous ASK transmission in opposite directions.
> - text_in_image: B = 50 kHz; B = 50 kHz; fc1; fc2; 200; 300; (225); (275)
> - use_when: Teach ch05-example-5-4, interpret Figure 5.5, compare modulation methods, or support a linked practice question.
> - confidence: high

#### Multilevel ASK
> id: ch05-5-1-2-multilevel-ask | src: book p.140 | kind: concept

The above discussion uses only two amplitude levels. We can have multilevel ASK in
which there are more than two levels. We can use 4, 8, 16, or more different amplitudes
for the signal and modulate the data using 2, 3, 4, or more bits at a time. In these cases,
r = 2, r = 3, r = 4, and so on. Although this is not implemented with pure ASK, it is
implemented with QAM (as we will see later).

### 5.1.3 Frequency Shift Keying
> id: ch05-5-1-3 | src: book 5.1.3; p.140 | kind: concept

In frequency shift keying, the frequency of the carrier signal is varied to represent data.
The frequency of the modulated signal is constant for the duration of one signal element, but changes for the next signal element if the data element changes. Both peak
amplitude and phase remain constant for all signal elements.

#### Binary FSK (BFSK)
> id: ch05-5-1-3-binary-fsk-bfsk | src: book p.140 | kind: concept

One way to think about binary FSK (or BFSK) is to consider two carrier frequencies. In
Figure 5.6, we have selected two carrier frequencies, $f_{1}$ and $f_{2}$. We use the first carrier if
the data element is 0; we use the second if the data element is 1. However, note that this
is an unrealistic example used only for demonstration purposes. Normally the carrier
frequencies are very high, and the difference between them is very small.

> **[ASSET ch05_ill_006]** Figure 5.6: Binary frequency shift keying
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_006.png
> - src: book Figure 5.6; p.140
> - shows: Figure 5.6: Binary frequency shift keying. The same bit stream selects between two carrier frequencies f1 and f2. Two adjacent spectra are separated by 2Δf, and the diagram states B = (1 + d)S + 2Δf with r = 1 and S = N.
> - structure: The same bit stream selects between two carrier frequencies f1 and f2. Two adjacent spectra are separated by 2Δf, and the diagram states B = (1 + d)S + 2Δf with r = 1 and S = N.
> - text_in_image: Amplitude; r = 1; S = N; B = (1 + d)S + 2Δf; Bit rate: 5; 1; 0; 1; 1; 0; B = S(1 + d) + 2Δf; S(1 + d); S(1 + d); Time; 1 signal; 1 signal; 1 signal; 1 signal; 1 signal; element; element; element; element; element; 0; 0; f1; f2; 1 s; Baud rate: 5; 2Δf
> - use_when: Teach ch05-5-1-3-binary-fsk-bfsk, interpret Figure 5.6, compare modulation methods, or support a linked practice question.
> - confidence: high

As Figure 5.6 shows, the middle of one bandwidth is $f_{1}$ and the middle of the other
is $f_{2}$. Both $f_{1}$ and $f_{2}$ are Δf apart from the midpoint between the two bands. The difference between the two frequencies is 2Δf.

#### Bandwidth for BFSK
> id: ch05-5-1-3-bandwidth-for-bfsk | src: book p.141 | kind: concept

Figure 5.6 also shows the bandwidth of FSK. Again the carrier signals are only simple
sine waves, but the modulation creates a nonperiodic composite signal with continuous
frequencies. We can think of FSK as two ASK signals, each with its own carrier frequency ( $f_{1}$ or $f_{2}$). If the difference between the two frequencies is 2Δf, then the required
bandwidth is
$$B = (1+d)S + 2\Delta f$$

What should be the minimum value of 2Δf? In Figure 5.6, we have chosen a value
greater than (1 + d )S. It can be shown that the minimum value should be at least S for
the proper operation of modulation and demodulation.

##### Example 5.5
> id: ch05-example-5-5 | src: book Example 5.5 | kind: worked_example
We have an available bandwidth of 100 kHz which spans from 200 to 300 kHz. What should be
the carrier frequency and the bit rate if we modulated our data by using FSK with d = 1?

**Solution**
This problem is similar to Example 5.3, but we are modulating by using FSK. The midpoint of
the band is at 250 kHz. We choose 2Δf to be 50 kHz; this means
$$B=(1+d)S+2\Delta f=100\ \text{kHz}\;\Rightarrow\;2S=50\ \text{kHz}\;\Rightarrow\;S=25\ \text{kbaud}\;\Rightarrow\;N=25\ \text{kbps}$$

Compared to Example 5.3, we can see the bit rate for ASK is 50 kbps while the bit rate for FSK
is 25 kbps.

#### Implementation
> id: ch05-5-1-3-implementation | src: book p.141 | kind: concept

There are two implementations of BFSK: noncoherent and coherent. In noncoherent
BFSK, there may be discontinuity in the phase when one signal element ends and the
next begins. In coherent BFSK, the phase continues through the boundary of two signal
elements. Noncoherent BFSK can be implemented by treating BFSK as two ASK modulations and using two carrier frequencies. Coherent BFSK can be implemented by
using one voltage-controlled oscillator (VCO) that changes its frequency according to
the input voltage. Figure 5.7 shows the simplified idea behind the second implementation. The input to the oscillator is the unipolar NRZ signal. When the amplitude of NRZ
is zero, the oscillator keeps its regular frequency; when the amplitude is positive, the
frequency is increased.

#### Multilevel FSK
> id: ch05-5-1-3-multilevel-fsk | src: book p.141 | kind: concept

Multilevel modulation (MFSK) is not uncommon with the FSK method. We can use
more than two frequencies. For example, we can use four different frequencies $f_{1}$, $f_{2}$, $f_{3}$,
and $f_{4}$ to send 2 bits at a time. To send 3 bits at a time, we can use eight frequencies.
And so on. However, we need to remember that the frequencies need to be 2Δf apart.
For the proper operation of the modulator and demodulator, it can be shown that the
minimum value of 2Δf needs to be S. We can show that the bandwidth is

$$B=(1+d)S+(L-1)2\Delta f \;\Rightarrow\; B=LS$$

> **[ASSET ch05_ill_007]** Figure 5.7: Implementation of BFSK
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_007.png
> - src: book Figure 5.7; p.142
> - shows: Figure 5.7: Implementation of BFSK. A unipolar NRZ input controls a voltage-controlled oscillator. Low and high input levels select the two BFSK frequencies while preserving a continuous phase in the coherent implementation.
> - structure: A unipolar NRZ input controls a voltage-controlled oscillator. Low and high input levels select the two BFSK frequencies while preserving a continuous phase in the coherent implementation.
> - text_in_image: 1; 0; 1; 1; 0; VCO; Voltage-controlled; oscillator
> - use_when: Teach ch05-5-1-3-multilevel-fsk, interpret Figure 5.7, compare modulation methods, or support a linked practice question.
> - confidence: high

Note that MFSK uses more bandwidth than the other techniques; it should be used
when noise is a serious issue.

##### Example 5.6
> id: ch05-example-5-6 | src: book Example 5.6 | kind: worked_example
We need to send data 3 bits at a time at a bit rate of 3 Mbps. The carrier frequency is 10 MHz.
Calculate the number of levels (different frequencies), the baud rate, and the bandwidth.

**Solution**
We can have L = $2^{3}$ = 8. The baud rate is S = 3 MHz/3 = 1 Mbaud. This means that the carrier frequencies must be 1 MHz apart (2Δf  = 1 MHz). The bandwidth is B = 8 × 1 = 8 MHz. Figure 5.8
shows the allocation of frequencies and bandwidth.

> **[ASSET ch05_ill_008]** Figure 5.8: Bandwidth of MFSK used in Example 5.6
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_008.png
> - src: book Figure 5.8; p.142
> - shows: Figure 5.8: Bandwidth of MFSK used in Example 5.6. Eight 1 MHz-wide MFSK bands are arranged from 6.5 to 13.5 MHz around a 10 MHz center. Their total occupied bandwidth is 8 MHz.
> - structure: Eight 1 MHz-wide MFSK bands are arranged from 6.5 to 13.5 MHz around a 10 MHz center. Their total occupied bandwidth is 8 MHz.
> - text_in_image: Bandwidth = 8 MHz; f1; f2; f3; f4; fc; f5; f6; f7; f8; 6.5; 7.5; 8.5; 9.5; 10.5; 11.5; 12.5; 13.5; 10; MHz; MHz; MHz; MHz; MHz; MHz; MHz; MHz; MHz
> - use_when: Teach ch05-example-5-6, interpret Figure 5.8, compare modulation methods, or support a linked practice question.
> - confidence: high

### 5.1.4 Phase Shift Keying
> id: ch05-5-1-4 | src: book 5.1.4; p.142 | kind: concept

In phase shift keying, the phase of the carrier is varied to represent two or more different signal elements. Both peak amplitude and frequency remain constant as the phase
changes. Today, PSK is more common than ASK or FSK. However, we will see shortly
that QAM, which combines ASK and PSK, is the dominant method of digital-to-analog
modulation.

#### Binary PSK (BPSK)
> id: ch05-5-1-4-binary-psk-bpsk | src: book p.142 | kind: concept

The simplest PSK is binary PSK, in which we have only two signal elements, one with
a phase of 0°, and the other with a phase of 180°. Figure 5.9 gives a conceptual view
of PSK. Binary PSK is as simple as binary ASK with one big advantage—it is less
susceptible to noise. In ASK, the criterion for bit detection is the amplitude of the

> **[ASSET ch05_ill_009]** Figure 5.9: Binary phase shift keying
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_009.png
> - src: book Figure 5.9; p.143
> - shows: Figure 5.9: Binary phase shift keying. Aligned panels show a five-bit input, the binary phase-shift-keyed carrier, signal-element boundaries, and its centered spectrum. The annotations connect r = 1, S = N, and B = (1 + d)S.
> - structure: Aligned panels show a five-bit input, the binary phase-shift-keyed carrier, signal-element boundaries, and its centered spectrum. The annotations connect r = 1, S = N, and B = (1 + d)S.
> - text_in_image: Bit rate: 5; Amplitude; r = 1; S = N; B = (1 + d)S; 1; 0; 1; 1; 0; Bandwidth; Time; 1 signal; 1 signal; 1 signal; 1 signal; 1 signal; element; element; element; element; element; 0; 0; 1 s; fc; Baud rate: 5
> - use_when: Teach ch05-5-1-4-binary-psk-bpsk, interpret Figure 5.9, compare modulation methods, or support a linked practice question.
> - confidence: high

signal; in PSK, it is the phase. Noise can change the amplitude easier than it can change
the phase. In other words, PSK is less susceptible to noise than ASK. PSK is superior to
FSK because we do not need two carrier signals. However, PSK needs more sophisticated hardware to be able to distinguish between phases.

#### Bandwidth
> id: ch05-5-1-4-bandwidth | src: book p.143 | kind: concept

Figure 5.9 also shows the bandwidth for BPSK. The bandwidth is the same as that for
binary ASK, but less than that for BFSK. No bandwidth is wasted for separating two
carrier signals.

#### Implementation
> id: ch05-5-1-4-implementation | src: book p.143 | kind: concept

The implementation of BPSK is as simple as that for ASK. The reason is that the signal
element with phase 180° can be seen as the complement of the signal element with
phase 0°. This gives us a clue on how to implement BPSK. We use the same idea we
used for ASK but with a polar NRZ signal instead of a unipolar NRZ signal, as shown
in Figure 5.10. The polar NRZ signal is multiplied by the carrier frequency; the 1 bit
(positive voltage) is represented by a phase starting at 0°; the 0 bit (negative voltage) is
represented by a phase starting at 180°.

> **[ASSET ch05_ill_010]** Figure 5.10: BPSK multiplier implementation (source caption: Implementation of BASK)
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_010.png
> - src: book Figure 5.10; p.143
> - shows: Figure 5.10: BPSK multiplier implementation (source caption: Implementation of BASK). A polar NRZ waveform and a carrier oscillator feed a multiplier. Positive and negative input levels produce carrier phases separated by 180 degrees, implementing BPSK; the book caption itself says BASK.
> - structure: A polar NRZ waveform and a carrier oscillator feed a multiplier. Positive and negative input levels produce carrier phases separated by 180 degrees, implementing BPSK; the book caption itself says BASK.
> - text_in_image: 1; 0; 1; 1; 0; Multiplier; Carrier signal; fc; Modulated signal; Oscillator
> - use_when: Teach ch05-5-1-4-implementation, interpret Figure 5.10, compare modulation methods, or support a linked practice question.
> - confidence: high

#### Quadrature PSK (QPSK)
> id: ch05-5-1-4-quadrature-psk-qpsk | src: book p.143 | kind: concept

The simplicity of BPSK enticed designers to use 2 bits at a time in each signal element,
thereby decreasing the baud rate and eventually the required bandwidth. The scheme is
called quadrature PSK or QPSK because it uses two separate BPSK modulations; one
is in-phase, the other quadrature (out-of-phase). The incoming bits are first passed
through a serial-to-parallel conversion that sends one bit to one modulator and the next
bit to the other modulator. If the duration of each bit in the incoming signal is T, the
duration of each bit sent to the corresponding BPSK signal is 2T. This means that the
bit to each BPSK signal has one-half the frequency of the original signal. Figure 5.11
shows the idea.

> **[ASSET ch05_ill_011]** Figure 5.11: QPSK and its implementation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_011.png
> - src: book Figure 5.11; p.144
> - shows: Figure 5.11: QPSK and its implementation. A serial bit stream is split into odd and even branches, each branch modulates a carrier, and a 90-degree phase shift makes the two carriers orthogonal. Their sum produces four QPSK phases and the associated bit pairs.
> - structure: A serial bit stream is split into odd and even branches, each branch modulates a carrier, and a 90-degree phase shift makes the two carriers orthogonal. Their sum produces four QPSK phases and the associated bit pairs.
> - text_in_image: 0 0; 1 0; 0 1; 1 1; 0; 1; 0; 1; 2/1; Oscillator; 0; 0; 1; 1; S; converter; 90°; –135; –45; 135; 45
> - use_when: Teach ch05-5-1-4-quadrature-psk-qpsk, interpret Figure 5.11, compare modulation methods, or support a linked practice question.
> - confidence: high

The two composite signals created by each multiplier are sine waves with the same
frequency, but different phases. When they are added, the result is another sine wave,
with one of four possible phases: 45°, −45°, 135°, and −135°. There are four kinds of
signal elements in the output signal (L = 4), so we can send 2 bits per signal element (r = 2).

##### Example 5.7
> id: ch05-example-5-7 | src: book Example 5.7 | kind: worked_example
Find the bandwidth for a signal transmitting at 12 Mbps for QPSK. The value of d = 0.

**Solution**
For QPSK, 2 bits are carried by one signal element. This means that r = 2. So the signal rate
(baud rate) is S = N × (1/r) = 6 Mbaud. With a value of d = 0, we have B = S = 6 MHz.

#### Constellation Diagram
> id: ch05-5-1-4-constellation-diagram | src: book p.144 | kind: concept

A constellation diagram can help us define the amplitude and phase of a signal element,
particularly when we are using two carriers (one in-phase and one quadrature). The
diagram is useful when we are dealing with multilevel ASK, PSK, or QAM (see next
section). In a constellation diagram, a signal element type is represented as a dot. The
bit or combination of bits it can carry is often written next to it.
The diagram has two axes. The horizontal X axis is related to the in-phase carrier;
the vertical Y axis is related to the quadrature carrier. For each point on the diagram,
four pieces of information can be deduced. The projection of the point on the X axis
defines the peak amplitude of the in-phase component; the projection of the point on
the Y axis defines the peak amplitude of the quadrature component. The length of the
line (vector) that connects the point to the origin is the peak amplitude of the signal
element (combination of the X and Y components); the angle the line makes with the
X axis is the phase of the signal element. All the information we need can easily be found
on a constellation diagram. Figure 5.12 shows a constellation diagram.

> **[ASSET ch05_ill_012]** Figure 5.12: Concept of a constellation diagram
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_012.png
> - src: book Figure 5.12; p.145
> - shows: Figure 5.12: Concept of a constellation diagram. A constellation point is projected onto the in-phase X axis and quadrature Y axis. The projections give I and Q amplitudes, while the vector length and angle give the signal amplitude and phase.
> - structure: A constellation point is projected onto the in-phase X axis and quadrature Y axis. The projections give I and Q amplitudes, while the vector length and angle give the signal amplitude and phase.
> - text_in_image: Y (Quadrature carrier); Length: amplitude; Q component; Amplitude of; Angle: phase; X (In-phase carrier); Amplitude of; I component
> - use_when: Teach ch05-5-1-4-constellation-diagram, interpret Figure 5.12, compare modulation methods, or support a linked practice question.
> - confidence: high

##### Example 5.8
> id: ch05-example-5-8 | src: book Example 5.8 | kind: worked_example
Show the constellation diagrams for ASK (OOK), BPSK, and QPSK signals.

**Solution**
Figure 5.13 shows the three constellation diagrams. Let us analyze each case separately:

> **[ASSET ch05_ill_013]** Figure 5.13: Three constellation diagrams
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_013.png
> - src: book Figure 5.13; p.145
> - shows: Figure 5.13: Three constellation diagrams. Three coordinate plots compare OOK with points at zero and positive I, BPSK with symmetric I-axis points, and QPSK with four equal-radius points in the four quadrants.
> - structure: Three coordinate plots compare OOK with points at zero and positive I, BPSK with symmetric I-axis points, and QPSK with four equal-radius points in the four quadrants.
> - text_in_image: 01; 11; 0; 0; 1; 1; 00; 10; ASK (OOK); BPSK; QPSK
> - use_when: Teach ch05-example-5-8, interpret Figure 5.13, compare modulation methods, or support a linked practice question.
> - confidence: high

- For ASK, we are using only an in-phase carrier. Therefore, the two points should be on the
X axis. Binary 0 has an amplitude of 0 V; binary 1 has an amplitude of 1 V (for example).
The points are located at the origin and at 1 unit.
- BPSK also uses only an in-phase carrier. However, we use a polar NRZ signal for modulation. It creates two types of signal elements, one with amplitude 1 and the other with
amplitude −1. This can be stated in other words: BPSK creates two different signal
elements, one with amplitude 1 V and in phase and the other with amplitude 1 V and 180°
out of phase.
- QPSK uses two carriers, one in-phase and the other quadrature. The point representing 11 is
made of two combined signal elements, both with an amplitude of 1 V. One element is represented by an in-phase carrier, the other element by a quadrature carrier. The amplitude of
the final signal element sent for this 2-bit data element is $\sqrt{2}$, and the phase is 45°. The
argument is similar for the other three points. All signal elements have an amplitude of $\sqrt{2}$,
but their phases are different (45°, 135°, −135°, and −45°). Of course, we could have chosen
the amplitude of the carrier to be $1/\sqrt{2}$ to make the final amplitudes 1 V.

### 5.1.5 Quadrature Amplitude Modulation
> id: ch05-5-1-5 | src: book 5.1.5; p.146 | kind: concept

PSK is limited by the ability of the equipment to distinguish small differences in phase.
This factor limits its potential bit rate. So far, we have been altering only one of the
three characteristics of a sine wave at a time; but what if we alter two? Why not combine
ASK and PSK? The idea of using two carriers, one in-phase and the other quadrature,
with different amplitude levels for each carrier is the concept behind quadrature
amplitude modulation (QAM).

Quadrature amplitude modulation is a combination of ASK and PSK.

The possible variations of QAM are numerous. Figure 5.14 shows some of these
schemes. Figure 5.14a shows the simplest 4-QAM scheme (four different signal element types) using a unipolar NRZ signal to modulate each carrier. This is the same
mechanism we used for ASK (OOK). Part b shows another 4-QAM using polar NRZ,
but this is exactly the same as QPSK. Part c shows another QAM-4 in which we used a
signal with two positive levels to modulate each of the two carriers. Finally, Figure 5.14d
shows a 16-QAM constellation of a signal with eight levels, four positive and four
negative.

> **[ASSET ch05_ill_014]** Figure 5.14: Constellation diagrams for some QAMs
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_014.png
> - src: book Figure 5.14; p.146
> - shows: Figure 5.14: Constellation diagrams for some QAMs. Four constellation plots compare three 4-QAM arrangements and one 16-QAM grid, showing how different I/Q amplitude choices create the same or larger number of signal points.
> - structure: Four constellation plots compare three 4-QAM arrangements and one 16-QAM grid, showing how different I/Q amplitude choices create the same or larger number of signal points.
> - text_in_image: a. 4-QAM; b. 4-QAM; c. 4-QAM; d. 16-QAM
> - use_when: Teach ch05-5-1-5, interpret Figure 5.14, compare modulation methods, or support a linked practice question.
> - confidence: high

#### Bandwidth for QAM
> id: ch05-5-1-5-bandwidth-for-qam | src: book p.147 | kind: concept

The minimum bandwidth required for QAM transmission is the same as that required
for ASK and PSK transmission. QAM has the same advantages as PSK over ASK.

## 5.2 ANALOG-TO-ANALOG CONVERSION
> id: ch05-5-2 | src: book 5.2; p.147 | kind: concept

Analog-to-analog conversion, or analog modulation, is the representation of analog
information by an analog signal. One may ask why we need to modulate an analog signal; it is already analog. Modulation is needed if the medium is bandpass in nature or if
only a bandpass channel is available to us. An example is radio. The government assigns
a narrow bandwidth to each radio station. The analog signal produced by each station is
a low-pass signal, all in the same range. To be able to listen to different stations, the
low-pass signals need to be shifted, each to a different range.
Analog-to-analog conversion can be accomplished in three ways: amplitude
modulation (AM), frequency modulation (FM), and phase modulation (PM). FM
and PM are usually categorized together. See Figure 5.15.

> **[ASSET ch05_ill_015]** Figure 5.15: Types of analog-to-analog modulation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_015.png
> - src: book Figure 5.15; p.147
> - shows: Figure 5.15: Types of analog-to-analog modulation. A classification tree branches analog-to-analog conversion into amplitude modulation, frequency modulation, and phase modulation.
> - structure: A classification tree branches analog-to-analog conversion into amplitude modulation, frequency modulation, and phase modulation.
> - text_in_image: Analog-to-analog; conversion; Amplitude modulation; Frequency modulation; Phase modulation
> - use_when: Teach ch05-5-2, interpret Figure 5.15, compare modulation methods, or support a linked practice question.
> - confidence: high

### 5.2.1 Amplitude Modulation (AM)
> id: ch05-5-2-1 | src: book 5.2.1; p.147 | kind: concept

In AM transmission, the carrier signal is modulated so that its amplitude varies with the
changing amplitudes of the modulating signal. The frequency and phase of the carrier
remain the same; only the amplitude changes to follow variations in the information.
Figure 5.16 shows how this concept works. The modulating signal is the envelope of
the carrier.  As Figure 5.16 shows, AM is normally implemented by using a simple
multiplier because the amplitude of the carrier signal needs to be changed according to
the amplitude of the modulating signal.

#### AM Bandwidth
> id: ch05-5-2-1-am-bandwidth | src: book p.147 | kind: concept

Figure 5.16 also shows the bandwidth of an AM signal. The modulation creates a bandwidth that is twice the bandwidth of the modulating signal and covers a range centered
on the carrier frequency. However, the signal components above and below the carrier
frequency carry exactly the same information. For this reason, some implementations
discard one-half of the signals and cut the bandwidth in half.

> **[ASSET ch05_ill_016]** Figure 5.16: Amplitude modulation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_016.png
> - src: book Figure 5.16; p.148
> - shows: Figure 5.16: Amplitude modulation. An audio waveform multiplies a sinusoidal carrier to form an AM waveform whose envelope follows the audio. A spectrum centered at fc spans B_AM = 2B.
> - structure: An audio waveform multiplies a sinusoidal carrier to form an AM waveform whose envelope follows the audio. A spectrum centered at fc spans B_AM = 2B.
> - text_in_image: Modulating signal; Multiplier; Carrier frequency; fc; Oscillator; Modulated signal; BAM = 2B; 0; fc
> - use_when: Teach ch05-5-2-1-am-bandwidth, interpret Figure 5.16, compare modulation methods, or support a linked practice question.
> - confidence: high

The total bandwidth required for AM can be determined
from the bandwidth of the audio signal: $B_{\mathrm{AM}}=2B$.

#### Standard Bandwidth Allocation for AM Radio
> id: ch05-5-2-1-standard-bandwidth-allocation-for-am-radio | src: book p.148 | kind: concept

The bandwidth of an audio signal (speech and music) is usually 5 kHz. Therefore, an
AM radio station needs a bandwidth of 10 kHz. In fact, the Federal Communications
Commission (FCC) allows 10 kHz for each AM station.
AM stations are allowed carrier frequencies anywhere between 530 and 1700 kHz
(1.7 MHz). However, each station’s carrier frequency must be separated from those on
either side of it by at least 10 kHz (one AM bandwidth) to avoid interference. If one
station uses a carrier frequency of 1100 kHz, the next station’s carrier frequency cannot
be lower than 1110 kHz (see Figure 5.17).

> **[ASSET ch05_ill_017]** Figure 5.17: AM band allocation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_017.png
> - src: book Figure 5.17; p.148
> - shows: Figure 5.17: AM band allocation. Carrier frequencies are placed at 10 kHz intervals across the 530-to-1700 kHz AM broadcast band; each station occupies one 10 kHz channel.
> - structure: Carrier frequencies are placed at 10 kHz intervals across the 530-to-1700 kHz AM broadcast band; each station occupies one 10 kHz channel.
> - text_in_image: fc; fc; fc; fc; fc; • • •; 530; 1700; 10 kHz; kHz; kHz
> - use_when: Teach ch05-5-2-1-standard-bandwidth-allocation-for-am-radio, interpret Figure 5.17, compare modulation methods, or support a linked practice question.
> - confidence: high

### 5.2.2 Frequency Modulation (FM)
> id: ch05-5-2-2 | src: book 5.2.2; p.148 | kind: concept

In FM transmission, the frequency of the carrier signal is modulated to follow the changing voltage level (amplitude) of the modulating signal. The peak amplitude and phase of
the carrier signal remain constant, but as the amplitude of the information signal
changes, the frequency of the carrier changes correspondingly. Figure 5.18 shows the
relationships of the modulating signal, the carrier signal, and the resultant FM signal.
As Figure 5.18 shows, FM is normally implemented by using a voltage-controlled
oscillator as with FSK. The frequency of the oscillator changes according to the input
voltage which is the amplitude of the modulating signal.

#### FM Bandwidth
> id: ch05-5-2-2-fm-bandwidth | src: book p.149 | kind: concept

Figure 5.18 also shows the bandwidth of an FM signal. The actual bandwidth is difficult to determine exactly, but it can be shown empirically that it is several times that
of the analog signal or 2(1 + β)B where β is a factor that depends on modulation technique with a common value of 4.

The total bandwidth required for FM can be determined from
the bandwidth of the audio signal: $B_{\mathrm{FM}}=2(1+\beta)B$.

> **[ASSET ch05_ill_018]** Figure 5.18: Frequency modulation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_018.png
> - src: book Figure 5.18; p.149
> - shows: Figure 5.18: Frequency modulation. The audio amplitude controls a voltage-controlled oscillator, changing the instantaneous frequency of the FM waveform while its amplitude stays constant. The spectrum states B_FM = 2(1 + β)B.
> - structure: The audio amplitude controls a voltage-controlled oscillator, changing the instantaneous frequency of the FM waveform while its amplitude stays constant. The spectrum states B_FM = 2(1 + β)B.
> - text_in_image: Amplitude; Modulating signal (audio); Time; Carrier frequency; VCO; Voltage-controlled; oscillator; Time; BFM = 2(1 + β)B; FM signal; 0; fc; Time
> - use_when: Teach ch05-5-2-2-fm-bandwidth, interpret Figure 5.18, compare modulation methods, or support a linked practice question.
> - confidence: high

#### Standard Bandwidth Allocation for FM Radio
> id: ch05-5-2-2-standard-bandwidth-allocation-for-fm-radio | src: book p.149 | kind: concept

The bandwidth of an audio signal (speech and music) broadcast in stereo is almost
15 kHz. The FCC allows 200 kHz (0.2 MHz) for each station. This mean β = 4 with
some extra guard band. FM stations are allowed carrier frequencies anywhere between
88 and 108 MHz. Stations must be separated by at least 200 kHz to keep their bandwidths from overlapping. To create even more privacy, the FCC requires that in a given
area, only alternate bandwidth allocations may be used. The others remain unused to prevent any possibility of two stations interfering with each other. Given 88 to 108 MHz as
a range, there are 100 potential FM bandwidths in an area, of which 50 can operate at
any one time. Figure 5.19 illustrates this concept.

### 5.2.3 Phase Modulation (PM)
> id: ch05-5-2-3 | src: book 5.2.3; p.149 | kind: concept

In PM transmission, the phase of the carrier signal is modulated to follow the changing
voltage level (amplitude) of the modulating signal. The peak amplitude and frequency

> **[ASSET ch05_ill_019]** Figure 5.19: FM band allocation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_019.png
> - src: book Figure 5.19; p.150
> - shows: Figure 5.19: FM band allocation. Potential FM carriers are spaced by 200 kHz across 88-to-108 MHz, with alternating slots marked as having no station to reduce adjacent-channel interference.
> - structure: Potential FM carriers are spaced by 200 kHz across 88-to-108 MHz, with alternating slots marked as having no station to reduce adjacent-channel interference.
> - text_in_image: fc; fc; fc; fc; No; No; • • •; station; station; 88; 108; MHz; 200 kHz; MHz
> - use_when: Teach ch05-5-2-3, interpret Figure 5.19, compare modulation methods, or support a linked practice question.
> - confidence: high

of the carrier signal remain constant, but as the amplitude of the information signal
changes, the phase of the carrier changes correspondingly. It can be proved mathematically (see Appendix E) that PM is the same as FM with one difference. In FM, the
instantaneous change in the carrier frequency is proportional to the amplitude of the
modulating signal; in PM the instantaneous change in the carrier frequency is proportional to the derivative of the amplitude of the modulating signal. Figure 5.20 shows
the relationships of the modulating signal, the carrier signal, and the resultant PM
signal.

> **[ASSET ch05_ill_020]** Figure 5.20: Phase modulation
> - type: illustration
> - kind: diagram
> - file: assets/ch05_ill_020.png
> - src: book Figure 5.20; p.150
> - shows: Figure 5.20: Phase modulation. The derivative of the audio waveform drives a voltage-controlled oscillator, producing phase modulation. The spectrum states B_PM = 2(1 + β)B.
> - structure: The derivative of the audio waveform drives a voltage-controlled oscillator, producing phase modulation. The spectrum states B_PM = 2(1 + β)B.
> - text_in_image: Amplitude; Modulating signal (audio); VCO; Time; Carrier frequency; d/dt; Time; BPM = 2(1 + β)B; PM signal; Time; 0; fc
> - use_when: Teach ch05-5-2-3, interpret Figure 5.20, compare modulation methods, or support a linked practice question.
> - confidence: high

As Figure 5.20 shows, PM is normally implemented by using a voltage-controlled
oscillator along with a derivative. The frequency of the oscillator changes according to
the derivative of the input voltage, which is the amplitude of the modulating signal.

#### PM Bandwidth
> id: ch05-5-2-3-pm-bandwidth | src: book p.150 | kind: concept

Figure 5.20 also shows the bandwidth of a PM signal. The actual bandwidth is difficult to determine exactly, but it can be shown empirically that it is several times that
of the analog signal. Although the formula shows the same bandwidth for FM and
PM, the value of β is lower in the case of PM (around 1 for narrowband and 3 for
wideband).
The total bandwidth required for PM can be determined from the bandwidth and
maximum amplitude of the modulating signal: $B_{\mathrm{PM}}=2(1+\beta)B$.

## 5.3 END-CHAPTER MATERIALS
> id: ch05-5-3 | src: book 5.3; p.151 | kind: concept

### 5.3.1 Recommended Reading
> id: ch05-5-3-1 | src: book 5.3.1; p.151 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [. . .] refer to the reference list at the end of the text.

#### Books
> id: ch05-5-3-1-books | src: book p.151 | kind: concept

Digital-to-analog conversion is discussed in [Pea92], [Cou01], and [Sta04]. Analog-to-analog conversion is discussed in [Pea92], Chapter 5 of [Cou01], [Sta04]. [Hsu03]
gives a good mathematical approach to all materials discussed in this chapter. More
advanced materials can be found in [Ber96].

### 5.3.2 Key Terms
> id: ch05-5-3-2 | src: book 5.3.2; p.151 | kind: concept

- amplitude modulation (AM)
- amplitude shift keying (ASK)
- analog-to-analog conversion
- carrier signal
- constellation diagram
- digital-to-analog conversion
- frequency modulation (FM)
- frequency shift keying (FSK)
- phase modulation (PM)
- phase shift keying (PSK)
- quadrature amplitude modulation (QAM)

### 5.3.3 Summary
> id: ch05-5-3-3 | src: book 5.3.3; p.151 | kind: summary

Digital-to-analog conversion is the process of changing one of the characteristics of an
analog signal based on the information in the digital data. Digital-to-analog conversion
can be accomplished in several ways: amplitude shift keying (ASK), frequency shift
keying (FSK), and phase shift keying (PSK). Quadrature amplitude modulation (QAM)
combines ASK and PSK. In amplitude shift keying, the amplitude of the carrier signal
is varied to create signal elements. Both frequency and phase remain constant while the
amplitude changes. In frequency shift keying, the frequency of the carrier signal is varied to represent data. The frequency of the modulated signal is constant for the duration
of one signal element, but changes for the next signal element if the data element
changes. Both peak amplitude and phase remain constant for all signal elements. In
phase shift keying, the phase of the carrier is varied to represent two or more different
signal elements. Both peak amplitude and frequency remain constant as the phase
changes. A constellation diagram shows us the amplitude and phase of a signal element, particularly when we are using two carriers (one in-phase and one quadrature).
Quadrature amplitude modulation (QAM) is a combination of ASK and PSK. QAM
uses two carriers, one in-phase and the other quadrature, with different amplitude levels
for each carrier. Analog-to-analog conversion is the representation of analog information by an analog signal. Conversion is needed if the medium is bandpass in nature or if
only a bandpass bandwidth is available to us.
Analog-to-analog conversion can be accomplished in three ways: amplitude modulation (AM), frequency modulation (FM), and phase modulation (PM). In AM transmission, the carrier signal is modulated so that its amplitude varies with the changing
amplitudes of the modulating signal. The frequency and phase of the carrier remain the
same; only the amplitude changes to follow variations in the information. In FM transmission, the frequency of the carrier signal is modulated to follow the changing voltage
level (amplitude) of the modulating signal. The peak amplitude and phase of the carrier
signal remain constant, but as the amplitude of the information signal changes, the frequency of the carrier changes correspondingly. In PM transmission, the phase of the
carrier signal is modulated to follow the changing voltage level (amplitude) of the modulating signal. The peak amplitude and frequency of the carrier signal remain constant,
but as the amplitude of the information signal changes, the phase of the carrier changes
correspondingly.
