from utils.uuid_manager import UUIDManager

if __name__ == "__main__":
    my_uuid = UUIDManager.generate_uuid()
    print("Generated UUID:", my_uuid)

    uuid_str = "c3a12449-a52a-4b7a-8f1c-8f432f58f93f"
    print("Is valid UUID?", UUIDManager.is_valid_uuid(uuid_str))

    print("UUID version:", UUIDManager.get_version(uuid_str))

    print("UUID variant:", UUIDManager.get_variant(uuid_str))

