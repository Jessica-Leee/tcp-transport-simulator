#!/usr/bin/env python3
"""Run the course autograder with this interpreter and a meaningful exit code."""

import os
from pathlib import Path
import shlex
import sys
import unittest


def main():
    repository_root = Path(__file__).resolve().parent
    course_directory = repository_root / "ext" / "cs168p2"
    os.chdir(course_directory)
    sys.path.insert(0, str(course_directory))
    import autograder

    # The supplied launcher otherwise searches PATH for a separate python3.
    # Keep every simulation on the interpreter chosen for this command.
    autograder.Pox.POX_PY = "{} {}".format(
        shlex.quote(sys.executable),
        shlex.quote(str(repository_root / "pox.py")),
    )

    class ReportingAutoGrader(autograder.AutoGrader):
        result = None

        def test(self, test_cases):
            suite = unittest.TestSuite()
            loader = unittest.TestLoader()
            for test_class in test_cases:
                suite.addTests(loader.loadTestsFromTestCase(test_class))
            self.result = unittest.TextTestRunner(verbosity=2).run(suite)

    grader = ReportingAutoGrader()
    grader.run(sys.argv[1:] or ["all"])
    return 0 if grader.result is not None and grader.result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())

