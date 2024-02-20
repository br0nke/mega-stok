from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StockListingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_listings'
    verbose_name = _('stock listings')