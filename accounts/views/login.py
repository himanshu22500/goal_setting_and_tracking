from rest_framework.decorators import api_view

from accounts.dtos import UserLoginParamsDTO
from accounts.interactor.user_login import LoginUserInteractor
from accounts.presenters.presenter import Presenter
from accounts.storages.account_storage import AccountStorage
from accounts.views import UserLoginSerializer


@api_view(["POST"])
def login(request):
    post_body = request.data
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_login_params_dto = UserLoginParamsDTO(
        user_name=post_body["user_name"],
        password=post_body["password"],
    )

    account_storage = AccountStorage()
    presenter = Presenter()
    interactor = LoginUserInteractor(account_storage=account_storage)
    return interactor.login_user_wrapper(
        user_login_params_dto=user_login_params_dto, presenter=presenter
    )
