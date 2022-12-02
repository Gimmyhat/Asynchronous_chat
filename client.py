import socket
import time
from common.constants import *
from common.utils import *


class Client:

    def __init__(self, account_name='Guest', server_address=DEFAULT_IP_ADDRESS, server_port=DEFAULT_PORT):
        self.server_address = server_address
        self.server_port = int(server_port)
        self.account_name = account_name

    def create_presence(self):
        out_mes = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: self.account_name
            }
        }
        return out_mes

    @staticmethod
    def answer_handler(message):
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return 'OK'
            return f'400 : {message[ERROR]}'
        raise ValueError

    def main(self):
        if self.server_port < 1024 or self.server_port > 65535:
            raise ValueError

        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((self.server_address, self.server_port))
        message = self.create_presence()
        send_message(transport, message)
        try:
            answer = self.answer_handler(get_message(transport))
            print(answer)
        except ValueError:
            print('Не удалось декодировать сообщение')


if __name__ == '__main__':
    client = Client()
    client.main()