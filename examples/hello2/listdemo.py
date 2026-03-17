from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "hu_HU.UTF-8")  # Linux/Mac
# locale.setlocale(locale.LC_TIME, "Hungarian")   # Windows
now = datetime.now()
print(now.strftime("%Y. %b %d. (%a) %H:%M:%S"))
