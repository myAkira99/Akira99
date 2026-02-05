# Akira99 — Project Context

## Overview

Story-based prediction gambling on Solana DEX. LLM generates narratives, players bet on outcomes, Claude judges results, Solana settles.

## Architecture

```
Scenario Generation (Claude) 
    ↓
Betting Engine (Odds Management)
    ↓
Outcome Resolution (Claude Judge)
    ↓
Solana Settlement
    ↓
Narrative Cascade (Hooks)
```

## Core Modules

- **scenario_generator.py**: Claude generates story scenarios
- **betting_engine.py**: Odds calculation, pool management
- **outcome_resolver.py**: Claude judges which option won
- **models.py**: Pydantic data structures
- **solana_settlement.py**: On-chain settlement via Solana

## Testing

45+ tests covering scenario generation, betting logic, outcome resolution, settlement.

## Performance Targets

- Scenario generation: <1s (Claude API)
- Odds calculation: <50ms
- Settlement: <1s on-chain
