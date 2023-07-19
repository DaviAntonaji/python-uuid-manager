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

# Exemplo de uso:
if __name__ == "__main__":
    my_uuid = UUIDManager.generate_uuid()
    print("Generated UUID:", my_uuid)

    uuid_str = "c3a12449-a52a-4b7a-8f1c-8f432f58f93f"
    print("Is valid UUID?", UUIDManager.is_valid_uuid(uuid_str))

    print("UUID version:", UUIDManager.get_version(uuid_str))

    print("UUID variant:", UUIDManager.get_variant(uuid_str))

