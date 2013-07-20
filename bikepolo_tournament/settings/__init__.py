from .base import *
try:
    from .local import *
except ImportError:
    pass

def get_run_mode(filename='run_mode.txt'):
    """Return the 'run mode' environment.

    :param filename: name of the file (inside this directory) that contains the
        run mode value
    :return: run mode
    :rtype: string

    """
    run_mode = read_string_from_file(
        os.path.join(SETTINGS_DIR, filename)).lower()

    if run_mode:
        if run_mode in RUN_MODES:
            return run_mode
        else:
            raise ValueError('Invalid run_mode: %s. Use only one of these run '
                             'modes:\n%s' % (run_mode, str(RUN_MODES)))
    else:
        return None


SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, "../../"))
PASSWORDS_DIR = BASE_PATH + 'passwords/'

RUN_MODES = ('prod', 'dev', 'coverage')


def read_string_from_file(filename, default=''):
    """If reading or processing fails, `default` is returned."""
    try:
        string_ = open(filename).read().strip()
    except Exception:
        string_ = default
    return string_


def read_password_from_file(name, default=''):
    """If reading or processing fails, `default` is returned."""
    return read_string_from_file(os.path.join(PASSWORDS_DIR, name), default)


def read_setting_from_file(name, default=''):
    """If reading or processing fails, `default` is returned."""
    return read_string_from_file(os.path.join(SETTINGS_DIR, name), default)

run_mode = get_run_mode()

if run_mode == 'prod':
    from .base import *
elif run_mode == 'dev':
    from .local import *
elif run_mode == 'coverage':
    from .coverage import *
else:
    raise ValueError('Unexpected run mode: %s' % run_mode)

from .s3utils import *
