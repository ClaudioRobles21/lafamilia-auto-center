#!/bin/bash

# 🚗 La Familia Auto Center - Script de Inicio

set -e

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        🚗 La Familia Auto Center - Chatbot Server 🤖          ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar .env
if [ ! -f .env ]; then
    echo "❌ ERROR: No existe archivo .env"
    echo ""
    echo "Cómo crear .env:"
    echo "  1. Abre .env.example"
    echo "  2. Copia el contenido"
    echo "  3. Reemplaza 'tu_clave_aqui' con tu API Key de Anthropic"
    echo "  4. Guarda como .env"
    echo ""
    exit 1
fi

# Cargar variables de entorno
export $(cat .env | xargs)

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ERROR: ANTHROPIC_API_KEY no está configurada en .env"
    exit 1
fi

# Verificar imágenes
echo "📸 Verificando imágenes de autos..."
REQUIRED_IMAGES=("Corolla.jpg" "Swift.jpg" "Corvette.jpg" "CX-50.jpg" "F150.jpg")
ALL_OK=true

for img in "${REQUIRED_IMAGES[@]}"; do
    if [ ! -f "autos/$img" ]; then
        echo "   ❌ Falta: autos/$img"
        ALL_OK=false
    else
        echo "   ✅ $img"
    fi
done

if [ "$ALL_OK" = false ]; then
    echo ""
    echo "❌ Faltan imágenes. Verifica la carpeta 'autos/'"
    exit 1
fi

echo ""
echo "✅ Configuración verificada"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 INICIANDO SERVIDOR DEL CHATBOT..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📍 Servidor escuchando en: http://localhost:5000"
echo ""
echo "PRÓXIMOS PASOS:"
echo "  1. Abre otra terminal en la misma carpeta"
echo "  2. Ejecuta: python -m http.server 8000"
echo "  3. Abre en tu navegador: http://localhost:8000"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

python chatbot_server.py
