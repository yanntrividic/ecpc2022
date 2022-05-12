# -*- coding: utf-8 -*-

from bottle import run, Bottle
import mic

app = Bottle()

run(host='localhost', port=8080, debug=True)