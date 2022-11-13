# IIntegrationWhales 

## Возможности приложения
- Загрузка файла (файлов) в формате jpg, png, jpeg
- Выгрузка размечанных данных в формате .csv в корневой каталог программы
- Кнопка "загрузить снова" удаляет предыдущие картинки и загружет новые фото
- Под каждым файлом будет топ 5 id

<details>
  <summary>Скриншоты программы</summary>

  ![Приветственное окно](https://i.imgur.com/teau9SH.png)

  ![Главный экран](https://i.imgur.com/5zvPsSY.png)

  ![Демонстрация работы](https://i.imgur.com/eia45fu.png)

</details>

## Установка
### Готовый .exe
- Скачать установщик `main.exe` с [Яндекс.Диска](https://disk.yandex.ru/d/cSATxqzKU7qYug)
- Установить

### Сборка проекта
- Склонируйте репозиторий `git clone https://github.com/kirka50/IIntegrationWhales.git`
- Перейдите в папку с проектом `cd IIntegrationWhales`
- Установите зависимости `pip install -r requirements.txt`
- Скачайте веса с [Яндекс.Диска](https://disk.yandex.ru/d/cSATxqzKU7qYug) и поместите в корень проекта
- Запустите проект `py main.py`

### Сборка .exe
- Выполните сборку проекта
- Установите pyinstaller `pip install pyinstaller`
- Запустите сборку `pyinstaller --noconsole --add-data "autoencoder.h5;." --add-data "model.h5;." --add-data "ui;ui" --add-data "assets;assets" main.py`

## Обучение
- [learn/train_effnet.ipynb](https://github.com/kirka50/IIntegrationWhales/blob/master/learn/train_effnet.ipynb) - обучение моделей
- [learn/add_training.ipynb](https://github.com/kirka50/IIntegrationWhales/blob/master/learn/add_training.ipynb) - дообучение модели
- [learn/create_data.py](https://github.com/kirka50/IIntegrationWhales/blob/master/learn/create_data.py) - создание датасета
- [learn/hack_6.ipynb](https://github.com/kirka50/IIntegrationWhales/blob/master/learn/hack_6.ipynb) - автоэнкодер
