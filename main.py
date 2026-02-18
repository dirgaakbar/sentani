import os
from jinja2 import Template
from datetime import datetime
import pytz

def get_real_scheduled_flights():
    """
    Daftar jadwal tetap penerbangan di Bandara Sentani (DJJ).
    Data ini disesuaikan dengan rute rutin maskapai.
    """
    return [
        {"flight_no": "GA 651", "airline": "Garuda Indonesia", "destination": "Jakarta (CGK)", "time": "08:15"},
        {"flight_no": "ID 6181", "airline": "Batik Air", "destination": "Makassar (UPG)", "time": "09:40"},
        {"flight_no": "JT 795", "airline": "Lion Air", "destination": "Merauke (MKG)", "time": "11:00"},
        {"flight_no": "IL 271", "airline": "Trigana Air", "destination": "Wamena (WMX)", "time": "12:30"},
        {"flight_no": "IW 1632", "airline": "Wings Air", "destination": "Dekai (DEX)", "time": "13:15"},
        {"flight_no": "GA 653", "airline": "Garuda Indonesia", "destination": "Timika (TIM)", "time": "14:45"},
        {"flight_no": "JT 798", "airline": "Lion Air", "destination": "Jayapura - Makassar", "time": "15:20"},
        {"flight_no": "ID 6183", "airline": "Batik Air", "destination": "Jakarta (CGK)", "time": "16:00"},
        {"flight_no": "IL 273", "airline": "Trigana Air", "destination": "Wamena (WMX)", "time": "16:45"},
    ]

def main():
    # 1. Setup Waktu Papua (WIT)
    wit = pytz.timezone('Asia/Jayapura')
    now = datetime.now(wit)
    now_str = now.strftime("%d %B %Y, %H:%M:%S")
    current_time_only = now.strftime("%H:%M")

    # 2. Ambil Jadwal Tetap
    raw_flights = get_real_scheduled_flights()
    processed_flights = []

    # 3. Logika Penentuan Status Otomatis
    for flight in raw_flights:
        # Jika waktu sekarang sudah melewati waktu pesawat, status DEPARTED
        if current_time_only > flight['time']:
            status = "DEPARTED"
        else:
            status = "SCHEDULED"
        
        flight['status'] = status
        processed_flights.append(flight)

    # 4. Render ke HTML
    try:
        with open("templates/index_template.html", "r", encoding="utf-8") as f:
            template_content = f.read()

        template = Template(template_content)
        rendered_html = template.render(flights=processed_flights, last_update=now_str)

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(rendered_html)
            
        print(f"Update Berhasil pada {now_str} WIT")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
