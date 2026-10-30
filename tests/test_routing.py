import unittest

from handlers.common import router


class RoutingTests(unittest.TestCase):
    def test_fallback_is_registered_after_commands(self):
        handlers = router.message.handlers
        self.assertGreaterEqual(len(handlers), 3)
        self.assertEqual(handlers[-1].callback.__name__, "fallback")
