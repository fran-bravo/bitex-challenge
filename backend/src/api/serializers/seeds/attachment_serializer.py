import base64
from src.api.exceptions.no_included_seed_exception import NoIncludedSeedException


class AttachmentSerializer:

    def serialize(self, seed):
        return {
            'data': {
                'type': seed.type(),
                'attributes': self._serialize_file(seed.file),
                'relationships': {
                    'attached_to_seed': {
                        'data': self._serialize_first_included(seed)
                    }
                }
            },
            'included': [self._serialize_included(seed) for seed in seed.included_seeds]
        }

    def _serialize_file(self, file):
        encoded_file = self._encode_file(file)
        return {
            'document': f"data:{file.mimetype};base64,{encoded_file}",
            'document_file_name': file.filename,
            'document_content_type': file.mimetype,
            'document_size': len(encoded_file)
        }

    @staticmethod
    def _encode_file(file):
        return base64.b64encode(file.stream.read())

    @staticmethod
    def _serialize_included(seed):
        return {
            'type': seed.type(),
            'attributes': seed.attributes(),
            'relationships': {
                'attachments': {
                    'data': []
                }
            },
            'id': seed.id
        }

    @staticmethod
    def _serialize_first_included(seed):
        if len(seed.included_seeds) > 0:
            first_seed = seed.included_seeds[0]
            return {
                'type': first_seed.type(),
                'id': first_seed.id
            }
        else:
            raise NoIncludedSeedException('AttachmentSeed needs to have an included seed attached to it')
