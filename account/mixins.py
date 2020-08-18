from blog.models import UserProfile


class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            self.fields = ['title', 'cover', 'content', 'category']
        else:
            self.fields = ['title', 'cover', 'content', 'category', 'author']
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            form.instance.author = UserProfile.objects.get(user=self.request.user, )
        return super().form_valid(form)
