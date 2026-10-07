---
doc_type: chapter_data_card
chapter_id: data_communications_ch09
course_id: data_communications
chapter: 9
title: Introduction to Data-Link Layer
part: PART III Data-Link Layer
layer: data_link
order: 9
previous_chapters:
- data_communications_ch08
next_chapters:
- data_communications_ch12
prerequisites: []
builds_on: []
enables: []
topics:
- id: ch09-0
  title: Chapter Objectives
  covers: Chapter Objectives
- id: ch09-9-1
  title: 9.1 INTRODUCTION
  covers: INTRODUCTION
- id: ch09-9-1-1
  title: 9.1.1 Nodes and Links
  covers: Nodes and Links
- id: ch09-9-1-2
  title: 9.1.2 Services
  covers: Services
- id: ch09-9-1-3
  title: 9.1.3 Two Categories of Links
  covers: Two Categories of Links
- id: ch09-9-1-4
  title: 9.1.4 Two Sublayers
  covers: Two Sublayers
- id: ch09-9-2
  title: 9.2 LINK-LAYER ADDRESSING
  covers: LINK-LAYER ADDRESSING
- id: ch09-9-2-1
  title: 9.2.1 Three Types of addresses
  covers: Three Types of addresses
- id: ch09-9-2-2
  title: 9.2.2 Address Resolution Protocol (ARP)
  covers: Address Resolution Protocol (ARP)
- id: ch09-9-2-3
  title: 9.2.3 An Example of Communication
  covers: An Example of Communication
- id: ch09-9-3
  title: 9.3 END-CHAPTER MATERIALS
  covers: END-CHAPTER MATERIALS
- id: ch09-9-3-1
  title: 9.3.1 Recommended Reading
  covers: Recommended Reading
- id: ch09-9-3-2
  title: 9.3.2 Key Terms
  covers: Key Terms
- id: ch09-9-3-3
  title: 9.3.3 Summary
  covers: Summary
key_terms:
- Address Resolution Protocol (ARP)
- data link control (DLC)
- frame
- framing
- links
- media access control (MAC)
- nodes
standards_and_protocols:
- Ethernet
- IP
- TCP/IP
formulas_present: false
content_stats:
  sections: 14
  words: 7573
  approx_tokens: 9845
asset_stats:
  illustration: 16
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
question_stats:
  total: 29
  by_group:
    Questions: 14
    Problems: 15
syllabus_applied: false
syllabus_notes: No section-level exclusions applied.
source_files:
- Slide/ch_9/ch9.pdf
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
generated_at: '2026-10-07T03:32:00+00:00'
status: complete
source_authority:
  primary: book PDF
  supplementary: slides
  book_sha256: 2b60e3e88d1dd801b5f268d67e3fb4c889a22a275b5a1197f7822257f2bda932
retrieval_sections:
- id: ch09-0
  title: Chapter Objectives
  level: 2
- id: ch09-9-1
  title: 9.1 INTRODUCTION
  level: 2
- id: ch09-9-1-1
  title: 9.1.1 Nodes and Links
  level: 3
- id: ch09-9-1-2
  title: 9.1.2 Services
  level: 3
- id: ch09-9-1-2-framing
  title: Framing
  level: 4
- id: ch09-9-1-2-flow-control
  title: Flow Control
  level: 4
- id: ch09-9-1-2-error-control
  title: Error Control
  level: 4
- id: ch09-9-1-2-congestion-control
  title: Congestion Control
  level: 4
- id: ch09-9-1-3
  title: 9.1.3 Two Categories of Links
  level: 3
- id: ch09-9-1-4
  title: 9.1.4 Two Sublayers
  level: 3
- id: ch09-9-2
  title: 9.2 LINK-LAYER ADDRESSING
  level: 2
- id: ch09-9-2-1
  title: 9.2.1 Three Types of addresses
  level: 3
- id: ch09-9-2-1-unicast-address
  title: Unicast Address
  level: 4
- id: ch09-example-9-1
  title: Example 9.1
  level: 5
- id: ch09-9-2-1-multicast-address
  title: Multicast Address
  level: 4
- id: ch09-example-9-2
  title: Example 9.2
  level: 5
- id: ch09-9-2-1-broadcast-address
  title: Broadcast Address
  level: 4
- id: ch09-example-9-3
  title: Example 9.3
  level: 5
- id: ch09-9-2-2
  title: 9.2.2 Address Resolution Protocol (ARP)
  level: 3
- id: ch09-9-2-2-caching
  title: Caching
  level: 4
- id: ch09-9-2-2-packet-format
  title: Packet Format
  level: 4
- id: ch09-example-9-4
  title: Example 9.4
  level: 5
- id: ch09-9-2-3
  title: 9.2.3 An Example of Communication
  level: 3
- id: ch09-9-2-3-activities-at-alice-s-site
  title: Activities at Alice’s Site
  level: 4
- id: ch09-9-2-3-activities-at-router-r1
  title: Activities at Router R1
  level: 4
- id: ch09-9-2-3-activities-at-router-r2
  title: Activities at Router R2
  level: 4
- id: ch09-9-2-3-activities-at-bob-s-site
  title: Activities at Bob’s Site
  level: 4
- id: ch09-9-2-3-changes-in-addresses
  title: Changes in Addresses
  level: 4
- id: ch09-9-3
  title: 9.3 END-CHAPTER MATERIALS
  level: 2
- id: ch09-9-3-1
  title: 9.3.1 Recommended Reading
  level: 3
- id: ch09-9-3-1-books
  title: Books
  level: 4
- id: ch09-9-3-2
  title: 9.3.2 Key Terms
  level: 3
- id: ch09-9-3-3
  title: 9.3.3 Summary
  level: 3
review:
  source_pages: 235–255
  figures: 16
  questions: 29
  tables: 0
  formulas: no standalone mathematical formulas; address fields and values checked
  source_order_checked: true
  reviewed_at: '2026-10-07T03:33:20+00:00'
  method: native PDF reconstruction, annotation-free figure review, ARP field review,
    and question comparison
---
# Chapter 9: Introduction to Data-Link Layer — Data Card
