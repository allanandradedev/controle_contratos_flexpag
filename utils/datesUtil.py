import datetime
from datetime import timedelta

TODAY = datetime.datetime.today()
TODAY_WITH_HIFEN = datetime.datetime.today().strftime('%d-%m-%Y')
TODAY_WITH_DOT = datetime.datetime.today().strftime('%d.%m.%Y')
YERSTERDAY = datetime.datetime.today() - timedelta(days=1)
YERSTERDAY_FORMAT = YERSTERDAY.strftime('%d/%m/%Y')
YERSTERDAY_WITH_HIFEN = YERSTERDAY.strftime('%d-%m-%Y')
YERSTERDAY_WITH_DOT = YERSTERDAY.strftime('%d.%m.%Y')
DATE_DD_MM = datetime.datetime.today().strftime('%d/%m')
DATE_MM_AA = datetime.datetime.today().strftime('%m/%Y')
DATE_AA = datetime.datetime.today().strftime('%Y')
DATE_DD_MM_WITH_DOT = datetime.datetime.today().strftime('%d.%m')
DATE_MM_AA_WITH_DOT = datetime.datetime.today().strftime('%m.%Y')
DATE_DD_MM_WITH_HIFEN = datetime.datetime.today().strftime('%d-%m')
DATE_MM_AA_WITH_HIFEN = datetime.datetime.today().strftime('%m-%Y')
YERSTERDAY_FORMAT_EXPORT = YERSTERDAY.strftime('%Y-%m-%d')
DATE_MM = datetime.datetime.today().strftime('%m')
DATE_DD = datetime.datetime.today().strftime('%d')
