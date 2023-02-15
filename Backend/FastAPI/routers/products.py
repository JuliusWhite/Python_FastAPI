from fastapi import APIRouter

# instantiation of router, in this case the prefix products is directly setted in the instantiation
router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "not found"}})

products_list = ["Product 1", "Product 2",
                 "Product 3", "Product 4", "Product 5"]


# petitions
@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id - 1]
