## Motivation and Use Cases

- IDE-agnostic architecture allows teams to use different IDE/Plugins while sharing same instruction base.
- Team alignment on LLM model choice is more critical than IDE choice - IDE switching is less disruptive.
- Instructions are pure markdown docs describing SDLC workflows without platform-specific adaptors like `alwaysApply: true` or `mode: agent`.
- Following Single Responsibility Principle (SRP) - one SDLC workflow piece per instruction file.
  + Recommended soft limit: ~700 lines per file. Exceeding this is a signal to split.
  + Complex instructions can reference other instructions — composability over monoliths.
  + Terminology hint: large multi-step workflows → "agents", small focused actions → "instructions". Naming may vary by author.
- `main.agent.md` serves as catalog of all instructions with brief descriptions - when asked about (what to do), follow this instruction (with file path).
  + Each entry has optional sub-fields after `+`: **Keywords** (trigger words), **Target** (file glob pattern), **Exceptions** (edge cases).
  + When adding new instruction to catalog, fill in at least Keywords to help model match user requests to instructions.
- Platform-specific entry points (`.github/copilot-instructions.md` for Copilot, `.cursor/rules/*.mdc` for Cursor, `.claude/CLAUDE.md` for Claude Code) reference `main.agent.md` to load with every prompt.
- Optionally, `AGENTS.md` in project root with same content as entry point — universal fallback recognized by Claude, Copilot, Cursor agents.
  + Important when `.github/`, `.cursor/`, or `.claude/` are not committed — without them other non-IDE agents have no entry point to discover `instructions/` folder.
  + Decision is up to the team.
- `instructions/` can live in the project repo or be extracted into a separate sub-repository (git submodule, etc.).
  + `.github/`, `.cursor/` stay local per team member's IDE choice — not committed.
  + For cloud agents — add `AGENTS.md` in project root as described above.
  + Or commit instructions together with the project — simpler, fewer moving parts.
  + Each team decides what fits their workflow.
- Why tool-agnostic over native systems (GitHub `.instructions.md`, Cursor `.mdc`):
  + Native formats are incompatible: Copilot's `applyTo` globs, `excludeAgent` fields, Cursor's `alwaysApply`, `globs`, `description` frontmatter, Claude Code's `paths:` frontmatter in `.claude/rules/*.md` — none of these cross-compatible.
  + Instruction goals differ from IDE adapter mechanics. Instructions define **what to do** (workflows, standards). IDE adapters define **when to apply** (file patterns, contexts).
  + Markdown is universal, readable by all models and developers. No proprietary parser dependencies.
  + Team can switch IDEs without rewriting instructions — just adjust entry points.
  + Reduces vendor lock-in risk.
- Reference implementation: https://github.com/codenjoyme/vibecoding-training/tree/main/instructions

## Configuration Instructions

For **CodeMie Plugin** in VSCode:

### 1. Entry Point Setup
Create `AGENTS.md` in project root:
```markdown
# Project Instructions

This project uses a structured instruction system for AI agents.

**All instructions are cataloged in:** `instructions/main.agent.md`

Please refer to that file for the complete list of available instructions.
```

### 2. Instructions Catalog
Create/update `instructions/main.agent.md` with this format:

```markdown
# Agent Instructions Catalog

## Available Instructions

### 1. [instructions/your-instruction.agent.md](your-instruction.agent.md)
**Purpose:** Brief description of what this instruction does  
**Output:** Expected output format and structure  
+ **Keywords:** trigger, words, phrases, that, match, user, intent
+ **Target:** file-pattern-*.js (optional - file glob patterns this applies to)
+ **Exceptions:** Edge cases or when NOT to use this instruction
```

### 3. Individual Instructions
Each instruction file should include:
- **Purpose** - What problem does this solve?
- **Format** - Output format specifications
- **Required Sections** - Structure of output
- **Style Guidelines** - Tone, language, constraints
- **Examples** - Templates or sample outputs
- **Notes** - Additional context or edge cases

### 4. Naming Convention
- Use pattern: `[task-name].agent.md`
- Examples: `create-status-report.agent.md`, `code-review.agent.md`
- Keep names descriptive and kebab-case

### 5. Best Practices
- **One workflow per file** - Follow SRP
- **Keep under 700 lines** - Split if larger
- **Include examples** - Show expected output
- **Define constraints** - Length, format, style rules
- **Update catalog** - Always add to main.agent.md with keywords

### 6. Project-Specific Setup
For this project (Turbo-Flux):
- Entry point: `AGENTS.md` in root
- Catalog: `instructions/main.agent.md`
- Instructions: `instructions/*.agent.md`
- No `.github/` or `.cursor/` needed for CodeMie

## Reference
Based on: https://github.com/codenjoyme/vibecoding-training/blob/main/instructions/creating-instructions.agent.md
