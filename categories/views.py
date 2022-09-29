from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import GenericAPIView
# Create your views here.

class CategoryAPIView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        projects = Category.objects.all()
        serializer = CategorySerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'category': request.data.get('category'),
            'description': request.data.get('description'),
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(GenericAPIView):
  permission_classes = [permissions.AllowAny]
  serializer_class = CategorySerializer

  def delete(self, request, id, *args, **kwargs):
      if Category.objects.filter(id=id).exists():
        project = Category.objects.get(id=id)
        project.delete()
        return Response({"response":"Category Deleted"}, status=status.HTTP_200_OK)
      else:
          return Response(
              {"res": "Category Doesn't Exists"},
              status=status.HTTP_400_BAD_REQUEST
          )

  def patch(self, request, id, *args, **kwargs):
    if Category.objects.filter(id=id).exists():
      category = Category.objects.get(id=id)
      data = {
      'category': request.data.get('category'),
      'description': request.data.get('description'),
      }
      serializer = CategorySerializer(instance = category, data=data, partial = True)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
                {"res": "Category Doesn't Exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
