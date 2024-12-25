from django.shortcuts import render
from .models import Post, Category
from django.http import Http404
from django.utils import timezone


def index(request):
    posts = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )[:5]
    return render(
        request,
        template_name='blog/index.html',
        context={'posts': posts}
    )


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)

        if not post.is_published:
            raise Http404("Публикация не существует или скрыта.")

        if not post.category.is_published:
            raise Http404("Категория этой публикации скрыта.")

        if post.pub_date > timezone.now():
            raise Http404("Публикация еще не опубликована.")

    except Post.DoesNotExist:
        raise Http404("Публикация не найдена.")

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)

        if not category.is_published:
            raise Http404("Категория не существует или скрыта.")

        now = timezone.now()

        posts = Post.objects.filter(
            category=category,
            is_published=True,
            pub_date__lte=now
        ).order_by('-pub_date')

    except Category.DoesNotExist:
        raise Http404("Категория не найдена.")

    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts,
    })
