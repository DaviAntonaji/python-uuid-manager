import uuid

class UUIDManager:
    @staticmethod
    def generate_uuid():
        """Gera e retorna um novo UUID."""
        return str(uuid.uuid4())

    @staticmethod
    def is_valid_uuid(uuid_str):
        """Verifica se uma string é um UUID válido."""
        try:
            uuid.UUID(uuid_str)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_version(uuid_str):
        """Retorna a versão do UUID (1 para UUID baseado em tempo, 4 para UUID aleatório)."""
        try:
            uuid_obj = uuid.UUID(uuid_str)
            return uuid_obj.version
        except ValueError:
            return None

    @staticmethod
    def get_variant(uuid_str):
        """Retorna a variante do UUID (uma das constantes: RESERVED_NCS, RFC_4122, RESERVED_MICROSOFT, RESERVED_FUTURE)."""
        try:
            uuid_obj = uuid.UUID(uuid_str)
            return uuid_obj.variant
        except ValueError:
            return None


