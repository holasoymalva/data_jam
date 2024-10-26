from flask import jsonify
from app import app
from app.predictor import RoutePredictor
import os

# Inicializar el predictor con el archivo CSV
csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'data_example.csv')
predictor = RoutePredictor(csv_path)

@app.route('/routes', methods=['GET'])
def get_routes():
    """Obtener todas las rutas disponibles"""
    routes = predictor.get_route_info()
    return jsonify({
        'status': 'success',
        'data': routes
    })

@app.route('/predict/<int:route_id>', methods=['GET'])
def predict_route(route_id):
    """Predecir próximos horarios para una ruta específica"""
    predictions = predictor.predict_next_times(route_id)
    
    if not predictions:
        return jsonify({
            'status': 'error',
            'message': 'Route not found'
        }), 404
        
    return jsonify({
        'status': 'success',
        'route_id': route_id,
        'predictions': predictions
    })

