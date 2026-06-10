# Agentic Skills

A collection of reusable [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills) for common workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [quiz](./quiz/) | Interactive quizzes to test understanding of any topic or source material |

## Installation

To install a skill, copy its folder into your Claude Code skills directory:

```bash
# Global (available across all projects)
cp -r quiz/ ~/.claude/skills/quiz/

# Project-specific
cp -r quiz/ .claude/skills/quiz/
```

Then restart Claude Code. The skill will appear in your available skills list.

## Usage

Each skill folder contains a `SKILL.md` that defines when and how the skill triggers. Once installed, just use natural language — Claude will invoke the skill automatically when your request matches.

For example, with the quiz skill installed:
- "Quiz me on Python decorators"
- "Test my understanding of this paper"
- "I have an exam on Thursday, help me study git branching"

## Contributing

To add a new skill:

1. Create a new directory with the skill name
2. Add a `SKILL.md` with YAML frontmatter (`name` and `description`) and markdown instructions
3. Open a pull request

## License

MIT
