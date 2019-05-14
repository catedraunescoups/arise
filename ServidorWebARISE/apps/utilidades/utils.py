import os
import datetime
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from yattag import Doc
from arise.settings import AUX, STATICFILES_DIRS
from django.template.defaultfilters import date as _date

def get_html_head_section():
    doc, tag, text = Doc().tagtext()
    
    with tag('head'):
        with tag('title'):
            text('{{ titulo }}')
    
    res = '<!DOCTYPE html><html lang="es">'+doc.getvalue()+'<body>'
    doc, tag, text = Doc().tagtext()
    
    with tag('div', ('id','header_content')):
        text('')
    with tag('div', ('id','footer_content')):
        doc.asis('Página <pdf:pagenumber> de <pdf:pagecount>\n')
    return res+doc.getvalue()

def get_table_columns(table):
    val = []
    for i in table:
        val.append(len(i))
    return val

def generarTabla(estructura, titulo, borde=1):
    doc, tag, text = Doc().tagtext()
    columnas = get_table_columns(estructura)
    m = max(columnas) - 1
    valor = ''
    
    doc.stag('br')
    with tag('h3', ('class','strong')):
        text(titulo)
    with tag('table', border=str(borde), cellpadding='4'):
        for i in range(0, len(estructura)):
            with tag('tr'):
                for j in range(0,columnas[i]):
                    valor = str(estructura[i][j])
                    print(valor)
                    if(valor != 'None'):
                        l = len(valor)
                        if valor.startswith(':s:', 0 ,l):
                            with tag('td', colspan=str(m), id="id_j"):
                                text(valor[3:])
                        else:
                            if valor.startswith(':b:', 0 ,l):
                                with tag('td', id='id_b'):
                                    text(valor[3:])
                            else:
                                with tag('td', id='id_c'):
                                    text(valor)
                    else:
                        with tag('td', id='id_c'):
                            text('')
    res = doc.getvalue()
    return res

def generarTituloPrincipal(titulo):
    doc, tag, text = Doc().tagtext()
    
    with tag('h3', ('class', 'header')):
        text(titulo)
    res = doc.getvalue()
    return res

def generarTitulo(titulo):
    doc, tag, text = Doc().tagtext()
    
    doc.stag('br')
    with tag('h3'):
        text(titulo)
    res = doc.getvalue()
    return res

def crear_html(nombre):
    try:
        html_file = open(AUX+nombre, 'w', encoding='utf-8')
        html_file.write(get_html_head_section())
        return html_file
    except IOError:
        print("No se puede crear el fichero "+nombre)
        return None

def guardar_html(file, texto):
        if os.path.exists(file.name):
            file.write(texto)
        else:
            print("No se puede escribir en el fichero "+file.name)

def finalizar_html(file):
        # Finalizado de fichero
        if os.path.exists(file.name):
            file.write('</body></html>')
            file.close()
            return True
        else:
            print("No se puede leer el fichero "+file.name)
            return False

def eliminar_html(file):
    if os.path.exists(file.name):
        os.remove(file.name)

def existe_html(nombre):
    if os.path.exists(AUX+nombre):
        return True

def render_to_pdf(orientacion, template_src, context_dict={}):
    css=STATICFILES_DIRS[0]+'/css/pdf_report_template_'+str(orientacion)+'.css'
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, default_css=open(css,'r').read())
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        return response
    return None

def current_time():
    return datetime.datetime.now()

def formated_age(fec_nacimiento):
    if fec_nacimiento != None:
        return  _date(fec_nacimiento, "d , F , Y").replace(',', 'de')
    return None