PYTHON ?= python3
.PHONY: test check-intake check
test:
	$(PYTHON) -m unittest discover -s tests -v
check-intake:
	$(PYTHON) claims/claim-intake.py --help
check:
	$(MAKE) test
	$(MAKE) check-intake
	$(PYTHON) portal/app/app.py --check
