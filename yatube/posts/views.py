from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
            'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
            'если у тебя нет правильных <s>вопросов</s> запросов.')


def group_posts(request, slug):
    return HttpResponse(f'Запрос на группу {slug}')
