import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import date
from django.db import connection


# Create your models here.

class Room(models.Model):
    RoomID = models.CharField('Ký hiệu phòng',max_length=30)
    def __str__(self):
        return self.RoomID    #hiển thị tên từng loại tờ trình theo tên phòng
    class Meta:
        verbose_name_plural = 'Phòng ban'

class LoaiTT(models.Model):
    TTId = models.CharField('Ký hiệu TT',max_length=20)
    #TTName = models.CharField('Tên đầy đủ',max_length=50)
    def __str__(self):
        return self.TTId  #hiển thị tên từng loại tờ trình theo tên tờ trình 
    class Meta:
        verbose_name_plural = 'Loại tờ trình' 

class ToTrinh(models.Model):
    SoTT = models.CharField('Số tờ trình',max_length=50,editable=False,null=True,blank=True)
    TTId = models.ForeignKey(LoaiTT, on_delete=models.PROTECT,verbose_name='Loại tờ trình')
    TTtitle = models.CharField('Tên tờ trình',max_length=150)
    TTText = models.TextField('Nội dung tóm tắt',max_length=500,null=True,blank=True)
    Creted_on = models.DateField('Ngày lấy số',auto_now_add=True)
    Year = models.CharField(max_length=4,null=True,blank=True,editable=False)
    user = models.ForeignKey(User,on_delete=PROTECT,editable=False,null=True,verbose_name='Người tạo')
    RoomId = models.ForeignKey(Room,on_delete=PROTECT,null=True,verbose_name='Phòng')
    Count_on_Year = models.CharField(max_length=5, null=True,blank=True,editable=False)
    Count_on_Room = models.IntegerField(null=True,blank=True,editable=False)
    
     
    def __str__(self):
        return self.TTtitle  #hiển thị tờ trình theo SoTT

    class Meta:
        verbose_name_plural  = 'Tờ trình'
    #Year = date.today().year
     
def CountYear(self):
    with connection.cursor() as cursor:
        cursor .execute("SELECT count(*) FROM CreNumb_ToTrinh WHERE Year = strftime('%Y','now')")
        row = cursor.fetchone()
    return row[0]

def CountRoom(self):
    with connection.cursor() as cursor:
        cursor .execute("SELECT count(*) FROM CreNumb_ToTrinh WHERE Year = strftime('%Y','now') AND CreNumb_ToTrinh.RoomId_id = CreNumb_loaitt.TTId")
        row = cursor.fetchone()
    return row[0]
