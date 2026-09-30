def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_positive(value):
    if is_number(value):
        return float(value) >= 0
    return False

def valid_ph(value):
    if not is_number(value):
        return False
    ph = float(value)
    return 0 <= ph <= 14

def valid_date(date):
    parts = date.split("-")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 4:
        return False
    if len(parts[1]) != 2:
        return False
    if len(parts[2]) != 2:
        return False
    return True
    
def valid_location(location):
    return len(location.strip()) > 0
