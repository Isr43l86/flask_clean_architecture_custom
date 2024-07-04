from flask import Blueprint, jsonify
from src.application import update_ppt_service


PptGeneratorController = Blueprint(
    'pptGenerator',
    __name__,
    url_prefix='/pptGenerator'
)


@PptGeneratorController.route('/generate', methods=['POST'])
def update_ppt():
    # Obtener los datos del formulario
    # slide_title = request.form.get('title', 'New Slide Title')
    # slide_content = request.form.get(
    #     'content', 'This is the content of the new slide.')

    # Llamar al servicio para actualizar el PowerPoint
    ppt_io = update_ppt_service()

    return jsonify({"message": "PowerPoint updated successfully! at path  " + ppt_io})
