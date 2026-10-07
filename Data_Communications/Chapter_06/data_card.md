---
doc_type: chapter_data_card
chapter_id: data_communications_ch06
course_id: data_communications
chapter: 6
title: 'Bandwidth Utilization: Multiplexing and Spectrum Spreading'
part: PART II Physical Layer
layer: physical
order: 6
previous_chapters:
- data_communications_ch05
next_chapters:
- data_communications_ch07
prerequisites: []
builds_on: []
enables: []
topics:
- id: ch06-0
  title: Chapter Objectives
  covers: Chapter Objectives
- id: ch06-6-1
  title: 6.1 MULTIPLEXING
  covers: MULTIPLEXING
- id: ch06-6-1-1
  title: 6.1.1 Frequency-Division Multiplexing
  covers: Frequency-Division Multiplexing
- id: ch06-6-1-2
  title: 6.1.2 Wavelength-Division Multiplexing
  covers: Wavelength-Division Multiplexing
- id: ch06-6-1-3
  title: 6.1.3 Time-Division Multiplexing
  covers: Time-Division Multiplexing
- id: ch06-6-2
  title: 6.2 SPREAD SPECTRUM
  covers: SPREAD SPECTRUM
- id: ch06-6-2-1
  title: 6.2.1 Frequency Hopping Spread Spectrum
  covers: Frequency Hopping Spread Spectrum
- id: ch06-6-2-2
  title: 6.2.2 Direct Sequence Spread Spectrum
  covers: Direct Sequence Spread Spectrum
- id: ch06-6-3
  title: 6.3 END-CHAPTER MATERIALS
  covers: END-CHAPTER MATERIALS
- id: ch06-6-3-1
  title: 6.3.1 Recommended Reading
  covers: Recommended Reading
- id: ch06-6-3-2
  title: 6.3.2 Key Terms
  covers: Key Terms
- id: ch06-6-3-3
  title: 6.3.3 Summary
  covers: Summary
key_terms:
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
standards_and_protocols: []
formulas_present: true
content_stats:
  sections: 12
  words: 13310
  approx_tokens: 17303
  markdown_tables: 2
asset_stats:
  illustration: 35
  table_image: 0
  equation: 0
  graph: 0
  picture: 0
  code_image: 0
  text_image: 0
question_stats:
  total: 30
  by_group:
    Questions: 12
    Problems: 18
syllabus_applied: false
syllabus_notes: No section-level exclusions applied.
source_files:
- Slide/ch_6/ch6.pdf
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
generated_at: '2026-10-07T06:16:26+03:00'
status: complete
tables_present:
- id: Table 6.1
  title: DS and T line rates
  location: content
  source_page: 171
  rows: 4
- id: Table 6.2
  title: E line rates
  location: content
  source_page: 173
  rows: 4
source_priority: The chapter PDF is authoritative; available slides are supportive
  material.
source_authority:
  primary: book PDF
  supplementary: slides
  book_sha256: 445f706699b1142d5552b7d074277f767b6b77265e31f8d4eba09c106c38b087
retrieval_sections:
- id: ch06-0
  title: Chapter Objectives
  level: 2
- id: ch06-6-1
  title: 6.1 MULTIPLEXING
  level: 2
- id: ch06-6-1-1
  title: 6.1.1 Frequency-Division Multiplexing
  level: 3
- id: ch06-6-1-1-multiplexing-process
  title: Multiplexing Process
  level: 4
- id: ch06-6-1-1-demultiplexing-process
  title: Demultiplexing Process
  level: 4
- id: ch06-example-6-1
  title: Example 6.1
  level: 5
- id: ch06-example-6-2
  title: Example 6.2
  level: 5
- id: ch06-example-6-3
  title: Example 6.3
  level: 5
- id: ch06-6-1-1-the-analog-carrier-system
  title: The Analog Carrier System
  level: 4
- id: ch06-6-1-1-other-applications-of-fdm
  title: Other Applications of FDM
  level: 4
- id: ch06-example-6-4
  title: Example 6.4
  level: 5
- id: ch06-6-1-1-implementation
  title: Implementation
  level: 4
- id: ch06-6-1-2
  title: 6.1.2 Wavelength-Division Multiplexing
  level: 3
- id: ch06-6-1-3
  title: 6.1.3 Time-Division Multiplexing
  level: 3
- id: ch06-6-1-3-synchronous-tdm
  title: Synchronous TDM
  level: 4
- id: ch06-6-1-3-time-slots-and-frames
  title: Time Slots and Frames
  level: 4
- id: ch06-example-6-5
  title: Example 6.5
  level: 5
- id: ch06-example-6-6
  title: Example 6.6
  level: 5
- id: ch06-example-6-7
  title: Example 6.7
  level: 5
- id: ch06-6-1-3-interleaving
  title: Interleaving
  level: 4
- id: ch06-example-6-8
  title: Example 6.8
  level: 5
- id: ch06-example-6-9
  title: Example 6.9
  level: 5
- id: ch06-6-1-3-empty-slots
  title: Empty Slots
  level: 4
- id: ch06-6-1-3-data-rate-management
  title: Data Rate Management
  level: 4
- id: ch06-6-1-3-multilevel-multiplexing
  title: Multilevel Multiplexing
  level: 4
- id: ch06-6-1-3-multiple-slot-allocation
  title: Multiple-Slot Allocation
  level: 4
- id: ch06-6-1-3-pulse-stuffing
  title: Pulse Stuffing
  level: 4
- id: ch06-6-1-3-frame-synchronizing
  title: Frame Synchronizing
  level: 4
- id: ch06-example-6-10
  title: Example 6.10
  level: 5
- id: ch06-example-6-11
  title: Example 6.11
  level: 5
- id: ch06-6-1-3-digital-signal-service
  title: Digital Signal Service
  level: 4
- id: ch06-6-1-3-t-lines
  title: T Lines
  level: 4
- id: ch06-6-1-3-t-lines-for-analog-transmission
  title: T Lines for Analog Transmission
  level: 4
- id: ch06-6-1-3-the-t-1-frame
  title: The T-1 Frame
  level: 4
- id: ch06-6-1-3-e-lines
  title: E Lines
  level: 4
- id: ch06-6-1-3-more-synchronous-tdm-applications
  title: More Synchronous TDM Applications
  level: 4
- id: ch06-6-1-3-statistical-time-division-multiplexing
  title: Statistical Time-Division Multiplexing
  level: 4
- id: ch06-6-1-3-addressing
  title: Addressing
  level: 4
- id: ch06-6-1-3-slot-size
  title: Slot Size
  level: 4
- id: ch06-6-1-3-no-synchronization-bit
  title: No Synchronization Bit
  level: 4
- id: ch06-6-1-3-bandwidth
  title: Bandwidth
  level: 4
- id: ch06-6-2
  title: 6.2 SPREAD SPECTRUM
  level: 2
- id: ch06-6-2-1
  title: 6.2.1 Frequency Hopping Spread Spectrum
  level: 3
- id: ch06-6-2-1-bandwidth-sharing
  title: Bandwidth Sharing
  level: 4
- id: ch06-6-2-2
  title: 6.2.2 Direct Sequence Spread Spectrum
  level: 3
- id: ch06-6-2-2-bandwidth-sharing
  title: Bandwidth Sharing
  level: 4
- id: ch06-6-3
  title: 6.3 END-CHAPTER MATERIALS
  level: 2
- id: ch06-6-3-1
  title: 6.3.1 Recommended Reading
  level: 3
- id: ch06-6-3-1-books
  title: Books
  level: 4
- id: ch06-6-3-2
  title: 6.3.2 Key Terms
  level: 3
- id: ch06-6-3-3
  title: 6.3.3 Summary
  level: 3
review:
  source_pages: 155–184
  figures: 35
  questions: 30
  tables: 2
  formulas: rendered equations, rates, units, and worked-example arithmetic checked
  source_order_checked: true
  reviewed_at: '2026-10-07T03:18:09+00:00'
  method: native PDF reconstruction, annotation-free figure rendering, rendered page
    review, and question/table comparison
editorial_corrections:
- location: Example 6.11
  source_issue: The book labels 1/100,000 s as 10 ms.
  correction: Uses 10 μs.
- location: DS-3 prose and Figure 6.23
  source_issue: The book prints 44.376 Mbps and 1.368 Mbps overhead, conflicting with
    Table 6.1.
  correction: Uses Table 6.1's 44.736 Mbps and the resulting 1.728 Mbps overhead;
    asset metadata retains the printed-figure note.
---
# Chapter 6: Bandwidth Utilization: Multiplexing and Spectrum Spreading — Data Card
