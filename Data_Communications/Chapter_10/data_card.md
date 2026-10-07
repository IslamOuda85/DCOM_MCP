---
doc_type: chapter_data_card
chapter_id: data_communications_ch10
course_id: data_communications
chapter: 10
title: Error Detection and Correction
part: PART III Data-Link Layer
layer: data_link
order: 10
previous_chapters:
- data_communications_ch09
next_chapters:
- data_communications_ch12
prerequisites: []
builds_on: []
enables: []
topics:
- id: ch10-0
  title: Chapter Objectives
  covers: Chapter Objectives
- id: ch10-1
  title: 10.1 Introduction
  covers: Introduction
- id: ch10-1-1
  title: 10.1.1 Types of Errors
  covers: Types of Errors
- id: ch10-1-2
  title: 10.1.2 Redundancy
  covers: Redundancy
- id: ch10-1-3
  title: 10.1.3 Detection Versus Correction
  covers: Detection Versus Correction
- id: ch10-1-4
  title: 10.1.4 Coding
  covers: Coding
- id: ch10-2
  title: 10.2 Block Coding
  covers: Block Coding
- id: ch10-2-1
  title: 10.2.1 Error Detection
  covers: Error Detection
- id: ch10-3
  title: 10.3 Cyclic Codes
  covers: Cyclic Codes
- id: ch10-3-1
  title: 10.3.1 CRC (Cyclic Redundancy Check)
  covers: CRC (Cyclic Redundancy Check)
- id: ch10-3-2
  title: 10.3.2 Polynomials
  covers: Polynomials
- id: ch10-3-3
  title: 10.3.3 Encoder Using Polynomials
  covers: Encoder Using Polynomials
- id: ch10-3-4
  title: 10.3.4 Analysis of Cyclic Codes
  covers: Analysis of Cyclic Codes
- id: ch10-3-5
  title: 10.3.5 Advantages of Cyclic Codes
  covers: Advantages of Cyclic Codes
- id: ch10-3-6
  title: 10.3.6 Other Cyclic Codes
  covers: Other Cyclic Codes
- id: ch10-3-7
  title: 10.3.7 Hardware Implementation
  covers: Hardware Implementation
- id: ch10-4
  title: 10.4 Checksum
  covers: Checksum
- id: ch10-4-1
  title: 10.4.1 Concept
  covers: Concept
- id: ch10-4-2
  title: 10.4.2 Other Approaches to the Checksum
  covers: Other Approaches to the Checksum
- id: ch10-5
  title: 10.5 Forward Error Correction
  covers: Forward Error Correction
- id: ch10-5-1
  title: 10.5.1 Using Hamming Distance
  covers: Using Hamming Distance
- id: ch10-5-2
  title: 10.5.2 Using XOR
  covers: Using XOR
- id: ch10-5-3
  title: 10.5.3 Chunk Interleaving
  covers: Chunk Interleaving
- id: ch10-5-4
  title: 10.5.4 Combining Hamming Distance and Interleaving
  covers: Combining Hamming Distance and Interleaving
- id: ch10-5-5
  title: 10.5.5 Compounding High- and Low-Resolution Packets
  covers: Compounding High- and Low-Resolution Packets
- id: ch10-summary
  title: Chapter Summary
  covers: Chapter Summary
key_terms:
- single-bit error
- burst error
- redundancy
- error detection
- error correction
- block coding
- convolution coding
- datawords
- codewords
- Hamming distance
- minimum Hamming distance
- linear block codes
- parity-check code
- parity bit
- syndrome
- cyclic codes
- cyclic redundancy check
- generator polynomial
- error polynomial
- checksum
- Fletcher checksum
- Adler checksum
- forward error correction
- chunk interleaving
standards_and_protocols:
- CRC-8
- CRC-10
- CRC-16
- CRC-32
- ATM
- HDLC
- LANs
formulas_present: true
content_stats:
  sections: 26
  words: 9064
  approx_tokens: 11783
asset_stats:
  illustration: 23
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
question_stats:
  total: 45
  by_group:
    Questions: 15
    Problems: 30
syllabus_applied: false
syllabus_notes: 'Syllabus Week 11 covers ''D. L. layer, Error Detection and Correction''
  matching textbook Chapter 9 and Chapter 10. No section-level exclusions applied
  (syllabus_applied: false).'
source_files:
- Slide/ch_10/ch10.pdf
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
generated_at: '2026-10-07T03:42:37+00:00'
source_authority:
  primary: book PDF
  supplementary: slides
  book_sha256: d61671f4e55d29078ad825e95e326044c3955a4811f40ac3818761d4b700ab49
retrieval_sections:
- id: ch10-0
  title: Chapter Objectives
  level: 2
- id: ch10-1
  title: 10.1 Introduction
  level: 2
- id: ch10-1-1
  title: 10.1.1 Types of Errors
  level: 3
- id: ch10-1-2
  title: 10.1.2 Redundancy
  level: 3
- id: ch10-1-3
  title: 10.1.3 Detection Versus Correction
  level: 3
- id: ch10-1-4
  title: 10.1.4 Coding
  level: 3
- id: ch10-2
  title: 10.2 Block Coding
  level: 2
- id: ch10-2-1
  title: 10.2.1 Error Detection
  level: 3
- id: ch10-example-10-1
  title: Example 10.1
  level: 4
- id: ch10-2-1-hamming-distance
  title: Hamming Distance
  level: 4
- id: ch10-example-10-2
  title: Example 10.2
  level: 4
- id: ch10-2-1-minimum-hamming-distance
  title: Minimum Hamming Distance for Error Detection
  level: 4
- id: ch10-example-10-3
  title: Example 10.3
  level: 4
- id: ch10-example-10-4
  title: Example 10.4
  level: 4
- id: ch10-2-1-linear-block-codes
  title: Linear Block Codes
  level: 4
- id: ch10-example-10-5
  title: Example 10.5
  level: 4
- id: ch10-2-1-minimum-distance-linear
  title: Minimum Distance for Linear Block Codes
  level: 4
- id: ch10-example-10-6
  title: Example 10.6
  level: 4
- id: ch10-2-1-parity-check-code
  title: Parity-Check Code
  level: 4
- id: ch10-example-10-7
  title: Example 10.7
  level: 4
- id: ch10-3
  title: 10.3 Cyclic Codes
  level: 2
- id: ch10-3-1
  title: 10.3.1 CRC (Cyclic Redundancy Check)
  level: 3
- id: ch10-3-2
  title: 10.3.2 Polynomials
  level: 3
- id: ch10-3-3
  title: 10.3.3 Encoder Using Polynomials
  level: 3
- id: ch10-3-4
  title: 10.3.4 Analysis of Cyclic Codes
  level: 3
- id: ch10-3-4-single-bit-error
  title: Single-Bit Error
  level: 4
- id: ch10-example-10-8
  title: Example 10.8
  level: 4
- id: ch10-3-4-two-isolated-single-bit-errors
  title: Two Isolated Single-Bit Errors
  level: 4
- id: ch10-example-10-9
  title: Example 10.9
  level: 4
- id: ch10-3-4-odd-numbers-of-errors
  title: Odd Numbers of Errors
  level: 4
- id: ch10-3-4-burst-errors
  title: Burst Errors
  level: 4
- id: ch10-example-10-10
  title: Example 10.10
  level: 4
- id: ch10-3-5
  title: 10.3.5 Advantages of Cyclic Codes
  level: 3
- id: ch10-3-6
  title: 10.3.6 Other Cyclic Codes
  level: 3
- id: ch10-3-7
  title: 10.3.7 Hardware Implementation
  level: 3
- id: ch10-4
  title: 10.4 Checksum
  level: 2
- id: ch10-4-1
  title: 10.4.1 Concept
  level: 3
- id: ch10-example-10-11
  title: Example 10.11
  level: 4
- id: ch10-example-10-12
  title: Example 10.12
  level: 4
- id: ch10-example-10-13
  title: Example 10.13
  level: 4
- id: ch10-4-1-internet-checksum
  title: Internet Checksum
  level: 4
- id: ch10-4-2
  title: 10.4.2 Other Approaches to the Checksum
  level: 3
- id: ch10-4-2-fletcher-checksum
  title: Fletcher Checksum
  level: 4
- id: ch10-4-2-adler-checksum
  title: Adler Checksum
  level: 4
- id: ch10-5
  title: 10.5 Forward Error Correction
  level: 2
- id: ch10-5-1
  title: 10.5.1 Using Hamming Distance
  level: 3
- id: ch10-5-2
  title: 10.5.2 Using XOR
  level: 3
- id: ch10-5-3
  title: 10.5.3 Chunk Interleaving
  level: 3
- id: ch10-5-4
  title: 10.5.4 Combining Hamming Distance and Interleaving
  level: 3
- id: ch10-5-5
  title: 10.5.5 Compounding High- and Low-Resolution Packets
  level: 3
- id: ch10-summary
  title: Chapter Summary
  level: 2
review:
  source_pages: 257–292
  figures: 23
  questions: 45
  tables: 5
  worked_examples: 13
  formulas: Hamming distance, CRC polynomial arithmetic, checksum, and FEC equations
    checked and represented in LaTeX
  source_order_checked: true
  reviewed_at: '2026-10-07T03:42:44+00:00'
  method: native PDF comparison, annotation-free figure review, worked-example reconstruction,
    formula audit, and question comparison
source_corrections:
- location: Problems P10-9
  source_text: Table 5.4
  corrected_to: Table 10.4
  reason: CRC-8 is listed in this chapter’s standard-polynomial table.
- location: Problem P10-16
  source_text: Table 10.7
  corrected_to: Table 10.4
  reason: Chapter 10 contains no Table 10.7; CRC-8 is in Table 10.4.
---
# Chapter 10: Error Detection and Correction — Data Card

Chapter 10 is the core error-control module in Part III (Data-Link Layer) of the course. It occupies position 10 in the curricular sequence.

In the course progression, it follows Chapter 9 (Introduction to Data-Link Layer) and precedes Chapter 12 (Media Access Control). No explicit intra-book backward cross-references were identified in the source text; however, it conceptually grounds the framing and error-checking mechanisms utilized across the data-link layer.

All 23 visual components (22 body illustrations and 1 question figure) were rendered at 300 DPI and cataloged in the asset manifest. All five body tables were reconstructed from native text layout into GitHub-flavored Markdown. Thirteen worked examples were compared with the book and repaired where the earlier draft had shifted numbering or substituted calculations.
