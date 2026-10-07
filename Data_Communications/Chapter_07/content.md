---
doc_type: scientific_content
course_id: data_communications
chapter: 7
chapter_id: data_communications_ch07
chapter_title: Transmission Media
textbook: Data Communications and Networking (Forouzan)
textbook_edition: 5th
language: en
syllabus_applied: false
sources:
- role: book
  file: Slide/ch_7/ch7.pdf
  pages: 185-206
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
generated_at: '2026-10-07T03:22:16+00:00'
status: complete
---
# Chapter 7: Transmission Media

## Chapter Objectives
> id: ch07-0 | src: book p.185 | kind: objectives

We discussed many issues related to the physical layer in Chapters 3 through 6. In
this chapter, we discuss transmission media. We definitely need transmission
media to conduct signals from the source to the destination. However, the media can be
wired or wireless.
This chapter is divided into three sections:

- The first section introduces the transmission media and defines its position in the
Internet model. It shows that we can classify transmission media into two broad
categories: guided and unguided media.

- The second section discusses guided media. The first part describes twisted-pair
cables and their characteristics and applications. The second part describes coaxial
cables and their characteristics and applications. Finally, the third part describes
fiber-optic cables and their characteristics and applications.

- The third section discusses unguided media. The first part describes radio waves
and their characteristics and applications. The second part describes microwaves
and their characteristics and applications. Finally, the third part describes infrared
waves and their characteristics and applications.

## 7.1 INTRODUCTION
> id: ch07-7-1 | src: book 7.1; p.186 | kind: concept

Transmission media are actually located below the physical layer and are directly controlled by the physical layer. We could say that transmission media belong to layer
zero. Figure 7.1 shows the position of transmission media in relation to the physical
layer.

> **[ASSET ch07_ill_001]** Figure 7.1: Transmission medium and physical layer
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_001.png
> - src: book Figure 7.1; p.186
> - shows: Figure 7.1: Transmission medium and physical layer. A sender physical layer reaches a receiver physical layer through a transmission medium, shown as cable or air beneath the protocol-layer blocks.
> - structure: A sender physical layer reaches a receiver physical layer through a transmission medium, shown as cable or air beneath the protocol-layer blocks.
> - text_in_image: Sender; Physical layer; Physical layer; Receiver; Transmission medium; Cable or air
> - use_when: Teach ch07-7-1, interpret Figure 7.1, compare transmission media, or solve a linked practice question.
> - confidence: high

A transmission medium can be broadly defined as anything that can carry information from a source to a destination. For example, the transmission medium for two
people having a dinner conversation is the air. The air can also be used to convey the
message in a smoke signal or semaphore. For a written message, the transmission
medium might be a mail carrier, a truck, or an airplane.
In data communications the definition of the information and the transmission
medium is more specific. The transmission medium is usually free space, metallic cable,
or fiber-optic cable. The information is usually a signal that is the result of a conversion
of data from another form.
The use of long-distance communication using electric signals started with the
invention of the telegraph by Morse in the 19th century. Communication by telegraph
was slow and dependent on a metallic medium.
Extending the range of the human voice became possible when the telephone was
invented in 1869. Telephone communication at that time also needed a metallic medium
to carry the electric signals that were the result of a conversion from the human voice.
The communication was, however, unreliable due to the poor quality of the wires. The
lines were often noisy and the technology was unsophisticated.
Wireless communication started in 1895 when Hertz was able to send high-frequency signals. Later, Marconi devised a method to send telegraph-type messages
over the Atlantic Ocean.
We have come a long way. Better metallic media have been invented (twisted-pair
and coaxial cables, for example). The use of optical fibers has increased the data rate
incredibly. Free space (air, vacuum, and water) is used more efficiently, in part due
to the technologies (such as modulation and multiplexing) discussed in the previous
chapters.
As discussed in Chapter 3, computers and other telecommunication devices use
signals to represent data. These signals are transmitted from one device to another in the
form of electromagnetic energy, which is propagated through transmission media.
Electromagnetic energy, a combination of electric and magnetic fields vibrating in
relation to each other, includes power, radio waves, infrared light, visible light, ultraviolet
light, and X, gamma, and cosmic rays. Each of these constitutes a portion of the electromagnetic spectrum. Not all portions of the spectrum are currently usable for telecommunications, however. The media to harness those that are usable are also limited
to a few types.
In telecommunications, transmission media can be divided into two broad categories: guided and unguided. Guided media include twisted-pair cable, coaxial cable, and
fiber-optic cable. Unguided medium is free space. Figure 7.2 shows this taxonomy.

> **[ASSET ch07_ill_002]** Figure 7.2: Classes of transmission media
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_002.png
> - src: book Figure 7.2; p.187
> - shows: Figure 7.2: Classes of transmission media. A hierarchy divides transmission media into guided media (twisted-pair, coaxial, fiber-optic) and unguided media (radio, microwave, infrared).
> - structure: A hierarchy divides transmission media into guided media (twisted-pair, coaxial, fiber-optic) and unguided media (radio, microwave, infrared).
> - text_in_image: Transmission; media; Guided; Unguided; (wired); (wireless); Twisted-pair; Coaxial; Fiber-optic; Radio wave; Microwave; Infrared; cable; cable; cable
> - use_when: Teach ch07-7-1, interpret Figure 7.2, compare transmission media, or solve a linked practice question.
> - confidence: high

## 7.2 GUIDED MEDIA
> id: ch07-7-2 | src: book 7.2; p.187 | kind: concept

Guided media, which are those that provide a conduit from one device to another,
include twisted-pair cable, coaxial cable, and fiber-optic cable. A signal traveling
along any of these media is directed and contained by the physical limits of the
medium. Twisted-pair and coaxial cable use metallic (copper) conductors that accept
and transport signals in the form of electric current. Optical fiber is a cable that accepts
and transports signals in the form of light.

### 7.2.1 Twisted-Pair Cable
> id: ch07-7-2-1 | src: book 7.2.1; p.187 | kind: concept

A twisted pair consists of two conductors (normally copper), each with its own plastic
insulation, twisted together, as shown in Figure 7.3.

> **[ASSET ch07_ill_003]** Figure 7.3: Twisted-pair cable
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_003.png
> - src: book Figure 7.3; p.187
> - shows: Figure 7.3: Twisted-pair cable. Two insulated copper conductors twist around each other; callouts identify the conductor and its insulating jacket.
> - structure: Two insulated copper conductors twist around each other; callouts identify the conductor and its insulating jacket.
> - text_in_image: Insulator; Conductor
> - use_when: Teach ch07-7-2-1, interpret Figure 7.3, compare transmission media, or solve a linked practice question.
> - confidence: high

One of the wires is used to carry signals to the receiver, and the other is used only
as a ground reference. The receiver uses the difference between the two.
In addition to the signal sent by the sender on one of the wires, interference (noise)
and crosstalk may affect both wires and create unwanted signals.
If the two wires are parallel, the effect of these unwanted signals is not the same in
both wires because they are at different locations relative to the noise or crosstalk sources
(e.g., one is closer and the other is farther). This results in a difference at the receiver.
By twisting the pairs, a balance is maintained. For example, suppose in one twist, one
wire is closer to the noise source and the other is farther; in the next twist, the reverse is
true. Twisting makes it probable that both wires are equally affected by external influences (noise or crosstalk). This means that the receiver, which calculates the difference
between the two, receives no unwanted signals. The unwanted signals are mostly canceled out. From the above discussion, it is clear that the number of twists per unit of
length (e.g., inch) has some effect on the quality of the cable.

#### Unshielded Versus Shielded Twisted-Pair Cable
> id: ch07-7-2-1-unshielded-versus-shielded-twisted-pair-cable | src: book p.188 | kind: concept

The most common twisted-pair cable used in communications is referred to as
unshielded twisted-pair (UTP). IBM has also produced a version of twisted-pair cable
for its use, called shielded twisted-pair (STP). STP cable has a metal foil or braidedmesh covering that encases each pair of insulated conductors. Although metal casing
improves the quality of cable by preventing the penetration of noise or crosstalk, it is
bulkier and more expensive. Figure 7.4 shows the difference between UTP and STP.
Our discussion focuses primarily on UTP because STP is seldom used outside of IBM.

> **[ASSET ch07_ill_004]** Figure 7.4: UTP and STP cables
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_004.png
> - src: book Figure 7.4; p.188
> - shows: Figure 7.4: UTP and STP cables. Cutaway views compare UTP, which has a plastic cover around insulated pairs, with STP, which adds a metal shield beneath the cover.
> - structure: Cutaway views compare UTP, which has a plastic cover around insulated pairs, with STP, which adds a metal shield beneath the cover.
> - text_in_image: Metal shield; Plastic cover; Plastic cover; a. UTP; b. STP
> - use_when: Teach ch07-7-2-1-unshielded-versus-shielded-twisted-pair-cable, interpret Figure 7.4, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Categories
> id: ch07-7-2-1-categories | src: book p.188 | kind: concept

The Electronic Industries Association (EIA) has developed standards to classify
unshielded twisted-pair cable into seven categories. Categories are determined by cable
quality, with 1 as the lowest and 7 as the highest. Each EIA category is suitable for
specific uses. Table 7.1 shows these categories.

**Table 7.1: Categories of unshielded twisted-pair cables**

| Category | Specification | Data Rate (Mbps) | Use |
| --- | --- | --- | --- |
| 1 | Unshielded twisted-pair used in telephone | < 0.1 | Telephone |
| 2 | Unshielded twisted-pair originally used in T lines | 2 | T-1 lines |
| 3 | Improved CAT 2 used in LANs | 10 | LANs |
| 4 | Improved CAT 3 used in Token Ring networks | 20 | LANs |
| 5 | Cable wire is normally 24 AWG with a jacket and outside sheath | 100 | LANs |
| 5E | An extension to category 5 that includes extra features to minimize the crosstalk and electromagnetic interference | 125 | LANs |
| 6 | A new category with matched components coming from the same manufacturer. The cable must be tested at a 200-Mbps data rate. | 200 | LANs |
| 7 | Sometimes called SSTP (shielded screen twisted-pair). Each pair is individually wrapped in a helical metallic foil followed by a metallic foil shield in addition to the outside sheath. The shield decreases the effect of crosstalk and increases the data rate. | 600 | LANs |

Data Rate


(Mbps)

Unshielded twisted-pair originally used in


T lines

Cable wire is normally 24 AWG with a jacket


and outside sheath

Categories of unshielded twisted-pair cables (continued)

Data Rate


(Mbps)


An extension to category 5 that includes


extra features to minimize the crosstalk and
electromagnetic interference

A new category with matched components


coming from the same manufacturer. The
cable must be tested at a 200-Mbps data rate.
Sometimes called SSTP (shielded screen

twisted-pair). Each pair is individually
wrapped in a helical metallic foil followed by
a metallic foil shield in addition to the outside
sheath. The shield decreases the effect of
crosstalk and increases the data rate.

#### Connectors
> id: ch07-7-2-1-connectors | src: book p.189 | kind: concept

The most common UTP connector is RJ45 (RJ stands for registered jack), as shown
in Figure 7.5. The RJ45 is a keyed connector, meaning the connector can be inserted in
only one way.

> **[ASSET ch07_ill_005]** Figure 7.5: UTP connector
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_005.png
> - src: book Figure 7.5; p.189
> - shows: Figure 7.5: UTP connector. Front and perspective views identify the eight contacts and cable entry of female and male RJ-45 connectors.
> - structure: Front and perspective views identify the eight contacts and cable entry of female and male RJ-45 connectors.
> - text_in_image: 12345678; 12345678; RJ-45 Male; RJ-45 Female
> - use_when: Teach ch07-7-2-1-connectors, interpret Figure 7.5, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Performance
> id: ch07-7-2-1-performance | src: book p.189 | kind: concept

One way to measure the performance of twisted-pair cable is to compare attenuation
versus frequency and distance. A twisted-pair cable can pass a wide range of frequencies.
However, Figure 7.6 shows that with increasing frequency, the attenuation, measured in
decibels per kilometer (dB/km), sharply increases with frequencies above 100 kHz. Note
that gauge is a measure of the thickness of the wire.

#### Applications
> id: ch07-7-2-1-applications | src: book p.189 | kind: concept

Twisted-pair cables are used in telephone lines to provide voice and data channels.
The local loop—the line that connects subscribers to the central telephone office—
commonly consists of unshielded twisted-pair cables. We discuss telephone networks
in Chapter 14.
The DSL lines that are used by the telephone companies to provide high-data-rate
connections also use the high-bandwidth capability of unshielded twisted-pair cables.
We discuss DSL technology in Chapter 14.

> **[ASSET ch07_ill_006]** Figure 7.6: UTP performance
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_006.png
> - src: book Figure 7.6; p.190
> - shows: Figure 7.6: UTP performance. A log-frequency graph plots attenuation in dB/km for 18-, 22-, 24-, and 26-gauge UTP; attenuation rises with frequency and thinner conductors attenuate more.
> - structure: A log-frequency graph plots attenuation in dB/km for 18-, 22-, 24-, and 26-gauge UTP; attenuation rises with frequency and thinner conductors attenuate more.
> - text_in_image: 26 gauge; Gauge; Diameter (inches); 20; 24 gauge; 18; 0.0403; 18; 0.02320; 22; 0.02010; 24; 16; 0.0159; 26; 22 gauge; Attenuation (dB/km); 14; 12; 18 gauge; 10; 8; 6; 4; 2; 1; 10; 100; 1000; f (kHz)
> - use_when: Teach ch07-7-2-1-performance, interpret Figure 7.6, compare transmission media, or solve a linked practice question.
> - confidence: high

Local-area networks, such as 10Base-T and 100Base-T, also use twisted-pair cables.
We discuss these networks in Chapter 13.

### 7.2.2 Coaxial Cable
> id: ch07-7-2-2 | src: book 7.2.2; p.190 | kind: concept

Coaxial cable (or coax) carries signals of higher frequency ranges than those in twisted-pair cable, in part because the two media are constructed quite differently. Instead of
having two wires, coax has a central core conductor of solid or stranded wire (usually
copper) enclosed in an insulating sheath, which is, in turn, encased in an outer conductor
of metal foil, braid, or a combination of the two. The outer metallic wrapping serves
both as a shield against noise and as the second conductor, which completes the circuit.
This outer conductor is also enclosed in an insulating sheath, and the whole cable is
protected by a plastic cover (see Figure 7.7).

> **[ASSET ch07_ill_007]** Figure 7.7: Coaxial cable
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_007.png
> - src: book Figure 7.7; p.190
> - shows: Figure 7.7: Coaxial cable. A coaxial cable cutaway labels the inner conductor, inner insulator, braided outer conductor or shield, and plastic outer cover.
> - structure: A coaxial cable cutaway labels the inner conductor, inner insulator, braided outer conductor or shield, and plastic outer cover.
> - text_in_image: Insulator; Insulator; Inner conductor; Outer conductor; (shield); Plastic cover
> - use_when: Teach ch07-7-2-2, interpret Figure 7.7, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Coaxial Cable Standards
> id: ch07-7-2-2-coaxial-cable-standards | src: book p.190 | kind: concept

Coaxial cables are categorized by their Radio Government (RG) ratings. Each RG
number denotes a unique set of physical specifications, including the wire gauge of the
inner conductor, the thickness and type of the inner insulator, the construction of the
shield, and the size and type of the outer casing. Each cable defined by an RG rating is
adapted for a specialized function, as shown in Table 7.2.

**Table 7.2: Categories of coaxial cables**

| Category | Impedance | Use |
| --- | --- | --- |
| RG-59 | 75 Ω | Cable TV |
| RG-58 | 50 Ω | Thin Ethernet |
| RG-11 | 50 Ω | Thick Ethernet |

#### Coaxial Cable Connectors
> id: ch07-7-2-2-coaxial-cable-connectors | src: book p.191 | kind: concept

To connect coaxial cable to devices, we need coaxial connectors. The most common
type of connector used today is the Bayonet Neill-Concelman (BNC) connector.
Figure 7.8 shows three popular types of these connectors: the BNC connector, the
BNC T connector, and the BNC terminator.

> **[ASSET ch07_ill_008]** Figure 7.8: BNC connectors
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_008.png
> - src: book Figure 7.8; p.191
> - shows: Figure 7.8: BNC connectors. A connector chain shows a cable-mounted BNC connector, a BNC T, and a 50-ohm terminator connected to ground.
> - structure: A connector chain shows a cable-mounted BNC connector, a BNC T, and a 50-ohm terminator connected to ground.
> - text_in_image: BNC T; Cable; BNC connector; 50-W; Ground; BNC terminator; wire
> - use_when: Teach ch07-7-2-2-coaxial-cable-connectors, interpret Figure 7.8, compare transmission media, or solve a linked practice question.
> - confidence: high

The BNC connector is used to connect the end of the cable to a device, such as a
TV set. The BNC T connector is used in Ethernet networks (see Chapter 13) to branch
out to a connection to a computer or other device. The BNC terminator is used at the
end of the cable to prevent the reflection of the signal.

#### Performance
> id: ch07-7-2-2-performance | src: book p.191 | kind: concept

As we did with twisted-pair cable, we can measure the performance of a coaxial cable.
We notice in Figure 7.9 that the attenuation is much higher in coaxial cable than in
twisted-pair cable. In other words, although coaxial cable has a much higher bandwidth,
the signal weakens rapidly and requires the frequent use of repeaters.

#### Applications
> id: ch07-7-2-2-applications | src: book p.191 | kind: concept

Coaxial cable was widely used in analog telephone networks where a single coaxial
network could carry 10,000 voice signals. Later it was used in digital telephone
networks where a single coaxial cable could carry digital data up to 600 Mbps. However, coaxial cable in telephone networks has largely been replaced today with fiber-optic cable.

> **[ASSET ch07_ill_009]** Figure 7.9: Coaxial cable performance
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_009.png
> - src: book Figure 7.9; p.192
> - shows: Figure 7.9: Coaxial cable performance. A log-frequency graph compares attenuation in dB/km for three coaxial dimensions; attenuation rises with frequency and varies by cable geometry.
> - structure: A log-frequency graph compares attenuation in dB/km for three coaxial dimensions; attenuation rises with frequency and varies by cable geometry.
> - text_in_image: 0.7/2.9 mm; 35; 30; Attenuation (dB/km); 25; 1.2/4.4 mm; 20; 2.6/9.5 mm; 15; 10; 5; 0.01; 0.1; 1.0; 10; 100; f (MHz)
> - use_when: Teach ch07-7-2-2-performance, interpret Figure 7.9, compare transmission media, or solve a linked practice question.
> - confidence: high

Cable TV networks (see Chapter 14) also use coaxial cables. In the traditional cable
TV network, the entire network used coaxial cable. Later, however, cable TV providers
replaced most of the media with fiber-optic cable; hybrid networks use coaxial cable
only at the network boundaries, near the consumer premises. Cable TV uses RG-59
coaxial cable.
Another common application of coaxial cable is in traditional Ethernet LANs (see
Chapter 13). Because of its high bandwidth, and consequently high data rate, coaxial
cable was chosen for digital transmission in early Ethernet LANs. The 10Base-2, or Thin
Ethernet, uses RG-58 coaxial cable with BNC connectors to transmit data at 10 Mbps
with a range of 185 m. The 10Base5, or Thick Ethernet, uses RG-11 (thick coaxial cable)
to transmit 10 Mbps with a range of 5000 m. Thick Ethernet has specialized connectors.

### 7.2.3 Fiber-Optic Cable
> id: ch07-7-2-3 | src: book 7.2.3; p.192 | kind: concept

A fiber-optic cable is made of glass or plastic and transmits signals in the form of light.
To understand optical fiber, we first need to explore several aspects of the nature of
light.
Light travels in a straight line as long as it is moving through a single uniform substance. If a ray of light traveling through one substance suddenly enters another substance
(of a different density), the ray changes direction. Figure 7.10 shows how a ray of light
changes direction when going from a more dense to a less dense substance.
As the figure shows, if the angle of incidence I (the angle the ray makes with the
line perpendicular to the interface between the two substances) is less than the critical
angle, the ray refracts and moves closer to the surface. If the angle of incidence is
equal to the critical angle, the light bends along the interface. If the angle is greater than
the critical angle, the ray reflects (makes a turn) and travels again in the denser

> **[ASSET ch07_ill_010]** Figure 7.10: Bending of light ray
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_010.png
> - src: book Figure 7.10; p.193
> - shows: Figure 7.10: Bending of light ray. Three ray diagrams compare refraction below the critical angle, refraction along the boundary at the critical angle, and total internal reflection above it.
> - structure: Three ray diagrams compare refraction below the critical angle, refraction along the boundary at the critical angle, and total internal reflection above it.
> - text_in_image: Less; Less; Less; dense; dense; dense; More; More; More; dense; dense; dense; I; I; I; I < critical angle,; I = critical angle,; I > critical angle,; refraction; refraction; reflection
> - use_when: Teach ch07-7-2-3-propagation-modes, interpret Figure 7.10, compare transmission media, or solve a linked practice question.
> - confidence: high

substance. Note that the critical angle is a property of the substance, and its value differs
from one substance to another.
Optical fibers use reflection to guide light through a channel. A glass or plastic core
is surrounded by a cladding of less dense glass or plastic. The difference in density of the
two materials must be such that a beam of light moving through the core is reflected off
the cladding instead of being refracted into it. See Figure 7.11.

> **[ASSET ch07_ill_011]** Figure 7.11: Optical fiber
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_011.png
> - src: book Figure 7.11; p.193
> - shows: Figure 7.11: Optical fiber. A light ray repeatedly reflects inside the fiber core while lower-index cladding confines it between sender and receiver.
> - structure: A light ray repeatedly reflects inside the fiber core while lower-index cladding confines it between sender and receiver.
> - text_in_image: Cladding; Core; Sender; Receiver; Cladding
> - use_when: Teach ch07-7-2-3, interpret Figure 7.11, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Propagation Modes
> id: ch07-7-2-3-propagation-modes | src: book p.193 | kind: concept

Current technology supports two modes (multimode and single mode) for propagating light
along optical channels, each requiring fiber with different physical characteristics. Multimode can be implemented in two forms: step-index or graded-index (see Figure 7.12).

> **[ASSET ch07_ill_012]** Figure 7.12: Propagation modes
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_012.png
> - src: book Figure 7.12; p.193
> - shows: Figure 7.12: Propagation modes. A classification tree divides propagation into multimode step-index, multimode graded-index, and single-mode operation.
> - structure: A classification tree divides propagation into multimode step-index, multimode graded-index, and single-mode operation.
> - text_in_image: Mode; Multimode; Single mode; Step index; Graded index
> - use_when: Teach ch07-7-2-3-propagation-modes, interpret Figure 7.12, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Multimode
> id: ch07-7-2-3-multimode | src: book p.193 | kind: concept

Multimode is so named because multiple beams from a light source move through the
core in different paths. How these beams move within the cable depends on the structure of the core, as shown in Figure 7.13.

> **[ASSET ch07_ill_013]** Figure 7.13: Modes
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_013.png
> - src: book Figure 7.13; p.194
> - shows: Figure 7.13: Modes. Three fiber paths compare multimode step-index reflections, curved multimode graded-index paths, and a nearly straight single-mode path, with representative pulses at source and destination.
> - structure: Three fiber paths compare multimode step-index reflections, curved multimode graded-index paths, and a nearly straight single-mode path, with representative pulses at source and destination.
> - text_in_image: Source; Destination; a. Multimode, step index; Source; Destination; b. Multimode, graded index; Destination; Source; c. Single mode
> - use_when: Teach ch07-7-2-3-propagation-modes, interpret Figure 7.13, compare transmission media, or solve a linked practice question.
> - confidence: high

In multimode step-index fiber, the density of the core remains constant from the
center to the edges. A beam of light moves through this constant density in a straight
line until it reaches the interface of the core and the cladding. At the interface, there is
an abrupt change due to a lower density; this alters the angle of the beam’s motion. The
term step-index refers to the suddenness of this change, which contributes to the distortion of the signal as it passes through the fiber.
A second type of fiber, called multimode graded-index fiber, decreases this distortion of the signal through the cable. The word index here refers to the index of
refraction. As we saw above, the index of refraction is related to density. A graded-index fiber, therefore, is one with varying densities. Density is highest at the center of
the core and decreases gradually to its lowest at the edge. Figure 7.13 shows the impact
of this variable density on the propagation of light beams.

#### Single-Mode
> id: ch07-7-2-3-single-mode | src: book p.194 | kind: concept

Single-mode uses step-index fiber and a highly focused source of light that limits
beams to a small range of angles, all close to the horizontal. The single-mode fiber
itself is manufactured with a much smaller diameter than that of multimode fiber, and
with substantially lower density (index of refraction). The decrease in density results in
a critical angle that is close enough to 90° to make the propagation of beams almost
horizontal. In this case, propagation of different beams is almost identical, and delays
are negligible. All the beams arrive at the destination “together” and can be recombined
with little distortion to the signal (see Figure 7.13).

#### Fiber Sizes
> id: ch07-7-2-3-fiber-sizes | src: book p.195 | kind: concept

Optical fibers are defined by the ratio of the diameter of their core to the diameter of
their cladding, both expressed in micrometers. The common sizes are shown in Table 7.3.
Note that the last size listed is for single-mode only.

**Table 7.3: Fiber types**

| Type | Core (μm) | Cladding (μm) | Mode |
| --- | --- | --- | --- |
| 50/125 | 50.0 | 125 | Multimode, graded index |
| 62.5/125 | 62.5 | 125 | Multimode, graded index |
| 100/125 | 100.0 | 125 | Multimode, graded index |
| 7/125 | 7.0 | 125 | Single mode |

#### Cable Composition
> id: ch07-7-2-3-cable-composition | src: book p.195 | kind: concept

Figure 7.14 shows the composition of a typical fiber-optic cable. The outer jacket is

> **[ASSET ch07_ill_014]** Figure 7.14: Fiber construction
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_014.png
> - src: book Figure 7.14; p.195
> - shows: Figure 7.14: Fiber construction. A fiber cable cutaway labels the glass or plastic core, cladding, plastic buffer, Kevlar strength member, and outer jacket.
> - structure: A fiber cable cutaway labels the glass or plastic core, cladding, plastic buffer, Kevlar strength member, and outer jacket.
> - text_in_image: DuPont Kevlar; for strength; Outer jacket; Cladding; Plastic; buffer; Glass or; plastic core
> - use_when: Teach ch07-7-2-3-cable-composition, interpret Figure 7.14, compare transmission media, or solve a linked practice question.
> - confidence: high

made of either PVC or Teflon. Inside the jacket are Kevlar strands to strengthen the cable.
Kevlar is a strong material used in the fabrication of bulletproof vests. Below the Kevlar is
another plastic coating to cushion the fiber. The fiber is at the center of the cable, and it
consists of cladding and core.

#### Fiber-Optic Cable Connectors
> id: ch07-7-2-3-fiber-optic-cable-connectors | src: book p.195 | kind: concept

There are three types of connectors for fiber-optic cables, as shown in Figure 7.15. The
subscriber channel (SC) connector is used for cable TV. It uses a push/pull locking
system. The straight-tip (ST) connector is used for connecting cable to networking
devices. It uses a bayonet locking system and is more reliable than SC. MT-RJ is a
connector that is the same size as RJ45.

#### Performance
> id: ch07-7-2-3-performance | src: book p.195 | kind: concept

The plot of attenuation versus wavelength in Figure 7.16 shows a very interesting
phenomenon in fiber-optic cable. Attenuation is flatter than in the case of twisted-pair
cable and coaxial cable. The performance is such that we need fewer (actually onetenth as many) repeaters when we use fiber-optic cable.

> **[ASSET ch07_ill_015]** Figure 7.15: Fiber-optic cable connectors
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_015.png
> - src: book Figure 7.15; p.196
> - shows: Figure 7.15: Fiber-optic cable connectors. Drawings identify SC, ST, and MT-RJ fiber connectors; the MT-RJ view labels its transmit and receive fibers.
> - structure: Drawings identify SC, ST, and MT-RJ fiber connectors; the MT-RJ view labels its transmit and receive fibers.
> - text_in_image: SC connector; ST connector; RX; TX; MT-RJ connector
> - use_when: Teach ch07-7-2-3-fiber-optic-cable-connectors, interpret Figure 7.15, compare transmission media, or solve a linked practice question.
> - confidence: high

> **[ASSET ch07_ill_016]** Figure 7.16: Optical fiber performance
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_016.png
> - src: book Figure 7.16; p.196
> - shows: Figure 7.16: Optical fiber performance. A wavelength graph plots optical-fiber loss in dB/km from roughly 800 to 1800 nm, including low-loss windows and an absorption peak near 1400 nm.
> - structure: A wavelength graph plots optical-fiber loss in dB/km from roughly 800 to 1800 nm, including low-loss windows and an absorption peak near 1400 nm.
> - text_in_image: 100; 50; 10; 5; Loss (dB/km); 1; 0.5; 0.1; 0.05; 0.01; 800; 1000; 1200; 1400; 1600; 1800; Wavelength (nm)
> - use_when: Teach ch07-7-2-3-performance, interpret Figure 7.16, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Applications
> id: ch07-7-2-3-applications | src: book p.196 | kind: concept

Fiber-optic cable is often found in backbone networks because its wide bandwidth is
cost-effective. Today, with wavelength-division multiplexing (WDM), we can transfer
data at a rate of 1600 Gbps. The SONET network that we discuss in Chapter 14 provides
such a backbone.
Some cable TV companies use a combination of optical fiber and coaxial cable,
thus creating a hybrid network. Optical fiber provides the backbone structure while
coaxial cable provides the connection to the user premises. This is a cost-effective configuration since the narrow bandwidth requirement at the user end does not justify the
use of optical fiber.
Local-area networks such as 100Base-FX network (Fast Ethernet) and 1000Base-X
also use fiber-optic cable.

#### Advantages and Disadvantages of Optical Fiber
> id: ch07-7-2-3-advantages-and-disadvantages-of-optical-fiber | src: book p.197 | kind: concept

#### Advantages
> id: ch07-7-2-3-advantages | src: book p.197 | kind: concept

Fiber-optic cable has several advantages over metallic cable (twisted-pair or coaxial).

- Higher bandwidth. Fiber-optic cable can support dramatically higher bandwidths
(and hence data rates) than either twisted-pair or coaxial cable. Currently, data rates
and bandwidth utilization over fiber-optic cable are limited not by the medium but
by the signal generation and reception technology available.

- Less signal attenuation. Fiber-optic transmission distance is significantly greater
than that of other guided media. A signal can run for 50 km without requiring
regeneration. We need repeaters every 5 km for coaxial or twisted-pair cable.

- Immunity to electromagnetic interference. Electromagnetic noise cannot affect
fiber-optic cables.

- Resistance to corrosive materials. Glass is more resistant to corrosive materials
than copper.

- Light weight. Fiber-optic cables are much lighter than copper cables.

- Greater immunity to tapping. Fiber-optic cables are more immune to tapping than
copper cables. Copper cables create antenna effects that can easily be tapped.

#### Disadvantages
> id: ch07-7-2-3-disadvantages | src: book p.197 | kind: concept

There are some disadvantages in the use of optical fiber.

- Installation and maintenance. Fiber-optic cable is a relatively new technology. Its
installation and maintenance require expertise that is not yet available everywhere.

- Unidirectional light propagation. Propagation of light is unidirectional. If we
need bidirectional communication, two fibers are needed.

- Cost. The cable and the interfaces are relatively more expensive than those of other
guided media. If the demand for bandwidth is not high, often the use of optical fiber
cannot be justified.

## 7.3 UNGUIDED MEDIA: WIRELESS
> id: ch07-7-3 | src: book 7.3; p.197 | kind: concept

Unguided medium transport electromagnetic waves without using a physical conductor. This type of communication is often referred to as wireless communication. Signals are normally broadcast through free space and thus are available to anyone who
has a device capable of receiving them.
Figure 7.17 shows the part of the electromagnetic spectrum, ranging from 3 kHz to
900 THz, used for wireless communication.
Unguided signals can travel from the source to the destination in several ways: ground
propagation, sky propagation, and line-of-sight propagation, as shown in Figure 7.18.

> **[ASSET ch07_ill_017]** Figure 7.17: Electromagnetic spectrum for wireless communication
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_017.png
> - src: book Figure 7.17; p.198
> - shows: Figure 7.17: Electromagnetic spectrum for wireless communication. The wireless spectrum bar places radio and microwave from 3 kHz to 300 GHz, infrared from 300 GHz to 400 THz, and visible light from 400 to 900 THz.
> - structure: The wireless spectrum bar places radio and microwave from 3 kHz to 300 GHz, infrared from 300 GHz to 400 THz, and visible light from 400 to 900 THz.
> - text_in_image: Light wave; Radio wave and microwave; Infrared; 3; 300; 400; 900; kHz; GHz; THz; THz
> - use_when: Teach ch07-7-3, interpret Figure 7.17, compare transmission media, or solve a linked practice question.
> - confidence: high

> **[ASSET ch07_ill_018]** Figure 7.18: Propagation methods
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_018.png
> - src: book Figure 7.18; p.198
> - shows: Figure 7.18: Propagation methods. Earth cross-sections compare ground propagation below 2 MHz, ionospheric sky propagation from 2 to 30 MHz, and line-of-sight propagation above 30 MHz.
> - structure: Earth cross-sections compare ground propagation below 2 MHz, ionospheric sky propagation from 2 to 30 MHz, and line-of-sight propagation above 30 MHz.
> - text_in_image: Ionosphere; Ionosphere; Ionosphere; Ground propagation; Sky propagation; Line-of-sight propagation; (below 2 MHz); (2–30 MHz); (above 30 MHz)
> - use_when: Teach ch07-7-3, interpret Figure 7.18, compare transmission media, or solve a linked practice question.
> - confidence: high

In ground propagation, radio waves travel through the lowest portion of the atmosphere, hugging the earth. These low-frequency signals emanate in all directions from the
transmitting antenna and follow the curvature of the planet. Distance depends on the
amount of power in the signal: The greater the power, the greater the distance. In sky
propagation, higher-frequency radio waves radiate upward into the ionosphere (the layer
of atmosphere where particles exist as ions) where they are reflected back to earth. This
type of transmission allows for greater distances with lower output power. In line-of-sight
propagation, very high-frequency signals are transmitted in straight lines directly from
antenna to antenna. Antennas must be directional, facing each other, and either tall
enough or close enough together not to be affected by the curvature of the earth. Line-of-sight propagation is tricky because radio transmissions cannot be completely focused.
The section of the electromagnetic spectrum defined as radio waves and microwaves
is divided into eight ranges, called bands, each regulated by government authorities.
These bands are rated from very low frequency (VLF) to extremely high frequency (EHF).
Table 7.4 lists these bands, their ranges, propagation methods, and some applications.

**Table 7.4: Bands**

| Band | Range | Propagation | Application |
| --- | --- | --- | --- |
| very low frequency (VLF) | 3–30 kHz | Ground | Long-range radio navigation |
| low frequency (LF) | 30–300 kHz | Ground | Radio beacons and navigational locators |
| middle frequency (MF) | 300 kHz–3 MHz | Sky | AM radio |
| high frequency (HF) | 3–30 MHz | Sky | Citizens band (CB), ship/aircraft |
| very high frequency (VHF) | 30–300 MHz | Sky and line-of-sight | VHF TV, FM radio |
| ultrahigh frequency (UHF) | 300 MHz–3 GHz | Line-of-sight | UHF TV, cellular phones, paging, satellite |
| superhigh frequency (SF) | 3–30 GHz | Line-of-sight | Satellite |
| extremely high frequency (EHF) | 30–300 GHz | Line-of-sight | Radar, satellite |

Long-range radio
navigation

Radio beacons and
navigational locators

Bands (continued)

Citizens band (CB),
ship/aircraft


Sky and

300 MHz–3 GHz Line-of-sight
UHF TV, cellular phones,
paging, satellite

We can divide wireless transmission into three broad groups: radio waves, microwaves, and infrared waves.

### 7.3.1 Radio Waves
> id: ch07-7-3-1 | src: book 7.3.1; p.199 | kind: concept

Although there is no clear-cut demarcation between radio waves and microwaves, electromagnetic waves ranging in frequencies between 3 kHz and 1 GHz are normally called
radio waves; waves ranging in frequencies between 1 and 300 GHz are called microwaves. However, the behavior of the waves, rather than the frequencies, is a better
criterion for classification.
Radio waves, for the most part, are omnidirectional. When an antenna transmits
radio waves, they are propagated in all directions. This means that the sending and
receiving antennas do not have to be aligned. A sending antenna sends waves that can
be received by any receiving antenna. The omnidirectional property has a disadvantage,
too. The radio waves transmitted by one antenna are susceptible to interference by
another antenna that may send signals using the same frequency or band.
Radio waves, particularly those waves that propagate in the sky mode, can travel
long distances. This makes radio waves a good candidate for long-distance broadcasting such as AM radio.
Radio waves, particularly those of low and medium frequencies, can penetrate
walls. This characteristic can be both an advantage and a disadvantage. It is an advantage because, for example, an AM radio can receive signals inside a building. It is a disadvantage because we cannot isolate a communication to just inside or outside a
building. The radio wave band is relatively narrow, just under 1 GHz, compared to
the microwave band. When this band is divided into subbands, the subbands are also
narrow, leading to a low data rate for digital communications.
Almost the entire band is regulated by authorities (e.g., the FCC in the United
States). Using any part of the band requires permission from the authorities.

#### Omnidirectional Antenna
> id: ch07-7-3-1-omnidirectional-antenna | src: book p.199 | kind: concept

Radio waves use omnidirectional antennas that send out signals in all directions.
Based on the wavelength, strength, and the purpose of transmission, we can have several types of antennas. Figure 7.19 shows an omnidirectional antenna.

> **[ASSET ch07_ill_019]** Figure 7.19: Omnidirectional antenna
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_019.png
> - src: book Figure 7.19; p.200
> - shows: Figure 7.19: Omnidirectional antenna. A broadcast tower radiates concentric coverage in all horizontal directions, illustrating an omnidirectional antenna.
> - structure: A broadcast tower radiates concentric coverage in all horizontal directions, illustrating an omnidirectional antenna.
> - text_in_image: No text labels appear in the source figure.
> - use_when: Teach ch07-7-3-1-omnidirectional-antenna, interpret Figure 7.19, compare transmission media, or solve a linked practice question.
> - confidence: high

#### Applications
> id: ch07-7-3-1-applications | src: book p.200 | kind: concept

The omnidirectional characteristics of radio waves make them useful for multicasting,
in which there is one sender but many receivers. AM and FM radio, television, maritime radio, cordless phones, and paging are examples of multicasting.

Radio waves are used for multicast communications,
such as radio and television, and paging systems.

### 7.3.2 Microwaves
> id: ch07-7-3-2 | src: book 7.3.2; p.200 | kind: concept

Electromagnetic waves having frequencies between 1 and 300 GHz are called microwaves. Microwaves are unidirectional. When an antenna transmits microwaves, they
can be narrowly focused. This means that the sending and receiving antennas need to
be aligned. The unidirectional property has an obvious advantage. A pair of antennas
can be aligned without interfering with another pair of aligned antennas. The following
describes some characteristics of microwave propagation:

- Microwave propagation is line-of-sight. Since the towers with the mounted antennas
need to be in direct sight of each other, towers that are far apart need to be very tall.
The curvature of the earth as well as other blocking obstacles do not allow two short
towers to communicate by using microwaves. Repeaters are often needed for long-distance communication.

- Very high-frequency microwaves cannot penetrate walls. This characteristic can be
a disadvantage if receivers are inside buildings.

- The microwave band is relatively wide, almost 299 GHz. Therefore wider subbands
can be assigned, and a high data rate is possible.

- Use of certain portions of the band requires permission from authorities.

#### Unidirectional Antenna
> id: ch07-7-3-2-unidirectional-antenna | src: book p.200 | kind: concept

Microwaves need unidirectional antennas that send out signals in one direction. Two
types of antennas are used for microwave communications: the parabolic dish and the
horn (see Figure 7.20).

> **[ASSET ch07_ill_020]** Figure 7.20: Unidirectional antennas
> - type: illustration
> - kind: diagram
> - file: assets/ch07_ill_020.png
> - src: book Figure 7.20; p.201
> - shows: Figure 7.20: Unidirectional antennas. A parabolic dish focuses parallel rays at its feed, while a horn antenna couples a waveguide to a directional flared aperture.
> - structure: A parabolic dish focuses parallel rays at its feed, while a horn antenna couples a waveguide to a directional flared aperture.
> - text_in_image: Focus; Waveguide; a. Parabolic dish antenna; b. Horn antenna
> - use_when: Teach ch07-7-3-2-unidirectional-antenna, interpret Figure 7.20, compare transmission media, or solve a linked practice question.
> - confidence: high

A parabolic dish antenna is based on the geometry of a parabola: Every line
parallel to the line of symmetry (line of sight) reflects off the curve at angles such that
all the lines intersect in a common point called the focus. The parabolic dish works as a
funnel, catching a wide range of waves and directing them to a common point. In
this way, more of the signal is recovered than would be possible with a single-point
receiver.
Outgoing transmissions are broadcast through a horn aimed at the dish. The microwaves hit the dish and are deflected outward in a reversal of the receipt path.
A horn antenna looks like a gigantic scoop. Outgoing transmissions are broadcast
up a stem (resembling a handle) and deflected outward in a series of narrow parallel
beams by the curved head. Received transmissions are collected by the scooped shape of
the horn, in a manner similar to the parabolic dish, and are deflected down into the stem.

#### Applications
> id: ch07-7-3-2-applications | src: book p.201 | kind: concept

Microwaves, due to their unidirectional properties, are very useful when unicast (oneto-one) communication is needed between the sender and the receiver. They are used
in cellular phones (Chapter 16), satellite networks (Chapter 16), and wireless LANs
(Chapter 15).

Microwaves are used for unicast communication such as cellular telephones,
satellite networks, and wireless LANs.

### 7.3.3 Infrared
> id: ch07-7-3-3 | src: book 7.3.3; p.201 | kind: concept

Infrared waves, with frequencies from 300 GHz to 400 THz (wavelengths from 1 mm
to 770 nm), can be used for short-range communication. Infrared waves, having high
frequencies, cannot penetrate walls. This advantageous characteristic prevents interference between one system and another; a short-range communication system in one
room cannot be affected by another system in the next room. When we use our infrared
remote control, we do not interfere with the use of the remote by our neighbors. However, this same characteristic makes infrared signals useless for long-range communication. In addition, we cannot use infrared waves outside a building because the sun’s
rays contain infrared waves that can interfere with the communication.

#### Applications
> id: ch07-7-3-3-applications | src: book p.202 | kind: concept

The infrared band, almost 400 THz, has an excellent potential for data transmission.
Such a wide bandwidth can be used to transmit digital data with a very high data rate.
The Infrared Data Association (IrDA), an association for sponsoring the use of infrared
waves, has established standards for using these signals for communication between
devices such as keyboards, mice, PCs, and printers. For example, some manufacturers
provide a special port called the IrDA port that allows a wireless keyboard to commnicate
with a PC. The standard originally defined a data rate of 75 kbps for a distance up to
8 m. The recent standard defines a data rate of 4 Mbps.
Infrared signals defined by IrDA transmit through line of sight; the IrDA port on
the keyboard needs to point to the PC for transmission to occur.

Infrared signals can be used for short-range communication in a closed
area using line-of-sight propagation

## 7.4 END-CHAPTER MATERIALS
> id: ch07-7-4 | src: book 7.4; p.202 | kind: concept

### 7.4.1 Recommended Reading
> id: ch07-7-4-1 | src: book 7.4.1; p.202 | kind: concept

For more details about subjects discussed in this chapter, we recommend the following
books. The items in brackets [. . .] refer to the reference list at the end of the text.

#### Books
> id: ch07-7-4-1-books | src: book p.202 | kind: concept

Transmission media is discussed in [GW04], [Sta04], and [Tan03]. [SSS05] gives full
coverage of transmission media.

### 7.4.2 Key Terms
> id: ch07-7-4-2 | src: book 7.4.2; p.202 | kind: concept

- angle of incidence
- Bayonet Neill-Concelman (BNC)
- cladding
- coaxial cable
- core
- critical angle
- electromagnetic spectrum
- fiber-optic cable
- gauge
- ground propagation
- guided media
- horn antenna
- infrared wave
- IrDA port
- line-of-sight propagation
- microwave
- MT-RJ
- multimode graded-index fiber
- multimode step-index fiber
- omnidirectional antenna
- optical fiber
- parabolic dish antenna
- Radio Government (RG) rating
- radio wave
- reflection
- refraction
- RJ45
- shielded twisted-pair (STP)
- single-mode fiber
- sky propagation
- straight-tip (ST) connector
- subscriber channel (SC) connector
- transmission medium
- twisted-pair cable
- unguided medium
- unidirectional antenna
- unshielded twisted-pair (UTP)
- wireless communication

### 7.4.3 Summary
> id: ch07-7-4-3 | src: book 7.4.3; p.203 | kind: summary

Transmission media are actually located below the physical layer and are directly controlled by the physical layer. We could say that transmission media belong to layer
zero.
A guided medium provides a physical conduit from one device to another.
Twisted-pair cable consists of two insulated copper wires twisted together. Twisted-pair
cable is used for voice and data communications. Coaxial cable consists of a central
conductor and a shield. Coaxial cable is used in cable TV networks and traditional
Ethernet LANs. Fiber-optic cables are composed of a glass or plastic inner core surrounded by cladding, all encased in an outside jacket. Fiber-optic transmission is
becoming increasingly popular due to its noise resistance, low attenuation, and high-bandwidth capabilities. Fiber-optic cable is used in backbone networks, cable TV networks, and Fast Ethernet networks.
Unguided media (free space) transport electromagnetic waves without the use of a
physical conductor. Wireless data are transmitted through ground propagation, sky
propagation, and line-of-sight propagation.Wireless waves can be classified as radio
waves, microwaves, or infrared waves. Radio waves are omnidirectional; microwaves
are unidirectional. Microwaves are used for cellular phone, satellite, and wireless LAN
communications. Infrared waves are used for short-range communications such as
those between a PC and a peripheral device. They can also be used for indoor LANs.
