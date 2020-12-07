from django.db import models


# Create your models here.

# class Topic(models.Model):
#     '''用户学习的主题'''
#     # 创建两个属性：text(文本限制200个字符)、date_added(自动设置成当前时间)
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         '''返回模型的字符串表示'''
#         return self.text
#
#
# class Entry(models.Model):
#     """学到的有关某个主题的具体知识"""
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     '''用于存储管理模型的额外信息'''
#
#     class Meta:
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         """返回模型的字符串表示"""
#         if len(self.text) < 50:
#             return self.text
#         else:
#             return self.text[:50] + '...'

class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name
