from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from django.conf import settings


# def render_to_pdf(template_src, context_dict, download=False):
#     # Render the template to HTML
#     template = get_template(template_src)
#     html = template.render(context_dict)
    
#     # Create a BytesIO buffer for the PDF
#     result = BytesIO()
    
#     # Generate PDF with WeasyPrint
#     base_url = settings.STATIC_ROOT  # Base path for static files
#     weasy_html = HTML(string=html, base_url=base_url)
#     weasy_html.write_pdf(result)
    
#     # Create HTTP response
#     response = HttpResponse(content_type='application/pdf')
#     filename = context_dict.get('course_code', 'cover_page') + '.pdf'
#     response['Content-Disposition'] = f'{"attachment" if download else "inline"}; filename="{filename}"'
    
#     # Write PDF to response
#     response.write(result.getvalue())
#     return response

def render_to_pdf(template_src, context_dict, download=False):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    base_url = settings.BASE_DIR
    HTML(string=html, base_url=base_url).write_pdf(result)

    response = HttpResponse(content_type='application/pdf')
    filename = context_dict.get('course_code', 'cover_page') + '.pdf'
    response['Content-Disposition'] = f'{"attachment" if download else "inline"}; filename="{filename}"'
    response.write(result.getvalue())
    return response