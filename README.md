# CDMA Симуляция с использованием кодов Уолша

## Описание
Этот проект реализует симуляцию технологии **CDMA** (Кодовое разделение каналов), которая используется для передачи нескольких сообщений по одному каналу с использованием уникальных кодов Уолша для каждой станции. Программа модулирует сообщения в двоичный код, использует матрицу Уолша для кодирования каждого сообщения, суммирует их и затем демодулирует, чтобы восстановить исходные сообщения.

## Основные функции:
1. **Генерация кодов Уолша** для кодирования сообщений.
2. **Модуляция сообщений** каждой станции с использованием двоичного кода ASCII.
3. **Комбинирование сигналов** от всех станций в общий сигнал.
4. **Демодуляция сигналов** для каждой станции и восстановление исходных сообщений.

## Как использовать
1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Установите библиотеку **NumPy**, если она ещё не установлена:

    ```bash
    pip install numpy
    ```

3. Запустите скрипт:

    ```bash
    python main.py
    ```

4. Введите количество станций и их сообщения, следуя инструкциям программы.

## Пример работы
```bash
Введите количество станций: 3

=== Ввод сообщений для станций ===
Введите сообщение для станции A: HELLO
Введите сообщение для станции B: WORLD
Введите сообщение для станции C: CODE!

▶ Матрица Уолша 2x2 сгенерирована:
[[ 1  1]
 [ 1 -1]]

▶ Матрица Уолша 4x4 сгенерирована:
[[ 1  1  1  1]
 [ 1 -1  1 -1]
 [ 1  1 -1 -1]
 [ 1 -1 -1  1]]
 
=== Модуляция сообщений ===

▶ Текст "HELLO" преобразован в двоичный код: 0100100001000101010011000100110001001111

▶ Текст "WORLD" преобразован в двоичный код: 0101011101001111010100100100110001000100

▶ Текст "CODE!" преобразован в двоичный код: 0100001101001111010001000100010100100001

=== Демодуляция сигналов для каждой станции ===

◀ Двоичный код "0100100001000101010011000100110001001111" преобразован в текст:
✔ Сообщение станции A успешно декодировано: HELLO

◀ Двоичный код "0101011101001111010100100100110001000100" преобразован в текст:
✔ Сообщение станции B успешно декодировано: WORLD

◀ Двоичный код "0100001101001111010001000100010100100001" преобразован в текст:
✔ Сообщение станции C успешно декодировано: CODE!
```

## Функции программы
- **`generate_walsh_codes(size)`**: Генерирует матрицу Уолша для кодирования сообщений.
- **`text_to_binary(text)`**: Преобразует текст в двоичный код ASCII.
- **`binary_to_text(binary_sequence)`**: Конвертирует двоичную последовательность обратно в текст.
- **`modulate_message(message, walsh_code)`**: Модулирует сообщение с использованием кода Уолша.
- **`demodulate_message(received_signal, walsh_code)`**: Демодулирует сообщение на основе общего сигнала и кода Уолша.

## Требования
- Python 3.6 или выше
- Библиотека **NumPy** (установить через `pip`)