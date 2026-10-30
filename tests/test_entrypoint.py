import subprocess
import sys
import unittest


class EntrypointTests(unittest.TestCase):
    def test_import_does_not_require_environment(self):
        result = subprocess.run(
            [sys.executable, "-c", "import os; os.environ.pop('BOT_TOKEN', None); import main"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
