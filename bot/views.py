from django.shortcuts import render
import markdown

# Create your views here.
from django.http import JsonResponse, HttpResponse
from bardapi import Bard

token = 'ZAgXXuGFh4-pARuj0XWe36RkTUppCJa5PsW05a3VI3RdtGU9hmTBeJQutRATaDSmiFc4Og.'
bard = Bard(token=token)
maxs=4
def chat(request):
    print(request.POST)
    if request.method == 'POST':
        user_message = request.POST['message']
        bot_response = bard.get_answer(user_message)['content']
        print(str(markdown.markdown(str(bot_response))))
        return JsonResponse({'bot_response': str(markdown.markdown(str(bot_response)))})

def index(request):
    return HttpResponse(render(request, 'index4.html'))