#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        resp = a / b
    except ZeroDivisionError:
        resp = None
    finally:
        print('Inside result: {}'.format(resp))

    return resp
