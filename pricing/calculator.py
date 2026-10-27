#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(description="Draft price arithmetic only; not a quote")
p.add_argument("--monthly",type=float,default=5.0); p.add_argument("--option",choices=["monthly","annual"],required=True); p.add_argument("--months",type=int,default=12)
a=p.parse_args(); print(f"Draft assumption: ${a.monthly:.2f}/month, option={a.option}, {a.months} months = ${a.monthly*a.months:.2f}. Not a quote.")
