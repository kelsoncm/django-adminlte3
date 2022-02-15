from django.db.models import Model
from django.db.models import \
    SmallIntegerField, IntegerField, BigIntegerField, PositiveSmallIntegerField, PositiveIntegerField, PositiveBigIntegerField, \
    DecimalField, FloatField, \
    BooleanField, \
    CharField, TextField, SlugField, \
    DateField, TimeField, DateTimeField, DurationField, \
    EmailField, GenericIPAddressField, URLField, \
    JSONField, BinaryField, UUIDField, \
    ForeignKey, OneToOneField, ManyToManyField, \
    FilePathField, FileField, ImageField, CASCADE
from django.contrib.auth.models import User, Group, Permission
from django.conf import settings


class AllDataTypes(Model):
    small_integer_field = SmallIntegerField()
    integer_field = IntegerField()
    big_integer_field = BigIntegerField()
    positive_small_integer_field = PositiveSmallIntegerField()
    positive_integer_field = PositiveIntegerField()
    positive_big_integer_field = PositiveBigIntegerField()
    decimal_field = DecimalField(max_digits=10, decimal_places=2, )
    float_field = FloatField()
    boolean_field = BooleanField()
    null_boolean_field = BooleanField(null=True, blank=True)
    char_field = CharField(max_length=255)
    text_field = TextField()
    slug_field = SlugField()
    date_field = DateField()
    time = TimeField()
    date_time_field = DateTimeField()
    duration_field = DurationField()
    email_field = EmailField()
    generic_ip_address_field = GenericIPAddressField()
    url_field = URLField()
    json_field = JSONField()
    binary_field = BinaryField()
    uuid_field = UUIDField()
    foreign_key_field = ForeignKey(Group, on_delete=CASCADE)
    one_to_one_field = OneToOneField(User, on_delete=CASCADE)
    many_to_many_field = ManyToManyField(Permission)
    file_path_field = FilePathField(path=settings.PROJECT_DIR)
    file_field = FileField()
    image_field = ImageField()
