from datetime import date, datetime
from functools import total_ordering
from django.contrib import admin
from django.db import models
from django.db.models.aggregates import Count
from .models import CountRoom, CountYear, Room, LoaiTT, ToTrinh
import sqlite3 
connection = sqlite3.connect("db.sqlite3", check_same_thread=False) 
#cursor = connection.cursor() 
# Register your models here.

"""def CountYear(self):
    with connection.cursor() as cursor:
        cursor .execute("SELECT count(*) FROM CreNumb_ToTrinh WHERE Year = strftime('%Y','now')")
        row = cursor.fetchone()
    return row
    connection.commit()
"""
class ToTrinhAdmin(admin.ModelAdmin):
    list_display = ('TTtitle','SoTT','TTId','user','RoomId','Year','Creted_on','Count_on_Year','Count_on_Room')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.Year = datetime.today().year
        obj.Count_on_Year = CountYear(ToTrinh)+1
        obj.Count_on_Room = CountRoom(ToTrinhAdmin)+1
        obj.SoTT = str(obj.Count_on_Year) + '/' + str(obj.Year) + '/' + str(obj.RoomId) + '/' + str(obj.TTId) + '/' +str(obj.Count_on_Room)
        obj.save()
        

admin.site.register(Room)
admin.site.register(LoaiTT)
admin.site.register(ToTrinh,ToTrinhAdmin)

admin.site.site_header  =  "Eras Group"  
admin.site.site_title  =  "Eras Group"
admin.site.index_title  =  "Lấy số tờ trình"
