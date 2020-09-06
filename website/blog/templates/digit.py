from django import template
register=template.Library()

@register.filter
def number(str_number):
        str_number=str(str_number)
        while(len(str_number)<lent):
            str_number='0'+str_number
        return str_number


register.filter(number)
