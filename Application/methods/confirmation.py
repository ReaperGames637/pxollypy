from . import reg_signal


@reg_signal('confirmation')
def confirmation(**kwargs):
    return kwargs['db'].code
