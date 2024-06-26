from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    # Количество элементов на странице
    page_size = 5
    # Параметр запроса количества элементов на странице
    page_size_query_param = ('page_size')
    # Максимальное количество элементов на странице
    max_page_size = 20
