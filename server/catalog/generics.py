"""
Generics Module

This module contains a collection of utility functions designed to aid in the development of Django admin interfaces. These functions provide generic implementations for common tasks such as creating links to changelist views, concatenating names of related objects, annotating and prefetching querysets, and setting custom short descriptions in the admin.

Functions:
    - create_link_to_changelist: Generates a hyperlink to a changelist view in the Django admin, filtered by a specific query parameter.
    - get_related_names: Retrieves and concatenates the names of related objects for a given object.
    - annotate_and_prefetch: Annotates a queryset with a count of related objects and prefetches related data.
    - short_description: A decorator to set a custom short description for a function, typically used in the Django admin.

Use these functions to enhance the readability and maintainability of your admin interfaces by abstracting common functionality into reusable components.

Examples and detailed descriptions for each function are provided in their respective docstrings.
"""
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

def get_related_names(obj, related_field_name):
    """
    Retrieves and concatenates the names of related objects for a given object.

    :param obj: Model instance, the object for which to retrieve related names.
        E.g., a book instance when retrieving author names.
    :param related_field_name: str, the name of the related field on the object.
        E.g., 'author_books' to get authors of a book.

    :return: str, a concatenated string of related names, separated by commas.
    """
    related_objects = getattr(obj, related_field_name).all()
    names = [str(related_obj) for related_obj in related_objects]
    return ', '.join(names)


def annotate_and_prefetch(queryset, count_field, prefetch_field):
    """
    Annotates a queryset with a count of related objects and prefetches related data.

    :param queryset: QuerySet, the queryset to annotate and prefetch.
    :param count_field: str, the field to count for the annotation.
        E.g., 'author_books' to count the books for each author.
    :param prefetch_field: str, the field to prefetch for optimization.
        E.g., 'genres' to prefetch genres for books.

    :return: QuerySet, the annotated and prefetched queryset.
    """
    # ...
    return queryset.annotate(
        book_count=Count(count_field)
    ).prefetch_related(prefetch_field)


def short_description(description):
    """
    Decorator to set a custom short description for a function, typically used in the Django admin.

    :param description: str, the custom description to set.

    :return: function, the decorated function with the custom short_description attribute.
    """
    def decorator(func):
        func.short_description = description
        return func
    return decorator


def create_link_to_changelist(admin_view_name, query_param_name, obj, related_field_name):
    """
    Creates a link to a changelist view in the Django admin interface, 
    filtered by a specific query parameter.

    :param admin_view_name: str, the name of the view in the admin site to reverse.
        E.g., 'admin:catalog_book_changelist' for the changelist view of books.
    :param query_param_name: str, the name of the query parameter used to filter the changelist.
        E.g., 'authors__id' to filter books by author ID.
    :param obj: Model instance, the object whose details are being used to create the link.
        E.g., an author instance when linking to a list of their books.
    :param related_field_name: str, the name of the attribute on the object containing the count 
        or other information to display in the link text.
        E.g., 'book_count' for the count of books related to an author.

    :return: SafeString, an HTML link to the filtered changelist view, with the count or other info as the link text.
    """
    url = (
        reverse(admin_view_name)
        + '?'
        + urlencode({
            query_param_name: str(getattr(obj, 'id'))
        })
    )
    count = getattr(obj, related_field_name)
    return format_html('<a href="{}">{}</a>', url, count)


