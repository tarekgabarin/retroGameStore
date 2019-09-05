from games.models import Game
from rest_framework import viewsets, permissions
from .serializers import GameSerializer

# Game Viewset

class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = GameSerializer
