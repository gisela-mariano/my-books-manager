from src.core.middlewares.models.enum.type import ErrorType
from src.core.utils.exceptions.base_exception import BaseException


class AlreadyRegisteredError(BaseException):
    def __init__(
        self,
        message="Face already registered",
        default_message="Face already registered",
        raised_error="AlreadyRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class ApiServiceCodeError(BaseException):
    def __init__(
        self,
        message="Api has code error",
        default_message="Api has code error",
        raised_error="ApiServiceCodeError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class AssetAlreadyRegisteredError(BaseException):
    def __init__(
        self,
        message="Asset already is registered",
        default_message="Asset already is registered",
        raised_error="AssetAlreadyRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class AssetNotFoundError(BaseException):
    def __init__(
        self,
        message="No asset found for validation",
        default_message="No asset found for validation",
        raised_error="AssetNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class AuthenticatorNotFoundError(BaseException):
    def __init__(
        self,
        message="Error to authenticate, authenticate not found",
        default_message="Error to authenticate, authenticate not found",
        raised_error="AuthenticatorNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class AuthUnauthorizedError(BaseException):

    def __init__(
        self,
        message="Error to authenticate, incorrect or unregistered credentials",
        default_message="Error to authenticate, incorrect or unregistered credentials",
        raised_error="AuthUnauthorizedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class BankNotFoundError(BaseException):
    def __init__(
        self,
        message="Not possible to find this bank",
        default_message="Not possible to find this bank",
        raised_error="BankNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class BucketError(BaseException):
    def __init__(
        self,
        message="Failed in get bucket",
        default_message="Failed in get bucket",
        raised_error="BucketError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class CNPJNotFoundError(BaseException):
    def __init__(
        self,
        message="Cnpj not found",
        default_message="Cnpj not found",
        raised_error="CNPJNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class CardNotFoundError(BaseException):
    def __init__(
        self,
        message="Card could not be found",
        default_message="Card could not be found",
        raised_error="CardNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class CertificateNotFoundError(BaseException):
    def __init__(
        self,
        message="Certificate not found",
        default_message="Certificate not found",
        raised_error="CertificateNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class ClassError(BaseException):
    def __init__(
        self,
        message="Class not found on routine",
        default_message="Class not found on routine",
        raised_error="ClassError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ClassificationError(BaseException):
    def __init__(
        self,
        message="Error to classificate your data",
        default_message="Error to classificate your data",
        raised_error="ClassificationError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class ColumnNotFoundError(BaseException):
    def __init__(
        self,
        message="Column not found",
        default_message="Column not found",
        raised_error="ColumnNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ColumnValidationError(BaseException):
    def __init__(
        self,
        message="Column validation error",
        default_message="Column validation error",
        raised_error="ColumnValidationError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class CompanyNotAllowedError(BaseException):
    def __init__(
        self,
        message="Company is not allowed",
        default_message="Company is not allowed",
        raised_error="CompanyNotAllowedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class ConnectionDbError(BaseException):
    def __init__(
        self,
        message="Data base connection with error",
        default_message="Data base connection with error",
        raised_error="ConnectionDbError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class CorruptedFileError(BaseException):
    def __init__(
        self,
        message="File is corrupted",
        default_message="File is corrupted",
        raised_error="CorruptedFileError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class CreateLedgerError(BaseException):
    def __init__(
        self,
        message="Create ledger exception",
        default_message="Create ledger exception",
        raised_error="CreateLedgerError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class CredentialError(BaseException):
    def __init__(
        self,
        message="Failed to find your crendencials",
        default_message="Failed to find your crendencials",
        raised_error="CredentialError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class DaskError(BaseException):
    def __init__(
        self,
        message="Error to Authenticate Dask",
        default_message="Error to Authenticate Dask",
        raised_error="DaskError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class DataBaseNotFoundError(BaseException):
    def __init__(
        self,
        message="Database not found",
        default_message="Database not found",
        raised_error="DataBaseNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class DataSourceError(BaseException):
    def __init__(
        self,
        message="Data source error",
        default_message="Data source error",
        raised_error="DataSourceError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class DbError(BaseException):
    def __init__(
        self,
        message="Db with error",
        default_message="Db with error",
        raised_error="DbError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class CreateAHPTableError(BaseException):
    def __init__(
        self,
        message="Error onto create AHP table",
        default_message="Error onto create AHP table",
        raised_error="CreateAHPTableError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class CreateKeyError(BaseException):
    def __init__(
        self,
        message="Error to create the key",
        default_message="Error to create the key",
        raised_error="CreateKeyError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class RuleSelectionError(BaseException):
    def __init__(
        self,
        message="Rule selection error",
        default_message="Rule selection error",
        raised_error="RuleSelectionError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class UpdatingKeysError(BaseException):
    def __init__(
        self,
        message="Error to update Keys",
        default_message="Error to update Keys",
        raised_error="UpdatingKeysError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ExpatError(BaseException):
    def __init__(
        self,
        message="Failed while parsing XML",
        default_message="Failed while parsing XML",
        raised_error="ExpatError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class ExtensionError(BaseException):
    def __init__(
        self,
        message="The extension provided isn't allowed on processor",
        default_message="The extension provided isn't allowed on processor",
        raised_error="ExtensionError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FailedApiServiceCodeError(BaseException):
    def __init__(
        self,
        message="Fail inside process of api-service-code",
        default_message="Fail inside process of api-service-code",
        raised_error="FailedApiServiceCodeError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class FieldsIsEmptyError(BaseException):
    def __init__(
        self,
        message="fields cannot be an empty list",
        default_message="fields cannot be an empty list",
        raised_error="FieldsIsEmptyError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FileEmptyError(BaseException):
    def __init__(
        self,
        message="File is empty",
        default_message="File is empty",
        raised_error="FileEmptyError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FileError(BaseException):
    def __init__(
        self,
        message="File with error",
        default_message="File with error",
        raised_error="FileError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FileNotExecutedError(BaseException):
    def __init__(
        self,
        message="File was not executed",
        default_message="File was not executed",
        raised_error="FileNotExecutedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FileNotFoundError(BaseException):
    def __init__(
        self,
        message="Error to find specific file",
        default_message="Error to find specific file",
        raised_error="FileNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FirebaseDocumentNotFoundError(BaseException):
    def __init__(
        self,
        message="You document doesn't exist on the path",
        default_message="You document doesn't exist on the path",
        raised_error="FirebaseDocumentNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class GetLedgersError(BaseException):
    def __init__(
        self,
        message="Exception on ledger get",
        default_message="Exception on ledger get",
        raised_error="GetLedgersError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class InputValidationError(BaseException):
    def __init__(
        self,
        message="Input validation error",
        default_message="Input validation error",
        raised_error="InputValidationError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class InvalidDataFormatError(BaseException):
    def __init__(
        self,
        message="Data format is invalid",
        default_message="Data format is invalid",
        raised_error="InvalidDataFormatError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class InvalidInputProvidedError(BaseException):
    def __init__(
        self,
        message="Input invalid provided",
        default_message="Input invalid provided",
        raised_error="InvalidInputProvidedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class InvalidPayloadSecretsError(BaseException):
    def __init__(
        self,
        message="Invalid payload secret",
        default_message="Invalid payload secret",
        raised_error="InvalidPayloadSecretsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class InvalidTokenError(BaseException):
    def __init__(
        self,
        message="Your token is invalid",
        default_message="Your token is invalid",
        raised_error="InvalidTokenError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class LedgerAlreadyExistsError(BaseException):
    def __init__(
        self,
        message="There is already a ledger for period and cnpj",
        default_message="There is already a ledger for period and cnpj",
        raised_error="LedgerAlreadyExistsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class LedgerNotFoundError(BaseException):
    def __init__(
        self,
        message="Ledger not found",
        default_message="Ledger not found",
        raised_error="LedgerNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class LedgerSumNotZeroError(BaseException):
    def __init__(
        self,
        message="Ledger sum is not zero",
        default_message="Ledger sum is not zero",
        raised_error="LedgerSumNotZeroError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class MetadataError(BaseException):
    def __init__(
        self,
        message="Metadata error",
        default_message="Metadata error",
        raised_error="MetadataError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class MoreThenOneFaceError(BaseException):
    def __init__(
        self,
        message="More than one face",
        default_message="More than one face",
        raised_error="MoreThenOneFaceError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class MoreThenOneFaceCompareError(BaseException):
    def __init__(
        self,
        message="More than one face to compare",
        default_message="More than one face to compare",
        raised_error="MoreThenOneFaceCompareError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class NerError(BaseException):
    def __init__(
        self,
        message="Model load fail or Fail in NER extraction",
        default_message="Model load fail or Fail in NER extraction",
        raised_error="NerError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoCompanyRegisteredError(BaseException):
    def __init__(
        self,
        message="The company is not registered",
        default_message="The company is not registered",
        raised_error="NoCompanyRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoFaceInImageError(BaseException):
    def __init__(
        self,
        message="No face in image",
        default_message="No face in image",
        raised_error="NoFaceInImageError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoFaceInImageCompareError(BaseException):
    def __init__(
        self,
        message="Please make sure your image has face to compare",
        default_message="Please make sure your image has face to compare",
        raised_error="NoFaceInImageCompareError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoKeyFoundError(BaseException):
    def __init__(
        self,
        message="Key not found",
        default_message="Key not found",
        raised_error="NoKeyFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoRegisterError(BaseException):
    def __init__(
        self,
        message="No registrer found",
        default_message="No registrer found",
        raised_error="NoRegisterError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoRulesRegisteredError(BaseException):
    def __init__(
        self,
        message="No rules registred",
        default_message="No rules registred",
        raised_error="NoRulesRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoTrainedModelError(BaseException):
    def __init__(
        self,
        message="No trained model found",
        default_message="No trained model found",
        raised_error="NoTrainedModelError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class NotFoundEquityAccountsError(BaseException):
    def __init__(
        self,
        message="Equity accounts are not found",
        default_message="Equity accounts are not found",
        raised_error="NotFoundEquityAccountsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class NotInDataBaseError(BaseException):
    def __init__(
        self,
        message="Image is not in database",
        default_message="Image is not in database",
        raised_error="NotFaceInDataBaseError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class OcrError(BaseException):
    def __init__(
        self,
        message="Failed to execute OCR on file",
        default_message="Failed to execute OCR on file",
        raised_error="OcrError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class OfxError(BaseException):
    def __init__(
        self,
        message="Organization not found in Ofx document",
        default_message="Organization not found in Ofx document",
        raised_error="OfxError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class PageAlreadyLoadedError(BaseException):
    def __init__(
        self,
        message="Page already loaded",
        default_message="Page already loaded",
        raised_error="PageAlreadyLoadedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class PageDataTooLagerError(BaseException):
    def __init__(
        self,
        message="Payload Too Large, server limit is 20MB",
        default_message="Payload Too Large, server limit is 20MB",
        raised_error="PageDataTooLagerError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ParameterError(BaseException):
    def __init__(
        self,
        message="Failed to pass the right parameter",
        default_message="Failed to pass the right parameter",
        raised_error="ParameterError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class PasswordError(BaseException):
    def __init__(
        self,
        message="Password with Error",
        default_message="Password with Error",
        raised_error="PasswordError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class PipeNotFoundError(BaseException):
    def __init__(
        self,
        message="Pipe not found",
        default_message="Pipe not found",
        raised_error="PipeNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class PipefyError(BaseException):
    def __init__(
        self,
        message="Exception on pipefy",
        default_message="Exception on pipefy",
        raised_error="PipefyError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ProjectNotFoundError(BaseException):
    def __init__(
        self,
        message="Project not found",
        default_message="Project not found",
        raised_error="ProjectNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class PubSubError(BaseException):
    def __init__(
        self,
        message="Failed to push the message",
        default_message="Failed to push the message",
        raised_error="PubSubError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ReclassificationError(BaseException):
    def __init__(
        self,
        message="Failed to reclassify the request",
        default_message="Failed to reclassify the request",
        raised_error="ReclassificationError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ReportC100C170NotExistsError(BaseException):
    def __init__(
        self,
        message="Report C100C17 not exists",
        default_message="Report C100C17 not exists",
        raised_error="ReportC100C170NotExistsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class RequiredFieldError(BaseException):
    def __init__(
        self,
        message="Required field error",
        default_message="Required field error",
        raised_error="RequiredFieldError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class SchemaAlreadyRegisteredError(BaseException):
    def __init__(
        self,
        message="Schema already registered",
        default_message="Schema already registered",
        raised_error="SchemaAlreadyRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SchemaError(BaseException):
    def __init__(
        self,
        message="Error on schema",
        default_message="Error on schema",
        raised_error="SchemaError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SchemaExistsError(BaseException):
    def __init__(
        self,
        message="Schema already exists",
        default_message="Schema already exists",
        raised_error="SchemaExistsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SchemaNotExistsError(BaseException):
    def __init__(
        self,
        message="Schema doesn't exists",
        default_message="Schema doesn't exists",
        raised_error="SchemaNotExistsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SchemaNotFoundError(BaseException):
    def __init__(
        self,
        message="Schema not found",
        default_message="Schema not found",
        raised_error="SchemaNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SecretNotFoundError(BaseException):
    def __init__(
        self,
        message="Secret is not found",
        default_message="Secret is not found",
        raised_error="SecretNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SecretServiceUnavailableError(BaseException):
    def __init__(
        self,
        message="Secret Service is unavailable,try again later",
        default_message="Secret Service is unavailable,try again later",
        raised_error="SecretServiceUnavailableError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class SecretUnavailableError(BaseException):
    def __init__(
        self,
        message="Secret is not avaliable",
        default_message="Secret is not avaliable",
        raised_error="SecretUnavailableError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class SheetModelNotFoundError(BaseException):
    def __init__(
        self,
        message="Sheet model not found",
        default_message="Sheet model not found",
        raised_error="SheetModelNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class TableAlreadyRegisteredError(BaseException):
    def __init__(
        self,
        message="Table already registered",
        default_message="Table already registered",
        raised_error="TableAlreadyRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class TableNotFoundError(BaseException):
    def __init__(
        self,
        message="Table not exists",
        default_message="Table not exists",
        raised_error="TableNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class TextExtractionError(BaseException):
    def __init__(
        self,
        message="Text extraction error",
        default_message="Text extraction error",
        raised_error="TextExtractionError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class TrackingEndpointError(BaseException):
    def __init__(
        self,
        message="Failed to tracking endpoint",
        default_message="Failed to tracking endpoint",
        raised_error="TrackingEndpointError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class TriggerLedgerError(BaseException):
    def __init__(
        self,
        message="Ledger exception trigger",
        default_message="Ledger exception trigger",
        raised_error="TriggerLedgerExceptionError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type="system ",
            acknowledge=True,
            metadata=metadata,
        )


class TypeError(BaseException):
    def __init__(
        self,
        message="Invalid type",
        default_message="Invalid type",
        raised_error="TypeError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class UnicodeDecodeError(BaseException):
    def __init__(
        self,
        message="The file is corrupt or is not a XML or JSON file",
        default_message="The file is corrupt or is not a XML or JSON file",
        raised_error="UnicodeDecodeError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class UploadError(BaseException):
    def __init__(
        self,
        message="Upload with error",
        default_message="Upload with error",
        raised_error="UploadError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class UploadLedgerError(BaseException):
    def __init__(
        self,
        message="Exception on ledger upload",
        default_message="Exception on ledger upload",
        raised_error="UploadLedgerExceptionError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class ValidationError(BaseException):
    def __init__(
        self,
        message="Validation error",
        default_message="Validation error",
        raised_error="ValidationError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class ValidationPayloadError(BaseException):
    def __init__(
        self,
        message="Validation payload error",
        default_message="Validation payload error",
        raised_error="ValidationPayloadError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class VersionModelError(BaseException):
    def __init__(
        self,
        message="Version model not found",
        default_message="Version model not found",
        raised_error="VersionModelError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class WithoutConnectionError(BaseException):
    def __init__(
        self,
        message="Connection is failed",
        default_message="Connection is failed",
        raised_error="WithoutConnectionError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class WordNotInCorpusError(BaseException):
    def __init__(
        self,
        message="Word not found on embeddings vocab",
        default_message="Word not found on embeddings vocab",
        raised_error="WordNotInCorpusError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class WorkspaceNotFoundError(BaseException):
    def __init__(
        self,
        message="Could not find workspaceId refered to this workspaceName",
        default_message="Could not find workspaceId refered to this workspaceName",
        raised_error="WorkspaceNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ZohoAnalyticsError(BaseException):
    def __init__(
        self,
        message="Zoho Analytics Internal Error",
        default_message="Zoho Analytics Internal Error",
        raised_error="ZohoAnalyticsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class EnvironmentPropertyError(BaseException):
    def __init__(
        self,
        message="The environment property required",
        default_message="The environment property required",
        raised_error="EnvironmentPropertyError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class CaptchaError(BaseException):
    def __init__(
        self,
        message="Error in resolve captcha ",
        default_message="Error in resolve captcha ",
        raised_error="CaptchaError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class EmptyPropertiesError(BaseException):
    def __init__(
        self,
        message="The schema has to be built inside of properties",
        default_message="The schema has to be built inside of properties",
        raised_error="EmptyPropertiesError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class InvalidIntegrationURLError(BaseException):
    def __init__(
        self,
        message="The URL sent is invalid.",
        default_message="The URL sent is invalid.",
        raised_error="InvalidIntegrationURLError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class IntegrationFailedError(BaseException):
    def __init__(
        self,
        message="Integration process failed",
        default_message="Integration process failed",
        raised_error="IntegrationFailedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=False,
            metadata=metadata,
        )


class RouteNotFoundError(BaseException):
    def __init__(
        self,
        message="Route not found",
        default_message="Route not found",
        raised_error="RouteNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class DocumentNotFoundError(BaseException):
    def __init__(
        self,
        message="Document Not Found",
        default_message="Document Not Found",
        raised_error="DocumentNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class DocumentParserError(BaseException):
    def __init__(
        self,
        message="Failed to parse the document",
        default_message="Failed to parse the document",
        raised_error="DocumentParserError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class QuotationAlreadyBeenAnswered(BaseException):
    def __init__(
        self,
        message="This quotation has already been answered by someone else.",
        default_message="This quotation has already been answered by someone else.",
        raised_error="QuotationAlreadyBeenAnswered",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class PageNotFoundError(BaseException):
    def __init__(
        self,
        message="Page not found",
        default_message="Page not found",
        raised_error="PageNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class NoSuchFieldError(BaseException):
    def __init__(
        self,
        message="Failed inserting to table",
        default_message="Failed inserting to table",
        raised_error="NoSuchFieldError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=False,
            metadata=metadata,
        )


class IndexError(BaseException):
    def __init__(
        self,
        message="failed to recognize index",
        default_message="failed to recognize index",
        raised_error="IndexError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class CertificateDecodeError(BaseException):
    def __init__(
        self,
        message="Error json decode certificate consult",
        default_message="Error json decode certificate consult",
        raised_error="CertificateDecodeError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class FileWithoutContentError(BaseException):
    def __init__(
        self,
        message="file without valid content",
        default_message="file without valid content",
        raised_error="FileWithoutContentError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class FileAlreadyExistsError(BaseException):
    def __init__(
        self,
        message="File already exists",
        default_message="File already exists",
        raised_error="FileAlreadyExistsError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class InvalidLinkValueError(BaseException):
    def __init__(
        self,
        message="Invalid link value",
        default_message="Invalid link value",
        raised_error="InvalidLinkValueError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class CityNotImplementedError(BaseException):
    def __init__(
        self,
        message="Authenticity not implemented for this city",
        default_message="Authenticity not implemented for this city",
        raised_error="CityNotImplementedError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class WebServiceResponseError(BaseException):
    def __init__(
        self,
        message="Web service not responding",
        default_message="Web service not responding",
        raised_error="WebServiceResponseError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ExpiredAccess(BaseException):
    def __init__(
        self,
        message="Access expired when trying to access the website",
        default_message="Access expired when trying to access the website",
        raised_error="ExpiredAccess",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class BlockedAccess(BaseException):
    def __init__(
        self,
        message="Access blocked when trying to access the website",
        default_message="Access blocked when trying to access the website",
        raised_error="BlockedAccess",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class PendenciesToResolve(BaseException):
    def __init__(
        self,
        message="There are pendencies that need to be resolved before continuing the process",
        default_message="There are pendencies that need to be resolved before continuing the process",
        raised_error="PendenciesToResolve",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class ProductNotFoundError(BaseException):
    def __init__(
        self,
        message="Requested product not found.",
        default_message="Requested product not found.",
        raised_error="ProductNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )


class NumberNotFoundError(BaseException):
    def __init__(
        self,
        message="Requested number not found.",
        default_message="Requested number not found.",
        raised_error="NumberNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=True,
            metadata=metadata,
        )
