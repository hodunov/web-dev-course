import string
from django import template
from core.models import Teacher


register = template.Library()


@register.filter
def get_even_numbers(list_value):
    """
    This function returns the resulting list, which contains only even numbers.
    """
    return [num for num in list_value if not num % 2]


@register.filter
def count_words(str_value):
    """
    This function counts the number of words in the passed string
    """
    return sum(word.strip(string.punctuation).isalpha() for word in str_value.split())


@register.inclusion_tag('includes/random_teachers.html')
def random_teachers(select=5):
    """

    """
    selected_teachers = Teacher.objects.all().order_by('?')[:select]
    return {'teachers': selected_teachers}
