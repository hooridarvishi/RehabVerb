# # from django.shortcuts import render
# #
# # # Create your views here.
# # from django.shortcuts import render, get_object_or_404
# # from django.http import JsonResponse
# # from .models import Card
# #
# # def home(request):
# #     cards = Card.objects.all()[:4]
# #     return render(request, 'home.html', {'cards': cards})
# #
# # def card_detail(request, card_id, page_number):
# #     card = get_object_or_404(Card, pk=card_id)
# #     template_name = f'pages/page_{page_number}.html'
# #     return render(request, template_name, {'card': card})
# #
# # def toggle_image(request, card_id):
# #     if request.method == 'POST':
# #         return JsonResponse({'success': True})
# #     return JsonResponse({'success': False})
# #
# # def toggle_text(request, card_id, field_type):
# #     if request.method == 'POST':
# #         return JsonResponse({'success': True})
# #     return JsonResponse({'success': False})
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from .models import Card
#
#
# def home(request):
#     cards = Card.objects.all()[:4]
#     return render(request, 'home.html', {'cards': cards})
#
#
# def card_detail(request, card_id, page_number):
#     card = get_object_or_404(Card, pk=card_id)
#
#     # تعیین متن صفحه بعدی برای دکمه
#     page_next = page_number + 1
#     page_next_text = convert_to_persian_text(page_next)
#
#     context = {
#         'card': card,
#         'page_number': page_number,
#         'page_next': page_next,
#         'page_next_text': page_next_text
#     }
#
#     template_name = f'pages/page_{page_number}.html'
#     return render(request, template_name, context)
#
#
# def convert_to_persian_text(number):
#     persian_numbers = {
#         1: 'اول',
#         2: 'دوم',
#         3: 'سوم',
#         4: 'چهارم',
#         5: 'پنجم',
#         6: 'ششم',
#         7: 'هفتم',
#         8: 'هشتم',
#         9: 'نهم',
#         10: 'دهم',
#         11: 'یازدهم',
#         12: 'دوازدهم',
#         13: 'سیزدهم',
#         14: 'چهاردهم',
#         15: 'پانزدهم',
#         16: 'شانزدهم',
#         17: 'هفدهم',
#         18: 'هجدهم',
#         19: 'نوزدهم',
#         20: 'بیستم',
#         21: 'بیست و یکم',
#         22: 'بیست و دوم',
#         23: 'بیست و سوم'
#     }
#     return persian_numbers.get(number, str(number))
#
#
# def toggle_image(request, card_id):
#     if request.method == 'POST':
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})
#
#
# def toggle_text(request, card_id, field_type):
#     if request.method == 'POST':
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def template_view(request):
    template = TextTemplate.objects.first()
    return render(request, 'pages/page_6.html', {'template': template})


@csrf_exempt
def update_blank(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        template = TextTemplate.objects.first()
        blank_number = data.get('blank_number')
        text = data.get('text')

        if blank_number == 1:
            template.blank1_text = text
        elif blank_number == 2:
            template.blank2_text = text
        elif blank_number == 3:
            template.blank3_text = text

        template.save()
        return JsonResponse({'status': 'success'})

def home(request):
    cards = Card.objects.all()[:40]
    return render(request, 'home.html', {'cards': cards})


def card_detail(request, card_id, page_number):
    card = get_object_or_404(Card, pk=card_id)

    # تعیین متن صفحه بعدی برای دکمه
    page_next = page_number + 1
    page_next_text = convert_to_persian_text(page_next)

    context = {
        'card': card,
        'page_number': page_number,
        'page_next': page_next,
        'page_next_text': page_next_text
    }

    template_name = f'pages/page_{page_number}.html'
    return render(request, template_name, context)


def convert_to_persian_text(number):
    persian_numbers = {
        1: 'اول',
        2: 'دوم',
        3: 'سوم',
        4: 'چهارم',
        5: 'پنجم',
        6: 'ششم',
        7: 'هفتم',
        8: 'هشتم',
        9: 'نهم',
        10: 'دهم',
        11: 'یازدهم',
        12: 'دوازدهم',
        13: 'سیزدهم',
        14: 'چهاردهم',
        15: 'پانزدهم',
        16: 'شانزدهم',
        17: 'هفدهم',
        18: 'هجدهم',
        19: 'نوزدهم',
        20: 'بیستم',
        21: 'بیست و یکم',
        22: 'بیست و دوم',
        23: 'بیست و سوم'
    }
    return persian_numbers.get(number, str(number))


def toggle_image(request, card_id):
    if request.method == 'POST':
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def toggle_text(request, card_id, field_type):
    if request.method == 'POST':
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})