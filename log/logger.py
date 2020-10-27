import logging

logging.basicConfig(format='%(asctime)-15s %(processName)-8s [%(threadName)s] %(levelname)-8s %(message)s',
                    level=logging.DEBUG, filename='/home/carlossanchezpaez/log/web_interface.log')
logger = logging.getLogger()
