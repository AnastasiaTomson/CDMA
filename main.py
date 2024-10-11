import numpy as np


def generate_walsh_codes(size):
    """Генерация матрицы Уолша для кодов нужного размера."""
    if size == 1:
        return np.array([[1]])
    smaller_matrix = generate_walsh_codes(size // 2)
    top = np.hstack((smaller_matrix, smaller_matrix))
    bottom = np.hstack((smaller_matrix, -smaller_matrix))
    walsh_matrix = np.vstack((top, bottom))
    print(f"\n▶ Матрица Уолша {size}x{size} сгенерирована:")
    print(walsh_matrix)
    return walsh_matrix


def text_to_binary(text):
    """Преобразование текста в двоичный код по ASCII."""
    binary_form = ''.join(f'{ord(char):08b}' for char in text)
    print(f"\n▶ Текст \"{text}\" преобразован в двоичный код: {binary_form}")
    return binary_form


def binary_to_text(binary_sequence):
    """Конвертация двоичной последовательности в исходный текст."""
    characters = [chr(int(binary_sequence[i:i + 8], 2)) for i in range(0, len(binary_sequence), 8)]
    text_output = ''.join(characters)
    print(f"\n◀ Двоичный код \"{binary_sequence}\" преобразован в текст:")
    return text_output


def modulate_message(message, walsh_code):
    """Модуляция сообщения с помощью кода Уолша."""
    binary_msg = text_to_binary(message)
    modulated_signal = []
    for bit in binary_msg:
        modulated_signal.extend(walsh_code if bit == '1' else -walsh_code)
    return np.array(modulated_signal)


def demodulate_message(received_signal, walsh_code):
    """Демодуляция сообщения на основе переданного сигнала."""
    code_length = len(walsh_code)
    bits_decoded = []
    for i in range(0, len(received_signal), code_length):
        chunk = received_signal[i:i + code_length]
        bit = 1 if np.dot(chunk, walsh_code) > 0 else 0
        bits_decoded.append(bit)
    binary_output = ''.join(map(str, bits_decoded))
    return binary_to_text(binary_output)


def main():
    # Ввод количества станций и сообщений
    num_stations = int(input("Введите количество станций: "))
    station_messages = {}

    print("\n=== Ввод сообщений для станций ===")
    for i in range(num_stations):
        station = chr(65 + i)  # A, B, C, D и так далее
        message = input(f"Введите сообщение для станции {station}: ")
        station_messages[station] = message

    # Генерация кодов Уолша
    matrix_size = 2**((num_stations - 1).bit_length())  # Минимальная степень двойки >= num_stations
    walsh_codes = generate_walsh_codes(matrix_size)

    # Модуляция сообщений
    all_signals = []
    print("\n=== Модуляция сообщений ===")
    for i, (station, message) in enumerate(station_messages.items()):
        signal = modulate_message(message, walsh_codes[i])
        all_signals.append(signal)

    # Суммирование всех сигналов
    combined_signal = np.sum(all_signals, axis=0)

    # Демодуляция для каждой станции
    print("\n=== Демодуляция сигналов для каждой станции ===")
    for i, (station, _) in enumerate(station_messages.items()):
        decoded_msg = demodulate_message(combined_signal, walsh_codes[i])
        print(f"✔ Сообщение станции {station} успешно декодировано: {decoded_msg}")


if __name__ == "__main__":
    main()
