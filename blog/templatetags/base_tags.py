from django import template

register = template.Library()


@register.inclusion_tag("registration/partials/active_sidebar.html")
def active_sidebar(request, link_name, content,ic_name):
    return {
        "requset": request,
        "link_name": link_name,
        "content": content,
        "ic_name": ic_name,
        "link": "account:{}".format(link_name),
    }
