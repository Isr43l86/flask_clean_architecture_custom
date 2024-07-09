from flask import Blueprint, jsonify, request
from src.application import update_ppt_service


PptGeneratorController = Blueprint(
    'pptGenerator',
    __name__,
    url_prefix='/pptGenerator'
)


@PptGeneratorController.route('/generate', methods=['POST'])
def update_ppt():
    # Obtener los datos del formulario

    # Llamar al servicio para actualizar el PowerPoint
    # ppt_io = update_ppt_service(body)

    # Obtener los datos del formulario

    #    # Validar que el payload contiene los campos necesarios
    #    if 'slide_company_name' not in data or 'array_slides' not in data:
    #         return jsonify({"error": "Invalid payload"}), 400

    data = request.get_json()
    # slide_company_name = data['slide_company_name']
    # array_slides = data['array_slides']

    # #     # Puedes agregar más validaciones aquí según tus necesidades
    # for slide in array_slides:
    #     if 'slide_theme' not in slide or 'slide_title' not in slide or 'slide_content' not in slide:
    #         return jsonify({"error": "Invalid slide format"}), 400

    # Lógica para procesar los datos y actualizar el PowerPoint
    ppt_path = update_ppt_service(data)

    return jsonify({"message": "PowerPoint updated successfully! at path "+ppt_path})
