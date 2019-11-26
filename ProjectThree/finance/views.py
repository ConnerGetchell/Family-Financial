from django.shortcuts import render, get_object_or_404
from .models import Debt, Spending, Earning, Investment,  Memo, MemoComment
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.views import generic
from .forms import CommentForm

# finance views


# class home(generic.ListView):
#     queryset = Memo.objects.filter(status=1).order_by('-created_on')
#     template_name = 'home.html'
#
#
# def post_detail(request, slug):
#     template_name = 'comment.html'
#     memo = get_object_or_404(Memo, slug=slug)
#     comments = memo.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.memo = memo
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'memo': memo,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})

def home(request):
    memo = Memo.objects.all()
    context = {'memos': memo}
    return render(request, 'home.html', context)


def comment(request):
    memoComment = MemoComment.objects.all()
    context = {'memoComments': memoComment}
    return render(request, 'comment.html', context)


def earning(request):
    earning = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Earning},
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
    return render(request, 'earning.html', {'chart_list': [cht]})


def debt(request):
    debt = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Debt},
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


def spending(request):
    spending = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Spending},
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


def investment(request):
    investment = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[
            {'options': {
                'source': Investment},
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


def inandout(request):
    debt = DataPool(  # what data is being retrieved and where it is being retrieved from
        series=[{'options': {
            'source': Earning},
            'terms': [
                {'wage': 'wage', 'year': 'year'}]},
            {'options': {
                'source': Spending},
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
