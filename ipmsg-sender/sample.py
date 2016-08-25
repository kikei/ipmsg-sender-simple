import logging
import sys

from IPMessageSender import IPMessageSender

def getLogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    return logger

def main():
    logger = getLogger()
    ipmsg = IPMessageSender('t-fujii', 'VM_T-FUJII', '10.100.103.233',
                             logger=logger)
    ipmsg.send_message('10.100.103.233', 'yomemasuka -> カレー')

if __name__ == '__main__':
    main()
