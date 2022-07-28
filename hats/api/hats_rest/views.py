from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json


from common.json import ModelEncoder
from .models import LocationVO, Hat

class LocationVOEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "closet_name",
        "section_number",
        "shelf_number",
    ]

class HatListEncoder(ModelEncoder):
    model = Hat
    properties = [
        "name",
        "style",
        "id",
    ]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "name",
        "fabric",
        "style",
        "color",
        "picture_url",
        "location",
        "id",
    ]
    encoders = {
        "location": LocationVOEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            location_href = content["location"]
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location"},
                status=400,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET"])
def api_show_hats(request, pk):
    if request.method == "GET":
        try:
            hat = Hat.objects.get(id=pk)
            return JsonResponse(
                hat,
                encoder=HatDetailEncoder,
                safe=False
            )
        except Hat.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400
            )

    else:
        count, _ = Hat.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})