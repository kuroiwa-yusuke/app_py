import sys
import signal

sys.path
def sigterm(x, y):
    pass


signal.signal(signal.SIGTERM, sigterm)

print("hello pipenv-docker-development world!", flush=True)

signal.sigwait([signal.SIGTERM])

print("shutdown...", flush=True)