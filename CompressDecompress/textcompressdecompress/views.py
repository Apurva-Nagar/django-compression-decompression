from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .huff import main


class Home(TemplateView):
	template_name = 'textcompressdecompress/index.html'


def text_file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        try:
            request.POST['compress']
            mode = 'compress'
            #print('MODE = COMPRESS')
        except:
            try:
                request.POST['decompress']
                mode = 'decompress'
                #print('MODE = DECOMPRESS')
            except:
                mode = None
                #print('ERROR: NO MODE')

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        BASE_FILE_URL = '/mnt/c/Users/apurv/Documents/Programming/DjangoCompressDecompress/CompressDecompress'
        mode_error = False
        output_path = None
        if mode is None:
            mode_error = True
        else:
            print(BASE_FILE_URL+uploaded_file_url)
            output_path = main(mode, BASE_FILE_URL + uploaded_file_url)
            print(output_path)

        return render(request, 'textcompressdecompress/index.html', {
            'uploaded_file_url': uploaded_file_url, 
            'mode_error': mode_error,
            'output_path': output_path
        })
    return render(request, 'textcompressdecompress/index.html')


