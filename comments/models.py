from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    comment_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    comment_text = models.TextField(blank=True, verbose_name='Comment Text')
    comment_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment_creators',verbose_name='Created By')
    parent_comment = models.ManyToManyField('self', blank=True, verbose_name='Parent Comment')

    def __str__(self):
        return  self.comment_created + ' - ' + self.comment_created_by

    class Meta:
        ordering = ['-comment_created']
        get_latest_by = ['-comment_created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
