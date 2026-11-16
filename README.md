# tiny-chess-01-v2

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Rudhay863/tiny-chess-01-v2/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Rudhay863/tiny-chess-01-v2/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A fresh, fast tiny chess engine for the [make.fun](https://make.fun) bounty `tiny-chess-01` ($500). Written from scratch in a single `main.py` (4,096 bytes max, Python 3.13 stdlib only).

- 0x88 board, negamax alpha-beta with iterative deepening, quiescence (captures + check evasions), MVV-LVA + killer move ordering, material + piece-square evaluation.
- Fixed node budget per move (no wall clock anywhere) — deterministic and replay-safe, so it cannot time out the way the first submission did.
- Speaks the harness env protocol over HTTP (`MAKEFUN_ENV_URL`).

## Play

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

## Referral

Built for the make.fun bounty — if you join, use this link: https://make.fun/r/xk7vph3j

## License

MIT — see `LICENSE`.
