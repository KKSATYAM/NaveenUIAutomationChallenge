from django.http import HttpResponse

class FirstMiddleWare(object):

    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print("Pre Processing First Middleware")
        response=self.get_response(request)
        print("Post Processing First Middleware")
        response=HttpResponse("Response from 1st middleware")
        return response

    def process_exception(self,request,exception):
        return HttpResponse(f"<h1>Exception raised:: {exception.__class__.__name__}, pls wait we are fixing it for you</h1>")
    

class SecondMiddleWare(object):

    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print("Pre Processing Second Middleware")
        response=self.get_response(request)
        print("Post Processing Second Middleware")
        
        response=HttpResponse("<h1>Response from 2nd middleware</h1>")
        return response

    def process_exception(self,request,exception):
        return HttpResponse(f"<h1>Exception raised:: {exception.__class__.__name__}, pls wait we are fixing it for you</h1>")
    