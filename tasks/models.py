from django.db import models
from comments.models import Comment
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=12, verbose_name='Task Name')
    task_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    task_notes = models.TextField(blank=True, verbose_name='Task Notes')
    task_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_creators',verbose_name='Created By')
    task_assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_assignees',verbose_name='Assigned To')
    task_due = models.DateField(blank=True, null=True, verbose_name='Date Created')
    task_completed = models.DateField(blank=True, null=True, verbose_name='Date Completed')
    task_comments = models.ManyToManyField(Comment, blank=True, verbose_name='Comments')

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['-task_created']
        get_latest_by = ['task_created']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
