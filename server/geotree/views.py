from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import GeoName, GeoData
from django.utils.text import slugify
import math
from django.views import View

SPACE_REPLACE = "-"

# Create your views here.


def geotree(request):
    values = GeoName.objects.order_by("name")
    context = {'geography': values}
    return render(request, "geotree/geoselect.html", context)


def geo_selected(request):
    return HttpResponseRedirect(reverse("geotree:details", args=(request.POST['geography'].replace(" ", SPACE_REPLACE),)))

class DetailView(View):

    def get(self, request, geoname):
        geoname = geoname.replace(SPACE_REPLACE, " ")

        geoname = GeoName.objects.get(name=geoname)
        gd = GeoData.objects.filter(geo_name=geoname)

        geodata = {"year": [{"age": [], "male":[], "female":[]}], "max_count": 0}
        max_count = 0

        for datum in gd:
            try:
                geodata[datum.year]["age"].append(datum.age)
                geodata[datum.year]["male"].append(datum.male)
                geodata[datum.year]["female"].append(datum.female)

                if datum.male > max_count:
                    max_count = datum.male
                if datum.female > max_count:
                    max_count = datum.female

            except KeyError:
                # Haven't yet added this year
                geodata[datum.year] = {"age": [datum.age], "male": [
                    datum.male], "female": [datum.female]}
                if max(datum.male, datum.female) > max_count:
                    max_count = max(datum.male, datum.female)

        geodata["max_count"] = DetailView.round_max(max_count)
        print(geodata["max_count"])

        context = {"name": geoname, "geodata": geodata, 'geography': GeoName.objects.order_by("name")}
        return render(request, "geotree/geodetails.html", context)


    def round_max(max_val):
        """Rounds a value to a number suitable for a maximum in a graph limits. For numbers with a leading digit greater than 3, rounds values up to the nearest 10^(number of digits-1). For other numbers, rounds values to the nearest 10^(number of digits-2).

        Args:
            The value to round (int)

        Raises:
            TypeError: _description_

        Returns:
            _type_: A rounded value
        """
        if not isinstance(max_val, int):
            raise TypeError()

        first_dig = int(str(max_val)[0])
        num_digs = len(str(max_val))

        if first_dig < 3:
            num_digs -= 1

        max_val = math.ceil(max_val/(10**(num_digs-1)))*10**(num_digs-1)

        return max_val
