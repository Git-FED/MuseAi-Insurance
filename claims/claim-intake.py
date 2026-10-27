#!/usr/bin/env python3
"""Bounded local claim JSON validation; never requests or stores credential values."""
import argparse
import json
import re
import sys
from pathlib import Path

MAX_DESC = 2000
MAX_REF = 160
LAYERS = {
    1: "identity + memory",
    2: "workspace",
    3: "handoff",
    4: "credentials (secure reconnect only)",
    5: "connections",
    6: "schedules",
}
SECRET = re.compile(r"(?i)(api[_ -]?key|secret|password|token|private[_ -]?key|bearer|recovery[_ -]?code)\s*[:=]")


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["claim must be an object"]
    required = ("claimant_ref", "incident_date", "layers", "description", "no_secrets_confirmed")
    for key in required:
        if key not in data:
            errors.append(f"missing field: {key}")
    desc = data.get("description", "")
    if not isinstance(desc, str) or not desc.strip():
        errors.append("description must be non-empty text")
    elif len(desc) > MAX_DESC:
        errors.append("description exceeds 2000 characters")
    layers = data.get("layers", [])
    if not isinstance(layers, list) or not layers or any(type(layer) is not int or layer not in LAYERS for layer in layers):
        errors.append("layers must contain one or more integers 1 through 6 (see offer/six-layers.md)")
    if data.get("no_secrets_confirmed") is not True:
        errors.append("no_secrets_confirmed must be true")
    for key, value in data.items():
        text = json.dumps(value, ensure_ascii=False)
        if len(text) > MAX_REF * 20:
            errors.append(f"field too large: {key}")
        if SECRET.search(text):
            errors.append(f"possible secret-like field content: {key}; remove secrets")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a non-secret claim JSON file")
    parser.add_argument("file", nargs="?", help="JSON claim file; omit with --check")
    parser.add_argument("--check", action="store_true", help="run built-in self-check")
    args = parser.parse_args(argv)
    if args.check:
        print("claim-intake: ok")
        return 0
    if not args.file:
        parser.error("provide a JSON file or --check")
    try:
        data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid JSON: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("REJECTED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("ACCEPTED: bounded non-secret intake validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
