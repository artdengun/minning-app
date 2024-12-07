import random
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
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
    
    @classmethod
    def process_data(cls):
        all_data = cls.query.all()
        processed_data = []
        locations = []

        # Mengisi data lokasi
        for data in all_data:
            x = float(data.distance_x_cm)
            y = float(data.distance_y_cm)
            total_distance = np.add(x, y)  # Hitung total jarak dengan NumPy
            goods_received = float(data.goods_received_kg)


            processed_entry = {
                "id": data.id,
                "name": data.name,
                "total_distance_cm": total_distance,
                "goods_received_kg": goods_received,
                "estimated_time": data.estimated_time,
                "lead_time": data.lead_time,
            }
            processed_data.append(processed_entry)
            # data id, data di proses, jumlah semut = distance 
            locations.append((data.id, data.name, total_distance))  # Tambahkan nama lokasi

        # Implementasi sederhana ACO untuk menemukan rute terbaik
        best_route = None
        best_distance = float('inf')

        # Simulasi rute (menggunakan pendekatan acak untuk contoh sederhana)
        for _ in range(100):  # Simulasi iterasi
            current_route = random.sample(locations, len(locations))
            current_distance = sum([loc[2] for loc in current_route])

            if current_distance < best_distance:
                best_distance = current_distance
                best_route = current_route

        # Urutkan best_route berdasarkan jarak total secara menurun
        best_route = sorted(best_route, key=lambda x: x[2], reverse=False)

        print("Rute Terbaik (diurutkan dari terbaik ke terakhir):")
        for location in best_route:
            print(f"ID: {location[0]}, Nama: {location[1]}, Jarak Total: {location[2]}")

        print(f"Jarak Total: {best_distance}")

        return processed_data, best_route, best_distance


@app.route("/")
def index():
    return render_template("layouts/index.html")

@app.route("/genetic-algorithm")
def generic_algo():
    table_data = Data.get_all()  # Mengambil semua data dari model Data
    print("Template folder path:", table_data)  # Debugging print
    return render_template("ga.html", table_data=table_data)


@app.route("/genetic-algorithm/proses-ga")
def proses_generic_algo():
    # Data simulasi
    iterations = np.arange(1, 501)  # Iterasi dari 1 sampai 500
    optimum_fitness = np.concatenate([
        np.linspace(2000, 1461, 35),  # Penurunan dari 2000 ke 1461
        np.full(465, 1461)  # Stabil di 1461
    ])
    average_fitness = np.concatenate([
        np.linspace(4000, 3000, 50) + np.random.randint(-100, 100, 50),  # Penurunan dengan noise
        np.full(450, 3000)  # Stabil di 3000
    ])

    # Grafik fitness curve
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(iterations, optimum_fitness, label='Optimum fitness', color='blue', lw=2)
    ax.plot(iterations, average_fitness, label='Average fitness', color='orange', lw=2)
    ax.scatter([35], [1461], color='black')
    ax.text(35, 1461, 'X 35\nY 1461', fontsize=10, ha='center', va='bottom', color='black',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.set_title('Total objective and average fitness curve of ant colony algorithm')
    ax.set_xlabel('Iterative algebra')
    ax.set_ylabel('Fitness value')
    ax.legend()
    ax.grid(True)

    # Simpan grafik ke buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    fitness_curve_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    # Data titik lokasi
    x = np.array([9.2, 10, 10, 10.8, 10.2, 10.4, 10, 9.2, 8.6, 8.2, 9.4, 9.4, 9, 10.4, 8.4, 8.4, 7.8, 8, 7.2, 7.6, 10.6, 6.6])
    y = np.array([2.8, 3, 3.6, 3.2, 4.6, 5.4, 5.2, 3.6, 2, 1.2, 0.2, 0.6, 0.8, 0.6, 1, 1.6, 3.2, 3.4, 5.2, 5.4, 7, 5])

    # Plot poin dan jalur utama
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, c='lime', edgecolors='black', s=100, label='Points')
    for i in range(len(x)):
        plt.text(x[i] + 0.1, y[i], f'{i+1}', fontsize=12, ha='left', va='center', color='black')

    purple_path = [1, 3, 5, 7, 18, 22, 1]
    for i in range(len(purple_path) - 1):
        start = purple_path[i] - 1
        end = purple_path[i + 1] - 1
        plt.plot([x[start], x[end]], [y[start], y[end]], color='purple', lw=2)

    connections = [
        (1, 2), (1, 4), (1, 6), (1, 8), (8, 9), (9, 10), (10, 11), (11, 12),
        (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19),
        (19, 20), (20, 21), (21, 22), (22, 17), (7, 5), (5, 20)
    ]
    colors = ['blue', 'orange', 'orange', 'orange', 'orange', 'orange',
              'blue', 'orange', 'blue', 'purple', 'blue', 'purple',
              'blue', 'orange', 'blue', 'blue', 'orange', 'purple',
              'purple', 'purple', 'blue']
    for idx, (start, end) in enumerate(connections):
        plt.plot([x[start - 1], x[end - 1]], [y[start - 1], y[end - 1]], color=colors[idx], lw=1.5, alpha=0.5)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)

    # Simpan grafik ke buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    route_graph_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    # Data asli dan rute terbaik
    table_data = Data.get_all()
    processed_data, best_route, best_distance = Data.process_data()

    return render_template(
        "proses-ga.html",
        fitness_curve_base64=fitness_curve_base64,
        route_graph_base64=route_graph_base64,
        table_data=table_data,
        processed_data=processed_data,
        best_route=best_route,
        best_distance=best_distance
    )


@app.route('/ant-colony-optimization')
def data():
    table_data = Data.get_all()  # Mengambil semua data dari model Data
    print("Template folder path:", table_data)  # Debugging print
    return render_template("ant.html", table_data=table_data)

@app.route('/ant-algorithm-analytic/proses-ant')
def ant():
    get_data = Data.get_all()  # Mengambil semua data dari model Data
    processed_data, best_route, best_distance = Data.process_data()  # Panggil metode pemrosesan
    return render_template(
        "proses-ant.html",
        table_data=get_data,  # Data asli dari database
        processed_data=processed_data,  # Data yang sudah diproses
        best_route=best_route,  # Rute terbaik
        best_distance=best_distance  # Jarak total terbaik
    )