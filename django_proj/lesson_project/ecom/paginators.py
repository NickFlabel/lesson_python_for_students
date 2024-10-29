from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page" #?page=2
    page_size_query_param = "page_size"
    max_page_size = 100