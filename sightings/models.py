from django.db import models
import datetime


def to_string(obj):
    if obj is None:
        return ''
    else:
        return str(obj)


def parse_int(obj):
    try:
        return int(obj)
    except ValueError:
        return None


def parse_bool(obj):
    if type(obj) != str:
        return None
    elif obj.lower() == 'true':
        return True
    elif obj.lower() == 'false':
        return False
    else:
        return None


class SquirrelManager(models.Manager):
    def create_squirrel(self, X, Y, USID, Hectare, Shift, Date, HSN, Age, PFC, HFC, CPHC, CN, Location, AGSM, SL,
                        Running, Chasing, Climbing, Eating, Foraging, OA, Kuks, Quaas, Moans, TF, TT, Approaches,
                        Indifferent, RF, OI, LL, Zip, CD, BB, CCD, PP):
        try:
            squirrel = self.create(
                X=float(X), Y=float(Y),
                USID=USID, Hectare=Hectare, Shift=Shift,
                Date=datetime.datetime.strptime(Date, "%m%d%Y").date(),
                HSN=parse_int(HSN),
                Age=Age, PFC=PFC, HFC=HFC, CPHC=CPHC, CN=CN, Location=Location,
                AGSM=parse_int(AGSM),
                SL=SL,
                Running=parse_bool(Running), Chasing=parse_bool(Chasing), Climbing=parse_bool(Climbing),
                Eating=parse_bool(Eating), Foraging=parse_bool(Foraging),
                OA=OA,
                Kuks=parse_bool(Kuks), Quaas=parse_bool(Quaas), Moans=parse_bool(Moans), TF=parse_bool(TF),
                TT=parse_bool(TT), Approaches=parse_bool(Approaches), Indifferent=parse_bool(Indifferent),
                RF=parse_bool(RF),
                OI=OI, LL=LL,
                Zip=parse_int(Zip), CD=parse_int(CD), BB=parse_int(BB), CCD=parse_int(CCD), PP=parse_int(PP)
            )
        except Exception as e:
            print(e)
        else:
            squirrel.save()


class Squirrel(models.Model):
    X = models.FloatField(null=True)
    Y = models.FloatField(null=True)
    USID = models.CharField(max_length=100, verbose_name='Unique Squirrel ID', null=True)
    Hectare = models.CharField(max_length=100, null=True)
    Shift = models.CharField(max_length=100, null=True)
    Date = models.DateField(null=True)
    HSN = models.IntegerField(verbose_name='Hectare Squirrel Number', null=True)
    Age = models.CharField(max_length=100, null=True)
    PFC = models.CharField(max_length=100, verbose_name='Primary Fur Color', null=True)
    HFC = models.CharField(max_length=100, verbose_name='Highlight Fur Color', null=True)
    CPHC = models.CharField(max_length=100, verbose_name='Combination of Primary and Highlight Color', null=True)
    CN = models.CharField(max_length=100, verbose_name='Color notes', null=True)
    Location = models.CharField(max_length=100, null=True)
    AGSM = models.IntegerField(verbose_name='Above Ground Sighter Measurement', null=True)
    SL = models.CharField(max_length=100, verbose_name='Specific Location', null=True)
    Running = models.BooleanField(null=True)
    Chasing = models.BooleanField(null=True)
    Climbing = models.BooleanField(null=True)
    Eating = models.BooleanField(null=True)
    Foraging = models.BooleanField(null=True)
    OA = models.CharField(max_length=100, verbose_name='Other Activities', null=True)
    Kuks = models.BooleanField(null=True)
    Quaas = models.BooleanField(null=True)
    Moans = models.BooleanField(null=True)
    TF = models.BooleanField(verbose_name='Tail flags', null=True)
    TT = models.BooleanField(verbose_name='Tail twitches', null=True)
    Approaches = models.BooleanField(null=True)
    Indifferent = models.BooleanField(null=True)
    RF = models.BooleanField(verbose_name='Runs from', null=True)
    OI = models.CharField(max_length=100, verbose_name='Other Interactions', null=True)
    LL = models.CharField(max_length=100, verbose_name='Lat/Long', null=True)
    Zip = models.IntegerField(verbose_name='Zip Codes', null=True)
    CD = models.IntegerField(verbose_name='Community Districts', null=True)
    BB = models.IntegerField(verbose_name='Borough Boundaries', null=True)
    CCD = models.IntegerField(verbose_name='City Council Districts', null=True)
    PP = models.IntegerField(verbose_name='Police Precincts', null=True)
