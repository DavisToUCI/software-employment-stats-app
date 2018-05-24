# Sorts the information by the employment available
def sort_by_employment(sheet: dict(dict())) -> list:
    return [key[0] for key in sorted(sheet.items(), key = lambda key: key[1]['Employment(1)'], reverse = True)]

# Sorts the information by the annual mean wage
def sort_by_annual_mean_wage(sheet: dict(dict())) -> list:
    return [key[0] for key in sorted(sheet.items(), key = lambda key: key[1]['Annual mean wage(2)'], reverse = True)]

# Sorts the information by the annual median wage
def sort_by_annual_median_wage(sheet: dict(dict())) -> list:
    return [key[0] for key in sorted(sheet.items(), key = lambda key: key[1]['Annual median wage(2)'], reverse = True)]

# Sorts the information by the hourly mean wage
def sort_by_hourly_mean_wage(sheet: dict(dict())) -> list:
    return [key[0] for key in sorted(sheet.items(), key = lambda key: key[1]['Hourly mean wage'], reverse = True)]

# Sorts the information by the hourly median wage
def sort_by_hourly_median_wage(sheet: dict(dict())) -> list:
    return [key[0] for key in sorted(sheet.items(), key = lambda key: key[1]['Hourly median wage'], reverse = True)]
