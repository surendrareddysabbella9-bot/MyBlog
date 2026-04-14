from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Profile

class Command(BaseCommand):
    help = 'Seeds the database with initial users and posts'

    def handle(self, *args, **kwargs):
        # 1. Create Admin User
        admin_username = 'admin'
        if not User.objects.filter(username=admin_username).exists():
            admin = User.objects.create_superuser(
                username=admin_username,
                email='admin@example.com',
                password='adminpassword123'
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {admin_username}'))
        else:
            admin = User.objects.get(username=admin_username)

        # 2. Create a Regular User
        user_username = 'suren'
        if not User.objects.filter(username=user_username).exists():
            user = User.objects.create_user(
                username=user_username,
                email='suren@example.com',
                password='password123'
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user_username}'))
        else:
            user = User.objects.get(username=user_username)

        # 3. Create Sample Posts
        posts_data = [
            {
                'title': 'Welcome to MyBlog',
                'content': 'This is our first post! We are excited to share stories with you. MyBlog is built with Django and a premium UI design.',
                'tags': 'Welcome, Django, First'
            },
            {
                'title': 'The Beauty of Modern Design',
                'content': 'Design is not just what it looks like; it\'s how it feels. This blog uses Outfit and Inter fonts to provide a superior reading experience.',
                'tags': 'Design, UI, UX'
            },
            {
                'title': 'Getting Started with Coding',
                'content': 'Code is the language of the future. Whether it\'s Python or JavaScript, starting is the most important step.',
                'tags': 'Python, Coding, Future'
            }
        ]

        for p in posts_data:
            post, created = Post.objects.get_or_create(
                title=p['title'],
                defaults={
                    'content': p['content'],
                    'author': admin if 'Welcome' in p['title'] else user,
                    'tags': p['tags']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created post: {p['title']}"))

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))
