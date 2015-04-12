import sys
import unittest

if sys.version_info[:2] >= (3, 0):
    from tests.py3 import run_tests
else:
    from tests.py2 import run_tests


test_runner = unittest.TextTestRunner()
test_runner.run(run_tests())