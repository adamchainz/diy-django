diy-django markdown
===================

Install using pip::

    pip install markdown

Using markdown with django models
---------------------------------

Set up your models like this::

    from django.utils.safestring import mark_safe
    import markdown


    class MyModel(models.Model):
        content = models.TextField()

        def content_markdown(self):
            return mark_safe(markdown.markdown(self.content))

In your template, render the markdown like so::

    {{ my_object.content_markdown }}


Using markdown with django template tags
----------------------------------------

An alternative is to use a markdown templatetag::

    from django import template
    register = template.Library()

    @register.filter
    def markdown(value):
        import markdown
        return markdown.markdown(value)
    markdown.is_safe = True

This can be used in a template like so::

    {{ my_object.content|markdown }}
