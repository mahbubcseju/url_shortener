from .models import StoreUrl


def generate_shortened_url(given_url):
    stored_url = StoreUrl.objects.filter(given_url=given_url)
    processed_url = "http://127.0.0.1:8000/" + str(stored_url[0].id)
    return processed_url


def shortened_url(url_id):
    stored_url = StoreUrl.objects.filter(id=url_id)
    return stored_url[0].given_url
