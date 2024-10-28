from rest_framework import serializers
from .models import Product, Order, OrderItem, Category, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductOutSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"


class ProductInSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()
    
    class Meta:
        model = Product
        fields = "__all__"

    def validate_price(self, value): # validate_<название проверяемого поля>
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительной")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Количество товара на складе не может быть отрицательным")
        return value
    
    def create(self, validated_data):
        category_data = validated_data.pop("category_id")

        category, _ = Category.objects.get_or_create(**category_data)

        product = Product.objects.create(category_id=category, **validated_data)
        return product
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop("category_id")

        category, _ = Category.objects.get_or_create(**category_data)

        instance.category_id = category
        instance.name = validated_data["name"]
        instance.description = validated_data["description"]
        instance.price = validated_data["price"]
        instance.stock = validated_data["stock"]
        instance.save()

        return instance


class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    # write_only - поле доступно только для записи
    # read_only - поле доступно только для чтения
    # required - поле обязательно для заполнения
    # default - значение по умолчанию

    class Meta:
        model = Order
        fields = '__all__'

    # когда мы вызываем метод save() у сериализатора он вызывает внутри себя метод
    # create() если у нас нет экземпляра модели или метод update - если у нас есть 
    # экземпляр
    def create(self, validated_data: dict):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        for item_id in items_data:
            product = Product.objects.get(id=item_id)
            OrderItem.objects.create(order_id=order, product_id=product, quantity=1)

        return order

    def update(self, instance: Order, validated_data: dict):
        items_data = validated_data.pop("items")
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        if items_data:
            instance.items.all().delete()
            for item_id in items_data:
                product = Product.objects.get(id=item_id)
                OrderItem.objects.create(order_id=instance, product_id=product, quantity=1)

        return instance
    
    def validate(self, attrs):
        request = self.context.get("request")
        if attrs["profile_id"].user_id != request.user:
            raise serializers.ValidationError("Вы не можете создать заказ за другого пользователя")
        if attrs["status"] == 'completed' and not attrs['items']:
            raise serializers.ValidationError("Нельзя завершить заказ без товаров")
        return attrs


class OrderOutSerializer(serializers.ModelSerializer):
    profile_id = ProfileSerializer()

    class Meta:
        model = Order
        fields = "__all__"


class ProductPriceFilterSerializer(serializers.Serializer):
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    def validate(self, attrs):
        min_price = attrs.get("min_price") # attrs["min_price"] - KeyError
        max_price = attrs.get("max_price")
        if min_price and max_price and min_price > max_price:
            raise serializers.ValidationError("Максимальная цена не может быть меньше минимальной")
        return attrs
