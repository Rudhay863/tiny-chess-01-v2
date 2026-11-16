# tiny-chess-01-v2

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Rudhay863/tiny-chess-01-v2/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Rudhay863/tiny-chess-01-v2/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A fresh, fast tiny chess engine for the [make.fun](https://make.fun) bounty `tiny-chess-01` ($500). Written from scratch in Python 3.13 stdlib only — readable source is `src/bot.py`, and `main.py` is its packed entrypoint (`makefun compress`, 3,131 bytes, under the 4,096-byte limit).

- 0x88 board, negamax alpha-beta with iterative deepening, quiescence (captures + check evasions), transposition table, MVV-LVA + killer/history move ordering, material + piece-square evaluation, and game-history threefold-repetition handling (a move that would repeat a position a third time scores as a draw).
- Fixed 100,000-node budget per move (no wall clock anywhere) — deterministic and replay-safe, so it cannot time out the way the first submission did.
- Speaks the harness env protocol over HTTP (`MAKEFUN_ENV_URL`).

## Local trial results (kit level 18, practice trials, measured 2026-11-17)

- Trial 0 (the practice grade): **Elo 1,364** — 3 wins, 1 draw, 2 losses (W vs depth-2, W vs depth-3, W vs depth-4, D vs nodes-100k, L vs nodes-250k, L vs nodes-500k). Practice floor is 1,154 — clears it by 210.
- Trials 0–2 combined: 9.5/18 points, ≈ Elo 1,300 (trial 1: 1,279; trial 2: 1,279).
- Perft verified (startpos, Kiwipete and 4 tricky positions, depths 1–3) — all correct, including en passant, castling and promotions.

## Play

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

## Referral

Built for the make.fun bounty — if you join, use this link: https://make.fun/r/xk7vph3j

## License

MIT — see `LICENSE`.
