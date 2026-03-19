<div align="center">
  <img src='https://eosc.eu/wp-content/uploads/2024/02/EOSC-Beyond-logo.png'>
</div>

# Resource Catalogue Documentation [v5.3.0]

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
<a href="https://confluence.egi.eu/display/EOSCBeyond/Software+and+Services+Quality+Assurance+%28SQA%29+guidelines">
<img src="https://img.shields.io/badge/SQAaaS-Bronze-CD7F32"/></a>

---

## Description

**Resource Catalogue Documentation** provides a comprehensive guide to the API endpoints, models, and core components
of the **[Resource Catalogue](https://github.com/madgeek-arc/resource-catalogue)** project, offering detailed
descriptions of each controller, along with their
associated functionalities and endpoints. It includes an overview of its data models and a detailed list of vocabularies
used within the platform. Additionally, the documentation provides schemas for validating data of the various classes,
ensuring consistency and reliability across the system.

---

## Table of Contents

1. [API](#api)
2. [Swagger UI](#swagger-ui)
3. [Controllers](#controllers)
    1. [Adapter Controller](#adapter-controller)
    2. [Catalogue Controller](#catalogue-controller)
    3. [Configuration Template Instance Controller](#configuration-template-instance-controller)
    4. [Datasource Controller](#datasource-controller)
    5. [Deployable Application Controller](#deployable-application-controller)
    6. [Interoperability Record Controller](#interoperability-record-controller)
    7. [Organisation Controller](#organisation-controller)
    8. [Public Controller](#public-controller)
    9. [Resource Interoperability Record Controller](#resource-interoperability-record-controller)
    10. [Service Controller](#service-controller)
    11. ~~[Service Extensions Controller](#service-extensions-controller)~~ (*deprecated*)
    12. [Training Resource Controller](#training-resource-controller)
    13. [Vocabulary Controller](#vocabulary-controller)
4. [Model](#model)
    1. [Adapter](#adapter)
    2. [Catalogue](#catalogue)
    3. [Configuration Template Instance](#configuration-template-instance)
    4. [Datasource](#datasource)
    5. [Deployable Application](#deployable-application)
    6. ~~[Helpdesk](#helpdesk)~~ (*deprecated*)
    7. [Interoperability Record](#interoperability-record)
    8. ~~[Monitoring](#monitoring)~~ (*deprecated*)
    9. [Organisation](#organisation)
    10. [Resource Interoperability Record](#resource-interoperability-record)
    11. [Service](#service)
    12. [Training Resource](#training-resource)
    13. [Vocabulary](#vocabulary)
5. [List of Vocabularies](#list-of-vocabularies)
6. [Data Validation](#data-validation)
7. [External Services](#external-services)

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

- ### Adapter Controller

  #### Operations for Adapters

    - DELETE
        - Deletes the Adapter with the given id.
          ```diff
          /adapter/{prefix}/{suffix}
          Params:
            prefix : String [required]
            suffix: String [required]
          ```  

    - GET
        - Returns the Adapter with the given id.
          ```diff
          /adapter/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
          ```
        - Returns a list of Adapters where user is admin.
          ```diff
          /adapter/getMy
          ```
        - Filter a list of Adapters based on a set of filters or get a list of all Adapters in the Catalogue.
          ```diff
          /adapter/all
          Params:
            query : String (Keyword to refine the search) [optional]
            from : String (Starting index in the result set, default 0) [optional]
            quantity: String (Quantity to be fetched, default 10) [optional]
            order: String (Order of results - asc/desc, default asc) [optional]
            orderField: String (Field to use for ordering) [optional]
          ```

    - POST
        - Creates a new Adapter.
          ```diff
          /adapter
          Body:
            Adapter JSON [required]
          ```

    - PUT
        - Updates a specific Adapter.
          ```diff
          /adapter
          Body:
            Adapter JSON [required]
          ```

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
        - Deletes the Organisation of the specific Catalogue with the given id.
          ```diff
          /catalogue/{catalogueId}/organisation/{prefix}/{suffix}
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
        - Get all the Training Resources of a specific Organisation of a specific Catalogue.
          ```diff
          /catalogue/{catalogueId}/{prefix}/{suffix}/trainingResource/all
          Params:
            catalogueId: String [required]
            prefix : String [required]
            suffix : String [required]
          ```
        - Get all the Services of a specific Organisation of a specific Catalogue.
          ```diff
          /catalogue/{catalogueId}/{prefix}/{suffix}/service/all
          Params:
            catalogueId: String [required]
            prefix : String [required]
            suffix : String [required]
          ```
        - Get all the Interoperability Records of a specific Organisation of a specific Catalogue.
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
        - Returns the Organisation of the specific Catalogue with the given id.
          ```diff
          /catalogue/{catalogueId}/organisation/{prefix}/{suffix}
          Params:
            catalogueId: String [required]
            prefix : String [required]
            suffix : String [required]
          ```
        - Filter a list of Organisations based on a set of filters or get a list of all Organisations in the Catalogue.
          ```diff
          /catalogue/{catalogueId}/organisation/all
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
        - Creates a new Organisation for the specific Catalogue.
          ```diff
          /catalogue/{catalogueId}/organisation
          Params:
            catalogueId: String [required]
          Body:
            Organisation JSON [required]
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
        - Updates the Organisation of the specific Catalogue.
          ```diff
          /catalogue/{catalogueId}/organisation
          Params:
            catalogueId: String [required]
            comment: String [optional]
          Body:
            Organisation JSON [required]
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
        - Filter a list of Configuration Template Instances based on a set of filters or get a list of all Configuration
          Template Instances in the Catalogue.
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

- ### Deployable Application Controller

  #### Operations for Deployable Applications

    - DELETE
        - Deletes the Deployable Application of the specific Catalogue given its id.
          ```diff
          /deployableApplication/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
            catalogue_id: String (default 'eosc') [optional]
          ```

    - GET
        - Returns the Deployable Application of the specific Catalogue given its id.
          ```diff
            /deployableApplication/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
              catalogue_id: String (default 'eosc') [optional]
          ```
        - Returns a list of all inactive Deployable Applications.
          ```diff
            /deployableApplication/inactive/all
            Params:
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
              catalogue: String (default 'eosc') [optional]
          ```
        - Returns a list of Deployable Applications under a specific Organisation.
          ```diff
            /deployableApplication/byOrganisation/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
          ```
        - Returns a list of Deployable Applications of a specific Catalogue.
          ```diff
            /deployableApplication/byCatalogue/{id}
            Params:
              id: String [required]
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
          ```
        - Returns a list of all Deployable Applications of the specific Catalogue in the Portal.
          ```diff
            /deployableApplication/all
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
        - Creates a new Deployable Application.
          ```diff
            /deployableApplication
            Body:
              Deployable Application JSON [required]
        - Validates a Deployable Application without actually changing the repository.
          ```diff
          /deployableApplication/validate
          Body:
            Deployable Application JSON [required]
    - PUT
        - Updates a specific Deployable Application.
          ```diff
          /deployableApplication
          Params:
            comment: String
          Body:
            Deployable Application JSON [required]
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
        - Filter a list of Interoperability Records based on a set of filters or get a list of all Interoperability
          Records
          of a specific Organisation in the Catalogue.
          ```diff
          /interoperabilityRecord/byOrganisation/{prefix}/{suffix}
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

- ### Organisation Controller

  #### Operations for Organisations

    - DELETE
        - Deletes the Organisation of the specific Catalogue given its id.
          ```diff
          /organisation/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
          ```
        - Deletes the Draft Organisation of the specific Catalogue given its id.
          ```diff
          /organisation/draft/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
          ```      

    - GET
        - Returns the Organisation of the specific Catalogue given its id.
          ```diff
          /organisation/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
            catalogue_id: String (default 'eosc') [optional]
          ```
        - Validates a url.
          ```diff
          /organisation/validateUrl
          Params:
            urlForValidation: URL [required]
          ```             
        - Get a list of all inactive Services of a specific Organisation.
          ```diff
          /organisation/services/inactive/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
          ```
        - Get a list of all rejected resources (Services or Training Resources) of a specific Organisation.
          ```diff
          /organisation/services/inactive/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
            resourceType: String [required]
            query : String (Keyword to refine the search) [optional]
            from : String (Starting index in the result set, default 0) [optional]
            quantity: String (Quantity to be fetched, default 10) [optional]
            order: String (Order of results - asc/desc, default asc) [optional]
            orderField: String (Field to use for ordering) [optional]
        - Get all inactive Organisations of the Catalogue.
          ```diff
          /organisation/inactive/all
          ```
        - Returns a list of Organisations where user is admin.
          ```diff
          /organisation/getMyServiceProviders
          ```
        - Returns the Draft Organisation given its id.
          ```diff
          /organisation/draft/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
          ```
        - Returns a list of Draft Organisations where user is admin.
          ```diff
          /organisation/draft/getMyDraftProviders
          ```
        - Get a list of all Organisations under a specific Catalogue.
          ```diff
          /organisation/byCatalogue/{id}
          Params:
            id: String [required]
            query : String (Keyword to refine the search) [optional]
            from : String (Starting index in the result set, default 0) [optional]
            quantity: String (Quantity to be fetched, default 10) [optional]
            order: String (Order of results - asc/desc, default asc) [optional]
            orderField: String (Field to use for ordering) [optional]
        - Filter a list of Organisations based on a set of filters or get a list of all Organisations in the Catalogue.
          ```diff
          /organisation/all
          Params:
            suspended: boolean (default false) [optional]
            query : String (Keyword to refine the search) [optional]
            from : String (Starting index in the result set, default 0) [optional]
            quantity: String (Quantity to be fetched, default 10) [optional]
            order: String (Order of results - asc/desc, default asc) [optional]
            orderField: String (Field to use for ordering) [optional]
            catalogue: String (default 'eosc') [optional]

    - POST
        - Create a new Organisation.
          ```diff
          /organisation
          Body:
            Organisation JSON [required]
          ```
        - Create a new Draft Organisation.
          ```diff
          /organisation/draft
          Body:
            Organisation JSON [required]
          ```
        - Validates the Organisation without actually changing the repository.
          ```diff
          /organisation/validate
          Body:
            Organisation JSON [required]
          ```

    - PUT
        - Updates the Organisation of the specific Catalogue give its id.
          ```diff
          /organisation
          Params:
            catalogue_id: String (default 'eosc') [optional]
            comment: String [optional]
          Body:
            Organisation JSON [required]
          ```
        - Updates the Draft Organisation of the specific Catalogue give its id.
          ```diff
          /organisation/draft
          Body:
            Organisation JSON [required]
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
        - Returns the Public Organisation with the given id.
          ```diff
          /public/organisation/{id}
          Params:
            id: String [required]
          ```
        - Returns a list of Public Organisations where user is admin.
          ```diff
          /public/organisation/my
          ```
        - Get a list of all Public Organisations of the specific Catalogue in the Portal.
          ```diff
          /public/organisation/all
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
        - Filter a list of Resource Interoperability Records based on a set of filters or get a list of all Resource
          Interoperability Records in the Catalogue.
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
        - Returns a list of Draft Services under a specific Organisation.
          ```diff
            /service/draft/byOrganisation/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
          ```
        - Returns a list of Services under a specific Organisation.
          ```diff
            /service/byOrganisation/{prefix}/{suffix}
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
        - Returns a list of Training Resources under a specific Organisation.
          ```diff
            /trainingResource/byOrganisation/{prefix}/{suffix}
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

### Adapter

| Field                 | Type                    | Required | Description                                                                                                |
|-----------------------|-------------------------|----------|------------------------------------------------------------------------------------------------------------|
| `id`                  | `String`                | auto-gen | Unique identifier for the adapter.                                                                         |
| `name`                | `String`                | Yes      | Name of the resource.                                                                                      |
| `urls`                | `List<URL>`             | No       | URLs resolving to the resource.                                                                            |
| `alternativePIDs`     | `List<AlternativePIDs>` | No       | Other persistent identifiers.                                                                              |
| `nodePID`             | `Vocabulary`            | Yes      | Node the resource belongs to.                                                                              |
| `description`         | `String`                | Yes      | Description of the adapter.                                                                                |
| `publishingDate`      | `Date`                  | Yes      | Date in which the resource was made available for discovery and access to others.                          |
| `type`                | `String`                | Yes      | Type of the resource.                                                                                      |
| `resourceOwner`       | `Vocabulary`            | Yes      | The organisation that manages or delivers the Resource.                                                    |
| `linkedResource`      | `LinkedResource`        | Yes      | Service or Guideline linked with the Adapter.                                                              |
| `tagline`             | `String`                | Yes      | Short tagline summarizing the adapter.                                                                     |
| `logo`                | `URL`                   | No       | Link to the logo/visual identity of the adapter.                                                           |
| `documentation`       | `URL`                   | Yes      | Documentation webpage (e.g., read-the-docs page).                                                          |
| `repository`          | `URL`                   | Yes      | Code repository webpage (e.g., a GitHub repository).                                                       |
| `package`             | `List<URL>`             | Yes      | Links to the latest package release page(s) (e.g., PyPI project, Docker image, GitHub releases page).      |
| `programmingLanguage` | `Vocabulary`            | Yes      | Programming language.                                                                                      |
| `license`             | `License`               | No       | A license document that applies to this resource.                                                          |
| `version`             | `String`                | Yes      | Software version.                                                                                          |
| `changeLog`           | `String`                | Yes      | Changes in the latest version.                                                                             |
| `lastUpdate`          | `Date`                  | Yes      | Latest update date.                                                                                        |
| `creators`            | `List<Creators>`        | Yes      | The main researchers involved in producing the data, or the authors of the publication, in priority order. |
| `publicContacts`      | `List<String>`          | Yes      | List of public contact emails.                                                                             |
| `sqa`                 | `SQA`                   | No       | Software Quality Assurance information.                                                                    |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### LinkedResource

| Field           | Type     | Required | Description                                                               |
|-----------------|----------|----------|---------------------------------------------------------------------------|
| `resource_type` | `String` | Yes      | Type of the linked resource (e.g., `service`, `interoperability_record`). |
| `id`            | `String` | Yes      | ID of the linked resource.                                                |

##### License

| Field         | Type         | Required | Description                                                                  |
|---------------|--------------|----------|------------------------------------------------------------------------------|
| `licenseName` | `Vocabulary` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`        | No       | A license document that applies to this content, typically indicated by URL. |

##### Creators

| Field          | Type                 | Required | Description                    |
|----------------|----------------------|----------|--------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator. |
| `lastName`     | `String`             | Yes      | Last name of the creator.      |
| `email`        | `String`             | Yes      | Email of the creator.          |
| `role`         | `Vocabulary`         | No       |                                |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the creator.           |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the creator.   |

##### PIDs

| Field              | Type     | Required | Description                                                                      |
|--------------------|----------|----------|----------------------------------------------------------------------------------|
| `creatorPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `creatorPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the creator.               |

##### Affiliations

| Field                   | Type                          | Required | Description                                                        |
|-------------------------|-------------------------------|----------|--------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the creator.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the creator. |

##### AffiliationIdentifier

| Field         | Type     | Required | Description |
|---------------|----------|----------|-------------|
| `creatorID`   | `String` | Yes      |             |
| `creatorType` | `String` | Yes      |             |

##### SQA

| Field      | Type         | Required | Description                                |
|------------|--------------|----------|--------------------------------------------|
| `sqaURL`   | `URL`        | No       | Automatically filled after SQA assessment. |
| `sqaBadge` | `Vocabulary` | No       | Automatically filled after SQA assessment. |

#### Example

```json
{
  "id": "adapter_001",
  "name": "Sample Adapter",
  "urls": [
    "https://example.com/adapter",
    "https://mirror.example.com/adapter"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/adapter",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": null,
  "description": "This is a sample adapter description.",
  "publishingDate": "2024-01-15T00:00:00Z",
  "type": "Adapter",
  "resourceOwner": null,
  "linkedResource": {
    "resource_type": "service",
    "id": "service_001"
  },
  "tagline": "Sample tagline",
  "logo": "https://example.com/logo.png",
  "documentation": "https://example.com/documentation",
  "repository": "https://example.com/repository",
  "package": [
    "https://example.com/package1",
    "https://example.com/package2"
  ],
  "programmingLanguage": null,
  "license": {
    "licenseName": null,
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  },
  "version": "1.0.0",
  "changeLog": "Initial release.",
  "lastUpdate": "2025-06-19T13:10:58.119Z",
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": null,
      "PIDs": [
        {
          "creatorPID": "0000-0001-2345-6789",
          "creatorPIDScheme": "ORCID"
        }
      ],
      "affiliations": [
        {
          "affiliationName": "Sample Organisation",
          "affiliationIdentifier": [
            {
              "creatorID": "https://ror.org/example123",
              "creatorType": "ROR"
            }
          ]
        }
      ]
    }
  ],
  "publicContacts": [
    "support@example.com",
    "info@example.com"
  ],
  "sqa": {
    "sqaURL": null,
    "sqaBadge": null
  }
}
```

### Catalogue

| Field                    | Type                          | Required | Description                                                      |
|--------------------------|-------------------------------|----------|------------------------------------------------------------------|
| `id`                     | `String`                      | auto-gen | Unique identifier for the catalogue.                             |
| `abbreviation`           | `String`                      | Yes      | Abbreviation of the catalogue's name.                            |
| `name`                   | `String`                      | Yes      | Full name of the catalogue.                                      |
| `node`                   | `String`                      | No       | Catalogue's original Node.                                       |
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

| Field                 | Type     | Required | Description                                     |
|-----------------------|----------|----------|-------------------------------------------------|
| `streetNameAndNumber` | `String` | Yes      | Street address of the catalogue's location.     |
| `postalCode`          | `String` | Yes      | Postal code of the catalogue's location.        |
| `city`                | `String` | Yes      | City where the catalogue is located.            |
| `region`              | `String` | No       | Region or state where the catalogue is located. |
| `country`             | `String` | Yes      | Country where the catalogue is located.         |

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
  "node": "node-sandbox",
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
  "tags": [
    "science",
    "research"
  ],
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
  "participatingCountries": [
    "Country1",
    "Country2"
  ],
  "affiliations": [
    "Affiliation1",
    "Affiliation2"
  ],
  "networks": [
    "Network1",
    "Network2"
  ],
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

| Field                     | Type         | Required | Description                                                |
|---------------------------|--------------|----------|------------------------------------------------------------|
| `id`                      | `String`     | auto-gen | Unique identifier for the configuration template instance. |
| `resourceId`              | `Vocabulary` | Yes      | Identifier of the resource associated with the instance.   |
| `configurationTemplateId` | `Vocabulary` | Yes      | Identifier of the configuration template used.             |
| `nodePID`                 | `Vocabulary` | Yes      | Configuration Template Instance's original Node.           |
| `description`             | `String`     | No       | Description.                                               |
| `payload`                 | `Composite`  | Yes      | The configuration data or settings in JSON format.         |

### Example

```json
{
  "id": "conf_temp_inst_001",
  "resourceId": "resource_001",
  "configurationTemplateId": "conf_temp_001",
  "nodePID": "node-sandbox",
  "description": "This is a description",
  "payload": {
    "key1": "value",
    "key2": "value"
  }
}
```

### Datasource

| Field                       | Type                             | Required | Description                                                                                                                           |
|-----------------------------|----------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | `String`                         | auto-gen | Unique identifier for the datasource.                                                                                                 |
| `name`                      | `String`                         | Yes      | Name of the datasource.                                                                                                               |
| `urls`                      | `List<URL>`                      | No       | URLs resolving to the datasource.                                                                                                     |
| `alternativePIDs`           | `List<AlternativePIDs>`          | No       | Other persistent identifiers.                                                                                                         |
| `nodePID`                   | `Vocabulary`                     | Yes      | Node the resource belongs to.                                                                                                         |
| `description`               | `String`                         | Yes      | Description of the datasource.                                                                                                        |
| `publishingDate`            | `Date`                           | Yes      | Date in which the resource was made available for discovery and access to others.                                                     |
| `type`                      | `String`                         | Yes      | Type of the resource.                                                                                                                 |
| `resourceOwner`             | `Vocabulary`                     | Yes      | The organisation that manages or delivers the datasource.                                                                             |
| `serviceProviders`          | `Vocabulary`                     | No       | The name(s) (or abbreviation(s)) of Organisation(s) that manage or deliver the Service in federated scenarios.                        |
| `webpage`                   | `URL`                            | Yes      | Webpage with information about the Service usually hosted and maintained by the Organisation.                                         |
| `logo`                      | `URL`                            | No       | Link to the logo/visual identity of the datasource.                                                                                   |
| `jurisdiction`              | `Vocabulary`                     | Yes      | The property defines the jurisdiction of the users of the data source, based on the vocabulary for this property.                     |
| `scientificDomains`         | `List<ScientificDomains>`        | No       |                                                                                                                                       |
| `categories`                | `List<Categories>`               | No       |                                                                                                                                       |
| `accessTypes`               | `Vocabulary`                     | Yes      | The way a user can access the datasource (Remote, Physical, Virtual, etc.).                                                           |
| `tags`                      | `List<String>`                   | No       | Keywords associated to the datasource to simplify search by relevant keywords.                                                        |
| `trl`                       | `Vocabulary`                     | Yes      | The Technology Readiness Level of the datasource (to be further updated in the context of the EOSC).                                  |
| `termsOfUse`                | `URL`                            | No       | Webpage describing the rules, datasource conditions and usage policy which one must agree to abide by in order to use the datasource. |
| `privacyPolicy`             | `URL`                            | No       | Link to the privacy policy applicable to the datasource.                                                                              |
| `accessPolicy`              | `URL`                            | No       | Information about the access policies that apply.                                                                                     |
| `orderType`                 | `Vocabulary`                     | Yes      | Information on the ordering process type.                                                                                             |
| `order`                     | `URL`                            | No       | Webpage through which an order for the Resource can be placed.                                                                        |
| `mainContact`               | `MainContact`                    | Yes      |                                                                                                                                       |
| `publicContacts`            | `List<String>`                   | Yes      | List of public contact emails.                                                                                                        |
| `submissionPolicyURL`       | `URL`                            | No       | URL of the submission policy.                                                                                                         |
| `preservationPolicyURL`     | `URL`                            | No       | URL of the preservation policy.                                                                                                       |
| `versionControl`            | `Boolean`                        | No       | Indicates if version control is used.                                                                                                 |
| `persistentIdentitySystems` | `List<PersistentIdentitySystem>` | No       | List of persistent identity systems associated with the datasource.                                                                   |
| `datasourceClassification`  | `Vocabulary`                     | Yes      | The specific type of the data source based on the vocabulary defined for this property.                                               |
| `researchProductTypes`      | `Vocabulary`                     | Yes      | The types of OpenAIRE products managed by the data source, based on the vocabulary for this property.                                 |
| `thematic`                  | `Boolean`                        | Yes      | Boolean value specifying if the data source is dedicated to a given discipline or is instead discipline agnostic.                     |
| `metadataLicense`           | `MetadataLicense`                | No       |                                                                                                                                       |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### ScientificDomains

| Field                 | Type         | Required | Description                                                                                                  |
|-----------------------|--------------|----------|--------------------------------------------------------------------------------------------------------------|
| `scientificDomain`    | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of datasources.                            |
| `scientificSubdomain` | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of datasources, within the defined domain. |

##### Categories

| Field         | Type         | Required | Description                                                                                                  |
|---------------|--------------|----------|--------------------------------------------------------------------------------------------------------------|
| `category`    | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of datasources.                            |
| `subcategory` | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of datasources, within the defined domain. |

##### MainContact

| Field          | Type                 | Required | Description                               |
|----------------|----------------------|----------|-------------------------------------------|
| `firstName`    | `String`             | Yes      | First name of the main contact person.    |
| `lastName`     | `String`             | Yes      | Last name of the main contact person.     |
| `email`        | `String`             | Yes      | Email address of the main contact person. |
| `role`         | `Vocabulary`         | No       | Role of the main contact person.          |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the main contact person.          |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the main contact person.  |

##### PIDs

| Field                  | Type     | Required | Description                                                                      |
|------------------------|----------|----------|----------------------------------------------------------------------------------|
| `mainContactPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `mainContactPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the main contact.          |

##### Affiliations

| Field                   | Type                          | Required | Description                                                             |
|-------------------------|-------------------------------|----------|-------------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the main contact.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the main contact. |

##### AffiliationIdentifier

| Field             | Type     | Required | Description |
|-------------------|----------|----------|-------------|
| `mainContactID`   | `String` | Yes      |             |
| `mainContactType` | `String` | Yes      |             |

##### PersistentIdentitySystem

| Field                                  | Type         | Required | Description                                                                      |
|----------------------------------------|--------------|----------|----------------------------------------------------------------------------------|
| `persistentIdentityProductType`        | `Vocabulary` | No       | Specify the ProductType to which the persistent identifier is referring to.      |
| `persistentIdentityProductTypeSchemes` | `Vocabulary` | No       | Specify the list of persistent identifier schemes used to refer to ProductTypes. |

##### MetadataLicense

| Field                 | Type     | Required | Description                       |
|-----------------------|----------|----------|-----------------------------------|
| `metadataLicenseName` | `String` | No       | The name of the metadata License. |
| `metadataLicenseURL`  | `URL`    | No       | The url of the metadata License.  |

### Example

```json
{
  "id": "datasource_001",
  "name": "European Research Data Repository",
  "urls": [
    "https://example.com/datasource",
    "https://mirror.example.com/datasource"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/datasource",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": null,
  "description": "A comprehensive repository for European research data across multiple scientific domains.",
  "publishingDate": "2024-01-15T00:00:00Z",
  "type": "Repository",
  "resourceOwner": null,
  "serviceProviders": null,
  "webpage": "https://example.com/datasource/info",
  "logo": "https://example.com/datasource/logo.png",
  "jurisdiction": null,
  "scientificDomains": [
    {
      "scientificDomain": null,
      "scientificSubdomain": null
    }
  ],
  "categories": [
    {
      "category": null,
      "subcategory": null
    }
  ],
  "accessTypes": null,
  "tags": [
    "open data",
    "research",
    "EOSC"
  ],
  "trl": null,
  "termsOfUse": "https://example.com/datasource/terms",
  "privacyPolicy": "https://example.com/datasource/privacy",
  "accessPolicy": "https://example.com/datasource/access-policy",
  "orderType": null,
  "order": "https://example.com/datasource/order",
  "mainContact": {
    "firstName": "Jane",
    "lastName": "Smith",
    "email": "jane.smith@example.com",
    "role": null,
    "PIDs": [
      {
        "mainContactPID": "0000-0001-2345-6789",
        "mainContactPIDScheme": "ORCID"
      }
    ],
    "affiliations": [
      {
        "affiliationName": "European Research Institute",
        "affiliationIdentifier": [
          {
            "mainContactID": "https://ror.org/example123",
            "mainContactType": "ROR"
          }
        ]
      }
    ]
  },
  "publicContacts": [
    "support@example.com",
    "info@example.com"
  ],
  "submissionPolicyURL": "https://example.com/datasource/submission-policy",
  "preservationPolicyURL": "https://example.com/datasource/preservation-policy",
  "versionControl": true,
  "persistentIdentitySystems": [
    {
      "persistentIdentityProductType": null,
      "persistentIdentityProductTypeSchemes": null
    }
  ],
  "datasourceClassification": null,
  "researchProductTypes": null,
  "thematic": false,
  "metadataLicense": {
    "metadataLicenseName": "Creative Commons CC0 1.0",
    "metadataLicenseURL": "https://creativecommons.org/publicdomain/zero/1.0/"
  }
}
```

### Deployable Application

| Field               | Type                      | Required | Description                                                                                                |
|---------------------|---------------------------|----------|------------------------------------------------------------------------------------------------------------|
| `id`                | `String`                  | auto-gen | Unique identifier for the deployable application.                                                          |
| `name`              | `String`                  | Yes      | Name of the resource.                                                                                      |
| `urls`              | `List<URL>`               | No       | URLs resolving to the resource.                                                                            |
| `alternativePIDs`   | `List<AlternativePIDs>`   | No       | Other persistent identifiers.                                                                              |
| `nodePID`           | `Vocabulary`              | Yes      | Node the resource belongs to.                                                                              |
| `description`       | `String`                  | Yes      | Description of the deployable application.                                                                 |
| `publishingDate`    | `Date`                    | Yes      | Date in which the resource was made available for discovery and access to others.                          |
| `type`              | `String`                  | Yes      | Type of the resource.                                                                                      |
| `resourceOwner`     | `Vocabulary`              | Yes      | The organisation that manages or delivers the Resource.                                                    |
| `acronym`           | `String`                  | Yes      | Acronym of the deployable application.                                                                     |
| `tagline`           | `String`                  | No       | Short tagline summarizing the deployable application.                                                      |
| `logo`              | `URL`                     | No       | Link to the logo/visual identity of the deployable application.                                            |
| `scientificDomains` | `List<ScientificDomains>` | No       |                                                                                                            |
| `tags`              | `List<String>`            | No       | Keywords associated with the deployable application.                                                       |
| `creators`          | `List<Creators>`          | Yes      | The main researchers involved in producing the data, or the authors of the publication, in priority order. |
| `publicContacts`    | `List<String>`            | Yes      | List of public contact emails.                                                                             |
| `version`           | `String`                  | Yes      | Version of the deployable application.                                                                     |
| `lastUpdate`        | `Date`                    | No       | Date of the latest update.                                                                                 |
| `license`           | `License`                 | No       | A license document that applies to this resource.                                                          |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### ScientificDomains

| Field                 | Type         | Required | Description                                                                                                |
|-----------------------|--------------|----------|------------------------------------------------------------------------------------------------------------|
| `scientificDomain`    | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of Resources.                            |
| `scientificSubdomain` | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of Resources, within the defined domain. |

##### Creators

| Field          | Type                 | Required | Description                    |
|----------------|----------------------|----------|--------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator. |
| `lastName`     | `String`             | Yes      | Last name of the creator.      |
| `email`        | `String`             | Yes      | Email of the creator.          |
| `role`         | `Vocabulary`         | No       |                                |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the creator.           |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the creator.   |

##### PIDs

| Field              | Type     | Required | Description                                                                      |
|--------------------|----------|----------|----------------------------------------------------------------------------------|
| `creatorPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `creatorPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the creator.               |

##### Affiliations

| Field                   | Type                          | Required | Description                                                        |
|-------------------------|-------------------------------|----------|--------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the creator.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the creator. |

##### AffiliationIdentifier

| Field         | Type     | Required | Description |
|---------------|----------|----------|-------------|
| `creatorID`   | `String` | Yes      |             |
| `creatorType` | `String` | Yes      |             |

##### License

| Field         | Type         | Required | Description                                                                  |
|---------------|--------------|----------|------------------------------------------------------------------------------|
| `licenseName` | `Vocabulary` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`        | No       | A license document that applies to this content, typically indicated by URL. |

#### Example

```json
{
  "id": "deployable_application_001",
  "name": "Sample Deployable Application",
  "urls": [
    "https://example.com/deployable",
    "https://mirror.example.com/deployable"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/deployable",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": null,
  "description": "A sample deployable application description.",
  "publishingDate": "2024-01-15T00:00:00Z",
  "type": "DeployableApplication",
  "resourceOwner": null,
  "acronym": "SDA",
  "tagline": "Sample tagline",
  "logo": "https://example.com/logo.png",
  "scientificDomains": [
    {
      "scientificDomain": null,
      "scientificSubdomain": null
    }
  ],
  "tags": [
    "tag1",
    "tag2"
  ],
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": null,
      "PIDs": [
        {
          "creatorPID": "0000-0001-2345-6789",
          "creatorPIDScheme": "ORCID"
        }
      ],
      "affiliations": [
        {
          "affiliationName": "Sample Organisation",
          "affiliationIdentifier": [
            {
              "creatorID": "https://ror.org/example123",
              "creatorType": "ROR"
            }
          ]
        }
      ]
    }
  ],
  "publicContacts": [
    "support@example.com",
    "info@example.com"
  ],
  "version": "v1",
  "lastUpdate": "2024-09-09T12:00:00Z",
  "license": {
    "licenseName": null,
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  }
}
```

### Helpdesk

| Field                | Type           | Required | Description                                                                     |
|----------------------|----------------|----------|---------------------------------------------------------------------------------|
| `id`                 | `String`       | auto-gen | Unique identifier for the helpdesk.                                             |
| `serviceId`          | `String`       | Yes      | Identifier of the associated service.                                           |
| `catalogueId`        | `String`       | Yes      | Identifier of the catalogue containing this record.                             |
| `node`               | `String`       | No       | Helpdesk's original Node.                                                       |
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
  "catalogueId": "catalogue_001",
  "node": "node-sandbox",
  "services": [
    "serviceA",
    "serviceB"
  ],
  "helpdeskType": "Technical Support",
  "supportGroups": [
    "group1",
    "group2"
  ],
  "organisation": "SupportOrg",
  "emails": [
    "support@example.com",
    "escalation@example.com"
  ],
  "agents": [
    "agent1",
    "agent2"
  ],
  "signatures": [
    "Best regards, Support Team",
    "Thank you for contacting support"
  ],
  "ticketPreservation": true,
  "webform": false
}
```

### Interoperability Record

| Field              | Type                    | Required | Description                                                                                                |
|--------------------|-------------------------|----------|------------------------------------------------------------------------------------------------------------|
| `id`               | `String`                | auto-gen | Unique identifier for the interoperability record.                                                         |
| `name`             | `String`                | Yes      | Name of the resource.                                                                                      |
| `urls`             | `List<URL>`             | No       | URLs resolving to the resource.                                                                            |
| `alternativePIDs`  | `List<AlternativePIDs>` | No       | Other persistent identifiers.                                                                              |
| `nodePID`          | `Vocabulary`            | Yes      | Node the resource belongs to.                                                                              |
| `description`      | `String`                | Yes      | Description of the interoperability record.                                                                |
| `publishingDate`   | `Date`                  | Yes      | Date in which the resource was made available for discovery and access to others.                          |
| `type`             | `String`                | Yes      | Type of the resource.                                                                                      |
| `resourceOwner`    | `Vocabulary`            | Yes      | The organisation that manages or delivers the Resource.                                                    |
| `resourceTypeInfo` | `ResourceTypeInfo`      | Yes      |                                                                                                            |
| `relatedStandards` | `List<RelatedStandard>` | No       | List of related standards connected to the interoperability record.                                        |
| `license`          | `License`               | No       | A license document that applies to this resource.                                                          |
| `creators`         | `List<Creators>`        | Yes      | The main researchers involved in producing the data, or the authors of the publication, in priority order. |
| `publicContacts`   | `List<String>`          | Yes      | List of public contact emails.                                                                             |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### ResourceTypeInfo

| Field                 | Type     | Required | Description                                                                                 |
|-----------------------|----------|----------|---------------------------------------------------------------------------------------------|
| `resourceType`        | `String` | Yes      | A description of the resource (e.g., API, Configuration Template, Policy, Metadata Schema). |
| `resourceTypeGeneral` | `String` | Yes      | The general type of the resource.                                                           |

##### RelatedStandard

| Field                       | Type     | Required | Description                                 |
|-----------------------------|----------|----------|---------------------------------------------|
| `relatedStandardURI`        | `URL`    | No       | URI linking to the related standard.        |
| `relatedStandardIdentifier` | `String` | No       | Name or identifier of the related standard. |

##### License

| Field         | Type         | Required | Description                                                                  |
|---------------|--------------|----------|------------------------------------------------------------------------------|
| `licenseName` | `Vocabulary` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`        | No       | A license document that applies to this content, typically indicated by URL. |

##### Creators

| Field          | Type                 | Required | Description                    |
|----------------|----------------------|----------|--------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator. |
| `lastName`     | `String`             | Yes      | Last name of the creator.      |
| `email`        | `String`             | Yes      | Email of the creator.          |
| `role`         | `Vocabulary`         | No       |                                |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the creator.           |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the creator.   |

##### PIDs

| Field              | Type     | Required | Description                                                                      |
|--------------------|----------|----------|----------------------------------------------------------------------------------|
| `creatorPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `creatorPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the creator.               |

##### Affiliations

| Field                   | Type                          | Required | Description                                                        |
|-------------------------|-------------------------------|----------|--------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the creator.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the creator. |

##### AffiliationIdentifier

| Field         | Type     | Required | Description |
|---------------|----------|----------|-------------|
| `creatorID`   | `String` | Yes      |             |
| `creatorType` | `String` | Yes      |             |

### Example

```json
{
  "id": "interop_001",
  "name": "Sample Interoperability Record",
  "urls": [
    "https://example.com/interop",
    "https://mirror.example.com/interop"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/interop",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": null,
  "description": "A sample interoperability record description.",
  "publishingDate": "2024-01-15T00:00:00Z",
  "type": "InteroperabilityGuidelines",
  "resourceOwner": null,
  "resourceTypeInfo": {
    "resourceType": "API",
    "resourceTypeGeneral": "Software"
  },
  "relatedStandards": [
    {
      "relatedStandardURI": "https://example.com/standard",
      "relatedStandardIdentifier": "standard_001"
    }
  ],
  "license": {
    "licenseName": null,
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  },
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": null,
      "PIDs": [
        {
          "creatorPID": "0000-0001-2345-6789",
          "creatorPIDScheme": "ORCID"
        }
      ],
      "affiliations": [
        {
          "affiliationName": "Research Institute",
          "affiliationIdentifier": [
            {
              "creatorID": "https://ror.org/example123",
              "creatorType": "ROR"
            }
          ]
        }
      ]
    }
  ],
  "publicContacts": [
    "support@example.com",
    "info@example.com"
  ]
}
```

### Monitoring

| Field              | Type                    | Required | Description                                          |
|--------------------|-------------------------|----------|------------------------------------------------------|
| `id`               | `String`                | auto-gen | Unique identifier for the monitoring record.         |
| `serviceId`        | `String`                | Yes      | Identifier of the associated service.                |
| `catalogueId`      | `String`                | Yes      | Identifier of the catalogue containing this record.  |
| `node`             | `String`                | No       | Monitoring's original Node.                          |
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
  "catalogueId": "catalogue_001",
  "node": "node-sandbox",
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

### Organisation

| Field                | Type                    | Required | Description                                                                                                                                             |
|----------------------|-------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                 | `String`                | auto-gen | Unique identifier for the organisation.                                                                                                                 |
| `name`               | `String`                | Yes      | Full name of the organisation.                                                                                                                          |
| `abbreviation`       | `String`                | Yes      | Abbreviation of the organisation's name.                                                                                                                |
| `alternativePIDs`    | `List<AlternativePIDs>` | No       | Other persistent identifiers.                                                                                                                           |
| `nodePID`            | `Vocabulary`            | Yes      | Node the organisation is contributing to.                                                                                                               |
| `website`            | `URL`                   | Yes      | URL of the organisation's website.                                                                                                                      |
| `country`            | `Vocabulary`            | Yes      | Country of incorporation or physical location of the organisation or its coordinating centre in the case of distributed, virtual, and mobile providers. |
| `legalEntity`        | `Boolean`               | Yes      | Indicates if the organisation is a legal entity.                                                                                                        |
| `legalStatus`        | `Vocabulary`            | No       | Legal status of the organisation.                                                                                                                       |
| `hostingLegalEntity` | `Vocabulary`            | No       | Hosting legal entity responsible for the organisation.                                                                                                  |
| `description`        | `String`                | Yes      | Description of the organisation.                                                                                                                        |
| `logo`               | `URL`                   | Yes      | URL of the organisation's logo.                                                                                                                         |
| `multimedia`         | `List<MultimediaPair>`  | No       | List of multimedia items associated with the organisation.                                                                                              |
| `mainContact`        | `MainContact`           | Yes      | Main contact information for the organisation.                                                                                                          |
| `publicContacts`     | `List<String>`          | Yes      | List of public contact emails for the organisation.                                                                                                     |
| `users`              | `List<User>`            | No       | List of users associated with the organisation.                                                                                                         |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### MultimediaPair

| Field            | Type     | Required | Description                      |
|------------------|----------|----------|----------------------------------|
| `multimediaURL`  | `URL`    | No       | URL to the multimedia resource.  |
| `multimediaName` | `String` | No       | Name of the multimedia resource. |

##### MainContact

| Field          | Type                 | Required | Description                               |
|----------------|----------------------|----------|-------------------------------------------|
| `firstName`    | `String`             | Yes      | First name of the main contact person.    |
| `lastName`     | `String`             | Yes      | Last name of the main contact person.     |
| `email`        | `String`             | Yes      | Email address of the main contact person. |
| `role`         | `Vocabulary`         | No       | Role of the main contact person.          |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the main contact person.          |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the main contact person.  |

##### PIDs

| Field                  | Type     | Required | Description                                                                      |
|------------------------|----------|----------|----------------------------------------------------------------------------------|
| `mainContactPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `mainContactPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the main contact.          |

##### Affiliations

| Field                   | Type                          | Required | Description                                                             |
|-------------------------|-------------------------------|----------|-------------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the main contact.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the main contact. |

##### AffiliationIdentifier

| Field             | Type     | Required | Description |
|-------------------|----------|----------|-------------|
| `mainContactID`   | `String` | Yes      |             |
| `mainContactType` | `String` | Yes      |             |

##### User

| Field     | Type     | Required | Description                                             |
|-----------|----------|----------|---------------------------------------------------------|
| `id`      | `String` | No       | Unique identifier for the organisation's administrator. |
| `name`    | `String` | Yes      | First name of the organisation's administrator.         |
| `surname` | `String` | Yes      | Last name of the organisation's administrator.          |
| `email`   | `String` | Yes      | Email of the organisation's administrator.              |

#### Example

```json
{
  "id": "organisation_001",
  "name": "Sample Organisation",
  "abbreviation": "ORG",
  "alternativePIDs": [
    {
      "pid": "10.1234/organisation",
      "pidSchema": "ROR"
    }
  ],
  "nodePID": null,
  "website": "https://example.com",
  "country": null,
  "legalEntity": true,
  "legalStatus": null,
  "hostingLegalEntity": null,
  "description": "This is a sample organisation description.",
  "logo": "https://example.com/logo.png",
  "multimedia": [
    {
      "multimediaURL": "https://example.com/media",
      "multimediaName": "Sample Multimedia"
    }
  ],
  "mainContact": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "role": null,
    "PIDs": [
      {
        "mainContactPID": "0000-0001-2345-6789",
        "mainContactPIDScheme": "ORCID"
      }
    ],
    "affiliations": [
      {
        "affiliationName": "Sample Organisation",
        "affiliationIdentifier": [
          {
            "mainContactID": "https://ror.org/example123",
            "mainContactType": "ROR"
          }
        ]
      }
    ]
  },
  "publicContacts": [
    "info@example.com",
    "contact@example.com"
  ],
  "users": [
    {
      "id": "user_001",
      "name": "User Name",
      "surname": "Surname",
      "email": "user@example.com"
    }
  ]
}
```

### Resource Interoperability Record

| Field                       | Type         | Required | Description                                                  |
|-----------------------------|--------------|----------|--------------------------------------------------------------|
| `id`                        | `String`     | auto-gen | Unique identifier for the resource interoperability record.  |
| `resourceId`                | `String`     | Yes      | Identifier of the resource associated with the record.       |
| `nodePID`                   | `Vocabulary` | No       | Resource Interoperability Record's original Node.            |
| `interoperabilityRecordIds` | `Vocabulary` | Yes      | List of interoperability record IDs related to the resource. |

### Example

```json
{
  "id": "resource_interop_001",
  "resourceId": "resource_001",
  "nodePID": "node-sandbox",
  "interoperabilityRecordIds": [
    "interop_001",
    "interop_002"
  ]
}
```

### Service

| Field               | Type                      | Required | Description                                                                                                    |
|---------------------|---------------------------|----------|----------------------------------------------------------------------------------------------------------------|
| `id`                | `String`                  | auto-gen | Unique identifier for the service.                                                                             |
| `name`              | `String`                  | Yes      | Name of the service.                                                                                           |
| `urls`              | `List<URL>`               | No       | URLs resolving to the resource.                                                                                |
| `alternativePIDs`   | `List<AlternativePIDs>`   | No       | Other persistent identifiers.                                                                                  |
| `nodePID`           | `Vocabulary`              | Yes      | Node the resource belongs to.                                                                                  |
| `description`       | `String`                  | Yes      | Detailed description of the service.                                                                           |
| `publishingDate`    | `Date`                    | Yes      | Date in which the resource was made available for discovery and access to others.                              |
| `type`              | `String`                  | Yes      | Type of the resource.                                                                                          |
| `resourceOwner`     | `Vocabulary`              | Yes      | The organisation that manages or delivers the Resource.                                                        |
| `serviceProviders`  | `Vocabulary`              | No       | The name(s) (or abbreviation(s)) of Organisation(s) that manage or deliver the Service in federated scenarios. |
| `webpage`           | `URL`                     | Yes      | Webpage with information about the Service usually hosted and maintained by the Organisation.                  |
| `logo`              | `URL`                     | No       | Link to the logo/visual identity of the Resource.                                                              |
| `scientificDomains` | `List<ScientificDomains>` | No       |                                                                                                                |
| `categories`        | `List<Categories>`        | No       |                                                                                                                |
| `accessTypes`       | `Vocabulary`              | Yes      | The way a user can access the resource (Remote, Physical, Virtual, etc.).                                      |
| `tags`              | `List<String>`            | No       | Keywords associated to the Resource to simplify search by relevant keywords.                                   |
| `jurisdiction`      | `Vocabulary`              | Yes      | The property defines the jurisdiction of the users of the resource, based on the vocabulary for this property. |
| `trl`               | `Vocabulary`              | Yes      | The Technology Readiness Level of the Resource.                                                                |
| `termsOfUse`        | `URL`                     | No       | Webpage describing the rules, Resource conditions and usage policy which one must agree to abide by.           |
| `privacyPolicy`     | `URL`                     | No       | Link to the privacy policy applicable to the Resource.                                                         |
| `accessPolicy`      | `URL`                     | No       | Information about the access policies that apply.                                                              |
| `orderType`         | `Vocabulary`              | Yes      | Information on the ordering process type.                                                                      |
| `order`             | `URL`                     | No       | Webpage through which an order for the Resource can be placed.                                                 |
| `mainContact`       | `MainContact`             | Yes      |                                                                                                                |
| `publicContacts`    | `List<String>`            | Yes      | List of public contact emails.                                                                                 |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### ScientificDomains

| Field                 | Type         | Required | Description                                                                                                |
|-----------------------|--------------|----------|------------------------------------------------------------------------------------------------------------|
| `scientificDomain`    | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of Resources.                            |
| `scientificSubdomain` | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of Resources, within the defined domain. |

##### Categories

| Field         | Type         | Required | Description                                                                                                |
|---------------|--------------|----------|------------------------------------------------------------------------------------------------------------|
| `category`    | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of Resources.                            |
| `subcategory` | `Vocabulary` | No       | A named group of Organisations that offer access to the same type of Resources, within the defined domain. |

##### MainContact

| Field          | Type                 | Required | Description                               |
|----------------|----------------------|----------|-------------------------------------------|
| `firstName`    | `String`             | Yes      | First name of the main contact person.    |
| `lastName`     | `String`             | Yes      | Last name of the main contact person.     |
| `email`        | `String`             | Yes      | Email address of the main contact person. |
| `role`         | `Vocabulary`         | No       | Role of the main contact person.          |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the main contact person.          |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the main contact person.  |

##### PIDs

| Field                  | Type     | Required | Description                                                                      |
|------------------------|----------|----------|----------------------------------------------------------------------------------|
| `mainContactPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `mainContactPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the main contact.          |

##### Affiliations

| Field                   | Type                          | Required | Description                                                             |
|-------------------------|-------------------------------|----------|-------------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the main contact.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the main contact. |

##### AffiliationIdentifier

| Field             | Type     | Required | Description |
|-------------------|----------|----------|-------------|
| `mainContactID`   | `String` | Yes      |             |
| `mainContactType` | `String` | Yes      |             |

### Example

```json
{
  "id": "service_001",
  "name": "Sample Service",
  "urls": [
    "https://example.com/service",
    "https://mirror.example.com/service"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/service",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": null,
  "description": "A sample service description.",
  "publishingDate": "2024-01-15T00:00:00Z",
  "type": "Service",
  "resourceOwner": null,
  "serviceProviders": null,
  "webpage": "https://example.com/service/info",
  "logo": "https://example.com/service/logo.png",
  "scientificDomains": [
    {
      "scientificDomain": null,
      "scientificSubdomain": null
    }
  ],
  "categories": [
    {
      "category": null,
      "subcategory": null
    }
  ],
  "accessTypes": null,
  "tags": [
    "innovation",
    "technology"
  ],
  "jurisdiction": null,
  "trl": null,
  "termsOfUse": "https://example.com/service/terms",
  "privacyPolicy": "https://example.com/service/privacy",
  "accessPolicy": "https://example.com/service/access-policy",
  "orderType": null,
  "order": "https://example.com/service/order",
  "mainContact": {
    "firstName": "Jane",
    "lastName": "Smith",
    "email": "jane.smith@example.com",
    "role": null,
    "PIDs": [
      {
        "mainContactPID": "0000-0001-2345-6789",
        "mainContactPIDScheme": "ORCID"
      }
    ],
    "affiliations": [
      {
        "affiliationName": "Sample Organisation",
        "affiliationIdentifier": [
          {
            "mainContactID": "https://ror.org/example123",
            "mainContactType": "ROR"
          }
        ]
      }
    ]
  },
  "publicContacts": [
    "support@example.com",
    "info@example.com"
  ]
}
```

### Training Resource

| Field                   | Type                      | Required | Description                                                                                                                  |
|-------------------------|---------------------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| `id`                    | `String`                  | auto-gen | Unique identifier for the training resource.                                                                                 |
| `name`                  | `String`                  | Yes      | Name of the resource.                                                                                                        |
| `urls`                  | `List<URL>`               | No       | URLs resolving to the resource.                                                                                              |
| `alternativePIDs`       | `List<AlternativePIDs>`   | No       | Other persistent identifiers.                                                                                                |
| `nodePID`               | `Vocabulary`              | Yes      | Node the resource belongs to.                                                                                                |
| `description`           | `String`                  | Yes      | Description of the resource.                                                                                                 |
| `publishingDate`        | `Date`                    | Yes      | Date in which the resource was made available for discovery and access to others.                                            |
| `type`                  | `String`                  | Yes      | Type of the resource.                                                                                                        |
| `resourceOwner`         | `Vocabulary`              | Yes      | The organisation that manages or delivers the Resource.                                                                      |
| `eoscRelatedServices`   | `Vocabulary`              | No       | The name(s) of (all) the Provider(s) that manage or deliver the Resource in federated scenarios.                             |
| `keywords`              | `List<String>`            | No       | The keyword(s) or tag(s) used to describe the resource.                                                                      |
| `license`               | `License`                 | No       | A license document that applies to this resource.                                                                            |
| `accessRights`          | `Vocabulary`              | Yes      | The access status of a resource (open, restricted, paid).                                                                    |
| `versionDate`           | `Date`                    | Yes      | The version date for the most recently published or broadcast resource.                                                      |
| `targetGroups`          | `Vocabulary`              | Yes      | The principal users(s) for which the learning resource was designed.                                                         |
| `learningResourceTypes` | `Vocabulary`              | No       | The predominant type or kind that characterizes the learning resource.                                                       |
| `learningOutcomes`      | `List<String>`            | Yes      | The descriptions of what knowledge, skills or abilities students should acquire on completion of the resource.               |
| `expertiseLevel`        | `Vocabulary`              | Yes      | Target skill level in the topic being taught.                                                                                |
| `contentResourceTypes`  | `Vocabulary`              | No       | The predominant content type of the learning resource (video, game, diagram, slides, etc.).                                  |
| `qualifications`        | `Vocabulary`              | No       | Identification of certification, accreditation or badge obtained with course or learning resource.                           |
| `duration`              | `String`                  | No       | Approximate or typical time it takes to work with or through the learning resource for the typical intended target audience. |
| `languages`             | `Vocabulary`              | Yes      | The languages in which the resource was originally published or made available.                                              |
| `scientificDomains`     | `List<ScientificDomains>` | No       |                                                                                                                              |
| `creators`              | `List<Creators>`          | Yes      | The main researchers involved in producing the data, or the authors of the publication, in priority order                    |
| `publicContacts`        | `List<String>`            | Yes      | List of public contact emails.                                                                                               |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       |             |
| `pidSchema` | `String` | No       |             |

##### License

| Field         | Type         | Required | Description                                                                  |
|---------------|--------------|----------|------------------------------------------------------------------------------|
| `licenseName` | `Vocabulary` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`        | No       | A license document that applies to this content, typically indicated by URL. |

##### ScientificDomains

| Field                 | Type         | Required | Description                                                                                            |
|-----------------------|--------------|----------|--------------------------------------------------------------------------------------------------------|
| `scientificDomain`    | `Vocabulary` | No       | A named group of Providers that offer access to the same type of Resources.                            |
| `scientificSubdomain` | `Vocabulary` | No       | A named group of Providers that offer access to the same type of Resources, within the defined domain. |

##### Creators

| Field          | Type                 | Required | Description                              |
|----------------|----------------------|----------|------------------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator.           |
| `lastName`     | `String`             | Yes      | Last name of the creator.                |
| `email`        | `String`             | Yes      | Email of the creator.                    |
| `role`         | `Vocabulary`         | No       |                                          |
| `PIDs`         | `List<PIDs>`         | No       | PIDs of the main contact person.         |
| `affiliations` | `List<Affiliations>` | No       | Affiliations of the main contact person. |

##### PIDs

| Field              | Type     | Required | Description                                                                      |
|--------------------|----------|----------|----------------------------------------------------------------------------------|
| `creatorPID`       | `String` | Yes      | Uniquely identifies an individual or legal entity, according to various schemes. |
| `creatorPIDScheme` | `String` | Yes      | Uniquely identifies the organizational affiliation of the creator.               |

##### Affiliations

| Field                   | Type                          | Required | Description                                                        |
|-------------------------|-------------------------------|----------|--------------------------------------------------------------------|
| `affiliationName`       | `String`                      | Yes      | The organizational or institutional affiliation of the creator.    |
| `affiliationIdentifier` | `List<AffiliationIdentifier>` | No       | Uniquely identifies the organizational affiliation of the creator. |

##### AffiliationIdentifier

| Field         | Type     | Required | Description |
|---------------|----------|----------|-------------|
| `creatorID`   | `String` | Yes      |             |
| `creatorType` | `String` | Yes      |             |

### Example

```json
{
  "id": "training_001",
  "name": "Introduction to Data Science",
  "urls": [
    "https://example.com/training-resource",
    "https://mirror.example.com/training-resource"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/training",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": null,
  "description": "An introductory course on data science concepts.",
  "publishingDate": "2024-01-15T00:00:00Z",
  "type": "Course",
  "resourceOwner": null,
  "eoscRelatedServices": null,
  "keywords": [
    "Data Science",
    "Machine Learning"
  ],
  "license": {
    "licenseName": null,
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  },
  "accessRights": null,
  "versionDate": "2024-09-10T00:00:00Z",
  "targetGroups": null,
  "learningResourceTypes": null,
  "learningOutcomes": [
    "Understand basics of data science",
    "Apply machine learning models"
  ],
  "expertiseLevel": null,
  "contentResourceTypes": null,
  "qualifications": null,
  "duration": "3 hours",
  "languages": null,
  "scientificDomains": [
    {
      "scientificDomain": null,
      "scientificSubdomain": null
    }
  ],
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": null,
      "PIDs": [
        {
          "creatorPID": "0000-0001-2345-6789",
          "creatorPIDScheme": "ORCID"
        }
      ],
      "affiliations": [
        {
          "affiliationName": "Data Science Institute",
          "affiliationIdentifier": [
            {
              "creatorID": "https://ror.org/example123",
              "creatorType": "ROR"
            }
          ]
        }
      ]
    }
  ],
  "publicContacts": [
    "support@example.com",
    "info@example.com"
  ]
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
- [ADAPTER_LICENSE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ADAPTER_LICENSE.json)
- [ADAPTER_PROGRAMMING_LANGUAGE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ADAPTER_PROGRAMMING_LANGUAGE.json)
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
- [NODE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/NODE.json)
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
Simply provide your data and use LinkML's built-in tools or Python libraries to run the validation process. Errors or
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

---

## External Services

In addition to its core functionality, this project also integrates with external services that extend its capabilities.
These services are optional but can provide added value depending on the use case:

1. **PID Service** – The Persistent Identifiers (PID) Service offers a robust, reliable solution for the long-term
   identification and management of digital objects underpinned by leading European data centers and cutting-edge
   technology. [Read the docs](https://docs.sandbox.eosc-beyond.eu/Service%20Portfolio/PID/PID/)
2. **Helpdesk Service** - The EOSC Helpdesk provides you with the information and support you need to troubleshoot your
   service problems. You can report incidents, bugs or change requests.
   [Read the docs](https://docs.sandbox.eosc-beyond.eu/Service%20Portfolio/Helpdesk/Helpdesk/)
3. **Accounting Service** – The EOSC Accounting for Services is a comprehensive platform designed to streamline the
   collection, aggregation, and exchange of metrics across various infrastructures, providers, and projects.
   [Read the docs](https://docs.sandbox.eosc-beyond.eu/Service%20Portfolio/Accounting/Accounting/)