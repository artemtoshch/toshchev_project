student_name = "ощев Артём Павлович"
group_number = "3140801_52501"
project_name = "ЖК Астрамарин"
floors = "7 этажей"
height = "28.0 м"
is_residentional = True
constraction_year ="2024"

print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Состовитель: {student_name}")
print(f"Группа: {group_number}")
print(f"Объект: {project_name}")
print(f"Этажность: {floors}")
print(f"Высота: {height}")

if is_residentional:
    print("Тип: жилой")
else:
    print("Тип: нежилой")

print(f"Год постройки: {constraction_year}")

# Объект находится у метро Елизаровская
# Выбран, так как проходил там практику на строительной площадке