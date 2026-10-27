import importlib.util, json, unittest
from pathlib import Path
p=Path(__file__).parents[1]/'claims'/'claim-intake.py'
spec=importlib.util.spec_from_file_location('claim_intake',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class ClaimTests(unittest.TestCase):
 def test_valid_claim(self):
  self.assertEqual(m.validate({'claimant_ref':'C-1','incident_date':'2026-01-01T00:00:00Z','layers':[1,5],'description':'runtime failed','no_secrets_confirmed':True}),[])
 def test_reject_secret(self):
  self.assertTrue(m.validate({'claimant_ref':'C-1','incident_date':'x','layers':[1],'description':'api_key: abc','no_secrets_confirmed':True}))
 def test_reject_unconfirmed(self):
  self.assertTrue(m.validate({'claimant_ref':'C-1','incident_date':'x','layers':[1],'description':'x','no_secrets_confirmed':False}))
if __name__=='__main__': unittest.main()
