import logging
import socket

class IPMessageSender:
    def __init__(self, username, hostname, host,
                 port=2425, packet_no=0, logger=None):
        self.username  = username
        self.hostname  = hostname
        self.host_from = host
        self.port_from = port
        self.packet_no = packet_no
        self.logger = logger or logging.getLogger(__name__)

    def build_command(self, message):
        self.packet_no += 1
        # Version(1):PacketNo:MyUserName:MyHostName:Command:Extra
        command = '1:{}:{}:{}:{}:{}\0'.format(self.packet_no,
                                              self.username, self.hostname,
                                              32, message)
        return command
    
    def send_message(self, host, message, port=2425):
        
        command = self.build_command(message)

        # assume message is encoded by utf8
        bs = command.encode('sjis', 'replace')
        self.logger.debug('Send IPMsg, host={}, port={}, command={}'
                          .format(host, port, bs))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((self.host_from, self.port_from))
        sock.sendto(bs, (host, port))
        sock.close()
