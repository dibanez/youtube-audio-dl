import re
from unicodedata import normalize

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')

def slugify(text, delim=u'-'):
    """
    Slugifies a string.

    This is slightly different from the built-in one in Django.

    Source: http://stackoverflow.com/questions/9042515/normalizing-unicode-\
        text-to-filenames-etc-in-python
    """
    result = []

    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        word = word.decode('utf-8')
        if word:
            result.append(word)
    return delim.join(result)


def get_client_ip(request):
    """
    Retrieve the client's IPv4 address from the request object.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
