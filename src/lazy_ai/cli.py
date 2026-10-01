"""CLI for lazy-ai."""

import click
from pathlib import Path

from lazy_ai.prompts import get_system_prompt, get_review_prompt, get_precommit_prompt
from lazy_ai.config import (
    load_config,
    save_config,
    install_claude_code_config,
    install_cursor_config,
    get_config_path,
)


@click.group()
@click.version_option(version="0.1.0")
def main():
    """lazy-ai: Make your AI agent think like the laziest senior dev.

    The best code is the code you never write.
    """
    pass


@main.command()
def system():
    """Print the lazy system prompt."""
    click.echo(get_system_prompt())


@main.command()
def review():
    """Print the code review prompt."""
    click.echo(get_review_prompt())


@main.command()
def precommit():
    """Print the pre-commit reminder."""
    click.echo(get_precommit_prompt())


@main.command()
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def export(output):
    """Export all prompts to a file."""
    content = f"""# Lazy AI Prompts

## System Prompt

{get_system_prompt()}

---

## Review Prompt

{get_review_prompt()}

---

## Pre-commit Prompt

{get_precommit_prompt()}
"""

    if output:
        Path(output).write_text(content)
        click.echo(f"Prompts exported to {output}")
    else:
        click.echo(content)


@main.command()
def install():
    """Install lazy-ai configuration to AI agents."""
    click.echo("Installing lazy-ai configurations...")

    # Claude Code
    if install_claude_code_config():
        click.echo("✓ Claude Code configured")
    else:
        click.echo("✗ Claude Code configuration failed (not found or no write permission)")

    # Cursor
    if install_cursor_config():
        click.echo("✓ Cursor configured")
    else:
        click.echo("✗ Cursor configuration failed (not found or no write permission)")


@main.command()
def config_show():
    """Show current configuration."""
    config = load_config()
    import json
    click.echo(json.dumps(config, indent=2))


@main.command()
@click.argument("key")
@click.argument("value")
def config_set(key, value):
    """Set a configuration value."""
    config = load_config()
    keys = key.split(".")

    # Navigate to the right nested dict
    current = config
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]

    # Set the value
    current[keys[-1]] = value
    save_config(config)
    click.echo(f"Set {key} = {value}")


if __name__ == "__main__":
    main()
