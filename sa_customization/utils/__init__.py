import frappe


def money_in_arabic_words(number, main_currency="SAR", fraction_currency=None):
    """
    Returns string in words with currency and fraction currency.
    """
    from sa_customization.utils.number2words import number2word

    words = number2word(float(number))
    out = words.validate()

    return out
