#!/usr/bin/env python3
"""采集 Hyperliquid 公共 metaAndAssetCtxs，写带时间戳的 jsonl。

只做三件事：拉、存、不加工。分析放别的层。
用法：
    python3 hyperliquid_meta.py --out data/hl_meta.jsonl --once
    python3 hyperliquid_meta.py --out data/hl_meta.jsonl --interval 300
"""
import argparse
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://api.hyperliquid.xyz/info"


def fetch():
    req = urllib.request.Request(
        URL,
        data=json.dumps({"type": "metaAndAssetCtxs"}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        uni, ctx = json.loads(r.read())
    rows = []
    ts = datetime.now(timezone.utc).isoformat()
    for meta, c in zip(uni["universe"], ctx):
        name = meta.get("name")
        if not name:
            continue
        rows.append({
            "id": f"hl-{name}-{ts}",
            "source": "hyperliquid.info.metaAndAssetCtxs",
            "captured_at": ts,
            "coin": name,
            "funding": c.get("funding"),
            "open_interest": c.get("openInterest"),
            "prev_day_px": c.get("prevDayPx"),
            "day_ntl_vlm": c.get("dayNtlVlm"),
            "mark_px": c.get("markPx"),
            "oracle_px": c.get("oraclePx"),
            "mid_px": c.get("midPx"),
            "day_base_vlm": c.get("dayBaseVlm"),
        })
    return rows


def append(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/hl_meta.jsonl")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--interval", type=int, default=300, help="秒")
    args = ap.parse_args()
    path = Path(args.out)
    while True:
        try:
            rows = fetch()
            append(path, rows)
            print(f"{datetime.now().isoformat()} wrote {len(rows)} rows -> {path}")
        except Exception as e:
            print("fetch error", e)
        if args.once:
            break
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
