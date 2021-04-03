from django.shortcuts import render
from .forms import UserRegisterForm, MyProfileForm, MyAddressProfileForm, MyShopForm
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import User, Address , Shop
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect#, render_to_response
from Products import models as products_models
from django.contrib import messages

# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your views here.


class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'your profile was created successfully'


class LogIn(LoginView):
    template_name = 'registration/login.html'


class LogOut(LogoutView):
    template_name = 'registration/logout.html'


class Profile(LoginRequiredMixin, DetailView):
    #loginRequiredMixin is for login required
    # model = User  #in below we define the "get_object", so we did not get the model hear
    template_name = 'profile/profile.html'
    # success_url = reverse_lazy('profile')
    # form_class = MyProfileForm 
    # second_form_class = MyAddressProfileForm


    # #for exclude to superusers to limit the edit of special profile items we need make the new 'kwargs'
    # def get_form_kwargs(self):
    #     kwargs = super(Profile, self).get_form_kwargs()
    #     kwargs.update({
    #         'user': self.request.user
    #     })
    #     return kwargs

    #for limited user to access another users profile we can do this or use 'LoginRequiredMixin'
    #now we did not use pk for address the profile page of logined user and did not use pk for url
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = products_models.Category.objects.all()
        # if 'form' not in context:
        #     context['form'] = self.form_class()
        # if 'form2' not in context:
        #     context['form2'] = self.second_form_class(self.request.GET, instance= self.request.user)
        return context


# def profile(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})


class PersonalDetailEdit(LoginRequiredMixin, UpdateView):
    template_name = 'profile/personal_detail_edit.html'
    success_url = reverse_lazy('profile')
    form_class = MyProfileForm 

    #for limited user to access another users profile we can do this or use 'LoginRequiredMixin'
    #now we did not use pk for address the profile page of logined user and did not use pk for url
    def get_object(self):
        return self.request.user

    #for exclude to superusers to limit the edit of special profile items we need make the new 'kwargs'
    def get_form_kwargs(self):
        kwargs = super(PersonalDetailEdit, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class PersonalAddressEdit(LoginRequiredMixin, UpdateView):
    # model = Address
    template_name = 'profile/personal_address_edit.html'
    success_url = reverse_lazy('profile')
    form_class = MyAddressProfileForm 

    #for limited user to access another users profile we can do this or use 'LoginRequiredMixin'
    #now we did not use pk for address the profile page of logined user and did not use pk for url
    def get_object(self, queryset=None):
        return get_object_or_404(Address, user=self.request.user, name=self.kwargs.get('name'))
        # print('id is: ', self.kwargs['id'])
        # return Address.objects.get(pk=self.kwargs.get('pk'))
        # return get_object_or_404(Address, pk=self.kwargs.get('pk')) # or request.POST

    # #for exclude to superusers to limit the edit of special profile items we need make the new 'kwargs'
    # def get_form_kwargs(self):
    #     kwargs = super(PersonalDetailEdit, self).get_form_kwargs()
    #     kwargs.update({
    #         'user': self.request.user
    #     })
    #     return kwargs


def remove_address(request, id):
    address_item = Address.objects.get(id = id)
    address_item.delete()
    #print(address_item[0].quantity)
    messages.info(request, 'این آدرس حذف شد')
    return redirect('profile')


class CreateNewAddress(LoginRequiredMixin, CreateView):
    form_class = MyAddressProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'profile/create_new_address.html'
    # success_message = 'your profile was created successfully'

    # for auto add the user_id field
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNewAddress, self).form_valid(form)


class CreateShop(LoginRequiredMixin, CreateView):
    form_class = MyShopForm
    success_url = reverse_lazy('profile')
    template_name = 'shop/create_shop.html'
    # success_message = 'your profile was created successfully'

    # for auto add the user_id field
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateShop, self).form_valid(form)


class UpdateShop(LoginRequiredMixin, UpdateView):
    # model = Address
    template_name = 'shop/update_shop.html'
    success_url = reverse_lazy('profile')
    form_class = MyShopForm 

    #for limited user to access another users profile we can do this or use 'LoginRequiredMixin'
    #now we did not use pk for address the profile page of logined user and did not use pk for url
    def get_object(self, queryset=None):
        return get_object_or_404(Shop, user=self.request.user)