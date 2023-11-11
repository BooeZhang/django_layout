from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    自定义分页
    """
    page_query_param = "page"
    page_size_query_param = "page_size"
