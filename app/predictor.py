import pandas as pd
from datetime import datetime, timedelta

class RoutePredictor:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['event_date'] = pd.to_datetime(self.df['event_date'])
        self.df['hour'] = self.df['event_date'].dt.hour
        
    def predict_next_times(self, route_id):
        # Filtrar por ruta
        route_data = self.df[self.df['route_id'] == route_id]
        
        if route_data.empty:
            return []
            
        # Agrupar por hora y contar frecuencia
        hourly_counts = route_data.groupby('hour').size()
        
        # Encontrar las horas más frecuentes (top 3)
        most_frequent_hours = hourly_counts.nlargest(3)
        
        # Crear predicciones para el siguiente día
        predictions = []
        current_date = datetime.now()
        next_date = current_date + timedelta(days=1)
        
        for hour, count in most_frequent_hours.items():
            prediction_time = next_date.replace(hour=hour, minute=0, second=0)
            predictions.append({
                'hour': hour,
                'predicted_time': prediction_time.strftime('%Y-%m-%d %H:%M:00'),
                'confidence': float(count) / len(route_data) * 100
            })
            
        return predictions

    def get_route_info(self):
        # Obtener información única de rutas
        routes = self.df[self.df['route_id'] != 0][['route_id', 'route_name']].drop_duplicates()
        return routes.to_dict('records')
