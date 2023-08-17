from django.contrib import messages
 
class RequestGenericUtils():
    @staticmethod
    def showSingleErrorMessage(request,message) -> None:
        messages.error(
                request,
                message,
                'danger'
            )

    def showSingleWarnigMessage(request,message) -> None:
        messages.warning(
                request,
                message
            )

    @staticmethod
    def showListErrorMessage(request,messageList) -> None:
        for message in messageList:
                    messages.error(
                            request,
                            message
                        )
    @staticmethod
    def showSingleSuccessMessage(request,message) -> None:
        messages.success(
                request,
                message
            )

    @staticmethod
    def showListSuccessMessage(request,messageList) -> None:
        for message in messageList:
            messages.success(
                    request,
                    message)
    @staticmethod
    def getSingleValueFromPost(POST,valueInputName)->str:
        return  POST.get(valueInputName)

    @staticmethod
    def getListValueFromPost(POST, valueInputName)->list:
        return  POST.getlist(valueInputName)