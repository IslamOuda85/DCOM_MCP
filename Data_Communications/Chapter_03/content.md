---
doc_type: scientific_content
course_id: data_communications
chapter: 3
chapter_id: data_communications_ch03
chapter_title: Introduction to Physical Layer
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_3/ch3.pdf
  pages: 51-94
assets_dir: assets
asset_counts:
  illustration: 37
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T12:09:54+00:00'
status: complete
---
# Chapter 3: Introduction to Physical Layer

## Chapter Objectives
> id: ch03-0 | src: book p.53 | kind: objectives

One of the major functions of the physical layer is to move data in the form of electromagnetic signals across a transmission medium. Whether you are collecting
numerical statistics from another computer, sending animated pictures from a design
workstation, or causing a bell to ring at a distant control center, you are working with
the transmission of data across network connections.
Generally, the data usable to a person or application are not in a form that can be
transmitted over a network. For example, a photograph must first be changed to a form
that transmission media can accept. Transmission media work by conducting energy
along a physical path. For transmission, data needs to be changed to signals.
This chapter is divided into six sections:

- The first section shows how data and signals can be either analog or digital. Analog refers to an entity that is continuous; digital refers to an entity that is discrete.

- The second section shows that only periodic analog signals can be used in data
communication. The section discusses simple and composite signals. The attributes of analog signals such as period, frequency, and phase are also explained.

- The third section shows that only nonperiodic digital signals can be used in data
communication. The attributes of a digital signal such as bit rate and bit length are
discussed. We also show how digital data can be sent using analog signals. Baseband and broadband transmission are also discussed in this section.

- The fourth section is devoted to transmission impairment. The section shows how
attenuation, distortion, and noise can impair a signal.

- The fifth section discusses the data rate limit: how many bits per second we can
send with the available channel. The data rates of noiseless and noisy channels are
examined and compared.

- The sixth section discusses the performance of data transmission. Several channel
measurements are examined including bandwidth, throughput, latency, and jitter.
Performance is an issue that is revisited in several future chapters.

## 3.1 DATA AND SIGNALS
> id: ch03-3-1 | src: book 3.1; p.54 | kind: concept

Figure 3.1 shows a scenario in which a scientist working in a research company, Sky
Research, needs to order a book related to her research from an online bookseller, Scientific Books.

> **[ASSET ch03_ill_001]** Figure 3.1: Communication at the physical layer
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_001.png
> - src: book Figure 3.1; p.54
> - shows: Figure 3.1: Communication at the physical layer. End-to-end physical-layer communication across two LANs, point-to-point and switched WANs, routers, and a national ISP is traced between Alice and Bob; upper-layer communication is logical while each physical hop is direct.
> - structure: End-to-end physical-layer communication across two LANs, point-to-point and switched WANs, routers, and a national ISP is traced between Alice and Bob; upper-layer communication is logical while each physical hop is direct.
> - text_in_image: Sky Research; Alice; Application; Alice; Transport; Network; Data-link; Physical; R2; Network; To other; Data-link; ISPs; Physical; R2; R1; R4; Network; To other; Data-link; R3; R4; ISPs; Physical; Switched; R5; WAN; Network; Data-link; R5; National ISP; Physical; ISP; R7; Network; To other; Data-link; ISPs; R6; R7; Physical; Legend; Point-to-point WAN; Bob; LAN switch; Application; Transport; WAN switch; Network; Data-link; Router; Bob; Physical; Scientific Books
> - use_when: Use to teach ch03-3-1, interpret Figure 3.1, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

We can think of five different levels of communication between Alice, the computer on which our scientist is working, and Bob, the computer that provides online service. Communication at application, transport, network, or data-link is logical;
communication at the physical layer is physical. For simplicity, we have shown only
host-to-router, router-to-router, and router-to-host, but the switches are also involved in
the physical communication.
Although Alice and Bob need to exchange data, communication at the physical
layer means exchanging signals. Data need to be transmitted and received, but the
media have to change data to signals. Both data and the signals that represent them can
be either analog or digital in form.

### 3.1.1 Analog and Digital Data
> id: ch03-3-1-1 | src: book 3.1.1; p.55 | kind: concept

Data can be analog or digital. The term analog data refers to information that is
continuous; digital data refers to information that has discrete states. For example, an
analog clock that has hour, minute, and second hands gives information in a continuous
form; the movements of the hands are continuous. On the other hand, a digital clock
that reports the hours and the minutes will change suddenly from 8:05 to 8:06.
Analog data, such as the sounds made by a human voice, take on continuous values.
When someone speaks, an analog wave is created in the air. This can be captured by a
microphone and converted to an analog signal or sampled and converted to a digital
signal.
Digital data take on discrete values. For example, data are stored in computer
memory in the form of 0s and 1s. They can be converted to a digital signal or modulated into an analog signal for transmission across a medium.

### 3.1.2 Analog and Digital Signals
> id: ch03-3-1-2 | src: book 3.1.2; p.55 | kind: concept

Like the data they represent, signals can be either analog or digital. An analog signal
has infinitely many levels of intensity over a period of time. As the wave moves from
value A to value B, it passes through and includes an infinite number of values along its
path. A digital signal, on the other hand, can have only a limited number of defined
values. Although each value can be any number, it is often as simple as 1 and 0.
The simplest way to show signals is by plotting them on a pair of perpendicular
axes. The vertical axis represents the value or strength of a signal. The horizontal axis
represents time. Figure 3.2 illustrates an analog signal and a digital signal. The curve
representing the analog signal passes through an infinite number of points. The vertical
lines of the digital signal, however, demonstrate the sudden jump that the signal makes
from value to value.

> **[ASSET ch03_ill_002]** Figure 3.2: Comparison of analog and digital signals
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_002.png
> - src: book Figure 3.2; p.55
> - shows: Figure 3.2: Comparison of analog and digital signals. Two time-domain plots contrast a continuously varying analog signal with a digital signal that jumps among discrete levels.
> - structure: Two time-domain plots contrast a continuously varying analog signal with a digital signal that jumps among discrete levels.
> - text_in_image: Value; Value; Time; Time; a. Analog signal; b. Digital signal
> - use_when: Use to teach ch03-3-1-2, interpret Figure 3.2, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

### 3.1.3 Periodic and Nonperiodic
> id: ch03-3-1-3 | src: book 3.1.3; p.56 | kind: concept

Both analog and digital signals can take one of two forms: periodic or nonperiodic
(sometimes referred to as aperiodic; the prefix a in Greek means “non”).
A periodic signal completes a pattern within a measurable time frame, called a
period, and repeats that pattern over subsequent identical periods. The completion of
one full pattern is called a cycle. A nonperiodic signal changes without exhibiting a pattern or cycle that repeats over time.
Both analog and digital signals can be periodic or nonperiodic. In data communications, we commonly use periodic analog signals and nonperiodic digital signals, as
we will see in future chapters.

In data communications, we commonly use
periodic analog signals and nonperiodic digital signals.

## 3.2 PERIODIC ANALOG SIGNALS
> id: ch03-3-2 | src: book 3.2; p.56 | kind: concept

Periodic analog signals can be classified as simple or composite. A simple periodic
analog signal, a sine wave, cannot be decomposed into simpler signals. A composite
periodic analog signal is composed of multiple sine waves.

### 3.2.1 Sine Wave
> id: ch03-3-2-1 | src: book 3.2.1; p.56 | kind: concept

The sine wave is the most fundamental form of a periodic analog signal. When we
visualize it as a simple oscillating curve, its change over the course of a cycle is smooth
and consistent, a continuous, rolling flow. Figure 3.3 shows a sine wave. Each cycle
consists of a single arc above the time axis followed by a single arc below it.

> **[ASSET ch03_ill_003]** Figure 3.3: A sine wave
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_003.png
> - src: book Figure 3.3; p.56
> - shows: Figure 3.3: A sine wave. A time-domain sine wave marks repeating positive and negative half-cycles around the zero axis.
> - structure: A time-domain sine wave marks repeating positive and negative half-cycles around the zero axis.
> - text_in_image: Value; • • •; Time
> - use_when: Use to teach ch03-3-2-1, interpret Figure 3.3, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

We discuss a mathematical approach to sine waves in Appendix E.

A sine wave can be represented by three parameters: the peak amplitude, the frequency, and the phase. These three parameters fully describe a sine wave.

#### Peak Amplitude
> id: ch03-3-2-1-peak-amplitude | src: book p.57 | kind: concept

The peak amplitude of a signal is the absolute value of its highest intensity, proportional to the energy it carries. For electric signals, peak amplitude is normally measured
in volts. Figure 3.4 shows two signals and their peak amplitudes.

> **[ASSET ch03_ill_004]** Figure 3.4: Two signals with the same phase and frequency, but different amplitudes
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_004.png
> - src: book Figure 3.4; p.57
> - shows: Figure 3.4: Two signals with the same phase and frequency, but different amplitudes. Two sine waves share frequency and phase but use peak amplitudes of 1 and 2, isolating the effect of amplitude.
> - structure: Two sine waves share frequency and phase but use peak amplitudes of 1 and 2, isolating the effect of amplitude.
> - text_in_image: Amplitude; Peak; amplitude; • • •; Time; a. A signal with high peak amplitude; Amplitude; Peak; amplitude; • • •; Time; b. A signal with low peak amplitude
> - use_when: Use to teach ch03-3-2-1-peak-amplitude, interpret Figure 3.4, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Example 3.1
> id: ch03-example-3-1 | src: book Example 3.1; p.57 | kind: worked_example
The power in your house can be represented by a sine wave with a peak amplitude of 155 to 170 V.
However, it is common knowledge that the voltage of the power in U.S. homes is 110 to 120 V.
This discrepancy is due to the fact that these are root mean square (rms) values. The signal is
squared and then the average amplitude is calculated. The peak value is $A_{\text{peak}}=\sqrt{2}\,A_{\text{rms}}$.

#### Example 3.2
> id: ch03-example-3-2 | src: book Example 3.2; p.57 | kind: worked_example
The voltage of a battery is a constant; this constant value can be considered a sine wave, as we
will see later. For example, the peak value of an AA battery is normally 1.5 V.

#### Period and Frequency
> id: ch03-3-2-1-period-and-frequency | src: book p.57 | kind: concept

Period refers to the amount of time, in seconds, a signal needs to complete 1 cycle.
Frequency refers to the number of periods in 1 s. Note that period and frequency are just
one characteristic defined in two ways. Period is the inverse of frequency, and frequency
is the inverse of period, as the following formulas show.

$$f=\frac{1}{T},\qquad T=\frac{1}{f}$$

Frequency and period are the inverse of each other.

Figure 3.5 shows two signals and their frequencies. Period is formally expressed in
seconds. Frequency is formally expressed in Hertz (Hz), which is cycle per second.
Units of period and frequency are shown in Table 3.1.

> **[ASSET ch03_ill_005]** Figure 3.5: Two signals with the same amplitude and phase, but different frequencies
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_005.png
> - src: book Figure 3.5; p.58
> - shows: Figure 3.5: Two signals with the same amplitude and phase, but different frequencies. Two sine waves share amplitude and phase while completing 12 and 6 cycles per second, illustrating the inverse relationship between frequency and period.
> - structure: Two sine waves share amplitude and phase while completing 12 and 6 cycles per second, illustrating the inverse relationship between frequency and period.
> - text_in_image: 12 periods in 1 s; Frequency is 12 Hz; Amplitude; 1 s; • • •; Time; 1; Period:; s; 12; a. A signal with a frequency of 12 Hz; 6 periods in 1 s; Frequency is 6 Hz; Amplitude; 1 s; • • •; Time; T; 1; Period: s; b. A signal with a frequency of 6 Hz; 6
> - use_when: Use to teach ch03-3-2-1-period-and-frequency, interpret Figure 3.5, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

**Table 3.1: Period and frequency equivalents**

| Period unit | Equivalent in seconds | Frequency unit | Equivalent in hertz |
| --- | ---: | --- | ---: |
| Second (s) | $1\ \mathrm{s}$ | Hertz (Hz) | $1\ \mathrm{Hz}$ |
| Millisecond (ms) | $10^{-3}\ \mathrm{s}$ | Kilohertz (kHz) | $10^{3}\ \mathrm{Hz}$ |
| Microsecond ($\mu$s) | $10^{-6}\ \mathrm{s}$ | Megahertz (MHz) | $10^{6}\ \mathrm{Hz}$ |
| Nanosecond (ns) | $10^{-9}\ \mathrm{s}$ | Gigahertz (GHz) | $10^{9}\ \mathrm{Hz}$ |
| Picosecond (ps) | $10^{-12}\ \mathrm{s}$ | Terahertz (THz) | $10^{12}\ \mathrm{Hz}$ |

#### Example 3.3
> id: ch03-example-3-3 | src: book Example 3.3; p.58 | kind: worked_example

The power used in homes has a frequency of 60 Hz in North America and 50 Hz in Europe. For 60 Hz,

$$T=\frac{1}{f}=\frac{1}{60}\ \mathrm{s}\approx 0.0166\ \mathrm{s}=16.6\ \mathrm{ms}$$

The period is 0.0166 s, so the waveform repeats 60 times each second.

#### Example 3.4
> id: ch03-example-3-4 | src: book Example 3.4; p.58 | kind: worked_example

Express a period of 100 ms in microseconds.

**Solution**

$$100\ \mathrm{ms}=100\times10^{-3}\ \mathrm{s}=100\times10^{-3}\times10^6\ \mu\mathrm{s}=10^5\ \mu\mathrm{s}$$

#### Example 3.5
> id: ch03-example-3-5 | src: book Example 3.5; p.59 | kind: worked_example

The period of a signal is 100 ms. What is its frequency in kilohertz?

**Solution**

$$f=\frac{1}{T}=\frac{1}{100\times10^{-3}\ \mathrm{s}}=10\ \mathrm{Hz}=0.01\ \mathrm{kHz}$$

### 3.2.2 Phase
> id: ch03-3-2-2 | src: book 3.2.2; p.59 | kind: concept

The term phase, or phase shift, describes the position of the waveform relative to time 0.
If we think of the wave as something that can be shifted backward or forward along the
time axis, phase describes the amount of that shift. It indicates the status of the first cycle.

Phase describes the position of the waveform relative to time 0.
Phase is measured in degrees or radians [360º is 2π rad; 1º is 2π/360 rad, and 1 rad
is 360/(2π)]. A phase shift of 360º corresponds to a shift of a complete period; a phase
shift of 180° corresponds to a shift of one-half of a period; and a phase shift of 90º corresponds to a shift of one-quarter of a period (see Figure 3.6).

> **[ASSET ch03_ill_006]** Figure 3.6: Three sine waves with the same amplitude and frequency, but different phases
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_006.png
> - src: book Figure 3.6; p.60
> - shows: Figure 3.6: Three sine waves with the same amplitude and frequency, but different phases. Three equal-frequency sine waves begin at different positions in their cycles to show phase shifts of 0, 90, and 180 degrees.
> - structure: Three equal-frequency sine waves begin at different positions in their cycles to show phase shifts of 0, 90, and 180 degrees.
> - text_in_image: • • •; 0; Time; a. 0 degrees; • • •; 0; Time; 1/4 T; b. 90 degrees; 0; • • •; Time; 1/2 T; c. 180 degrees
> - use_when: Use to teach ch03-3-2-2, interpret Figure 3.6, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Looking at Figure 3.6, we can say that
a. A sine wave with a phase of 0° starts at time 0 with a zero amplitude. The
amplitude is increasing.
b. A sine wave with a phase of 90° starts at time 0 with a peak amplitude. The
amplitude is decreasing.
c. A sine wave with a phase of 180° starts at time 0 with a zero amplitude. The
amplitude is decreasing.
Another way to look at the phase is in terms of shift or offset. We can say that
a. A sine wave with a phase of 0° is not shifted.
b. A sine wave with a phase of 90° is shifted left by one-quarter cycle; the signal does not actually exist before time 0.
c. A sine wave with a phase of 180° is shifted left by one-half cycle; the signal does not actually exist before time 0.

#### Example 3.6
> id: ch03-example-3-6 | src: book Example 3.6; p.60 | kind: worked_example

A sine wave is offset by one-sixth of a cycle with respect to time zero. What is its phase in degrees and radians?

**Solution**

$$\phi=\frac{1}{6}(360^\circ)=60^\circ=\frac{\pi}{3}\ \mathrm{rad}\approx1.047\ \mathrm{rad}$$

### 3.2.3 Wavelength
> id: ch03-3-2-3 | src: book 3.2.3; p.61 | kind: concept

Wavelength is another characteristic of a signal traveling through a transmission
medium. Wavelength binds the period or the frequency of a simple sine wave to the
propagation speed of the medium (see Figure 3.7).

> **[ASSET ch03_ill_007]** Figure 3.7: Wavelength and period
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_007.png
> - src: book Figure 3.7; p.61
> - shows: Figure 3.7: Wavelength and period. Wavefronts separated by one wavelength are shown moving through a transmission medium, relating wavelength to propagation speed and period.
> - structure: Wavefronts separated by one wavelength are shown moving through a transmission medium, relating wavelength to propagation speed and period.
> - text_in_image: Wavelength; Transmission medium; At time t; Direction of; propagation; Transmission medium; At time t + T
> - use_when: Use to teach ch03-3-2-3, interpret Figure 3.7, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

While the frequency of a signal is independent of the medium, the wavelength
depends on both the frequency and the medium. Wavelength is a property of any type
of signal. In data communications, we often use wavelength to describe the transmission of light in an optical fiber. The wavelength is the distance a simple signal can
travel in one period.
Wavelength can be calculated if one is given the propagation speed (the speed of
light) and the period of the signal. However, since period and frequency are related to
each other, if we represent wavelength by λ, propagation speed by c (speed of light), and
frequency by f, we get

Propagation speed, period, frequency, and wavelength are related by

$$\lambda=cT=\frac{c}{f}$$

The propagation speed of electromagnetic signals depends on the medium and on
the frequency of the signal. For example, in a vacuum, light is propagated with a speed
of 3 × $10^{8}$ m/s. That speed is lower in air and even lower in cable.
The wavelength is normally measured in micrometers (microns) instead of meters.
For example, for red light with $f=4\times10^{14}$ Hz in air,

$$\lambda=\frac{3\times10^8}{4\times10^{14}}=0.75\times10^{-6}\ \mathrm{m}=0.75\ \mu\mathrm{m}$$

In a coaxial or fiber-optic cable, however, the wavelength is shorter (0.5 μm) because the
propagation speed in the cable is decreased.

### 3.2.4 Time and Frequency Domains
> id: ch03-3-2-4 | src: book 3.2.4; p.61 | kind: concept

A sine wave is comprehensively defined by its amplitude, frequency, and phase. We
have been showing a sine wave by using what is called a time-domain plot. The
time-domain plot shows changes in signal amplitude with respect to time (it is an
amplitude-versus-time plot). Phase is not explicitly shown on a time-domain plot.
To show the relationship between amplitude and frequency, we can use what is
called a frequency-domain plot. A frequency-domain plot is concerned with only the
peak value and the frequency. Changes of amplitude during one period are not shown.
Figure 3.8 shows a signal in both the time and frequency domains.

> **[ASSET ch03_ill_008]** Figure 3.8: The time-domain and frequency-domain plots of a sine wave
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_008.png
> - src: book Figure 3.8; p.62
> - shows: Figure 3.8: The time-domain and frequency-domain plots of a sine wave. The same sine wave is represented as a time-domain oscillation and as one frequency-domain line whose height is the peak amplitude.
> - structure: The same sine wave is represented as a time-domain oscillation and as one frequency-domain line whose height is the peak amplitude.
> - text_in_image: 1 second: Frequency: 6 Hz; Amplitude; Peak value: 5 V; 5; • • •; Time; (s); a. A sine wave in the time domain (peak value: 5 V, frequency: 6 Hz); Amplitude; Peak value: 5 V; 5; Frequency; 1; 2; 3; 4; 5; 6; 7; 8; 9 10 11 12 13 14; (Hz); b. The same sine wave in the frequency domain (peak value: 5 V, frequency: 6 Hz)
> - use_when: Use to teach ch03-3-2-4, interpret Figure 3.8, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

It is obvious that the frequency domain is easy to plot and conveys the information
that one can find in a time domain plot. The advantage of the frequency domain is that
we can immediately see the values of the frequency and peak amplitude. A complete
sine wave is represented by one spike. The position of the spike shows the frequency;
its height shows the peak amplitude.

A complete sine wave in the time domain can be represented
by one single spike in the frequency domain.

#### Example 3.7
> id: ch03-example-3-7 | src: book Example 3.7; p.62 | kind: worked_example
The frequency domain is more compact and useful when we are dealing with more than one sine
wave. For example, Figure 3.9 shows three sine waves, each with different amplitude and frequency. All can be represented by three spikes in the frequency domain.

> **[ASSET ch03_ill_009]** Figure 3.9: The time domain and frequency domain of three sine waves
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_009.png
> - src: book Figure 3.9; p.62
> - shows: Figure 3.9: The time domain and frequency domain of three sine waves. Three sine waves are compared in time and frequency domains, where the frequency-domain plot exposes each component's frequency and amplitude directly.
> - structure: Three sine waves are compared in time and frequency domains, where the frequency-domain plot exposes each component's frequency and amplitude directly.
> - text_in_image: Amplitude; Amplitude; 15; 15; 10; 10; 5; 5; • • •; 0; 8; 16; Frequency; Time; b. Frequency-domain representation of; 1 s; the same three signals; a. Time-domain representation of three sine waves; with frequencies 0, 8, and 16
> - use_when: Use to teach ch03-3-2-4, interpret Figure 3.9, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

### 3.2.5 Composite Signals
> id: ch03-3-2-5 | src: book 3.2.5; p.63 | kind: concept

So far, we have focused on simple sine waves. Simple sine waves have many applications in daily life. We can send a single sine wave to carry electric energy from one
place to another. For example, the power company sends a single sine wave with a frequency of 60 Hz to distribute electric energy to houses and businesses. As another
example, we can use a single sine wave to send an alarm to a security center when a
burglar opens a door or window in the house. In the first case, the sine wave is carrying
energy; in the second, the sine wave is a signal of danger.
If we had only one single sine wave to convey a conversation over the phone, it
would make no sense and carry no information. We would just hear a buzz. As we will
see in Chapters 4 and 5, we need to send a composite signal to communicate data. A
composite signal is made of many simple sine waves.

A single-frequency sine wave is not useful in data communications;
we need to send a composite signal, a signal made of many simple sine waves.

In the early 1900s, the French mathematician Jean-Baptiste Fourier showed that
any composite signal is actually a combination of simple sine waves with different frequencies, amplitudes, and phases. Fourier analysis is discussed in Appendix E; for our
purposes, we just present the concept.

According to Fourier analysis, any composite signal is a combination of
simple sine waves with different frequencies, amplitudes, and phases.
Fourier analysis is discussed in Appendix E.

A composite signal can be periodic or nonperiodic. A periodic composite signal
can be decomposed into a series of simple sine waves with discrete frequencies—
frequencies that have integer values (1, 2, 3, and so on). A nonperiodic composite signal can be decomposed into a combination of an infinite number of simple sine waves
with continuous frequencies, frequencies that have real values.

If the composite signal is periodic, the decomposition gives a series of signals with
discrete frequencies; if the composite signal is nonperiodic, the decomposition
gives a combination of sine waves with continuous frequencies.

#### Example 3.8
> id: ch03-example-3-8 | src: book Example 3.8; p.63 | kind: worked_example
Figure 3.10 shows a periodic composite signal with frequency f. This type of signal is not typical
of those found in data communications.We can consider it to be three alarm systems, each with a
different frequency. The analysis of this signal can give us a good understanding of how to
decompose signals.
It is very difficult to manually decompose this signal into a series of simple sine waves.
However, there are tools, both hardware and software, that can help us do the job. We are not concerned about how it is done; we are only interested in the result. Figure 3.11 shows the result of
decomposing the above signal in both the time and frequency domains.
The amplitude of the sine wave with frequency f is almost the same as the peak amplitude
of the composite signal. The amplitude of the sine wave with frequency 3f is one-third of that of

> **[ASSET ch03_ill_010]** Figure 3.10: A composite periodic signal
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_010.png
> - src: book Figure 3.10; p.64
> - shows: Figure 3.10: A composite periodic signal. A periodic composite time-domain signal repeats a nonsinusoidal pattern while its frequency-domain representation contains discrete spectral lines.
> - structure: A periodic composite time-domain signal repeats a nonsinusoidal pattern while its frequency-domain representation contains discrete spectral lines.
> - text_in_image: • • •; Time
> - use_when: Use to teach ch03-3-2-5, interpret Figure 3.10, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

> **[ASSET ch03_ill_011]** Figure 3.11: Decomposition of a composite periodic signal in the time and frequency domains
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_011.png
> - src: book Figure 3.11; p.64
> - shows: Figure 3.11: Decomposition of a composite periodic signal in the time and frequency domains. Fourier decomposition builds a composite periodic signal by adding a fundamental sine wave and odd harmonics, with component and summed waveforms aligned.
> - structure: Fourier decomposition builds a composite periodic signal by adding a fundamental sine wave and odd harmonics, with component and summed waveforms aligned.
> - text_in_image: Frequency f; Amplitude; Frequency 3f; Frequency 9f; • • •; Time; a. Time-domain decomposition of a composite signal; Amplitude; 9f; 3f; f; Frequency; b. Frequency-domain decomposition of the composite signal
> - use_when: Use to teach ch03-3-2-5, interpret Figure 3.11, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

the first, and the amplitude of the sine wave with frequency 9f is one-ninth of the first. The frequency of the sine wave with frequency f is the same as the frequency of the composite signal; it
is called the fundamental frequency, or first harmonic. The sine wave with frequency 3f has a
frequency of 3 times the fundamental frequency; it is called the third harmonic. The third sine
wave with frequency 9f has a frequency of 9 times the fundamental frequency; it is called the
ninth harmonic.
Note that the frequency decomposition of the signal is discrete; it has frequencies f, 3f, and
9f. Because f is an integral number, 3f and 9f are also integral numbers. There are no frequencies
such as 1.2f or 2.6f. The frequency domain of a periodic composite signal is always made of discrete spikes.

#### Example 3.9
> id: ch03-example-3-9 | src: book Example 3.9; p.64 | kind: worked_example
Figure 3.12 shows a nonperiodic composite signal. It can be the signal created by a microphone
or a telephone set when a word or two is pronounced. In this case, the composite signal cannot be
periodic, because that implies that we are repeating the same word or words with exactly the
same tone.

> **[ASSET ch03_ill_012]** Figure 3.12: The time and frequency domains of a nonperiodic signal
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_012.png
> - src: book Figure 3.12; p.65
> - shows: Figure 3.12: The time and frequency domains of a nonperiodic signal. A nonperiodic time-domain waveform corresponds to a continuous frequency spectrum rather than discrete harmonic lines.
> - structure: A nonperiodic time-domain waveform corresponds to a continuous frequency spectrum rather than discrete harmonic lines.
> - text_in_image: Amplitude; Amplitude; Amplitude for sine; wave of frequency f; 0; f; 4 kHz; Time; Frequency; a. Time domain; b. Frequency domain
> - use_when: Use to teach ch03-3-2-5, interpret Figure 3.12, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

In a time-domain representation of this composite signal, there are an infinite number of simple sine frequencies. Although the number of frequencies in a human voice is
infinite, the range is limited. A normal human being can create a continuous range of
frequencies between 0 and 4 kHz.
Note that the frequency decomposition of the signal yields a continuous curve.
There are an infinite number of frequencies between 0.0 and 4000.0 (real values). To find
the amplitude related to frequency f, we draw a vertical line at f to intersect the envelope
curve. The height of the vertical line is the amplitude of the corresponding frequency.

### 3.2.6 Bandwidth
> id: ch03-3-2-6 | src: book 3.2.6; p.65 | kind: concept

The range of frequencies contained in a composite signal is its bandwidth. The bandwidth is normally a difference between two numbers. For example, if a composite signal
contains frequencies between 1000 and 5000, its bandwidth is 5000 − 1000, or 4000.

The bandwidth of a composite signal is the difference between the
highest and the lowest frequencies contained in that signal.

Figure 3.13 shows the concept of bandwidth. The figure depicts two composite
signals, one periodic and the other nonperiodic. The bandwidth of the periodic signal
contains all integer frequencies between 1000 and 5000 (1000, 1001, 1002, . . .). The
bandwidth of the nonperiodic signals has the same range, but the frequencies are
continuous.

#### Example 3.10
> id: ch03-example-3-10 | src: book Example 3.10; p.65 | kind: worked_example
If a periodic signal is decomposed into five sine waves with frequencies of 100, 300, 500, 700,
and 900 Hz, what is its bandwidth? Draw the spectrum, assuming all components have a maximum amplitude of 10 V.

**Solution**
Let $f_{h}$ be the highest frequency, $f_{l}$ the lowest frequency, and B the bandwidth. Then

B = $f_{h}$ − $f_{l}$  = 900 − 100 = 800 Hz
The spectrum has only five spikes, at 100, 300, 500, 700, and 900 Hz (see Figure 3.14).

> **[ASSET ch03_ill_013]** Figure 3.13: The bandwidth of periodic and nonperiodic composite signals
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_013.png
> - src: book Figure 3.13; p.66
> - shows: Figure 3.13: The bandwidth of periodic and nonperiodic composite signals. Bandwidth is the interval between minimum and maximum frequencies for both discrete periodic spectra and continuous nonperiodic spectra.
> - structure: Bandwidth is the interval between minimum and maximum frequencies for both discrete periodic spectra and continuous nonperiodic spectra.
> - text_in_image: Amplitude; • • •; • • •; 1000; 5000; Frequency; Bandwidth = 5000 – 1000 = 4000 Hz; a. Bandwidth of a periodic signal; Amplitude; 1000; 5000; Frequency; Bandwidth = 5000 – 1000 = 4000 Hz; b. Bandwidth of a nonperiodic signal
> - use_when: Use to teach ch03-3-2-6, interpret Figure 3.13, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

> **[ASSET ch03_ill_014]** Figure 3.14: The bandwidth for Example 3.10
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_014.png
> - src: book Figure 3.14; p.66
> - shows: Figure 3.14: The bandwidth for Example 3.10. A discrete spectrum marks 100, 300, 500, 700, and 900 Hz components, so the periodic signal spans an 800 Hz bandwidth.
> - structure: A discrete spectrum marks 100, 300, 500, 700, and 900 Hz components, so the periodic signal spans an 800 Hz bandwidth.
> - text_in_image: 10 V; 100; 300; 500; 700; 900; Frequency; Bandwidth = 900 − 100 = 800 Hz
> - use_when: Use to teach ch03-3-2-6, interpret Figure 3.14, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Example 3.11
> id: ch03-example-3-11 | src: book Example 3.11; p.66 | kind: worked_example
A periodic signal has a bandwidth of 20 Hz. The highest frequency is 60 Hz. What is the lowest
frequency? Draw the spectrum if the signal contains all frequencies of the same amplitude.

**Solution**
Let $f_{h}$ be the highest frequency, $f_{l}$ the lowest frequency, and B the bandwidth. Then

B = $f_{h}$ − $f_{l}$
20 = 60 − $f_{l}$
$f_{l}$ = 60 − 20 = 40 Hz

The spectrum contains all integer frequencies. We show this by a series of spikes (see Figure 3.15).

#### Example 3.12
> id: ch03-example-3-12 | src: book Example 3.12; p.66 | kind: worked_example
A nonperiodic composite signal has a bandwidth of 200 kHz, with a middle frequency of
140 kHz and peak amplitude of 20 V. The two extreme frequencies have an amplitude of 0. Draw
the frequency domain of the signal.

> **[ASSET ch03_ill_015]** Figure 3.15: The bandwidth for Example 3.11
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_015.png
> - src: book Figure 3.15; p.67
> - shows: Figure 3.15: The bandwidth for Example 3.11. The spectrum for Example 3.11 contains integer-frequency lines from 40 through 60 Hz, giving a 20 Hz bandwidth.
> - structure: The spectrum for Example 3.11 contains integer-frequency lines from 40 through 60 Hz, giving a 20 Hz bandwidth.
> - text_in_image: 40; 41; 42; 58; 59; 60; Frequency; (Hz); Bandwidth = 60 − 40 = 20 Hz
> - use_when: Use to teach ch03-3-2-6, interpret Figure 3.15, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

**Solution**
The lowest frequency must be at 40 kHz and the highest at 240 kHz. Figure 3.16 shows the frequency domain and the bandwidth.

> **[ASSET ch03_ill_016]** Figure 3.16: The bandwidth for Example 3.12
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_016.png
> - src: book Figure 3.16; p.67
> - shows: Figure 3.16: The bandwidth for Example 3.12. The continuous spectrum for Example 3.12 extends from 40 to 240 kHz and reaches its peak amplitude at the 140 kHz middle frequency.
> - structure: The continuous spectrum for Example 3.12 extends from 40 to 240 kHz and reaches its peak amplitude at the 140 kHz middle frequency.
> - text_in_image: Amplitude; 40 kHz; 140 kHz; 240 kHz; Frequency
> - use_when: Use to teach ch03-3-2-6, interpret Figure 3.16, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Example 3.13
> id: ch03-example-3-13 | src: book Example 3.13; p.67 | kind: worked_example
An example of a nonperiodic composite signal is the signal propagated by an AM radio station. In
the United States, each AM radio station is assigned a 10-kHz bandwidth. The total bandwidth dedicated to AM radio ranges from 530 to 1700 kHz. We will show the rationale behind this 10-kHz
bandwidth in Chapter 5.

#### Example 3.14
> id: ch03-example-3-14 | src: book Example 3.14; p.67 | kind: worked_example
Another example of a nonperiodic composite signal is the signal propagated by an FM radio station. In the United States, each FM radio station is assigned a 200-kHz bandwidth. The total
bandwidth dedicated to FM radio ranges from 88 to 108 MHz. We will show the rationale behind
this 200-kHz bandwidth in Chapter 5.

#### Example 3.15
> id: ch03-example-3-15 | src: book Example 3.15; p.67 | kind: worked_example
Another example of a nonperiodic composite signal is the signal received by an old-fashioned
analog black-and-white TV. A TV screen is made up of pixels (picture elements) with each pixel
being either white or black. The screen is scanned 30 times per second. (Scanning is actually
60 times per second, but odd lines are scanned in one round and even lines in the next and then
interleaved.) If we assume a resolution of 525 × 700 (525 vertical lines and 700 horizontal lines),
which is a ratio of 3:4, we have 367,500 pixels per screen. If we scan the screen 30 times per second, this is 367,500 × 30 = 11,025,000 pixels per second. The worst-case scenario is alternating
black and white pixels. In this case, we need to represent one color by the minimum amplitude
and the other color by the maximum amplitude. We can send 2 pixels per cycle. Therefore, we
need 11,025,000 / 2 = 5,512,500 cycles per second, or Hz. The bandwidth needed is 5.5124 MHz.
This worst-case scenario has such a low probability of occurrence that the assumption is that we
need only 70 percent of this bandwidth, which is 3.85 MHz. Since audio and synchronization signals are also needed, a 4-MHz bandwidth has been set aside for each black and white TV channel. An analog color TV channel has a 6-MHz bandwidth.

## 3.3 DIGITAL SIGNALS
> id: ch03-3-3 | src: book 3.3; p.68 | kind: concept

In addition to being represented by an analog signal, information can also be represented by a digital signal. For example, a 1 can be encoded as a positive voltage and a
0 as zero voltage. A digital signal can have more than two levels. In this case, we can
send more than 1 bit for each level. Figure 3.17 shows two signals, one with two levels and the other with four. We send 1 bit per level in part a of the figure and 2 bits
per level  in part b of the figure. In general, a signal with $L$ levels carries $\log_2 L$ bits per level. For the four-level signal in part b, $\log_2 4=2$ bits per level.

> **[ASSET ch03_ill_017]** Figure 3.17: Two digital signals: one with two signal levels and the other with four signal levels
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_017.png
> - src: book Figure 3.17; p.68
> - shows: Figure 3.17: Two digital signals: one with two signal levels and the other with four signal levels. Two digital waveforms show how two voltage levels carry one bit per level while four voltage levels carry two bits per level, producing 8 and 16 bps over the same interval.
> - structure: Two digital waveforms show how two voltage levels carry one bit per level while four voltage levels carry two bits per level, producing 8 and 16 bps over the same interval.
> - text_in_image: 8 bits sent in 1 s,; Amplitude; Bit rate = 8 bps; 1; 0; 1; 1; 0; 0; 0; 1; Level 2; • • •; Level 1; 1 s; Time; a. A digital signal with two levels; Amplitude; 16 bits sent in 1 s,; Bit rate = 16 bps; 11; 10; 01; 01; 00; 00; 00; 10; Level 4; Level 3; • • •; 1 s; Time; Level 2; Level 1; b. A digital signal with four levels
> - use_when: Use to teach ch03-3-3-1, interpret Figure 3.17, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

### Example 3.16
> id: ch03-example-3-16 | src: book Example 3.16; p.68 | kind: worked_example

A digital signal has eight levels. The number of bits carried by each level is

$$\log_2 8=3\ \text{bits per level}$$

### Example 3.17
> id: ch03-example-3-17 | src: book Example 3.17; p.68 | kind: worked_example

A digital signal has nine levels. The mathematical result is $\log_2 9\approx3.17$ bits per level, but a symbol must carry an integer number of bits. Four bits provide $2^4=16$ distinct combinations, enough to represent the nine levels.

### 3.3.1 Bit Rate
> id: ch03-3-3-1 | src: book 3.3.1; p.69 | kind: concept

Most digital signals are nonperiodic, and thus period and frequency are not appropriate characteristics. Another term—bit rate (instead of frequency)—is used to describe
digital signals. The bit rate is the number of bits sent in 1s, expressed in bits per
second (bps). Figure 3.17 shows the bit rate for two signals.

#### Example 3.18
> id: ch03-example-3-18 | src: book Example 3.18; p.69 | kind: worked_example
Assume we need to download text documents at the rate of 100 pages per second. What is the
required bit rate of the channel?

**Solution**
A page is an average of 24 lines with 80 characters in each line. If we assume that one character
requires 8 bits, the bit rate is

$$100\times24\times80\times8=1{,}536{,}000\ \mathrm{bps}=1.536\ \mathrm{Mbps}$$

#### Example 3.19
> id: ch03-example-3-19 | src: book Example 3.19; p.69 | kind: worked_example
A digitized voice channel, as we will see in Chapter 4, is made by digitizing a 4-kHz bandwidth
analog voice signal. We need to sample the signal at twice the highest frequency (two samples
per hertz). We assume that each sample requires 8 bits. What is the required bit rate?

**Solution**
The bit rate can be calculated as

$$2\times4000\times8=64{,}000\ \mathrm{bps}=64\ \mathrm{kbps}$$

#### Example 3.20
> id: ch03-example-3-20 | src: book Example 3.20; p.69 | kind: worked_example
What is the bit rate for high-definition TV (HDTV)?

**Solution**
HDTV uses digital signals to broadcast high quality video signals. The HDTV screen is normally
a ratio of 16 : 9 (in contrast to 4 : 3 for regular TV), which means the screen is wider. There are
1920 by 1080 pixels per screen, and the screen is renewed 30 times per second. Twenty-four bits
represents one color pixel. We can calculate the bit rate as

$$1920\times1080\times30\times24=1{,}492{,}992{,}000\ \mathrm{bps}\approx1.5\ \mathrm{Gbps}$$

The TV stations reduce this rate to 20 to 40 Mbps through compression.

### 3.3.2 Bit Length
> id: ch03-3-3-2 | src: book 3.3.2; p.69 | kind: concept

We discussed the concept of the wavelength for an analog signal: the distance one cycle
occupies on the transmission medium. We can define something similar for a digital
signal: the bit length. The bit length is the distance one bit occupies on the transmission medium.

$$\text{Bit length}=\text{propagation speed}\times\text{bit duration}$$

### 3.3.3 Digital Signal as a Composite Analog Signal
> id: ch03-3-3-3 | src: book 3.3.3; p.70 | kind: concept

Based on Fourier analysis (See Appendix E), a digital signal is a composite analog signal. The bandwidth is infinite, as you may have guessed. We can intuitively come up
with this concept when we consider a digital signal. A digital signal, in the time domain,
comprises connected vertical and horizontal line segments. A vertical line in the time
domain means a frequency of infinity (sudden change in time); a horizontal line in the
time domain means a frequency of zero (no change in time). Going from a frequency of
zero to a frequency of infinity (and vice versa) implies all frequencies in between are
part of the domain.
Fourier analysis can be used to decompose a digital signal. If the digital signal is
periodic, which is rare in data communications, the decomposed signal has a frequency-domain representation with an infinite bandwidth and discrete frequencies. If the digital
signal is nonperiodic, the decomposed signal still has an infinite bandwidth, but the frequencies are continuous. Figure 3.18 shows a periodic and a nonperiodic digital signal
and their bandwidths.

> **[ASSET ch03_ill_018]** Figure 3.18: The time and frequency domains of periodic and nonperiodic digital signals
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_018.png
> - src: book Figure 3.18; p.70
> - shows: Figure 3.18: The time and frequency domains of periodic and nonperiodic digital signals. Periodic and nonperiodic digital signals are paired with their discrete and continuous frequency spectra.
> - structure: Periodic and nonperiodic digital signals are paired with their discrete and continuous frequency spectra.
> - text_in_image: • • •; • • •; 3f; 5f; 7f; 9f; 13f; 11f; Time; f; Frequency; a. Time and frequency domains of periodic digital signal; • • •; 0; Time; Frequency; b. Time and frequency domains of nonperiodic digital signal
> - use_when: Use to teach ch03-3-3-3, interpret Figure 3.18, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Note that both bandwidths are infinite, but the periodic signal has discrete frequencies while the nonperiodic signal has continuous frequencies.

### 3.3.4 Transmission of Digital Signals
> id: ch03-3-3-4 | src: book 3.3.4; p.70 | kind: concept

The previous discussion asserts that a digital signal, periodic or nonperiodic, is a composite analog signal with frequencies between zero and infinity. For the remainder of
the discussion, let us consider the case of a nonperiodic digital signal, similar to the
ones we encounter in data communications. The fundamental question is, How can we
send a digital signal from point A to point B? We can transmit a digital signal by using
one of two different approaches: baseband transmission or broadband transmission
(using modulation).
A digital signal is a composite analog signal with an infinite bandwidth.

#### Baseband Transmission
> id: ch03-3-3-4-baseband-transmission | src: book p.71 | kind: concept

Baseband transmission means sending a digital signal over a channel without changing
the digital signal to an analog signal. Figure 3.19 shows baseband transmission.

> **[ASSET ch03_ill_019]** Figure 3.19: Baseband transmission
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_019.png
> - src: book Figure 3.19; p.71
> - shows: Figure 3.19: Baseband transmission. Baseband transmission sends a digital waveform directly through a low-pass channel and reconstructs the waveform at the receiver.
> - structure: Baseband transmission sends a digital waveform directly through a low-pass channel and reconstructs the waveform at the receiver.
> - text_in_image: Digital signal; Channel
> - use_when: Use to teach ch03-3-3-4, interpret Figure 3.19, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Baseband transmission requires that we have a low-pass channel, a channel with
a bandwidth that starts from zero. This is the case if we have a dedicated medium with
a bandwidth constituting only one channel. For example, the entire bandwidth of a
cable connecting two computers is one single channel. As another example, we may
connect several computers to a bus, but not allow more than two stations to communicate at a time. Again we have a low-pass channel, and we can use it for baseband communication. Figure 3.20 shows two low-pass channels: one with a narrow bandwidth
and the other with a wide bandwidth. We need to remember that a low-pass channel
with infinite bandwidth is ideal, but we cannot have such a channel in real life. However, we can get close.

> **[ASSET ch03_ill_020]** Figure 3.20: Bandwidths of two low-pass channels
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_020.png
> - src: book Figure 3.20; p.71
> - shows: Figure 3.20: Bandwidths of two low-pass channels. Low-pass channels are classified by bandwidth from an ideal unlimited channel through finite wide and narrow channels.
> - structure: Low-pass channels are classified by bandwidth from an ideal unlimited channel through finite wide and narrow channels.
> - text_in_image: Amplitude; 0; Frequency; f1; a. Low-pass channel, wide bandwidth; Amplitude; 0; Frequency; f1; b. Low-pass channel, narrow bandwidth
> - use_when: Use to teach ch03-3-3-4-baseband-transmission, interpret Figure 3.20, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Let us study two cases of a baseband communication: a low-pass channel with a
wide bandwidth and one with a limited bandwidth.

#### Case 1: Low-Pass Channel with Wide Bandwidth
> id: ch03-3-3-4-case-1-low-pass-channel-with-wide-bandwidth | src: book p.72 | kind: concept

If we want to preserve the exact form of a nonperiodic digital signal with vertical segments vertical and horizontal segments horizontal, we need to send the entire spectrum,
the continuous range of frequencies between zero and infinity. This is possible if we
have a dedicated medium with an infinite bandwidth between the sender and receiver
that preserves the exact amplitude of each component of the composite signal.
Although this may be possible inside a computer (e.g., between CPU and memory), it is
not possible between two devices. Fortunately, the amplitudes of the frequencies at the
border of the bandwidth are so small that they can be ignored. This means that if we
have a medium, such as a coaxial or fiber optic cable, with a very wide bandwidth, two
stations can communicate by using digital signals with very good accuracy, as shown in
Figure 3.21. Note that $f_{1}$ is close to zero, and $f_{2}$ is very high.

> **[ASSET ch03_ill_021]** Figure 3.21: Baseband transmission using a dedicated medium
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_021.png
> - src: book Figure 3.21; p.72
> - shows: Figure 3.21: Baseband transmission using a dedicated medium. A dedicated medium between two devices provides the low-pass path required for baseband transmission.
> - structure: A dedicated medium between two devices provides the low-pass path required for baseband transmission.
> - text_in_image: Input signal bandwidth; Bandwidth supported by medium; Output signal bandwidth; • • •; • • •; • • •; ∞; 0; f1; f1; f2; f2; t; t; Input signal; Wide-bandwidth channel; Output signal
> - use_when: Use to teach ch03-3-3-4-baseband-transmission, interpret Figure 3.21, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Although the output signal is not an exact replica of the original signal, the data
can still be deduced from the received signal. Note that although some of the frequencies are blocked by the medium, they are not critical.

Baseband transmission of a digital signal that preserves the shape of the digital signal is
possible only if we have a low-pass channel with an infinite or very wide bandwidth.

#### Example 3.21
> id: ch03-example-3-21 | src: book Example 3.21; p.72 | kind: worked_example
An example of a dedicated channel where the entire bandwidth of the medium is used as one single
channel is a LAN. Almost every wired LAN today uses a dedicated channel for two stations communicating with each other. In a bus topology LAN with multipoint connections, only two stations
can communicate with each other at each moment in time (timesharing); the other stations need to
refrain from sending data. In a star topology LAN, the entire channel between each station and the
hub is used for communication between these two entities. We study LANs in Chapter 13.

#### Case 2: Low-Pass Channel with Limited Bandwidth
> id: ch03-3-3-4-case-2-low-pass-channel-with-limited-bandwidth | src: book p.72 | kind: concept

In a low-pass channel with limited bandwidth, we approximate the digital signal with
an analog signal. The level of approximation depends on the bandwidth available.

#### Rough Approximation
> id: ch03-3-3-4-rough-approximation | src: book p.72 | kind: concept

Let us assume that we have a digital signal of bit rate N. If we want to send analog signals to roughly simulate this signal, we need to consider the worst case, a maximum
number of changes in the digital signal. This happens when the signal carries the
sequence 01010101 . . . or the sequence 10101010. . . . To simulate these two cases, we
need an analog signal of frequency f = N/2. Let 1 be the positive peak value and 0 be the
negative peak value. We send 2 bits in each cycle; the frequency of the analog signal is
one-half of the bit rate, or N/2. However, just this one frequency cannot make all patterns;
we need more components. The maximum frequency is N/2. As an example of this concept, let us see how a digital signal with a 3-bit pattern can be simulated by using analog
signals. Figure 3.22 shows the idea. The two similar cases (000 and 111) are simulated
with a signal with frequency f = 0 and a phase of 180° for 000 and a phase of 0° for 111.
The two worst cases (010 and 101) are simulated with an analog signal with frequency f =
N/2 and phases of 180° and 0°. The other four cases can only be simulated with an analog
signal with f = N/4 and phases of 180°, 270°, 90°, and 0°. In other words, we need a channel that can handle frequencies 0, N/4, and N/2. This rough approximation is referred to
as using the first harmonic (N/2) frequency. The required bandwidth is

$$B=\frac{N}{2}-0=\frac{N}{2}$$

> **[ASSET ch03_ill_022]** Figure 3.22: Rough approximation of a digital signal using the first harmonic for worst case
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_022.png
> - src: book Figure 3.22; p.73
> - shows: Figure 3.22: Rough approximation of a digital signal using the first harmonic for worst case. A digital bit pattern is approximated by only its first harmonic, showing the rough waveform recovered when bandwidth is limited.
> - structure: A digital bit pattern is approximated by only its first harmonic, showing the rough waveform recovered when bandwidth is limited.
> - text_in_image: Amplitude; N; Bandwidth = 2; 0; N/4; N/2; Frequency; Digital: bit rate N; Digital: bit rate N; Digital: bit rate N; Digital: bit rate N; 0; 0; 1; 0; 1; 0; 0; 1; 1; 0; 0; 0; Analog: f = 0, p = 180; Analog: f = N/4, p = 180; Analog: f = N/2, p = 180; Analog: f = N/4, p = 270; Digital: bit rate N; Digital: bit rate N; Digital: bit rate N; Digital: bit rate N; 1; 0; 0; 1; 0; 1; 1; 1; 0; 1; 1; 1; Analog: f = N/4, p = 90; Analog: f = N/2, p = 0; Analog: f = N/4, p = 0; Analog: f = 0, p = 0
> - use_when: Use to teach ch03-3-3-4-baseband-transmission, interpret Figure 3.22, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Better Approximation
> id: ch03-3-3-4-better-approximation | src: book p.73 | kind: concept

To make the shape of the analog signal look more like that of a digital signal, we need
to add more harmonics of the frequencies. We need to increase the bandwidth. We can
increase the bandwidth to 3N/2, 5N/2, 7N/2, and so on. Figure 3.23 shows the effect of

> **[ASSET ch03_ill_023]** Figure 3.23: Simulating a digital signal with first three harmonics
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_023.png
> - src: book Figure 3.23; p.74
> - shows: Figure 3.23: Simulating a digital signal with first three harmonics. Adding the third and fifth harmonics progressively improves the approximation of a digital signal compared with using only the first harmonic.
> - structure: Adding the third and fifth harmonics progressively improves the approximation of a digital signal compared with using only the first harmonic.
> - text_in_image: Amplitude; 5N; Bandwidth = 2; Frequency; 0; N/4; N/2; 3N/4; 3N/2; 5N/4; 5N/2; Digital: bit rate N; Analog: f = N/2 and 3N/2; 0; 1; 0; Analog: f = N/2; Analog: f = N/2, 3N/2, and 5N/2
> - use_when: Use to teach ch03-3-3-4-baseband-transmission, interpret Figure 3.23, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

this increase for one of the worst cases, the pattern 010. Note that we have shown only the
highest frequency for each harmonic. We use the first, third, and fifth harmonics. The
required bandwidth is now 5N/2, the difference between the lowest frequency 0 and
the highest frequency 5N/2. As we emphasized before, we need to remember that the
required bandwidth is proportional to the bit rate.

In baseband transmission, the required bandwidth is proportional to the bit rate;
if we need to send bits faster, we need more bandwidth.

By using this method, Table 3.2 shows how much bandwidth we need to send data
at different rates.

**Table 3.2: Bandwidth requirements**

| Bit Rate | Harmonic 1 | Harmonics 1, 3 | Harmonics 1, 3, 5 |
| --- | --- | --- | --- |
| n = 1 kbps | B = 500 Hz | B = 1.5 kHz | B = 2.5 kHz |
| n = 10 kbps | B = 5 kHz | B = 15 kHz | B = 25 kHz |
| n = 100 kbps | B = 50 kHz | B = 150 kHz | B = 250 kHz |

#### Example 3.22
> id: ch03-example-3-22 | src: book Example 3.22; p.74 | kind: worked_example
What is the required bandwidth of a low-pass channel if we need to send 1 Mbps by using baseband transmission?
**Solution**
The answer depends on the accuracy desired.
a. The minimum bandwidth, a rough approximation, is B = bit rate /2, or 500 kHz. We need
a low-pass channel with frequencies between 0 and 500 kHz.
b. A better result can be achieved by using the first and the third harmonics with the required
bandwidth B = 3 × 500 kHz = 1.5 MHz.
c. A still better result can be achieved by using the first, third, and fifth harmonics with
B = 5 × 500 kHz = 2.5 MHz.

#### Example 3.23
> id: ch03-example-3-23 | src: book Example 3.23; p.75 | kind: worked_example
We have a low-pass channel with bandwidth 100 kHz. What is the maximum bit rate of this
channel?

**Solution**
The maximum bit rate can be achieved if we use the first harmonic. The bit rate is 2 times the
available bandwidth, or 200 kbps.

#### Broadband Transmission (Using Modulation)
> id: ch03-3-3-4-broadband-transmission-using-modulation | src: book p.75 | kind: concept

Broadband transmission or modulation means changing the digital signal to an analog signal for transmission. Modulation allows us to use a bandpass channel—a channel
with a bandwidth that does not start from zero. This type of channel is more available than
a low-pass channel. Figure 3.24 shows a bandpass channel.

> **[ASSET ch03_ill_024]** Figure 3.24: Bandwidth of a bandpass channel
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_024.png
> - src: book Figure 3.24; p.75
> - shows: Figure 3.24: Bandwidth of a bandpass channel. Broadband transmission modulates a digital signal into an analog waveform that fits a bandpass channel, then demodulates it at the receiver.
> - structure: Broadband transmission modulates a digital signal into an analog waveform that fits a bandpass channel, then demodulates it at the receiver.
> - text_in_image: Amplitude; f1; f2; Frequency; Bandpass channel
> - use_when: Use to teach ch03-3-3-4-broadband-transmission-using-modulation, interpret Figure 3.24, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Note that a low-pass channel can be considered a bandpass channel with the lower
frequency starting at zero.
Figure 3.25 shows the modulation of a digital signal. In the figure, a digital signal is
converted to a composite analog signal. We have used a single-frequency analog signal
(called a carrier); the amplitude of the carrier has been changed to look like the digital signal. The result, however, is not a single-frequency signal; it is a composite signal, as we
will see in Chapter 5. At the receiver, the received analog signal is converted to digital,
and the result is a replica of what has been sent.

If the available channel is a bandpass channel, we cannot send the digital signal directly to
the channel; we need to convert the digital signal to an analog signal before transmission.

> **[ASSET ch03_ill_025]** Figure 3.25: Modulation of a digital signal for transmission on a bandpass channel
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_025.png
> - src: book Figure 3.25; p.76
> - shows: Figure 3.25: Modulation of a digital signal for transmission on a bandpass channel. A bandpass channel is shown carrying an analog modulated signal whose spectrum fits between the channel's lower and upper frequencies.
> - structure: A bandpass channel is shown carrying an analog modulated signal whose spectrum fits between the channel's lower and upper frequencies.
> - text_in_image: t; t; Input digital signal; Output digital signal; Digital/analog; Analog/digital; converter; converter; Available bandwidth; Output analog signal bandwidth; Input analog signal bandwidth; f1; f2; f1; f2; f1; f2; Bandpass channel; t; t; Input analog signal; Input analog signal
> - use_when: Use to teach ch03-3-3-4-broadband-transmission-using-modulation, interpret Figure 3.25, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Example 3.24
> id: ch03-example-3-24 | src: book Example 3.24; p.76 | kind: worked_example
An example of broadband transmission using modulation is the sending of computer data through
a telephone subscriber line, the line connecting a resident to the central telephone office. These
lines, installed many years ago, are designed to carry voice (analog signal) with a limited bandwidth (frequencies between 0 and 4 kHz). Although this channel can be used as a low-pass channel, it is normally considered a bandpass channel. One reason is that the bandwidth is so narrow
(4 kHz) that if we treat the channel as low-pass and use it for baseband transmission, the maximum
bit rate can be only 8 kbps. The solution is to consider the channel a bandpass channel, convert the
digital signal from the computer to an analog signal, and send the analog signal. We can install two
converters to change the digital signal to analog and vice versa at the receiving end. The converter,
in this case, is called a modem (modulator/demodulator), which we discuss in detail in Chapter 5.

#### Example 3.25
> id: ch03-example-3-25 | src: book Example 3.25; p.76 | kind: worked_example
A second example is the digital cellular telephone. For better reception, digital cellular phones
convert the analog voice signal to a digital signal (see Chapter 16). Although the bandwidth allocated to a company providing digital cellular phone service is very wide, we still cannot send the
digital signal without conversion. The reason is that we only have a bandpass channel available
between caller and callee. For example, if the available bandwidth is W and we allow 1000 couples to talk simultaneously, this means the available channel is W/1000, just part of the entire
bandwidth. We need to convert the digitized voice to a composite analog signal before sending.
The digital cellular phones convert the analog audio signal to digital and then convert it again to
analog for transmission over a bandpass channel.

## 3.4 TRANSMISSION IMPAIRMENT
> id: ch03-3-4 | src: book 3.4; p.76 | kind: concept

Signals travel through transmission media, which are not perfect. The imperfection causes
signal impairment. This means that the signal at the beginning of the medium is not the
same as the signal at the end of the medium. What is sent is not what is received. Three
causes of impairment are attenuation, distortion, and noise (see Figure 3.26).

> **[ASSET ch03_ill_026]** Figure 3.26: Causes of impairment
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_026.png
> - src: book Figure 3.26; p.77
> - shows: Figure 3.26: Causes of impairment. Transmission impairment is organized into attenuation, distortion, and noise as the three causes that change a signal in transit.
> - structure: Transmission impairment is organized into attenuation, distortion, and noise as the three causes that change a signal in transit.
> - text_in_image: Impairment; causes; Attenuation; Distortion; Noise
> - use_when: Use to teach ch03-3-4, interpret Figure 3.26, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

### 3.4.1 Attenuation
> id: ch03-3-4-1 | src: book 3.4.1; p.77 | kind: concept

Attenuation means a loss of energy. When a signal, simple or composite, travels
through a medium, it loses some of its energy in overcoming the resistance of the
medium. That is why a wire carrying electric signals gets warm, if not hot, after a
while. Some of the electrical energy in the signal is converted to heat. To compensate
for this loss, amplifiers are used to amplify the signal. Figure 3.27 shows the effect of
attenuation and amplification.

> **[ASSET ch03_ill_027]** Figure 3.27: Attenuation
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_027.png
> - src: book Figure 3.27; p.77
> - shows: Figure 3.27: Attenuation. Input and output sine waves show attenuation as a reduction in amplitude while frequency and phase remain unchanged.
> - structure: Input and output sine waves show attenuation as a reduction in amplitude while frequency and phase remain unchanged.
> - text_in_image: Original; Attenuated; Amplified; Amplifier; Transmission medium; Point 1; Point 2; Point 3
> - use_when: Use to teach ch03-3-4-1, interpret Figure 3.27, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Decibel
> id: ch03-3-4-1-decibel | src: book p.77 | kind: concept

To show that a signal has lost or gained strength, engineers use the unit of the decibel.
The decibel (dB) measures the relative strengths of two signals or one signal at two different points. Note that the decibel is negative if a signal is attenuated and positive if a
signal is amplified.
$$\mathrm{dB}=10\log_{10}\left(\frac{P_2}{P_1}\right)$$

Variables $P_{1}$ and $P_{2}$ are the powers of a signal at points 1 and 2, respectively. Note that
some engineering books define the decibel in terms of voltage instead of power. In this
case, because power is proportional to the square of the voltage, the formula is $\mathrm{dB}=20\log_{10}(V_2/V_1)$. In this text, we express dB in terms of power.
#### Example 3.26
> id: ch03-example-3-26 | src: book Example 3.26; p.78 | kind: worked_example

If a signal's power is reduced to one-half, its attenuation is

$$10\log_{10}\left(\frac{P_1/2}{P_1}\right)=10\log_{10}(0.5)\approx-3\ \mathrm{dB}$$

#### Example 3.27
> id: ch03-example-3-27 | src: book Example 3.27; p.78 | kind: worked_example

If an amplifier makes the output power 10 times the input power, its gain is

$$10\log_{10}\left(\frac{10P_1}{P_1}\right)=10\ \mathrm{dB}$$

#### Example 3.28
> id: ch03-example-3-28 | src: book Example 3.28; p.78 | kind: worked_example

Figure 3.28 shows a signal passing through two lossy sections and an amplifier. Decibel values add, so the net change is

$$-3+7-3=+1\ \mathrm{dB}$$

> **[ASSET ch03_ill_028]** Figure 3.28: Decibels for Example 3.28
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_028.png
> - src: book Figure 3.28; p.78
> - shows: Figure 3.28: Decibels for Example 3.28. A transmission path combines losses and amplifier gain in decibels; adding the stage values gives the net power change.
> - structure: A transmission path combines losses and amplifier gain in decibels; adding the stage values gives the net power change.
> - text_in_image: 1 dB; –3 dB; 7 dB; –3 dB; Amplifier; Transmission; Transmission; Point 4; Point 1; Point 2; Point 3; medium; medium
> - use_when: Use to teach ch03-3-4-1-decibel, interpret Figure 3.28, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Example 3.29
> id: ch03-example-3-29 | src: book Example 3.29; p.78 | kind: worked_example

The unit dBm measures signal power relative to 1 mW:

$$\mathrm{dBm}=10\log_{10} P_m$$

where $P_m$ is measured in milliwatts. A power level of $-30$ dBm is therefore

$$P_m=10^{-30/10}\ \mathrm{mW}=10^{-3}\ \mathrm{mW}=1\ \mu\mathrm{W}$$

#### Example 3.30
> id: ch03-example-3-30 | src: book Example 3.30; p.79 | kind: worked_example

A 5 km cable loses 0.3 dB per kilometer and begins with 2 mW. Its total loss is $-1.5$ dB, so

$$10\log_{10}\left(\frac{P_2}{2\ \mathrm{mW}}\right)=-1.5,\qquad P_2\approx1.4\ \mathrm{mW}$$

### 3.4.2 Distortion
> id: ch03-3-4-2 | src: book 3.4.2; p.79 | kind: concept

Distortion means that the signal changes its form or shape. Distortion can occur in a
composite signal made of different frequencies. Each signal component has its own
propagation speed (see the next section) through a medium and, therefore, its own
delay in arriving at the final destination. Differences in delay may create a difference in
phase if the delay is not exactly the same as the period duration. In other words, signal
components at the receiver have phases different from what they had at the sender. The
shape of the composite signal is therefore not the same. Figure 3.29 shows the effect of
distortion on a composite signal.

> **[ASSET ch03_ill_029]** Figure 3.29: Distortion
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_029.png
> - src: book Figure 3.29; p.79
> - shows: Figure 3.29: Distortion. A composite signal's frequency components arrive with unequal delays and amplitudes, so their recombination produces a distorted output waveform.
> - structure: A composite signal's frequency components arrive with unequal delays and amplitudes, so their recombination produces a distorted output waveform.
> - text_in_image: Composite signal; Composite signal; sent; received; Components,; Components,; in phase; out of phase; At the sender; At the receiver
> - use_when: Use to teach ch03-3-4-2, interpret Figure 3.29, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

### 3.4.3 Noise
> id: ch03-3-4-3 | src: book 3.4.3; p.79 | kind: concept

Noise is another cause of impairment. Several types of noise, such as thermal noise,
induced noise, crosstalk, and impulse noise, may corrupt the signal. Thermal noise is
the random motion of electrons in a wire, which creates an extra signal not originally
sent by the transmitter. Induced noise comes from sources such as motors and appliances. These devices act as a sending antenna, and the transmission medium acts as the
receiving antenna. Crosstalk is the effect of one wire on the other. One wire acts as a
sending antenna and the other as the receiving antenna. Impulse noise is a spike (a signal with high energy in a very short time) that comes from power lines, lightning, and so
on. Figure 3.30 shows the effect of noise on a signal. We discuss error in Chapter 10.

> **[ASSET ch03_ill_030]** Figure 3.30: Noise
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_030.png
> - src: book Figure 3.30; p.80
> - shows: Figure 3.30: Noise. Four noise types are illustrated: thermal noise, induced noise, crosstalk, and impulse noise superimposed on a signal.
> - structure: Four noise types are illustrated: thermal noise, induced noise, crosstalk, and impulse noise superimposed on a signal.
> - text_in_image: Transmitted; Noise; Received; Transmission medium; Point 1; Point 2
> - use_when: Use to teach ch03-3-4-3, interpret Figure 3.30, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

#### Signal-to-Noise Ratio (SNR)
> id: ch03-3-4-3-signal-to-noise-ratio-snr | src: book p.80 | kind: concept

As we will see later, to find the theoretical bit rate limit, we need to know the ratio of
the signal power to the noise power. The signal-to-noise ratio compares average signal power with average noise power:

$$\mathrm{SNR}=\frac{P_{\text{signal}}}{P_{\text{noise}}}$$

Because it is a power ratio, it is often expressed in decibels:

$$\mathrm{SNR}_{\mathrm{dB}}=10\log_{10}(\mathrm{SNR})$$

Figure 3.31 shows the idea of SNR.

> **[ASSET ch03_ill_031]** Figure 3.31: Two cases of SNR: a high SNR and a low SNR
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_031.png
> - src: book Figure 3.31; p.80
> - shows: Figure 3.31: Two cases of SNR: a high SNR and a low SNR. Two received signals contrast a high signal-to-noise ratio with a low ratio where noise obscures the data waveform.
> - structure: Two received signals contrast a high signal-to-noise ratio with a low ratio where noise obscures the data waveform.
> - text_in_image: Signal; Noise; Signal + noise; a. High SNR; Signal; Noise; Signal + noise; b. Low SNR
> - use_when: Use to teach ch03-3-4-3-signal-to-noise-ratio-snr, interpret Figure 3.31, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

SNR is the ratio of the wanted signal to unwanted noise. A high SNR means less corruption; a low SNR means more corruption.
#### Example 3.31
> id: ch03-example-3-31 | src: book Example 3.31; p.81 | kind: worked_example

The signal power is 10 mW and the noise power is 1 $\mu$W. Thus

$$\mathrm{SNR}=\frac{10{,}000\ \mu\mathrm{W}}{1\ \mu\mathrm{W}}=10{,}000,\qquad \mathrm{SNR}_{\mathrm{dB}}=10\log_{10}(10^4)=40\ \mathrm{dB}$$

#### Example 3.32
> id: ch03-example-3-32 | src: book Example 3.32; p.81 | kind: worked_example

For a noiseless channel, $P_{\text{noise}}=0$, so both SNR and $\mathrm{SNR}_{\mathrm{dB}}$ approach infinity.

## 3.5 DATA RATE LIMITS
> id: ch03-3-5 | src: book 3.5; p.81 | kind: concept

A very important consideration in data communications is how fast we can send data, in
bits per second, over a channel. Data rate depends on three factors:

1. The bandwidth available
2. The level of the signals we use
3. The quality of the channel (the level of noise)

Two theoretical formulas were developed to calculate the data rate: one by Nyquist for
a noiseless channel, another by Shannon for a noisy channel.

### 3.5.1 Noiseless Channel: Nyquist Bit Rate
> id: ch03-3-5-1 | src: book 3.5.1; p.81 | kind: concept

For a noiseless channel, the Nyquist bit rate formula defines the theoretical maximum
bit rate

$$\mathrm{BitRate}=2B\log_2 L$$

In this formula, bandwidth is the bandwidth of the channel, L is the number of signal
levels used to represent data, and BitRate is the bit rate in bits per second.
According to the formula, we might think that, given a specific bandwidth, we can
have any bit rate we want by increasing the number of signal levels. Although the idea
is theoretically correct, practically there is a limit. When we increase the number of signal levels, we impose a burden on the receiver. If the number of levels in a signal is just 2,
the receiver can easily distinguish between a 0 and a 1. If the level of a signal is 64, the
receiver must be very sophisticated to distinguish between 64 different levels. In other
words, increasing the levels of a signal reduces the reliability of the system.

Increasing the levels of a signal may reduce the reliability of the system.
#### Example 3.33
> id: ch03-example-3-33 | src: book Example 3.33; p.82 | kind: worked_example

The Nyquist formula agrees with the intuitive baseband result for two signal levels: $2B\log_2 2=2B$. Nyquist is more general because it also handles more than two levels and modulated signals.

#### Example 3.34
> id: ch03-example-3-34 | src: book Example 3.34; p.82 | kind: worked_example

For a noiseless 3000 Hz channel with two signal levels,

$$\mathrm{BitRate}=2(3000)\log_2 2=6000\ \mathrm{bps}$$

#### Example 3.35
> id: ch03-example-3-35 | src: book Example 3.35; p.82 | kind: worked_example

For the same channel with four signal levels,

$$\mathrm{BitRate}=2(3000)\log_2 4=12{,}000\ \mathrm{bps}$$

#### Example 3.36
> id: ch03-example-3-36 | src: book Example 3.36; p.82 | kind: worked_example

To send 265 kbps through a noiseless 20 kHz channel,

$$265{,}000=2(20{,}000)\log_2 L,\qquad \log_2L=6.625,\qquad L=2^{6.625}\approx98.7$$

The result is not a power of two. Using 128 levels supports 280 kbps; using 64 levels supports 240 kbps.

### 3.5.2 Noisy Channel: Shannon Capacity
> id: ch03-3-5-2 | src: book 3.5.2; p.82 | kind: concept

In reality, we cannot have a noiseless channel; the channel is always noisy. In 1944,
Claude Shannon introduced a formula, called the Shannon capacity, to determine the
theoretical highest data rate for a noisy channel:

$$C=B\log_2(1+\mathrm{SNR})$$

In this formula, bandwidth is the bandwidth of the channel, SNR is the signal-to-noise ratio, and capacity is the capacity of the channel in bits per second. Note that in the
Shannon formula there is no indication of the signal level, which means that no matter
how many levels we have, we cannot achieve a data rate higher than the capacity of the
channel. In other words, the formula defines a characteristic of the channel, not the method
of transmission.
#### Example 3.37
> id: ch03-example-3-37 | src: book Example 3.37; p.83 | kind: worked_example

For an extremely noisy channel with $\mathrm{SNR}\approx0$,

$$C=B\log_2(1+0)=0$$

The channel cannot carry data regardless of its bandwidth.

#### Example 3.38
> id: ch03-example-3-38 | src: book Example 3.38; p.83 | kind: worked_example

For a telephone channel with $B=3000$ Hz and $\mathrm{SNR}=3162$,

$$C=3000\log_2(1+3162)\approx34{,}860\ \mathrm{bps}$$

#### Example 3.39
> id: ch03-example-3-39 | src: book Example 3.39; p.83 | kind: worked_example

Given $\mathrm{SNR}_{\mathrm{dB}}=36$ dB and $B=2$ MHz,

$$\mathrm{SNR}=10^{36/10}\approx3981$$

$$C=2\times10^6\log_2(1+3981)\approx23.9\ \mathrm{Mbps}$$

#### Example 3.40
> id: ch03-example-3-40 | src: book Example 3.40; p.83 | kind: worked_example

For large SNR, the book's useful approximation is

$$C\approx\frac{B\,\mathrm{SNR}_{\mathrm{dB}}}{3}$$

With $B=2$ MHz and $\mathrm{SNR}_{\mathrm{dB}}=36$ dB, it gives $C\approx24$ Mbps, close to the exact result.

### 3.5.3 Using Both Limits
> id: ch03-3-5-3 | src: book 3.5.3; p.83 | kind: concept

In practice, we need to use both methods to find the limits and signal levels. Let us show
this with an example.

#### Example 3.41
> id: ch03-example-3-41 | src: book Example 3.41; p.83 | kind: worked_example

A channel has a 1 MHz bandwidth and an SNR of 63. Shannon gives the upper bound:

$$C=10^6\log_2(1+63)=6\ \mathrm{Mbps}$$

Choosing 4 Mbps for margin, Nyquist gives the required number of levels:

$$4\times10^6=2(10^6)\log_2L,\qquad L=4$$

Shannon limits the achievable rate; Nyquist determines the signal-level count for the chosen rate.

## 3.6 PERFORMANCE
> id: ch03-3-6 | src: book 3.6; p.84 | kind: concept

Up to now, we have discussed the tools of transmitting data (signals) over a network
and how the data behave. One important issue in networking is the performance of the
network—how good is it? We discuss quality of service, an overall measurement of
network performance, in greater detail in Chapter 30. In this section, we introduce
terms that we need for future chapters.

### 3.6.1 Bandwidth
> id: ch03-3-6-1 | src: book 3.6.1; p.84 | kind: concept

One characteristic that measures network performance is bandwidth. However, the term
can be used in two different contexts with two different measuring values: bandwidth in
hertz and bandwidth in bits per second.

#### Bandwidth in Hertz
> id: ch03-3-6-1-bandwidth-in-hertz | src: book p.84 | kind: concept

We have discussed this concept. Bandwidth in hertz is the range of frequencies contained in a composite signal or the range of frequencies a channel can pass. For example, we can say the bandwidth of a subscriber telephone line is 4 kHz.

#### Bandwidth in Bits per Seconds
> id: ch03-3-6-1-bandwidth-in-bits-per-seconds | src: book p.84 | kind: concept

The term bandwidth can also refer to the number of bits per second that a channel, a
link, or even a network can transmit. For example, one can say the bandwidth of a Fast
Ethernet network (or the links in this network) is a maximum of 100 Mbps. This means
that this network can send 100 Mbps.

#### Relationship
> id: ch03-3-6-1-relationship | src: book p.84 | kind: concept

There is an explicit relationship between the bandwidth in hertz and bandwidth in bits
per second. Basically, an increase in bandwidth in hertz means an increase in bandwidth
in bits per second. The relationship depends on whether we have baseband transmission
or transmission with modulation. We discuss this relationship in Chapters 4 and 5.

In networking, we use the term bandwidth in two contexts.

- The first, bandwidth in hertz, refers to the range of frequencies in a composite signal or the range of frequencies that a channel can pass.
- The second, bandwidth in bits per second, refers to the speed of bit transmission in a
channel or link.
#### Example 3.42
> id: ch03-example-3-42 | src: book Example 3.42; p.85 | kind: worked_example
The bandwidth of a subscriber line is 4 kHz for voice or data. The bandwidth of this line for data transmission can be up to 56,000 bps using a sophisticated modem to change the digital signal to analog.

#### Example 3.43
> id: ch03-example-3-43 | src: book Example 3.43; p.85 | kind: worked_example
If the telephone company improves the quality of the line and increases the bandwidth to 8 kHz,
we can send 112,000 bps by using the same technology as mentioned in Example 3.42.

### 3.6.2 Throughput
> id: ch03-3-6-2 | src: book 3.6.2; p.85 | kind: concept

The throughput is a measure of how fast we can actually send data through a network.
Although, at first glance, bandwidth in bits per second and throughput seem the same,
they are different. A link may have a bandwidth of B bps, but we can only send T bps
through this link with T always less than B. In other words, the bandwidth is a potential
measurement of a link; the throughput is an actual measurement of how fast we can
send data. For example, we may have a link with a bandwidth of 1 Mbps, but the
devices connected to the end of the link may handle only 200 kbps. This means that we
cannot send more than 200 kbps through this link.
Imagine a highway designed to transmit 1000 cars per minute from one point
to another. However, if there is congestion on the road, this figure may be reduced to
100 cars per minute. The bandwidth is 1000 cars per minute; the throughput is 100 cars
per minute.

#### Example 3.44
> id: ch03-example-3-44 | src: book Example 3.44; p.85 | kind: worked_example
A network with bandwidth of 10 Mbps can pass only an average of 12,000 frames per minute
with each frame carrying an average of 10,000 bits. What is the throughput of this network?

**Solution**
We can calculate the throughput as

$$\text{Throughput}=\frac{12{,}000\times10{,}000}{60}=2\ \mathrm{Mbps}$$

The throughput is almost one-fifth of the bandwidth in this case.

### 3.6.3 Latency (Delay)
> id: ch03-3-6-3 | src: book 3.6.3; p.85 | kind: concept

The latency or delay defines how long it takes for an entire message to completely
arrive at the destination from the time the first bit is sent out from the source. We can
say that latency is made of four components: propagation time, transmission time,
queuing time and processing delay.

$$\text{Latency}=T_p+T_t+T_q+T_{proc}$$

#### Propagation Time
> id: ch03-3-6-3-propagation-time | src: book p.85 | kind: concept

Propagation time measures the time required for a bit to travel from the source to the
destination. The propagation time is calculated by dividing the distance by the propagation speed.

$$T_p=\frac{\text{distance}}{\text{propagation speed}}$$
The propagation speed of electromagnetic signals depends on the medium and on
the frequency of the signal. For example, in a vacuum, light is propagated with a speed
of 3 × $10^{8}$ m/s. It is lower in air; it is much lower in cable.

#### Example 3.45
> id: ch03-example-3-45 | src: book Example 3.45; p.86 | kind: worked_example

For a 12,000 km path and propagation speed $2.4\times10^8$ m/s,

$$T_p=\frac{12{,}000\times10^3}{2.4\times10^8}=0.05\ \mathrm{s}=50\ \mathrm{ms}$$

The propagation time depends on distance and propagation speed, not packet size.

#### Transmission Time
> id: ch03-3-6-3-transmission-time | src: book p.86 | kind: concept

Transmission time is the time required to put all message bits onto the link:

$$T_t=\frac{\text{message size in bits}}{\text{bit rate}}$$

#### Example 3.46
> id: ch03-example-3-46 | src: book Example 3.46; p.86 | kind: worked_example

To transmit a 2.5 kbyte packet on a 1 Gbps link,

$$T_t=\frac{2500\times8}{10^9}=20\ \mu\mathrm{s}$$

Transmission time depends on message size and bit rate, not path distance.

#### Example 3.47
> id: ch03-example-3-47 | src: book Example 3.47; p.86 | kind: worked_example

For Example 3.45's path and Example 3.46's packet, ignoring queuing and processing,

$$\text{Latency}=50\ \mathrm{ms}+20\ \mu\mathrm{s}=50.02\ \mathrm{ms}$$

### 3.6.4 Bandwidth-Delay Product
> id: ch03-3-6-4 | src: book 3.6.4; p.87 | kind: concept

Bandwidth and delay are two performance metrics of a link. However, as we will see in
this chapter and future chapters, what is very important in data communications is the
product of the two, the bandwidth-delay product. Let us elaborate on this issue, using
two hypothetical cases as examples.

- Case 1. Figure 3.32 shows case 1.

> **[ASSET ch03_ill_032]** Figure 3.32: Filling the link with bits for case 1
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_032.png
> - src: book Figure 3.32; p.87
> - shows: Figure 3.32: Filling the link with bits for case 1. A one-bit-per-second link with a five-second propagation delay is shown at successive times as five bits fill the path.
> - structure: A one-bit-per-second link with a five-second propagation delay is shown at successive times as five bits fill the path.
> - text_in_image: Sender; Receiver; Delay: 5 s; Bandwidth: 1 bps; Bandwidth × delay = 5 bits; After 1 s; 1st bit; After 2 s; 2nd bit; 1st bit; 3rd bit; 2nd bit; 1st bit; After 3 s; After 4 s; 4th bit; 3rd bit; 2nd bit; 1st bit; 1st bit; After 5 s; 5th bit; 4th bit; 3rd bit; 2nd bit; 1 s; 1 s; 1 s; 1 s; 1 s
> - use_when: Use to teach ch03-3-6-4, interpret Figure 3.32, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

Let us assume that we have a link with a bandwidth of 1 bps (unrealistic, but good
for demonstration purposes). We also assume that the delay of the link is 5 s (also
unrealistic). We want to see what the bandwidth-delay product means in this case.
Looking at the figure, we can say that this product 1 × 5 is the maximum number of
bits that can fill the link. There can be no more than 5 bits at any time on the link.

- Case 2. Now assume we have a bandwidth of 5 bps. Figure 3.33 shows that there
can be maximum 5 × 5 = 25 bits on the line. The reason is that, at each second,
there are 5 bits on the line; the duration of each bit is 0.20 s.

The above two cases show that the product of bandwidth and delay is the number of
bits that can fill the link. This measurement is important if we need to send data in bursts
and wait for the acknowledgment of each burst before sending the next one. To use the
maximum capability of the link, we need to make the size of our burst 2 times the product

> **[ASSET ch03_ill_033]** Figure 3.33: Filling the link with bits in case 2
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_033.png
> - src: book Figure 3.33; p.88
> - shows: Figure 3.33: Filling the link with bits in case 2. A five-bit-per-second link with the same five-second delay contains 25 bits in flight, demonstrating the bandwidth-delay product.
> - structure: A five-bit-per-second link with the same five-second delay contains 25 bits in flight, demonstrating the bandwidth-delay product.
> - text_in_image: Sender; Receiver; Bandwidth: 5 bps; Delay: 5 s; Bandwidth × delay = 25 bits; First 5 bits; After 1 s; First 5 bits; After 2 s; First 5 bits; After 3 s; First 5 bits; After 4 s; First 5 bits; After 5 s; 1 s; 1 s; 1 s; 1 s; 1 s
> - use_when: Use to teach ch03-3-6-4, interpret Figure 3.33, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

of bandwidth and delay; we need to fill up the full-duplex channel (two directions). The
sender should send a burst of data of (2 × bandwidth × delay) bits. The sender then waits
for receiver acknowledgment for part of the burst before sending another burst. The
amount 2 × bandwidth × delay is the number of bits that can be in transition at any time.

The bandwidth-delay product defines the number of bits that can fill the link.

#### Example 3.48
> id: ch03-example-3-48 | src: book Example 3.48; p.88 | kind: worked_example
We can think about the link between two points as a pipe. The cross section of the pipe represents
the bandwidth, and the length of the pipe represents the delay. We can say the volume of the pipe
defines the bandwidth-delay product, as shown in Figure 3.34.

> **[ASSET ch03_ill_034]** Figure 3.34: Concept of bandwidth-delay product
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_034.png
> - src: book Figure 3.34; p.88
> - shows: Figure 3.34: Concept of bandwidth-delay product. A pipe analogy relates bandwidth to pipe width, propagation delay to pipe length, and bandwidth-delay product to the volume in transit.
> - structure: A pipe analogy relates bandwidth to pipe width, propagation delay to pipe length, and bandwidth-delay product to the volume in transit.
> - text_in_image: Length: delay; Cross section: bandwidth; Volume: bandwidth × delay
> - use_when: Use to teach ch03-3-6-4, interpret Figure 3.34, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

### 3.6.5 Jitter
> id: ch03-3-6-5 | src: book 3.6.5; p.88 | kind: concept

Another performance issue that is related to delay is jitter. We can roughly say that jitter is a problem if different packets of data encounter different delays and the application using the data at the receiver site is time-sensitive (audio and video data, for
example). If the delay for the first packet is 20 ms, for the second is 45 ms, and for the
third is 40 ms, then the real-time application that uses the packets endures jitter. We discuss jitter in greater detail in Chapter 28.

## 3.7 END-CHAPTER MATERIALS
> id: ch03-3-7 | src: book 3.7; p.89 | kind: concept

### 3.7.1 Recommended Reading
> id: ch03-3-7-1 | src: book 3.7.1; p.89 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [. . .] refer to the reference list at the end of the text.

#### Books
> id: ch03-3-7-1-books | src: book p.89 | kind: concept

Data and signals are discussed in [Pea92]. [Cou01] gives excellent coverage of signals.
More advanced materials can be found in [Ber96]. [Hsu03] gives a good mathematical
approach to signaling. Complete coverage of Fourier Analysis can be found in [Spi74].
Data and signals are discussed in [Sta04] and [Tan03].

### 3.7.2 Key Terms
> id: ch03-3-7-2 | src: book 3.7.2; p.89 | kind: concept

- analog
- analog data
- analog signal
- attenuation
- bandpass channel
- bandwidth
- baseband transmission
- bit length
- bit rate
- bits per second (bps)
- broadband transmission
- composite signal
- cycle
- data
- decibel (dB)
- digital
- digital data
- digital signal
- distortion
- Fourier analysis
- frequency
- frequency-domain
- fundamental frequency
- harmonic
- Hertz (Hz)
- jitter
- latency
- low-pass channel
- noise
- nonperiodic signal
- Nyquist bit rate
- peak amplitude
- period
- periodic signal
- phase
- processing delay
- propagation speed
- propagation time
- queuing time
- Shannon capacity
- signal
- signal-to-noise ratio (SNR)
- sine wave
- throughput
- time-domain
- transmission time
- wavelength

### 3.7.3 Summary
> id: ch03-3-7-3 | src: book 3.7.3; p.89 | kind: summary

Data must be transformed to electromagnetic signals to be transmitted. Data can be
analog or digital. Analog data are continuous and take continuous values. Digital data
have discrete states and take discrete values. Signals can be analog or digital. Analog
signals can have an infinite number of values in a range; digital signals can have only a
limited number of values.
In data communications, we commonly use periodic analog signals and nonperiodic digital signals. Frequency and period are the inverse of each other. Frequency is
the rate of change with respect to time. Phase describes the position of the waveform
relative to time 0. A complete sine wave in the time domain can be represented by one
single spike in the frequency domain. A single-frequency sine wave is not useful in data
communications; we need to send a composite signal, a signal made of many simple
sine waves. According to Fourier analysis, any composite signal is a combination of
simple sine waves with different frequencies, amplitudes, and phases. The bandwidth
of a composite signal is the difference between the highest and the lowest frequencies
contained in that signal.
A digital signal is a composite analog signal with an infinite bandwidth. Baseband
transmission of a digital signal that preserves the shape of the digital signal is possible
only if we have a low-pass channel with an infinite or very wide bandwidth. If the
available channel is a bandpass channel, we cannot send a digital signal directly
to the channel; we need to convert the digital signal to an analog signal before
transmission.
For a noiseless channel, the Nyquist bit rate formula defines the theoretical maximum bit rate. For a noisy channel, we need to use the Shannon capacity to find the
maximum bit rate. Attenuation, distortion, and noise can impair a signal. Attenuation is
the loss of a signal’s energy due to the resistance of the medium. Distortion is the alteration of a signal due to the differing propagation speeds of each of the frequencies that
make up a signal. Noise is the external energy that corrupts a signal. The bandwidth-delay product defines the number of bits that can fill the link.

### Practice Problem Figures
> id: ch03-3-7-practice-problem-figures | src: book p.92 | kind: concept

These source figures provide the visual data required by Problems P3-9 through P3-11.

> **[ASSET ch03_ill_035]** Figure 3.35: Problem P3-9
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_035.png
> - src: book Figure 3.35; p.92
> - shows: Figure 3.35: Problem P3-9. Problem Figure 3.35 gives a digital pulse train with a labeled 16 ns timing interval for calculating bit rate.
> - structure: Problem Figure 3.35 gives a digital pulse train with a labeled 16 ns timing interval for calculating bit rate.
> - text_in_image: 16 ns; • • •; Time
> - use_when: Use to teach ch03-q-p3-9, interpret Figure 3.35, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

> **[ASSET ch03_ill_036]** Figure 3.36: Problem P3-10
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_036.png
> - src: book Figure 3.36; p.92
> - shows: Figure 3.36: Problem P3-10. Problem Figure 3.36 gives a sinusoidal waveform with a labeled 4 ms time interval for calculating frequency.
> - structure: Problem Figure 3.36 gives a sinusoidal waveform with a labeled 4 ms time interval for calculating frequency.
> - text_in_image: 4 ms; • • •; Time
> - use_when: Use to teach ch03-q-p3-10, interpret Figure 3.36, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high

> **[ASSET ch03_ill_037]** Figure 3.37: Problem P3-11
> - type: illustration
> - kind: diagram
> - file: assets/ch03_ill_037.png
> - src: book Figure 3.37; p.92
> - shows: Figure 3.37: Problem P3-11. Problem Figure 3.37 gives discrete spectral lines with labeled frequencies and amplitudes for calculating composite-signal bandwidth.
> - structure: Problem Figure 3.37 gives discrete spectral lines with labeled frequencies and amplitudes for calculating composite-signal bandwidth.
> - text_in_image: 180; Frequency; 5; 5; 5; 5; 5
> - use_when: Use to teach ch03-q-p3-11, interpret Figure 3.37, compare the depicted signals or channels, or solve a linked practice problem.
> - confidence: high
