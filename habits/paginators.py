from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    # Количество элементов на странице
    page_size = 5
    # Параметр запроса количества элементов на странице
    page_size_query_param = ('page_size')
    # Максимальное количество элементов на странице
    max_page_size = 20


class UserPagination(PageNumberPagination):
    # Количество элементов на странице
    user_count = 5
    # Параметр запроса количества элементов на странице
    user_size_query_param = ('user_count')
    # Максимальное количество элементов на странице
    max_user_size = 20
