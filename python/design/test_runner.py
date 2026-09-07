"""Unified Test Runner for LeetCode Design Problems."""
import importlib.util
from pathlib import Path
import sys
import unittest

def create_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    design_dir = Path(__file__).parent
    py_files = sorted([f for f in design_dir.glob("*.py") if f.name[:4].isdigit()])

    for py_file in py_files:
        module_name = py_file.stem
        spec = importlib.util.spec_from_file_location(module_name, py_file)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            tests = unittest.defaultTestLoader.loadTestsFromModule(module)
            suite.addTests(tests)
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=1)
    suite = create_suite()
    result = runner.run(suite)
    num_files = len(list(Path(__file__).parent.glob("[0-9]*.py")))
    print("\n" + "=" * 60)
    print(f"TEST RUN SUMMARY: {result.testsRun} test cases run across {num_files} design problems.")
    if result.wasSuccessful():
        print("ALL TESTS PASSED SUCCESSFULLY! Ready for interview practice.")
        sys.exit(0)
    else:
        print(f"TESTS FAILED: {len(result.failures)} failures, {len(result.errors)} errors.")
        sys.exit(1)
