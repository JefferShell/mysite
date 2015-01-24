#coding:utf-8
from django.contrib import admin

from mysite.blog.models import Book, Author, Publisher
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')
class BookAdmin(admin.ModelAdmin):
    #这个是表单显示的字段，默认是显示一个
    list_display = ('title','publication_date','publisher')
    #顶部搜索栏搜索的字段范围
    search_fields = ('title',)
    #右侧会出现搜索的表格选项
    list_filter  = ('publication_date',)
    #顶部会出现表格搜索的选项
    date_hierarchy = 'publication_date'
    #数据默认的排序
    ordering = ('-publication_date',)
    #字段显示的前后
#    fields = ('publisher','authors','title')
    #多对多关系时选择样式
#    filter_horizontal = ('authors',)
    filter_vertical = ('authors',)
    #外键过多时，使用这个
    raw_id_fields = ('publisher',)


admin.site.register(Book,BookAdmin) 
admin.site.register(Publisher) 
admin.site.register(Author,AuthorAdmin)
