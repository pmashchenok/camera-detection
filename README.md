# camera-detection
В проекте реализована детекция людей с уличной камеры видеонаблюдения с использованием модели YOLOv8.
Система принимает видеофайл, обрабатывает каждый кадр с помощью предварительно обученной модели, обнаруживает объекты класса "person" и выводит на видео рамки вокруг людей с указанием вероятности обнаружения. Проект может быть использован для систем видеонаблюдения, анализа посетителей, подсчёта людей и других задач, связанных с мониторингом городской среды.

 
Файл **detect.mp4** - Результат. Видео с отрисовкой bbox каждого распознаного человека на видео.
### Клонирование репозитория
```bash
git clone https://github.com/pmashchenok/camera-detection.git
```

### Установка зависимостей
Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Linux / macOS
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Запуск программы
```bash
python main.py
```
