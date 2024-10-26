# Route Prediction API

This project provides a simple Flask API for predicting public transport route times based on historical data. It analyzes patterns in route schedules and predicts the most likely times for future route occurrences.

## 🚀 Features

- List all available routes
- Predict next day's most likely times for specific routes
- Confidence scoring for predictions
- Simple REST API interface

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Basic knowledge of REST APIs
- Your route data in CSV format

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/holasoymalva/data_jam.git
cd data_jam
```

2. Create a virtual environment and activate it:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Place your data file:
   - Copy your route data CSV file to the `data/` directory
   - Name it `data_example.csv`

## 📁 Project Structure
```
flask_route_predictor/
│
├── data/
│   └── data_example.csv
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── predictor.py
│
├── requirements.txt
└── run.py
```

## 🚀 Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python run.py
```
The API will start running on `http://localhost:5000`

## 🔍 API Endpoints

### Get All Routes
```http
GET /routes
```
Returns a list of all available routes.

Example response:
```json
{
    "status": "success",
    "data": [
        {
            "route_id": 908,
            "route_name": "82 García Gíneres"
        },
        ...
    ]
}
```

### Get Route Predictions
```http
GET /predict/<route_id>
```
Returns predictions for a specific route.

Example response:
```json
{
    "status": "success",
    "route_id": 908,
    "predictions": [
        {
            "hour": 8,
            "predicted_time": "2024-10-27 08:00:00",
            "confidence": 85.5
        },
        ...
    ]
}
```

## 📊 Input Data Format

The CSV file should have the following columns:
- event_date
- route_id
- route_name
- (other columns will be ignored)

Example:
```csv
event_date,route_id,route_name
2024-09-22 13:44:00.000,908,82 García Gíneres
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Made with ❤️ by [holasoymalva](https://github.com/holasoymalva)

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by public transport optimization needs
- Built with Flask framework

## 📞 Support

If you have any questions or need help, please:
1. Check the existing issues
2. Create a new issue if needed
3. Contact me through GitHub

---
Remember to ⭐️ this repository if you found it helpful!
