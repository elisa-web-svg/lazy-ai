# lazy-ai

> Make your AI agent think like the laziest senior dev — because the best code is the code you never write.

[![PyPI version](https://img.shields.io/pypi/v/lazy-ai.svg)](https://pypi.org/project/lazy-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Philosophy

Every line of code is a liability. Every feature you don't build is a feature you never have to maintain.

**lazy-ai** is a prompt framework and CLI tool that teaches AI coding agents to be genuinely lazy — to question whether code needs to be written at all, to prefer deletion over addition, and to solve problems with the minimum necessary code.

## Features

- **System Prompt**: Makes AI agents think like lazy senior devs
- **Review Prompt**: Score code changes on "laziness"
- **Pre-commit Prompt**: Reminder before writing any code
- **CLI Tool**: Export, install, and manage lazy prompts
- **Agent Integration**: One-command setup for Claude Code and Cursor

## Installation

```bash
pip install lazy-ai
```

Or install from source:

```bash
git clone https://github.com/elisa-web-svg/lazy-ai.git
cd lazy-ai
pip install -e .
```

## Quick Start

### CLI Usage

```bash
# Print the lazy system prompt
lazy-ai system

# Print the code review prompt
lazy-ai review

# Export all prompts to a file
lazy-ai export --output my-prompts.md

# Install to Claude Code / Cursor
lazy-ai install
```

### Claude Code Integration

```bash
lazy-ai install
```

This adds the lazy system prompt to your Claude Code settings.

### Manual Integration

**Claude Code** — Add to `settings.json`:
```json
{
  "systemPrompt": "You are a lazy senior developer. Delete first, write second. The best code is code you don't write. Before adding any code, ask: can I delete something instead?"
}
```

**Cursor** — Add to `.cursorrules`:
```
You are a lazy senior developer.
- Delete first, write second
- Copy-paste > abstraction for one-off code
- 0 lines added > any number of lines added
- Before adding code: can I delete something instead?
```

## Core Principles

1. **Delete first, write second** — Before adding code, check if you can delete something
2. **Copy-paste is fine** — Reference existing code rather than rewriting
3. **No premature abstraction** — Don't create utilities for code used only once
4. **0 lines > 10 lines** — The best code is code that doesn't exist
5. **Ask before writing** — When asked to add a feature, first ask "can this be simpler?"

## The Lazy Code Review Score

Review your PRs with the laziness lens:

| Score | Description |
|-------|-------------|
| 8-10 | Excellent laziness, significant deletion or minimal addition |
| 5-7 | Good effort, could still delete more |
| 3-5 | Too much code written, needs simplification |
| 0-3 | Anti-lazy, over-engineered |

## Examples

See [examples/](examples/) for integration examples with different AI coding agents.

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*"The best code is the code you never write."*
