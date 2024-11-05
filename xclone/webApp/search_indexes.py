from haystack import indexes
from .models import Article, Writer, Comment


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)  # Primary search field
    headline = indexes.CharField(model_attr='headline')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    content = indexes.CharField(model_attr='content')
    slug = indexes.CharField(model_attr='slug')

    def get_model(self):
        return Article
    
    def prepare_text(self, obj):
        """
        This method combines multiple fields into the `text` field, making them searchable.
        """
        return f"{obj.headline} {obj.content}"  # Concatenate fields into one searchable text field.


    def index_queryset(self, using=None):
        # Return all articles to be indexed
        return self.get_model().objects.all()


class WriterIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)  # Primary search field
    name = indexes.CharField(model_attr='name')
    email = indexes.CharField(model_attr='email')
    bio = indexes.CharField(model_attr='bio')

    def get_model(self):
        return Writer
    
    def prepare_text(self, obj):
        """
        This method combines multiple fields into the `text` field, making them searchable.
        """
        return f"{obj.name} {obj.email} {obj.bio}"

    def index_queryset(self, using=None):
        # Return all writers to be indexed
        return self.get_model().objects.all()


class CommentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)  # Primary search field
    user = indexes.CharField(model_attr='user__username')  # User's username for searching
    article = indexes.CharField(model_attr='article__headline')  # The related article's headline
    created_at = indexes.DateTimeField(model_attr='created_at')
    comment_text = indexes.CharField(model_attr='text')  # The actual comment text

    def get_model(self):
        return Comment
    
    def prepare_text(self, obj):
        """
        This method combines multiple fields into the `text` field, making them searchable.
        """
        return f"{obj.user.username} {obj.text}"

    def index_queryset(self, using=None):
        # Return all comments to be indexed
        return self.get_model().objects.all()

