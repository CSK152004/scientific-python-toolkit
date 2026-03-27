import argparse
from pathlib import Path
from .demo_decay import run_demo

def main():
    p = argparse.ArgumentParser(prog="satool")
    sub = p.add_subparsers(dest="cmd", required=True)

    demo = sub.add_parser("demo", help="Generate + fit + plot exponential decay demo")
    demo.add_argument("--outdir", type=str, default="out", help="Output directory")

    args = p.parse_args()

    if args.cmd == "demo":
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        run_demo(outdir)
