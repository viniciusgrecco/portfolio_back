from fastapi import APIRouter, Response, Request, requests
from use_cases.tests.test.test_use_case import TestUseCase

get_ticker_use_case = TestUseCase()

router = APIRouter()

@router.get("/tickers/test")
def get_ticker(response: Response, request: Request):
    return get_ticker_use_case.execute(response,request)