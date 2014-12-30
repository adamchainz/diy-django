diy-django ajax file upload progress widget
===========================================

The Field, Widget, and Javascript
---------------------------------

Create an UploadField and UploadWidget like this::

    from django.forms import fields, widgets
    from django.utils.safestring import mark_safe


    class UploadWidget(widgets.TextInput):

        def render(self, name, value, attrs=None):
            attrs = attrs or {}
            attrs['class'] = 'vTextField'
            input = super(UploadWidget, self).render(name, value, attrs=attrs)
            value = ('<a href="%s" target="_blank">view</a>' % value.url) if hasattr(value, 'url') else value
            onchange = r'''
    f = this.files[0]
    this.value = ''
    var xhr = new XMLHttpRequest()
    xhr.open('POST', '/simple_upload/' + f.name, true)
    xhr.setRequestHeader('X-CSRFToken', this.form.csrfmiddlewaretoken.value)
    xhr.upload.status = this.parentNode.firstChild.nextElementSibling // <span>
    xhr.upload.status.innerHTML = 'pending...'
    xhr.upload.onprogress = function(e){ this.status.innerHTML = Math.round(100 * e.loaded / e.total) + '% uploaded' }
    xhr.send(f)
    xhr.onload = function(){
      this.upload.status.innerHTML = '<a href=\'/media/' + encodeURI(this.responseText) + '\' target=_blank>view</a>'
      this.upload.status.previousElementSibling.value = this.responseText // <input type=hidden>
    }'''
            assert '"' not in onchange
            return mark_safe('<p>%s<span>%s</span><br><input type="file" onchange="%s" value="upload"></p>' % (input, value, onchange))


    class UploadField(fields.CharField):
        widget = UploadWidget

The backend view to receive the file upload
-------------------------------------------

In views.py::

    from django.contrib.admin.views.decorators import staff_member_required
    from django.core.files.base import ContentFile
    from django.core.files.storage import default_storage
    from django.http import HttpResponse


    @staff_member_required
    def simple_upload(request, name):
        return HttpResponse(default_storage.save(name, ContentFile(request.body)), 'text/plain')

In urls.py::

    from . import views
    urlpatterns = [
        url(r'^simple_upload/$', views.simple_upload),
    ]

Using the FileUpload field in the admin
---------------------------------------

In admin.py::
    
    class MyAdmin(admin.ModelAdmin):
        formfield_overrides = {models.FileField: {'form_class': UploadField}}
