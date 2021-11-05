from . import reg_signal, ErrorVK


@reg_signal('set_admin')
def set_admin(**kwargs):
    db = kwargs['db']
    event_obj = kwargs['event']['object']

    try:
        kwargs['vk'].method('messages.setMemberRole', {'member_id': event_obj['user_id'],
                                                       'peer_id': db.get_chat_uid(event_obj['chat_id'])+2000000000,
                                                       'role': 'admin' if event_obj['admin'] else 'member'})
    except ErrorVK as ev:
        return '0'
    return '1'
