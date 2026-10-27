import unittest
from pathlib import Path
class PolicyFilesTests(unittest.TestCase):
 def test_required_policy_files_exist(self):
  root=Path(__file__).parents[1]
  for name in ['POLICY-TEMPLATE.md','coverage-schedule.md','exclusions.md','definitions.md','guarantee-clause.md','acceptance-template.md']:
   self.assertTrue((root/'policy'/name).is_file(),name)
 def test_draft_safety_language(self):
  text=(Path(__file__).parents[1]/'policy'/'POLICY-TEMPLATE.md').read_text().lower()
  self.assertIn('not legal advice',text); self.assertIn('draft',text)
if __name__=='__main__': unittest.main()
