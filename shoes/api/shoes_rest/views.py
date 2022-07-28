from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from shoes_rest.models import Shoe, BinVO

# Create your views here.

class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "id",
        "closet_name",
        "bin_number",
        "bin_size",
        
    ]

class ShoeEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
        "manufacturer",
        "model",
        "color",
        "picture",
        "bin"
    ]
    encoders = {
        "bin": BinVOEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes}, 
            encoder=ShoeEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        try:
            bin = BinVO.objects.get(id=content["bin"])
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Bin id"},
                status=400,
            )
        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_detail_shoe(request, pk):
    if request.method == "GET":
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeEncoder,
            safe=False,
        )
        
    elif request.method == "DELETE":
        count, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})

    else:
        content = json.loads(request.body)
        try:
            if "bin" in content:
                bin = BinVO.objects.get(id=content["bin"])
                content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Bin id"},
                status=400,
            )
        
        Shoe.objects.filter(id=pk).update(**content)
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeEncoder,
            safe=False,
        )

