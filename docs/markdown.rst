diy-django markdown
===================

Install using pip::

    pip install markdown

Using markdown with django
--------------------------

Set up your models like this::

    from django.utils.safestring import mark_safe
    import markdown


    class MyModel(models.Model):
        content = models.TextField()

        def content_markdown(self):
            return mark_safe(markdown.markdown(self.content))

In your template, render the markdown like so::

    {{ my_object.content_markdown }}
