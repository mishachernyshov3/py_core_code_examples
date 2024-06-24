# Навчальна секція відкрита, коли вона
# - є першою секцією
# - АБО попередня секція переглянута та оцінена
# Визначити, чи відкрита секція

is_available = False

is_first_section = False
is_prev_sec_completed = True
is_prev_sec_graded = False

if is_first_section:
    is_available = True
elif is_prev_sec_completed:
    if is_prev_sec_graded:
        is_available = True

print(f"Is section opened: {is_available}")
