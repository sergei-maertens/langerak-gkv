from .google import geolocation


class GeoLocateMixin(object):
    geo_field = "geom"
    adress_fields = ["address", "postal_code", "city"]

    def save(self, *args, **kwargs):
        need_geo = not self.pk and not getattr(self, self.geo_field)
        # TODO: celery...
        if need_geo:
            address_bits = [getattr(self, attr) for attr in self.adress_fields]
            lat, lng = geolocation(" ".join(address_bits))
            setattr(self, self.geo_field, {"latitude": lat, "longitude": lng})
        super(GeoLocateMixin, self).save(*args, **kwargs)
