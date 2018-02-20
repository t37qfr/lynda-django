from django.shortcuts import render,get_object_or_404
'''Paginator'''
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post,Comment
'''form'''
from .forms import EmailPostForm,CommentForm
'''taggit'''
from taggit.models import Tag
from django.db.models import Count



def post_list(request,tag_slug=None):
    object_list=Post.published.all()

    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        '''if page not an integer deliver the first page'''
        posts = paginator.page(1)
    except EmptyPage:
        '''if page out of range deliver last page of result'''
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{
        'posts':posts,
        'page':page,
        'tag':tag

    })


def post_detail(request,post):
    print('ok')
    post = get_object_or_404(Post,slug=post,status='published')

    '''Comments'''
    comments=post.comments.filter(active=True)
    if request.method=='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            '''assign corrent post to the comment'''
            new_comment.post = post
            '''save'''
            new_comment.save()
    else:
        comment_form = CommentForm()


    #List of similar posts
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]


    return render(request,'blog/post/detail.html',{
        'post':post,
        'comments':comments,
        'comment_form':comment_form,
        'similar_posts':similar_posts
    })


def post_share(request,post_id):
    '''Retrive post by id'''
    post = get_object_or_404(Post,id=post_id,status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_abolute_uri(post.get_absolute_url())
            subject = 'Recommend0'
            message = 'msg'
            send_email(subject,message,admin@myblog.com,[cd['to']])
            sent=True
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{
        'post':post,
        'form':form,
        'sent':sent
    })
