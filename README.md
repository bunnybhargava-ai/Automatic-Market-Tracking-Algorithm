# Automatic Market Tracker Algorithm

A modular, cross-platform quantitative data pipeline engineered to ingest, sanitize, and chronologically sequence multi-asset financial metrics (Nifty 50, India VIX, Bitcoin) into a high-fidelity time-series database. 

This infrastructure pairs automated data extraction with disciplined macroeconomic tracking, engineered entirely within a minimalist environment to enforce complete syntactic and structural code ownership.

---

## Architectural Philosophy & Proof of Work

To maintain strict data integrity and eliminate external skepticism regarding project authenticity or automated AI generation, this system operates on an intentional **Dual-Track Verification Workflow**:

1. **The Quantitative Automation Layer (This Codebase):** A Python-driven engineering pipeline that runs via system triggers to fetch, calculate, and commit unbiased mathematical market metrics.
2. **The Qualitative Analyst Journal (Air-Gapped/Manual):** A handwritten, daily-updated macroeconomic matrix maintained separately on an iPad (Apple Numbers). This companion log captures pre-market structural hypotheses, post-market analyses, and fundamental macro annotations (e.g., Central Bank rate adjustments, liquidity shifts, and geopolitical milestones).

By decoupling the human analytical layer from the mathematical processing framework, the project establishes verifiable proof of continuous operational discipline and authentic software authorship.

---

## System Component Breakdown

The software architecture strictly adheres to the **Single Responsibility Principle**. Rather than utilizing a monolithic script layout, the application is intentionally decoupled into independent functional layers:

* **`core_math.py`** — Handles high-speed, localized algorithmic operations. Computes geometric intraday asset variance and percentage changes using defensive $O(1)$ boundaries to block runtime `ZeroDivisionError` or `NaN` data pollution.
* **`sanitizer.py`** — An input-protection gateway using regular expressions to tokenize raw terminal strings, filter breaking character formatting, and isolate citation URLs from macro remarks.
* **`storage_indexer.py`** — A specialized document file scanner that maps spreadsheet index positions directly into system memory using `openpyxl`'s fast row iterators, scaling exponentially faster than traditional cell-by-cell coordinate loops.
* **`sequencer.py`** — An in-memory data organizer that builds dictionary mapping schemas, resolves timeline duplicate conflicts, and completely rewrites data records in absolute chronological order while automatically adjusting continuous Day counters.
* **`fetcher.py`** — The network ingestion layer designed to query market APIs via streamlined multi-ticker batch requests, keeping network overhead minimal and neutralizing rate-limiting blocks.
* **`main.py`** — The primary runtime orchestration engine mapping user command-line parameters to downstream data layers.

---

## print-Driven Lifecycle Roadmap

This project evolves systematically following industry-standard **bi-weekly development cycles**. Every 14 days, a new isolated tier of the system is built from scratch, unit-tested via local execution assertions, and committed to the repository tree. 

### Current Implementation Phase
- [x] **Sprint 1 (Weeks 1–2):** Core Schema Definitions, Global Constants, and `MarketSnapshot` Typing Models.
- [x] **Sprint 2 (Weeks 3–4):** regular expression String Sanitization Utilities, Domain Citation Extraction, and Safe Percentage Mathematics.
- [x] **Sprint 3 (Weeks 5–6):** Memory-Mapped Spreadsheet Row Scanning and High-Speed Value-Only Matrix Processing.
- [ ] **Sprint 4 (Weeks
