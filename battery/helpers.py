def battery_service_year(date, duration):
    service_year = date.replace(year = date.year + duration)
    return service_year