from django.contrib import admin
from finance.models import Earning, Spending, Investment, Debt, Goal, Memo, MemoComment, Member, Family


# Register your models here.
admin.site.register(Earning)
admin.site.register(Spending)
admin.site.register(Investment)
admin.site.register(Debt)
admin.site.register(Goal)
admin.site.register(Memo)
admin.site.register(MemoComment)
admin.site.register(Member)
admin.site.register(Family)