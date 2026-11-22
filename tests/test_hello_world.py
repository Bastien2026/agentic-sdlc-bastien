"""Smoke test for the hello world script."""

import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "hello_world.py"


def load_script():
    spec = importlib.util.spec_from_file_location("hello_world", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HelloWorldTest(unittest.TestCase):
    def test_script_prints_greeting(self) -> None:
        module = load_script()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            module.main()
        self.assertEqual(buffer.getvalue().strip(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
