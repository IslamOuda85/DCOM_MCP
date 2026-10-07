---
doc_type: scientific_content
course_id: data_communications
chapter: 6
chapter_id: data_communications_ch06
chapter_title: 'Bandwidth Utilization: Multiplexing and Spectrum Spreading'
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_6/ch6.pdf
  pages: 155-184
assets_dir: assets
asset_counts:
  illustration: 35
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
spec_version: 1.1-controller
generated_at: '2026-10-07T03:15:22+00:00'
status: complete
---
# Chapter 6: Bandwidth Utilization: Multiplexing and Spectrum Spreading

## Chapter Objectives
> id: ch06-0 | src: book p.155 | kind: objectives

In real life, we have links with limited bandwidths. The wise use of these bandwidths
has been, and will be, one of the main challenges of electronic communications.
However, the meaning of wise may depend on the application. Sometimes we need to
combine several low-bandwidth channels to make use of one channel with a larger
bandwidth. Sometimes we need to expand the bandwidth of a channel to achieve goals
such as privacy and antijamming. In this chapter, we explore these two broad categories
of bandwidth utilization: multiplexing and spectrum spreading. In multiplexing, our
goal is efficiency; we combine several channels into one. In spectrum spreading, our
goals are privacy and antijamming; we expand the bandwidth of a channel to insert
redundancy, which is necessary to achieve these goals.
This chapter is divided into two sections:

- The first section discusses multiplexing. The first method described in this section
is called frequency-division multiplexing (FDM), which means to combine several
analog signals into a single analog signal. The second method is called wavelength-division multiplexing (WDM), which means to combine several optical signals into
one optical signal.The third method is called time-division multiplexing (TDM),
which allows several digital signals to share a channel in time.

- The second section discusses spectrum spreading, in which we first spread the bandwidth of a signal to add redundancy for the purpose of more secure transmission
before combining different channels. The first method described in this section is
called frequency hopping spread spectrum (FHSS), in which different modulation
frequencies are used in different periods of time. The second method is called direct
sequence spread spectrum (DSSS), in which a single bit in the original signal is
changed to a sequence before transmission.

## 6.1 MULTIPLEXING
> id: ch06-6-1 | src: book 6.1; p.156 | kind: concept

Whenever the bandwidth of a medium linking two devices is greater than the bandwidth needs of the devices, the link can be shared. Multiplexing is the set of techniques
that allow the simultaneous transmission of multiple signals across a single data link.
As data and telecommunications use increases, so does traffic. We can accommodate
this increase by continuing to add individual links each time a new channel is needed;
or we can install higher-bandwidth links and use each to carry multiple signals. As
described in Chapter 7, today’s technology includes high-bandwidth media such as
optical fiber and terrestrial and satellite microwaves. Each has a bandwidth far in
excess of that needed for the average transmission signal. If the bandwidth of a link is
greater than the bandwidth needs of the devices connected to it, the bandwidth
is wasted. An efficient system maximizes the utilization of all resources; bandwidth is
one of the most precious resources we have in data communications.
In a multiplexed system, n lines share the bandwidth of one link. Figure 6.1 shows
the basic format of a multiplexed system. The lines on the left direct their transmission
streams to a multiplexer (MUX), which combines them into a single stream (many-to-one). At the receiving end, that stream is fed into a demultiplexer (DEMUX), which
separates the stream back into its component transmissions (one-to-many) and
directs them to their corresponding lines. In the figure, the word link refers to the
physical path. The word channel refers to the portion of a link that carries a transmission between a given pair of lines. One link can have many (n) channels.

> **[ASSET ch06_ill_001]** Figure 6.1: Dividing a link into channels
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_001.png
> - src: book Figure 6.1; p.156
> - shows: Figure 6.1: Dividing a link into channels. Multiple input lines enter a multiplexer, one shared link carries n logical channels, and a demultiplexer separates them into the corresponding output lines.
> - structure: Multiple input lines enter a multiplexer, one shared link carries n logical channels, and a demultiplexer separates them into the corresponding output lines.
> - text_in_image: MUX: Multiplexer; DEMUX: Demultiplexer; D; n; n; E; M; Input; Output; M; U; • • •; • • •; lines; lines; U; X; 1 link, n channels; X
> - use_when: Teach ch06-6-1, interpret Figure 6.1, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

There are three basic multiplexing techniques: frequency-division multiplexing,
wavelength-division multiplexing, and time-division multiplexing. The first two are
techniques designed for analog signals, the third, for digital signals (see Figure 6.2).

> **[ASSET ch06_ill_002]** Figure 6.2: Categories of multiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_002.png
> - src: book Figure 6.2; p.156
> - shows: Figure 6.2: Categories of multiplexing. A classification tree divides multiplexing into frequency-division and wavelength-division techniques for analog signals and time-division multiplexing for digital signals.
> - structure: A classification tree divides multiplexing into frequency-division and wavelength-division techniques for analog signals and time-division multiplexing for digital signals.
> - text_in_image: Multiplexing; Frequency-division; Wavelength-division; Time-division; multiplexing; multiplexing; multiplexing; Analog; Analog; Digital
> - use_when: Teach ch06-6-1, interpret Figure 6.2, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

Although some textbooks consider carrier division multiple access (CDMA)
as a fourth multiplexing category, we discuss CDMA as an access method (see
Chapter 12).

### 6.1.1 Frequency-Division Multiplexing
> id: ch06-6-1-1 | src: book 6.1.1; p.157 | kind: concept

Frequency-division multiplexing (FDM) is an analog technique that can be applied
when the bandwidth of a link (in hertz) is greater than the combined bandwidths of
the signals to be transmitted. In FDM, signals generated by each sending device modulate different carrier frequencies. These modulated signals are then combined into a single
composite signal that can be transported by the link. Carrier frequencies are separated
by sufficient bandwidth to accommodate the modulated signal. These bandwidth
ranges are the channels through which the various signals travel. Channels can be separated by strips of unused bandwidth—guard bands—to prevent signals from overlapping. In addition, carrier frequencies must not interfere with the original data
frequencies.
Figure 6.3 gives a conceptual view of FDM. In this illustration, the transmission path
is divided into three parts, each representing a channel that carries one transmission.

> **[ASSET ch06_ill_003]** Figure 6.3: Frequency-division multiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_003.png
> - src: book Figure 6.3; p.157
> - shows: Figure 6.3: Frequency-division multiplexing. A frequency-domain view places three input signals in nonoverlapping channel bands inside one wider link spectrum, then separates them at the receiver.
> - structure: A frequency-domain view places three input signals in nonoverlapping channel bands inside one wider link spectrum, then separates them at the receiver.
> - text_in_image: D; Channel 1; E; M; Input; Output; M; U; Channel 2; lines; lines; U; X; Channel 3; X
> - use_when: Teach ch06-6-1-1, interpret Figure 6.3, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

We consider FDM to be an analog multiplexing technique; however, this does not
mean that FDM cannot be used to combine sources sending digital signals. A digital
signal can be converted to an analog signal (with the techniques discussed in Chapter 5)
before FDM is used to multiplex them.

FDM is an analog multiplexing technique that combines analog signals.

#### Multiplexing Process
> id: ch06-6-1-1-multiplexing-process | src: book p.157 | kind: concept

Figure 6.4 is a conceptual illustration of the multiplexing process. Each source generates a signal of a similar frequency range. Inside the multiplexer, these similar signals
modulate different carrier frequencies ( $f_{1}$, $f_{2}$, and $f_{3}$). The resulting modulated signals
are then combined into a single composite signal that is sent out over a media link that
has enough bandwidth to accommodate it.

> **[ASSET ch06_ill_004]** Figure 6.4: FDM process
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_004.png
> - src: book Figure 6.4; p.158
> - shows: Figure 6.4: FDM process. Three baseband analog signals modulate carriers f1, f2, and f3; an adder combines their shifted spectra into one composite FDM signal.
> - structure: Three baseband analog signals modulate carriers f1, f2, and f3; an adder combines their shifted spectra into one composite FDM signal.
> - text_in_image: Modulator; Carrier f1; Modulator; +; Carrier f2; Modulator; Baseband; Carrier f3; analog signals
> - use_when: Teach ch06-6-1-1-multiplexing-process, interpret Figure 6.4, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### Demultiplexing Process
> id: ch06-6-1-1-demultiplexing-process | src: book p.158 | kind: concept

The demultiplexer uses a series of filters to decompose the multiplexed signal into its
constituent component signals. The individual signals are then passed to a demodulator
that separates them from their carriers and passes them to the output lines. Figure 6.5 is
a conceptual illustration of demultiplexing process.

> **[ASSET ch06_ill_005]** Figure 6.5: FDM demultiplexing example
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_005.png
> - src: book Figure 6.5; p.158
> - shows: Figure 6.5: FDM demultiplexing example. A composite FDM signal fans out through three bandpass filters and demodulators tuned to f1, f2, and f3, recovering the three original baseband signals.
> - structure: A composite FDM signal fans out through three bandpass filters and demodulators tuned to f1, f2, and f3, recovering the three original baseband signals.
> - text_in_image: Demodulator; Filter; Carrier f1; Demodulator; Filter; Carrier f2; Demodulator; Baseband; Filter; Carrier  f3; analog signals
> - use_when: Teach ch06-6-1-1-demultiplexing-process, interpret Figure 6.5, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

##### Example 6.1
> id: ch06-example-6-1 | src: book Example 6.1 | kind: worked_example
Assume that a voice channel occupies a bandwidth of 4 kHz. We need to combine three voice
channels into a link with a bandwidth of 12 kHz, from 20 to 32 kHz. Show the configuration,
using the frequency domain. Assume there are no guard bands.

**Solution**
We shift (modulate) each of the three voice channels to a different bandwidth, as shown in Figure 6.6. We use the 20- to 24-kHz bandwidth for the first channel, the 24- to 28-kHz bandwidth

> **[ASSET ch06_ill_006]** Figure 6.6: Example 6.1
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_006.png
> - src: book Figure 6.6; p.159
> - shows: Figure 6.6: Example 6.1. Three 4 kHz voice spectra are shifted into contiguous 20-24, 24-28, and 28-32 kHz bands, combined on the link, then filtered and shifted back at the receiver.
> - structure: Three 4 kHz voice spectra are shifted into contiguous 20-24, 24-28, and 28-32 kHz bands, combined on the link, then filtered and shifted back at the receiver.
> - text_in_image: Shift and combine; Modulator; 0; 4; 20; 24; +; Modulator; 24; 28; 0; 4; 20; 32; Modulator; 28; 32; 0; 4; Higher-bandwidth link; Bandpass; filter; 0; 4; 20; 24; Bandpass; 20; 32; 24; 28; 0; 4; filter; Bandpass; filter; 28; 32; 0; 4; Filter and shift
> - use_when: Teach ch06-example-6-1, interpret Figure 6.6, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

for the second channel, and the 28- to 32-kHz bandwidth for the third one. Then we combine
them as shown in Figure 6.6. At the receiver, each channel receives the entire signal, using a
filter to separate out its own signal. The first channel uses a filter that passes frequencies
between 20 and 24 kHz and filters out (discards) any other frequencies. The second channel
uses a filter that passes frequencies between 24 and 28 kHz, and the third channel uses a filter
that passes frequencies between 28 and 32 kHz. Each channel then shifts the frequency to start
from zero.

##### Example 6.2
> id: ch06-example-6-2 | src: book Example 6.2 | kind: worked_example
Five channels, each with a 100-kHz bandwidth, are to be multiplexed together. What is the minimum bandwidth of the link if there is a need for a guard band of 10 kHz between the channels to
prevent interference?

**Solution**
For five channels, we need at least four guard bands. This means that the required bandwidth is at
least 5 × 100 + 4 × 10 = 540 kHz, as shown in Figure 6.7.

##### Example 6.3
> id: ch06-example-6-3 | src: book Example 6.3 | kind: worked_example
Four data channels (digital), each transmitting at 1 Mbps, use a satellite channel of 1 MHz.
Design an appropriate configuration, using FDM.

**Solution**
The satellite channel is analog. We divide it into four channels, each channel having a 250-kHz
bandwidth. Each digital channel of 1 Mbps is modulated so that each 4 bits is modulated to
1 Hz. One solution is 16-QAM modulation. Figure 6.8 shows one possible configuration.

> **[ASSET ch06_ill_007]** Figure 6.7: Example 6.2
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_007.png
> - src: book Figure 6.7; p.160
> - shows: Figure 6.7: Example 6.2. Five 100 kHz channels are separated by four 10 kHz guard bands, producing a total FDM bandwidth of 540 kHz.
> - structure: Five 100 kHz channels are separated by four 10 kHz guard bands, producing a total FDM bandwidth of 540 kHz.
> - text_in_image: Guard band; of 10 kHz; 100 kHz; 100 kHz; 100 kHz; 100 kHz; 100 kHz; 540 kHz
> - use_when: Teach ch06-example-6-2, interpret Figure 6.7, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

> **[ASSET ch06_ill_008]** Figure 6.8: Example 6.3
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_008.png
> - src: book Figure 6.8; p.160
> - shows: Figure 6.8: Example 6.3. Four 1 Mbps digital inputs use 16-QAM to become four 250 kHz analog channels; FDM combines them into a 1 MHz satellite channel.
> - structure: Four 1 Mbps digital inputs use 16-QAM to become four 250 kHz analog channels; FDM combines them into a 1 MHz satellite channel.
> - text_in_image: 1 Mbps; 250 kHz; 16-QAM; Digital; Analog; 1 Mbps; 250 kHz; 16-QAM; Digital; Analog; 1 MHz; FDM; 1 Mbps; 250 kHz; 16-QAM; Digital; Analog; 1 Mbps; 250 kHz; 16-QAM; Digital; Analog
> - use_when: Teach ch06-example-6-3, interpret Figure 6.8, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### The Analog Carrier System
> id: ch06-6-1-1-the-analog-carrier-system | src: book p.160 | kind: concept

To maximize the efficiency of their infrastructure, telephone companies have traditionally multiplexed signals from lower-bandwidth lines onto higher-bandwidth lines. In
this way, many switched or leased lines can be combined into fewer but bigger channels. For analog lines, FDM is used.
One of these hierarchical systems used by telephone companies is made up of
groups, supergroups, master groups, and jumbo groups (see Figure 6.9).
In this analog hierarchy, 12 voice channels are multiplexed onto a higher-bandwidth
line to create a group. A group has 48 kHz of bandwidth and supports 12 voice channels.
At the next level, up to five groups can be multiplexed to create a composite signal
called a supergroup. A supergroup has a bandwidth of 240 kHz and supports up to
60 voice channels. Supergroups can be made up of either five groups or 60 independent
voice channels.
At the next level, 10 supergroups are multiplexed to create a master group. A
master group must have 2.40 MHz of bandwidth, but the need for guard bands between
the supergroups increases the necessary bandwidth to 2.52 MHz. Master groups support
up to 600 voice channels.
Finally, six master groups can be combined into a jumbo group. A jumbo group
must have 15.12 MHz (6 × 2.52 MHz) but is augmented to 16.984 MHz to allow for
guard bands between the master groups.

> **[ASSET ch06_ill_009]** Figure 6.9: Analog hierarchy
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_009.png
> - src: book Figure 6.9; p.161
> - shows: Figure 6.9: Analog hierarchy. The analog carrier hierarchy combines 12 voice channels into a 48 kHz group, five groups into a 240 kHz supergroup, ten supergroups into a 2.52 MHz master group, and six master groups into a 16.984 MHz jumbo group.
> - structure: The analog carrier hierarchy combines 12 voice channels into a 48 kHz group, five groups into a 240 kHz supergroup, ten supergroups into a 2.52 MHz master group, and six master groups into a 16.984 MHz jumbo group.
> - text_in_image: 48 kHz; 12 voice channels; 4 kHz; 12 voice channels; 240 kHz; 4 kHz; 60 voice channels; 5 Group; F; D; • • •; 2.52 MHz; M; 600 voice channels; 10 Supergroup; 4 kHz; F; 16.984 MHz; D; 3600 voice channels; M; 6 Master group; F; • • •; D; Jumbo; M; F; group; D; M
> - use_when: Teach ch06-6-1-1-the-analog-carrier-system, interpret Figure 6.9, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### Other Applications of FDM
> id: ch06-6-1-1-other-applications-of-fdm | src: book p.161 | kind: concept

A very common application of FDM is AM and FM radio broadcasting. Radio uses the
air as the transmission medium. A special band from 530 to 1700 kHz is assigned
to AM radio. All radio stations need to share this band. As discussed in Chapter 5, each
AM station needs 10 kHz of bandwidth. Each station uses a different carrier frequency,
which means it is shifting its signal and multiplexing. The signal that goes to the air is a
combination of signals. A receiver receives all these signals, but filters (by tuning) only
the one which is desired. Without multiplexing, only one AM station could broadcast
to the common link, the air. However, we need to know that there is no physical multiplexer or demultiplexer here. As we will see in Chapter 12, multiplexing is done at the
data-link layer.
The situation is similar in FM broadcasting. However, FM has a wider band of 88
to 108 MHz because each station needs a bandwidth of 200 kHz.
Another common use of FDM is in television broadcasting. Each TV channel has
its own bandwidth of 6 MHz.
The first generation of cellular telephones (See Chapter 16) also uses FDM. Each
user is assigned two 30-kHz channels, one for sending voice and the other for receiving. The voice signal, which has a bandwidth of 3 kHz (from 300 to 3300 Hz), is modulated by using FM. Remember that an FM signal has a bandwidth 10 times that of the
modulating signal, which means each channel has 30 kHz (10 × 3) of bandwidth.
Therefore, each user is given, by the base station, a 60-kHz bandwidth in a range available at the time of the call.

##### Example 6.4
> id: ch06-example-6-4 | src: book Example 6.4 | kind: worked_example
The Advanced Mobile Phone System (AMPS) uses two bands. The first band of 824 to 849 MHz
is used for sending, and 869 to 894 MHz is used for receiving. Each user has a bandwidth of
30 kHz in each direction. The 3-kHz voice is modulated using FM, creating 30 kHz of modulated
signal. How many people can use their cellular phones simultaneously?
**Solution**
Each band is 25 MHz. If we divide 25 MHz by 30 kHz, we get 833.33. In reality, the band
is divided into 832 channels. Of these, 42 channels are used for control, which means only
790 channels are available for cellular phone users. We discuss AMPS in greater detail in
Chapter 16.

#### Implementation
> id: ch06-6-1-1-implementation | src: book p.162 | kind: concept

FDM can be implemented very easily. In many cases, such as radio and television
broadcasting, there is no need for a physical multiplexer or demultiplexer. As long as
the stations agree to send their broadcasts to the air using different carrier frequencies,
multiplexing is achieved. In other cases, such as the cellular telephone system, a base
station needs to assign a carrier frequency to the telephone user. There is not enough
bandwidth in a cell to permanently assign a bandwidth range to every telephone user.
When a user hangs up, her or his bandwidth is assigned to another caller.

### 6.1.2 Wavelength-Division Multiplexing
> id: ch06-6-1-2 | src: book 6.1.2; p.162 | kind: concept

Wavelength-division multiplexing (WDM) is designed to use the high-data-rate
capability of fiber-optic cable. The optical fiber data rate is higher than the data rate of
metallic transmission cable, but using a fiber-optic cable for a single line wastes the
available bandwidth. Multiplexing allows us to combine several lines into one.
WDM is conceptually the same as FDM, except that the multiplexing and demultiplexing involve optical signals transmitted through fiber-optic channels. The idea is the
same: We are combining different signals of different frequencies. The difference is
that the frequencies are very high.
Figure 6.10 gives a conceptual view of a WDM multiplexer and demultiplexer.
Very narrow bands of light from different sources are combined to make a wider band
of light. At the receiver, the signals are separated by the demultiplexer.

> **[ASSET ch06_ill_010]** Figure 6.10: Wavelength-division multiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_010.png
> - src: book Figure 6.10; p.162
> - shows: Figure 6.10: Wavelength-division multiplexing. Three optical wavelengths enter a wavelength multiplexer, travel together through one fiber, and are separated by a wavelength demultiplexer at the far end.
> - structure: Three optical wavelengths enter a wavelength multiplexer, travel together through one fiber, and are separated by a wavelength demultiplexer at the far end.
> - text_in_image: λ1; λ1; D; M; E; λ2; λ2; U; M; λ1  +  λ2  +  λ3; X; U; X; λ3; λ3
> - use_when: Teach ch06-6-1-2, interpret Figure 6.10, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

WDM is an analog multiplexing technique to combine optical signals.

Although WDM technology is very complex, the basic idea is very simple. We
want to combine multiple light sources into one single light at the multiplexer and do
the reverse at the demultiplexer. The combining and splitting of light sources are easily
handled by a prism. Recall from basic physics that a prism bends a beam of light based
on the angle of incidence and the frequency. Using this technique, a multiplexer can be
made to combine several input beams of light, each containing a narrow band of
frequencies, into one output beam of a wider band of frequencies. A demultiplexer can
also be made to reverse the process. Figure 6.11 shows the concept.

> **[ASSET ch06_ill_011]** Figure 6.11: Prisms in wavelength-division multiplexing and demultiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_011.png
> - src: book Figure 6.11; p.163
> - shows: Figure 6.11: Prisms in wavelength-division multiplexing and demultiplexing. A prism combines three incident wavelengths into one fiber beam; a second prism separates the composite beam back into the original wavelengths.
> - structure: A prism combines three incident wavelengths into one fiber beam; a second prism separates the composite beam back into the original wavelengths.
> - text_in_image: λ1; λ1; λ1 + λ2 + λ3; λ2; λ2; Fiber-optic cable; λ3; λ3; Multiplexer; Demultiplexer
> - use_when: Teach ch06-6-1-2, interpret Figure 6.11, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

One application of WDM is the SONET network, in which multiple optical
fiber lines are multiplexed and demultiplexed. We discuss SONET in Chapter 14.
A new method, called dense WDM (DWDM), can multiplex a very large number of
channels by spacing channels very close to one another. It achieves even greater efficiency.

### 6.1.3 Time-Division Multiplexing
> id: ch06-6-1-3 | src: book 6.1.3; p.163 | kind: concept

Time-division multiplexing (TDM) is a digital process that allows several connections
to share the high bandwidth of a link. Instead of sharing a portion of the bandwidth as in
FDM, time is shared. Each connection occupies a portion of time in the link. Figure 6.12
gives a conceptual view of TDM. Note that the same link is used as in FDM; here, however, the link is shown sectioned by time rather than by frequency. In the figure, portions
of signals 1, 2, 3, and 4 occupy the link sequentially.

> **[ASSET ch06_ill_012]** Figure 6.12: TDM
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_012.png
> - src: book Figure 6.12; p.163
> - shows: Figure 6.12: TDM. Four digital input streams feed a TDM multiplexer. Successive source units occupy repeating time slots in the shared output stream and a demultiplexer restores the four outputs.
> - structure: Four digital input streams feed a TDM multiplexer. Successive source units occupy repeating time slots in the shared output stream and a demultiplexer restores the four outputs.
> - text_in_image: 1; 1; Data flow; 2; 2; D; E; M; 4; 3; 2; 1; 4; 3; 2; 1; 4; 3; 2; 1; M; U; 3; 3; U; X; X; 4; 4
> - use_when: Teach ch06-6-1-3, interpret Figure 6.12, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

Note that in Figure 6.12 we are concerned with only multiplexing, not switching.
This means that all the data in a message from source 1 always go to one specific destination, be it 1, 2, 3, or 4. The delivery is fixed and unvarying, unlike switching.
We also need to remember that TDM is, in principle, a digital multiplexing technique.
Digital data from different sources are combined into one timeshared link. However, this
does not mean that the sources cannot produce analog data; analog data can be sampled,
changed to digital data, and then multiplexed by using TDM.

TDM is a digital multiplexing technique for combining
several low-rate channels into one high-rate one.

We can divide TDM into two different schemes: synchronous and statistical. We
first discuss synchronous TDM and then show how statistical TDM differs.

#### Synchronous TDM
> id: ch06-6-1-3-synchronous-tdm | src: book p.164 | kind: concept

In synchronous TDM, each input connection has an allotment in the output even if it is
not sending data.

#### Time Slots and Frames
> id: ch06-6-1-3-time-slots-and-frames | src: book p.164 | kind: concept

In synchronous TDM, the data flow of each input connection is divided into units,
where each input occupies one input time slot. A unit can be 1 bit, one character, or one
block of data. Each input unit becomes one output unit and occupies one output time
slot. However, the duration of an output time slot is n times shorter than the duration of
an input time slot. If an input time slot is T s, the output time slot is T/n s, where n is the
number of connections. In other words, a unit in the output connection has a shorter
duration; it travels faster. Figure 6.13 shows an example of synchronous TDM where n
is 3.

> **[ASSET ch06_ill_013]** Figure 6.13: Synchronous time-division multiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_013.png
> - src: book Figure 6.13; p.164
> - shows: Figure 6.13: Synchronous time-division multiplexing. Three input lines contribute one unit every T seconds. Each output frame contains three slots of duration T/3, preserving source order across successive frames.
> - structure: Three input lines contribute one unit every T seconds. Each output frame contains three slots of duration T/3, preserving source order across successive frames.
> - text_in_image: T; T; T; T; T/3; A3; A2; A1; C3 B3; A3; C2 B2; A2; C1 B1; A1; B3; B2; B1; Frame 3; Frame 2; Frame 1; MUX; TDM; Each frame is 3 time slots.; Each time slot duration is T/3 s.; C3; C2; C1; Data are taken from each; line every T s.
> - use_when: Teach ch06-6-1-3-time-slots-and-frames, interpret Figure 6.13, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

In synchronous TDM, a round of data units from each input connection is collected
into a frame (we will see the reason for this shortly). If we have n connections, a frame
is divided into n time slots and one slot is allocated for each unit, one for each input
line. If the duration of the input unit is T, the duration of each slot is T/n and the duration of each frame is T (unless a frame carries some other information, as we will see
shortly).
The data rate of the output link must be n times the data rate of a connection to
guarantee the flow of data. In Figure 6.13, the data rate of the link is 3 times the data
rate of a connection; likewise, the duration of a unit on a connection is 3 times that of
the time slot (duration of a unit on the link). In the figure we represent the data prior to
multiplexing as 3 times the size of the data after multiplexing. This is just to convey the
idea that each unit is 3 times longer in duration before multiplexing than after.

In synchronous TDM, the data rate of the link is n times faster,
and the unit duration is n times shorter.

Time slots are grouped into frames. A frame consists of one complete cycle of
time slots, with one slot dedicated to each sending device. In a system with n input
lines, each frame has n slots, with each slot allocated to carrying data from a specific
input line.

##### Example 6.5
> id: ch06-example-6-5 | src: book Example 6.5 | kind: worked_example
In Figure 6.13, the data rate for each input connection is 1 kbps. If 1 bit at a time is multiplexed
(a unit is 1 bit), what is the duration of
1. each input slot,
2. each output slot, and
3. each frame?

**Solution**
We can answer the questions as follows:
1. The data rate of each input connection is 1 kbps. This means that the bit duration is 1/1000 s
or 1 ms. The duration of the input time slot is 1 ms (same as bit duration).
2. The duration of each output time slot is one-third of the input time slot. This means that the
duration of the output time slot is 1/3 ms.
3. Each frame carries three output time slots. So the duration of a frame is 3 × 1/3 ms, or 1 ms.
The duration of a frame is the same as the duration of an input unit.

##### Example 6.6
> id: ch06-example-6-6 | src: book Example 6.6 | kind: worked_example
Figure 6.14 shows synchronous TDM with a data stream for each input and one data stream for
the output. The unit of data is 1 bit. Find (1) the input bit duration, (2) the output bit duration,
(3) the output bit rate, and (4) the output frame rate.

> **[ASSET ch06_ill_014]** Figure 6.14: Example 6.6
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_014.png
> - src: book Figure 6.14; p.165
> - shows: Figure 6.14: Example 6.6. Four 1 Mbps bit streams are interleaved one bit at a time into a sequence of four-bit frames, illustrating the input and output patterns used in Example 6.6.
> - structure: Four 1 Mbps bit streams are interleaved one bit at a time into a sequence of four-bit frames, illustrating the input and output patterns used in Example 6.6.
> - text_in_image: • • •; 1       1       1       1       1; 1 Mbps; Frames; • • •; 0       0       0       0       0; 1 Mbps; • • • 0 1 0 1 0 0 0 1 1 1 0 1 0 0 0 1 0 1 0 1; MUX; • • •; 1       0       1       0       1; 1 Mbps; • • •; 0       0       1       0       0; 1 Mbps
> - use_when: Teach ch06-example-6-6, interpret Figure 6.14, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

**Solution**
We can answer the questions as follows:
1. The input bit duration is the inverse of the bit rate: 1/1 Mbps = 1 μs.
2. The output bit duration is one-fourth of the input bit duration, or 1/4 μs.
3. The output bit rate is the inverse of the output bit duration, or 1/4 μs, or 4 Mbps. This can
also be deduced from the fact that the output rate is 4 times as fast as any input rate; so the
output rate = 4 × 1 Mbps = 4 Mbps.
4. The frame rate is always the same as any input rate. So the frame rate is 1,000,000 frames
per second. Because we are sending 4 bits in each frame, we can verify the result of the previous question by multiplying the frame rate by the number of bits per frame.

##### Example 6.7
> id: ch06-example-6-7 | src: book Example 6.7 | kind: worked_example
Four 1-kbps connections are multiplexed together. A unit is 1 bit. Find (1) the duration of 1 bit
before multiplexing, (2) the transmission rate of the link, (3) the duration of a time slot, and
(4) the duration of a frame.

**Solution**
We can answer the questions as follows:
1. The duration of 1 bit before multiplexing is 1/1 kbps, or 0.001 s (1 ms).
2. The rate of the link is 4 times the rate of a connection, or 4 kbps.
3. The duration of each time slot is one-fourth of the duration of each bit before multiplexing,
or 1/4 ms or 250 μs. Note that we can also calculate this from the data rate of the link, 4 kbps.
The bit duration is the inverse of the data rate, or 1/4 kbps or 250 μs.
4. The duration of a frame is always the same as the duration of a unit before multiplexing, or
1 ms. We can also calculate this in another way. Each frame in this case has four time slots.
So the duration of a frame is 4 times 250 μs, or 1 ms.

#### Interleaving
> id: ch06-6-1-3-interleaving | src: book p.166 | kind: concept

TDM can be visualized as two fast-rotating switches, one on the multiplexing side and
the other on the demultiplexing side. The switches are synchronized and rotate at the
same speed, but in opposite directions. On the multiplexing side, as the switch opens in
front of a connection, that connection has the opportunity to send a unit onto the path.
This process is called interleaving. On the demultiplexing side, as the switch opens in
front of a connection, that connection has the opportunity to receive a unit from the
path.
Figure 6.15 shows the interleaving process for the connection shown in Figure 6.13.
In this figure, we assume that no switching is involved and that the data from the first
connection at the multiplexer site go to the first connection at the demultiplexer. We
discuss switching in Chapter 8.

##### Example 6.8
> id: ch06-example-6-8 | src: book Example 6.8 | kind: worked_example
Four channels are multiplexed using TDM. If each channel sends 100 bytes/s and we multiplex
1 byte per channel, show the frame traveling on the link, the size of the frame, the duration of a
frame, the frame rate, and the bit rate for the link.

**Solution**
The multiplexer is shown in Figure 6.16. Each frame carries 1 byte from each channel; the size of
each frame, therefore, is 4 bytes, or 32 bits. Because each channel is sending 100 bytes/s and a
frame carries 1 byte from each channel, the frame rate must be 100 frames per second. The

> **[ASSET ch06_ill_015]** Figure 6.15: Interleaving
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_015.png
> - src: book Figure 6.15; p.167
> - shows: Figure 6.15: Interleaving. Synchronized rotating switches visit inputs and outputs in opposite directions, interleaving A, B, and C units into matching frame slots and delivering them to the corresponding lines.
> - structure: Synchronized rotating switches visit inputs and outputs in opposite directions, interleaving A, B, and C units into matching frame slots and delivering them to the corresponding lines.
> - text_in_image: Synchronization; A3; A2; A1; A3; A2; A1; Frame 3; Frame 2; Frame 1; C2; C3; B3; A3; B2; A2; C1; B1; A1; B2; B1; B3; B2; B1; B3; C3; C2; C1; C3; C2; C1
> - use_when: Teach ch06-6-1-3-interleaving, interpret Figure 6.15, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

duration of a frame is therefore 1/100 s. The link is carrying 100 frames per second, and since
each frame contains 32 bits, the bit rate is 100 × 32, or 3200 bps. This is actually 4 times the bit
rate of each channel, which is 100 × 8 = 800 bps.

> **[ASSET ch06_ill_016]** Figure 6.16: Example 6.8
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_016.png
> - src: book Figure 6.16; p.167
> - shows: Figure 6.16: Example 6.8. Four 100-byte-per-second sources contribute one byte per frame. Each frame is four bytes or 32 bits, the frame rate is 100 frames/s, and the link rate is 3200 bps.
> - structure: Four 100-byte-per-second sources contribute one byte per frame. Each frame is four bytes or 32 bits, the frame rate is 100 frames/s, and the link rate is 3200 bps.
> - text_in_image: Frame 4 bytes; Frame 4 bytes; 32 bits; 32 bits; • • •; MUX; 100 frames/s; 1; Frame duration =        s; 3200 bps; 100; 100 bytes/s
> - use_when: Teach ch06-example-6-8, interpret Figure 6.16, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

##### Example 6.9
> id: ch06-example-6-9 | src: book Example 6.9 | kind: worked_example
A multiplexer combines four 100-kbps channels using a time slot of 2 bits. Show the output with
four arbitrary inputs. What is the frame rate? What is the frame duration? What is the bit rate?
What is the bit duration?

**Solution**
Figure 6.17 shows the output for four arbitrary inputs. The link carries 50,000 frames per second
since each frame contains 2 bits per channel. The frame duration is therefore 1/50,000 s or 20 μs.
The frame rate is 50,000 frames per second, and each frame carries 8 bits; the bit rate is 50,000 ×
8 = 400,000 bits or 400 kbps. The bit duration is 1/400,000 s, or 2.5 μs. Note that the frame duration is 8 times the bit duration because each frame is carrying 8 bits.

#### Empty Slots
> id: ch06-6-1-3-empty-slots | src: book p.167 | kind: concept

Synchronous TDM is not as efficient as it could be. If a source does not have data to
send, the corresponding slot in the output frame is empty. Figure 6.18 shows a case in
which one of the input lines has no data to send and one slot in another input line has
discontinuous data.
The first output frame has three slots filled, the second frame has two slots filled,
and the third frame has three slots filled. No frame is full. We learn in the next section

> **[ASSET ch06_ill_017]** Figure 6.17: Example 6.9
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_017.png
> - src: book Figure 6.17; p.168
> - shows: Figure 6.17: Example 6.9. Four 100 kbps sources contribute two bits per frame. Eight-bit frames repeat at 50,000 frames/s, giving a 20 microsecond frame duration and a 400 kbps link rate.
> - structure: Four 100 kbps sources contribute two bits per frame. Eight-bit frames repeat at 50,000 frames/s, giving a 20 microsecond frame duration and a 400 kbps link rate.
> - text_in_image: Frame duration = 1/50,000 s = 20 μs; 1 1 0 0 1 0; • • •; 100 kbps; Frame: 8 bits; Frame: 8 bits; Frame: 8 bits; 0 0 1 0 1 0; • • •; • • •; 00; 10; 00; 11; 01; 11; 10; 00; 11; 01; 10; 10; 100 kbps; MUX; 1 0 1 1 0 1; • • •; 50,000 frames/s; 100 kbps; 400 kbps; 0 0 0 1 1 1; • • •; 100 kbps
> - use_when: Teach ch06-example-6-9, interpret Figure 6.17, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

> **[ASSET ch06_ill_018]** Figure 6.18: Empty slots
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_018.png
> - src: book Figure 6.18; p.168
> - shows: Figure 6.18: Empty slots. Synchronous TDM reserves a position for every source in each frame; inactive sources therefore create visibly empty output slots.
> - structure: Synchronous TDM reserves a position for every source in each frame; inactive sources therefore create visibly empty output slots.
> - text_in_image: MUX
> - use_when: Teach ch06-6-1-3-empty-slots, interpret Figure 6.18, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

that statistical TDM can improve the efficiency by removing the empty slots from the
frame.

#### Data Rate Management
> id: ch06-6-1-3-data-rate-management | src: book p.168 | kind: concept

One problem with TDM is how to handle a disparity in the input data rates. In all our
discussion so far, we assumed that the data rates of all input lines were the same. However,
if data rates are not the same, three strategies, or a combination of them, can be used.
We call these three strategies multilevel multiplexing, multiple-slot allocation, and
pulse stuffing.

#### Multilevel Multiplexing
> id: ch06-6-1-3-multilevel-multiplexing | src: book p.168 | kind: concept

Multilevel multiplexing is a technique used when the data
rate of an input line is a multiple of others. For example, in Figure 6.19, we have two
inputs of 20 kbps and three inputs of 40 kbps. The first two input lines can be multiplexed
together to provide a data rate equal to the last three. A second level of multiplexing can
create an output of 160 kbps.

> **[ASSET ch06_ill_019]** Figure 6.19: Multilevel multiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_019.png
> - src: book Figure 6.19; p.168
> - shows: Figure 6.19: Multilevel multiplexing. Two 20 kbps inputs are first combined to match three 40 kbps inputs; a final multiplexer interleaves four equal-rate streams into a 160 kbps link.
> - structure: Two 20 kbps inputs are first combined to match three 40 kbps inputs; a final multiplexer interleaves four equal-rate streams into a 160 kbps link.
> - text_in_image: 20 kbps; 40 kbps; 20 kbps; 40 kbps; 160 kbps; MUX; 40 kbps; 40 kbps
> - use_when: Teach ch06-6-1-3-multilevel-multiplexing, interpret Figure 6.19, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### Multiple-Slot Allocation
> id: ch06-6-1-3-multiple-slot-allocation | src: book p.169 | kind: concept

Sometimes it is more efficient to allot more than one slot in
a frame to a single input line. For example, we might have an input line that has a data
rate that is a multiple of another input. In Figure 6.20, the input line with a 50-kbps
data rate can be given two slots in the output. We insert a demultiplexer in the line to
make two inputs out of one.

> **[ASSET ch06_ill_020]** Figure 6.20: Multiple-slot multiplexing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_020.png
> - src: book Figure 6.20; p.169
> - shows: Figure 6.20: Multiple-slot multiplexing. One 50 kbps input receives two slots per frame while three 25 kbps inputs receive one each, yielding five-slot frames on a 125 kbps link.
> - structure: One 50 kbps input receives two slots per frame while three 25 kbps inputs receive one each, yielding five-slot frames on a 125 kbps link.
> - text_in_image: 25 kbps; 50 kbps; 25 kbps; • • •; M; 25 kbps; 125 kbps; U; The input with a; X; 25 kbps; 50-kHz data rate has two; slots in each frame.; 25 kbps
> - use_when: Teach ch06-6-1-3-multiple-slot-allocation, interpret Figure 6.20, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### Pulse Stuffing
> id: ch06-6-1-3-pulse-stuffing | src: book p.169 | kind: concept

Sometimes the bit rates of sources are not multiple integers of each
other. Therefore, neither of the above two techniques can be applied. One solution is to
make the highest input data rate the dominant data rate and then add dummy bits to the
input lines with lower rates. This will increase their rates. This technique is called pulse
stuffing, bit padding, or bit stuffing. The idea is shown in Figure 6.21. The input with a
data rate of 46 is pulse-stuffed to increase the rate to 50 kbps. Now multiplexing can
take place.

> **[ASSET ch06_ill_021]** Figure 6.21: Pulse stuffing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_021.png
> - src: book Figure 6.21; p.169
> - shows: Figure 6.21: Pulse stuffing. A pulse-stuffing block raises a 46 kbps input to 50 kbps so it can be multiplexed with two native 50 kbps inputs into a 150 kbps output.
> - structure: A pulse-stuffing block raises a 46 kbps input to 50 kbps so it can be multiplexed with two native 50 kbps inputs into a 150 kbps output.
> - text_in_image: 50 kbps; 150 kbps; M; 50 kbps; U; 50 kbps; X; Pulse; 46 kbps; stuffing
> - use_when: Teach ch06-6-1-3-pulse-stuffing, interpret Figure 6.21, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### Frame Synchronizing
> id: ch06-6-1-3-frame-synchronizing | src: book p.169 | kind: concept

The implementation of TDM is not as simple as that of FDM. Synchronization between
the multiplexer and demultiplexer is a major issue. If the multiplexer and the demultiplexer are not synchronized, a bit belonging to one channel may be received by the
wrong channel. For this reason, one or more synchronization bits are usually added to
the beginning of each frame. These bits, called framing bits, follow a pattern, frame
to frame, that allows the demultiplexer to synchronize with the incoming stream so that
it can separate the time slots accurately. In most cases, this synchronization information
consists of 1 bit per frame, alternating between 0 and 1, as shown in Figure 6.22.

> **[ASSET ch06_ill_022]** Figure 6.22: Framing bits
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_022.png
> - src: book Figure 6.22; p.170
> - shows: Figure 6.22: Framing bits. Successive three-slot frames carry a leading synchronization bit that follows the repeating 1-0-1 pattern, allowing the receiver to locate frame boundaries.
> - structure: Successive three-slot frames carry a leading synchronization bit that follows the repeating 1-0-1 pattern, allowing the receiver to locate frame boundaries.
> - text_in_image: Synchronization; 1      0      1; pattern; Frame 3; Frame 2; Frame 1; C3; B3; A3; B2; A2; C1; A1; 1; 0; 1
> - use_when: Teach ch06-6-1-3-frame-synchronizing, interpret Figure 6.22, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

##### Example 6.10
> id: ch06-example-6-10 | src: book Example 6.10 | kind: worked_example
We have four sources, each creating 250 characters per second. If the interleaved unit is a character and 1 synchronizing bit is added to each frame, find (1) the data rate of each source, (2) the
duration of each character in each source, (3) the frame rate, (4) the duration of each frame,
(5) the number of bits in each frame, and (6) the data rate of the link.

**Solution**
We can answer the questions as follows:
1. The data rate of each source is 250 × 8 = 2000 bps = 2 kbps.
2. Each source sends 250 characters per second; therefore, the duration of a character is 1/250 s,
or 4 ms.
3. Each frame has one character from each source, which means the link needs to send
250 frames per second to keep the transmission rate of each source.
4. The duration of each frame is 1/250 s, or 4 ms. Note that the duration of each frame is the
same as the duration of each character coming from each source.
5. Each frame carries 4 characters and 1 extra synchronizing bit. This means that each frame is
4 × 8 + 1 = 33 bits.
6. The link sends 250 frames per second, and each frame contains 33 bits. This means that the
data rate of the link is 250 × 33, or 8250 bps. Note that the bit rate of the link is greater than
the combined bit rates of the four channels. If we add the bit rates of four channels, we get
8000 bps. Because 250 frames are traveling per second and each contains 1 extra bit for
synchronizing, we need to add 250 to the sum to get 8250 bps.

##### Example 6.11
> id: ch06-example-6-11 | src: book Example 6.11 | kind: worked_example
Two channels, one with a bit rate of 100 kbps and another with a bit rate of 200 kbps, are to be
multiplexed. How this can be achieved? What is the frame rate? What is the frame duration?
What is the bit rate of the link?

**Solution**
We can allocate one slot to the first channel and two slots to the second channel. Each frame carries 3 bits. The frame rate is 100,000 frames per second because it carries 1 bit from the first
channel. The frame duration is 1/100,000 s, or 10 μs. The bit rate is 100,000 frames/s × 3 bits per
frame, or 300 kbps. Note that because each frame carries 1 bit from the first channel, the bit rate
for the first channel is preserved. The bit rate for the second channel is also preserved because
each frame carries 2 bits from the second channel.

#### Digital Signal Service
> id: ch06-6-1-3-digital-signal-service | src: book p.171 | kind: concept

Telephone companies implement TDM through a hierarchy of digital signals, called
digital signal (DS) service or digital hierarchy. Figure 6.23 shows the data rates supported by each level.

> **[ASSET ch06_ill_023]** Figure 6.23: Digital hierarchy (source DS-3 label corrected in teaching text by Table 6.1)
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_023.png
> - src: book Figure 6.23; p.171
> - shows: Figure 6.23: Digital hierarchy (source DS-3 label corrected in teaching text by Table 6.1). The digital hierarchy multiplexes 24 DS-0 channels into DS-1, four DS-1 streams into DS-2, seven DS-2 streams into DS-3, and six DS-3 streams into DS-4. The source figure prints 44.376 Mbps for DS-3; Table 6.1 gives 44.736 Mbps.
> - structure: The digital hierarchy multiplexes 24 DS-0 channels into DS-1, four DS-1 streams into DS-2, seven DS-2 streams into DS-3, and six DS-3 streams into DS-4. The source figure prints 44.376 Mbps for DS-3; Table 6.1 gives 44.736 Mbps.
> - text_in_image: 6.312 Mbps; DS-0; 4 DS-1; 44.376 Mbps; T; DS-1; 7 DS-2; 24; D; • • •; T; DS-2; M; 274.176 Mbps; D; 6 DS-3; M; T; DS-3; D; M; 64 kbps; T; DS-4; D; 1.544 Mbps; 24 DS-0; M
> - use_when: Teach ch06-6-1-3-digital-signal-service, interpret Figure 6.23, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

- DS-0 is a single digital channel of 64 kbps.

- DS-1 is a 1.544-Mbps service; 1.544 Mbps is 24 times 64 kbps plus 8 kbps of overhead. It can be used as a single service for 1.544-Mbps transmissions, or it can be
used to multiplex 24 DS-0 channels or to carry any other combination desired by
the user that can fit within its 1.544-Mbps capacity.

- DS-2 is a 6.312-Mbps service; 6.312 Mbps is 96 times 64 kbps plus 168 kbps of
overhead. It can be used as a single service for 6.312-Mbps transmissions; or it can
be used to multiplex 4 DS-1 channels, 96 DS-0 channels, or a combination of these
service types.

- DS-3 is a 44.736-Mbps service; 44.736 Mbps is 672 times 64 kbps plus 1.728 Mbps
of overhead. It can be used as a single service for 44.736-Mbps transmissions; or it
can be used to multiplex 7 DS-2 channels, 28 DS-1 channels, 672 DS-0 channels,
or a combination of these service types.

- DS-4 is a 274.176-Mbps service; 274.176 is 4032 times 64 kbps plus 16.128 Mbps of
overhead. It can be used to multiplex 6 DS-3 channels, 42 DS-2 channels, 168 DS-1
channels, 4032 DS-0 channels, or a combination of these service types.

#### T Lines
> id: ch06-6-1-3-t-lines | src: book p.171 | kind: concept

DS-0, DS-1, and so on are the names of services. To implement those services, the telephone companies use T lines (T-1 to T-4). These are lines with capacities precisely
matched to the data rates of the DS-1 to DS-4 services (see Table 6.1). So far only T-1
and T-3 lines are commercially available.
**Table 6.1: DS and T line rates**

| Service | Line | Rate (Mbps) | Voice Channels |
| --- | --- | --- | --- |
| DS-1 | T-1 | 1.544 | 24 |
| DS-2 | T-2 | 6.312 | 96 |
| DS-3 | T-3 | 44.736 | 672 |
| DS-4 | T-4 | 274.176 | 4032 |

The T-1 line is used to implement DS-1; T-2 is used to implement DS-2; and so on.
As you can see from Table 6.1, DS-0 is not actually offered as a service, but it has been
defined as a basis for reference purposes.

#### T Lines for Analog Transmission
> id: ch06-6-1-3-t-lines-for-analog-transmission | src: book p.172 | kind: concept

T lines are digital lines designed for the transmission of digital data, audio, or
video. However, they also can be used for analog transmission (regular telephone
connections), provided the analog signals are first sampled, then time-division
multiplexed.
The possibility of using T lines as analog carriers opened up a new generation of
services for the telephone companies. Earlier, when an organization wanted 24 separate
telephone lines, it needed to run 24 twisted-pair cables from the company to the central
exchange. (Remember those old movies showing a busy executive with 10 telephones
lined up on his desk? Or the old office telephones with a big fat cable running from
them? Those cables contained a bundle of separate lines.) Today, that same organization
can combine the 24 lines into one T-1 line and run only the T-1 line to the exchange.
Figure 6.24 shows how 24 voice channels can be multiplexed onto one T-1 line. (Refer
to Chapter 4 for PCM encoding.)

> **[ASSET ch06_ill_024]** Figure 6.24: T-1 line for multiplexing telephone lines
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_024.png
> - src: book Figure 6.24; p.172
> - shows: Figure 6.24: T-1 line for multiplexing telephone lines. Twenty-four 4 kHz voice channels are sampled at 8000 samples/s and encoded with 8-bit PCM, producing 64 kbps channels that TDM combines with 8 kbps overhead into a 1.544 Mbps T-1 line.
> - structure: Twenty-four 4 kHz voice channels are sampled at 8000 samples/s and encoded with 8-bit PCM, producing 64 kbps channels that TDM combines with 8 kbps overhead into a 1.544 Mbps T-1 line.
> - text_in_image: Sampling at 8000 samples/s; using 8 bits per sample; PCM; 24 Voice channels; T-1 line 1.544 Mbps; T; 24 × 64 kbps + 8 kbps overhead; D; PCM; M; • • •; • • •; 4 kHz; 64,000 bps; PCM
> - use_when: Teach ch06-6-1-3-t-lines-for-analog-transmission, interpret Figure 6.24, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### The T-1 Frame
> id: ch06-6-1-3-the-t-1-frame | src: book p.172 | kind: concept

As noted above, DS-1 requires 8 kbps of overhead. To understand
how this overhead is calculated, we must examine the format of a 24-voice-channel
frame.
The frame used on a T-1 line is usually 193 bits divided into 24 slots of 8 bits each
plus 1 extra bit for synchronization (24 × 8 + 1 = 193); see Figure 6.25. In other words,

> **[ASSET ch06_ill_025]** Figure 6.25: T-1 frame structure
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_025.png
> - src: book Figure 6.25; p.173
> - shows: Figure 6.25: T-1 frame structure. A T-1 frame contains one synchronization bit followed by twenty-four 8-bit channel samples, totaling 193 bits. Sending 8000 frames/s produces 1.544 Mbps.
> - structure: A T-1 frame contains one synchronization bit followed by twenty-four 8-bit channel samples, totaling 193 bits. Sending 8000 frames/s produces 1.544 Mbps.
> - text_in_image: Sample n; Channel; Channel; Channel; • • •; 24; 2; 1; 1 bit 8 bits; 8 bits; 8 bits; 1 frame = 193 bits; Frame; Frame; Frame; Frame; • • •; • • •; 8000; 2; 1; n; T-1: 8000 frames/s = 8000 × 193 bps = 1.544 Mbps
> - use_when: Teach ch06-6-1-3-the-t-1-frame, interpret Figure 6.25, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

each slot contains one signal segment from each channel; 24 segments are interleaved
in one frame. If a T-1 line carries 8000 frames, the data rate is 1.544 Mbps (193 × 8000 =
1.544 Mbps)—the capacity of the line.

#### E Lines
> id: ch06-6-1-3-e-lines | src: book p.173 | kind: concept

Europeans use a version of T lines called E lines. The two systems are conceptually
identical, but their capacities differ. Table 6.2 shows the E lines and their capacities.

**Table 6.2: E line rates**

| Line | Rate (Mbps) | Voice Channels |
| --- | --- | --- |
| E-1 | 2.048 | 30 |
| E-2 | 8.448 | 120 |
| E-3 | 34.368 | 480 |
| E-4 | 139.264 | 1920 |

#### More Synchronous TDM Applications
> id: ch06-6-1-3-more-synchronous-tdm-applications | src: book p.173 | kind: concept

Some second-generation cellular telephone companies use synchronous TDM. For
example, the digital version of cellular telephony divides the available bandwidth into
30-kHz bands. For each band, TDM is applied so that six users can share the band. This
means that each 30-kHz band is now made of six time slots, and the digitized voice
signals of the users are inserted in the slots. Using TDM, the number of telephone users
in each area is now 6 times greater. We discuss second-generation cellular telephony in
Chapter 16.

#### Statistical Time-Division Multiplexing
> id: ch06-6-1-3-statistical-time-division-multiplexing | src: book p.174 | kind: concept

As we saw in the previous section, in synchronous TDM, each input has a reserved slot
in the output frame. This can be inefficient if some input lines have no data to send. In
statistical time-division multiplexing, slots are dynamically allocated to improve bandwidth efficiency. Only when an input line has a slot’s worth of data to send is it given a
slot in the output frame. In statistical multiplexing, the number of slots in each frame is
less than the number of input lines. The multiplexer checks each input line in round-robin fashion; it allocates a slot for an input line if the line has data to send; otherwise,
it skips the line and checks the next line.
Figure 6.26 shows a synchronous and a statistical TDM example. In the former,
some slots are empty because the corresponding line does not have data to send. In the
latter, however, no slot is left empty as long as there are data to be sent by any input
line.

> **[ASSET ch06_ill_026]** Figure 6.26: TDM slot comparison
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_026.png
> - src: book Figure 6.26; p.174
> - shows: Figure 6.26: TDM slot comparison. Parallel panels compare synchronous TDM, which emits reserved and sometimes empty slots, with statistical TDM, which emits only active data slots plus source addresses.
> - structure: Parallel panels compare synchronous TDM, which emits reserved and sometimes empty slots, with statistical TDM, which emits only active data slots plus source addresses.
> - text_in_image: Line A; A1; B2; B1; Line B; 0; E2; D2; B2; 1; D1; B1; A1; Line C; MUX; Line D; D2; D1; a. Synchronous TDM; E2; Line E; Line A; A1; B2; B1; Line B; e; E2; d; D2; b; B2; d; D1; b; B1; a; A1; Line C; MUX; Line D; D2; D1; b. Statistical TDM; E2; Line E
> - use_when: Teach ch06-6-1-3-statistical-time-division-multiplexing, interpret Figure 6.26, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

#### Addressing
> id: ch06-6-1-3-addressing | src: book p.174 | kind: concept

Figure 6.26 also shows a major difference between slots in synchronous TDM and statistical TDM. An output slot in synchronous TDM is totally occupied by data; in statistical TDM, a slot needs to carry data as well as the address of the destination.
In synchronous TDM, there is no need for addressing; synchronization and preassigned
relationships between the inputs and outputs serve as an address. We know, for example, that input 1 always goes to input 2. If the multiplexer and the demultiplexer are
synchronized, this is guaranteed. In statistical multiplexing, there is no fixed relationship between the inputs and outputs because there are no preassigned or reserved slots.
We need to include the address of the receiver inside each slot to show where it is to be
delivered. The addressing in its simplest form can be n bits to define N different output
lines with $n=\log_2 N$. For example, for eight different output lines, we need a 3-bit
address.

#### Slot Size
> id: ch06-6-1-3-slot-size | src: book p.175 | kind: concept

Since a slot carries both data and an address in statistical TDM, the ratio of the data size
to address size must be reasonable to make transmission efficient. For example, it
would be inefficient to send 1 bit per slot as data when the address is 3 bits. This would
mean an overhead of 300 percent. In statistical TDM, a block of data is usually many
bytes while the address is just a few bytes.

#### No Synchronization Bit
> id: ch06-6-1-3-no-synchronization-bit | src: book p.175 | kind: concept

There is another difference between synchronous and statistical TDM, but this time it is
at the frame level. The frames in statistical TDM need not be synchronized, so we do not
need synchronization bits.

#### Bandwidth
> id: ch06-6-1-3-bandwidth | src: book p.175 | kind: concept

In statistical TDM, the capacity of the link is normally less than the sum of the capacities of each channel. The designers of statistical TDM define the capacity of the link
based on the statistics of the load for each channel. If on average only x percent of the
input slots are filled, the capacity of the link reflects this. Of course, during peak times,
some slots need to wait.

## 6.2 SPREAD SPECTRUM
> id: ch06-6-2 | src: book 6.2; p.175 | kind: concept

Multiplexing combines signals from several sources to achieve bandwidth efficiency;
the available bandwidth of a link is divided between the sources. In spread spectrum
(SS), we also combine signals from different sources to fit into a larger bandwidth, but
our goals are somewhat different. Spread spectrum is designed to be used in wireless
applications (LANs and WANs). In these types of applications, we have some concerns
that outweigh bandwidth efficiency. In wireless applications, all stations use air (or a
vacuum) as the medium for communication. Stations must be able to share this medium
without interception by an eavesdropper and without being subject to jamming from a
malicious intruder (in military operations, for example).
To achieve these goals, spread spectrum techniques add redundancy; they spread
the original spectrum needed for each station. If the required bandwidth for each station
is B, spread spectrum expands it to $B_{ss}$, such that $B_{\mathrm{SS}} \gg B$. The expanded bandwidth
allows the source to wrap its message in a protective envelope for a more secure transmission. An analogy is the sending of a delicate, expensive gift. We can insert the gift
in a special box to prevent it from being damaged during transportation, and we can use
a superior delivery service to guarantee the safety of the package.
Figure 6.27 shows the idea of spread spectrum. Spread spectrum achieves its goals
through two principles:
1. The bandwidth allocated to each station needs to be, by far, larger than what is
needed. This allows redundancy.
2. The expanding of the original bandwidth B to the bandwidth $B_{ss}$ must be done by a
process that is independent of the original signal. In other words, the spreading
process occurs after the signal is created by the source.

> **[ASSET ch06_ill_027]** Figure 6.27: Spread spectrum
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_027.png
> - src: book Figure 6.27; p.176
> - shows: Figure 6.27: Spread spectrum. A spreading process combines an original signal of bandwidth B with a spreading code to produce a signal occupying the wider bandwidth B_SS.
> - structure: A spreading process combines an original signal of bandwidth B with a spreading code to produce a signal occupying the wider bandwidth B_SS.
> - text_in_image: BSS; B; Spreading; process; Spreading; code
> - use_when: Teach ch06-6-2, interpret Figure 6.27, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

After the signal is created by the source, the spreading process uses a spreading
code and spreads the bandwidth. The figure shows the original bandwidth B and the
spread bandwidth $B_{\mathrm{SS}}$. The spreading code is a series of numbers that look random, but
are actually a pattern.
There are two techniques to spread the bandwidth: frequency hopping spread spectrum (FHSS) and direct sequence spread spectrum (DSSS).

### 6.2.1 Frequency Hopping Spread Spectrum
> id: ch06-6-2-1 | src: book 6.2.1; p.176 | kind: concept

The frequency hopping spread spectrum (FHSS) technique uses M different carrier
frequencies that are modulated by the source signal. At one moment, the signal modulates one carrier frequency; at the next moment, the signal modulates another carrier
frequency. Although the modulation is done using one carrier frequency at a time,
M frequencies are used in the long run. The bandwidth occupied by a source after
spreading is $B_{\mathrm{FHSS}} \gg B$.
Figure 6.28 shows the general layout for FHSS. A pseudorandom code generator,
called pseudorandom noise (PN), creates a k-bit pattern for every hopping period $T_{h}$.
The frequency table uses the pattern to find the frequency to be used for this hopping
period and passes it to the frequency synthesizer. The frequency synthesizer creates a
carrier signal of that frequency, and the source signal modulates the carrier signal.
Suppose we have decided to have eight hopping frequencies. This is extremely low
for real applications and is just for illustration. In this case, M is 8 and k is 3. The pseudorandom code generator will create eight different 3-bit patterns. These are mapped to
eight different frequencies in the frequency table (see Figure 6.29).
The pattern for this station is 101, 111, 001, 000, 010, 011, 100. Note that the pattern is pseudorandom; it is repeated after eight hoppings. This means that at hopping
period 1, the pattern is 101. The frequency selected is 700 kHz; the source signal modulates this carrier frequency. The second k-bit pattern selected is 111, which selects the
900-kHz carrier; the eighth pattern is 100, and the frequency is 600 kHz. After eight
hoppings, the pattern repeats, starting from 101 again. Figure 6.30 shows how the signal

> **[ASSET ch06_ill_028]** Figure 6.28: Frequency hopping spread spectrum (FHSS)
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_028.png
> - src: book Figure 6.28; p.177
> - shows: Figure 6.28: Frequency hopping spread spectrum (FHSS). An FHSS transmitter maps pseudorandom code words through a frequency table and synthesizer to select the carrier used by the modulator during each hop.
> - structure: An FHSS transmitter maps pseudorandom code words through a frequency table and synthesizer to select the carrier used by the modulator during each hop.
> - text_in_image: Modulator; Original; Spread; signal; signal; Frequency; synthesizer; code generator; Pseudorandom; Frequency table
> - use_when: Teach ch06-6-2-1, interpret Figure 6.28, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

> **[ASSET ch06_ill_029]** Figure 6.29: Frequency selection in FHSS
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_029.png
> - src: book Figure 6.29; p.177
> - shows: Figure 6.29: Frequency selection in FHSS. A 3-bit hopping sequence indexes a table that maps 000 through 111 to carriers from 200 through 900 kHz; the first code 101 selects 700 kHz.
> - structure: A 3-bit hopping sequence indexes a table that maps 000 through 111 to carriers from 200 through 900 kHz; the first code 101 selects 700 kHz.
> - text_in_image: First-hop frequency; k-bit; Frequency; 000; 200 kHz; k-bit patterns; 001; 300 kHz; 010; 400 kHz; 101; 111; 001; 000; 010; 110; 011 100; 011; 500 kHz; 100; 600 kHz; First selection; 101; 700 kHz; 110; 800 kHz; 111; 900 kHz; Frequency table
> - use_when: Teach ch06-6-2-1, interpret Figure 6.29, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

hops around from carrier to carrier. We assume the required bandwidth of the original
signal is 100 kHz.
It can be shown that this scheme can accomplish the previously mentioned goals. If
there are many k-bit patterns and the hopping period is short, a sender and receiver can
have privacy. If an intruder tries to intercept the transmitted signal, she can only access
a small piece of data because she does not know the spreading sequence to quickly
adapt herself to the next hop. The scheme also has an antijamming effect. A malicious
sender may be able to send noise to jam the signal for one hopping period (randomly),
but not for the whole period.

#### Bandwidth Sharing
> id: ch06-6-2-1-bandwidth-sharing | src: book p.177 | kind: concept

If the number of hopping frequencies is M, we can multiplex M channels into one by
using the same $B_{ss}$ bandwidth. This is possible because a station uses just one frequency
in each hopping period; M − 1 other frequencies can be used by M − 1 other stations. In

> **[ASSET ch06_ill_030]** Figure 6.30: FHSS cycles
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_030.png
> - src: book Figure 6.30; p.178
> - shows: Figure 6.30: FHSS cycles. A time-frequency grid plots two repeated FHSS cycles across eight hop periods each, with the carrier moving among 200-to-900 kHz channels according to the pseudorandom sequence.
> - structure: A time-frequency grid plots two repeated FHSS cycles across eight hop periods each, with the carrier moving among 200-to-900 kHz channels according to the pseudorandom sequence.
> - text_in_image: Carrier; frequencies; (kHz); Cycle 1; Cycle 2; 900; 800; 700; 600; 500; 400; 300; 200; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10 11 12 13 14 15 16; Hop; periods
> - use_when: Teach ch06-6-2-1-bandwidth-sharing, interpret Figure 6.30, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

other words, M different stations can use the same $B_{ss}$ if an appropriate modulation
technique such as multiple FSK (MFSK) is used. FHSS is similar to FDM, as shown in
Figure 6.31.

> **[ASSET ch06_ill_031]** Figure 6.31: Bandwidth sharing
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_031.png
> - src: book Figure 6.31; p.178
> - shows: Figure 6.31: Bandwidth sharing. An FDM panel assigns each station a fixed frequency band, while an FHSS panel shows stations changing bands from one time interval to the next without colliding.
> - structure: An FDM panel assigns each station a fixed frequency band, while an FHSS panel shows stations changing bands from one time interval to the next without colliding.
> - text_in_image: Frequency; Frequency; f4; f4; f3; f3; f2; f2; f1; f1; Time; Time; a. FDM; b. FHSS
> - use_when: Teach ch06-6-2-1-bandwidth-sharing, interpret Figure 6.31, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

Figure 6.31 shows an example of four channels using FDM and four channels using
FHSS. In FDM, each station uses 1/M of the bandwidth, but the allocation is fixed; in
FHSS, each station uses 1/M of the bandwidth, but the allocation changes hop to hop.

### 6.2.2 Direct Sequence Spread Spectrum
> id: ch06-6-2-2 | src: book 6.2.2; p.178 | kind: concept

The direct sequence spread spectrum (DSSS) technique also expands the bandwidth
of the original signal, but the process is different. In DSSS, we replace each data bit
with n bits using a spreading code. In other words, each bit is assigned a code of n bits,
called chips, where the chip rate is n times that of the data bit. Figure 6.32 shows the
concept of DSSS.

> **[ASSET ch06_ill_032]** Figure 6.32: DSSS
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_032.png
> - src: book Figure 6.32; p.179
> - shows: Figure 6.32: DSSS. A DSSS transmitter multiplies the original signal by a chip sequence from a chip generator, producing the spread signal.
> - structure: A DSSS transmitter multiplies the original signal by a chip sequence from a chip generator, producing the spread signal.
> - text_in_image: Modulator; Original; Spread; signal; signal; Chips generator
> - use_when: Teach ch06-6-2-2, interpret Figure 6.32, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

As an example, let us consider the sequence used in a wireless LAN, the famous
Barker sequence, where n is 11. We assume that the original signal and the chips in
the chip generator use polar NRZ encoding. Figure 6.33 shows the chips and the result
of multiplying the original data by the chips to get the spread signal.

> **[ASSET ch06_ill_033]** Figure 6.33: DSSS example
> - type: illustration
> - kind: diagram
> - file: assets/ch06_ill_033.png
> - src: book Figure 6.33; p.179
> - shows: Figure 6.33: DSSS example. Each original bit in 1-0-1 is multiplied by the 11-chip Barker sequence, producing the displayed higher-rate bipolar spread waveform.
> - structure: Each original bit in 1-0-1 is multiplied by the 11-chip Barker sequence, producing the displayed higher-rate bipolar spread waveform.
> - text_in_image: 1; 0; 1; Original; signal; 1; 0; 1 1; 0; 1 1 1; 0 0 0; 1; 0; 1 1; 0; 1 1 1; 0 0 0 1; 0; 1 1; 0; 1 1 1; 0 0 0; Spreading; code; Spread; signal
> - use_when: Teach ch06-6-2-2, interpret Figure 6.33, compare multiplexing or spreading methods, or solve its linked practice question.
> - confidence: high

In Figure 6.33, the spreading code is 11 chips having the pattern 10110111000 (in
this case). If the original signal rate is N, the rate of the spread signal is 11N. This
means that the required bandwidth for the spread signal is 11 times larger than the
bandwidth of the original signal. The spread signal can provide privacy if the intruder
does not know the code. It can also provide immunity against interference if each station uses a different code.

#### Bandwidth Sharing
> id: ch06-6-2-2-bandwidth-sharing | src: book p.179 | kind: concept

Can we share a bandwidth in DSSS as we did in FHSS? The answer is no and yes. If
we use a spreading code that spreads signals (from different stations) that cannot be
combined and separated, we cannot share a bandwidth. For example, as we will see
in Chapter 15, some wireless LANs use DSSS and the spread bandwidth cannot be
shared. However, if we use a special type of sequence code that allows the combining
and separating of spread signals, we can share the bandwidth. As we will see in
Chapter 16, a special spreading code allows us to use DSSS in cellular telephony and
share a bandwidth among several users.

## 6.3 END-CHAPTER MATERIALS
> id: ch06-6-3 | src: book 6.3; p.180 | kind: concept

### 6.3.1 Recommended Reading
> id: ch06-6-3-1 | src: book 6.3.1; p.180 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets […] refer to the reference list at the end of the text.

#### Books
> id: ch06-6-3-1-books | src: book p.180 | kind: concept

Multiplexing is discussed in [Pea92]. [Cou01] gives excellent coverage of TDM and
FDM. More advanced materials can be found in [Ber96]. Multiplexing is discussed
in [Sta04]. A good coverage of spread spectrum can be found in [Cou01] and
[Sta04].

### 6.3.2 Key Terms
> id: ch06-6-3-2 | src: book 6.3.2; p.180 | kind: concept

- analog hierarchy
- Barker sequence
- channel
- chip
- demultiplexer (DEMUX)
- dense WDM (DWDM)
- digital signal (DS) service
- direct sequence spread spectrum (DSSS)
- E line
- framing bit
- frequency hopping spread spectrum (FHSS)
- frequency-division multiplexing (FDM)
- group
- guard band
- hopping period
- interleaving
- jumbo group
- link
- master group
- multilevel multiplexing
- multiple-slot allocation
- multiplexer (MUX)
- multiplexing
- pseudorandom code generator
- pseudorandom noise (PN)
- pulse stuffing
- spread spectrum (SS)
- statistical TDM
- supergroup
- synchronous TDM
- T line
- time-division multiplexing (TDM)
- wavelength-division multiplexing (WDM)

### 6.3.3 Summary
> id: ch06-6-3-3 | src: book 6.3.3; p.180 | kind: summary

Bandwidth utilization is the use of available bandwidth to achieve specific goals. Efficiency can be achieved by using multiplexing; privacy and antijamming can be
achieved by using spreading.
Multiplexing is the set of techniques that allow the simultaneous transmission of
multiple signals across a single data link. In a multiplexed system, n lines share the
bandwidth of one link. The word link refers to the physical path. The word channel
refers to the portion of a link that carries a transmission. There are three basic multiplexing techniques: frequency-division multiplexing, wavelength-division multiplexing, and
time-division multiplexing. The first two are techniques designed for analog signals, the
third, for digital signals. Frequency-division multiplexing (FDM) is an analog
technique that can be applied when the bandwidth of a link (in hertz) is greater than the
combined bandwidths of the signals to be transmitted. Wavelength-division multiplexing (WDM) is designed to use the high bandwidth capability of fiber-optic cable.
WDM is an analog multiplexing technique to combine optical signals. Time-division
multiplexing (TDM) is a digital process that allows several connections to share the
high bandwidth of a link. TDM is a digital multiplexing technique for combining several low-rate channels into one high-rate one. We can divide TDM into two different
schemes: synchronous or statistical. In synchronous TDM, each input connection has
an allotment in the output even if it is not sending data. In statistical TDM, slots are
dynamically allocated to improve bandwidth efficiency.
In spread spectrum (SS), we combine signals from different sources to fit into a
larger bandwidth. Spread spectrum is designed to be used in wireless applications in
which stations must be able to share the medium without interception by an eavesdropper and without being subject to jamming from a malicious intruder. The frequency
hopping spread spectrum (FHSS) technique uses M different carrier frequencies that
are modulated by the source signal. At one moment, the signal modulates one carrier
frequency; at the next moment, the signal modulates another carrier frequency. The
direct sequence spread spectrum (DSSS) technique expands the bandwidth of a signal
by replacing each data bit with n bits using a spreading code. In other words, each bit is
assigned a code of n bits, called chips.
