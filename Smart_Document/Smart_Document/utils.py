# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


# def render_to_pdf(template_src, context_dict, download=False):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
#     if not pdf.err:
#         response = HttpResponse(
#             result.getvalue(), content_type='application/pdf')
#         if download:
#             response['Content-Disposition'] = 'attachment; filename="cover_page.pdf"'  # noqa
#         return response
#     return HttpResponse("Error generating PDF", status=400)


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import os

def render_to_pdf(template_src, context_dict, download=False):
    # Render the template to HTML
    template = get_template(template_src)
    html = template.render(context_dict)
    
    # Create a BytesIO buffer for the PDF
    result = BytesIO()
    
    # Generate PDF with WeasyPrint
    base_url = settings.STATIC_ROOT  # Base path for static files
    weasy_html = HTML(string=html, base_url=base_url)
    weasy_html.write_pdf(result)
    
    # Create HTTP response
    response = HttpResponse(content_type='application/pdf')
    filename = context_dict.get('course_code', 'cover_page') + '.pdf'
    response['Content-Disposition'] = f'{"attachment" if download else "inline"}; filename="{filename}"'
    
    # Write PDF to response
    response.write(result.getvalue())
    return response