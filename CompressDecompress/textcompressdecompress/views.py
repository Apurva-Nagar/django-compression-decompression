from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .huff import main


class Home(TemplateView):
	template_name = 'textcompressdecompress/index.html'


def text_file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        try:
            mode = request.POST['mode']
        except:
            mode = None

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        extension = uploaded_file_url.split('.')[-1] 

        BASE_FILE_URL = '/mnt/c/Users/apurv/Documents/Programming/DjangoCompressDecompress/CompressDecompress'
        
        mode_error = True if mode is None else False 
        ext_error = False if extension == 'txt' or extension == 'bin' else True
        error = True if mode_error or ext_error else False

        output_path = None if error else main(mode, BASE_FILE_URL + uploaded_file_url)

        return render(request, 'textcompressdecompress/index.html', {
            'uploaded_file_url': uploaded_file_url, 
            'error': error,
            'mode_error': mode_error,
            'ext_error': ext_error,
            'output_path': output_path,
        })
    return render(request, 'textcompressdecompress/index.html')


