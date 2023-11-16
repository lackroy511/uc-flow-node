import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class CredentialType(flow.CredentialType):
    id: str = 'example_oauth2_api'
    is_public: bool = True
    displayName: str = 'example OAuth2 API'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    protocol: CredentialProtocol = CredentialProtocol.OAuth2
    properties: List[Property] = [
        Property(
            displayName='Client ID',
            name='client_id',
            type=Property.Type.STRING,
            required=True,
        ),
        Property(
            displayName='Client secret',
            name='client_secret',
            type=Property.Type.STRING,
            required=True,
        ),
        Property(
            displayName='Authorization Scope',
            name='scope',
            type=Property.Type.STRING,
            default='https://www.googleapis.com/auth/userinfo.profile',
        ),
    ]
    protected_properties: List[Property] = [
        Property(
            displayName='Authorization URL',
            name='authorization_endpoint',
            type=Property.Type.STRING,
            default=' '.join([
                'https://accounts.google.com/o/oauth2/v2/auth',
            ]),
            required=True,
        ),
        Property(
            displayName='Token URL',
            name='token_endpoint',
            type=Property.Type.STRING,
            default='https://oauth2.googleapis.com/' + 
                    'token?access_type=offline&prompt=consent',
            required=True,
        ),
        Property(
            displayName='Token URL',
            name='token_endpoint_auth_method',
            type=Property.Type.STRING,
            default='client_secret_post',
            required=True,
        ),
    ]


class NodeType(flow.NodeType):
    id: str = 'example'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'example'
    displayName: str = 'example'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'example'
    properties: List[Property] = [
        Property(
            displayName='URL to call',
            name='foo_field1',
            type=Property.Type.JSON,
            placeholder='Foo placeholder',
            description='Foo description',
            required=True,
            default='https://www.googleapis.com/oauth2/v1/userinfo',
        ),
        Property(
            displayName='URL params',
            name='foo_field2',
            type=Property.Type.JSON,
            placeholder='Foo2 placeholder',
            description='Foo2 description',
            default={'alt': 'json'},
        ),
    ]
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(name='test_ya', required=True),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType
        credential_types: Tuple[CredentialType] = (CredentialType(),)


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            data = await json.requester.request(
                Request(
                    url=json.node.data.properties['foo_field1'],
                    params=json.node.data.properties['foo_field2'],
                    auth=json.credential_id,
                ),
            )
            content = ujson.loads(data['content'])
            await json.save_result(content)
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
            
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
