# Contributing to Security Agent Cookbook

Thanks for your interest in contributing recipes!

## Adding a New Recipe

1. Fork this repository
2. Create a new directory: `recipes/XX-your-recipe-name/`
3. Include these files:
   - `agent.py` — Main agent implementation
   - `README.md` — Documentation with usage and example output
   - `requirements.txt` — Recipe-specific dependencies
   - `example_output/` — Sample output files
4. Submit a pull request

## Recipe Guidelines

- **Self-contained** — Each recipe should work independently
- **Well-documented** — Code should have comments explaining the logic
- **Provider agnostic** — Use the shared LLM abstraction when possible
- **Responsible** — Include scope checking and authorization reminders
- **Tested** — Include example output showing the recipe works

## Code Style

- Python 3.10+ with type hints
- Format with `ruff format`
- Lint with `ruff check`
- Use async/await for I/O operations
