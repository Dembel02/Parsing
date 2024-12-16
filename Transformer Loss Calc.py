import math

def calculate_losses(input_power, copper_loss_primary, copper_loss_secondary, core_loss, split_ratio):
    """
    Расчет потерь в двухобмоточном трансформаторе с расщепленной обмоткой.

    :param input_power: Входная мощность трансформатора (Вт)
    :param copper_loss_primary: Потери в меди первичной обмотки (Вт)
    :param copper_loss_secondary: Потери в меди вторичной обмотки (Вт)
    :param core_loss: Потери в магнитопроводе (Вт)
    :param split_ratio: Коэффициент расщепления обмотки (доля мощности на вторичную обмотку)
    :return: Общие потери и КПД трансформатора
    """
    # Потери в меди вторичной обмотки учитывают расщепление
    adjusted_secondary_loss = copper_loss_secondary * split_ratio

    # Общие потери в трансформаторе
    total_losses = copper_loss_primary + adjusted_secondary_loss + core_loss

    # Полезная мощность на выходе трансформатора
    output_power = input_power - total_losses

    # Расчет КПД (в процентах)
    efficiency = (output_power / input_power) * 100

    return total_losses, efficiency

# Пример ввода данных
input_power = float(input("Введите входную мощность трансформатора (Вт): "))
copper_loss_primary = float(input("Введите потери в меди первичной обмотки (Вт): "))
copper_loss_secondary = float(input("Введите потери в меди вторичной обмотки (Вт): "))
core_loss = float(input("Введите потери в магнитопроводе (Вт): "))
split_ratio = float(input("Введите коэффициент расщепления обмотки (от 0 до 1): "))

# Расчет потерь и КПД
losses, efficiency = calculate_losses(input_power, copper_loss_primary, copper_loss_secondary, core_loss, split_ratio)

# Вывод результатов
print(f"\nОбщие потери в трансформаторе: {losses:.2f} Вт")
print(f"КПД трансформатора: {efficiency:.2f} %")