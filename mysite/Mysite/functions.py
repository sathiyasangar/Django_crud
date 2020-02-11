def handle_uploaded_file(f):  
    with open('Mystie/myfile/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  