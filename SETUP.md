# 🚗 La Familia Auto Center - Guía de Configuración

## Requisitos Previos

- Python 3.8+
- pip
- API Key de Anthropic (Claude)
- Navegador web moderno

## 📋 Paso 1: Obtener API Key de Anthropic

1. Ve a https://console.anthropic.com/
2. Crea una cuenta o inicia sesión
3. Ve a "API Keys" en el panel lateral
4. Crea una nueva clave
5. Cópialaa (necesitarás esto en el Paso 3)

## 📁 Paso 2: Copiar Imágenes de Autos

Las imágenes deben estar en la carpeta `autos/` con estos nombres exactos:

```
autos/
├── Corolla.jpg       (Toyota Corolla 2020)
├── Swift.jpg         (Suzuki Swift 2021)
├── Corvette.jpg      (Chevrolet Corvette C8 2025)
├── CX-50.jpg         (Mazda CX-50 2024)
└── F150.jpg          (Ford F150 Raptor 2015)
```

**Instrucciones:**
1. Descarga las 5 imágenes que subió el Boss
2. Crea la carpeta `autos` en la raíz del proyecto
3. Coloca las imágenes con los nombres exactos listados arriba

## 🔧 Paso 3: Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
ANTHROPIC_API_KEY=tu_clave_aqui
```

Reemplaza `tu_clave_aqui` con tu API Key de Anthropic.

## 📦 Paso 4: Instalar Dependencias

```bash
pip install -r requirements_chatbot.txt
```

## 🚀 Paso 5: Ejecutar el Servidor

```bash
python chatbot_server.py
```

Deberías ver:
```
🚗 La Familia Auto Center - Chatbot Server iniciando...
⚠️  Asegúrate de tener ANTHROPIC_API_KEY en las variables de entorno
 * Running on http://0.0.0.0:5000
```

## 🌐 Paso 6: Abrir la Página Web

1. Abre tu navegador
2. Ve a: `http://localhost:8000` (o donde tengas servida la página)
3. O simplemente abre el archivo `index.html` directamente

**Nota:** Si abres `index.html` directamente (sin servidor), el chatbot no funcionará. Necesitas servir la página con un servidor web simple.

### Opción A: Servir con Python (Recomendado)

```bash
# En otra terminal, en la carpeta del proyecto:
python -m http.server 8000
```

Luego abre: http://localhost:8000

### Opción B: Servir con Node.js

```bash
npx http-server
```

## ✅ Verificar que Todo Funcione

1. Abre http://localhost:8000 en tu navegador
2. Haz clic en "💬 Habla con nuestro Asesor"
3. Escribe: "Hola"
4. El chatbot debe responder con un mensaje de bienvenida

## 🐛 Solución de Problemas

### El chatbot no responde:
- Verifica que el servidor está corriendo (`python chatbot_server.py`)
- Verifica que tu API Key de Anthropic es correcta
- Abre la consola del navegador (F12) y revisa los errores

### Las imágenes no se ven:
- Verifica que las imágenes están en `autos/` con los nombres correctos
- Revisa la consola del navegador para ver los errores

### El puerto 5000 está en uso:
```bash
# Cambiar puerto en chatbot_server.py
# Línea final: app.run(debug=False, host='0.0.0.0', port=8001)
```

## 📱 Usar en Producción (GitHub Pages)

Para usar en GitHub Pages con un servidor externo:

1. Reemplaza `http://localhost:5000` en el HTML con tu servidor de producción
2. Configura CORS en tu servidor de producción
3. Despliega el servidor en una plataforma como Heroku, Railway, o tu propio servidor

## 📞 Contacto

- **Teléfono:** 81 2609 7169
- **Facebook:** https://www.facebook.com/share/1Y5sxcB7Qm/?mibextid=wwXIfr

---

**Creado por:** Car IA  
**Última actualización:** 2026-05-16
