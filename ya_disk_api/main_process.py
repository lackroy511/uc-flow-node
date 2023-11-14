from typing import Any, Dict
from uc_flow_nodes.schemas import NodeRunContext
from node.enums import Resources

from ya_disk_api.async_operation import (
    AsyncOperation, 
    AsyncOperationProcess)

from ya_disk_api.files_and_folders import (
    FilesAndFolders, 
    FilesAndFoldersProcess)

from ya_disk_api.public_files_and_folders import (
    PublicFilesAndFolders, 
    PublicFilesAndFoldersProcess)

from ya_disk_api.trash import (
    Trash, 
    TrashProcess)

from ya_disk_api.user_disk import (
    UserDisk, 
    UserDiskProcess)


class MainProcess:
    
    def __init__(
            self, 
            ya_disk_token: str, 
            resource: str,
            properties: Dict[str, Any],
            json: NodeRunContext) -> None:
    
        self.ya_disk_token = ya_disk_token
        self.resource = resource
        self.properties = properties
        self.json = json
        
    async def execute(self) -> None:
        
        if self.resource == Resources.user_disk:
            await self.__run_user_disk_process()
                
        if self.resource == Resources.files_and_folders:
            await self.__run_files_and_folders_process()
        
        if self.resource == Resources.public_files_and_folders:
            await self.__run_public_files_and_folders_process()
        
        if self.resource == Resources.trash:
            await self.__run_trash_process()
        
        if self.resource == Resources.async_operation:
            await self.__run_async_operation_process()
    
    async def __run_user_disk_process(self) -> None:
        user_disk = UserDisk(
            self.ya_disk_token,
        )
        operation: str = self.properties['user_disk_operations']
        
        process = UserDiskProcess(
            operation, 
            user_disk, 
            self.properties, 
            self.json)
        await process.execute()
    
    async def __run_files_and_folders_process(self) -> None:
        files_and_folders = FilesAndFolders(
            self.ya_disk_token,
        )
        operation: str = self.properties['files_and_folders_operations']
        
        process = FilesAndFoldersProcess(
            operation, 
            files_and_folders, 
            self.properties, 
            self.json)
        await process.execute()
        
    async def __run_public_files_and_folders_process(self) -> None:
        public_files_and_folders = PublicFilesAndFolders(
            self.ya_disk_token,
        )
        operation: str = self.properties['public_files_and_folders_operations']
        process = PublicFilesAndFoldersProcess(
            operation, 
            public_files_and_folders, 
            self.properties, 
            self.json)
        await process.execute()
    
    async def __run_trash_process(self) -> None:
        trash = Trash(
            self.ya_disk_token,
        )
        operation: str = self.properties['trash_operations']
        
        process = TrashProcess(
            operation, 
            trash, 
            self.properties, 
            self.json)
        await process.execute()
    
    async def __run_async_operation_process(self) -> None:
        async_operation = AsyncOperation(
            self.ya_disk_token,
        )
        operation: str = self.properties['async_operation_operations']
        
        process = AsyncOperationProcess(
            operation, 
            async_operation, 
            self.properties, 
            self.json)
        await process.execute()
