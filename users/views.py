from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response




class UserDetailView(APIView):

    def post(self, request, format=None):
        """
        Return a user detail data.
        """
        
        name = request.POST.get('name')
        print(name)

        if not name:
            return Response("Please enter name", status=status.HTTP_400_BAD_REQUEST)

        email = name.replace(" ", "").lower()
        
        user_detail = {
            "name" : "Hi "+name,
            "email" : email+"@gmail.com"
        }

        return Response(user_detail, status=status.HTTP_200_OK)