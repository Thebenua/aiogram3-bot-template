import unittest
from unittest.mock import AsyncMock

from handlers.common import cmd_start, cmd_help, fallback


class HandlerTests(unittest.IsolatedAsyncioTestCase):
    async def test_start_replies(self):
        message = AsyncMock()
        await cmd_start(message)
        message.answer.assert_awaited_once()
        self.assertIn("Telegram", message.answer.await_args.args[0])

    async def test_help_mentions_available_commands(self):
        message = AsyncMock()
        await cmd_help(message)
        reply = message.answer.await_args.args[0]
        self.assertIn("/start", reply)
        self.assertIn("/help", reply)

    async def test_fallback_explains_available_commands(self):
        message = AsyncMock()
        await fallback(message)
        self.assertIn("/help", message.answer.await_args.args[0])
