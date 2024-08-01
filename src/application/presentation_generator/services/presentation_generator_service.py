from abc import ABC
from datetime import datetime

import pytz
from pptx import Presentation

from ...constants import app_constants


class PresentationGeneratorImpl(ABC):
    @staticmethod
    def generate_ppt_document(data: dict, path: str, sections_to_delete: list):
        new_dict = {f"[{key}]": str(value).upper() for key, value in data.items()}
        new_dict['[currentDate]'] = str(datetime.now(pytz.timezone(app_constants.APP_TIMEZONE)).strftime('%m-%d-%Y'))
        new_dict['[projectVersion]'] = '1'

        ppt = Presentation(path)
        print(data)
        return 'works'
