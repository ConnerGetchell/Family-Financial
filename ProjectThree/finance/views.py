from django.shortcuts import render, get_object_or_404
from .models import  Family, Member, Debt, Spending, Earning, Investment,  Memo, MemoComment
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.views import generic
from .forms import CommentForm, NewMemoForm
from django.contrib.auth.decorators import login_required
# finance views

def new_memo(request):
    currentMember = Member.objects.get(user_id=request.user)
    if request.method == 'POST':
        form = NewMemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.Member_id = currentMember
            memo.save()
            MemoComment.objects.create(
                comment = form.cleaned_data.get('message'),
                memo = memo,
                Member_id = currentMember
                )
    else:
        form = NewMemoForm()
    return render(request, 'new_memo.html', {'form' : form})


@login_required
def memberIncome(request):
    return render(request, 'memberIncome.html')

@login_required
def memberSpending(request):
    return render(request, 'memberSpending.html')

@login_required
def home(request):
    memo = Memo.objects.all()
    context = {'memos': memo}
    return render(request, 'home.html', context)

@login_required
def comment(request):
    memoComment = MemoComment.objects.all()
    context = {'memoComments': memoComment}
    return render(request, 'comment.html', context)

@login_required
def earning(request):
    member = Member.objects.get(user_id=request.user.id)
    family_id = member.fam_id
    all_family_members = Member.objects.filter(fam_id=family_id)
    Earnings = Earning.objects.filter(Member_id__in=all_family_members)
    earning = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Earnings},
             'terms': [{
                 'wage': 'wage', 'year': 'year'}]},
        ]
    )

    cht = Chart(
        datasource=earning,
        series_options=[{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'year': ['wage']
        }}],
        chart_options={'title': {
            'text': 'Family Income over the Past 10 Years'},
            'xAxis': {
            'title': {'text': 'Year'}},
            'yAxis': {
            'title': {'text': 'Wage'}},
            'legend': {
            'enabled': True},
            'credits': {
            'enabled': True}},

    )
    return render(request, 'earning.html', {'chart_list': [cht], 'member' : member})

@login_required
def debt(request):
    member = Member.objects.get(user_id=request.user.id)
    family_id = member.fam_id
    all_family_members = Member.objects.filter(fam_id=family_id)
    Debts = Debt.objects.filter(Member_id__in=all_family_members)
    debt = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Debts},
             'terms': [{
                 'type': 'type', 'net_amount': 'net_amount'}]},
        ]
    )

    cht = Chart(
        datasource=debt,
        series_options=[{'options': {
            'type': 'column',
            'stacking': False},
            'terms': {
                'type': [
                    'net_amount']
        }}],
        chart_options={'title': {
            'text': 'Amount of Debts vs Type of Loan in the Past 5 Years'},
            'xAxis': {
            'title': {'text': 'Type'}},
            'yAxis': {
            'title': {'text': 'Net Amount'}},
            'legend': {
            'enabled': True},
            'credits': {
            'enabled': True}},

    )
    return render(request, 'debt.html', {'chart_list': [cht]})

@login_required
def spending(request):
    member = Member.objects.get(user_id=request.user.id)
    family_id = member.fam_id
    all_family_members = Member.objects.filter(fam_id=family_id)
    Spendings = Spending.objects.filter(Member_id__in=all_family_members)
    spending = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Spendings},
             'terms': [{
                 'type': 'type', 'neg_amount': 'neg_amount'}]},
        ]
    )

    cht = Chart(
        datasource=spending,
        series_options=[{'options': {
            'type': 'column',
            'stacking': False},
            'terms': {
                'type': [
                    'neg_amount']
        }}],
        chart_options={'title': {
            'text': 'Spending Habits'},
            'xAxis': {
            'title': {'text': 'Type'}},
            'yAxis': {
            'title': {'text': 'Amount'}},
            'legend': {
            'enabled': True},
            'credits': {
            'enabled': True}},

    )
    return render(request, 'spending.html', {'chart_list': [cht]})

@login_required
def investment(request):
    member = Member.objects.get(user_id=request.user.id)
    family_id = member.fam_id
    all_family_members = Member.objects.filter(fam_id=family_id)
    Investments = Investment.objects.filter(Member_id__in=all_family_members)
    investment = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Investments},
             'terms': [{
                 'type': 'type', 'net_amount': 'net_amount'}]},
        ]
    )

    cht = Chart(
        datasource=investment,
        series_options=[{'options': {
            'type': 'pie',
            'stacking': False},
            'terms': {
                'type': [
                    'net_amount']
        }}],
        chart_options={'title': {
            'text': 'Percentage Distribution of Investments'},
            'xAxis': {
            'title': {'text': 'Type'}},
            'yAxis': {
            'title': {'text': 'Net Amount'}},
            'legend': {
            'enabled': True},
            'credits': {
            'enabled': True}},
    )
    return render(request, 'investment.html', {'chart_list': [cht]})

@login_required
def inandout(request):
    member = Member.objects.get(user_id=request.user.id)
    family_id = member.fam_id
    all_family_members = Member.objects.filter(fam_id=family_id)
    Earnings = Earning.objects.filter(Member_id__in=all_family_members)
    Spendings = Spending.objects.filter(Member_id__in=all_family_members)
    debt = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[{'options': {
            'source': Earnings},
            'terms': [
                {'wage': 'wage', 'year': 'year'}]},
            {'options': {
                'source': Spendings},
             'terms': [
                {'neg_amount': 'neg_amount', 'year2': 'year'}]}]


    )

    cht = Chart(
        datasource=debt,
        series_options=[{'options': {
            'type': 'column',
            'stacking': False},
            'terms': {
                'year': [
                    'wage'],
                'year2': [
                    'neg_amount']
        }}],
        chart_options={'title': {
            'text': 'Income vs Spending over the Last 10 Years'},
            'xAxis': {
            'title': {'text': 'Income and Spending'}},
            'yAxis': {
            'title': {'text': 'Amount'}},
            'legend': {
            'enabled': True},
            'credits': {
            'enabled': True}},

    )
    return render(request, 'inandout.html', {'chart_list': [cht]})
