import datetime
from data.getItemData import *


today = datetime.date.today()
current_month = datetime.date.today().month
month_range = range(1, 13)
current_year = datetime.date.today().year
year_range = range(current_year-3, current_year + 3)

material_options = getMaterialOption()

metode_tender_option = getTenderOption()

