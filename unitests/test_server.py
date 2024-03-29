import unittest

from common.constants import ACCOUNT_NAME
from common.constants import ACTION
from common.constants import ERROR
from common.constants import PRESENCE
from common.constants import RESPONSE
from common.constants import TIME
from common.constants import USER
from server import Server


class TestServer(unittest.TestCase):
    server = Server()
    error_dict = {RESPONSE: 400, ERROR: "BAD REQUEST"}
    ok_dict = {RESPONSE: 200}

    def test_without_action(self):
        self.assertEqual(self.server.client_message_handler({TIME: "2", USER: {ACCOUNT_NAME: "Guest"}}), self.error_dict)

    def test_action_not_presence(self):
        self.assertEqual(self.server.client_message_handler({ACTION: "msg", TIME: "2", USER: {ACCOUNT_NAME: "Guest"}}), self.error_dict)

    def test_without_time(self):
        self.assertEqual(self.server.client_message_handler({ACTION: PRESENCE, USER: {ACCOUNT_NAME: "Guest"}}), self.error_dict)

    def test_without_user(self):
        self.assertEqual(self.server.client_message_handler({ACTION: PRESENCE, TIME: "2"}), self.error_dict)

    def test_unknown_user(self):
        self.assertEqual(self.server.client_message_handler({ACTION: PRESENCE, TIME: "2", USER: {ACCOUNT_NAME: "Unknown"}}), self.error_dict)

    def test_ok(self):
        self.assertEqual(self.server.client_message_handler({ACTION: PRESENCE, TIME: "2", USER: {ACCOUNT_NAME: "Guest"}}), self.ok_dict)


if __name__ == "__main__":
    unittest.main()
