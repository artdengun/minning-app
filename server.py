from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inisialisasi db dan migrate
db = SQLAlchemy()
migrate = Migrate()

# Fungsi untuk membuat aplikasi
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inisialisasi db dengan app
    db.init_app(app)
    migrate.init_app(app, db)

    return app

# Inisialisasi aplikasi Flask
app = create_app()

# Model Data
class Data(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    distance_x_cm = db.Column(db.String(60), index=True, unique=True, nullable=False)
    distance_y_cm = db.Column(db.String(100), nullable=False)
    goods_received_kg = db.Column(db.String(100), nullable=False)
    estimated_time = db.Column(db.String(100), nullable=False)
    lead_time = db.Column(db.String(100), nullable=False)

    @property
    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "distance_x_cm": self.distance_x_cm,
            "distance_y_cm": self.distance_y_cm,
            "goods_received_kg": self.goods_received_kg,
            "estimated_time": self.estimated_time,
            "lead_time": self.lead_time,
        }

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []

        for i in r:
            result.append(i.data)
        return result

# Routes
@app.route("/")
def index():
    return render_template("layouts/index.html")

@app.route("/genetic-algorithm")
def generic_algo():
    table_data = [
        {
            'id': 1,
            'name': 'Sample Location',
            'distance_x_cm': '10',
            'distance_y_cm': '5',
            'goods_received_kg': '100',
            'estimated_time': '10:00',
            'lead_time': '12:00'
        }
    ]
    return render_template("ga.html", table_data=table_data)

@app.route('/ant-colony-optimization')
def data():
    table_data = Data.get_all()  # Mengambil semua data dari model Data
    print("Template folder path:", table_data)  # Debugging print
    return render_template("ant.html", table_data=table_data)

@app.route('/ant-algorithm-analytic/proses-ant')
def ant():
    return render_template("proses-ant.html")

# Jalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)
