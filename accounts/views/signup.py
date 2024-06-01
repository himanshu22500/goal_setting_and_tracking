from rest_framework.decorators import api_view

from accounts.dtos import CreateUserParamsDTO
from accounts.interactor.create_user import CreateUserInteractor
from accounts.presenters.presenter import Presenter
from accounts.storages.account_storage import AccountStorage
from accounts.views import CreateUserSerializer


@api_view(["POST"])
def create_user(request):
    post_body = request.data
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    create_user_params_dto = CreateUserParamsDTO(
        user_name=post_body["user_name"],
        password=post_body["password"],
        email=post_body["email"],
    )

    account_storage = AccountStorage()
    presenter = Presenter()
    interactor = CreateUserInteractor(account_storage=account_storage)
    return interactor.create_account_user_wrapper(
        create_user_params_dto=create_user_params_dto, presenter=presenter
    )
