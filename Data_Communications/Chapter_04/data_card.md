---
doc_type: chapter_data_card
chapter_id: data_communications_ch04
course_id: data_communications
chapter: 4
title: Digital Transmission
part: PART II Physical Layer
layer: physical
order: 4
previous_chapters:
- data_communications_ch03
next_chapters:
- data_communications_ch05
prerequisites: []
builds_on: []
enables: []
topics:
- id: ch04-0
  title: Chapter Objectives
  covers: Chapter Objectives
- id: ch04-4-1
  title: 4.1 DIGITAL-TO-DIGITAL CONVERSION
  covers: DIGITAL-TO-DIGITAL CONVERSION
- id: ch04-4-1-1
  title: 4.1.1 Line Coding
  covers: Line Coding
- id: ch04-4-1-2
  title: 4.1.2 Line Coding Schemes
  covers: Line Coding Schemes
- id: ch04-4-1-3
  title: 4.1.3 Block Coding
  covers: Block Coding
- id: ch04-4-1-4
  title: 4.1.4 Scrambling
  covers: Scrambling
- id: ch04-4-2
  title: 4.2 ANALOG-TO-DIGITAL CONVERSION
  covers: ANALOG-TO-DIGITAL CONVERSION
- id: ch04-4-2-1
  title: 4.2.1 Pulse Code Modulation (PCM)
  covers: Pulse Code Modulation (PCM)
- id: ch04-4-2-2
  title: 4.2.2 Delta Modulation (DM)
  covers: Delta Modulation (DM)
- id: ch04-4-3
  title: 4.3 TRANSMISSION MODES
  covers: TRANSMISSION MODES
- id: ch04-4-3-1
  title: 4.3.1 Parallel Transmission
  covers: Parallel Transmission
- id: ch04-4-3-2
  title: 4.3.2 Serial Transmission
  covers: Serial Transmission
- id: ch04-4-4
  title: 4.4 END-CHAPTER MATERIALS
  covers: END-CHAPTER MATERIALS
- id: ch04-4-4-1
  title: 4.4.1 Recommended Reading
  covers: Recommended Reading
- id: ch04-4-4-2
  title: 4.4.2 Key Terms
  covers: Key Terms
- id: ch04-4-4-3
  title: 4.4.3 Summary
  covers: Summary
key_terms:
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
standards_and_protocols: []
formulas_present: true
content_stats:
  sections: 16
  words: 17703
  approx_tokens: 23014
  markdown_tables: 2
asset_stats:
  illustration: 36
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
question_stats:
  total: 32
  by_group:
    Questions: 12
    Problems: 20
syllabus_applied: false
syllabus_notes: No section-level exclusions applied.
source_files:
- Slide/ch_4/ch4.pdf
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
generated_at: '2026-10-07T06:03:32+03:00'
status: complete
tables_present:
- id: Table 4.1
  title: Summary of line-coding schemes
  location: content
  source_page: 109
  rows: 9
- id: Table 4.2
  title: 4B/5B mapping codes
  location: content
  source_page: 111
  rows: 16
source_priority: The chapter PDF is authoritative; available slides are supportive
  material.
source_authority:
  primary: book PDF
  supplementary: slides
  book_sha256: 8da436150fdec1b8b33f3ec7b8653a59bc3adc092cbf9b2a151070844e6eafc4
retrieval_sections:
- id: ch04-0
  title: Chapter Objectives
  level: 2
- id: ch04-4-1
  title: 4.1 DIGITAL-TO-DIGITAL CONVERSION
  level: 2
- id: ch04-4-1-1
  title: 4.1.1 Line Coding
  level: 3
- id: ch04-4-1-1-characteristics
  title: Characteristics
  level: 4
- id: ch04-4-1-1-signal-element-versus-data-element
  title: Signal Element Versus Data Element
  level: 4
- id: ch04-4-1-1-data-rate-versus-signal-rate
  title: Data Rate Versus Signal Rate
  level: 4
- id: ch04-4-1-1-bandwidth
  title: Bandwidth
  level: 4
- id: ch04-4-1-1-baseline-wandering
  title: Baseline Wandering
  level: 4
- id: ch04-4-1-1-dc-components
  title: DC Components
  level: 4
- id: ch04-4-1-1-self-synchronization
  title: Self-synchronization
  level: 4
- id: ch04-4-1-1-built-in-error-detection
  title: Built-in Error Detection
  level: 4
- id: ch04-4-1-1-immunity-to-noise-and-interference
  title: Immunity to Noise and Interference
  level: 4
- id: ch04-4-1-1-complexity
  title: Complexity
  level: 4
- id: ch04-4-1-2
  title: 4.1.2 Line Coding Schemes
  level: 3
- id: ch04-4-1-2-unipolar-scheme
  title: Unipolar Scheme
  level: 4
- id: ch04-4-1-2-nrz-non-return-to-zero
  title: NRZ (Non-Return-to-Zero)
  level: 4
- id: ch04-4-1-2-polar-schemes
  title: Polar Schemes
  level: 4
- id: ch04-4-1-2-non-return-to-zero-nrz
  title: Non-Return-to-Zero (NRZ)
  level: 4
- id: ch04-4-1-2-return-to-zero-rz
  title: Return-to-Zero (RZ)
  level: 4
- id: ch04-4-1-2-biphase-manchester-and-differential-manchester
  title: 'Biphase: Manchester and Differential Manchester'
  level: 4
- id: ch04-4-1-2-bipolar-schemes
  title: Bipolar Schemes
  level: 4
- id: ch04-4-1-2-ami-and-pseudoternary
  title: AMI and Pseudoternary
  level: 4
- id: ch04-4-1-2-multilevel-schemes
  title: Multilevel Schemes
  level: 4
- id: ch04-4-1-2-2b1q
  title: 2B1Q
  level: 4
- id: ch04-4-1-2-8b6t
  title: 8B6T
  level: 4
- id: ch04-4-1-2-4d-pam5
  title: 4D-PAM5
  level: 4
- id: ch04-4-1-2-multitransition-mlt-3
  title: 'Multitransition: MLT-3'
  level: 4
- id: ch04-4-1-2-summary-of-line-coding-schemes
  title: Summary of Line Coding Schemes
  level: 4
- id: ch04-4-1-3
  title: 4.1.3 Block Coding
  level: 3
- id: ch04-4-1-3-4b-5b
  title: 4B/5B
  level: 4
- id: ch04-4-1-3-8b-10b
  title: 8B/10B
  level: 4
- id: ch04-4-1-4
  title: 4.1.4 Scrambling
  level: 3
- id: ch04-4-1-4-b8zs
  title: B8ZS
  level: 4
- id: ch04-4-1-4-hdb3
  title: HDB3
  level: 4
- id: ch04-4-2
  title: 4.2 ANALOG-TO-DIGITAL CONVERSION
  level: 2
- id: ch04-4-2-1
  title: 4.2.1 Pulse Code Modulation (PCM)
  level: 3
- id: ch04-4-2-1-sampling
  title: Sampling
  level: 4
- id: ch04-4-2-1-sampling-rate
  title: Sampling Rate
  level: 4
- id: ch04-4-2-1-quantization
  title: Quantization
  level: 4
- id: ch04-4-2-1-quantization-levels
  title: Quantization Levels
  level: 4
- id: ch04-4-2-1-quantization-error
  title: Quantization Error
  level: 4
- id: ch04-4-2-1-uniform-versus-nonuniform-quantization
  title: Uniform Versus Nonuniform Quantization
  level: 4
- id: ch04-4-2-1-encoding
  title: Encoding
  level: 4
- id: ch04-4-2-1-original-signal-recovery
  title: Original Signal Recovery
  level: 4
- id: ch04-4-2-1-pcm-bandwidth
  title: PCM Bandwidth
  level: 4
- id: ch04-4-2-1-maximum-data-rate-of-a-channel
  title: Maximum Data Rate of a Channel
  level: 4
- id: ch04-4-2-1-minimum-required-bandwidth
  title: Minimum Required Bandwidth
  level: 4
- id: ch04-4-2-2
  title: 4.2.2 Delta Modulation (DM)
  level: 3
- id: ch04-4-2-2-modulator
  title: Modulator
  level: 4
- id: ch04-4-2-2-demodulator
  title: Demodulator
  level: 4
- id: ch04-4-2-2-adaptive-dm
  title: Adaptive DM
  level: 4
- id: ch04-4-2-2-quantization-error
  title: Quantization Error
  level: 4
- id: ch04-4-3
  title: 4.3 TRANSMISSION MODES
  level: 2
- id: ch04-4-3-1
  title: 4.3.1 Parallel Transmission
  level: 3
- id: ch04-4-3-2
  title: 4.3.2 Serial Transmission
  level: 3
- id: ch04-4-3-2-asynchronous-transmission
  title: Asynchronous Transmission
  level: 4
- id: ch04-4-3-2-synchronous-transmission
  title: Synchronous Transmission
  level: 4
- id: ch04-4-3-2-isochronous
  title: Isochronous
  level: 4
- id: ch04-4-4
  title: 4.4 END-CHAPTER MATERIALS
  level: 2
- id: ch04-4-4-1
  title: 4.4.1 Recommended Reading
  level: 3
- id: ch04-4-4-1-books
  title: Books
  level: 4
- id: ch04-4-4-2
  title: 4.4.2 Key Terms
  level: 3
- id: ch04-4-4-3
  title: 4.4.3 Summary
  level: 3
review:
  source_pages: 95–134
  figures: 36
  questions: 32
  tables: 2
  formulas: source-glyph and rendered-layout checked
  source_order_checked: true
  reviewed_at: '2026-10-07T03:07:29+00:00'
  method: native PDF reconstruction, rendered figure review, question and equation
    comparison
---
# Chapter 4: Digital Transmission — Data Card
