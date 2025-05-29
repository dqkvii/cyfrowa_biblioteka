# 📚 Cyfrowa Biblioteka

Cyfrowa aplikacja do zarządzania książkami, stworzona w Django z wykorzystaniem wzorca MVC.

## 📑 Spis treści

- [Opis projektu](#opis-projektu)
- [Struktura pojektu (MVC)](#-struktura-projektu-mvc)
- [Funkcjonalności](#funkcjonalności)
- [Technologie](#technologie)
- [Instalacja](#instalacja)
- [Uruchomienie](#uruchomienie)

---

## 📝 Opis projektu

Projekt umożliwia zarządzanie cyfrową biblioteką — dodawanie, edycję, przeglądanie i usuwanie książek. Każda książka posiada tytuł, autora, rok wydania, opis oraz gatunek.

Interfejs użytkownika umożliwia również przeglądanie książek według gatunku i przeszukiwanie bazy po tytule.

---

## 📂 Struktura projektu (MVC)

- **Model:** `models.py` – definicja książek, gatunków itp.
- **Widok (template):** `templates/` – lista, formularze, szczegóły
- **Kontroler:** `views.py` – logika obsługi żądań

---

## ✅ Funkcjonalności

- Dodawanie nowych książek z formularzem (tytuł, autor, rok, gatunek, opis, okładka)
- Przeglądanie listy książek z miniaturami
- Szczegóły książki (pełny widok z okładką, opisem i gatunkiem)
- Edycja i usuwanie książek
- Filtracja książek po gatunku (np. Fantastyka, Kryminał)
- Wyszukiwarka po tytule
- Obsługa okładek książek jako plików graficznych

---

## 💻 Technologie

- Python 3.9+
- Django 4.x
- SQLite (wbudowana baza danych)
- Bootstrap 5 (stylizacja)
- Docker (opcjonalnie)

---

## ⚙️ Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/dqkvii/cyfrowa_biblioteka.git
cd cyfrowa-biblioteka
```

2. Utwórz i aktywuj środowisko wirtualne:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

4. Wykonaj migracje i uruchom serwer:

```bash
python manage.py migrate
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Uruchomienie w Dockerze (opcjonalnie)

```bash
docker pull dqkvi/cyfrowa_biblioteka-web:latest
docker run -d -p 8000:8000 --rm --name biblioteka dqkvi/cyfrowa_biblioteka-web:latest
```

Otwórz w przeglądarce: [http://localhost:8000](http://localhost:8000)
