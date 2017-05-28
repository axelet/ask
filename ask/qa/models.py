from __future__ import unicode_literals

from django.db import models, connection
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new_questions(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM question q
            ORDER BY q.added_at DESC
            """)
        return cursor.fetchall()[:]

    def popular_questions(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM question q
            ORDER BY q.rating DESC
            """)
        return cursor.fetchall()[:]


class Question(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')

    objects = QuestionManager()

    def __unicode__(self):
        # reverse()
        return self.title

    def get_absolute_url(self):
        return '/question/%d' % self.pk

    def get_full_info(self):
        return [str(self.id), self.title, self.text, str(self.rating),  self.author.username]

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.text


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     c = models.TextField(choices=)
#     content = models.TextField()
#     creation_date = models.DateTimeField(blank=True)
#
#     category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL())
#     status = models.OneToOneField(PostStatus)
#     tags = models.ManyToManyField(Tag)
#
#     def __unicode__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return '/post/%d' % self.pk
#
#     class Meta:
#         db_table = 'blogposts'
#         ordering = ['-creation_date']# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     c = models.TextField(choices=)
#     content = models.TextField()
#     creation_date = models.DateTimeField(blank=True)
#
#     category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL())
#     status = models.OneToOneField(PostStatus)
#     tags = models.ManyToManyField(Tag)
#
#     def __unicode__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return '/post/%d' % self.pk
#
#     class Meta:
#         db_table = 'blogposts'
#         ordering = ['-creation_date']