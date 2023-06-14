from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from .models import Item, Comment
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    return render(request, 'board/homepage.html')


def board_detail(request, item_id):
    item = Item.objects.prefetch_related('comment_set').get(id=board_id)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            data = form.cleaned_data
            comment = Comment(content=data['content'], item=item)
            comment.save()
            return redirect(reverse('board:detail', kwargs={'item_id': item_id}))

    return render(request, 'board/detail.html', {
        'board': item,
        'form': form,
    })


def detail(request):
    return render(request, 'board/detail.html')


def comment_list(request):
    # 댓글을 모두 가져옵니다.
    comments = Comment.objects.all()

    # Paginator 객체를 생성합니다. 여기서 10은 한 페이지에 표시할 댓글 수입니다.
    paginator = Paginator(comments, 10)

    # request로부터 현재 페이지 번호를 가져옵니다.
    page = request.GET.get('page')

    # 현재 페이지의 댓글을 가져옵니다.
    comments = paginator.get_page(page)

    # 댓글과 페이지 정보를 템플릿에 전달합니다.
    return render(request, 'detail.html', {'comments': comments})
