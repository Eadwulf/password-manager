from django.views import View
from django.shortcuts import render, redirect


class CreateViewMixin(View):
    
    form_class = None
    template_name = ''

    def get(self, request):

        if request.user.is_anonymous:
            return render(request, 'authentication/unauthorized_access.html')
        
        context = {
            'form': self.form_class(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.user.is_anonymous:
            return render(request, 'authentication/unauthorized_access.html')

        form = self.form_class(request.POST)
        if form.is_valid():
            new_object = form.save()
            return redirect(new_object)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)