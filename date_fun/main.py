import pandas as pd
import datetime as dt


def get_date(input_dt: str, day_int: str):
    if input_dt is None:
        return None
    elif day_int is None or day_int == 0:
        return dt.datetime.strptime(input_dt, '%m/%d/%Y').date()
    else:
        pd_ts = pd.Timestamp(input_dt)
        return dt.date(pd_ts.year, pd_ts.month, int(day_int))


