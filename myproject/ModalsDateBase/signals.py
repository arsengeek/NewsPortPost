from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from .models import Post, User, Subscription, Author, Catigory


# @receiver(post_save, sender=Post)
# def subscriptions_post_created(instance, created, **kwargs):
#     if not created:
#         return

#     emails = User.objects.filter(subcribers__category=instance.content_post).values_list('email', flat=True)
        
#     subject = f'New post: {instance.title}'

#     text_content = (
#         f'Author: {instance.author.user}\n'
#         f'Post: {instance.title}\n'
#         f'http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'{instance.title}<br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#     )
    
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.send()
        
# # @receiver(m2m_changed, sender=Post.content_post)
# # def author_post_create(instance, action, pk_set, **kwargs):
# #     if action == 'post_add':
# #         post = instance
# #         category = post.content_post
# #         subscribers = Subscription.objects.filter(category=category).select_related('user')
# #         for subscriber in subscribers:
# #             user = subscriber.user
# #             subject = f'New Post in {category}'
# #             message = f'Hello {user.username},\n\nA new post has been published in the category {category.category}.\n\nYou can read it here: {post.get_absolute_url()}'
# #             email = EmailMultiAlternatives(subject, message, to=[user.email])
# #             email.send()