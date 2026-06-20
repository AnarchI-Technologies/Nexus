# Nexus Legacy Design Kits

Earlier integration experiments for AnarchI Technologies.

Hardcoding freedom into the systems of tomorrow.

## Status

This repository is legacy research. The canonical integration path is now:

https://github.com/AnarchI-Technologies/Nexusv2

## Purpose

Nexus contains earlier design-kit iterations for event routing, worker coordination, replay, transport, plugin execution, metrics, and control-plane concepts. These folders are preserved as public research history while the strongest ideas are consolidated into `Nexusv2`.

## Structure

```text
.
├── Nexus_DEK/      # First design kit
├── Nexus_DEK_v2/   # Event bus and worker cluster iteration
├── Nexus_DEK_v3/   # Distributed router and shared-state iteration
└── Nexus_DEK_v4/   # Metrics, trace, and control-plane iteration
```

## How To Read This Repo

- Treat these folders as prototypes and references.
- Do not build new production work here.
- Move useful concepts into `Nexusv2` with tests before relying on them.
- Keep private runtime state, credentials, and unreleased decision chains out of public commits.

## Consolidation Rule

`Nexus` records the exploration. `Nexusv2` carries the production direction.
