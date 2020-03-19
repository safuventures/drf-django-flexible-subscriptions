from rest_framework import serializers

from subscriptions import models

from .models import PlanCost, UserSubscription


class PlanTagSerializer(serializers.ModelSerializer):
    """Serializer for PlanTag model"""

    class Meta:
        model = models.PlanTag
        fields = '__all__'


class PlanCostSerializer(serializers.ModelSerializer):
    """PlanCost model serializer with property fields  exposed as serializer method fields"""
    recurrent_unit_text = serializers.SerializerMethodField()
    billing_frequency_text = serializers.SerializerMethodField()

    def get_recurrent_unit_text(self, obj):
        return obj.display_recurrent_unit_text

    def get_billing_frequency_text(self, obj):
        return obj.display_billing_frequency_text

    class Meta:
        model = PlanCost
        fields = '__all__'


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    """Serializer for SubscriptionPlan model and Tags can be created directly on it"""

    tags = PlanTagSerializer(many=True, read_only=True)
    tags_str = serializers.SerializerMethodField()
    costs = PlanCostSerializer(many=True, read_only=True)

    def get_tags_str(self, obj):
        return obj.display_tags()

    class Meta:
        model = models.SubscriptionPlan
        fields = '__all__'


class UserSubscriptionSerializer(serializers.ModelSerializer):
    """User subscription model serializer"""

    class Meta:
        model = UserSubscription
        fields = '__all__'


class SubscriptionTransactionSerializer(serializers.ModelSerializer):
    """SubscriptionTransaction serializer"""

    class Meta:
        model = models.SubscriptionTransaction
        fields = '__all__'


class PlanListSerializer(serializers.ModelSerializer):
    """PlanList serializer"""

    class Meta:
        model = models.PlanList
        fields = '__all__'


class PlanListDetailSerializer(serializers.ModelSerializer):
    """PlanListDetail serializer"""

    class Meta:
        model = models.PlanListDetail
        fields = '__all__'