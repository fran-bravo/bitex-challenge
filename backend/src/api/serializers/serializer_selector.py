from src.api.exceptions.unknown_serializer_exception import UnknownSerializerException


class SerializerSelector:

    def __init__(self, **serializers):
        self.serializers = serializers

    def __setitem__(self, serializer_type, serializer):
        self.serializers[serializer_type] = serializer

    def __getitem__(self, serializer_type):
        if serializer_type in self.serializers.keys():
            return self.serializers[serializer_type]
        else:
            raise UnknownSerializerException(f"Could not find serializer for {serializer_type}")
