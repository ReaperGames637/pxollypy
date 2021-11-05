import os
from Application.utils.handler import HandlerSignals

Signals = HandlerSignals()
reg_signal = Signals.reg_signal


def init_routes(path: str, alter_path: str = ''):
    for file in os.listdir(path):
        if file in ['__init__.py', '__pycache__']:
            continue
        ext = file.split('.')
        if len(ext) > 1:
            ext = ext[-1]
        if ext == 'py':
            exec(f"from {alter_path}.{file.replace('.py', '')} import __name__")


init_routes(os.path.dirname(__file__))
