from django.shortcuts import render, redirect
from datetime import datetime
# forms.pyと連携
from . import forms

# Create your views here.


def top(request):

    return render(request, 'badApp/top.html')


def member(request):
    # 都度セッションをフラッシュ
    # request.session.flush()

    d = {
        'left_name1': request.POST.get('left_name1'),
        'left_name2': request.POST.get('left_name2'),
        'right_name1': request.POST.get('right_name1'),
        'right_name2': request.POST.get('right_name2'),
    }

    if request.POST.get('left_name1') and request.POST.get('left_name2') and request.POST.get('right_name1') and request.POST.get('right_name2'):
        request.session['form_data'] = request.POST
        # urls.pyを経由してtest関数を呼ぶのでapp_nameを先頭に付ける
        return redirect('badApp:bad')

    return render(request, 'badApp/member.html', d)


def bad(request):

    if not request.POST.get('score'):
        left_count = 0
        right_count = 0
    else:
        left_count = int(request.POST.get('left'))
        right_count = int(request.POST.get('right'))

    score = request.POST.get('score')

    if score == '1':
        left_count += 1
        if left_count % 2 == 0:
            flag = "left_even"
        else:
            flag = "left_odd"
        data = {
            'leftCount': left_count,
            'rightCount': right_count,
            'server': flag,
        }
        return render(request, 'badApp/bad.html', data)
    elif score == '2':
        right_count += 1
        if right_count % 2 == 0:
            flag = "right_even"
        else:
            flag = "right_odd"

        data = {
            'leftCount': left_count,
            'rightCount': right_count,
            'server': flag,

        }
        return render(request, 'badApp/bad.html', data)
    else:
        flag = "original"
        data = {
            'leftCount': left_count,
            'rightCount': right_count,
            'server': flag,
        }
        return render(request, 'badApp/bad.html', data)
