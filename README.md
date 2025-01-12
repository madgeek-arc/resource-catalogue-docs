<div align="center">
  <img src='https://eosc.eu/wp-content/uploads/2024/02/EOSC-Beyond-logo.png'></img>
</div>

# Resource Catalogue Documentation [v5.0.0]
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

---

**Work in Progress:** This section is a work in progress and is subject to modification.

## Description
**Resource Catalogue Documentation** provides a comprehensive guide to the API endpoints, models, and core components 
of the **[Resource Catalogue](https://github.com/madgeek-arc/resource-catalogue)** project, offering detailed 
descriptions of each controller, along with their associated functionalities and endpoints. It includes an overview of 
its data models and a detailed list of vocabularies used within the platform. Additionally, the documentation provides 
schemas for validating data of the various classes, ensuring consistency and reliability across the system.

---

## Table of Contents
1. [API](#api)
2. [Swagger UI](#swagger-ui)
3. [Controllers](#controllers)
    1. [Catalogue Controller](#catalogue-controller)
    2. [Configuration Template Instance Controller](#configuration-template-instance-controller)
    3. [Datasource Controller](#datasource-controller)
    4. [Interoperability Record Controller](#interoperability-record-controller)
    5. [Provider Controller](#provider-controller)
    6. [Public Controller](#public-controller)
    7. [Resource Interoperability Record Controller](#resource-interoperability-record-controller)
    8. [Service Controller](#service-controller)
    9. [Service Extensions Controller](#service-extensions-controller)
    10. [Training Resource Controller](#training-resource-controller)
    11. [Vocabulary Controller](#vocabulary-controller)
4. [Model](#model)
    1. [Catalogue](#catalogue)
    2. [Configuration Template Instance](#configuration-template-instance)
    3. [Datasource](#datasource)
    4. [Helpdesk](#helpdesk)
    5. [Interoperability Record](#interoperability-record)
    6. [Monitoring](#monitoring)
    7. [Provider](#provider)
    8. [Resource Interoperability Record](#resource-interoperability-record)
    9. [Service](#service)
    10. [Training Resource](#training-resource)
    11. [Vocabulary](#vocabulary)
5. [List of Vocabularies](#list-of-vocabularies)
6. [Data Validation](#data-validation)

---

## API
- https://providers.sandbox.eosc-beyond.eu/api
- https://integration.providers.sandbox.eosc-beyond.eu/api
- https://dev.providers.sandbox.eosc-beyond.eu/api

---

## Swagger UI
- [Production](https://providers.sandbox.eosc-beyond.eu/api/swagger-ui/index.html)
- [Integration](https://integration.providers.sandbox.eosc-beyond.eu/api/swagger-ui/index.html)
- [Dev](https://dev.providers.sandbox.eosc-beyond.eu/api/swagger-ui/index.html)

---

## Controllers

- ### Catalogue Controller
  
  #### Operations for Catalogues + external resources

  - DELETE
    - Deletes the Training Resource of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/trainingResource/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix: String [required]
      ```
    - Deletes the Service of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/service/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Deletes the Provider of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/provider/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Deletes the Interoperability Record of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/interoperabilityRecord/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Deletes the Datasource of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/datasource/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
      
  - GET
    - Returns the Catalogue with the given id.
      ```diff
      /catalogue/{id}
      Params:
        id: String [required]
      ```
    - Get all the Training Resources of a specific Provider of a specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/{prefix}/{suffix}/trainingResource/all
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Get all the Services of a specific Provider of a specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/{prefix}/{suffix}/service/all
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Get all the Interoperability Records of a specific Provider of a specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/{prefix}/{suffix}/interoperabilityRecord/all
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Returns the Training Resource of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/trainingResource/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Returns the Service of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/service/{prefix}/{suffix}
      Params:
        catalogueId: String (required)
        prefix : String (required)
        suffix : String (required)
      ```
    - Returns the Provider of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/provider/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Filter a list of Providers based on a set of filters or get a list of all Providers in the Catalogue.
      ```diff
      /catalogue/{catalogueId}/provider/all
      Params:
        catalogueId: String [required]
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
      ```
    - Returns the Interoperability Record of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/interoperabilityRecord/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Returns the Datasource of the specific Service of the specific Catalogue with the given id.
      ```diff
      /catalogue/{catalogueId}/datasource/{prefix}/{suffix}
      Params:
        catalogueId: String [required]
        prefix : String [required]
        suffix : String [required]
      ```
    - Returns a list of Catalogues where user is admin.
      ```diff
      /catalogue/getMyCatalogues
      ```
    - Get a list of all Catalogues in the Portal.
      ```diff
      /catalogue/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
      ```
      
  - POST
    - Creates a new Catalogue.
      ```diff
      /catalogue
      Body:
        Catalogue JSON [required]
      ```
    - Creates a new Training Resource for the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/trainingResource
      Params:
        catalogueId: String [required]
      Body:
        Training Resource JSON [required]
      ```
    - Creates a new Service for the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/service
      Params:
        catalogueId: String [required]
      Body:
        Service JSON [required]
      ```
    - Creates a new Provider for the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/provider
      Params:
        catalogueId: String [required]
      Body:
        Provider JSON [required]
      ```
    - Creates a new Interoperability Record for the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/interoperabilityRecord
      Params:
        catalogueId: String [required]
      Body:
        Interoperability Record JSON [required]
      ```
    - Creates a new Datasource for the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/datasource
      Params:
        catalogueId: String [required]
      Body:
        Datasource JSON [required]
      ```
   
  - PUT
    - Updates a specific Catalogue.
      ```diff
      /catalogue
      Params:
        comment: String
      Body:
        Catalogue JSON [required]
      ```
    - Updates the Training Resource of the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/trainingResource
      Params:
        catalogueId: String [required]
        comment: String [optional]
      Body:
        Training Resource JSON [required]
      ```
    - Updates the Service of the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/service
      Params:
        catalogueId: String [required]
        comment: String [optional]
      Body:
        Service JSON [required]
      ```
    - Updates the Provider of the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/provider
      Params:
        catalogueId: String [required]
        comment: String [optional]
      Body:
        Provider JSON [required]
      ```
    - Updates the Interoperability Record of the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/interoperabilityRecord
      Params:
        catalogueId: String [required]
        comment: String [optional]
      Body:
        Interoperability Record JSON [required]
      ```
    - Updates the Datasource of the specific Catalogue.
      ```diff
      /catalogue/{catalogueId}/datasource
      Params:
        catalogueId: String [required]
        comment: String [optional]
      Body:
        Datasource JSON [required]
      ```
      
- ### Configuration Template Instance Controller
  
  #### Operations for Configuration Template Instances
  
  - GET
    - Returns the ConfigurationTemplateInstance with the given id.
      ```diff
      /configurationTemplateInstance/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns a List of Configuration Template Instances associated with the given 'resourceId'.
      ```diff
      /configurationTemplateInstance/getAllByResourceId/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns a List of Configuration Template Instances associated with the given 'configurationTemplateId'.
      ```diff
      /configurationTemplateInstance/getAllByConfigurationTemplateId/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Filter a list of Configuration Template Instances based on a set of filters or get a list of all Configuration Template Instances in the Catalogue.
      ```diff
      /configurationTemplateInstance/all
      Params:
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
      ```
      
  - POST
    - Creates a new Configuration Template Instance.
      ```diff
      /configurationTemplateInstance
      Body:
        Configuration Template Instance JSON [required]
      ```
      
  - PUT
    - Updates a specific Configuration Template Instance.
      ```diff
      /configurationTemplateInstance
      Body:
        Configuration Template Instance JSON [required]
      ```
     
- ### Datasource Controller
  
  #### Operations for Datasources
  
  - DELETE
    - Deletes the Datasource with the given id.
      ```diff
      /datasource/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
      
  - GET
    - Returns the Datasource with the given id.
      ```diff
      /datasource/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns the Datasource of the given Service of the given Catalogue.
      ```diff
      /datasource/byService/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Filter a list of Datasources based on a set of filters or get a list of all Datasources in the Catalogue.
      ```diff
      /datasource/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (Catalogue ID) [optional]
      ```
      
  - POST
    - Creates a new Datasource.
      ```diff
      /datasource
      Body:
        Datasource JSON [required]
      ```
        
  - PUT
    - Updates a specific Datasource.
      ```diff
      /datasource
      Params:
        comment: String [optional]
      Body:
        Datasource JSON [required]
      ```
        
- ### Interoperability Record Controller
  
  #### Operations for Interoperability Records
  
  - DELETE
    - Deletes the Interoperability Record with the given id.
      ```diff
      /interoperabilityRecord/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Deletes the Draft Interoperability Record with the given id.
      ```diff
      /interoperabilityRecord/draft/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
      
  - GET
    - Returns the Interoperability Record with the given id.
      ```diff
      /interoperabilityRecord/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Returns the Related Resources of a specific Interoperability Record given its id.
      ```diff
      /interoperabilityRecord/relatedResources/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns the Draft Interoperability Record with the given id.
      ```diff
      /interoperabilityRecord/draft/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns a list of Draft Interoperability Records where user is admin.
      ```diff
      /interoperabilityRecord/draft/getMyDraftInteroperabilityRecords
      ```
    - Filter a list of Interoperability Records based on a set of filters or get a list of all Interoperability Records of a specific Provider in the Catalogue.
      ```diff
      /interoperabilityRecord/byProvider/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
      ```
    - Get all Interoperability Records.
      ```diff
      /interoperabilityRecord/all
      Params:
        suspended: String (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (Catalogue ID) [optional]
      ```
      
  - POST
    - Creates a new Interoperability Record.
      ```diff
      /interoperabilityRecord
      Body:
        Interoperability Record JSON [required]
      ```
    - Creates a new Draft Interoperability Record.
      ```diff
      /interoperabilityRecord/draft
      Body:
        Interoperability Record JSON [required]
      ```
    - Validates the Interoperability Record without actually changing the repository.
      ```diff
      /interoperabilityRecord/validate
      Body:
        Interoperability Record JSON [required]
      ```
      
  - PUT
    - Updates the Interoperability Record with the given id.
      ```diff
      /interoperabilityRecord
      Body:
        Interoperability Record JSON [required]
      ```
    - Updates the Draft Interoperability Record with the given id.
      ```diff
      /interoperabilityRecord/draft
      Body:
        Interoperability Record JSON [required]
      ```
        
- ### Provider Controller
  
  #### Operations for Providers
  
  - DELETE
    - Deletes the Provider of the specific Catalogue given its id.
      ```diff
      /provider/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Deletes the Draft Provider of the specific Catalogue given its id.
      ```diff
      /provider/draft/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```      
      
  - GET
    - Returns the Provider of the specific Catalogue given its id.
      ```diff
      /provider/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Validates a url.
      ```diff
      /provider/validateUrl
      Params:
        urlForValidation: URL [required]
      ```             
    - Get a list of all inactive Services of a specific Provider.
      ```diff
      /provider/services/inactive/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Get a list of all rejected resources (Services or Training Resources) of a specific Provider.
      ```diff
      /provider/services/inactive/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        resourceType: String [required]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
    - Get all inactive Providers of the Catalogue.
      ```diff
      /provider/inactive/all
      ```
    - Returns a list of Providers where user is admin.
      ```diff
      /provider/getMyServiceProviders
      ```
    - Returns the Draft Provider given its id.
      ```diff
      /provider/draft/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns a list of Draft Providers where user is admin.
      ```diff
      /provider/draft/getMyDraftProviders
      ```
    - Get a list of all Providers under a specific Catalogue.
      ```diff
      /provider/byCatalogue/{id}
      Params:
        id: String [required]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
    - Filter a list of Providers based on a set of filters or get a list of all Providers in the Catalogue.
      ```diff
      /provider/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]

  - POST
    - Create a new Provider.
      ```diff
      /provider
      Body:
        Provider JSON [required]
      ```
    - Create a new Draft Provider.
      ```diff
      /provider/draft
      Body:
        Provider JSON [required]
      ```
    - Validates the Provider without actually changing the repository.
      ```diff
      /provider/validate
      Body:
        Provider JSON [required]
      ```
      
  - PUT
    - Updates the Provider of the specific Catalogue give its id.
      ```diff
      /provider
      Params:
        catalogue_id: String (default 'eosc') [optional]
        comment: String [optional]
      Body:
        Provider JSON [required]
      ```
    - Updates the Draft Provider of the specific Catalogue give its id.
      ```diff
      /provider/draft
      Body:
        Provider JSON [required]
      ```
      
- ### Public Controller
  
  #### Get information about Public resources
  
  - GET
    - Returns the Public Configuration Template Instance with the given id.
      ```diff
      /public/configurationTemplateInstance/{id}
      Params:
        id: String [required]
      ```
    - Get a list of all Public Configuration Template Instances in the Portal.
      ```diff
      /public/configurationTemplateInstance/all
      Params:
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
      ```
    - Returns the Public Datasource with the given id.
      ```diff
      /public/datasource/{id}
      Params:
        id: String [required]
      ```
    - Get a list of all Public Datasources of the specific Catalogue in the Portal.
      ```diff
      /public/datasource/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Interoperability Record of the specific Catalogue with the given id.
      ```diff
      /public/interoperabilityRecord/{id}
      Params:
        id: String [required]
        catalogue_id: String (default 'eosc) [optional]
      ```
    - Returns the Public Related Resources of a specific Interoperability Record given its id.
      ```diff
      /public/interoperabilityRecord/relatedResources/{id}
      Params:
        id: String [required]
      ```
    - Returns a list of Public Interoperability Records where user is admin.
      ```diff
      /public/interoperabilityRecord/my
      ```
    - Get a list of all Public Interoperability Records of the specific Catalogue in the Portal.
      ```diff
      /public/interoperabilityRecord/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Provider with the given id.
      ```diff
      /public/provider/{id}
      Params:
        id: String [required]
      ```
    - Returns a list of Public Providers where user is admin.
      ```diff
      /public/provider/my
      ```
    - Get a list of all Public Providers of the specific Catalogue in the Portal.
      ```diff
      /public/provider/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Resource Interoperability Record with the given id.
      ```diff
      /public/resourceInteroperabilityRecord/{id}
      Params:
        id: String [required]
      ```
    - Returns a list of Public Resource Interoperability Records where user is admin.
      ```diff
      /public/resourceInteroperabilityRecord/my
      ```
    - Get a list of all Public Resource Interoperability Records of the specific Catalogue in the Portal.
      ```diff
      /public/resourceInteroperabilityRecord/all
      Params:
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Service of the specific Catalogue with the given id.
      ```diff
      /public/service/{id}
      Params:
        id: String [required]
        catalogue_id (default 'eosc') [optional]
      ```
    - Returns a list of Public Services where user is admin.
      ```diff
      /public/services/my
      ```
    - Get a list of all Public Services of the specific Catalogue in the Portal.
      ```diff
      /public/services/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Monitoring with the given id.
      ```diff
      /public/monitoring/{id}
      Params:
        id: String [required]
      ```
    - Returns a list of Public Monitorings where user is admin.
      ```diff
      /public/monitoring/my
      ```
    - Get a list of all Public Monitorings of the specific Catalogue in the Portal.
      ```diff
      /public/monitoring/all
      Params:
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Helpdesk with the given id.
      ```diff
      /public/helpdesk/{id}
      Params:
        id: String [required]
      ```
    - Returns a list of Public Helpdesks where user is admin.
      ```diff
      /public/helpdesk/my
      ```
    - Get a list of all Public Helpdesks of the specific Catalogue in the Portal.
      ```diff
      /public/helpdesk/all
      Params:
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Public Training Resource of the specific Catalogue with the given id.
      ```diff
      /public/trainingResource/{id}
      Params:
        id: String [required]
        catalogue_id (default 'eosc') [optional]
      ```
    - Returns a list of Public Training Resources where user is admin.
      ```diff
      /public/trainingResource/my
      ```
    - Get a list of all Public Training Resources of the specific Catalogue in the Portal.
      ```diff
      /public/trainingResource/all
      Params:
        suspended: boolean (default false) [optional]
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (default 'eosc') [optional]
      ```

- ### Resource Interoperability Record Controller
  
  #### Operations for Resource Interoperability Records
  
  - DELETE
    - Deletes the Resource Interoperability Record of a specific resource with the given id.
      ```diff
      /resourceInteroperabilityRecord/{resourceIdPrefix}/{resourceIdSuffix}/{resourceInteroperabilityRecordIdPrefix}/{resourceInteroperabilityRecordIdSuffix}
      Params:
        resourceIdPrefix: String [required]
        resourceIdSuffix: String [required]
        resourceInteroperabilityRecordIdPrefix: String [required]
        resourceInteroperabilityRecordIdSuffix: String [required]
      ```
      
  - GET
    - Returns the Resource Interoperability Record with the given id.
      ```diff
      /resourceInteroperabilityRecord/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns the Resource Interoperability Record of the given Service of the given Catalogue.
      ```diff
      /resourceInteroperabilityRecord/byResource/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Filter a list of Resource Interoperability Records based on a set of filters or get a list of all Resource Interoperability Records in the Catalogue.
      ```diff
      /datasource/all
      Params:
        query : String (Keyword to refine the search) [optional]
        from : String (Starting index in the result set, default 0) [optional]
        quantity: String (Quantity to be fetched, default 10) [optional]
        order: String (Order of results - asc/desc, default asc) [optional]
        orderField: String (Field to use for ordering) [optional]
        catalogue: String (Catalogue ID) [optional]
      ```
      
  - POST
    - Creates a new Resource Interoperability Record.
      ```diff
      /resourceInteroperabilityRecord
      Params:
        resourceType : String [required]
      Body:
        Resource Interoperability Record JSON [required]
      ```
        
  - PUT
    - Updates a specific Resource Interoperability Record.
      ```diff
      /resourceInteroperabilityRecord
      Body:
        Resource Interoperability Record JSON [required]
      ```
  
- ### Service Controller
  
  #### Operations for Services
  
  - DELETE
    - Deletes the Service of the specific Catalogue given its id.
      ```diff
      /service/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Deletes the Draft Service given its id.
      ```diff
      /service/draft/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
      
  - GET
    - Returns the Service of the specific Catalogue given its id.
      ```diff
        /service/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
          catalogue_id: String (default 'eosc') [optional]
      ```
    - Returns a list of all inactive Services.
      ```diff
        /service/inactive/all
        Params:
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
          catalogue: String (default 'eosc') [optional]
      ```
    - Returns the Draft Service of the specific Catalogue given its id.
      ```diff
        /service/draft/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
      ```
    - Returns a list of Draft Services where user is admin.
      ```diff
      /service/draft/my
      ```
    - Returns a list of Draft Services under a specific Provider.
      ```diff
        /service/draft/byProvider/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Returns a list of Services under a specific Provider.
      ```diff
        /service/byProvider/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Returns a list of Services of a specific Catalogue.
      ```diff
        /service/byCatalogue/{id}
        Params:
          id: String [required]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Get all Services in the Catalogue organized by an attribute (eg. name)
      ```diff
        /service/by/{field}
        Params:
          field: Service field (required)
      ```
    - Returns a list of all Services of the specific Catalogue in the Portal.
      ```diff
        /service/all
        Params:
          suspended: boolean (default false) [optional]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
          catalogue: String (default 'eosc') [optional]
      ```
      
  - POST
    - Creates a new Service.
      ```diff
        /service
        Body:
          Service JSON [required]
    - Creates a new Draft Service.
      ```diff
        /service/draft
        Body:
          Service JSON [required]
    - Validates a Service without actually changing the repository.
      ```diff
      /service/validate
      Body:
        Service JSON [required]
  - PUT
    - Updates a specific Service.
      ```diff
      /service
      Params:
        comment: String
      Body:
        Service JSON [required]
      ```
    - Updates a specific Draft Service.
      ```diff
      /service/draft
      Body:
        Service JSON [required]
      ```
  
- ### Service Extensions Controller
  
  #### Operations for Service Extensions (Helpdesks && Monitorings)
  
  - DELETE
    - Deletes the specific Monitoring.
      ```diff
      /service-extensions/monitoring/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Deletes the specific Helpdesk.
      ```diff
      /service-extensions/helpdesk/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
      
  - GET
    - Returns the Monitoring with the given id.
      ```diff
      /service-extensions/monitoring/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns a list of available Monitoring service types.
      ```diff
      /service-extensions/monitoring/serviceTypes
      ```
    - Returns the Monitoring of the given Service of the given Catalogue.
      ```diff
      /service-extensions/monitoring/byService/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Filter a list of Monitorings based on a set of filters or get a list of all Monitorings in the Catalogue.
      ```diff
        /service-extensions/monitoring/all
        Params:
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Returns the Helpdesk with the given id.
      ```diff
      /service-extensions/helpdesk/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
    - Returns the Helpdesk of the given Service of the given Catalogue.
      ```diff
      /service-extensions/helpdesk/byService/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Filter a list of Helpdesks based on a set of filters or get a list of all Helpdesks in the Catalogue.
      ```diff
        /service-extensions/helpdesk/all
        Params:
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
        
  - POST
    - Creates a new Monitoring.
      ```diff
        /service-extensions/monitoring
        Params:
          catalogue_id: String [required]
          resourceType: String [required]
        Body:
          Monitoring JSON [required]
      ```
    - Creates a new Helpdesk.
      ```diff
        /service-extensions/helpdesk
        Params:
          catalogue_id: String [required]
          resourceType: String [required]
        Body:
          Helpdesk JSON [required]
      ```

  - PUT
    - Updates the Monitoring with the given id.
      ```diff
      /service-extensions/monitoring
      Params:
        catalogue_id: String (default 'eosc') [optional]
      Body:
        Monitoring JSON [required]
      ```
    - Updates the Helpdesk with the given id.
      ```diff
      /service-extensions/helpdesk
      Params:
        catalogue_id: String (default 'eosc') [optional]
      Body:
        Helpdesk JSON [required]
      ```

- ### Training Resource Controller
  
  #### Operations for Training Resources
  
  - DELETE
    - Deletes the Training Resource of the specific Catalogue given its id.
      ```diff
      /trainingResource/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
        catalogue_id: String (default 'eosc') [optional]
      ```
    - Deletes the Draft Training Resource given its id.
      ```diff
      /trainingResource/draft/{prefix}/{suffix}
      Params:
        prefix: String [required]
        suffix: String [required]
      ```
      
  - GET
    - Returns the Training Resource of the specific Catalogue given its id.
      ```diff
        /trainingResource/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
          catalogue_id: String (default 'eosc') [optional]
      ```
    - Returns a list of all inactive Training Resources.
      ```diff
        /trainingResource/inactive/all
        Params:
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Returns the Draft Training Resource of the specific Catalogue given its id.
      ```diff
        /trainingResource/draft/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
      ```
    - Returns a list of Draft Training Resources where user is admin.
      ```diff
      /trainingResource/draft/getMyDraftTrainingResources
      ```
    - Returns a list of Training Resources under a specific Provider.
      ```diff
        /trainingResource/byProvider/{prefix}/{suffix}
        Params:
          prefix: String [required]
          suffix: String [required]
          catalogue_id: String (default 'eosc') [optional]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Returns a list of Training Resources of a specific Catalogue.
      ```diff
        /trainingResource/byCatalogue/{id}
        Params:
          id: String [required]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
      ```
    - Get all Training Resources in the Catalogue organized by an attribute (eg. name)
      ```diff
        /trainingResource/by/{field}
        Params:
          field: Service field (required)
      ```
    - Returns a list of all Training Resources of the specific Catalogue in the Portal.
      ```diff
        /trainingResource/all
        Params:
          suspended: boolean (default false) [optional]
          query : String (Keyword to refine the search) [optional]
          from : String (Starting index in the result set, default 0) [optional]
          quantity: String (Quantity to be fetched, default 10) [optional]
          order: String (Order of results - asc/desc, default asc) [optional]
          orderField: String (Field to use for ordering) [optional]
          catalogue: String (default 'eosc') [optional]
      ```
      
  - POST
    - Creates a new Training Resource.
      ```diff
        /trainingResource
        Body:
          Training Resource JSON [required]
    - Creates a new Draft Training Resource.
      ```diff
        /trainingResource/draft
        Body:
          Training Resource JSON [required]
    - Validates a Training Resource without actually changing the repository.
      ```diff
      /trainingResource/validate
      Body:
        Training Resource JSON [required]
  - PUT
    - Updates a specific Training Resource.
      ```diff
      /trainingResource
      Params:
        comment: String
      Body:
        Training Resource JSON [required]
      ```
    - Updates a specific Draft Training Resource.
      ```diff
      /trainingResource/draft
      Body:
        Training Resource JSON [required]
      ```

- ### Vocabulary Controller
  
  #### Get information about Vocabularies
  
  - GET
    - Get all Vocabularies grouped by Type:
      ```diff
      /vocabulary/byType
      ```
    - Get all Vocabularies of a specific Type:
      ```diff
      /vocabulary/byType/{type}
      Params:
        type: Vocabulary Type [required]
      ```
    - Get a list of EU Countries:
      ```diff
      /vocabulary/countries/EU
      ```
    - Get a list of WW Countries:
      ```diff
      /vocabulary/countries/WW
      ```
    - Get a specific Vocabulary given its ID:
      ```diff
      /vocabulary/{id}
      Params:[required](required)
      ```

---

## Model

### Catalogue

| Field                    | Type                          | Required | Description                                                      |
|--------------------------|-------------------------------|----------|------------------------------------------------------------------|
| `id`                     | `String`                      | auto-gen | Unique identifier for the catalogue.                             |
| `abbreviation`           | `String`                      | Yes      | Abbreviation of the catalogue's name.                            |
| `name`                   | `String`                      | Yes      | Full name of the catalogue.                                      |
| `website`                | `URL`                         | Yes      | URL of the catalogue's website.                                  |
| `legalEntity`            | `boolean`                     | Yes      | Indicates if the catalogue is a legal entity.                    |
| `legalStatus`            | `String`                      | No       | Legal status of the catalogue.                                   |
| `hostingLegalEntity`     | `String`                      | No       | Hosting legal entity responsible for the catalogue.              |
| `inclusionCriteria`      | `URL`                         | Yes      | URL with criteria for inclusion in the catalogue.                |
| `validationProcess`      | `URL`                         | Yes      | URL describing the validation process.                           |
| `endOfLife`              | `String`                      | No       | Information on the end-of-life policies for the catalogue.       |
| `description`            | `String`                      | Yes      | Description of the catalogue.                                    |
| `scope`                  | `String`                      | Yes      | Scope of the catalogue.                                          |
| `logo`                   | `URL`                         | Yes      | URL of the catalogue's logo.                                     |
| `multimedia`             | `List<MultimediaPair>`        | No       | List of multimedia items associated with the catalogue.          |
| `scientificDomains`      | `List<ServiceProviderDomain>` | No       | Scientific domains related to the catalogue's service providers. |
| `tags`                   | `List<String>`                | No       | Tags associated with the catalogue.                              |
| `location`               | `ProviderLocation`            | Yes      | Physical location details of the catalogue provider.             |
| `mainContact`            | `ProviderMainContact`         | Yes      | Main contact information for the catalogue.                      |
| `publicContacts`         | `List<ProviderPublicContact`  | Yes      | List of public contacts for the catalogue.                       |
| `participatingCountries` | `List<String>`                | No       | List of countries participating in the catalogue.                |
| `affiliations`           | `List<String>`                | No       | List of affiliations related to the catalogue.                   |
| `networks`               | `List<String>`                | No       | Networks associated with the catalogue.                          |
| `users`                  | `List<User>`                  | Yes      | List of users associated with the catalogue.                     |

#### Nested Objects

##### MultimediaPair

| Field            | Type     | Required | Description                      |
|------------------|----------|----------|----------------------------------|
| `multimediaURL`  | `URL`    | Yes      | URL to the multimedia resource.  |
| `multimediaName` | `String` | No       | Name of the multimedia resource. |

##### ServiceProviderDomain

| Field                 | Type     | Required | Description                                    |
|-----------------------|----------|----------|------------------------------------------------|
| `scientificDomain`    | `String` | Yes      | Scientific domain related to the catalogue.    |
| `scientificSubdomain` | `String` | No       | Scientific subdomain related to the catalogue. |

##### ProviderLocation

| Field                 | Type      | Required | Description                                     |
|-----------------------|-----------|----------|-------------------------------------------------|
| `streetNameAndNumber` | `String`  | Yes      | Street address of the catalogue's location.     |
| `postalCode`          | `String`  | Yes      | Postal code of the catalogue's location.        |
| `city`                | `String`  | Yes      | City where the catalogue is located.            |
| `region`              | `String`  | No       | Region or state where the catalogue is located. |
| `country`             | `String`  | Yes      | Country where the catalogue is located.         |

##### ProviderMainContact

| Field          | Type     | Required | Description                               |
|----------------|----------|----------|-------------------------------------------|
| `firstName`    | `String` | Yes      | First name of the main contact person.    |
| `lastName`     | `String` | No       | Last name of the main contact person.     |
| `email`        | `String` | Yes      | Email address of the main contact person. |
| `phone`        | `String` | No       | Phone number of the main contact person.  |
| `position`     | `String` | No       | Position of the main contact person.      |
| `organisation` | `String` | No       | Organisation of the main contact person.  |

##### ProviderPublicContact

| Field          | Type     | Required | Description                                 |
|----------------|----------|----------|---------------------------------------------|
| `firstName`    | `String` | No       | First name of the public contact person.    |
| `lastName`     | `String` | No       | Last name of the public contact person.     |
| `email`        | `String` | Yes      | Email address of the public contact person. |
| `phone`        | `String` | No       | Phone number of the public contact person.  |
| `position`     | `String` | No       | Position of the public contact person.      |
| `organisation` | `String` | No       | Organisation of the public contact person.  |

##### User

| Field     | Type     | Required | Description                     |
|-----------|----------|----------|---------------------------------|
| `id`      | `String` | No       | Unique identifier for the user. |
| `email`   | `String` | Yes      | Email address of the user.      |
| `name`    | `String` | Yes      | First name of the user.         |
| `surname` | `String` | Yes      | Last name of the user.          |


#### Example

```json
{
  "id": "catalogue_001",
  "abbreviation": "CAT",
  "name": "Sample Catalogue",
  "website": "https://example.com",
  "legalEntity": true,
  "legalStatus": "Non-profit",
  "hostingLegalEntity": "Hosting Entity",
  "inclusionCriteria": "https://example.com/inclusion",
  "validationProcess": "https://example.com/validation",
  "endOfLife": "No specific policy",
  "description": "This is a sample catalogue description.",
  "scope": "International",
  "logo": "https://example.com/logo.png",
  "multimedia": [
    {
      "multimediaURL": "https://example.com/media",
      "multimediaName": "Sample Multimedia"
    }
  ],
  "scientificDomains": [
    {
      "scientificDomain": "Science",
      "scientificSubdomain": "Physics"
    }
  ],
  "tags": ["science", "research"],
  "location": {
    "streetNameAndNumber": "123 Main St",
    "postalCode": "12345",
    "city": "Sample City",
    "region": "Sample Region",
    "country": "Sample Country"
  },
  "mainContact": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "+123456789",
    "position": "Manager"
  },
  "publicContacts": [
    {
      "firstName": "Jane",
      "lastName": "Smith",
      "email": "jane.smith@example.com",
      "phone": "+987654321",
      "position": "Support"
    }
  ],
  "participatingCountries": ["Country1", "Country2"],
  "affiliations": ["Affiliation1", "Affiliation2"],
  "networks": ["Network1", "Network2"],
  "users": [
    {
      "id": "user_001",
      "email": "user@example.com",
      "name": "User Name",
      "surname": "Surname"
    }
  ]
}
```

### Configuration Template Instance

| Field                     | Type       | Required | Description                                                |
|---------------------------|------------|----------|------------------------------------------------------------|
| `id`                      | `String`   | auto-gen | Unique identifier for the configuration template instance. |
| `resourceId`              | `String`   | Yes      | Identifier of the resource associated with the instance.   |
| `configurationTemplateId` | `String`   | Yes      | Identifier of the configuration template used.             |
| `payload`                 | `String`   | Yes      | The configuration data or settings in JSON format.         |

### Example

```json
{
  "id": "resource_interop_001",
  "resourceId": "resource_001",
  "catalogueId": "catalogue_001",
  "interoperabilityRecordIds": [
    "interop_001",
    "interop_002"
  ]
}
```

### Datasource

| Field                                   | Type                               | Required | Description                                                         |
|-----------------------------------------|------------------------------------|----------|---------------------------------------------------------------------|
| `id`                                    | `String`                           | auto-gen | Unique identifier for the datasource.                               |
| `serviceId`                             | `String`                           | Yes      | Identifier of the associated service.                               |
| `catalogueId`                           | `String`                           | Yes      | Identifier of the associated catalogue.                             |
| `submissionPolicyURL`                   | `URL`                              | No       | URL of the submission policy.                                       |
| `preservationPolicyURL`                 | `URL`                              | No       | URL of the preservation policy.                                     |
| `versionControl`                        | `Boolean`                          | No       | Indicates if version control is used.                               |
| `persistentIdentitySystems`             | `List<PersistentIdentitySystem>`   | No       | List of persistent identity systems associated with the datasource. |
| `jurisdiction`                          | `String`                           | Yes      | Jurisdiction where the datasource operates.                         |
| `datasourceClassification`              | `String`                           | Yes      | Classification of the datasource.                                   |
| `researchEntityTypes`                   | `List<String>`                     | No       | List of research entity types related to the datasource.            |
| `thematic`                              | `Boolean`                          | Yes      | Indicates if the datasource is thematic.                            |
| `researchProductLicensings`             | `List<ResearchProductLicensing>`   | No       | List of research product licensing details.                         |
| `researchProductAccessPolicies`         | `List<String>`                     | No       | List of research product access policies.                           |
| `researchProductMetadataLicensing`      | `ResearchProductMetadataLicensing` | No       | Metadata licensing details for research products.                   |
| `researchProductMetadataAccessPolicies` | `List<String>`                     | No       | List of research product metadata access policies.                  |
| `harvestable`                           | `Boolean`                          | No       | Indicates if the datasource is harvestable.                         |

#### Nested Objects

##### PersistentIdentitySystem

| Field                                 | Type                           | Required | Description                                       |
|---------------------------------------|--------------------------------|----------|---------------------------------------------------|
| `persistentIdentityEntityType`        | `String`                       | Yes      | Type of the persistent identity entity.           |
| `persistentIdentityEntityTypeSchemes` | `List<String>`                 | No       | Schemes for the persistent identity entity types. |

##### ResearchProductLicensing

| Field                        | Type     | Required | Description                           |
|------------------------------|----------|----------|---------------------------------------|
| `researchProductLicenseName` | `String` | Yes      | Name of the research product license. |
| `researchProductLicenseURL`  | `URL`    | Yes      | URL of the research product license.  |

##### ResearchProductMetadataLicensing

| Field                                | Type     | Required | Description                                    |
|--------------------------------------|----------|----------|------------------------------------------------|
| `researchProductMetadataLicenseName` | `String` | Yes      | Name of the research product metadata license. |
| `researchProductMetadataLicenseURL`  | `URL`    | Yes      | URL of the research product metadata license.  |

### Example

```json
{
  "id": "datasource_001",
  "serviceId": "service_001",
  "catalogueId": "catalogue_001",
  "submissionPolicyURL": "https://example.com/submission-policy",
  "preservationPolicyURL": "https://example.com/preservation-policy",
  "versionControl": true,
  "persistentIdentitySystems": [
    {
      "persistentIdentityEntityType": "Type1",
      "persistentIdentityEntityTypeSchemes": ["Scheme1", "Scheme2"]
    }
  ],
  "jurisdiction": "Country X",
  "datasourceClassification": "Public",
  "researchEntityTypes": ["Type1", "Type2"],
  "thematic": true,
  "researchProductLicensings": [
    {
      "researchProductLicenseName": "License1",
      "researchProductLicenseURL": "https://example.com/license1"
    }
  ],
  "researchProductAccessPolicies": ["Policy1", "Policy2"],
  "researchProductMetadataLicensing": {
    "researchProductMetadataLicenseName": "Metadata License1",
    "researchProductMetadataLicenseURL": "https://example.com/metadata-license1"
  },
  "researchProductMetadataAccessPolicies": ["MetadataPolicy1", "MetadataPolicy2"],
  "harvestable": true
}
```

### Helpdesk

| Field                | Type           | Required | Description                                                                     |
|----------------------|----------------|----------|---------------------------------------------------------------------------------|
| `id`                 | `String`       | auto-gen | Unique identifier for the helpdesk.                                             |
| `serviceId`          | `String`       | Yes      | Identifier of the associated service.                                           |
| `services`           | `List<String>` | No       | List of services associated with the helpdesk.                                  |
| `helpdeskType`       | `String`       | No       | Type of the helpdesk (e.g., technical support, customer support).               |
| `supportGroups`      | `List<String>` | No       | List of support groups related to the helpdesk.                                 |
| `organisation`       | `String`       | No       | Organisation managing the helpdesk.                                             |
| `emails`             | `List<String>` | No       | List of email addresses for direct assignment of tickets, bypassing L1 support. |
| `agents`             | `List<String>` | No       | List of agents working in the helpdesk.                                         |
| `signatures`         | `List<String>` | No       | List of signatures used by the helpdesk.                                        |
| `ticketPreservation` | `Boolean`      | No       | Indicates if ticket preservation is enabled.                                    |
| `webform`            | `Boolean`      | No       | Indicates if a webform is used for ticket submission.                           |

#### Example

```json
{
  "id": "helpdesk_001",
  "serviceId": "service_001",
  "services": ["serviceA", "serviceB"],
  "helpdeskType": "Technical Support",
  "supportGroups": ["group1", "group2"],
  "organisation": "SupportOrg",
  "emails": ["support@example.com", "escalation@example.com"],
  "agents": ["agent1", "agent2"],
  "signatures": ["Best regards, Support Team", "Thank you for contacting support"],
  "ticketPreservation": true,
  "webform": false
}
```

### Interoperability Record

| Field                    | Type                          | Required | Description                                                                      |
|--------------------------|-------------------------------|----------|----------------------------------------------------------------------------------|
| `id`                     | `String`                      | auto-gen | Unique identifier for the interoperability record.                               |
| `catalogueId`            | `String`                      | Yes      | Identifier of the catalogue containing this record.                              |
| `providerId`             | `String`                      | Yes      | Identifier of the provider associated with the record.                           |
| `identifierInfo`         | `IdentifierInfo`              | Yes      | Information about the primary identifier of the record.                          |
| `creators`               | `List<Creator>`               | Yes      | List of creators involved in the creation of the resource.                       |
| `title`                  | `String`                      | Yes      | Title of the interoperability record.                                            |
| `publicationYear`        | `Integer`                     | Yes      | Year of publication for the record.                                              |
| `resourceTypesInfo`      | `List<ResourceTypeInfo>`      | Yes      | List of resource types associated with the record.                               |
| `created`                | `String`                      | No       | Timestamp indicating when the record was created.                                |
| `updated`                | `String`                      | No       | Timestamp indicating the last update to the record.                              |
| `relatedStandards`       | `List<RelatedStandard>`       | No       | List of related standards connected to the interoperability record.              |
| `rights`                 | `List<Right>`                 | Yes      | List of rights associated with the record.                                       |
| `description`            | `String`                      | Yes      | Description of the interoperability record.                                      |
| `status`                 | `String`                      | Yes      | Current status of the interoperability record.                                   |
| `domain`                 | `String`                      | No       | Domain to which the record pertains.                                             |
| `eoscGuidelineType`      | `String`                      | Yes      | Type of EOSC (European Open Science Cloud) guideline associated with the record. |
| `eoscIntegrationOptions` | `List<String>`                | No       | Options for integrating the record into EOSC.                                    |
| `alternativeIdentifiers` | `List<AlternativeIdentifier>` | No       | Alternative identifiers for the record.                                          |

#### Nested Objects

##### IdentifierInfo

| Field            | Type     | Required | Description                                      |
|------------------|----------|----------|--------------------------------------------------|
| `identifier`     | `String` | Yes      | Main identifier for the interoperability record. |
| `identifierType` | `String` | Yes      | Type of the identifier, e.g., DOI, Handle.       |

##### Creator

| Field                    | Type                     | Required | Description                                     |
|--------------------------|--------------------------|----------|-------------------------------------------------|
| `creatorNameTypeInfo`    | `CreatorNameTypeInfo`    | Yes      | Information about the creator's name and type.  |
| `givenName`              | `String`                 | No       | Given name of the creator.                      |
| `familyName`             | `String`                 | No       | Family name of the creator.                     |
| `nameIdentifier`         | `String`                 | No       | Unique identifier for the creator, e.g., ORCID. |
| `creatorAffiliationInfo` | `CreatorAffiliationInfo` | No       | Affiliation details of the creator.             |

##### CreatorNameTypeInfo

| Field         | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| `creatorName` | `String` | Yes      | Full name of the creator.                     |
| `nameType`    | `String` | Yes      | Type of name, e.g., personal, organizational. |

##### CreatorAffiliationInfo

| Field                   | Type     | Description                             |
|-------------------------|----------|-----------------------------------------|
| `affiliation`           | `String` | Name of the affiliation of the creator. |
| `affiliationIdentifier` | `String` | Identifier for the affiliation, if any. |

##### ResourceTypeInfo

| Field                 | Type     | Required | Description                                         |
|-----------------------|----------|----------|-----------------------------------------------------|
| `resourceType`        | `String` | Yes      | Specific type of the resource, e.g., dataset, tool. |
| `resourceTypeGeneral` | `String` | Yes      | General category of the resource type.              |

##### RelatedStandard

| Field                       | Type     | Description                          |
|-----------------------------|----------|--------------------------------------|
| `relatedStandardIdentifier` | `String` | Identifier for the related standard. |
| `relatedStandardURI`        | `URL`    | URI linking to the related standard. |

##### Right

| Field             | Type     | Required | Description                                    |
|-------------------|----------|----------|------------------------------------------------|
| `rightTitle`      | `String` | Yes      | Title of the right associated with the record. |
| `rightURI`        | `URL`    | Yes      | URI linking to the right.                      |
| `rightIdentifier` | `String` | Yes      | Identifier for the right.                      |

##### AlternativeIdentifier

| Field   | Type     | Description                                      |
|---------|----------|--------------------------------------------------|
| `type`  | `String` | Type of alternative identifier, e.g., DOI, ISBN. |
| `value` | `String` | Value of the alternative identifier.             |

### Example

```json
{
  "id": "interop_001",
  "catalogueId": "catalogue_001",
  "providerId": "provider_001",
  "identifierInfo": {
    "identifier": "10.1234/interop",
    "identifierType": "DOI"
  },
  "creators": [
    {
      "creatorNameTypeInfo": {
        "creatorName": "John Smith",
        "nameType": "Personal"
      },
      "givenName": "John",
      "familyName": "Smith",
      "nameIdentifier": "0000-0002-1825-0097",
      "creatorAffiliationInfo": {
        "affiliation": "University of Example",
        "affiliationIdentifier": "org_001"
      }
    }
  ],
  "title": "Interoperability Record Example",
  "publicationYear": 2024,
  "resourceTypesInfo": [
    {
      "resourceType": "Dataset",
      "resourceTypeGeneral": "Data"
    }
  ],
  "created": "2024-01-01T12:00:00Z",
  "updated": "2024-09-01T12:00:00Z",
  "relatedStandards": [
    {
      "relatedStandardIdentifier": "standard_001",
      "relatedStandardURI": "https://example.com/standard"
    }
  ],
  "rights": [
    {
      "rightTitle": "Open Access",
      "rightURI": "https://example.com/right",
      "rightIdentifier": "right_001"
    }
  ],
  "description": "This is a sample interoperability record description.",
  "status": "Active",
  "domain": "Data Science",
  "eoscGuidelineType": "EOSC Interoperability",
  "eoscIntegrationOptions": ["Integration A", "Integration B"],
  "alternativeIdentifiers": [
    {
      "type": "Handle",
      "value": "hdl:20.500.12345"
    }
  ]
}
```

### Monitoring

| Field              | Type                    | Required | Description                                          |
|--------------------|-------------------------|----------|------------------------------------------------------|
| `id`               | `String`                | auto-gen | Unique identifier for the monitoring record.         |
| `serviceId`        | `String`                | Yes      | Identifier of the associated service.                |
| `monitoredBy`      | `String`                | No       | Entity or system that is performing the monitoring.  |
| `monitoringGroups` | `List<MonitoringGroup>` | Yes      | List of monitoring groups related to the monitoring. |

#### Nested Objects

##### MonitoringGroup

| Field         | Type           | Required | Description                      |
|---------------|----------------|----------|----------------------------------|
| `serviceType` | `String`       | Yes      | Type of service being monitored. |
| `endpoint`    | `String`       | Yes      | Endpoint URL for monitoring.     |
| `metrics`     | `List<Metric>` | Yes      | List of metrics being monitored. |

##### Metric

| Field    | Type  | Required | Description                           |
|----------|-------|----------|---------------------------------------|
| `probe`  | `URL` | Yes      | URL for the probe used in monitoring. |
| `metric` | `URL` | Yes      | URL for the metric being measured.    |

### Example

```json
{
  "id": "monitoring123",
  "serviceId": "service456",
  "monitoredBy": "MonitoringServiceX",
  "monitoringGroups": [
    {
      "serviceType": "API",
      "endpoint": "https://api.example.com/status",
      "metrics": [
        {
          "probe": "https://metrics.example.com/probe1",
          "metric": "https://metrics.example.com/metric1"
        },
        {
          "probe": "https://metrics.example.com/probe2",
          "metric": "https://metrics.example.com/metric2"
        }
      ]
    },
    {
      "serviceType": "Database",
      "endpoint": "https://db.example.com/status",
      "metrics": [
        {
          "probe": "https://metrics.example.com/dbProbe1",
          "metric": "https://metrics.example.com/dbMetric1"
        }
      ]
    }
  ]
}
```

### Provider

| Field                     | Type                          | Required | Description                                                                                       |
|---------------------------|-------------------------------|----------|---------------------------------------------------------------------------------------------------|
| `id`                      | `String`                      | auto-gen | Unique identifier for the provider.                                                               |
| `abbreviation`            | `String`                      | Yes      | Abbreviation of the provider's name.                                                              |
| `name`                    | `String`                      | Yes      | Full name of the provider.                                                                        |
| `website`                 | `URL`                         | Yes      | URL of the provider's website.                                                                    |
| `legalEntity`             | `boolean`                     | Yes      | Indicates if the provider is a legal entity.                                                      |
| `legalStatus`             | `String`                      | No       | Legal status of the provider.                                                                     |
| `hostingLegalEntity`      | `String`                      | No       | Hosting legal entity responsible for the provider.                                                |
| `alternativeIdentifiers`  | `List<AlternativeIdentifier>` | No       | List of alternative identifiers for the provider.                                                 |
| `description`             | `String`                      | Yes      | Description of the provider.                                                                      |
| `logo`                    | `URL`                         | Yes      | URL of the provider's logo.                                                                       |
| `multimedia`              | `List<MultimediaPair>`        | No       | List of multimedia items associated with the provider.                                            |
| `scientificDomains`       | `List<ServiceProviderDomain>` | No       | Scientific domains related to the provider's services.                                            |
| `tags`                    | `List<String>`                | No       | Tags associated with the provider.                                                                |
| `structureTypes`          | `List<String>`                | No       | Types of structures associated with the provider.                                                 |
| `location`                | `ProviderLocation`            | Yes      | Physical location details of the provider.                                                        |
| `mainContact`             | `ProviderMainContact`         | Yes      | Main contact information for the provider.                                                        |
| `publicContacts`          | `List<ProviderPublicContact>` | Yes      | List of public contacts for the provider.                                                         |
| `lifeCycleStatus`         | `String`                      | No       | Current lifecycle status of the provider.                                                         |
| `certifications`          | `List<String>`                | No       | List of certifications held by the provider.                                                      |
| `participatingCountries`  | `List<String>`                | No       | List of countries participating in the provider's services.                                       |
| `affiliations`            | `List<String>`                | No       | List of affiliations related to the provider.                                                     |
| `networks`                | `List<String>`                | No       | Networks associated with the provider.                                                            |
| `catalogueId`             | `String`                      | No       | Identifier of the catalogue the provider belongs to.                                              |
| `esfriDomains`            | `List<String>`                | No       | ESFRI (European Strategy Forum on Research Infrastructures) domains associated with the provider. |
| `esfriType`               | `String`                      | No       | ESFRI type classification of the provider.                                                        |
| `merilScientificDomains`  | `List<ProviderMerilDomain>`   | No       | MERIL scientific domains associated with the provider.                                            |
| `areasOfActivity`         | `List<String>`                | No       | Areas of activity related to the provider's services.                                             |
| `societalGrandChallenges` | `List<String>`                | No       | Societal grand challenges addressed by the provider.                                              |
| `nationalRoadmaps`        | `List<String>`                | No       | National roadmaps associated with the provider.                                                   |
| `users`                   | `List<User>`                  | Yes      | List of users associated with the provider.                                                       |

#### Nested Objects

##### AlternativeIdentifier

| Field   | Type     | Required | Description                          |
|---------|----------|----------|--------------------------------------|
| `type`  | `String` | No       | Type of the alternative identifier.  |
| `value` | `String` | No       | Value of the alternative identifier. |

##### MultimediaPair

| Field            | Type     | Required | Description                      |
|------------------|----------|----------|----------------------------------|
| `multimediaURL`  | `URL`    | Yes      | URL to the multimedia resource.  |
| `multimediaName` | `String` | No       | Name of the multimedia resource. |

##### ServiceProviderDomain

| Field                 | Type     | Required | Description                                    |
|-----------------------|----------|----------|------------------------------------------------|
| `scientificDomain`    | `String` | Yes      | Scientific domain related to the catalogue.    |
| `scientificSubdomain` | `String` | No       | Scientific subdomain related to the catalogue. |

##### ProviderLocation

| Field                 | Type      | Required | Description                                     |
|-----------------------|-----------|----------|-------------------------------------------------|
| `streetNameAndNumber` | `String`  | Yes      | Street address of the catalogue's location.     |
| `postalCode`          | `String`  | Yes      | Postal code of the catalogue's location.        |
| `city`                | `String`  | Yes      | City where the catalogue is located.            |
| `region`              | `String`  | No       | Region or state where the catalogue is located. |
| `country`             | `String`  | Yes      | Country where the catalogue is located.         |

##### ProviderMainContact

| Field          | Type     | Required | Description                               |
|----------------|----------|----------|-------------------------------------------|
| `firstName`    | `String` | Yes      | First name of the main contact person.    |
| `lastName`     | `String` | No       | Last name of the main contact person.     |
| `email`        | `String` | Yes      | Email address of the main contact person. |
| `phone`        | `String` | No       | Phone number of the main contact person.  |
| `position`     | `String` | No       | Position of the main contact person.      |
| `organisation` | `String` | No       | Organisation of the main contact person.  |

##### ProviderPublicContact

| Field          | Type     | Required | Description                                 |
|----------------|----------|----------|---------------------------------------------|
| `firstName`    | `String` | No       | First name of the public contact person.    |
| `lastName`     | `String` | No       | Last name of the public contact person.     |
| `email`        | `String` | Yes      | Email address of the public contact person. |
| `phone`        | `String` | No       | Phone number of the public contact person.  |
| `position`     | `String` | No       | Position of the public contact person.      |
| `organisation` | `String` | No       | Organisation of the public contact person.  |

##### ProviderMerilDomain

| Field                      | Type     | Required | Description                                         |
|----------------------------|----------|----------|-----------------------------------------------------|
| `merilScientificDomain`    | `String` | Yes      | MERIL scientific domain related to the provider.    |
| `merilScientificSubdomain` | `String` | No       | MERIL scientific subdomain related to the provider. |

#### Example

```json
{
  "id": "provider_001",
  "abbreviation": "PROV",
  "name": "Sample Provider",
  "website": "https://example.com",
  "legalEntity": true,
  "legalStatus": "Non-profit",
  "hostingLegalEntity": "Hosting Entity",
  "alternativeIdentifiers": [
    {
      "type": "Other ID Type",
      "value": "123-abc"
    }
  ],
  "description": "This is a sample provider description.",
  "logo": "https://example.com/logo.png",
  "multimedia": [
    {
      "multimediaURL": "https://example.com/media",
      "multimediaName": "Sample Multimedia"
    }
  ],
  "scientificDomains": [
    {
      "scientificDomain": "Science",
      "scientificSubdomain": "Physics"
    }
  ],
  "tags": ["science", "research"],
  "structureTypes": ["type1", "type2"],
  "location": {
    "streetNameAndNumber": "123 Main St",
    "postalCode": "12345",
    "city": "Sample City",
    "region": "Sample Region",
    "country": "Sample Country"
  },
  "mainContact": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "+123456789",
    "position": "Manager"
  },
  "publicContacts": [
    {
      "firstName": "Jane",
      "lastName": "Smith",
      "email": "jane.smith@example.com",
      "phone": "+987654321",
      "position": "Support"
    }
  ],
  "lifeCycleStatus": "Active",
  "certifications": ["ISO9001", "ISO27001"],
  "participatingCountries": ["Country1", "Country2"],
  "affiliations": ["Affiliation1", "Affiliation2"],
  "networks": ["Network1", "Network2"],
  "catalogueId": "catalogue_001",
  "esfriDomains": ["Domain1", "Domain2"],
  "esfriType": "Type1",
  "merilScientificDomains": [
    {
      "merilScientificDomain": "MERIL Domain",
      "merilScientificSubdomain": "Subdomain"
    }
  ],
  "areasOfActivity": ["Activity1", "Activity2"],
  "societalGrandChallenges": ["Challenge1", "Challenge2"],
  "nationalRoadmaps": ["Roadmap1", "Roadmap2"],
  "users": [
    {
      "id": "user_001",
      "email": "user@example.com",
      "name": "User Name",
      "surname": "Surname"
    }
  ]
}
```

### Resource Interoperability Record

| Field                       | Type           | Required | Description                                                  |
|-----------------------------|----------------|----------|--------------------------------------------------------------|
| `id`                        | `String`       | auto-gen | Unique identifier for the resource interoperability record.  |
| `resourceId`                | `String`       | Yes      | Identifier of the resource associated with the record.       |
| `catalogueId`               | `String`       | Yes      | Identifier of the catalogue where the record is stored.      |
| `interoperabilityRecordIds` | `List<String>` | Yes      | List of interoperability record IDs related to the resource. |

### Example

```json
{
  "id": "resource_interop_001",
  "resourceId": "resource_001",
  "catalogueId": "catalogue_001",
  "interoperabilityRecordIds": [
    "interop_001",
    "interop_002"
  ]
}
```

### Service

| Field                         | Type                          | Required | Description                                                               |
|-------------------------------|-------------------------------|----------|---------------------------------------------------------------------------|
| `id`                          | `String`                      | auto-gen | Unique identifier for the service.                                        |
| `abbreviation`                | `String`                      | Yes      | Abbreviation of the service's name.                                       |
| `name`                        | `String`                      | Yes      | Full name of the service.                                                 |
| `resourceOrganisation`        | `String`                      | Yes      | Name of the resource organization providing the service.                  |
| `resourceProviders`           | `List<String>`                | No       | List of resource providers associated with the service.                   |
| `webpage`                     | `URL`                         | Yes      | URL of the service's webpage.                                             |
| `alternativeIdentifiers`      | `List<AlternativeIdentifier>` | No       | List of alternative identifiers for the service.                          |
| `description`                 | `String`                      | Yes      | Detailed description of the service.                                      |
| `tagline`                     | `String`                      | Yes      | Short tagline summarizing the service.                                    |
| `logo`                        | `URL`                         | Yes      | URL of the service's logo.                                                |
| `multimedia`                  | `List<MultimediaPair>`        | No       | List of multimedia items related to the service.                          |
| `useCases`                    | `List<UseCasesPair>`          | No       | List of use cases demonstrating the service in action.                    |
| `scientificDomains`           | `List<ServiceProviderDomain>` | Yes      | List of scientific domains related to the service.                        |
| `categories`                  | `List<ServiceCategory>`       | Yes      | Categories and subcategories of the service.                              |
| `targetUsers`                 | `List<String>`                | Yes      | List of target users for the service.                                     |
| `accessTypes`                 | `List<String>`                | No       | Types of access provided by the service (e.g., open, restricted).         |
| `accessModes`                 | `List<String>`                | No       | Modes of access available for the service (e.g., online, in-person).      |
| `tags`                        | `List<String>`                | No       | Tags associated with the service.                                         |
| `horizontalService`           | `Boolean`                     | No       | Indicates if the service is a horizontal service.                         |
| `serviceCategories`           | `List<String>`                | No       | List of service categories associated with the service.                   |
| `marketplaceLocations`        | `List<String>`                | No       | List of marketplace locations where the service is available.             |
| `geographicalAvailabilities`  | `List<String>`                | Yes      | List of geographical availabilities of the service.                       |
| `languageAvailabilities`      | `List<String>`                | Yes      | List of language availabilities of the service.                           |
| `resourceGeographicLocations` | `List<String>`                | No       | List of locations where the service resources are geographically located. |
| `mainContact`                 | `ServiceMainContact`          | Yes      | Main contact information for the service.                                 |
| `publicContacts`              | `List<ServicePublicContact>`  | Yes      | List of public contacts for the service.                                  |
| `helpdeskEmail`               | `String`                      | Yes      | Email address for the service's helpdesk.                                 |
| `securityContactEmail`        | `String`                      | Yes      | Email address for security contact.                                       |
| `trl`                         | `String`                      | Yes      | Technology Readiness Level of the service.                                |
| `lifeCycleStatus`             | `String`                      | No       | Life cycle status of the service.                                         |
| `certifications`              | `List<String>`                | No       | List of certifications related to the service.                            |
| `standards`                   | `List<String>`                | No       | Standards that the service complies with.                                 |
| `openSourceTechnologies`      | `List<String>`                | No       | List of open-source technologies used in the service.                     |
| `version`                     | `String`                      | No       | Current version of the service.                                           |
| `lastUpdate`                  | `Date`                        | No       | Date and time of the last update.                                         |
| `changeLog`                   | `List<String>`                | No       | List of changes made to the service.                                      |
| `requiredResources`           | `List<String>`                | No       | List of required resources for the service.                               |
| `relatedResources`            | `List<String>`                | No       | List of related resources linked to the service.                          |
| `relatedPlatforms`            | `List<String>`                | No       | List of related platforms connected to the service.                       |
| `catalogueId`                 | `String`                      | No       | Identifier of the associated catalogue.                                   |
| `fundingBody`                 | `List<String>`                | No       | List of funding bodies supporting the service.                            |
| `fundingPrograms`             | `List<String>`                | No       | List of funding programs related to the service.                          |
| `grantProjectNames`           | `List<String>`                | No       | List of grant project names associated with the service.                  |
| `helpdeskPage`                | `URL`                         | No       | URL of the helpdesk page.                                                 |
| `userManual`                  | `URL`                         | No       | URL of the user manual.                                                   |
| `termsOfUse`                  | `URL`                         | Yes      | URL of the terms of use.                                                  |
| `privacyPolicy`               | `URL`                         | Yes      | URL of the privacy policy.                                                |
| `accessPolicy`                | `URL`                         | No       | URL of the access policy.                                                 |
| `resourceLevel`               | `URL`                         | No       | URL of the resource level details.                                        |
| `trainingInformation`         | `URL`                         | No       | URL of the training information.                                          |
| `statusMonitoring`            | `URL`                         | No       | URL for status monitoring information.                                    |
| `maintenance`                 | `URL`                         | No       | URL of the maintenance details.                                           |
| `orderType`                   | `String`                      | Yes      | Type of order required for the service.                                   |
| `order`                       | `URL`                         | No       | URL for ordering the service.                                             |
| `paymentModel`                | `URL`                         | No       | URL of the payment model information.                                     |
| `pricing`                     | `URL`                         | No       | URL of the pricing details.                                               |

#### Nested Objects

##### AlternativeIdentifier

| Field   | Type     | Required | Description                          |
|---------|----------|----------|--------------------------------------|
| `type`  | `String` | No       | Type of the alternative identifier.  |
| `value` | `String` | No       | Value of the alternative identifier. |

##### MultimediaPair

| Field            | Type     | Required | Description                      |
|------------------|----------|----------|----------------------------------|
| `multimediaURL`  | `URL`    | Yes      | URL to the multimedia resource.  |
| `multimediaName` | `String` | No       | Name of the multimedia resource. |

##### UseCasesPair

| Field         | Type     | Required | Description                    |
|---------------|----------|----------|--------------------------------|
| `useCaseURL`  | `URL`    | Yes      | URL to the use case resource.  |
| `useCaseName` | `String` | No       | Name of the use case resource. |

##### ServiceProviderDomain

| Field                 | Type     | Required | Description                    |
|-----------------------|----------|----------|--------------------------------|
| `scientificDomain`    | `String` | Yes      | Main scientific domain.        |
| `scientificSubdomain` | `String` | Yes      | Specific scientific subdomain. |

##### ServiceCategory

| Field         | Type     | Required | Description                 |
|---------------|----------|----------|-----------------------------|
| `category`    | `String` | Yes      | Category of the service.    |
| `subcategory` | `String` | No       | Subcategory of the service. |

##### ServiceMainContact

| Field          | Type     | Required | Description                        |
|----------------|----------|----------|------------------------------------|
| `firstName`    | `String` | Yes      | First name of the main contact.    |
| `lastName`     | `String` | Yes      | Last name of the main contact.     |
| `email`        | `String` | Yes      | Email address of the main contact. |
| `phone`        | `String` | No       | Phone number of the main contact.  |
| `position`     | `String` | No       | Position of the main contact.      |
| `organisation` | `String` | No       | Organization of the main contact.  |

##### ServicePublicContact

| Field          | Type     | Required | Description                          |
|----------------|----------|----------|--------------------------------------|
| `firstName`    | `String` | No       | First name of the public contact.    |
| `lastName`     | `String` | No       | Last name of the public contact.     |
| `email`        | `String` | Yes      | Email address of the public contact. |
| `phone`        | `String` | No       | Phone number of the public contact.  |
| `position`     | `String` | No       | Position of the public contact.      |
| `organisation` | `String` | No       | Organization of the public contact.  |

### Example

```json
{
  "id": "service_001",
  "abbreviation": "SERV",
  "name": "Sample Service",
  "resourceOrganisation": "Sample Organisation",
  "resourceProviders": ["Provider1", "Provider2"],
  "webpage": "https://example.com",
  "alternativeIdentifiers": [
    {
      "type": "Other ID Type",
      "value": "abc-123"
    }
  ],
  "description": "This is a sample service description.",
  "tagline": "Providing high-quality services.",
  "logo": "https://example.com/logo.png",
  "multimedia": [
    {
      "multimediaURL": "https://example.com/media",
      "multimediaName": "Sample Multimedia"
    }
  ],
  "useCases": [
    {
      "useCaseURL": "https://example.com/use-case",
      "useCaseName": "Sample Use Case"
    }
  ],
  "scientificDomains": [
    {
      "scientificDomain": "Biology",
      "scientificSubdomain": "Molecular Biology"
    }
  ],
  "categories": [
    {
      "category": "Category1",
      "subcategory": "Subcategory1"
    }
  ],
  "targetUsers": ["Researchers", "Students"],
  "accessTypes": ["Open", "Restricted"],
  "accessModes": ["Online", "In-person"],
  "tags": ["innovation", "technology"],
  "horizontalService": true,
  "serviceCategories": ["CategoryA", "CategoryB"],
  "marketplaceLocations": ["Location1", "Location2"],
  "geographicalAvailabilities": ["Global"],
  "languageAvailabilities": ["English", "French"],
  "resourceGeographicLocations": ["Location A", "Location B"],
  "mainContact": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "contact@example.com",
    "phone": "123-456-7890",
    "position": "Manager",
    "organisation": "Sample Org"
  },
  "publicContacts": [
    {
      "firstName": "Jane",
      "lastName": "Smith",
      "email": "jane.smith@example.com",
      "phone": "098-765-4321",
      "position": "Support",
      "organisation": "Sample Org"
    }
  ],
  "helpdeskEmail": "helpdesk@example.com",
  "securityContactEmail": "security@example.com",
  "trl": "TRL 7",
  "lifeCycleStatus": "Active",
  "certifications": ["Certification1", "Certification2"],
  "standards": ["Standard1", "Standard2"],
  "openSourceTechnologies": ["Technology1", "Technology2"],
  "version": "1.0.0",
  "lastUpdate": "2024-09-09T12:00:00Z",
  "changeLog": ["Initial release.", "Minor updates."],
  "requiredResources": ["Resource1", "Resource2"],
  "relatedResources": ["RelatedResource1", "RelatedResource2"],
  "relatedPlatforms": ["Platform1", "Platform2"],
  "catalogueId": "catalogue_001",
  "fundingBody": ["Funding Body1", "Funding Body2"],
  "fundingPrograms": ["Program1", "Program2"],
  "grantProjectNames": ["Project1", "Project2"],
  "helpdeskPage": "https://example.com/helpdesk",
  "userManual": "https://example.com/user-manual",
  "termsOfUse": "https://example.com/terms",
  "privacyPolicy": "https://example.com/privacy",
  "accessPolicy": "https://example.com/access-policy",
  "resourceLevel": "https://example.com/resource-level",
  "trainingInformation": "https://example.com/training",
  "statusMonitoring": "https://example.com/status-monitoring",
  "maintenance": "https://example.com/maintenance",
  "orderType": "Online",
  "order": "https://example.com/order",
  "paymentModel": "https://example.com/payment-model",
  "pricing": "https://example.com/pricing"
}
```

### Training Resource

| Field                        | Type                          | Required | Description                                                                       |
|------------------------------|-------------------------------|----------|-----------------------------------------------------------------------------------|
| `id`                         | `String`                      | auto-gen | Unique identifier for the training resource.                                      |
| `title`                      | `String`                      | Yes      | Title of the training resource.                                                   |
| `resourceOrganisation`       | `String`                      | Yes      | Organisation providing the resource.                                              |
| `resourceProviders`          | `List<String>`                | No       | List of resource providers associated with the training resource.                 |
| `authors`                    | `List<String>`                | Yes      | List of authors who contributed to the training resource.                         |
| `url`                        | `URL`                         | Yes      | URL linking to the training resource.                                             |
| `urlType`                    | `String`                      | No       | Type of URL, e.g., landing page, direct link, etc.                                |
| `eoscRelatedServices`        | `List<String>`                | No       | List of related services in the European Open Science Cloud (EOSC).               |
| `alternativeIdentifiers`     | `List<AlternativeIdentifier>` | No       | List of alternative identifiers for the training resource.                        |
| `description`                | `String`                      | No       | Description of the training resource.                                             |
| `keywords`                   | `List<String>`                | No       | Keywords associated with the training resource.                                   |
| `license`                    | `String`                      | Yes      | License under which the training resource is distributed.                         |
| `accessRights`               | `String`                      | Yes      | Access rights for the training resource, e.g., open, restricted, etc.             |
| `versionDate`                | `Date`                        | Yes      | Date and time when the version was published.                                     |
| `targetGroups`               | `List<String>`                | Yes      | List of target groups intended for the training resource.                         |
| `learningResourceTypes`      | `List<String>`                | No       | Types of learning resources, e.g., video, article, tutorial.                      |
| `learningOutcomes`           | `List<String>`                | Yes      | List of learning outcomes expected from the training resource.                    |
| `expertiseLevel`             | `String`                      | Yes      | Expertise level required for the training resource, e.g., beginner, intermediate. |
| `contentResourceTypes`       | `List<String>`                | No       | Types of content included in the training resource, e.g., text, multimedia.       |
| `qualifications`             | `List<String>`                | No       | List of qualifications or certifications associated with the resource.            |
| `duration`                   | `String`                      | No       | Duration of the training resource, e.g., "2 hours".                               |
| `languages`                  | `List<String>`                | Yes      | Languages in which the training resource is available.                            |
| `geographicalAvailabilities` | `List<String>`                | Yes      | List of geographical locations where the resource is available.                   |
| `scientificDomains`          | `List<ServiceProviderDomain>` | Yes      | List of scientific domains and subdomains relevant to the training resource.      |
| `contact`                    | `ServiceMainContact`          | Yes      | Contact details for the main contact person for the training resource.            |
| `catalogueId`                | `String`                      | No       | Catalogue identifier for the training resource.                                   |

#### Nested Objects

##### AlternativeIdentifier

| Field   | Type     | Required | Description                          |
|---------|----------|----------|--------------------------------------|
| `type`  | `String` | No       | Type of the alternative identifier.  |
| `value` | `String` | No       | Value of the alternative identifier. |

##### ServiceProviderDomain

| Field                 | Type     | Required | Description                    |
|-----------------------|----------|----------|--------------------------------|
| `scientificDomain`    | `String` | Yes      | Main scientific domain.        |
| `scientificSubdomain` | `String` | Yes      | Specific scientific subdomain. |

##### ServiceMainContact

| Field          | Type     | Required | Description                        |
|----------------|----------|----------|------------------------------------|
| `firstName`    | `String` | Yes      | First name of the main contact.    |
| `lastName`     | `String` | Yes      | Last name of the main contact.     |
| `email`        | `String` | Yes      | Email address of the main contact. |
| `phone`        | `String` | No       | Phone number of the main contact.  |
| `position`     | `String` | No       | Position of the main contact.      |
| `organisation` | `String` | No       | Organization of the main contact.  |

### Example

```json
{
  "id": "training_001",
  "title": "Introduction to Data Science",
  "resourceOrganisation": "Data Science Institute",
  "resourceProviders": ["Provider A", "Provider B"],
  "authors": ["Author One", "Author Two"],
  "url": "https://example.com/training-resource",
  "urlType": "landingPage",
  "eoscRelatedServices": ["Service A", "Service B"],
  "alternativeIdentifiers": [
    {
      "type": "DOI",
      "value": "10.1234/training"
    }
  ],
  "description": "An introductory course on data science concepts.",
  "keywords": ["Data Science", "Machine Learning"],
  "license": "Creative Commons Attribution 4.0",
  "accessRights": "Open Access",
  "versionDate": "2024-09-10T00:00:00Z",
  "targetGroups": ["Researchers", "Students"],
  "learningResourceTypes": ["Course", "Tutorial"],
  "learningOutcomes": ["Understand basics of data science", "Apply machine learning models"],
  "expertiseLevel": "Beginner",
  "contentResourceTypes": ["Video", "PDF"],
  "qualifications": ["Certificate of Completion"],
  "duration": "3 hours",
  "languages": ["English", "Spanish"],
  "geographicalAvailabilities": ["Europe", "Global"],
  "scientificDomains": [
    {
      "scientificDomain": "Computer Science",
      "scientificSubdomain": "Machine Learning"
    }
  ],
  "contact": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "+123456789",
    "position": "Course Coordinator",
    "organisation": "Data Science Institute"
  },
  "catalogueId": "catalogue_001"
}
```

### Vocabulary

| Field         | Type                  | Required | Description                                             |
|---------------|-----------------------|----------|---------------------------------------------------------|
| `id`          | `String`              | auto-gen | A unique identifier for the vocabulary.                 |
| `name`        | `String`              | Yes      | The name of the vocabulary.                             |
| `description` | `String`              | No       | A brief description of the vocabulary.                  |
| `parentId`    | `String`              | No       | The identifier of the parent vocabulary, if applicable. |
| `type`        | `String`              | Yes      | Specifies the type/category of the vocabulary.          |
| `extras`      | `Map<String, String>` | No       | A map for storing additional key-value pairs.           |

#### Example

```json
{
    "id": "access_mode-free",
    "name": "Free",
    "description": "Users can freely access the Resource provided, registration may be needed.",
    "parentId": null,
    "type": "Access mode",
    "extras": {}
}
```

---

## List of Vocabularies
  - [ACCESS_MODE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ACCESS_MODE.json)
  - [ACCESS_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ACCESS_TYPE.json)
  - [CATALOGUE_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CATALOGUE_STATE.json)
  - [CATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CATEGORY.json)
  - [COUNTRY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/COUNTRY.json)
  - [CT_COMPATIBILITY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CT_COMPATIBILITY.json)
  - [CT_PROTOCOL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CT_PROTOCOL.json)
  - [DS_CLASSIFICATION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_CLASSIFICATION.json)
  - [DS_COAR_ACCESS_RIGHTS_1_0](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_COAR_ACCESS_RIGHTS_1_0.json)
  - [DS_JURISDICTION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_JURISDICTION.json)
  - [DS_PERSISTENT_IDENTITY_SCHEME](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_PERSISTENT_IDENTITY_SCHEME.json)
  - [DS_RESEARCH_ENTITY_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_RESEARCH_ENTITY_TYPE.json)
  - [FUNDING_BODY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/FUNDING_BODY.json)
  - [FUNDING_PROGRAM](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/FUNDING_PROGRAM.json)
  - [GEOGRAPHIC_LOCATION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/GEOGRAPHIC_LOCATION.json)
  - [IR_EOSC_GUIDELINE_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/IR_EOSC_GUIDELINE_TYPE.json)
  - [IR_IDENTIFIER_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/IR_IDENTIFIER_TYPE.json)
  - [IR_NAME_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/IR_NAME_TYPE.json)
  - [IR_RESOURCE_TYPE_GENERAL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/IR_RESOURCE_TYPE_GENERAL.json)
  - [IR_STATUS](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/IR_STATUS.json)
  - [LANGUAGE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/LANGUAGE.json)
  - [LIFE_CYCLE_STATUS](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/LIFE_CYCLE_STATUS.json)
  - [MARKETPLACE_LOCATION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/MARKETPLACE_LOCATION.json)
  - [MONITORING_MONITORED_BY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/MONITORING_MONITORED_BY.json)
  - [ORDER_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ORDER_TYPE.json)
  - [PROVIDER_AREA_OF_ACTIVITY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_AREA_OF_ACTIVITY.json)
  - [PROVIDER_ESFRI_DOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_ESFRI_DOMAIN.json)
  - [PROVIDER_ESFRI_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_ESFRI_TYPE.json)
  - [PROVIDER_HOSTING_LEGAL_ENTITY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_HOSTING_LEGAL_ENTITY.json)
  - [PROVIDER_LEGAL_STATUS](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_LEGAL_STATUS.json)
  - [PROVIDER_LIFE_CYCLE_STATUS](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_LIFE_CYCLE_STATUS.json)
  - [PROVIDER_MERIL_SCIENTIFIC_DOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_MERIL_SCIENTIFIC_DOMAIN.json)
  - [PROVIDER_MERIL_SCIENTIFIC_SUBDOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_MERIL_SCIENTIFIC_SUBDOMAIN.json)
  - [PROVIDER_NETWORK](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_NETWORK.json)
  - [PROVIDER_SOCIETAL_GRAND_CHALLENGE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_SOCIETAL_GRAND_CHALLENGE.json)
  - [PROVIDER_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_STATE.json)
  - [PROVIDER_STRUCTURE_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_STRUCTURE_TYPE.json)
  - [REGION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/REGION.json)
  - [RELATED_PLATFORM](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/RELATED_PLATFORM.json)
  - [RESEARCH_CATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/RESEARCH_CATEGORY.json)
  - [RESOURCE_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/RESOURCE_STATE.json)
  - [SCIENTIFIC_DOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SCIENTIFIC_DOMAIN.json)
  - [SCIENTIFIC_SUBDOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SCIENTIFIC_SUBDOMAIN.json)
  - [SEMANTIC_RELATIONSHIP](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SEMANTIC_RELATIONSHIP.json)
  - [SERVICE_CATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SERVICE_CATEGORY.json)
  - [SERVICE_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SERVICE_TYPE.json)
  - [SUBCATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SUBCATEGORY.json)
  - [SUPERCATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SUPERCATEGORY.json)
  - [TARGET_USER](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TARGET_USER.json)
  - [TEMPLATE_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TEMPLATE_STATE.json)
  - [TRL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TRL.json)
  - [TR_ACCESS_RIGHT](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_ACCESS_RIGHT.json)
  - [TR_CONTENT_RESOURCE_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_CONTENT_RESOURCE_TYPE.json)
  - [TR_DCMI_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_DCMI_TYPE.json)
  - [TR_EXPERTISE_LEVEL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_EXPERTISE_LEVEL.json)
  - [TR_QUALIFICATION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_QUALIFICATION.json)
  - [TR_URL_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_URL_TYPE.json)

---

## Data Validation
This project provides [LinkML](https://linkml.io/) schemas for validating your data. Users can validate their data files 
(e.g., YAML, JSON) against these schemas to ensure compliance with the defined structure, data types, and constraints. 
Simply provide your data and use LinkML’s built-in tools or Python libraries to run the validation process. Errors or 
mismatches will be reported to help you identify and fix issues.
  - [View All Available Schemas](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/linkml/schemas) to
    explore the structures and constraints defined for validation.
  - [Example Data Files](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/linkml/data) are provided to
    help you get started quickly and understand the expected format.

### Quick Guide (Linux based systems):
To validate your data against the provided LinkML schemas:
1. Install LinkML 
   `pip install linkml`
2. Download [schemas](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/linkml/schemas) folder
3. Create a folder for your data 
   `mkdir path/to/data`
4. Run the validation command 
   `linkml-validate -s path/to/schemas/schema.yaml path/to/data/data.yaml`