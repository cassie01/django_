from django.shortcuts import render, get_object_or_404
from django.core.paginator import  Paginator
from .models import Blog, BlogType
from django.conf import settings

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每10个进行分页
    page_num = request.GET.get('page', 1)  # 默认打开第一页，获取页码参数get请求
    page_of_blogs = paginator.get_page(page_num)  # page后面不合法的字符会自动识别
    current_page_num = page_of_blogs.number  # 获取当前页码
    # page_range = [current_page_num - 2, current_page_num - 1, current_page_num, current_page_num + 1,current_page_num + 2]
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(paginator.num_pages, current_page_num + 2) + 1))#paginator.num_pages总页数


    #加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >=2:
        page_range.append('...')
    #加上首尾页码
    if page_range[0] != 1:
        page_range.insert(0, 1) #向[0]插入1
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk = blog_pk)
    context['previous_blog'] = Blog.objects.filter(create_time__gt = blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt = blog.create_time).first()
    context['blog'] = blog
    return render(request, 'blog/blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):

    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每10个进行分页
    page_num = request.GET.get('page', 1)  # 默认打开第一页，获取页码参数get请求
    page_of_blogs = paginator.get_page(page_num)  # page后面不合法的字符会自动识别
    current_page_num = page_of_blogs.number  # 获取当前页码
    # page_range = [current_page_num - 2, current_page_num - 1, current_page_num, current_page_num + 1,current_page_num + 2]
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num,
                            min(paginator.num_pages, current_page_num + 2) + 1))  # paginator.num_pages总页数

    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首尾页码
    if page_range[0] != 1:
        page_range.insert(0, 1)  # 向[0]插入1
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blog_type'] = blog_type
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blogs_with_type.html', context)



