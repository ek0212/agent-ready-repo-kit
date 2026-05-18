---
name: ai-app-prompt-injection-review
description: Reviews LLM apps for prompt injection, unsafe tool access, data leakage, and missing evaluation boundaries. Use for chatbots, agents, RAG apps, and MCP-enabled AI products.
---

# AI App Prompt Injection Review

## Use When

- A repo includes an LLM, chatbot, agent, RAG pipeline, or tool-calling flow.
- User input, documents, web pages, emails, or issues are passed to a model.
- The model can call tools or affect external state.

## Threat Model

Treat these as untrusted:

- user prompts
- uploaded files
- retrieved documents
- web pages
- emails
- issue comments
- model outputs from other agents

## Review Checklist

- Are system and developer instructions separated from retrieved content?
- Does the app label untrusted content in prompts?
- Can retrieved text instruct the model to ignore rules?
- Can the model call tools based only on untrusted content?
- Are tool calls allowlisted?
- Are write actions confirmed or constrained?
- Is private data included in prompts unnecessarily?
- Are model outputs validated before use?
- Are logs safe?

## Common Fixes

- Wrap retrieved content in explicit delimiters.
- Tell the model retrieved content is data, not instructions.
- Gate tool calls through allowlists and schemas.
- Require confirmation for external mutations.
- Validate structured outputs.
- Reduce prompt exposure of secrets and personal data.

## Output

Return:

- attack surfaces
- concrete vulnerabilities
- recommended fixes
- test prompts to reproduce risks

