import unittest
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
