# Discord Python Hackpack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites

- Python 3.14 or higher
- Install `uv`: https://docs.astral.sh/uv/getting-started/installation/

```bash
# Linux / macOS / WSL
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Environment Variables

Copy the example environment file and add your Discord Bot Token:

```bash
cp .env.example .env
```

Set your token inside `.env`:
```env
DISCORD_BOT_TOKEN=your_token_here
```

## Commands

### Dependencies

```bash
# Install / sync dependencies
uv sync --locked

# Add a dependency
uv add <package>

# Add a development dependency
uv add --dev <package>

# Remove a dependency
uv remove <package>
```

### Running the Bot Locally

```bash
uv run bot
```

### Formatting

```bash
# Check formatting
uv run ruff format --check .

# Format in-place
uv run ruff format .
```

### Linting

```bash
# Check lint errors
uv run ruff check .

# Automatically fix fixable lint errors
uv run ruff check --fix .
```

### Build

```bash
uv build
```
