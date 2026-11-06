import os
from pathlib import Path
import random
import runpy
import string
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'generador.py'

class GeneratorTests(unittest.TestCase):
    def run_cli(self, answers, directory):
        return subprocess.run([sys.executable, str(SCRIPT)], input=answers, text=True,
                              capture_output=True, cwd=directory)

    def test_does_not_write_passwords_or_modify_existing_history(self):
        with tempfile.TemporaryDirectory() as directory:
            history = Path(directory, 'contrasenas.txt')
            history.write_text('existing history\n')
            result = self.run_cli('16\ns\ns\n', directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(history.read_text(), 'existing history\n')
            self.assertEqual(len(list(Path(directory).iterdir())), 1)

    def test_invalid_length_is_reprompted_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli('oops\n16\nn\nn\n', directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('Tu contraseña:', result.stdout)

    def test_uses_system_random_and_includes_requested_categories(self):
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                with patch('builtins.input', side_effect=['16', 's', 's']), \
                     patch.object(random, 'choice', side_effect=AssertionError('insecure RNG')), \
                     patch('builtins.print') as output:
                    runpy.run_path(str(SCRIPT), run_name='__main__')
                password = next(str(c.args[0]).split('Tu contraseña: ')[1]
                                for c in output.call_args_list if 'Tu contraseña: ' in str(c.args[0]))
                self.assertEqual(len(password), 16)
                for group in (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation):
                    self.assertTrue(any(c in group for c in password))
            finally:
                os.chdir(previous)

if __name__ == '__main__':
    unittest.main()
