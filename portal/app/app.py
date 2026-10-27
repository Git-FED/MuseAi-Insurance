#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse, html, json, os
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import importlib.util
_validator_path = Path(__file__).resolve().parents[2] / 'claims' / 'claim-intake.py'
_spec = importlib.util.spec_from_file_location('claim_intake', _validator_path)
_validator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_validator)
validate = _validator.validate
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body="""<!doctype html><title>Draft claim intake</title><h1>Draft claim intake</h1><p>Loopback-only demo. Do not submit secrets or sensitive personal data. No claim is filed.</p><p>Use the CLI validator for JSON.</p>"""
        self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.end_headers(); self.wfile.write(body.encode())
    def log_message(self,*args): pass
def main():
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); p.add_argument('--host',default=os.getenv('HOST','127.0.0.1')); p.add_argument('--port',type=int,default=int(os.getenv('PORT','8765'))); a=p.parse_args()
    if a.check: print('portal: ok (standard-library, no persistence)'); return 0
    if a.host not in ('127.0.0.1','localhost','::1'): raise SystemExit('Refusing non-loopback host in draft app')
    print(f'Listening on http://{a.host}:{a.port} (draft/local only)'); HTTPServer((a.host,a.port),Handler).serve_forever()
if __name__=='__main__': main()
