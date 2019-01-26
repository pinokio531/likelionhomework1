from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() #공백기준으로 나눠줌, list임
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary:
            #증가
            word_dictionary[word]+=1 #키를 문자열로 바꿈 , 인덱스에서

        else:
            #생성
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full' : text, 'total' :len(words), 'dictionary' :word_dictionary.items()})