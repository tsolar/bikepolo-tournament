#!/bin/bash

set -e

APP_NAME="bikepolo_tournament"
PROJ_NAME="bikepolo_tournament"
DIR_SUFFIX="-t1"

VENV_PROJECTS="/srv/sites"
VENV_DIR="/home/tom/venvs/bikepolo-tournament"
GUN_CONF_MODULE="deploy/gunicorn.conf.py"

PROJ_HOME=$VENV_PROJECTS/$PROJ_NAME$DIR_SUFFIX
WSGI_MODULE=$APP_NAME.wsgi

source $VENV_DIR/bin/activate

cd $PROJ_HOME
exec gunicorn -c $GUN_CONF_MODULE $WSGI_MODULE:application
