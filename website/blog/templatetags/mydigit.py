from django import template
register=template.Library()


def mydigit(value,lent="6"):

        value=str(value)
        while(len(value)<lent):
            value='0'+value
        return value


register.filter(mydigit)
