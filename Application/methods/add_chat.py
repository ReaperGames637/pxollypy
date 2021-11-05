from . import reg_signal


@reg_signal('add_chat')
def add_chat(**kwargs):
    db = kwargs['db']
    event_obj = kwargs['event']['object']
    if db.receive(f"SELECT COUNT(*) FROM conversations WHERE local_id = '{event_obj['chat_id']}'") == 1:
        db.save(f"UPDATE conversations SET peer_id = {event_obj['chat_uid']} WHERE local_id = '{event_obj['chat_id']}'")
    else:
        db.save(f"INSERT INTO conversations (peer_id, local_id) VALUES ({event_obj['chat_uid']}, '{event_obj['chat_id']}')")
    return '1'
