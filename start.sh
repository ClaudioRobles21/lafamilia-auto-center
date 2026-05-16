#!/bin/bash

echo "🚗 La Familia Auto Center - Iniciando..."
echo ""

# Verificar que .env existe
if [ ! -f .env ]; then
    echo "❌ Error: No existe archivo .env"
    echo "Crea un archivo .env con: ANTHROPIC_API_KEY=tu_clave"
    exit 1
fi

# Verificar que la carpeta autos existe
if [ ! -d "autos" ]; then
    echo "❌ Error: Carpeta 'autos' no existe"
    echo "Crea la carpeta: mkdir autos"
    exit 1
fi

# Verificar que las imágenes existen
REQUIRED_IMAGES=("Corolla.jpg" "Swift.jpg" "Corvette.jpg" "CX-50.jpg" "F150.jpg")
MISSING_IMAGES=()

for img in "${REQUIRED_IMAGES[@]}"; do
    if [ ! -f "autos/$img" ]; then
        MISSING_IMAGES+=("$img")
    fi
done

if [ ${#MISSING_IMAGES[@]} -gt 0 ]; then
    echo "⚠️  Imágenes faltantes:"
    for img in "${MISSING_IMAGES[@]}"; do
        echo "   - autos/$img"
    done
    echo ""
    echo "Por favor, copia las imágenes a la carpeta 'autos/'"
    exit 1
fi

# Cargar variables de entorno
export $(cat .env | xargs)

echo "✅ Configuración verificada"
echo ""
echo "🚀 Iniciando servidor del chatbot..."
echo "   Escuchando en: http://0.0.0.0:5000"
echo ""
echo "En otra terminal, ejecuta:"
echo "   python -m http.server 8000"
echo ""
echo "Luego abre en navegador:"
echo "   http://localhost:8000"
echo ""

python chatbot_server.py
