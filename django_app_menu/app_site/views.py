from django.views.generic import TemplateView

class home_detail(TemplateView):
    template_name = 'home-page.html'

class page_detail(TemplateView):
    template_name = 'site-page.html'

