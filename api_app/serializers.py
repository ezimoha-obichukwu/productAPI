from rest_framework import serializers
from product.models import Product




# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         # fields = ["title", "content", "author", "date_posted"]
#         fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "price", "description", "category"]
        # fields = "__all__"

