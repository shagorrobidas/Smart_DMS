from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict, download=False):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        response = HttpResponse(
            result.getvalue(), content_type='application/pdf')
        if download:
            response['Content-Disposition'] = 'attachment; filename="cover_page.pdf"'  # noqa
        return response
    return HttpResponse("Error generating PDF", status=400)
