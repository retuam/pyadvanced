import mongoengine as me
import datetime

me.connect('my_blog')


class Author(me.Document):
    name = me.StringField(min_length=1, max_length=128)
    surname = me.StringField(min_length=1, max_length=128)
    post_qty = me.IntField(default=0)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Tag(me.Document):
    title = me.StringField(min_length=3, max_length=256, required=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Post(me.Document):
    author = me.ReferenceField(Author)
    title = me.StringField(min_length=3, max_length=256, required=True)
    body = me.StringField(min_length=3, max_length=4096, required=True)
    created = me.DateTimeField(default=datetime.datetime.now())
    views = me.IntField(default=0)
    tags = me.ListField(me.ReferenceField(Tag))

    def add_view(self):
        self.views += 1
        self.save()

    def __str__(self):
        return f'{self.id} - {self.title}'


if __name__ == '__main__':
    author = Author.objects.create(name='Arthur', surname='Cohnan')
    tag1 = Tag.objects.create(title='Tag 1')
    tag2 = Tag.objects.create(title='Tag 2')
    post = Post.objects.create(author=author,
                               title='New book',
                               body='Text',
                               tags=[tag1, tag2])
