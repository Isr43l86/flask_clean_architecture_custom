from flask import Blueprint, request, send_file

from src.application import app_constants, WordGeneratorServiceImpl

DocumentGeneratorController = Blueprint(
    'word-generator',
    __name__,
    url_prefix=f'/{app_constants.APP_CONTEXT}/{app_constants.APP_VERSION}/document-generator'
)


@DocumentGeneratorController.route('/word', methods=['POST'])
def word_generator():
    file_stream, filename = WordGeneratorServiceImpl.generate_word_document(
        request.json['template_data'],
        request.json['template_path'],
        request.json['sections_to_delete']
    )
    return send_file(file_stream,
                     as_attachment=True,
                     download_name=filename,
                     mimetype=app_constants.MIME_TYPE_WORD)
