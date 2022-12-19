import logging
import socket
import sys
import project_logs.config.server_logs_config

from common.constants import *
from common.utils import *
from decors import Log


class Server:
    SERVER_LOGGER = logging.getLogger('server_logger')

    def __init__(self, server_address=DEFAULT_IP_ADDRESS, server_port=DEFAULT_PORT):
        self.server_address = server_address
        self.server_port = int(server_port)

    @Log()
    def client_message_handler(self, message):
        self.SERVER_LOGGER.debug(f'Received message: {message}')

        if ACTION in message and message[ACTION] == PRESENCE \
                and TIME in message and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            return {RESPONSE: 200}
        self.SERVER_LOGGER.error('Server response: 400')
        return {
            RESPONSE: 400,
            ERROR: 'BAD REQUEST'
        }

    @Log()
    def main(self):
        if self.server_port < 1024 or self.server_port > 65535:
            self.SERVER_LOGGER.critical('Invalid server port')
            raise ValueError

        self.SERVER_LOGGER.info(f'Server object created address: {self.server_address}, port: {self.server_port}')
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((self.server_address, self.server_port))

        transport.listen(MAX_CONNECTIONS)

        while True:
            client, client_addr = transport.accept()
            try:
                message = get_message(client)
                print(message)
                response = self.client_message_handler(message)
                send_message(client, response)
                client.close()
            except ValueError:
                self.SERVER_LOGGER.error('Invalid message')
            finally:
                client.close()


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-a' and sys.argv[2]:
            DEFAULT_IP_ADDRESS = sys.argv[2]
        if sys.argv[3] == '-p' and sys.argv[4]:
            DEFAULT_PORT = sys.argv[4]
    except:
        pass
    server = Server()
    server.main()
