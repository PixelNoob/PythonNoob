import logging

logging.basicConfig(filename='/file_destination_here',level=logging.DEBUG)

msg = input('Leave a Message: ')

logging.debug(msg)
