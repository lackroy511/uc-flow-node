from typing import List, Optional

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    CredentialProtocol,
)

from static.icon import ICON


class CredentialType(flow.CredentialType):
    id: str = 'yandex_api_oauth2'
    is_public: bool = True
    displayName: str = 'yandex_api_oauth2'
    icon = ICON
    protocol: CredentialProtocol = CredentialProtocol.OAuth2
    protected_properties: List[Property] = []
    properties: List[Property] = [
        Property(
            displayName='Client ID',
            name='client_id',
            type=Property.Type.HIDDEN,
            default='da854158137c496caafea4246173e3d4',
            required=True,
        ),
        Property(
            displayName='Client secret',
            name='client_secret',
            type=Property.Type.HIDDEN,
            default='fcbc962bd13f47f8bf49799efc708de6',
            required=True,
        ),
        Property(
            displayName='Token URL',
            name='token_endpoint',
            type=Property.Type.HIDDEN,
            default='https://oauth.yandex.ru/token',
            required=True,
        ),
        Property(
            displayName='Auth URL',
            name='authorization_endpoint',
            type=Property.Type.HIDDEN,
            default='https://oauth.yandex.ru/authorize',
            required=True,
        ),
        Property(
            default='OAuth',
            displayName='Token prefix',
            name='token_prefix',
            type=Property.Type.HIDDEN,
        ),
    ]
    extends: Optional[List[str]] = []
