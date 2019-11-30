# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
import uuid

class Family(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Member(models.Model):
    fam_id = models.ForeignKey(Family, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Debt(models.Model):
    net_amount = models.BigIntegerField(default=0, null=True)
    type = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    borrow_from = models.CharField(max_length=255, null=True)
    Member_id = models.ForeignKey(
        Member, default=0, related_name='debt', on_delete=models.CASCADE)

    def __str__(self):  # get function
        return self.type

    class Meta:
        # managed = False
        db_table = 'debt'


class Earning(models.Model):
    type = models.CharField(max_length=255, null=True)
    year = models.BigIntegerField(default=0, null=True)
    wage = models.BigIntegerField(default=0, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    Member_id = models.ForeignKey(
        Member, default=0, related_name='earning', on_delete=models.CASCADE)
    def __str__(self):  # get function
        return self.type

    class Meta:
        # managed = False
        db_table = 'earning'


class Goal(models.Model):
    task = models.CharField(max_length=255, null=True)
    budget = models.BigIntegerField(default=0, null=True)
    Member_id = models.ForeignKey(
        Member, default=0, related_name='goal', on_delete=models.CASCADE)

    def __str__(self):  # get function
        return self.task

    class Meta:
        # managed = False
        db_table = 'goal'


class Investment(models.Model):
    net_amount = models.BigIntegerField(default=0, null=True)
    type = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    Member_id = models.ForeignKey(
        Member, default=0, related_name='investment', on_delete=models.CASCADE)

    def __str__(self):  # get function
        return self.type

    class Meta:
        # managed = False
        db_table = 'investment'


class Spending(models.Model):
    neg_amount = models.BigIntegerField(default=0, null=True)
    year = models.BigIntegerField(default=0, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    type = models.CharField(max_length=255, null=True)
    purpose = models.CharField(max_length=255, null=True)
    Member_id = models.ForeignKey(
        Member, default=0, related_name='spending', on_delete=models.CASCADE)

    def __str__(self):  # get function
        return self.type

    class Meta:
        # managed = False
        db_table = 'spending'


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Memo(models.Model):
    subject = models.CharField(max_length=255, null=True)
    # slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1)
    date = models.DateTimeField(auto_now_add=True, null=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(
        User, default=0, related_name='Memo', on_delete=models.CASCADE)

    def __str__(self):  # get function
        return self.subject


class MemoComment(models.Model):
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, related_name='memoComment')
    comment = models.CharField(max_length=4000, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(
        User, default=0, related_name='memoComment', on_delete=models.CASCADE)

    def __str__(self):  # get function
        return self.comment
