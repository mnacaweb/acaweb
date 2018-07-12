#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acamar_web.settings")
    sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__)),'libs','unpacked'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
