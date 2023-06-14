from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from .models import Item, Comment
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.


# def index(request):
#     return render(request, 'board/homepage.html')

def board_item(request):
    items = Item.objects.all()  # 모든 아이템 가져오기

    # Paginator를 이용해 페이지네이션 구현
    paginator = Paginator(items, 12)  # 12개의 아이템을 한 페이지에 표시
    page = request.GET.get('page')  # 현재 페이지 번호를 가져옴
    items_on_page = paginator.get_page(page)  # 현재 페이지의 아이템을 가져옴

    # 템플릿에 데이터를 전달하며 렌더링
    return render(request, 'board/homepage.html', {'items': items})


def board_detail(request, item_id):
    item = Item.objects.prefetch_related('comment_set').get(id=item_id)
    form = CommentForm()

    comments = item.comment_set.all()  # 댓글을 모두 가져옵니다.
    # Paginator 객체를 생성합니다. 여기서 10은 한 페이지에 표시할 댓글 수입니다.
    paginator = Paginator(comments, 10)
    page = request.GET.get('page')     # request로부터 현재 페이지 번호를 가져옵니다.
    comments = paginator.get_page(page)   # 현재 페이지의 댓글을 가져옵니다.

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment(content=data['content'], item=item)
            comment.save()
            return redirect(reverse('board:detail', kwargs={'item_id': item_id}))

    return render(request, 'board/detail.html', {
        'item': item,
        'form': form,
        'comments': comments,
    })


# def detail(request):
#     return render(request, 'board/detail.html')


# def detail(request):

#     return render(request, 'board/detail.html', {'comments': comments})
