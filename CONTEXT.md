# Agent-Ready Repo Kit Context

## Language

**Agent-Ready Repo**: A repository with enough durable context for a coding agent to work without repeated guessing.
_Avoid_: AI-optimized repo

**Agent Context**: Stable instructions, constraints, diagrams, domain terms, and decisions used by coding agents.
_Avoid_: prompt dump

**Skill**: A reusable workflow in a `SKILL.md` file.
_Avoid_: one-off prompt

**Know-How Gap**: The procedural judgment an expert uses that a generic agent tends to miss.
_Avoid_: missing context

**Grill**: A structured interrogation workflow that asks sharp questions, checks docs and code, and preserves durable answers.
_Avoid_: interview, brainstorm

**Static Text Hygiene**: The practice of keeping agent docs focused on durable constraints while removing volatile details.
_Avoid_: documentation cleanup

**Recon Report**: A source-grounded report that ties claims to evidence and treats coverage gaps as findings.
_Avoid_: summary

**MCP Boundary**: The line between local repo work and external tool access such as GitHub, Gmail, Calendar, browser automation, or Composio.
_Avoid_: integration

## Relationships

- A **Skill** can create or improve **Agent Context**.
- A **Grill** is a type of **Skill**.
- **Skill Authoring** should happen only when there is a real **Know-How Gap**.
- **Static Text Hygiene** determines what belongs in `AGENTS.md`.
- A **Recon Report** should cite sources and distinguish facts from inferences.
- An **MCP Boundary** should be documented before agents mutate external state.

## Flagged Ambiguities

- "Agentic system" is too broad for this project. Use **Agent-Ready Repo** when describing the practical value.
- "Security" should usually mean lightweight agent safety, secrets, auth, prompt injection, and MCP boundaries, not incident response.
