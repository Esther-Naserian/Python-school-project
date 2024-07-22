from django.shortcuts import render

# Create your views here.
class StudentListView(Apiview):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    def post(self,request):
        serializer =  StudentListView(data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD REQUEST)
class StudentDEtailsView(Apiview):
    def get(self,request,id):
        student= Student.objects.get(id=id)
        serializer= StudentSerializers(student)
        return Response(serializer.data)

class Post(self,request,id):
    student=Student.objects.get(id=id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    serializer.Student,data=requested)
