#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         🌐 Sirviendo página web - La Familia Auto Center      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "📍 Servidor web escuchando en: http://localhost:8000"
echo ""
echo "🌐 Abre en tu navegador:"
echo "   http://localhost:8000"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""

python -m http.server 8000
