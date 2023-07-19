# 📝 UUIDManager - Gerenciador de UUID em Python

![Python Version](https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A classe `UUIDManager` é uma utilitária em Python para lidar com UUIDs (Universally Unique Identifier). Ela fornece funções para gerar UUIDs, verificar sua validade, obter informações sobre a versão e a variante do UUID.

## 🚀 Como usar

### Pré-requisitos

Certifique-se de ter o Python 3.6 ou superior instalado em sua máquina.

### Instalação

Nenhuma instalação adicional é necessária, pois a classe utiliza o módulo `uuid` da biblioteca padrão do Python.

### Exemplo de Uso

```python
from uuid_manager import UUIDManager

# Gerar um novo UUID
my_uuid = UUIDManager.generate_uuid()
print("Generated UUID:", my_uuid)

# Verificar a validade de um UUID
uuid_str = "c3a12449-a52a-4b7a-8f1c-8f432f58f93f"
print("Is valid UUID?", UUIDManager.is_valid_uuid(uuid_str))

# Obter a versão do UUID
print("UUID version:", UUIDManager.get_version(uuid_str))

# Obter a variante do UUID
print("UUID variant:", UUIDManager.get_variant(uuid_str))
```
## 📚 Métodos da Classe

A classe `UUIDManager` possui os seguintes métodos:

#### `generate_uuid()`

Gera e retorna um novo UUID.

#### `is_valid_uuid(uuid_str)`

Verifica se uma string é um UUID válido.

#### `get_version(uuid_str)`

Retorna a versão do UUID (1 para UUID baseado em tempo, 4 para UUID aleatório).

#### `get_variant(uuid_str)`

Retorna a variante do UUID (uma das constantes: RESERVED_NCS, RFC_4122, RESERVED_MICROSOFT ou RESERVED_FUTURE).

