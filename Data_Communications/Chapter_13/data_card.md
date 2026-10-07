---
doc_type: chapter_data_card
chapter_id: data_communications_ch13
course_id: data_communications
chapter: 13
title: 'Wired LANs: Ethernet'
part: PART III Data-Link Layer
layer: data_link
order: 12
previous_chapters:
- data_communications_ch12
next_chapters: []
prerequisites: []
builds_on: []
enables: []
topics:
- id: ch13-0
  title: Chapter Objectives
  covers: Chapter Objectives
- id: ch13-13-1
  title: 13.1 ETHERNET PROTOCOL
  covers: ETHERNET PROTOCOL
- id: ch13-13-1-1
  title: 13.1.1 IEEE Project 802
  covers: IEEE Project 802
- id: ch13-13-1-2
  title: 13.1.2 Ethernet Evolution
  covers: Ethernet Evolution
- id: ch13-13-2
  title: 13.2 STANDARD ETHERNET
  covers: STANDARD ETHERNET
- id: ch13-13-2-1
  title: 13.2.1 Characteristics
  covers: Characteristics
- id: ch13-13-2-2
  title: 13.2.2 Addressing
  covers: Addressing
- id: ch13-13-2-3
  title: 13.2.3 Access Method
  covers: Access Method
- id: ch13-13-2-4
  title: 13.2.4 Efficiency of Standard Ethernet
  covers: Efficiency of Standard Ethernet
- id: ch13-13-2-5
  title: 13.2.5 Implementation
  covers: Implementation
- id: ch13-13-2-6
  title: 13.2.6 Changes in the Standard
  covers: Changes in the Standard
- id: ch13-13-3
  title: 13.3 FAST ETHERNET (100 MBPS)
  covers: FAST ETHERNET (100 MBPS)
- id: ch13-13-3-1
  title: 13.3.1 Access Method
  covers: Access Method
- id: ch13-13-3-2
  title: 13.3.2 Physical Layer
  covers: Physical Layer
- id: ch13-13-4
  title: 13.4 GIGABIT ETHERNET
  covers: GIGABIT ETHERNET
- id: ch13-13-4-1
  title: 13.4.1 MAC Sublayer
  covers: MAC Sublayer
- id: ch13-13-4-2
  title: 13.4.2 Physical Layer
  covers: Physical Layer
- id: ch13-13-5
  title: 13.5 10 GIGABIT ETHERNET
  covers: 10 GIGABIT ETHERNET
- id: ch13-13-5-1
  title: 13.5.1 Implementation
  covers: Implementation
- id: ch13-13-6
  title: 13.6 END-CHAPTER MATERIALS
  covers: END-CHAPTER MATERIALS
- id: ch13-13-6-1
  title: 13.6.1 Recommended Reading
  covers: Recommended Reading
- id: ch13-13-6-2
  title: 13.6.2 Key Terms
  covers: Key Terms
- id: ch13-13-6-3
  title: 13.6.3 Summary
  covers: Summary
key_terms:
- 10 Gigabit Ethernet
- 1000Base-CX
- 1000Base-LX
- 1000Base-SX
- 1000Base-T
- 100Base-FX
- 100Base-T4
- 100Base-TX
- 10Base2
- 10Base5
- 10Base-F
- 10Base-T
- 10GBase-EW
- 10GBase-LR
- 10GBase-SR
- 10GBase-X4
- autonegotiation
- bridge
- carrier extension
- Cheapernet
- collision domain
- Fast Ethernet
- frame bursting
- full-duplex switched Ethernet
- Gigabit Ethernet
- hexadecimal notation
- logical link control (LLC)
- media access control (MAC)
- network interface card (NIC)
- Project 802
- Standard Ethernet
- switch
- switched Ethernet
- thick Ethernet
- Thicknet
- thin Ethernet
- transceiver
- twisted-pair Ethernet
standards_and_protocols:
- ATM
- ETHERNET
- Ethernet
- IEEE 802.3
- IP
- RFC 1141
- TCP/IP
formulas_present: true
content_stats:
  sections: 23
  words: 11591
  approx_tokens: 15068
  markdown_tables: 4
asset_stats:
  illustration: 17
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
question_stats:
  total: 21
  by_group:
    Questions: 10
    Problems: 11
syllabus_applied: false
syllabus_notes: No section-level exclusions applied.
source_files:
- Slide/ch_13/Ch13.pdf
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
generated_at: '2026-10-07T06:54:26+03:00'
status: complete
tables_present:
- id: Table 13.1
  title: Summary of Standard Ethernet implementations
  location: content
  source_page: 370
  rows: 4
- id: Table 13.2
  title: Summary of Fast Ethernet implementations
  location: content
  source_page: 379
  rows: 3
- id: Table 13.3
  title: Summary of Gigabit Ethernet implementations
  location: content
  source_page: 382
  rows: 4
- id: Table 13.4
  title: Summary of 10 Gigabit Ethernet implementations
  location: content
  source_page: 382
  rows: 8
source_priority: The chapter PDF is authoritative; available slides are supportive
  material.
source_authority:
  primary: book PDF
  supplementary: slides
  book_sha256: 4a762e1d7906040434267451e7cc670b00b9fa01e05b923549655667c0daeb14
retrieval_sections:
- id: ch13-0
  title: Chapter Objectives
  level: 2
- id: ch13-13-1
  title: 13.1 ETHERNET PROTOCOL
  level: 2
- id: ch13-13-1-1
  title: 13.1.1 IEEE Project 802
  level: 3
- id: ch13-13-1-1-logical-link-control-llc
  title: Logical Link Control (LLC)
  level: 4
- id: ch13-13-1-1-media-access-control-mac
  title: Media Access Control (MAC)
  level: 4
- id: ch13-13-1-2
  title: 13.1.2 Ethernet Evolution
  level: 3
- id: ch13-13-2
  title: 13.2 STANDARD ETHERNET
  level: 2
- id: ch13-13-2-1
  title: 13.2.1 Characteristics
  level: 3
- id: ch13-13-2-1-connectionless-and-unreliable-service
  title: Connectionless and Unreliable Service
  level: 4
- id: ch13-13-2-1-frame-format
  title: Frame Format
  level: 4
- id: ch13-13-2-1-frame-length
  title: Frame Length
  level: 4
- id: ch13-13-2-2
  title: 13.2.2 Addressing
  level: 3
- id: ch13-13-2-2-transmission-of-address-bits
  title: Transmission of Address Bits
  level: 4
- id: ch13-example-13-1
  title: Example 13.1
  level: 4
- id: ch13-13-2-2-unicast-multicast-and-broadcast-addresses
  title: Unicast, Multicast, and Broadcast Addresses
  level: 4
- id: ch13-example-13-2
  title: Example 13.2
  level: 4
- id: ch13-13-2-2-distinguish-between-unicast-multicast-and-broadcast-transmission
  title: Distinguish Between Unicast, Multicast, and Broadcast Transmission
  level: 4
- id: ch13-13-2-3
  title: 13.2.3 Access Method
  level: 3
- id: ch13-13-2-4
  title: 13.2.4 Efficiency of Standard Ethernet
  level: 3
- id: ch13-example-13-3
  title: Example 13.3
  level: 4
- id: ch13-13-2-5
  title: 13.2.5 Implementation
  level: 3
- id: ch13-13-2-5-encoding-and-decoding
  title: Encoding and Decoding
  level: 4
- id: ch13-13-2-5-10base5-thick-ethernet
  title: '10Base5: Thick Ethernet'
  level: 4
- id: ch13-13-2-5-10base2-thin-ethernet
  title: '10Base2: Thin Ethernet'
  level: 4
- id: ch13-13-2-5-10base-t-twisted-pair-ethernet
  title: '10Base-T: Twisted-Pair Ethernet'
  level: 4
- id: ch13-13-2-5-10base-f-fiber-ethernet
  title: '10Base-F: Fiber Ethernet'
  level: 4
- id: ch13-13-2-6
  title: 13.2.6 Changes in the Standard
  level: 3
- id: ch13-13-2-6-bridged-ethernet
  title: Bridged Ethernet
  level: 4
- id: ch13-13-2-6-raising-the-bandwidth
  title: Raising the Bandwidth
  level: 4
- id: ch13-13-2-6-separating-collision-domains
  title: Separating Collision Domains
  level: 4
- id: ch13-13-2-6-switched-ethernet
  title: Switched Ethernet
  level: 4
- id: ch13-13-2-6-full-duplex-ethernet
  title: Full-Duplex Ethernet
  level: 4
- id: ch13-13-2-6-no-need-for-csma-cd
  title: No Need for CSMA/CD
  level: 4
- id: ch13-13-2-6-mac-control-layer
  title: MAC Control Layer
  level: 4
- id: ch13-13-3
  title: 13.3 FAST ETHERNET (100 MBPS)
  level: 2
- id: ch13-13-3-1
  title: 13.3.1 Access Method
  level: 3
- id: ch13-13-3-1-autonegotiation
  title: Autonegotiation
  level: 4
- id: ch13-13-3-2
  title: 13.3.2 Physical Layer
  level: 3
- id: ch13-13-3-2-topology
  title: Topology
  level: 4
- id: ch13-13-3-2-encoding
  title: Encoding
  level: 4
- id: ch13-13-3-2-summary
  title: Summary
  level: 4
- id: ch13-13-4
  title: 13.4 GIGABIT ETHERNET
  level: 2
- id: ch13-13-4-1
  title: 13.4.1 MAC Sublayer
  level: 3
- id: ch13-13-4-1-full-duplex-mode
  title: Full-Duplex Mode
  level: 4
- id: ch13-13-4-1-half-duplex-mode
  title: Half-Duplex Mode
  level: 4
- id: ch13-13-4-1-traditional
  title: Traditional
  level: 4
- id: ch13-13-4-1-carrier-extension
  title: Carrier Extension
  level: 4
- id: ch13-13-4-1-frame-bursting
  title: Frame Bursting
  level: 4
- id: ch13-13-4-2
  title: 13.4.2 Physical Layer
  level: 3
- id: ch13-13-4-2-topology
  title: Topology
  level: 4
- id: ch13-13-4-2-implementation
  title: Implementation
  level: 4
- id: ch13-13-4-2-encoding
  title: Encoding
  level: 4
- id: ch13-13-4-2-implementation-summary
  title: Implementation Summary
  level: 4
- id: ch13-13-5
  title: 13.5 10 GIGABIT ETHERNET
  level: 2
- id: ch13-13-5-1
  title: 13.5.1 Implementation
  level: 3
- id: ch13-13-6
  title: 13.6 END-CHAPTER MATERIALS
  level: 2
- id: ch13-13-6-1
  title: 13.6.1 Recommended Reading
  level: 3
- id: ch13-13-6-1-books
  title: Books
  level: 4
- id: ch13-13-6-1-rfcs
  title: RFCs
  level: 4
- id: ch13-13-6-2
  title: 13.6.2 Key Terms
  level: 3
- id: ch13-13-6-3
  title: 13.6.3 Summary
  level: 3
review:
  source_pages: 361–385
  figures: 17
  questions: 21
  tables: 4
  worked_examples: 3
  formulas: Ethernet efficiency, propagation delay, and transmission delay checked
    and represented in LaTeX
  source_order_checked: true
  reviewed_at: '2026-10-07T03:54:27+00:00'
  method: native PDF reconstruction, native table recovery, annotation-free figure
    review, formula repair, and question comparison
source_notes:
- location: Table 13.2
  note: The book prints 185 m for 100Base-FX; this source value is preserved because
    the course PDF is authoritative.
---
# Chapter 13: Wired LANs: Ethernet — Data Card
