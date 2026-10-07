---
doc_type: chapter_data_card
chapter_id: data_communications_ch12
course_id: data_communications
chapter: 12
title: Media Access Control (MAC)
part: PART III Data-Link Layer
layer: data_link
order: 11
previous_chapters:
- data_communications_ch09
next_chapters:
- data_communications_ch13
prerequisites: []
builds_on: []
enables: []
topics:
- id: ch12-0
  title: Chapter Objectives
  covers: Chapter Objectives
- id: ch12-12-1
  title: 12.1 RANDOM ACCESS
  covers: RANDOM ACCESS
- id: ch12-12-1-1
  title: 12.1.1 ALOHA
  covers: ALOHA
- id: ch12-12-1-2
  title: 12.1.2 CSMA
  covers: CSMA
- id: ch12-12-1-3
  title: 12.1.3 CSMA/CD
  covers: CSMA/CD
- id: ch12-12-1-4
  title: 12.1.4 CSMA/CA
  covers: CSMA/CA
- id: ch12-12-2
  title: 12.2 CONTROLLED ACCESS
  covers: CONTROLLED ACCESS
- id: ch12-12-2-1
  title: 12.2.1 Reservation
  covers: Reservation
- id: ch12-12-2-2
  title: 12.2.2 Polling
  covers: Polling
- id: ch12-12-2-3
  title: 12.2.3 Token Passing
  covers: Token Passing
- id: ch12-12-3
  title: 12.3 CHANNELIZATION
  covers: CHANNELIZATION
- id: ch12-12-3-1
  title: 12.3.1 FDMA
  covers: FDMA
- id: ch12-12-3-2
  title: 12.3.2 TDMA
  covers: TDMA
- id: ch12-12-3-3
  title: 12.3.3 CDMA
  covers: CDMA
- id: ch12-12-4
  title: 12.4 END-CHAPTER MATERIALS
  covers: END-CHAPTER MATERIALS
- id: ch12-12-4-1
  title: 12.4.1 Recommended Reading
  covers: Recommended Reading
- id: ch12-12-4-2
  title: 12.4.2 Key Terms
  covers: Key Terms
- id: ch12-12-4-3
  title: 12.4.3 Summary
  covers: Summary
key_terms:
- 1-persistent method
- ALOHA
- binary exponential backoff
- carrier sense multiple access (CSMA)
- carrier sense multiple access with collision
- avoidance (CSMA/CA)
- carrier sense multiple access with collision
- detection (CSMA/CD)
- channelization
- code-division multiple access (CDMA)
- collision
- contention
- contention window
- controlled access
- DCF interframe space (DIFS)
- frequency-division multiple access (FDMA)
- inner product
- interface space (IFS)
- jamming signal
- media access control (MAC)
- multiple access (MA)
- network allocation vector (NAV)
- nonpersistent method
- orthogonal sequence
- p-persistent method
- polling
- primary station
- propagation time
- pure ALOHA
- random access
- reservation
- secondary station
- short interframe space (SIFS)
- slotted ALOHA
- time-division multiple access (TDMA)
- token
- token passing
- vulnerable time
- Walsh table
standards_and_protocols:
- Ethernet
- RFC 1141
formulas_present: true
content_stats:
  sections: 18
  words: 13874
  approx_tokens: 18036
asset_stats:
  illustration: 30
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
question_stats:
  total: 49
  by_group:
    Questions: 24
    Problems: 25
syllabus_applied: false
syllabus_notes: No section-level exclusions applied.
source_files:
- Slide/ch_12/ch12.pdf
files:
  content: content.md
  questions: questions.md
  assets: assets/
extraction_status:
  content: complete
  questions: complete
  assets: complete
open_issues: []
spec_version: 1.1-controller
generated_at: '2026-10-07T03:48:17+00:00'
status: complete
source_authority:
  primary: book PDF
  supplementary: slides
  book_sha256: 4cf1cefe4374811937a764797eb901b5cafc40a444e224bbecb64937297c8c27
retrieval_sections:
- id: ch12-0
  title: Chapter Objectives
  level: 2
- id: ch12-12-1
  title: 12.1 RANDOM ACCESS
  level: 2
- id: ch12-12-1-1
  title: 12.1.1 ALOHA
  level: 3
- id: ch12-12-1-1-pure-aloha
  title: Pure ALOHA
  level: 4
- id: ch12-example-12-1
  title: Example 12.1
  level: 5
- id: ch12-12-1-1-vulnerable-time
  title: Vulnerable time
  level: 4
- id: ch12-example-12-2
  title: Example 12.2
  level: 5
- id: ch12-12-1-1-pure-throughput
  title: Throughput
  level: 4
- id: ch12-example-12-3
  title: Example 12.3
  level: 5
- id: ch12-12-1-1-slotted-aloha
  title: Slotted ALOHA
  level: 4
- id: ch12-12-1-1-slotted-aloha-throughput
  title: Throughput
  level: 4
- id: ch12-example-12-4
  title: Example 12.4
  level: 5
- id: ch12-12-1-2
  title: 12.1.2 CSMA
  level: 3
- id: ch12-12-1-2-vulnerable-time
  title: Vulnerable Time
  level: 4
- id: ch12-12-1-2-persistence-methods
  title: Persistence Methods
  level: 4
- id: ch12-12-1-2-1-persistent
  title: 1-Persistent
  level: 4
- id: ch12-12-1-2-nonpersistent
  title: Nonpersistent
  level: 4
- id: ch12-12-1-3
  title: 12.1.3 CSMA/CD
  level: 3
- id: ch12-12-1-3-minimum-frame-size
  title: Minimum Frame Size
  level: 4
- id: ch12-example-12-5
  title: Example 12.5
  level: 5
- id: ch12-12-1-3-procedure
  title: Procedure
  level: 4
- id: ch12-12-1-3-energy-level
  title: Energy Level
  level: 4
- id: ch12-12-1-3-throughput
  title: Throughput
  level: 4
- id: ch12-12-1-3-traditional-ethernet
  title: Traditional Ethernet
  level: 4
- id: ch12-12-1-4
  title: 12.1.4 CSMA/CA
  level: 3
- id: ch12-12-1-4-frame-exchange-time-line
  title: Frame Exchange Time Line
  level: 4
- id: ch12-12-1-4-network-allocation-vector
  title: Network Allocation Vector
  level: 4
- id: ch12-12-1-4-collision-during-handshaking
  title: Collision During Handshaking
  level: 4
- id: ch12-12-1-4-hidden-station-problem
  title: Hidden-Station Problem
  level: 4
- id: ch12-12-1-4-csma-ca-and-wireless-networks
  title: CSMA/CA and Wireless Networks
  level: 4
- id: ch12-12-2
  title: 12.2 CONTROLLED ACCESS
  level: 2
- id: ch12-12-2-1
  title: 12.2.1 Reservation
  level: 3
- id: ch12-12-2-2
  title: 12.2.2 Polling
  level: 3
- id: ch12-12-2-2-select
  title: Select
  level: 4
- id: ch12-12-2-2-poll
  title: Poll
  level: 4
- id: ch12-12-2-3
  title: 12.2.3 Token Passing
  level: 3
- id: ch12-12-2-3-logical-ring
  title: Logical Ring
  level: 4
- id: ch12-12-3
  title: 12.3 CHANNELIZATION
  level: 2
- id: ch12-12-3-1
  title: 12.3.1 FDMA
  level: 3
- id: ch12-12-3-2
  title: 12.3.2 TDMA
  level: 3
- id: ch12-12-3-3
  title: 12.3.3 CDMA
  level: 3
- id: ch12-12-3-3-analogy
  title: Analogy
  level: 4
- id: ch12-12-3-3-idea
  title: Idea
  level: 4
- id: ch12-12-3-3-chips
  title: Chips
  level: 4
- id: ch12-12-3-3-data-representation
  title: Data Representation
  level: 4
- id: ch12-12-3-3-encoding-and-decoding
  title: Encoding and Decoding
  level: 4
- id: ch12-12-3-3-signal-level
  title: Signal Level
  level: 4
- id: ch12-12-3-3-sequence-generation
  title: Sequence Generation
  level: 4
- id: ch12-example-12-6
  title: Example 12.6
  level: 5
- id: ch12-example-12-7
  title: Example 12.7
  level: 5
- id: ch12-example-12-8
  title: Example 12.8
  level: 5
- id: ch12-12-4
  title: 12.4 END-CHAPTER MATERIALS
  level: 2
- id: ch12-12-4-1
  title: 12.4.1 Recommended Reading
  level: 3
- id: ch12-12-4-1-books
  title: Books
  level: 4
- id: ch12-12-4-1-rfcs
  title: RFCs
  level: 4
- id: ch12-12-4-2
  title: 12.4.2 Key Terms
  level: 3
- id: ch12-12-4-3
  title: 12.4.3 Summary
  level: 3
review:
  source_pages: 325–360
  figures: 30
  questions: 49
  worked_examples: 8
  formulas: ALOHA throughput, CSMA timing, CDMA inner products, and Walsh construction
    checked and represented in LaTeX
  source_order_checked: true
  reviewed_at: '2026-10-07T03:48:32+00:00'
  method: native PDF reconstruction, annotation-free figure review, equation repair,
    question-boundary reconstruction, and source comparison
source_corrections:
- location: Example 12.4
  source_text: 1000 × 0.0368 and 500 × 0.0303
  corrected_to: 1000 × 0.368 and 500 × 0.303
  reason: The printed decimal factors conflict with the stated percentages and products.
- location: Questions Q12-12 and Q12-13
  source_text: success in an Aloha network
  corrected_to: success in a CSMA/CD network; success in a CSMA/CA network
  reason: The cited figures are the CSMA/CD and CSMA/CA procedures.
- location: Problems P12-17 and P12-25
  source_text: CDMA/CD; CSMA using a Walsh table
  corrected_to: CSMA/CD; CDMA using a Walsh table
  reason: The surrounding concepts and cited Walsh table identify the intended protocols.
---
# Chapter 12: Media Access Control (MAC) — Data Card
