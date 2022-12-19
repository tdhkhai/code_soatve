import logging

from scanner import barcode_reader

# simple usage  - in python 3
if __name__ == '__main__':
    try:
        while True:
            reader = barcode_reader("/dev/hidraw1")
            upcnumber = reader.read_barcode()
            print(upcnumber)
    except KeyboardInterrupt:
        logging.debug('Keyboard interrupt')
    except Exception as err:
        logging.error(err)