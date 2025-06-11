# Task Tracker Uygulaması

Bu proje, FastAPI backend ve Streamlit frontend kullanılarak geliştirilmiş basit bir görev takip uygulamasıdır.

## Özellikler

- Yeni görev ekleme
- Mevcut görevleri listeleme
- Görev silme
- SQLite veritabanı ile kalıcı depolama

## Teknolojiler

- Backend: FastAPI
- Frontend: Streamlit
- Veritabanı: SQLite
- ORM: SQLAlchemy

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repository-url]
cd task-tracker
```

2. Sanal ortam oluşturun ve aktif edin:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install fastapi uvicorn sqlalchemy streamlit requests
```

## Çalıştırma

1. Backend sunucusunu başlatın:
```bash
uvicorn main:app --reload
```

2. Yeni bir terminal açın ve frontend uygulamasını başlatın:
```bash
streamlit run app.py
```

3. Tarayıcınızda aşağıdaki adreslere giderek uygulamayı kullanabilirsiniz:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Dokümantasyonu: http://localhost:8000/docs

## API Endpoints

- `GET /tasks/`: Tüm görevleri listeler
- `POST /tasks/`: Yeni görev ekler
- `GET /tasks/{task_id}`: Belirli bir görevi getirir
- `DELETE /tasks/{task_id}`: Görevi siler

