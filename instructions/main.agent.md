# Agent Instructions Catalog

## Overview
This directory contains instruction files for AI agents working on the Turbo-Flux Showcase Deck Automation project. Each instruction file defines specific SDLC workflows, formats, and guidelines following the Single Responsibility Principle.

## Available Instructions

### 1. [instructions/create-status-report.agent.md](create-status-report.agent.md)
**Purpose:** Generate weekly status reports for team updates  
**Output:** Markdown format, max 20 lines, 3 sections (accomplishments, blockers, next week)  
+ **Keywords:** status report, weekly update, team report, sprint summary, progress report
+ **Target:** N/A (report generation)
+ **Exceptions:** None

### 2. [instructions/creating-instructions.agent.md](creating-instructions.agent.md)
**Purpose:** Guidelines for creating new agent instruction files following IDE-agnostic architecture  
**Output:** Instruction file structure and best practices documentation  
+ **Keywords:** create instruction, new agent, instruction format, instruction guidelines, setup instructions
+ **Target:** instructions/*.agent.md
+ **Exceptions:** Don't use for modifying existing instructions, only for creating new ones

## How to Use These Instructions

1. **Select the appropriate instruction file** based on your task
2. **Read the full instruction** including format, style, and output specifications
3. **Follow the guidelines strictly** - especially format and length constraints
4. **Generate output** according to the template provided

## File Naming Convention
All agent instruction files follow the pattern: `[task-name].agent.md`

Examples:
- `create-status-report.agent.md`
- `generate-sprint-review.agent.md`
- `code-review-checklist.agent.md`

## Adding New Instructions

When creating new instruction files:
1. Follow the naming convention above
2. Include clear Purpose, Format, and Output sections
3. Provide examples or templates
4. Specify style guidelines and constraints
5. Update this main.agent.md index

## Best Practices

- **Be specific** - Define exact requirements, not general guidance
- **Include examples** - Show what good output looks like
- **Set constraints** - Length limits, format requirements, style rules
- **Make it actionable** - Instructions should be clear enough to follow without clarification

## Project Context
**Project:** Turbo-Flux Showcase Deck Automation  
**Team:** Turbo-Flux (Cox Automotive)  
**Product Manager:** Avinash Agarwal  
**Repository:** https://github.com/Avinasha1101/git-baby-steps-practice

---

*Last Updated: 2024*