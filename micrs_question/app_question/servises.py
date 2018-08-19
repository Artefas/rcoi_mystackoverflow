from django.contrib.contenttypes.models import ContentType

from .models import Comment

def get_comments(obj):
    """Возвращает комментарии к объекту 'obj'
    """
    obj_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=obj_type, object_id=obj.id)
    return comments