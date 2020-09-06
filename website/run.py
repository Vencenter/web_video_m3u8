#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

cmd ="python manage.py runserver  0.0.0.0:8000"
subprocess.Popen(cmd, shell=True)
