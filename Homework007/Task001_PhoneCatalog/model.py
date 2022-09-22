guide = {"Alena": "123456789", "Oleg": "987654321", "Vasya": "18185737871"}

def add_record(name, number):
    global guide 
    if name in guide:
        return "default"
    guide[name] = number

def find_by_name(name):
    global guide
    if name in guide:
        return guide[name]
    else:
        return "default"

def view_guide():
    global guide
    print (guide)

def get_guide():
    global guide
    return guide

def exportXML():
    xml = '<xml>\n'
    xml += '<Phone guide:\n>{}</guide>\n'.format(get_guide())
    xml += '</xml>'

    with open('guide.xml', 'w') as page:
        page.write(xml)

    return xml

def exportHTML():
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Phone guide: {} c</p>\n'.format(style, get_guide())
    html += '  </body>\n</html>'
    
    with open('guide.html', 'w') as page:
        page.write(html)

    return html


