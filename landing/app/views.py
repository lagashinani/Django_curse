from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    counter_click[from_landing] += 1
    return render(request, 'index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    counter_show[ab_test_arg] += 1
    if ab_test_arg == 'test':
        return render(request, 'landing_alternate.html')
    return render(request, 'landing.html')


def stats(request):
    return render(request, 'stats.html', context={
        'test_conversion': counter_click['test']/counter_show['test'],
        'original_conversion': counter_click['original']/counter_show['original'],
    })
