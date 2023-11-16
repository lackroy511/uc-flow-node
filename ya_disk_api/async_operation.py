import ujson
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request

from node.enums import AsyncOpOperations
from util.dict_formatter import form_dict_to_request
from ya_disk_api.yandex_disk_api import BaseYaDiskAPI


class AsyncOperation(BaseYaDiskAPI):

    base_url = 'https://cloud-api.yandex.net/v1/disk/operations/'

    async def get_operation_status(
            self,
            operation_id: str,
            params: Dict[str, str]) -> Dict[str, Any]:

        get_operation_status: Request = await self.make_request(
            json=self.json,
            params=params,
            operation_id=operation_id,
        )
        return ujson.loads(get_operation_status['content'])


class AsyncOperationProcess:

    def __init__(
            self,
            operation: str,
            async_operation: AsyncOperation,
            properties: Dict[str, Any],
            json: NodeRunContext,
    ) -> None:

        self.json: NodeRunContext = json
        self.operation = operation
        self.async_operation = async_operation
        self.properties = properties

    async def execute(self) -> None:

        if self.operation == AsyncOpOperations.get_operation_status:
            await self.__get_operation_status()

    async def __get_operation_status(self) -> None:

        operation_id: str = self.properties['operation_id']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_operation_status_params'],
        )
        status: Dict[str, str] = \
            await self.async_operation.get_operation_status(
                operation_id,
                params,
        )

        await self.json.save_result(status)
