from cornice.resource import resource, view

from c2corg_api.models.image import Image, schema_image, schema_update_image
from c2corg_api.views.document import DocumentRest
from c2corg_api.views import validate_id, json_view


@resource(collection_path='/images', path='/images/{id}')
class ImageRest(DocumentRest):

    def collection_get(self):
        return self._collection_get(Image, schema_image)

    @view(validators=validate_id)
    def get(self):
        return self._get(Image, schema_image)

    @json_view(schema=schema_image)
    def collection_post(self):
        return self._collection_post(Image, schema_image)

    @json_view(schema=schema_update_image, validators=validate_id)
    def put(self):
        return self._put(Image, schema_image)
