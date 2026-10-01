"""Configuration management for lazy-ai."""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional


DEFAULT_CONFIG = {
    "lazy_prompts": {
        "system": "default",
        "review": "default",
    },
    "rules": {
        "max_lines_per_file": 200,
        "allow_new_files": True,
        "require_deletion_justification": False,
    },
    "integrations": {
        "claude_code": False,
        "cursor": False,
    }
}


def get_config_path() -> Path:
    """Get the config file path."""
    config_dir = Path.home() / ".config" / "lazy-ai"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "config.json"


def load_config() -> Dict[str, Any]:
    """Load configuration from file."""
    config_path = get_config_path()
    if config_path.exists():
        with open(config_path, "r") as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()


def save_config(config: Dict[str, Any]) -> None:
    """Save configuration to file."""
    config_path = get_config_path()
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)


def get_agent_config_dir() -> Path:
    """Get the directory for agent configurations."""
    if os.name == "nt":  # Windows
        config_home = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:  # Unix-like
        config_home = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))

    return config_home


def install_claude_code_config() -> bool:
    """Install lazy-ai config for Claude Code."""
    try:
        agent_dir = get_agent_config_dir() / "claude-code"
        agent_dir.mkdir(parents=True, exist_ok=True)

        settings_file = agent_dir / "settings.json"
        settings = {}
        if settings_file.exists():
            with open(settings_file, "r") as f:
                settings = json.load(f)

        # Add our system prompt
        settings["systemPrompt"] = """You are a lazy senior developer. You follow these principles:

1. **Delete first, write second**: Before adding code, check if you can delete something instead.
2. **Copy-paste is fine**: If code exists elsewhere, reference it rather than rewriting.
3. **No premature abstraction**: Don't create utilities for code that might only be used once.
4. **0 lines > 10 lines**: The best code is code that doesn't exist.
5. **Ask before writing**: When asked to add a feature, first ask "can this be simpler?"

Your task is not to write code. Your task is to solve the problem with minimum code."""

        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=2)
        return True
    except Exception:
        return False


def install_cursor_config() -> bool:
    """Install lazy-ai config for Cursor."""
    try:
        agent_dir = get_agent_config_dir() / "cursor"
        agent_dir.mkdir(parents=True, exist_ok=True)

        settings_file = agent_dir / "settings.json"
        settings = {}
        if settings_file.exists():
            with open(settings_file, "r") as f:
                settings = json.load(f)

        # Add our rules to existing rules
        if "rules" not in settings:
            settings["rules"] = []

        lazy_rules = [
            "Before adding code: can I delete something instead?",
            "Before creating utility: is it used only once?",
            "Copy-paste > abstraction for one-off code",
            "0 lines added > any number of lines added",
        ]

        for rule in lazy_rules:
            if rule not in settings["rules"]:
                settings["rules"].append(rule)

        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=2)
        return True
    except Exception:
        return False
