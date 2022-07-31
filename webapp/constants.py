from django.utils.translation import gettext_lazy as _


class GenderVariants:
    MALE = 'male'
    FEMALE = 'female'
    OTHER = None

    CHOICES = (
        (MALE, _('MALE'),),
        (FEMALE, _('FEMALE'),),
        (OTHER, _('Other'),),
    )