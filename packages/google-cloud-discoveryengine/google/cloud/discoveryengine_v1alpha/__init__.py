# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.discoveryengine_v1alpha import gapic_version as package_version

__version__ = package_version.__version__


from .services.completion_service import (
    CompletionServiceAsyncClient,
    CompletionServiceClient,
)
from .services.conversational_search_service import (
    ConversationalSearchServiceAsyncClient,
    ConversationalSearchServiceClient,
)
from .services.data_store_service import (
    DataStoreServiceAsyncClient,
    DataStoreServiceClient,
)
from .services.document_service import DocumentServiceAsyncClient, DocumentServiceClient
from .services.engine_service import EngineServiceAsyncClient, EngineServiceClient
from .services.recommendation_service import (
    RecommendationServiceAsyncClient,
    RecommendationServiceClient,
)
from .services.schema_service import SchemaServiceAsyncClient, SchemaServiceClient
from .services.search_service import SearchServiceAsyncClient, SearchServiceClient
from .services.search_tuning_service import (
    SearchTuningServiceAsyncClient,
    SearchTuningServiceClient,
)
from .services.site_search_engine_service import (
    SiteSearchEngineServiceAsyncClient,
    SiteSearchEngineServiceClient,
)
from .services.user_event_service import (
    UserEventServiceAsyncClient,
    UserEventServiceClient,
)
from .types.common import (
    CustomAttribute,
    DoubleList,
    IndustryVertical,
    Interval,
    SearchAddOn,
    SearchTier,
    SolutionType,
    UserInfo,
)
from .types.completion_service import CompleteQueryRequest, CompleteQueryResponse
from .types.conversation import (
    Conversation,
    ConversationContext,
    ConversationMessage,
    Reply,
    TextInput,
)
from .types.conversational_search_service import (
    ConverseConversationRequest,
    ConverseConversationResponse,
    CreateConversationRequest,
    DeleteConversationRequest,
    GetConversationRequest,
    ListConversationsRequest,
    ListConversationsResponse,
    UpdateConversationRequest,
)
from .types.data_store import DataStore
from .types.data_store_service import (
    CreateDataStoreMetadata,
    CreateDataStoreRequest,
    DeleteDataStoreMetadata,
    DeleteDataStoreRequest,
    GetDataStoreRequest,
    ListDataStoresRequest,
    ListDataStoresResponse,
    UpdateDataStoreRequest,
)
from .types.document import Document
from .types.document_service import (
    CreateDocumentRequest,
    DeleteDocumentRequest,
    GetDocumentRequest,
    ListDocumentsRequest,
    ListDocumentsResponse,
    UpdateDocumentRequest,
)
from .types.engine import Engine
from .types.engine_service import (
    CreateEngineMetadata,
    CreateEngineRequest,
    DeleteEngineMetadata,
    DeleteEngineRequest,
    GetEngineRequest,
    ListEnginesRequest,
    ListEnginesResponse,
    PauseEngineRequest,
    ResumeEngineRequest,
    TuneEngineMetadata,
    TuneEngineRequest,
    TuneEngineResponse,
    UpdateEngineRequest,
)
from .types.import_config import (
    BigQuerySource,
    GcsSource,
    ImportDocumentsMetadata,
    ImportDocumentsRequest,
    ImportDocumentsResponse,
    ImportErrorConfig,
    ImportUserEventsMetadata,
    ImportUserEventsRequest,
    ImportUserEventsResponse,
)
from .types.purge_config import (
    PurgeDocumentsMetadata,
    PurgeDocumentsRequest,
    PurgeDocumentsResponse,
    PurgeUserEventsMetadata,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
)
from .types.recommendation_service import RecommendRequest, RecommendResponse
from .types.schema import FieldConfig, Schema
from .types.schema_service import (
    CreateSchemaMetadata,
    CreateSchemaRequest,
    DeleteSchemaMetadata,
    DeleteSchemaRequest,
    GetSchemaRequest,
    ListSchemasRequest,
    ListSchemasResponse,
    UpdateSchemaMetadata,
    UpdateSchemaRequest,
)
from .types.search_service import SearchRequest, SearchResponse
from .types.search_tuning_service import (
    TrainCustomModelMetadata,
    TrainCustomModelRequest,
    TrainCustomModelResponse,
)
from .types.site_search_engine import SiteSearchEngine, SiteVerificationInfo, TargetSite
from .types.site_search_engine_service import (
    BatchCreateTargetSiteMetadata,
    BatchCreateTargetSitesRequest,
    BatchCreateTargetSitesResponse,
    BatchVerifyTargetSitesMetadata,
    BatchVerifyTargetSitesRequest,
    BatchVerifyTargetSitesResponse,
    CreateTargetSiteMetadata,
    CreateTargetSiteRequest,
    DeleteTargetSiteMetadata,
    DeleteTargetSiteRequest,
    DisableAdvancedSiteSearchMetadata,
    DisableAdvancedSiteSearchRequest,
    DisableAdvancedSiteSearchResponse,
    EnableAdvancedSiteSearchMetadata,
    EnableAdvancedSiteSearchRequest,
    EnableAdvancedSiteSearchResponse,
    FetchDomainVerificationStatusRequest,
    FetchDomainVerificationStatusResponse,
    GetSiteSearchEngineRequest,
    GetTargetSiteRequest,
    ListTargetSitesRequest,
    ListTargetSitesResponse,
    RecrawlUrisMetadata,
    RecrawlUrisRequest,
    RecrawlUrisResponse,
    UpdateTargetSiteMetadata,
    UpdateTargetSiteRequest,
)
from .types.user_event import (
    CompletionInfo,
    DocumentInfo,
    MediaInfo,
    PageInfo,
    PanelInfo,
    SearchInfo,
    TransactionInfo,
    UserEvent,
)
from .types.user_event_service import CollectUserEventRequest, WriteUserEventRequest

__all__ = (
    "CompletionServiceAsyncClient",
    "ConversationalSearchServiceAsyncClient",
    "DataStoreServiceAsyncClient",
    "DocumentServiceAsyncClient",
    "EngineServiceAsyncClient",
    "RecommendationServiceAsyncClient",
    "SchemaServiceAsyncClient",
    "SearchServiceAsyncClient",
    "SearchTuningServiceAsyncClient",
    "SiteSearchEngineServiceAsyncClient",
    "UserEventServiceAsyncClient",
    "BatchCreateTargetSiteMetadata",
    "BatchCreateTargetSitesRequest",
    "BatchCreateTargetSitesResponse",
    "BatchVerifyTargetSitesMetadata",
    "BatchVerifyTargetSitesRequest",
    "BatchVerifyTargetSitesResponse",
    "BigQuerySource",
    "CollectUserEventRequest",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "CompletionInfo",
    "CompletionServiceClient",
    "Conversation",
    "ConversationContext",
    "ConversationMessage",
    "ConversationalSearchServiceClient",
    "ConverseConversationRequest",
    "ConverseConversationResponse",
    "CreateConversationRequest",
    "CreateDataStoreMetadata",
    "CreateDataStoreRequest",
    "CreateDocumentRequest",
    "CreateEngineMetadata",
    "CreateEngineRequest",
    "CreateSchemaMetadata",
    "CreateSchemaRequest",
    "CreateTargetSiteMetadata",
    "CreateTargetSiteRequest",
    "CustomAttribute",
    "DataStore",
    "DataStoreServiceClient",
    "DeleteConversationRequest",
    "DeleteDataStoreMetadata",
    "DeleteDataStoreRequest",
    "DeleteDocumentRequest",
    "DeleteEngineMetadata",
    "DeleteEngineRequest",
    "DeleteSchemaMetadata",
    "DeleteSchemaRequest",
    "DeleteTargetSiteMetadata",
    "DeleteTargetSiteRequest",
    "DisableAdvancedSiteSearchMetadata",
    "DisableAdvancedSiteSearchRequest",
    "DisableAdvancedSiteSearchResponse",
    "Document",
    "DocumentInfo",
    "DocumentServiceClient",
    "DoubleList",
    "EnableAdvancedSiteSearchMetadata",
    "EnableAdvancedSiteSearchRequest",
    "EnableAdvancedSiteSearchResponse",
    "Engine",
    "EngineServiceClient",
    "FetchDomainVerificationStatusRequest",
    "FetchDomainVerificationStatusResponse",
    "FieldConfig",
    "GcsSource",
    "GetConversationRequest",
    "GetDataStoreRequest",
    "GetDocumentRequest",
    "GetEngineRequest",
    "GetSchemaRequest",
    "GetSiteSearchEngineRequest",
    "GetTargetSiteRequest",
    "ImportDocumentsMetadata",
    "ImportDocumentsRequest",
    "ImportDocumentsResponse",
    "ImportErrorConfig",
    "ImportUserEventsMetadata",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "IndustryVertical",
    "Interval",
    "ListConversationsRequest",
    "ListConversationsResponse",
    "ListDataStoresRequest",
    "ListDataStoresResponse",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListEnginesRequest",
    "ListEnginesResponse",
    "ListSchemasRequest",
    "ListSchemasResponse",
    "ListTargetSitesRequest",
    "ListTargetSitesResponse",
    "MediaInfo",
    "PageInfo",
    "PanelInfo",
    "PauseEngineRequest",
    "PurgeDocumentsMetadata",
    "PurgeDocumentsRequest",
    "PurgeDocumentsResponse",
    "PurgeUserEventsMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "RecommendRequest",
    "RecommendResponse",
    "RecommendationServiceClient",
    "RecrawlUrisMetadata",
    "RecrawlUrisRequest",
    "RecrawlUrisResponse",
    "Reply",
    "ResumeEngineRequest",
    "Schema",
    "SchemaServiceClient",
    "SearchAddOn",
    "SearchInfo",
    "SearchRequest",
    "SearchResponse",
    "SearchServiceClient",
    "SearchTier",
    "SearchTuningServiceClient",
    "SiteSearchEngine",
    "SiteSearchEngineServiceClient",
    "SiteVerificationInfo",
    "SolutionType",
    "TargetSite",
    "TextInput",
    "TrainCustomModelMetadata",
    "TrainCustomModelRequest",
    "TrainCustomModelResponse",
    "TransactionInfo",
    "TuneEngineMetadata",
    "TuneEngineRequest",
    "TuneEngineResponse",
    "UpdateConversationRequest",
    "UpdateDataStoreRequest",
    "UpdateDocumentRequest",
    "UpdateEngineRequest",
    "UpdateSchemaMetadata",
    "UpdateSchemaRequest",
    "UpdateTargetSiteMetadata",
    "UpdateTargetSiteRequest",
    "UserEvent",
    "UserEventServiceClient",
    "UserInfo",
    "WriteUserEventRequest",
)
