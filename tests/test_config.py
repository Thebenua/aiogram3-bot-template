import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from config.config import Settings


class SettingsTests(unittest.TestCase):
    def test_token_is_required(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                Settings(_env_file=None)

    def test_infrastructure_urls_are_optional(self):
        with patch.dict("os.environ", {}, clear=True):
            settings = Settings(_env_file=None, BOT_TOKEN="example")
        self.assertIsNone(settings.DATABASE_URL)
        self.assertIsNone(settings.REDIS_URL)
        self.assertNotIn("example", repr(settings.BOT_TOKEN))

    def test_settings_read_token_from_env_file(self):
        with TemporaryDirectory() as directory:
            env_file = Path(directory) / ".env"
            env_file.write_text("BOT_TOKEN=example-token\n", encoding="utf-8")
            with patch.dict("os.environ", {}, clear=True):
                settings = Settings(_env_file=env_file)
        self.assertEqual(settings.BOT_TOKEN.get_secret_value(), "example-token")

    def test_environment_takes_priority_over_env_file(self):
        with TemporaryDirectory() as directory:
            env_file = Path(directory) / ".env"
            env_file.write_text("BOT_TOKEN=from-file\n", encoding="utf-8")
            with patch.dict("os.environ", {"BOT_TOKEN": "from-environment"}, clear=True):
                settings = Settings(_env_file=env_file)
        self.assertEqual(settings.BOT_TOKEN.get_secret_value(), "from-environment")
