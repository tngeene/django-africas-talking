number_format = {"0": "+254", "7": "+2547", "1": "+2541", "254": "+254"}


def format_phone_number(phone_number: str) -> str:
    """Handles formatting of various phone
    number inputs into Africas talking format"""
    for key, value in number_format.items():
        if phone_number.startswith(key):
            formatted_num = phone_number.replace(key, value, 1)
            return formatted_num
        return phone_number
