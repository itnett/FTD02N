python
    level = LEVELS[THRESHOLDS.index(next(t for t in THRESHOLDS if rank * 100 <= t))]
    return f"\nlevel: {level}\npercentile: {100-rank*100}\n"