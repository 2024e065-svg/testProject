from django.shortcuts import render
from .models import Post  # ← Postモデルを使うために必要です

# 既存のindex関数（もし残す必要があれば）
def index(request):
    context = {
        'title': 'こんにちは、yabu yuto',
        'message': 'これはテンプレートを使ったテストページです。',
        'food_list': ['焼肉','ラーメン','寿司','チャーハン','うどん'],
    }
    return render(request, 'index.html', context)

# app/views.py

def timeline(request):
    # 【良い例】select_related を追加して、ユーザー情報もまとめて取る
    posts = Post.objects.select_related('author').order_by('-created_at')
    
    return render(request, 'timeline.html', {'posts': posts})