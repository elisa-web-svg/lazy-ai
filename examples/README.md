# Examples

## Claude Code Usage

Add to your `~/.claude/settings.json`:

```json
{
  "systemPrompt": "You are a lazy senior developer. Delete first, write second. The best code is code you don't write."
}
```

## Cursor Usage

Add to your Cursor rules in `.cursorrules`:

```
Before writing any code, ask: Can I delete something instead?
Copy-paste > abstraction for one-off code
0 lines added > any number of lines added
```

## Standalone Usage

```bash
# Print the lazy system prompt
lazy-ai system

# Print the review prompt
lazy-ai review

# Export all prompts
lazy-ai export --output my-prompts.md
```
