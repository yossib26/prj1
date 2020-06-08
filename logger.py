import glob
import logging
import logging.handlers
import os
import zipfile

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

LOG_FILENAME = 'logging.out'

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024, backupCount=10)
handler.setFormatter(formatter)
my_logger.addHandler(handler)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# # add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
my_logger.addHandler(ch)

my_logger.debug('Great JOb !!!!!!!!!!!!!!!!!')

my_logger.debug('This is a debug message QQ')
my_logger.info('This is an info message')
my_logger.warning('This is a warning message')
my_logger.error('This is an error message')
my_logger.critical('This is a critical error message')

locfile = os.path.dirname(__file__) + "/logging.out"
locfile2 = os.path.dirname(__file__) + "/logging.out.10"

tarfile = os.path.dirname(__file__) + "/logging.zip"

# print(os.path.basename(locfile))
zip = zipfile.ZipFile(tarfile, "w", zipfile.ZIP_DEFLATED)

path = os.path.dirname(__file__)
files = []
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'logging.out' in i:
        files.append(i)
        zip.write(i)
        print(i)

print(files)

#
# zip.write(locfile)
# zip.write(locfile2)

quit()

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

LOG_FILENAME = 'logging.out'

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024, backupCount=10)
handler.setFormatter(formatter)
my_logger.addHandler(handler)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# # add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
my_logger.addHandler(ch)

my_logger.debug('Great JOb !!!!!!!!!!!!!!!!!')

my_logger.debug('This is a debug message QQ')
my_logger.info('This is an info message')
my_logger.warning('This is a warning message')
my_logger.error('This is an error message')
my_logger.critical('This is a critical error message')

# Log some messages
for i in range(20):
    my_logger.debug('LOG i = %d' % i)

quit()

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print(filename)


# ---------------------------------------------------------------

logging.warning("'warning!!!!!!11")
logging.error('This is an error message')
logging.info('I told you so')  # will not print anything

print(os.path.dirname(__file__))
p = os.path.dirname(__file__) + '/logfile.log'

print(p)

logging.basicConfig(filename=p, filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

name = "yossi"
logging.error('%s raised an error', name)

logging.info('Finished')
