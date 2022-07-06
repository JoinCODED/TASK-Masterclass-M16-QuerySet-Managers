from decimal import Decimal
from typing import TYPE_CHECKING, Optional, Union

from django.db import models

from shared.models import TimestampMixin


if TYPE_CHECKING:
    from django.db.models.expressions import Combinable
    from django.db.models.manager import RelatedManager

    from bands.models import BandForeignKey
    from shared.models import GenreM2M

    AlbumForeignKey = models.ForeignKey[Union["Album", "Combinable"], "Album"]


class Album(TimestampMixin, models.Model):
    songs: "RelatedManager[Song]"

    name = models.CharField(max_length=50)
    band: "BandForeignKey" = models.ForeignKey(
        "bands.Band", on_delete=models.CASCADE, related_name="albums"
    )
    genre: "GenreM2M" = models.ManyToManyField(
        "shared.Genre", related_name="albums"
    )
    purchase_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_top_ten(cls) -> models.QuerySet["Album"]:
        return cls.objects.order_by("-purchase_count")[:10]

    @property
    def singles(self) -> models.QuerySet["Song"]:
        return self.songs.filter(is_single=True)

    @property
    def features(self) -> models.QuerySet["Song"]:
        return self.songs.filter(name__icontains="feat")

    @property
    def top_single(self) -> Optional["Song"]:
        return self.singles.order_by("-purchase_count").first()

    @property
    def price(self) -> Decimal:
        return self.songs.aggregate(total=models.Sum("price"))["total"]


class Song(TimestampMixin, models.Model):
    name = models.CharField(max_length=100)
    album: "AlbumForeignKey" = models.ForeignKey(
        "albums.Album", on_delete=models.CASCADE, related_name="songs"
    )
    genre: "GenreM2M" = models.ManyToManyField(
        "shared.Genre", related_name="songs"
    )
    price = models.DecimalField(max_digits=6, decimal_places=3)
    purchase_count = models.PositiveIntegerField(default=0)
    is_single = models.BooleanField()

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_top_ten(cls) -> models.QuerySet["Song"]:
        return cls.objects.order_by("-purchase_count")[:10]
