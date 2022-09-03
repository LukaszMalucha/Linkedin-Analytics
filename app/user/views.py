from rest_framework.views import APIView
from rest_framework.response import Response


class CurrentUserView(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            return Response({"email": request.user.email })
        else:
            return Response({"error": "Anonymous"})
