<div align="center">
  <img src='https://eosc.eu/wp-content/uploads/2024/02/EOSC-Beyond-logo.png'>
</div>

# Resource Catalogue Documentation [v6.1.0]

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
    2. [Configuration Template Instance Controller](#configuration-template-instance-controller)
    3. [Datasource Controller](#datasource-controller)
    4. [Deployable Application Controller](#deployable-application-controller)
    5. [Interoperability Record Controller](#interoperability-record-controller)
    6. [Organisation Controller](#organisation-controller)
    7. [Public Controller](#public-controller)
    8. [Resource Interoperability Record Controller](#resource-interoperability-record-controller)
    9. [Service Controller](#service-controller)
    10. [Training Resource Controller](#training-resource-controller)
    11. [Vocabulary Controller](#vocabulary-controller)
4. [Model](#model)
    1. [Adapter](#adapter)
    2. [Configuration Template Instance](#configuration-template-instance)
    3. [Datasource](#datasource)
    4. [Deployable Application](#deployable-application)
    5. [Interoperability Record](#interoperability-record)
    6. [Organisation](#organisation)
    7. [Resource Interoperability Record](#resource-interoperability-record)
    8. [Service](#service)
    9. [Training Resource](#training-resource)
    10. [Vocabulary](#vocabulary)
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
        - Deletes the Datasource of the specific Catalogue given its id.
          ```diff
          /datasource/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
            catalogue_id: String (default 'eosc') [optional]
          ```
        - Deletes the Draft Datasource given its id.
          ```diff
          /datasource/draft/{prefix}/{suffix}
          Params:
            prefix: String [required]
            suffix: String [required]
          ```

    - GET
        - Returns the Datasource of the specific Catalogue given its id.
          ```diff
            /datasource/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
              catalogue_id: String (default 'eosc') [optional]
          ```
        - Returns a list of all inactive Datasources.
          ```diff
            /datasource/inactive/all
            Params:
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
              catalogue: String (default 'eosc') [optional]
          ```
        - Returns the Draft Datasource of the specific Catalogue given its id.
          ```diff
            /datasource/draft/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
          ```
        - Returns a list of Draft Datasources where user is admin.
          ```diff
          /datasource/draft/my
          ```
        - Returns a list of Draft Datasources under a specific Organisation.
          ```diff
            /datasource/draft/byOrganisation/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
          ```
        - Returns a list of Datasources under a specific Organisation.
          ```diff
            /datasource/byOrganisation/{prefix}/{suffix}
            Params:
              prefix: String [required]
              suffix: String [required]
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
          ```
        - Returns a list of Datasources of a specific Catalogue.
          ```diff
            /datasource/byCatalogue/{id}
            Params:
              id: String [required]
              query : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              orderField: String (Field to use for ordering) [optional]
          ```
        - Get all Datasources in the Catalogue organized by an attribute (eg. name)
          ```diff
            /datasource/by/{field}
            Params:
              field: Service field (required)
          ```
        - Returns a list of all Datasources of the specific Catalogue in the Portal.
          ```diff
            /datasource/all
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
        - Creates a new Datasource.
          ```diff
            /datasource
            Body:
              Service JSON [required]
        - Creates a new Draft Datasource.
          ```diff
            /datasource/draft
            Body:
              Service JSON [required]
        - Validates a Datasource without actually changing the repository.
          ```diff
          /datasource/validate
          Body:
            Service JSON [required]
    - PUT
        - Updates a specific Datasource.
          ```diff
          /datasource
          Params:
            comment: String
          Body:
            Service JSON [required]
          ```
        - Updates a specific Draft Datasource.
          ```diff
          /datasource/draft
          Body:
            Service JSON [required]
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
        - Get a list of all Public Datasources in the Portal.
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
        - Returns the Public Interoperability Record with the given id.
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
        - Get a list of all Public Interoperability Records in the Portal.
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
        - Get a list of all Public Organisations in the Portal.
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
        - Get a list of all Public Resource Interoperability Records in the Portal.
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
        - Returns the Public Service with the given id.
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
        - Get a list of all Public Services in the Portal.
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
        - Returns the Public Training Resource with the given id.
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
        - Get a list of all Public Training Resources in the Portal.
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
          /resourceInteroperabilityRecord/all
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
        - Deletes the Service given its id.
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
        - Returns the Service given its id.
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
        - Returns the Draft Service given its id.
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
        - Returns a list of all Services in the Portal.
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

- ### Training Resource Controller

  #### Operations for Training Resources

    - DELETE
        - Deletes the Training Resource given its id.
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
        - Returns the Training Resource given its id.
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
        - Returns the Draft Training Resource given its id.
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
        - Returns a list of all Training Resources in the Portal.
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
        - Get all Vocabularies:
          ```diff
          /vocabulary
          Params:
              keyword : String (Keyword to refine the search) [optional]
              from : String (Starting index in the result set, default 0) [optional]
              quantity: String (Quantity to be fetched, default 10) [optional]
              order: String (Order of results - asc/desc, default asc) [optional]
              sort: String (Field to use for ordering) [optional]
          ```
         - Get a specific Vocabulary:
          ```diff
          /vocabulary/{id}
          ```
        - Get all Vocabularies grouped by Type:
          ```diff
          /vocabulary/types/{type}
          Params:
              parent_id: String (The parent ID of the Vocabulary) [optional]
              sort: Object (Sort by a specific field, eg. name) [required]
                {
                  "sort": [
                    "string"
                  ]
                }
          ```
        - Get a specific Vocabulary of a specific Vocabulary Type:
          ```diff
          /vocabulary/types/{type}/{id}
          Params:
            type: Vocabulary Type [required]
            id: Vocabulary ID [required]
          ```
        - Get a list of EU Countries:
          ```diff
          /vocabulary/countries/EU
          ```
        - Get a list of WW Countries:
          ```diff
          /vocabulary/countries/WW
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
| `nodePID`             | `String`                | Yes      | Node the resource belongs to.                                                                              |
| `description`         | `String`                | Yes      | Description of the adapter.                                                                                |
| `publishingDate`      | `Date (ISO 8601)`       | Yes      | Date in which the resource was made available for discovery and access to others.                          |
| `type`                | `String`                | Yes      | Type of the resource.                                                                                      |
| `resourceOwner`       | `String`                | Yes      | The organisation that manages or delivers the Resource.                                                    |
| `linkedResource`      | `LinkedResource`        | Yes      | Service or Guideline linked with the Adapter.                                                              |
| `tagline`             | `String`                | Yes      | Short tagline summarizing the adapter.                                                                     |
| `logo`                | `URL`                   | No       | Link to the logo/visual identity of the adapter.                                                           |
| `documentation`       | `URL`                   | Yes      | Documentation webpage (e.g., read-the-docs page).                                                          |
| `repository`          | `URL`                   | Yes      | Code repository webpage (e.g., a GitHub repository).                                                       |
| `package`             | `List<URL>`             | Yes      | Links to the latest package release page(s) (e.g., PyPI project, Docker image, GitHub releases page).      |
| `programmingLanguage` | `String`                | Yes      | Programming language.                                                                                      |
| `license`             | `License`               | No       | A license document that applies to this resource.                                                          |
| `version`             | `String`                | Yes      | Software version.                                                                                          |
| `changeLog`           | `String`                | Yes      | Changes in the latest version.                                                                             |
| `lastUpdate`          | `Date (ISO 8601)`       | Yes      | Latest update date.                                                                                        |
| `creators`            | `List<Creators>`        | Yes      | The main researchers involved in producing the data, or the authors of the publication, in priority order. |
| `publicContacts`      | `List<String>`          | Yes      | List of public contact emails.                                                                             |
| `sqa`                 | `Sqa`                   | No       | Software Quality Assurance information.                                                                    |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       | PID.        |
| `pidSchema` | `String` | No       | PID Schema. |

##### LinkedResource

| Field           | Type     | Required | Description                                                               |
|-----------------|----------|----------|---------------------------------------------------------------------------|
| `resource_type` | `String` | Yes      | Type of the linked resource (e.g., `service`, `interoperability_record`). |
| `id`            | `String` | Yes      | ID of the linked resource.                                                |

##### License

| Field         | Type       | Required | Description                                                                  |
|---------------|------------|----------|------------------------------------------------------------------------------|
| `licenseName` | `String`   | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`      | No       | A license document that applies to this content, typically indicated by URL. |

##### Creators

| Field          | Type                 | Required | Description                    |
|----------------|----------------------|----------|--------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator. |
| `lastName`     | `String`             | Yes      | Last name of the creator.      |
| `email`        | `String`             | Yes      | Email of the creator.          |
| `role`         | `String`             | No       | Role.                          |
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

| Field         | Type     | Required | Description   |
|---------------|----------|----------|---------------|
| `creatorID`   | `String` | Yes      | Creator ID.   |
| `creatorType` | `String` | Yes      | Creator Type  |

##### SQA

| Field      | Type     | Required | Description                       |
|------------|----------|----------|-----------------------------------|
| `sqaURL`   | `URL`    | No       | Sqa assessment results.           |
| `sqaBadge` | `String` | No       | Sqa badge (bronze, silver, gold). |

#### Example

```json
{
  "id": "10.1234/adapter",
  "name": "Sample Adapter",
  "urls": [
    "https://example.com/adapter",
    "https://mirror.example.com/adapter"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/alternative_adapter_pid",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": "node-sandbox",
  "description": "This is a sample adapter description.",
  "publishingDate": "2026-01-01",
  "type": "Adapter",
  "resourceOwner": "10.1234/organisation",
  "linkedResource": {
    "resource_type": "service",
    "id": "10.1234/service"
  },
  "tagline": "Sample tagline",
  "logo": "https://example.com/logo.png",
  "documentation": "https://example.com/documentation",
  "repository": "https://example.com/repository",
  "package": [
    "https://example.com/package1",
    "https://example.com/package2"
  ],
  "programmingLanguage": "adapter_programming_language-python",
  "license": {
    "licenseName": "spdx_license-creative_commons",
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  },
  "version": "1.0.0",
  "changeLog": "Initial release.",
  "lastUpdate": "2026-01-01",
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": "credit-conceptualization",
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
    "sqaURL": "https://eosc-synergy/assessment-results",
    "sqaBadge": "sqa_badge-bronze"
  }
}
```

### Configuration Template Instance

| Field                     | Type                  | Required | Description                                                |
|---------------------------|-----------------------|----------|------------------------------------------------------------|
| `id`                      | `String`              | auto-gen | Unique identifier for the configuration template instance. |
| `resourceId`              | `String`              | Yes      | Identifier of the resource associated with the instance.   |
| `configurationTemplateId` | `String`              | Yes      | Identifier of the configuration template used.             |
| `nodePID`                 | `String`              | Yes      | Configuration Template Instance's original Node.           |
| `description`             | `String`              | No       | Description.                                               |
| `payload`                 | `Map<String, Object>` | Yes      | The configuration data or settings in JSON format.         |

### Example

```json
{
  "id": "10.1234/cti",
  "resourceId": "10.1234/service",
  "configurationTemplateId": "10.1234/con",
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
| `nodePID`                   | `String`                         | Yes      | Node the resource belongs to.                                                                                                         |
| `description`               | `String`                         | Yes      | Description of the datasource.                                                                                                        |
| `publishingDate`            | `Date (ISO 8601)`                | Yes      | Date in which the resource was made available for discovery and access to others.                                                     |
| `type`                      | `String`                         | Yes      | Type of the resource.                                                                                                                 |
| `resourceOwner`             | `String`                         | Yes      | The organisation that manages or delivers the datasource.                                                                             |
| `serviceProviders`          | `List<String>`                   | No       | The name(s) (or abbreviation(s)) of Organisation(s) that manage or deliver the Service in federated scenarios.                        |
| `webpage`                   | `URL`                            | Yes      | Webpage with information about the Service usually hosted and maintained by the Organisation.                                         |
| `logo`                      | `URL`                            | No       | Link to the logo/visual identity of the datasource.                                                                                   |
| `jurisdiction`              | `String`                         | Yes      | The property defines the jurisdiction of the users of the data source, based on the vocabulary for this property.                     |
| `scientificDomains`         | `List<ScientificDomains>`        | No       | Scientific Domains and Subdomains.                                                                                                    |
| `categories`                | `List<Categories>`               | No       | Categories and Subcategories.                                                                                                         |
| `accessTypes`               | `String`                         | Yes      | The way a user can access the datasource (Remote, Physical, Virtual, etc.).                                                           |
| `tags`                      | `List<String>`                   | No       | Keywords associated to the datasource to simplify search by relevant keywords.                                                        |
| `trl`                       | `String`                         | Yes      | The Technology Readiness Level of the datasource (to be further updated in the context of the EOSC).                                  |
| `termsOfUse`                | `URL`                            | No       | Webpage describing the rules, datasource conditions and usage policy which one must agree to abide by in order to use the datasource. |
| `privacyPolicy`             | `URL`                            | No       | Link to the privacy policy applicable to the datasource.                                                                              |
| `accessPolicy`              | `URL`                            | No       | Information about the access policies that apply.                                                                                     |
| `orderType`                 | `String`                         | Yes      | Information on the ordering process type.                                                                                             |
| `order`                     | `URL`                            | No       | Webpage through which an order for the Resource can be placed.                                                                        |
| `mainContact`               | `MainContact`                    | Yes      | Main Contact of the Datasource.                                                                                                       |
| `publicContacts`            | `List<String>`                   | Yes      | List of public contact emails.                                                                                                        |
| `submissionPolicyURL`       | `URL`                            | No       | URL of the submission policy.                                                                                                         |
| `preservationPolicyURL`     | `URL`                            | No       | URL of the preservation policy.                                                                                                       |
| `versionControl`            | `Boolean`                        | No       | Indicates if version control is used.                                                                                                 |
| `persistentIdentitySystems` | `List<PersistentIdentitySystem>` | No       | List of persistent identity systems associated with the datasource.                                                                   |
| `datasourceClassification`  | `String`                         | Yes      | The specific type of the data source based on the vocabulary defined for this property.                                               |
| `researchProductTypes`      | `String`                         | Yes      | The types of OpenAIRE products managed by the data source, based on the vocabulary for this property.                                 |
| `thematic`                  | `Boolean`                        | Yes      | Boolean value specifying if the data source is dedicated to a given discipline or is instead discipline agnostic.                     |
| `metadataLicense`           | `MetadataLicense`                | No       | Metadata License.                                                                                                                     |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       | PID.        |
| `pidSchema` | `String` | No       | PID Schema. |

##### ScientificDomains

| Field                 | Type       | Required | Description                                                                           |
|-----------------------|------------|----------|---------------------------------------------------------------------------------------|
| `scientificDomain`    | `String`   | No       | The branch of science, scientific discipline that is related to the resource.         |
| `scientificSubdomain` | `String`   | No       | The sub-branch of science, scientific sub-discipline that is related to the resource. |

##### Categories

| Field         | Type       | Required | Description                                                                                                                      |
|---------------|------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| `category`    | `String`   | No       | A named group of Resources that offer access to the same type of Resources.                                                      |
| `subcategory` | `String`   | No       | A named group of Resources that offer access to the same type of Resource or capabilities, within the defined Resource Category. |

##### MainContact

| Field          | Type                 | Required | Description                               |
|----------------|----------------------|----------|-------------------------------------------|
| `firstName`    | `String`             | Yes      | First name of the main contact person.    |
| `lastName`     | `String`             | Yes      | Last name of the main contact person.     |
| `email`        | `String`             | Yes      | Email address of the main contact person. |
| `role`         | `String`             | No       | Role of the main contact person.          |
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

| Field             | Type     | Required | Description        |
|-------------------|----------|----------|--------------------|
| `mainContactID`   | `String` | Yes      | Main Contact ID.   |
| `mainContactType` | `String` | Yes      | Main Contact Type. |

##### PersistentIdentitySystem

| Field                                  | Type       | Required | Description                                                                      |
|----------------------------------------|------------|----------|----------------------------------------------------------------------------------|
| `persistentIdentityProductType`        | `String`   | No       | Specify the ProductType to which the persistent identifier is referring to.      |
| `persistentIdentityProductTypeSchemes` | `String`   | No       | Specify the list of persistent identifier schemes used to refer to ProductTypes. |

##### MetadataLicense

| Field                 | Type     | Required | Description                       |
|-----------------------|----------|----------|-----------------------------------|
| `metadataLicenseName` | `String` | No       | The name of the metadata License. |
| `metadataLicenseURL`  | `URL`    | No       | The url of the metadata License.  |

### Example

```json
{
  "id": "10.1234/datasource",
  "name": "European Research Data Repository",
  "urls": [
    "https://example.com/datasource",
    "https://mirror.example.com/datasource"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/datasource_alternative_pid",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": "node-sandbox",
  "description": "A comprehensive repository for European research data across multiple scientific domains.",
  "publishingDate": "2026-01-01",
  "type": "Repository",
  "resourceOwner": "10.1234/organisation",
  "serviceProviders": [
    "10.1234/organisation1",
    "10.1234/organisation2"
  ],
  "webpage": "https://example.com/datasource/info",
  "logo": "https://example.com/datasource/logo.png",
  "jurisdiction": "ds_jurisdiction-global",
  "scientificDomains": [
    {
      "scientificDomain": "scientific_domain-agricultural_sciences",
      "scientificSubdomain": "scientific_subdomain-agricultural_sciences-agricultural_biotechnology"
    }
  ],
  "categories": [
    {
      "category": "category-access_physical_and_eInfrastructures-compute",
      "subcategory": "subcategory-access_physical_and_eInfrastructures-compute-container_management"
    }
  ],
  "accessType": "access_type-mail_in",
  "tags": [
    "open data",
    "research",
    "EOSC"
  ],
  "trl": "trl-1",
  "termsOfUse": "https://example.com/datasource/terms",
  "privacyPolicy": "https://example.com/datasource/privacy",
  "accessPolicy": "https://example.com/datasource/access-policy",
  "orderType": "order_type-open_access",
  "order": "https://example.com/datasource/order",
  "mainContact": {
    "firstName": "Jane",
    "lastName": "Smith",
    "email": "jane.smith@example.com",
    "role": "credit-conceptualization",
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
      "persistentIdentityProductType": "ds_research_entity_type-research_data",
      "persistentIdentityProductTypeSchemes": "ds_persistent_identity_scheme-doi"
    }
  ],
  "datasourceClassification": "ds_classification-repository",
  "researchProductTypes": "ds_research_entity_type-research_data",
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
| `nodePID`           | `String`                  | Yes      | Node the resource belongs to.                                                                              |
| `description`       | `String`                  | Yes      | Description of the deployable application.                                                                 |
| `publishingDate`    | `Date`                    | Yes      | Date in which the resource was made available for discovery and access to others.                          |
| `type`              | `String`                  | Yes      | Type of the resource.                                                                                      |
| `resourceOwner`     | `String`                  | Yes      | The organisation that manages or delivers the Resource.                                                    |
| `acronym`           | `String`                  | Yes      | Acronym of the deployable application.                                                                     |
| `tagline`           | `String`                  | No       | Short tagline summarizing the deployable application.                                                      |
| `logo`              | `URL`                     | No       | Link to the logo/visual identity of the deployable application.                                            |
| `scientificDomains` | `List<ScientificDomains>` | No       |                                                                                                            |
| `tags`              | `List<String>`            | No       | Keywords associated with the deployable application.                                                       |
| `creators`          | `List<Creators>`          | Yes      | The main researchers involved in producing the data, or the authors of the publication, in priority order. |
| `publicContacts`    | `List<String>`            | Yes      | List of public contact emails.                                                                             |
| `version`           | `String`                  | Yes      | Version of the deployable application.                                                                     |
| `lastUpdate`        | `Date (ISO 8601)`         | No       | Date of the latest update.                                                                                 |
| `license`           | `License`                 | No       | A license document that applies to this resource.                                                          |

#### Nested Objects

##### AlternativePIDs

| Field       | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `pid`       | `String` | No       | PID.        |
| `pidSchema` | `String` | No       | PID Schema. |

##### ScientificDomains

| Field                 | Type     | Required | Description                                                                       |
|-----------------------|----------|----------|-----------------------------------------------------------------------------------|
| `scientificDomain`    | `String` | No       | The branch of science, scientific discipline that is related to the resource.     |
| `scientificSubdomain` | `String` | No       | The sub-branch of science, scientific discipline that is related to the resource. |

##### Creators

| Field          | Type                 | Required | Description                    |
|----------------|----------------------|----------|--------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator. |
| `lastName`     | `String`             | Yes      | Last name of the creator.      |
| `email`        | `String`             | Yes      | Email of the creator.          |
| `role`         | `String`             | No       | Role.                          |
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

| Field         | Type     | Required | Description   |
|---------------|----------|----------|---------------|
| `creatorID`   | `String` | Yes      | Creator ID.   |
| `creatorType` | `String` | Yes      | Creator Type. |

##### License

| Field         | Type     | Required | Description                                                                  |
|---------------|----------|----------|------------------------------------------------------------------------------|
| `licenseName` | `String` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`    | No       | A license document that applies to this content, typically indicated by URL. |

#### Example

```json
{
  "id": "10.1234/deployable",
  "name": "Sample Deployable Application",
  "urls": [
    "https://example.com/deployable",
    "https://mirror.example.com/deployable"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/deployable_alternative_pid",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": "node-sandbox",
  "description": "A sample deployable application description.",
  "publishingDate": "2026-01-01",
  "type": "DeployableApplication",
  "resourceOwner": "10.1234/organisation",
  "acronym": "SDA",
  "tagline": "Sample tagline",
  "logo": "https://example.com/logo.png",
  "scientificDomains": [
    {
      "scientificDomain": "scientific_domain-agricultural_sciences",
      "scientificSubdomain": "scientific_subdomain-agricultural_sciences-agricultural_biotechnology"
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
      "role": "credit-conceptualization",
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
  "lastUpdate": "2026-01-01",
  "license": {
    "licenseName": "spdx_license-creative_commons",
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  }
}
```

### Interoperability Record

| Field              | Type                    | Required | Description                                                                                                |
|--------------------|-------------------------|----------|------------------------------------------------------------------------------------------------------------|
| `id`               | `String`                | auto-gen | Unique identifier for the interoperability record.                                                         |
| `name`             | `String`                | Yes      | Name of the resource.                                                                                      |
| `urls`             | `List<URL>`             | No       | URLs resolving to the resource.                                                                            |
| `alternativePIDs`  | `List<AlternativePIDs>` | No       | Other persistent identifiers.                                                                              |
| `nodePID`          | `String`                | Yes      | Node the resource belongs to.                                                                              |
| `description`      | `String`                | Yes      | Description of the interoperability record.                                                                |
| `publishingDate`   | `Date`                  | Yes      | Date in which the resource was made available for discovery and access to others.                          |
| `type`             | `String`                | Yes      | Type of the resource.                                                                                      |
| `resourceOwner`    | `String`                | Yes      | The organisation that manages or delivers the Resource.                                                    |
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

| Field         | Type     | Required | Description                                                                  |
|---------------|----------|----------|------------------------------------------------------------------------------|
| `licenseName` | `String` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`    | No       | A license document that applies to this content, typically indicated by URL. |

##### Creators

| Field          | Type                 | Required | Description                    |
|----------------|----------------------|----------|--------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator. |
| `lastName`     | `String`             | Yes      | Last name of the creator.      |
| `email`        | `String`             | Yes      | Email of the creator.          |
| `role`         | `String`             | No       |                                |
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
  "id": "10.1234/guideline",
  "name": "Sample Interoperability Record",
  "urls": [
    "https://example.com/guideline",
    "https://mirror.example.com/guideline"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/guideline_alternative_pid",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": "node-sandbox",
  "description": "A sample interoperability record description.",
  "publishingDate": "2026-01-01",
  "type": "InteroperabilityGuidelines",
  "resourceOwner": "10.1234/organisation",
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
    "licenseName": "spdx_license-creative_commons",
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  },
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": "credit-conceptualization",
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

### Organisation

| Field                | Type                    | Required | Description                                                                                                                                             |
|----------------------|-------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                 | `String`                | auto-gen | Unique identifier for the organisation.                                                                                                                 |
| `name`               | `String`                | Yes      | Full name of the organisation.                                                                                                                          |
| `abbreviation`       | `String`                | Yes      | Abbreviation of the organisation's name.                                                                                                                |
| `alternativePIDs`    | `List<AlternativePIDs>` | No       | Other persistent identifiers.                                                                                                                           |
| `nodePID`            | `String`                | Yes      | Node the organisation is contributing to.                                                                                                               |
| `website`            | `URL`                   | Yes      | URL of the organisation's website.                                                                                                                      |
| `country`            | `String`                | Yes      | Country of incorporation or physical location of the organisation or its coordinating centre in the case of distributed, virtual, and mobile providers. |
| `legalEntity`        | `Boolean`               | Yes      | Indicates if the organisation is a legal entity.                                                                                                        |
| `legalStatus`        | `String`                | No       | Legal status of the organisation.                                                                                                                       |
| `hostingLegalEntity` | `String`                | No       | Hosting legal entity responsible for the organisation.                                                                                                  |
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
| `role`         | `String`             | No       | Role of the main contact person.          |
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
  "id": "10.1234/organisation",
  "name": "Sample Organisation",
  "abbreviation": "ORG",
  "alternativePIDs": [
    {
      "pid": "10.1234/organisation_alternative_pid",
      "pidSchema": "ROR"
    }
  ],
  "nodePID": "node-sandbox",
  "website": "https://example.com",
  "country": "IT",
  "legalEntity": true,
  "legalStatus": "provider_legal_status-association",
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
    "role": "credit-conceptualization",
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

| Field                       | Type     | Required | Description                                                  |
|-----------------------------|----------|----------|--------------------------------------------------------------|
| `id`                        | `String` | auto-gen | Unique identifier for the resource interoperability record.  |
| `resourceId`                | `String` | Yes      | Identifier of the resource associated with the record.       |
| `nodePID`                   | `String` | No       | Resource Interoperability Record's original Node.            |
| `interoperabilityRecordIds` | `String` | Yes      | List of interoperability record IDs related to the resource. |

### Example

```json
{
  "id": "rir/resource_interoperability_record",
  "resourceId": "10.1234/service",
  "nodePID": "node-sandbox",
  "interoperabilityRecordIds": [
    "10.1234/guideline1",
    "10.1234/guideline2"
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
| `nodePID`           | `String`                  | Yes      | Node the resource belongs to.                                                                                  |
| `description`       | `String`                  | Yes      | Detailed description of the service.                                                                           |
| `publishingDate`    | `Date`                    | Yes      | Date in which the resource was made available for discovery and access to others.                              |
| `type`              | `String`                  | Yes      | Type of the resource.                                                                                          |
| `resourceOwner`     | `String`                  | Yes      | The organisation that manages or delivers the Resource.                                                        |
| `serviceProviders`  | `String`                  | No       | The name(s) (or abbreviation(s)) of Organisation(s) that manage or deliver the Service in federated scenarios. |
| `webpage`           | `URL`                     | Yes      | Webpage with information about the Service usually hosted and maintained by the Organisation.                  |
| `logo`              | `URL`                     | No       | Link to the logo/visual identity of the Resource.                                                              |
| `scientificDomains` | `List<ScientificDomains>` | No       |                                                                                                                |
| `categories`        | `List<Categories>`        | No       |                                                                                                                |
| `accessTypes`       | `String`                  | Yes      | The way a user can access the resource (Remote, Physical, Virtual, etc.).                                      |
| `tags`              | `List<String>`            | No       | Keywords associated to the Resource to simplify search by relevant keywords.                                   |
| `jurisdiction`      | `String`                  | Yes      | The property defines the jurisdiction of the users of the resource, based on the vocabulary for this property. |
| `trl`               | `String`                  | Yes      | The Technology Readiness Level of the Resource.                                                                |
| `termsOfUse`        | `URL`                     | No       | Webpage describing the rules, Resource conditions and usage policy which one must agree to abide by.           |
| `privacyPolicy`     | `URL`                     | No       | Link to the privacy policy applicable to the Resource.                                                         |
| `accessPolicy`      | `URL`                     | No       | Information about the access policies that apply.                                                              |
| `orderType`         | `String`                  | Yes      | Information on the ordering process type.                                                                      |
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

| Field                 | Type     | Required | Description                                                                                                |
|-----------------------|----------|----------|------------------------------------------------------------------------------------------------------------|
| `scientificDomain`    | `String` | No       | A named group of Organisations that offer access to the same type of Resources.                            |
| `scientificSubdomain` | `String` | No       | A named group of Organisations that offer access to the same type of Resources, within the defined domain. |

##### Categories

| Field         | Type     | Required | Description                                                                                                |
|---------------|----------|----------|------------------------------------------------------------------------------------------------------------|
| `category`    | `String` | No       | A named group of Organisations that offer access to the same type of Resources.                            |
| `subcategory` | `String` | No       | A named group of Organisations that offer access to the same type of Resources, within the defined domain. |

##### MainContact

| Field          | Type                 | Required | Description                               |
|----------------|----------------------|----------|-------------------------------------------|
| `firstName`    | `String`             | Yes      | First name of the main contact person.    |
| `lastName`     | `String`             | Yes      | Last name of the main contact person.     |
| `email`        | `String`             | Yes      | Email address of the main contact person. |
| `role`         | `String`             | No       | Role of the main contact person.          |
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
  "id": "10.1234/service",
  "name": "Sample Service",
  "urls": [
    "https://example.com/service",
    "https://mirror.example.com/service"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/service_alternative_pid",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": "node-sandbox",
  "description": "A sample service description.",
  "publishingDate": "2026-01-01",
  "type": "Service",
  "resourceOwner": "10.1234/organisation",
  "serviceProviders": [
    "10.1234/organisation2",
    "10.1234/organisation3"
  ],
  "webpage": "https://example.com/service/info",
  "logo": "https://example.com/service/logo.png",
  "scientificDomains": [
    {
      "scientificDomain": "scientific_domain-agricultural_sciences",
      "scientificSubdomain": "scientific_subdomain-agricultural_sciences-agricultural_biotechnology"
    }
  ],
  "categories": [
    {
      "category": "category-access_physical_and_eInfrastructures-compute",
      "subcategory": "subcategory-access_physical_and_eInfrastructures-compute-container_management"
    }
  ],
  "accessTypes": "access_type-mail_in",
  "tags": [
    "innovation",
    "technology"
  ],
  "jurisdiction": "ds_jurisdiction-global",
  "trl": "trl-9",
  "termsOfUse": "https://example.com/service/terms",
  "privacyPolicy": "https://example.com/service/privacy",
  "accessPolicy": "https://example.com/service/access-policy",
  "orderType": "order_type-open_access",
  "order": "https://example.com/service/order",
  "mainContact": {
    "firstName": "Jane",
    "lastName": "Smith",
    "email": "jane.smith@example.com",
    "role": "credit-conceptualization",
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
| `nodePID`               | `String`                  | Yes      | Node the resource belongs to.                                                                                                |
| `description`           | `String`                  | Yes      | Description of the resource.                                                                                                 |
| `publishingDate`        | `Date`                    | Yes      | Date in which the resource was made available for discovery and access to others.                                            |
| `type`                  | `String`                  | Yes      | Type of the resource.                                                                                                        |
| `resourceOwner`         | `String`                  | Yes      | The organisation that manages or delivers the Resource.                                                                      |
| `eoscRelatedServices`   | `String`                  | No       | The name(s) of (all) the Provider(s) that manage or deliver the Resource in federated scenarios.                             |
| `keywords`              | `List<String>`            | No       | The keyword(s) or tag(s) used to describe the resource.                                                                      |
| `license`               | `License`                 | No       | A license document that applies to this resource.                                                                            |
| `accessRights`          | `String`                  | Yes      | The access status of a resource (open, restricted, paid).                                                                    |
| `versionDate`           | `Date`                    | Yes      | The version date for the most recently published or broadcast resource.                                                      |
| `targetGroups`          | `List<String>`            | Yes      | The principal users(s) for which the learning resource was designed.                                                         |
| `learningResourceTypes` | `String`                  | No       | The predominant type or kind that characterizes the learning resource.                                                       |
| `learningOutcomes`      | `List<String>`            | Yes      | The descriptions of what knowledge, skills or abilities students should acquire on completion of the resource.               |
| `expertiseLevel`        | `String`                  | Yes      | Target skill level in the topic being taught.                                                                                |
| `contentResourceTypes`  | `String`                  | No       | The predominant content type of the learning resource (video, game, diagram, slides, etc.).                                  |
| `qualifications`        | `String`                  | No       | Identification of certification, accreditation or badge obtained with course or learning resource.                           |
| `duration`              | `String`                  | No       | Approximate or typical time it takes to work with or through the learning resource for the typical intended target audience. |
| `languages`             | `String`                  | Yes      | The languages in which the resource was originally published or made available.                                              |
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

| Field         | Type     | Required | Description                                                                  |
|---------------|----------|----------|------------------------------------------------------------------------------|
| `licenseName` | `String` | No       | SPDX License.                                                                |
| `licenseURL`  | `URL`    | No       | A license document that applies to this content, typically indicated by URL. |

##### ScientificDomains

| Field                 | Type     | Required | Description                                                                                            |
|-----------------------|----------|----------|--------------------------------------------------------------------------------------------------------|
| `scientificDomain`    | `String` | No       | A named group of Providers that offer access to the same type of Resources.                            |
| `scientificSubdomain` | `String` | No       | A named group of Providers that offer access to the same type of Resources, within the defined domain. |

##### Creators

| Field          | Type                 | Required | Description                              |
|----------------|----------------------|----------|------------------------------------------|
| `firstName`    | `String`             | Yes      | The first name of the creator.           |
| `lastName`     | `String`             | Yes      | Last name of the creator.                |
| `email`        | `String`             | Yes      | Email of the creator.                    |
| `role`         | `String`             | No       |                                          |
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
  "id": "10.1234/training",
  "name": "Introduction to Data Science",
  "urls": [
    "https://example.com/training-resource",
    "https://mirror.example.com/training-resource"
  ],
  "alternativePIDs": [
    {
      "pid": "10.1234/training_alternative_pid",
      "pidSchema": "DOI"
    }
  ],
  "nodePID": "node-sandbox",
  "description": "An introductory course on data science concepts.",
  "publishingDate": "2026-01-01",
  "type": "Course",
  "resourceOwner": "10.1234/organisation",
  "eoscRelatedServices": [
    "10.1234/service1",
    "10.1234/service2"
  ],
  "keywords": [
    "Data Science",
    "Machine Learning"
  ],
  "license": {
    "licenseName": "spdx_license-creative_commons",
    "licenseURL": "https://creativecommons.org/licenses/by/4.0/"
  },
  "accessRights": "tr_access_right-open_access",
  "versionDate": "2026-01-01",
  "targetGroups": [
    "target_user-businesses",
    "target_user-funders"
  ],
  "learningResourceTypes": "tr_dcmi_type-activity_plan",
  "learningOutcomes": [
    "Understand basics of data science",
    "Apply machine learning models"
  ],
  "expertiseLevel": "tr_expertise_level-advanced",
  "contentResourceTypes": "tr_content_resource_type-animation",
  "qualifications": "tr_qualification-badge",
  "duration": "2 years",
  "languages": [
    "aa",
    "en"
  ],
  "scientificDomains": [
    {
      "scientificDomain": "scientific_domain-agricultural_sciences",
      "scientificSubdomain": "scientific_subdomain-agricultural_sciences-agricultural_biotechnology"
    }
  ],
  "creators": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "role": "credit-conceptualization",
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

- [ACCESS_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ACCESS_TYPE.json)
- [ADAPTER_PROGRAMMING_LANGUAGE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ADAPTER_PROGRAMMING_LANGUAGE.json)
- [CATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CATEGORY.json)
- [COUNTRY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/COUNTRY.json)
- [CREDIT](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CREDIT.json)
- [CT_COMPATIBILITY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CT_COMPATIBILITY.json)
- [CT_PROTOCOL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CT_PROTOCOL.json)
- [DS_CLASSIFICATION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_CLASSIFICATION.json)
- [DS_JURISDICTION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_JURISDICTION.json)
- [DS_PERSISTENT_IDENTITY_SCHEME](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_PERSISTENT_IDENTITY_SCHEME.json)
- [DS_RESEARCH_ENTITY_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/DS_RESEARCH_ENTITY_TYPE.json)
- [LANGUAGE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/LANGUAGE.json)
- [NODE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/NODE.json)
- [ORDER_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ORDER_TYPE.json)
- [PROVIDER_HOSTING_LEGAL_ENTITY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_HOSTING_LEGAL_ENTITY.json)
- [PROVIDER_LEGAL_STATUS](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/PROVIDER_LEGAL_STATUS.json)
- [REGION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/REGION.json)
- [RESOURCE_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/RESOURCE_STATE.json)
- [SCIENTIFIC_DOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SCIENTIFIC_DOMAIN.json)
- [SCIENTIFIC_SUBDOMAIN](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SCIENTIFIC_SUBDOMAIN.json)
- [SPDX_LICENSE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SPDX_LICENSE.json)
- [SQA_BADGE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SQA_BADGE.json)
- [SUBCATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/SUBCATEGORY.json)
- [TARGET_USER](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TARGET_USER.json)
- [TEMPLATE_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TEMPLATE_STATE.json)
- [TRL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TRL.json)
- [TR_ACCESS_RIGHT](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_ACCESS_RIGHT.json)
- [TR_CONTENT_RESOURCE_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_CONTENT_RESOURCE_TYPE.json)
- [TR_DCMI_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_DCMI_TYPE.json)
- [TR_EXPERTISE_LEVEL](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_EXPERTISE_LEVEL.json)
- [TR_QUALIFICATION](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/TR_QUALIFICATION.json)

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