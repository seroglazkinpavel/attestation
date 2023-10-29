from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib import messages
from blog.forms import AddRecipeForm
from blog.models import Recipe, Category

from django.views.generic.edit import FormView, CreateView, UpdateView

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Отзывы", 'url_name': 'reviews'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Статьи", 'url_name': 'articles'}
]


class RecipeHome(ListView):
    model = Recipe
    template_name = 'blog/index.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Recipe.objects.order_by("?")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


class AddRecipe(CreateView):
    form_class = AddRecipeForm
    template_name = 'blog/addpecipe.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление рецепта'
        context['menu'] = menu
        return context


class NewsUpdateRecipe(UpdateView):
    form_class = AddRecipeForm
    template_name = 'blog/updatepecipe.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(NewsUpdateRecipe, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление рецепта'
        context['menu'] = menu
        return context


class RecipeCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'products'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Recipe.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        #ancestors = category.get_ancestors()
        # context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['title'] = category
        #context['ancestors'] = ancestors
        context['menu'] = menu
        return context


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О нас'})


def news(request):
    return HttpResponse('Новости')


def reviews(request):
    return HttpResponse('Отзывы')


def contacts(request):
    return HttpResponse('Контакты')


def articles(request):
    return HttpResponse('Статьи')


class ShowProduct(DetailView):
    model = Recipe
    template_name = 'blog/product.html'
    slug_url_kwarg = 'rec_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product']
        context['menu'] = menu
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Recipe.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['title'] = 'Поиск'
        context['menu'] = menu
        return context


class Office(ListView):
    model = Recipe
    template_name = 'blog/office.html'
    context_object_name = 'products'
    #paginate_by = 4

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш кабинет'
        context['menu'] = menu
        return context
