import mongoengine as me


me.connect('homework_11')


class User(me.Document):
    first_name = me.StringField(required=True, min_length=1, max_length=128)
    last_name = me.StringField(max_length=128)
    parent_name = me.StringField(max_length=128)
    telephone = me.StringField(max_length=16)
    email = me.EmailField()
    address = me.StringField(max_length=256)
    comments = me.StringField(max_length=4096)
    status = me.IntField(dump_only=True, default=0)
    chat_id = me.IntField(dump_only=True, required=True)
