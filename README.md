# 🎵 YouTube Music Setup Simulator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows-lightgrey?style=for-the-badge&logo=windows&logoColor=white)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Educativo-orange?style=for-the-badge)
![Ético](https://img.shields.io/badge/Uso-Educativo%20Únicamente-red?style=for-the-badge)

*Un simulador GUI sofisticado que recrea la experiencia auténtica de instalación de YouTube Music*

**⚠️ PROYECTO EXCLUSIVAMENTE EDUCATIVO - FINES DE INVESTIGACIÓN EN SEGURIDAD ⚠️**

</div>

---

## 🎯 Descripción General

El **YouTube Music Setup Simulator** es una aplicación Python meticulosamente diseñada que reproduce con precisión la interfaz de instalación de software profesional. Este proyecto ha sido desarrollado **exclusivamente con fines educativos** para demostrar técnicas de ingeniería social, análisis de seguridad y comprensión de vectores de ataque comunes en ciberseguridad.

### 🎓 **Propósito Educativo**
Este simulador está diseñado para:
- **Investigación en Ciberseguridad** - Análisis de técnicas de ingeniería social
- **Educación en Seguridad Informática** - Demostración de vectores de ataque comunes
- **Desarrollo de Defensas** - Comprensión de métodos de phishing y social engineering
- **Concienciación de Usuarios** - Educación sobre identificación de software malicioso

## 🚨 AVISO LEGAL IMPORTANTE

### ⚖️ **Disclaimer Legal Completo**

**ESTE SOFTWARE SE PROPORCIONA "TAL COMO ESTÁ" Y ÚNICAMENTE CON FINES EDUCATIVOS**

#### **Términos de Uso Obligatorios:**

1. **USO EXCLUSIVAMENTE EDUCATIVO**: Este proyecto está diseñado únicamente para fines de investigación, educación en ciberseguridad y concienciación sobre seguridad informática.

2. **PROHIBICIÓN DE USO MALICIOSO**: Queda ESTRICTAMENTE PROHIBIDO el uso de este software para:
   - Actividades ilegales o maliciosas
   - Distribución de malware real
   - Engaño o fraude a usuarios
   - Violación de términos de servicio
   - Cualquier actividad que cause daño

3. **RESPONSABILIDAD DEL USUARIO**: El usuario es COMPLETAMENTE RESPONSABLE del uso de este software y debe:
   - Cumplir con todas las leyes locales, nacionales e internacionales
   - Obtener permisos explícitos antes de cualquier demostración
   - Usar únicamente en entornos controlados y autorizados
   - No distribuir sin las advertencias apropiadas

4. **EXENCIÓN DE RESPONSABILIDAD**: Los desarrolladores NO se hacen responsables de:
   - Uso indebido del software
   - Daños directos o indirectos resultantes del uso
   - Violaciones legales cometidas por terceros
   - Mal uso en entornos no autorizados

5. **CUMPLIMIENTO LEGAL**: El uso de este software debe cumplir con:
   - Leyes de ciberseguridad locales
   - Regulaciones de protección de datos (GDPR, CCPA, etc.)
   - Términos de servicio de plataformas
   - Códigos éticos de investigación en seguridad

#### **Advertencias Específicas:**
- ⚠️ **NO** usar en sistemas de terceros sin autorización explícita
- ⚠️ **NO** distribuir como software legítimo
- ⚠️ **NO** modificar para propósitos maliciosos
- ⚠️ **NO** usar para obtener acceso no autorizado

### 🔒 **Uso Ético y Responsable**

Este proyecto sigue los principios de **Divulgación Responsable** y **Hacking Ético**:
- Transparencia total en el código fuente
- Documentación clara de propósitos educativos
- Advertencias prominentes sobre uso apropiado
- Colaboración con la comunidad de ciberseguridad

---

## ✨ Características Técnicas

### 🎨 **Interfaz Visual Avanzada**
- **Tema Oscuro Moderno** - Interfaz sofisticada con branding de YouTube Music
- **Diseño Auténtico** - Recreación pixel-perfect de interfaces de instalación reales
- **Animaciones Fluidas** - Transiciones suaves con temporización realista
- **Diseño Responsivo** - Ventana centrada y no redimensionable

### ⚡ **Funcionalidades Técnicas**
- **Simulación de Progreso Dinámica** - Seguimiento inteligente de progreso 0% a 100%
- **Mensajes Contextuales** - Actualizaciones realistas de estado de instalación
- **Control de Procesos** - Experiencia controlada con controles de ventana deshabilitados
- **Finalización Automática** - Terminación elegante con confirmación de éxito

### 🛡️ **Características Profesionales**
- **Integración Administrativa** - Elevación fluida para operaciones a nivel de sistema
- **Manejo de Errores** - Gestión robusta de errores y recuperación
- **Soporte Multi-Biblioteca** - Diseño modular con componentes opcionales
- **Integración Webhook** - Capacidades opcionales de monitoreo remoto

## 📋 Requisitos del Sistema

### **Especificaciones Mínimas**
| Componente | Especificación |
|-----------|----------------|
| **Sistema Operativo** | Windows 7/8/10/11 (x64) |
| **Versión Python** | 3.7+ (recomendado: 3.9+) |
| **Memoria RAM** | 512 MB mínimo |
| **Espacio en Disco** | 100 MB disponible |
| **Privilegios** | Administrador (recomendado) |

### **Especificaciones Recomendadas**
| Componente | Especificación |
|-----------|----------------|
| **Sistema Operativo** | Windows 10/11 (x64) |
| **Versión Python** | 3.10+ |
| **Memoria RAM** | 2 GB o más |
| **Espacio en Disco** | 500 MB disponible |
| **Conexión Internet** | Banda ancha (para webhooks) |

## 📦 Dependencias y Bibliotecas

### **Bibliotecas Principales (Obligatorias)**
```bash
# Componentes esenciales (auto-instalados con Python)
tkinter                 # Framework GUI principal
os                     # Operaciones del sistema operativo
sys                    # Parámetros y funciones específicas del sistema
time                   # Funciones de tiempo y retrasos
threading              # Programación multihilo

# Bibliotecas externas requeridas
pywin32                # Integración API de Windows
pycryptodomex          # Operaciones criptográficas avanzadas
```

### **Bibliotecas Opcionales (Funcionalidad Extendida)**
```bash
requests               # Solicitudes HTTP y webhooks
psutil                 # Gestión de procesos del sistema
pillow                 # Procesamiento de imágenes (PIL)
pygame                 # Audio y efectos de sonido
win32api              # API extendida de Windows
win32con              # Constantes de Windows
win32gui              # Interfaz gráfica de Windows
winreg                # Acceso al registro de Windows
```

### **Instalación de Dependencias**
```bash
# Instalación básica
pip install pywin32 pycryptodomex

# Instalación completa (recomendada)
pip install pywin32 pycryptodomex requests psutil pillow pygame

# Instalación desde requirements.txt
pip install -r requirements.txt
```

## 🚀 Guía de Instalación Detallada

### **Paso 1: Preparación del Entorno**
```bash
# Verificar versión de Python
python --version

# Crear entorno virtual (recomendado)
python -m venv youtube_music_simulator
cd youtube_music_simulator
Scripts\activate  # Windows
```

### **Paso 2: Clonación del Repositorio**
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/youtube-music-setup-simulator.git

# Navegar al directorio del proyecto
cd youtube-music-setup-simulator

# Verificar integridad de archivos
dir /s  # Windows
```


### **Paso 3: Ejecución del Simulador**
```bash
# Ejecución básica
python youtube_music_setup.py

# Ejecución con privilegios administrativos (recomendado)
# Ejecutar terminal como administrador, luego:
python youtube_music_setup.py

# Ejecución en modo debug
python youtube_music_setup.py --debug
```

## 💡 Guía de Uso Completa

### **Operación Básica**
1. **Inicialización** - Ejecutar el script para inicializar la GUI de instalación
2. **Observación** - Observar la simulación auténtica de progreso desarrollarse
3. **Interacción** - La aplicación es completamente automatizada
4. **Finalización** - La aplicación se cierra automáticamente al completarse

### **Fases de Simulación Detalladas**

| Fase | Duración | Descripción Técnica | Mensajes Mostrados |
|------|----------|--------------------|--------------------|
| **Inicialización** | 2-4s | Verificaciones de compatibilidad del sistema | "Iniciando instalador...", "Verificando sistema..." |
| **Descarga** | 15-25s | Simulación de descarga de paquetes | "Descargando YouTube Music...", "Obteniendo componentes..." |
| **Extracción** | 8-15s | Descompresión de archivos simulada | "Extrayendo archivos...", "Preparando instalación..." |
| **Instalación** | 12-20s | Despliegue de archivos y actualizaciones del registro | "Instalando componentes...", "Configurando sistema..." |
| **Configuración** | 6-10s | Configuración de preferencias y biblioteca | "Configurando biblioteca musical...", "Aplicando preferencias..." |
| **Finalización** | 3-7s | Limpieza y verificación | "Finalizando instalación...", "Verificando instalación..." |

### **Elementos Interactivos**
- **Barra de Progreso** - Retroalimentación visual en tiempo real con display de porcentaje
- **Mensajes de Estado** - Actualizaciones dinámicas reflejando fases de instalación
- **Controles de Ventana** - Temporalmente deshabilitados para experiencia controlada
- **Auto-Completado** - Cierre automático con notificación de éxito


### **Componentes Técnicos Principales**

#### **1. GUI Manager (`gui_manager.py`)**
```python
# Funcionalidades principales:
- Creación y gestión de ventana principal
- Aplicación de temas y estilos
- Manejo de eventos de ventana
- Renderizado de elementos visuales
```

#### **2. Progress Simulator (`progress_simulator.py`)**
```python
# Funcionalidades principales:
- Cálculo de incrementos de progreso
- Temporización realista de fases
- Gestión de hilos de ejecución
- Simulación de operaciones de archivo
```

#### **3. Message Handler (`message_handler.py`)**
```python
# Funcionalidades principales:
- Base de datos de mensajes contextuales
- Selección aleatoria de mensajes
- Sincronización con fases de progreso
- Localización de mensajes
```

## 🔧 Configuración Avanzada

### **Opciones de Personalización**
```python
# Archivo config.py - Variables de configuración principales

# Configuración de Apariencia
WINDOW_WIDTH = 500              # Ancho de ventana
WINDOW_HEIGHT = 300             # Alto de ventana
PROGRESS_COLOR = "#FF0000"      # Color de barra de progreso
BACKGROUND_COLOR = "#1a1a1a"    # Color de fondo
TEXT_COLOR = "#ffffff"          # Color de texto

# Configuración de Comportamiento
PROGRESS_SPEED = 1.0            # Multiplicador de velocidad de animación
MIN_PHASE_DURATION = 2.0        # Duración mínima de fase (segundos)
MAX_PHASE_DURATION = 8.0        # Duración máxima de fase (segundos)
ENABLE_SOUNDS = False           # Activar efectos de sonido
DEBUG_MODE = False              # Modo de depuración

# Configuración de Mensajes
LANGUAGE = "es"                 # Idioma de mensajes (es/en)
RANDOM_MESSAGES = True          # Mensajes aleatorios por fase
SHOW_TECHNICAL_INFO = False     # Mostrar información técnica

# Configuración de Red (Opcional)
ENABLE_WEBHOOKS = False         # Activar webhooks
WEBHOOK_URL = ""                # URL del webhook
WEBHOOK_TIMEOUT = 10            # Timeout de webhook (segundos)
```

### **Configuración de Webhooks**
```python
# Ejemplo de configuración de webhook
WEBHOOK_CONFIG = {
    "enabled": True,
    "url": "https://tu-servidor.com/webhook",
    "events": ["start", "progress", "complete"],
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer tu-token"
    },
    "timeout": 15,
    "retry_attempts": 3
}
```

### **Configuración de Logging**
```python
# Configuración de sistema de logs
LOGGING_CONFIG = {
    "level": "INFO",                    # DEBUG, INFO, WARNING, ERROR
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "file": "simulator.log",
    "max_size": "10MB",
    "backup_count": 5
}
```

## 🔍 Análisis de Seguridad

### **Vectores de Ataque Demostrados**
1. **Ingeniería Social Visual** - Imitación de interfaces legítimas
2. **Abuse de Confianza** - Uso de marcas reconocidas
3. **Evasión de Detección** - Comportamiento aparentemente legítimo
4. **Persistencia Psicológica** - Proceso de instalación convincente

### **Técnicas de Defensa Educadas**
1. **Verificación de Origen** - Siempre descargar de fuentes oficiales
2. **Análisis de Certificados** - Verificar firmas digitales
3. **Sandboxing** - Ejecutar software desconocido en entornos aislados
4. **Análisis de Comportamiento** - Monitorear actividades inusuales

### **Indicadores de Compromiso (IoCs)**
```python
# Ejemplos de IoCs que este simulador podría generar
POTENTIAL_IOCS = {
    "file_hashes": ["MD5", "SHA1", "SHA256"],
    "network_connections": ["webhook URLs", "suspicious domains"],
    "registry_modifications": ["startup entries", "system changes"],
    "file_system_changes": ["created files", "modified directories"]
}
```

## 🧪 Testing y Calidad de Código

### **Suite de Pruebas**
```bash
# Ejecutar todas las pruebas
python -m pytest tests/

# Ejecutar pruebas específicas
python -m pytest tests/test_gui.py -v

# Ejecutar con coverage
python -m pytest --cov=src tests/

# Ejecutar pruebas de seguridad
python -m pytest tests/test_security.py --strict
```

### **Análisis de Código**
```bash
# Análisis de calidad de código
pylint src/
flake8 src/
black src/ --check

# Análisis de seguridad
bandit -r src/
safety check
```

### **Benchmarking de Rendimiento**
```python
# Métricas de rendimiento típicas
PERFORMANCE_METRICS = {
    "startup_time": "< 2 segundos",
    "memory_usage": "< 50MB",
    "cpu_usage": "< 5%",
    "gui_response_time": "< 100ms"
}
```

## 🤝 Contribución y Desarrollo

### **Guía de Contribución**
1. **Fork del Repositorio** - Crear fork en tu cuenta de GitHub
2. **Clonar Localmente** - Clonar tu fork localmente
3. **Crear Rama de Característica** - `git checkout -b feature/nueva-caracteristica`
4. **Implementar Cambios** - Desarrollar nuevas funcionalidades
5. **Pruebas Exhaustivas** - Probar en múltiples entornos
6. **Commit Descriptivo** - `git commit -m "Add: Animaciones mejoradas de progreso"`
7. **Push a Rama** - `git push origin feature/nueva-caracteristica`
8. **Pull Request** - Enviar PR con descripción detallada

### **Estándares de Desarrollo**
- **Código Python**: Seguir PEP 8 y PEP 257
- **Documentación**: Docstrings completos en español
- **Pruebas**: Cobertura mínima del 80%
- **Seguridad**: Análisis con herramientas de seguridad
- **Compatibilidad**: Mantener compatibilidad hacia atrás

### **Áreas de Contribución Prioritarias**
- 🎨 **Mejoras de UI/UX** - Nuevos temas y animaciones
- 🔒 **Características de Seguridad** - Análisis y detección mejorados
- 🌐 **Internacionalización** - Soporte para más idiomas
- 📊 **Analytics y Métricas** - Mejores capacidades de logging
- 🛠️ **Herramientas de Desarrollo** - Scripts de automatización

## 📊 Métricas y Analytics

### **Métricas de Uso (Para Investigación)**
```python
# Ejemplos de métricas que pueden recopilarse para investigación
RESEARCH_METRICS = {
    "execution_time": "tiempo total de ejecución",
    "user_interactions": "clics e intentos de interacción",
    "phase_completion_rates": "tasas de finalización por fase",
    "error_rates": "frecuencia de errores",
    "detection_rates": "detección por software antivirus"
}
```

### **Dashboard de Monitoreo**
- **Tiempo Real** - Monitoreo de ejecuciones activas
- **Estadísticas Históricas** - Análisis de tendencias
- **Detección de Anomalías** - Identificación de comportamientos inusuales
- **Reportes de Seguridad** - Análisis de detecciones de seguridad

## 🔄 Ciclo de Vida del Proyecto

### **Roadmap de Desarrollo**

#### **Versión 1.0 (Actual)**
- ✅ Simulador básico funcional
- ✅ Interfaz gráfica completa
- ✅ Documentación comprehensiva
- ✅ Disclaimers legales

#### **Versión 1.1 (Próxima)**
- 🔄 Mejoras de rendimiento
- 🔄 Nuevos temas visuales
- 🔄 Soporte para múltiples idiomas
- 🔄 Analytics mejorados

#### **Versión 2.0 (Futuro)**
- 📋 Múltiples simuladores de software
- 📋 Framework de detección
- 📋 API RESTful
- 📋 Interfaz web

### **Proceso de Release**
1. **Development** - Desarrollo en ramas de características
2. **Testing** - Pruebas exhaustivas automatizadas
3. **Security Review** - Revisión de seguridad completa
4. **Documentation** - Actualización de documentación
5. **Release** - Publicación con changelog detallado

## 📚 Recursos Educativos

### **Material de Aprendizaje**
- **Cursos Recomendados** - Ciberseguridad y ethical hacking
- **Libros de Referencia** - Ingeniería social y análisis de malware
- **Conferencias** - DEF CON, Black Hat, BSides
- **Certificaciones** - CEH, OSCP, CISSP

### **Herramientas Relacionadas**
- **Análisis de Malware** - IDA Pro, Ghidra, x64dbg
- **Detección de Amenazas** - YARA, Sigma, MISP
- **Sandboxes** - Cuckoo, Joe Sandbox, Any.run
- **Forense** - Volatility, Autopsy, SIFT

---

## 📜 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - consulta el archivo [LICENSE](LICENSE) para términos y condiciones completos.

### **Resumen de la Licencia MIT:**
- ✅ Uso comercial permitido
- ✅ Modificación permitida
- ✅ Distribución permitida
- ✅ Uso privado permitido
- ❌ Sin garantía
- ❌ Sin responsabilidad del autor

---

## 🔐 Declaración de Responsabilidad Final

### **COMPROMISO CON EL USO ÉTICO**

Los creadores y mantenedores de este proyecto se comprometen a:

1. **Transparencia Total** - Todo el código es open source y auditable
2. **Propósito Educativo** - Uso exclusivo para educación en ciberseguridad
3. **Colaboración Responsable** - Trabajo con la comunidad de seguridad
4. **Mejora Continua** - Actualizaciones constantes de seguridad y funcionalidad

### **DECLARACIÓN ANTI-MALWARE**

Este proyecto:
- ❌ **NO contiene** código malicioso real
- ❌ **NO recopila** información personal
- ❌ **NO se comunica** con servidores externos sin consentimiento explícito
- ❌ **NO modifica** el sistema del usuario sin autorización
- ✅ **SÍ es** completamente transparente en su funcionamiento

---

<div align="center">

**"La educación es el arma más poderosa que puedes usar para cambiar el mundo." - Nelson Mandela**

*Si este proyecto contribuyó a tu educación en ciberseguridad, considera darle una ⭐ y compartirlo responsablemente*

</div>
