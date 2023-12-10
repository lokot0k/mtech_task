from internal.usecase.utils import ResponseExample, ResponseSchema

HTTP_201_CREATED = ResponseSchema(
    status_code=201,
    description='Successfully created',
    example=ResponseExample(successful=True, detail='Successfully created log'),
)

HTTP_418_SOMETHING_IS_WRONG = ResponseSchema(
    status_code=418,
    description='Something is wrong',
    example=ResponseExample(successful=False, detail='Something is wrong'),
)
