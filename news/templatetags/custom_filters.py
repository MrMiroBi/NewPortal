from django import template
import re

register = template.Library()

@register.filter()
def censor(value):
    unwanted_words = ["фреймворк", "django"]

    def replace_word(match):
        word = match.group()
        if len(word) > 1:
            return word[0] + '*' * (len(word) - 1)
        return word

    pattern = r'\b(' + '|'.join(re.escape(word) + r'\w*' for word in unwanted_words) + r')\b'

    return re.sub(pattern, replace_word, value, flags=re.IGNORECASE)