from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Movie
from .serializers import MovieSerializer


class MovieAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'genre': request.data.get('genre'),
        }
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def delete(self, request, id, *args, **kwargs):
      if Movie.objects.filter(id=id).exists():
        movie = Movie.objects.get(id=id)
        movie.delete()
        return Response({"response":"Movie Deleted"}, status=status.HTTP_200_OK)
      else:
          return Response(
              {"res": "Movie Doesn't Exists"},
              status=status.HTTP_400_BAD_REQUEST
          )

  def patch(self, request, id, *args, **kwargs):
    if Movie.objects.filter(id=id).exists():
      movie = Movie.objects.get(id=id)
      data = {
      'title': request.data.get('title'),
      'description': request.data.get('description'),
          'genre': request.data.get('genre'),
      }
      serializer = MovieSerializer(instance = movie, data=data, partial = True)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
                {"res": "Movie Doesn't Exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
