from src.api.models.domicile import Domicile


class DomicileFactory:

    @staticmethod
    def create(domicile_data):
        return Domicile(
            domicile_data['streetAddress'],
            domicile_data['streetNumber'],
            domicile_data['city'],
            domicile_data['floor'],
            domicile_data['postalCode'],
            domicile_data['country']
        )
