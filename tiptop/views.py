from django.shortcuts import render, redirect

def home(request):
    return render(request, 'submission_form.html')


def submission(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['loc'] = request.POST['location']
        print('Your form has been processed')
        return redirect('/result')
        


def result(request):

    # context = {
    #     'name': request.session['name'],
    #     'lang': request.session['language'],
    #     'loc': request.session['loc']
    # }
    return render(request, 'result.html')