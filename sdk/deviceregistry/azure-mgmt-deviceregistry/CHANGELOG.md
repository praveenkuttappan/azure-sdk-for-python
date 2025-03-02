# Release History

## 1.0.0 (2025-02-26)

### Features Added

  - Model `OperationStatusResult` added property `resource_id`

## 1.0.0b2 (2024-12-16)

### Features Added

  - Client `DeviceRegistryMgmtClient` added method `send_request`
  - Client `DeviceRegistryMgmtClient` added operation group `billing_containers`
  - Client `DeviceRegistryMgmtClient` added operation group `discovered_assets`
  - Client `DeviceRegistryMgmtClient` added operation group `discovered_asset_endpoint_profiles`
  - Client `DeviceRegistryMgmtClient` added operation group `schema_registries`
  - Client `DeviceRegistryMgmtClient` added operation group `schemas`
  - Client `DeviceRegistryMgmtClient` added operation group `schema_versions`
  - Model `AssetEndpointProfileProperties` added property `endpoint_profile_type`
  - Model `AssetEndpointProfileProperties` added property `authentication`
  - Model `AssetEndpointProfileProperties` added property `discovered_asset_endpoint_profile_ref`
  - Model `AssetEndpointProfileProperties` added property `status`
  - Model `AssetEndpointProfileUpdateProperties` added property `endpoint_profile_type`
  - Model `AssetEndpointProfileUpdateProperties` added property `authentication`
  - Model `AssetProperties` added property `asset_endpoint_profile_ref`
  - Model `AssetProperties` added property `discovered_asset_refs`
  - Model `AssetProperties` added property `default_datasets_configuration`
  - Model `AssetProperties` added property `default_topic`
  - Model `AssetProperties` added property `datasets`
  - Model `AssetStatus` added property `datasets`
  - Model `AssetStatus` added property `events`
  - Model `AssetUpdateProperties` added property `default_datasets_configuration`
  - Model `AssetUpdateProperties` added property `default_topic`
  - Model `AssetUpdateProperties` added property `datasets`
  - Model `Event` added property `topic`
  - Enum `ProvisioningState` added member `DELETING`
  - Added model `AssetEndpointProfileStatus`
  - Added model `AssetEndpointProfileStatusError`
  - Added model `AssetStatusDataset`
  - Added model `AssetStatusEvent`
  - Added model `Authentication`
  - Added enum `AuthenticationMethod`
  - Added model `BillingContainer`
  - Added model `BillingContainerProperties`
  - Added model `DataPointBase`
  - Added enum `DataPointObservabilityMode`
  - Added model `Dataset`
  - Added model `DiscoveredAsset`
  - Added model `DiscoveredAssetEndpointProfile`
  - Added model `DiscoveredAssetEndpointProfileProperties`
  - Added model `DiscoveredAssetEndpointProfileUpdate`
  - Added model `DiscoveredAssetEndpointProfileUpdateProperties`
  - Added model `DiscoveredAssetProperties`
  - Added model `DiscoveredAssetUpdate`
  - Added model `DiscoveredAssetUpdateProperties`
  - Added model `DiscoveredDataPoint`
  - Added model `DiscoveredDataset`
  - Added model `DiscoveredEvent`
  - Added model `EventBase`
  - Added enum `EventObservabilityMode`
  - Added enum `Format`
  - Added model `MessageSchemaReference`
  - Added model `ProxyResource`
  - Added model `Schema`
  - Added model `SchemaProperties`
  - Added model `SchemaRegistry`
  - Added model `SchemaRegistryProperties`
  - Added model `SchemaRegistryUpdate`
  - Added model `SchemaRegistryUpdateProperties`
  - Added enum `SchemaType`
  - Added model `SchemaVersion`
  - Added model `SchemaVersionProperties`
  - Added model `SystemAssignedServiceIdentity`
  - Added enum `SystemAssignedServiceIdentityType`
  - Added model `Topic`
  - Added enum `TopicRetainType`
  - Added operation group `BillingContainersOperations`
  - Added operation group `DiscoveredAssetEndpointProfilesOperations`
  - Added operation group `DiscoveredAssetsOperations`
  - Added operation group `SchemaRegistriesOperations`
  - Added operation group `SchemaVersionsOperations`
  - Added operation group `SchemasOperations`

### Breaking Changes

  - Model `Asset` deleted or renamed its instance variable `additional_properties`
  - Model `AssetEndpointProfile` deleted or renamed its instance variable `additional_properties`
  - Model `AssetEndpointProfileProperties` deleted or renamed its instance variable `user_authentication`
  - Model `AssetEndpointProfileProperties` deleted or renamed its instance variable `transport_authentication`
  - Model `AssetEndpointProfileProperties` deleted or renamed its instance variable `additional_properties`
  - Model `AssetEndpointProfileUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `AssetEndpointProfileUpdateProperties` deleted or renamed its instance variable `user_authentication`
  - Model `AssetEndpointProfileUpdateProperties` deleted or renamed its instance variable `transport_authentication`
  - Model `AssetEndpointProfileUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `AssetProperties` deleted or renamed its instance variable `asset_type`
  - Model `AssetProperties` deleted or renamed its instance variable `asset_endpoint_profile_uri`
  - Model `AssetProperties` deleted or renamed its instance variable `default_data_points_configuration`
  - Model `AssetProperties` deleted or renamed its instance variable `data_points`
  - Model `AssetProperties` deleted or renamed its instance variable `additional_properties`
  - Model `AssetStatus` deleted or renamed its instance variable `additional_properties`
  - Model `AssetStatusError` deleted or renamed its instance variable `additional_properties`
  - Model `AssetUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `AssetUpdateProperties` deleted or renamed its instance variable `asset_type`
  - Model `AssetUpdateProperties` deleted or renamed its instance variable `default_data_points_configuration`
  - Model `AssetUpdateProperties` deleted or renamed its instance variable `data_points`
  - Model `AssetUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `DataPoint` deleted or renamed its instance variable `capability_id`
  - Model `DataPoint` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Model `Event` deleted or renamed its instance variable `capability_id`
  - Model `Event` deleted or renamed its instance variable `additional_properties`
  - Model `ExtendedLocation` deleted or renamed its instance variable `additional_properties`
  - Model `Operation` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDisplay` deleted or renamed its instance variable `additional_properties`
  - Model `OperationStatusResult` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UsernamePasswordCredentials` deleted or renamed its instance variable `username_reference`
  - Model `UsernamePasswordCredentials` deleted or renamed its instance variable `password_reference`
  - Model `UsernamePasswordCredentials` deleted or renamed its instance variable `additional_properties`
  - Model `X509Credentials` deleted or renamed its instance variable `certificate_reference`
  - Model `X509Credentials` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `DataPointsObservabilityMode`
  - Deleted or renamed model `EventsObservabilityMode`
  - Deleted or renamed model `OwnCertificate`
  - Deleted or renamed model `TransportAuthentication`
  - Deleted or renamed model `TransportAuthenticationUpdate`
  - Deleted or renamed model `UserAuthentication`
  - Deleted or renamed model `UserAuthenticationMode`
  - Deleted or renamed model `UserAuthenticationUpdate`
  - Deleted or renamed model `UsernamePasswordCredentialsUpdate`
  - Deleted or renamed model `X509CredentialsUpdate`

## 1.0.0b1 (2024-04-22)

* Initial Release
