# Archivos de configuración

https://www.barenakedcoder.com/blog/2020/03/config-files-ini-xml-json-yaml-toml/


# YAML
YAML (YAML Ain’t Markup Language) es un formato de serialización de datos legible por humanos, usado para configurar aplicaciones o almacenar información estructurada.

- Propósito: Facilitar la lectura y escritura de datos complejos (listas, diccionarios, anidados) de forma clara y sencilla.

- Sintaxis: Basada en sangrías, sin llaves ni corchetes, con guiones para listas y dos puntos para pares clave-valor.

- Uso actual: Muy común en configuración de aplicaciones, despliegues (Docker, Kubernetes), pipelines de CI/CD y scripts de automatización.

- Historia: Apareció en 2001 como alternativa más legible que XML o JSON, enfocada en simplicidad y claridad.

Config.yaml

```yaml
database:
  host: localhost
  port: 5432
  user: admin
  password: secret

features:
  enable_logging: true
  max_connections: 10
```

```bash
pip install pyyaml
```

```python
import yaml

# Load the YAML file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Access values
print(config['database']['host'])        # localhost
print(config['features']['enable_logging'])  # True
```


# JSON como config

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "secret"
  },
  "features": {
    "enable_logging": true,
    "max_connections": 10
  }
}
```

```python
import json

with open("config.json", "r") as f:
    config = json.load(f)

print(config['database']['host'])         # localhost
print(config['features']['enable_logging'])  # True
```