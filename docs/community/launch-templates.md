# Community Launch & Listing Templates

This document provides ready-to-use launch templates, submission blurbs, and ecosystem PR entries to promote ResultSeal across developer communities.

---

## 1. Hacker News (Show HN)

**Title:**
> Show HN: ResultSeal – Fail-closed observation contracts for AI-agent tool results

**URL / Text:**
> https://github.com/sx4im/resultseal

**First Comment / Intro:**
> Hey HN,
>
> We built ResultSeal because AI agents regularly hallucinate success on tool failures:
> - A database query returns `[]`, and the agent reports *"Customer has zero transactions"* instead of *"No records found"*.
> - An HTTP `DELETE` returns 204 No Content, and the agent confirms deletion without verification.
> - An MCP server returns `isError: true` with text, and the agent interprets the error message as the factual answer.
>
> ResultSeal is a lightweight, framework-neutral Python toolkit that puts an observation-integrity gate between tool outputs and model context:
>
> 1. **Fail-Closed by Default:** Unknown, partial, or unverified evidence cannot be promoted to a factual claim.
> 2. **Deterministic Fingerprints:** Canonical hashing ensures evaluations and verdicts are 100% reproducible.
> 3. **Minimal Footprint:** No network calls, no subprocesses, and no heavy runtime dependencies in the core package. Works with LangChain, Pydantic-AI, CrewAI, MCP, or plain Python.
>
> Live interactive playground: https://sx4im.github.io/resultseal/
> Repo: https://github.com/sx4im/resultseal
>
> Would love your feedback on how you handle observation verification in production agent pipelines!

---

## 2. Reddit (`r/LocalLLaMA`, `r/Python`, `r/MachineLearning`)

**Title:**
> HTTP 200 is not an observation: ResultSeal enforces tool observation integrity for AI agents

**Body:**
> If you have built AI agents with tool-calling (LangChain, Pydantic-AI, AutoGen, CrewAI, or MCP), you've likely seen this failure mode:
>
> An agent calls a search tool. The tool returns an empty list `[]`. The agent confidently concludes that the item does not exist or fabricates missing fields. Standard Pydantic schema validation passes because `[]` is valid JSON, but the semantic claim is unverified.
>
> We open-sourced **ResultSeal**: https://github.com/sx4im/resultseal
>
> **What it does:**
> It normalizes tool responses (JSON, HTTP, MCP, stdio), checks them against declarative contracts (required fields, sentinels, freshness, target identity), and produces deterministic `SEALED` or `BLOCKED` decisions with stable reason codes (e.g. `EMPTY_WITHOUT_NOT_FOUND_SENTINEL`, `UNVERIFIED_EFFECT`).
>
> - **Install:** `pip install resultseal` (Python 3.11+)
> - **Playground:** https://sx4im.github.io/resultseal/
> - **Open Issues for Contributors:** https://github.com/sx4im/resultseal/issues
>
> Feedback, edge-case fixtures, and PRs welcome!

---

## 3. Pull Request for Awesome MCP (Model Context Protocol)

**Target Repository:** `punkpeye/awesome-mcp-servers` or `appcypher/awesome-mcp-servers`  
**Section:** *Frameworks & Developer Tools* / *Testing & Security*

**Markdown Entry:**
```markdown
- [ResultSeal](https://github.com/sx4im/resultseal) - Deterministic observation-integrity contracts for MCP tool results. Prevents empty, partial, or error-carrying MCP responses from being promoted into factual agent claims.
```

---

## 4. Pull Request for Awesome AI Agents

**Target Repository:** `e2b-dev/awesome-ai-agents` or `Significant-Gravitas/Awesome-AI-Agents`  
**Section:** *Guardrails & Reliability*

**Markdown Entry:**
```markdown
- [ResultSeal](https://github.com/sx4im/resultseal) - Lightweight, deterministic observation-integrity gate that fails-closed on empty, unverified, or source-mismatched tool results in agent loops.
```
