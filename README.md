# Automatización de Excel y Login Web con Playwright

## Descripción

Este proyecto automatiza el siguiente flujo:

1. Abre un archivo Excel.
2. Ejecuta una prueba de Login en una página web utilizando Playwright.
3. Obtiene el resultado de la prueba.
4. Escribe el resultado dentro del archivo Excel.
5. Guarda una copia del archivo en una nueva ubicación.
6. Cierra Excel automáticamente.

---

## Tecnologías utilizadas

- Python 3.12+
- PDM
- Playwright
- UIAutomation

---

## Instalación de PDM

Abrir PowerShell o CMD como administrador:

```powershell
pip install pipx
pipx install pdm
pipx ensurepath
```

Verificar instalación:

```powershell
pdm --version
```

---

## Descargar el proyecto

1. Descargar el archivo `.zip`.
2. Descomprimirlo en la carpeta deseada.
3. Abrir una terminal en la carpeta del proyecto.

Ejemplo:

```powershell
cd "C:\Users\Usuario\Desktop\PRUEBA"
```

Inicializar el entorno:

```powershell
pdm init
```

---

## Instalar dependencias

```powershell
pdm install
```

Si las dependencias no existen:

```powershell
pdm add playwright
pdm add uiautomation
```

---

## Verificar estructura de carpetas

Antes de ejecutar el programa, verificar que exista el archivo Excel de entrada:

```text
data/
├── input/
│   └── prueba.xlsx
│
└── output/
```

Si la carpeta `output` no existe, debe crearse manualmente.

El archivo:

```text
prueba.xlsx
```

debe colocarse dentro de:

```text
data/input/
```

ya que será utilizado por la automatización para registrar el resultado de la prueba.

### Importante

Si el archivo Excel fue descargado de Internet, se recomienda:

1. Abrir `prueba.xlsx`.
2. Habilitar edición si Excel lo solicita.

Si el archivo continúa presentando problemas, eliminarlo y crear un nuevo archivo Excel vacío con el mismo nombre:

```text
prueba.xlsx
```

---

## Estructura del proyecto

```text
PRUEBA/
│
├── data/
│   ├── input/
│   │   └── prueba.xlsx
│   │
│   └── output/
│
├── src/
│   └── proyecto/
│       └── main.py
│
├── pyproject.toml
└── README.md
```

---

## Ejecución

Desde la raíz del proyecto:

```powershell
pdm run python src/proyecto/main.py
```

---

## Resultado esperado

El sistema:

- Abre Excel.
- Realiza Login en la página de pruebas.
- Escribe el resultado en Excel.
- Guarda una copia en:

```text
data/output/modificado1.xlsx
```

- Cierra Excel.
- Finaliza la ejecución.

---

## Consideraciones

Si se desean realizar más pruebas, tener en cuenta que el archivo:

```text
modificado1.xlsx
```

ya existe en la carpeta `output`.

Antes de una nueva ejecución se recomienda:

- Eliminar el archivo anterior.
- O cambiarle el nombre.

Esto evitará conflictos durante el guardado.

---

## Credenciales utilizadas

```text
Usuario: student
Contraseña: Password123
```

---

## Página utilizada para la prueba

https://practicetestautomation.com/practice-test-login/
