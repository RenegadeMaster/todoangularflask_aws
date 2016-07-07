from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute,
    BooleanAttribute)



class Todo(Model):
    class Meta:
        table_name = 'todos'
        region = 'us-east-1'
    id = NumberAttribute(hash_key=True)
    task = UnicodeAttribute()
    done = BooleanAttribute()
    date = UTCDateTimeAttribute()
