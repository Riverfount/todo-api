from datetime import datetime

from mongoengine import (
    DateTimeField,
    Document,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    ObjectIdField,
    StringField,
)


class TodoGroupedData(EmbeddedDocument):
    id = ObjectIdField(required=True)
    name = StringField(required=True)


class UserData(Document):
    name = StringField(required=True)
    created_at = DateTimeField(default=datetime.now().replace(microsecond=0))
    email = EmailField(required=True)
    password = StringField(required=True)
    user_todo = EmbeddedDocumentListField(TodoGroupedData, required=False)

    meta = {
        "collection": "user",
        "indexes": ["created_at"],
        "strict": False,
        "ordering": ["-created_at"],
    }
