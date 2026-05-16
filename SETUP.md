# 🚗 La Familia Auto Center - Guía de Configuración (TODO LISTO)

## ✅ ESTADO ACTUAL

- ✅ Imágenes de los 5 autos descargadas
- ✅ Dependencias instaladas
- ✅ Servidor backend listo
- ✅ Página web profesional lista
- ⏳ Solo falta tu API Key de Anthropic

## 📋 PASO 1: Crear archivo `.env` con tu API Key

**⚠️ IMPORTANTE:** Ya subiste tu API Key. Ahora debes crear un archivo `.env` LOCAL (en tu VPS) con tu clave.

En tu terminal de VPS:

```bash
cd /data/.openclaw/workspace
cp .env.example .env
# Edita .env y cambia:
# ANTHROPIC_API_KEY=tu_clave_aqui
```

O usa nano/vi para crear el archivo:
```bash
nano .env
```

Luego pega tu API Key (la que usaste antes)

## ✅ Paso 2: Las Imágenes YA Están Descargadas

```
autos/
├── Corolla.jpg       ✅ (Toyota Corolla 2020)
├── Swift.jpg         ✅ (Suzuki Swift 2021)
├── Corvette.jpg      ✅ (Chevrolet Corvette C8 2025)
├── CX-50.jpg         ✅ (Mazda CX-50 2024)
└── F150.jpg          ✅ (Ford F150 Raptor 2015)
```

## ✅ Paso 3: Dependencias YA Están Instaladas

Las librerías necesarias ya se instalaron:
- Flask
- anthropic
- flask-cors
- python-dotenv

## 🚀 PASO 4: INICIAR EL SERVIDOR (EN UNA TERMINAL)

```bash
cd /data/.openclaw/workspace
./run_chatbot.sh
```

Deberías ver:
```
╔════════════════════════════════════════════════════════════════╗
║        🚗 La Familia Auto Center - Chatbot Server 🤖          ║
╚════════════════════════════════════════════════════════════════╝

📸 Verificando imágenes de autos...
   ✅ Corolla.jpg
   ✅ Swift.jpg
   ...
```

## 🌐 PASO 5: SERVIR LA PÁGINA WEB (EN OTRA TERMINAL)

Abre una NUEVA terminal en la misma carpeta:

```bash
cd /data/.openclaw/workspace
./serve_web.sh
```

Deberías ver:
```
📍 Servidor web escuchando en: http://localhost:8000
```

## 🌐 PASO 6: Abrir en tu Navegador

Abre: **http://localhost:8000**

Verifica que:
1. ✅ Se carga la página (galería de autos visible)
2. ✅ Las imágenes de los autos se ven
3. ✅ El botón "💬 Habla con nuestro Asesor" aparece

## ✅ VERIFICAR QUE TODO FUNCIONE

1. Abre http://localhost:8000 en tu navegador
2. Haz clic en "💬 Habla con nuestro Asesor"
3. Escribe: "Hola"
4. ✅ El chatbot debe responder con un mensaje de bienvenida
5. Prueba: "Quiero información sobre el Corolla"
6. Prueba: "Quiero agendar una cita"

## 🐛 SOLUCIÓN DE PROBLEMAS

### El chatbot no responde:
```bash
# 1. Verifica que .env existe con tu API Key
cat .env

# 2. Verifica que el servidor chatbot está corriendo
# (en la terminal 1, deberías ver puerto 5000)

# 3. En el navegador, presiona F12 y revisa la consola para errores
```

### Las imágenes no se ven:
```bash
# Verifica que existen:
ls -la autos/

# Deberías ver 5 imágenes JPEG (no HTML)
file autos/*.jpg
```

### El puerto 5000 está en uso:
```bash
# Ver qué está usando el puerto:
lsof -i :5000

# Cambiar puerto en chatbot_server.py (línea final):
# app.run(debug=False, host='0.0.0.0', port=8001)
```

### El puerto 8000 está en uso:
```bash
# Usar otro puerto:
python -m http.server 9000
# Luego abre: http://localhost:9000
```

## 📞 INFORMACIÓN DE CONTACTO

- **Teléfono:** 81 2609 7169
- **WhatsApp:** 81 2609 7169
- **Facebook:** https://www.facebook.com/share/1Y5sxcB7Qm/?mibextid=wwXIfr
- **Correo:** autocenterlafamilia@gmail.com

## 🔐 SEGURIDAD

⚠️ **IMPORTANTE:** Tu API Key está en `/.env` y NO se sube a GitHub gracias a `.gitignore`.

Si accidentalmente la subes:
1. Ve a https://console.anthropic.com/
2. Revoca la API Key comprometida
3. Crea una nueva

## 📱 PRÓXIMO PASO (OPCIONAL)

Para usar en producción con GitHub Pages:
1. Desplega `chatbot_server.py` en un servidor (Heroku, Railway, tu servidor)
2. Cambia `http://localhost:5000` por la URL de tu servidor en `index.html`
3. Habilita CORS en el servidor de producción

---

**Creado por:** Car IA  
**Última actualización:** 2026-05-16  
**Estado:** ✅ Listo para usar (solo falta tu API Key en .env)
