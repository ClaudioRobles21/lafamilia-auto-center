#!/usr/bin/env python3
"""
Servidor Flask para La Familia Auto Center - Chatbot con Claude Haiku 4.5
Maneja las llamadas a la API de Anthropic de forma segura
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Inicializar cliente de Anthropic
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

# Historial de conversaciones por sesión
conversations = {}

SYSTEM_PROMPT = """Eres un asesor de ventas profesional de La Familia Auto Center, una concesionaria de vehículos premium en México. 

Tu rol es:
- Responder preguntas sobre nuestros vehículos disponibles
- Proporcionar información sobre especificaciones, precios (cuando se pregunta)
- Ser amable, profesional e informativo
- Sugerir vehículos según las necesidades del cliente
- Facilitar el agendamiento de citas para que vean los vehículos
- Proporcionar información de contacto: 81 2609 7169, WhatsApp disponible

Vehículos disponibles:
1. Toyota Corolla 2020 - Sedán, color azul/gris, 180,000 km, transmisión automática, interiores sintético
2. Suzuki Swift 2021 - Hatchback, color blanco, 50,000 km, transmisión automática, interiores piel
3. Chevrolet Corvette C8 2025 - Deportivo, color blanco, 5,000 km, transmisión estándar, interiores piel
4. Mazda CX-50 2024 - SUV, color negra, 20,000 km, transmisión automática, interiores sintético
5. Ford F150 Raptor 2015 - Pickup, color roja, 98,000 km, transmisión estándar, interiores piel

Cuando el cliente quiera agendar una cita, debes recopilar:
- Nombre completo
- Teléfono/WhatsApp
- Correo electrónico
- Vehículo de interés
- Fecha y hora preferida

Una vez que tengas los datos, confirma la cita y ofrece enviarla por WhatsApp o email.

Responde siempre en español, mantén un tono profesional pero amable y cálido.
Usa emojis ocasionalmente para hacer la conversación más agradable.
Sé conciso pero informativo en tus respuestas."""

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint para procesar mensajes del chatbot"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({'error': 'Mensaje vacío'}), 400
        
        # Obtener o crear historial de conversación
        if session_id not in conversations:
            conversations[session_id] = []
        
        # Agregar mensaje del usuario al historial
        conversations[session_id].append({
            'role': 'user',
            'content': user_message
        })
        
        # Llamar a Claude Haiku 4.5
        response = client.messages.create(
            model='claude-3-5-haiku-20241022',
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=conversations[session_id]
        )
        
        # Extraer respuesta
        bot_message = response.content[0].text
        
        # Agregar respuesta al historial
        conversations[session_id].append({
            'role': 'assistant',
            'content': bot_message
        })
        
        return jsonify({
            'success': True,
            'message': bot_message,
            'session_id': session_id
        })
    
    except anthropic.APIError as e:
        print(f"Error de API de Anthropic: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Error al procesar tu mensaje: {str(e)}'
        }), 500
    
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Hubo un error al procesar tu solicitud. Intenta nuevamente.'
        }), 500

@app.route('/api/schedule', methods=['POST'])
def schedule_appointment():
    """Endpoint para agendar citas"""
    try:
        data = request.json
        
        # Validar datos
        required_fields = ['nombre', 'telefono', 'email', 'auto', 'fecha', 'hora']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Campo requerido: {field}'}), 400
        
        # Aquí guardarías los datos en una base de datos o los enviarías a Google Forms
        # Por ahora, solo confirmamos
        
        appointment_data = {
            'nombre': data.get('nombre'),
            'telefono': data.get('telefono'),
            'email': data.get('email'),
            'auto': data.get('auto'),
            'fecha': data.get('fecha'),
            'hora': data.get('hora'),
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"Cita agendada: {appointment_data}")
        
        return jsonify({
            'success': True,
            'message': '✅ ¡Cita agendada exitosamente! Nos pondremos en contacto pronto.',
            'appointment': appointment_data
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'La Familia Auto Center Chatbot'})

if __name__ == '__main__':
    print("🚗 La Familia Auto Center - Chatbot Server iniciando...")
    print("⚠️  Asegúrate de tener ANTHROPIC_API_KEY en las variables de entorno")
    app.run(debug=False, host='0.0.0.0', port=5000)
