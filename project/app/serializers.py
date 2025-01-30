from rest_framework import serializers
from .models import Janr, Book
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=200)
    year = serializers.IntegerField()
    janr_id = serializers.IntegerField()


def serlization():
    book = Book.objects.all(pk=1)
    serializer = BookSerializer(book)

    json = JSONRenderer().render(serializer.data)
    print(json)


def deserlization():
    json = b""
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    print(data)

    serializer = BookSerializer(data=data)
    serializer.is_valid(raise_exception=True)


def update(self, instance, validated_data):
    instance.name = validated_data.get("name", instance.name)
    instance.author = validated_data.get("author", instance.author)
    instance.year = validated_data.get("year", instance.year)
    instance.janr_id = validated_data.get("janr_id", instance.janr_id)
    instance.save()
    return instance
