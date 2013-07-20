import multiprocessing
import os
import sys


GB_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GB_LOGS_DIR = os.path.join(GB_BASE_DIR, 'z-logs')

sys.path.append(os.path.join(GB_BASE_DIR, 'bikepolo_tournament'))
#print GB_BASE_DIR
#print sys.path
#noinspection PyUnresolvedReferences
from settings import get_run_mode


_run_mode = get_run_mode()

if _run_mode == 'prod':
    _bind_port = '8100'
    _number_workers = 1 + multiprocessing.cpu_count() * 2
    _log_filename = 'gunicorn_www-error.log'
elif _run_mode == 'test' or _run_mode == 'dev':
    _bind_port = '8100'
    _number_workers = 1
    _log_filename = 'gunicorn_t1-error.log'
else:
    raise ValueError('Unexpected run mode: %s' % _run_mode)


###########################################
# Gunicorn docs | Configuration overview
# http://docs.gunicorn.org/en/latest/configure.html
###########################################

debug = True


###############
# Server Socket

# The socket to bind
bind = '127.0.0.1:%s' % _bind_port

# The maximum number of pending connections
backlog = 1024


###############
# Worker Processes

# The number of worker process for handling requests
workers = _number_workers

# The type of workers to use
# worker_class =

# The maximum number of simultaneous clients (only affects the Eventlet and Gevent worker types)
# worker_connections =

# The maximum number of requests a worker will process before restarting
# max_requests =

# Workers silent for more than this many seconds are killed and restarted
# timeout =

# Timeout for graceful workers restart
# graceful_timeout =

# The number of seconds to wait for requests on a Keep-Alive connection
# keepalive =


###############
# Security


###############
# Debugging


###############
# Server Mechanics #1
#user = "www-data"  #TODO: set this
#group = "www-data"  #TODO: set this


###############
# Logging
loglevel = "warning"
errorlog = os.path.join(GB_LOGS_DIR, _log_filename)


###############
# Process Naming


###############
# Django


###############
# Server Hooks


###############
# Server Mechanics #2
