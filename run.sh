#!/bin/bash
uwsgi --socket call411.sock --module call411.wsgi --chmod-socket=666
