from django.shortcuts import render, redirect
from datetime import datetime
# forms.pyと連携
from . import forms
# modelのテーブル
from badApp.models import Score


# Create your views here.


def top(request):
    return render(request, 'badApp/top.html')


def member(request):
    # 都度セッションをフラッシュ
    # request.session.flush()

    name = {
        'left_name1': request.POST.get('left_name1'),
        'left_name2': request.POST.get('left_name2'),
        'right_name1': request.POST.get('right_name1'),
        'right_name2': request.POST.get('right_name2'),
    }

    if request.POST.get('left_name1') and request.POST.get('left_name2') and request.POST.get(
            'right_name1') and request.POST.get('right_name2'):
        request.session['form_data'] = request.POST
        # urls.pyを経由してtest関数を呼ぶのでapp_nameを先頭に付ける

        # 4人の名前をインサート(主キーのidは自動採番1から～)
        initname = Score(
            leftScore=0,
            rightScore=0,
            image="original",
            leftLeft=name["left_name1"],
            leftRight=name["left_name2"],
            rightLeft=name["right_name1"],
            rightRight=name["right_name2"],
        )
        initname.save()

        return redirect('badApp:bad')

    return render(request, 'badApp/member.html', name)


def bad(request):
    # テーブルから4名の名前取得
    column = Score.objects.order_by('-id').first()
    ll = column.leftLeft
    lr = column.leftRight
    rl = column.rightLeft
    rr = column.rightRight

    if not request.POST.get('score'):
        left_count = 0
        right_count = 0
    else:
        left_count = int(request.POST.get('left'))
        right_count = int(request.POST.get('right'))

    # left=1,right=2
    score = request.POST.get('score')

    # 奇数偶数でサーブコート判定、左コートのメンバーを入れ替える
    if score == '1':
        left_count += 1
        if left_count % 2 == 0:
            flag = "left_even"
        else:
            flag = "left_odd"
        data = {
            'leftCount': left_count,
            'rightCount': right_count,
            'court': flag,
            'll': lr,
            'lr': ll,
            'rl': rl,
            'rr': rr,
        }

        # スコアをインサート
        insertscore = Score(
            leftScore=data['leftCount'],
            rightScore=data['rightCount'],
            image=data['court'],
            leftLeft=data['ll'],
            leftRight=data['lr'],
            rightLeft=data['rl'],
            rightRight=data['rr'],
        )
        insertscore.save()

        return render(request, 'badApp/bad.html', data)

    # 奇数偶数でサーブコート判定、右コートのメンバーを入れ替える
    elif score == '2':
        right_count += 1
        if right_count % 2 == 0:
            flag = "right_even"
        else:
            flag = "right_odd"

        data = {
            'leftCount': left_count,
            'rightCount': right_count,
            'court': flag,
            'll': ll,
            'lr': lr,
            'rl': rr,
            'rr': rl,
        }

        # スコアをインサート
        insertscore = Score(
            leftScore=data['leftCount'],
            rightScore=data['rightCount'],
            image=data['court'],
            leftLeft=data['ll'],
            leftRight=data['lr'],
            rightLeft=data['rl'],
            rightRight=data['rr'],
        )
        insertscore.save()

        return render(request, 'badApp/bad.html', data)

    # ゲームスタート時のみココ入る
    else:
        flag = "original"
        data = {
            'leftCount': left_count,
            'rightCount': right_count,
            'court': flag,
            'll': ll,
            'lr': lr,
            'rl': rl,
            'rr': rr,
        }
        return render(request, 'badApp/bad.html', data)
