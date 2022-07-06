from collections.abc import Sequence
from enum import IntEnum, auto
from typing import TYPE_CHECKING

from django.db import models


if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

    from albums.models import Album, Song
    from bands.models import Band

GenreM2M = models.ManyToManyField[Sequence["Genre"], "RelatedManager[Genre]"]


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GenreBy(IntEnum):
    album = auto()
    song = auto()
    revenue = auto()


class Genre(TimestampMixin, models.Model):
    albums: "RelatedManager[Album]"
    bands: "RelatedManager[Band]"
    songs: "RelatedManager[Song]"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_top_ten(cls, by: GenreBy) -> models.QuerySet["Genre"]:
        if by == GenreBy.album:
            qs = cls.objects.all()
        elif by == GenreBy.song:
            qs = cls.objects.all()
        elif by == GenreBy.revenue:
            qs = cls.objects.all()
        else:
            raise NotImplementedError

        return qs
