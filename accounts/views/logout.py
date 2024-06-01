from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.interactor.user_logout import LogoutUserInteractor
from accounts.presenters.presenter import Presenter
from accounts.storages.account_storage import AccountStorage
from accounts.views import UserLogoutSerializer


@api_view(["POST"])
def logout(request):
    serializer = UserLogoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    access_token = serializer.validated_data["access_token"]

    account_storage = AccountStorage()
    presenter = Presenter()
    interactor = LogoutUserInteractor(account_storage=account_storage)

    response = interactor.logout_user_wrapper(
        access_token=access_token, presenter=presenter
    )

    return response
