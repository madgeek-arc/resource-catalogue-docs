<div align="center">
  <img src='https://eosc-portal.eu/sites/all/themes/theme1/logo.png'></img>
</div>

# Resource Catalogue Documentation [v4 - EOSC Future]

- [Vocabularies](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/vocabularies)
- [Migration Scripts](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/scripts)

## Swagger UI Instances:

- [Production](https://providers.eosc-portal.eu/openapi)
- [Sandbox](https://beta.providers.eosc-portal.eu/openapi)
- [Beta](https://sandbox.providers.eosc-portal.eu/openapi)

## API:

- https://providers.eosc-portal.eu/api, https://api.eosc-portal.eu/
- https://sandbox.providers.eosc-portal.eu/api/
- https://beta.providers.eosc-portal.eu/api/

## Controllers:

  #### Obtain and Use API Token
  You can obtain an API token for the secured methods [here](https://aai.eosc-portal.eu/providers-api/). The obtained token can be used in a bearer authorization header like this: 'Authorization: Bearer [token]'

- ### Catalogue
  #### CRUD operations for Catalogues + external (non EOSC) resources (Datasources, Providers, Services)
  - DELETE
    - Deletes the Datasource of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/datasource/{id}
      Params:
        catalogueId: String (required)
        id : String (required)
      ```
    - Deletes the Provider of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/provider/{id}
      Params:
        catalogueId: String (required)
        id : String (required)
      ```
    - Deletes the Service of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/resource/{id}
      Params:
        catalogueId: String (required)
        id : String (required)
      ```
    - Deletes the Training Resource of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/trainingResource/{id}
      Params:
        catalogueId: String (required)
        id : String (required)
      ```
  - GET
    - Get a list of all Catalogues in the Portal:
      ```diff
      /catalogue/all
      Params:
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Datasource of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/datasource/{resourceId}
      Params:
        catalogueId: String (required)
        resourceId : String (required)
      ```
    - Get a list of all Providers of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/provider/all
      Params:
        catalogueId: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Provider of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/provider/{providerId}
      Params:
        catalogueId: String (required)
        providerId : String (required)
      ```
    - Returns the Service of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/resource/{resourceId}
      Params:
        catalogueId: String (required)
        resourceId : String (required)
      ```
    - Returns the Training Resource of the specific Catalogue given its ID:
      ```diff
      /catalogue/{catalogueId}/trainingResource/{trainingResourceId}
      Params:
        catalogueId: String (required)
        trainingResourceId : String (required)
      ```
    - Get a list of all Datasources of the specific Provider of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/{providerId}/datasource/all
      Params:
        catalogueId: String (required)
        providerId : String (required)
      ```
    - Get a list of all Service of the specific Provider of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/{providerId}/resource/all
      Params:
        catalogueId: String (required)
        providerId : String (required)
      ```
    - Get a list of all Training Resources of the specific Provider of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/{providerId}/trainingResource/all
      Params:
        catalogueId: String (required)
        providerId : String (required)
      ```
    - Get a specific Catalogue given its ID:
      ```diff
      /catalogue/{id}
      Params:
        id: String (required)
      ```
  - POST
    - Creates a new Datasource for the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/datasource
      Body:
        Datasource JSON (required)
      Params:
        catalogueId: String (required)
      ```
    - Creates a new Provider for the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/provider
      Body:
        Provider JSON (required)
      Params:
        catalogueId: String (required)
      ```
    - Creates a new Service for the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/resource
      Body:
        Service JSON (required)
      Params:
        catalogueId: String (required)
      ```
    - Creates a new Training Resource for the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/trainingResource
      Body:
        Training Resource JSON (required)
      Params:
        catalogueId: String (required)
      ```
  - PUT
    - Updates a specific Catalogue:
      ```diff
      /catalogue
      Body:
        Catalogue JSON (required)
      Params:
        comment: String
      ```
    - Updates the Datasource of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/datasource
      Body:
        Datasource JSON (required)
      Params:
        catalogueId: String (required)
        comment: String
      ```
    - Updates the Provider of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/provider
      Body:
        Provider JSON (required)
      Params:
        catalogueId: String (required)
        comment: String
      ```
    - Updates the Service of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/resource
      Body:
        Service JSON (required)
      Params:
        catalogueId: String (required)
        comment: String
      ```
    - Updates the Training Resource of the specific Catalogue:
      ```diff
      /catalogue/{catalogueId}/trainingResource
      Body:
        Training Resource JSON (required)
      Params:
        catalogueId: String (required)
        comment: String
      ```

- ### Datasource
  #### CRUD operations for Datasources
  - DELETE
    - Deletes the Datasource of the specific Catalogue given its ID:
      ```diff
      /datasource/{id}
      Params:
        id: String (required)
        catalogueId: String (required)
      ```
  - GET
    - Get a list of all Datasources of the specific Catalogue in the Portal:
      ```diff
      /datasource/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Datasource of the specific Catalogue given its ID:
      ```diff
      /datasource/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
  - POST
    - Creates a new EOSC Datasource:
      ```diff
      /datasource
      Body:
        Datasource JSON (required)
      ```
     - Validates a Datasource:
        ```diff
        /datasource/validate
        Body:
          Datasource JSON (required)
        ```
  - PUT
    - Updates a specific EOSC Datasource:
      ```diff
      /datasource
      Body:
        Datasource JSON (required)
      Params:
        comment: String
      ```
        
- ### Interoperability Record:
  #### Get information about Interoperability Records
  - GET
    - Get a list of all Interoperability Records in the Portal:
      ```diff
      /interoperabilityRecord/all
      Params:
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Interoperability Record given its ID:
      ```diff
      /interoperabilityRecord/{id}
      Params:
        id: String (required)
      ```
        
- ### Provider
  #### CRUD operations for Providers
  - DELETE
    - Deletes the Provider of the specific Catalogue given its ID:
      ```diff
      /provider/{id}
      Params:
        id: String (required)
        catalogue_id: String (required)
      ```
  - GET
    - Get a list of all Providers of the specific Catalogue in the Portal:
      ```diff
      /provider/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns all Datasources of a specific Provider of the EOSC Catalogue given its ID:
      ```diff
      /provider/datasources/{id}
      Params:
        id: String (required)
      ```
     - Returns all Services of a specific Provider of the EOSC Catalogue given its ID:
        ```diff
        /provider/services/{id}
        Params:
          id: String (required)
        ```
    - Returns the Provider of the specific Catalogue given its ID:
      ```diff
      /provider/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
  - PUT
    - Updates the Provider of the specific Catalogue give its ID:
      ```diff
      /provider
      Body:
        Provider JSON (required)
      Params:
        catalogue_id: String
        comment: String
      ```
- ### Public
  #### Get information about Public resources (Datasources, Providers, Services)
  - GET
    - Get a list of all Public Datasources of the specific Catalogue in the Portal:
      ```diff
      /public/datasource/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Public Datasource of the specific Catalogue given its ID:
      ```diff
      /public/datasource/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
    - Get a list of all Public Providers of the specific Catalogue in the Portal:
      ```diff
      /public/provider/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Public Provider of the specific Catalogue given its ID:
      ```diff
      /public/provider/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
    - Get a list of all Public Services of the specific Catalogue in the Portal:
      ```diff
      /public/resource/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Public Service of the specific Catalogue given its ID:
      ```diff
      /public/resource/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
    - Get a list of all Public Training Resources of the specific Catalogue in the Portal:
      ```diff
      /public/trainingResource/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Public Training Resource of the specific Catalogue given its ID:
      ```diff
      /public/trainingResource/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
  
- ### Resource 
  #### CRUD operations for Services
  ##### Mapping also supports '/resource'
  ##### Query GET API calls now support the 'type' path param with values 'service', 'datasource', 'all'
  - DELETE
    - Deletes the Service of the specific Catalogue given its ID:
      ```diff
      /service/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
  - GET
    - Returns a list of all Services of the specific Catalogue in the Portal:
      ```diff
        /service/all
        Params:
          catalogue_id: String (required)
          query: String (Keyword to refine the search)
          from : int (Starting index in the result set)
          quantity: int (Quantity to be fetched)
          order: String (asc/desc)
          orderField: String (eg. id)
      ```
    - Get all Services in the catalogue organized by an attribute:
      ```diff
        /service/by/{field}
        Params:
          field: Service field (required)
      ```
    - Returns the Service of the specific Catalogue given its ID:
      ```diff
        /service/{id}
        Params:
          id: String (required)
          catalogue_id: String
      ```
  - POST
    - Creates a new EOSC Service:
      ```diff
        /service
        Body:
          Service JSON (required)
    - Validates a Service:
      ```diff
      /service/validate
      Body:
        Service JSON (required)
  - PUT
    - Updates a specific EOSC Service:
      ```diff
      /service
      Body:
        Service JSON (required)
      Params:
        comment: String
      ```
  
- ### Resource Interoperability Record
  #### CRUD operations for Services
  - DELETE
    - Deletes the Resource Interoperability Record of the specific Resource:
      ```diff
      /resourceInteroperabilityRecord/{resourceId}/{resourceInteroperabilityRecordId}
      Params:
        resourceId: String (required)
        resourceInteroperabilityRecordId: String (required)
      ```
  - GET
    - Returns a list of all Resource Interoperability Records of the specific Catalogue in the Portal:
      ```diff
      /resourceInteroperabilityRecord/all
      Params:
        catalogue_id: String (required)
        query: String (Keyword to refine the search)
        from : int (Starting index in the result set)
        quantity: int (Quantity to be fetched)
        order: String (asc/desc)
        orderField: String (eg. id)
      ```
    - Returns the Resource Interoperability Record of the specific Catalogue given the Resource ID:
      ```diff
        /resourceInteroperabilityRecord/byResource/{resourceId}
        Params:
          resourceId: String (required)
          catalogue_id: String
      ```
    - Returns the Resource Interoperability Record of the specific Catalogue given its ID:
      ```diff
        /resourceInteroperabilityRecord/{id}
        Params:
          id: String (required)
      ```
  - POST
    - Creates a new Resource Interoperability Record given its resourceType (eg. service, datasource):
      ```diff
        /resourceInteroperabilityRecord
        Body:
          ResourceInteroperabilityRecord: JSON (required)
        Params:
          resourceType: String (required)
      ```
  - PUT
    - Updates a specific Resource Interoperability Record:
      ```diff
      /resourceInteroperabilityRecord
      Body:
        ResourceInteroperabilityRecord: JSON (required)
      ```
  
- ### Service Extensions
  #### CRUD operations for Service Extensions (Helpdesk/Monitoring)
  - DELETE
    - Deletes the Helpdesk of the specific Resource of the specific Catalogue:
      ```diff
      /service-extensions/helpdesk/{catalogueId}/{serviceId}
      Params:
        catalogueId: String (required)
        serviceId: String (required)
      ```
    - Deletes the Monitoring of the specific Resource of the specific Catalogue:
      ```diff
      /service-extensions/monitoring/{catalogueId}/{serviceId}
      Params:
        catalogueId: String (required)
        serviceId: String (required)
      ```
  - GET
    - Returns a list of all Helpdesks of the specific Catalogue in the Portal:
      ```diff
        /service-extensions/helpdesk/all
        Params:
          catalogue_id: String (required)
          query: String (Keyword to refine the search)
          from : int (Starting index in the result set)
          quantity: int (Quantity to be fetched)
          order: String (asc/desc)
          orderField: String (eg. id)
      ```
    - Returns the Helpdesk of the specific Catalogue given the Resource ID:
      ```diff
        /service-extensions/helpdesk/byService/{serviceId}
        Params:
          serviceId: String (required)
          catalogue_id: String
      ```
    - Returns the Helpdesk of the specific Catalogue given its ID:
      ```diff
        /service-extensions/helpdesk/{id}
        Params:
          id: String (required)
      ```
    - Returns a list of all Monitorings of the specific Catalogue in the Portal:
      ```diff
        /service-extensions/monitoring/all
        Params:
          catalogue_id: String (required)
          query: String (Keyword to refine the search)
          from : int (Starting index in the result set)
          quantity: int (Quantity to be fetched)
          order: String (asc/desc)
          orderField: String (eg. id)
      ```
    - Returns the Monitoring of the specific Catalogue given the Resource ID:
      ```diff
        /service-extensions/monitoring/byService/{serviceId}
        Params:
          serviceId: String (required)
          catalogue_id: String
      ```
    - Returns a list with all the available Monitoring Service Types:
      ```diff
        /service-extensions/monitoring/serviceTypes
      ```
    - Returns the Monitoring of the specific Catalogue given its ID:
      ```diff
        /service-extensions/monitoring/{id}
        Params:
          id: String (required)
      ```
  - POST
    - Creates a new Helpdesk for the specific Catalogue:
      ```diff
        /service-extensions/helpdesk
        Body:
          Helpdesk JSON (required)
        Params:
          catalogue_id: String
    - Creates a new Monitoring for the specific Catalogue:
      ```diff
        /service-extensions/monitoring
        Body:
          Monitoring JSON (required)
        Params:
          catalogue_id: String
  - PUT
    - Updates a specific Helpdesk of a specific Catalogue:
      ```diff
      /service-extensions/helpdesk
      Body:
        Helpdesk JSON (required)
      Params:
        catalogue_id: String
      ```
    - Updates a specific Monitoring of a specific Catalogue:
      ```diff
      /service-extensions/montoring
      Body:
        Monitoring JSON (required)
      Params:
        catalogue_id: String
      ```

- ### Training Resource
  #### CRUD operations for Training Resources
  - DELETE
    - Deletes the Training Resource of the specific Catalogue given its ID:
      ```diff
      /trainingResource/{id}
      Params:
        id: String (required)
        catalogue_id: String
      ```
  - GET
    - Returns a list of all Training Resources of the specific Catalogue in the Portal:
      ```diff
        /trainingResource/all
        Params:
          catalogue_id: String (required)
          query: String (Keyword to refine the search)
          from : int (Starting index in the result set)
          quantity: int (Quantity to be fetched)
          order: String (asc/desc)
          orderField: String (eg. id)
      ```
    - Get all Training Resources in the catalogue organized by an attribute:
      ```diff
        /trainingResource/by/{field}
        Params:
          field: Training Resource field (required)
      ```
    - Returns the Training Resource of the specific Catalogue given its ID:
      ```diff
        /trainingResource/{id}
        Params:
          id: String (required)
          catalogue_id: String
      ```
  - POST
    - Creates a new EOSC Training Resource:
      ```diff
        /trainingResource
        Body:
          Training Resource JSON (required)
    - Validates a Training Resource:
      ```diff
      /trainingResource/validate
      Body:
        Training Resource JSON (required)
  - PUT
    - Updates a specific EOSC Training Resource:
      ```diff
      /trainingResource
      Body:
        Training Resource JSON (required)
      Params:
        comment: String
      ```

- ### Vocabulary   
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
        type: Vocabulary Type (required)
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
      Params:
        id: String (required)
      ```

### Notes:
- Resource (with capital 'R') refers to both Services/Datasources
- If catalogueId/catalogue_id is not provided, the field gets automatically the Project's Catalogue name as its value (in our case 'eosc')
- catalogueId/catalogue_id = 'all' will fetch all the resources from all Catalogues.



## Objects:
  ### Catalogue:
    {
      "id": "(required on PUT only)",
      "abbreviation": "string",
      "name": "string",
      "website": "URL",
      "legalEntity": "boolean",
      "legalStatus": "string",
      "hostingLegalEntity": "string",
      "description": "string",
      "logo":"URL",
      "multimedia":[
        {
           "multimediaURL": "URL",
           "multimediaName": "string"
        }
      ],
      "scientificDomains":[
        {
           "scientificDomain": "string",
           "scientificSubdomain": "string"
        }
      ],
      "tags":[
        "string"
      ],
      "location":{
        "streetNameAndNumber": "string",
        "postalCode": "string",
        "city": "string",
        "region": "string",
        "country": "string"
      },
      "mainContact":{
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string",
        "position": "string"
      },
      "publicContacts":[
        {
           "firstName": "string",
           "lastName": "string",
           "email": "string",
           "phone": "string",
           "position": "string"
        }
      ],
      "participatingCountries":[
        "string"
      ],
      "affiliations":[
        "string"
      ],
      "networks":[
        "string"
      ],
      "users":[
        {
           "email": "string",
           "id": "string",
           "name": "string",
           "surname": "string"
        }
      ]
    }
    
  ### Datasource:
    {
      "id": "(required on PUT only)",
      "submissionPolicyURL": "URL",
      "abbreviation": "string",
      "preservationPolicyURL": "URL",
      "name": "string",
      "versionControl": "boolean",
      "persistentIdentitySystems": [
        {
          "persistentIdentityEntityType": "string",
          "persistentIdentityEntityTypeSchemes": [
            "string"
          ]
        }
      ],
      "resourceOrganisation": "string",
      "jurisdiction": "string",
      "resourceProviders": [
        "string"
      ],
      "datasourceClassification": "string",
      "webpage": "URL",
      "description": "string",
      "researchEntityTypes": [
        "string"
      ],
      "tagline": "string",
      "thematic": "boolean",
      "logo": "URL",
      "researchProductLicensings": [
        {
          "researchProductLicenseName": "string",
          "researchProductLicenseURL": "URL"
        }
      ],
      "multimedia": [
        {
          "multimediaURL": "URL",
          "multimediaName": "string"
        }
      ],
      "researchProductAccessPolicies": [
        "string"
      ],
      "researchProductMetadataLicensing": {
        "researchProductMetadataLicenseName": "string",
        "researchProductMetadataLicenseURL": "URL"
      },
      "useCases": [
        {
          "useCaseURL": "string",
          "useCaseName": "string"
        }
      ],
      "researchProductMetadataAccessPolicies": [
        "string"
      ],
      "scientificDomains": [
        {
          "scientificDomain": "string",
          "scientificSubdomain": "string"
        }
      ],
      "categories": [
        {
          "category": "string",
          "subcategory": "string"
        }
      ],
      "targetUsers": [
        "string"
      ],
      "accessTypes": [
        "string"
      ],
      "accessModes": [
        "string"
      ],
      "tags": [
        "string"
      ],
      "geographicalAvailabilities": [
        "string"
      ],
      "languageAvailabilities": [
        "string"
      ],
      "resourceGeographicLocations": [
        "string"
      ],
      "mainContact": {
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string",
        "position": "string",
        "organisation": "string"
      },
      "publicContacts": [
        {
          "firstName": "string",
          "lastName": "string",
          "email": "string",
          "phone": "string",
          "position": "string",
          "organisation": "string"
        }
      ],
      "helpdeskEmail": "string",
      "securityContactEmail": "string",
      "trl": "string",
      "lifeCycleStatus": "string",
      "certifications": [
        "string"
      ],
      "standards": [
        "string"
      ],
      "openSourceTechnologies": [
        "string"
      ],
      "version": "string",
      "lastUpdate": "string",
      "changeLog": [
        "string"
      ],
      "requiredResources": [
        "string"
      ],
      "relatedResources": [
        "string"
      ],
      "relatedPlatforms": [
        "string"
      ],
      "catalogueId": "string",
      "fundingBody": [
        "string"
      ],
      "fundingPrograms": [
        "string"
      ],
      "grantProjectNames": [
        "string"
      ],
      "helpdeskPage": "URL",
      "userManual": "URL",
      "termsOfUse": "URL",
      "privacyPolicy": "URL",
      "accessPolicy": "URL",
      "resourceLevel": "URL",
      "trainingInformation": "URL",
      "statusMonitoring": "URL",
      "maintenance": "URL",
      "orderType": "string",
      "order": "URL",
      "paymentModel": "URL",
      "pricing": "URL"
    }
    
  ### Interoperability Record:
    {
      "id": "(auto-assigned)",
      "identifierInfo": {
        "identifier": "string",
        "identifierType": "string"
      },
      "creators": [
        {
          "creatorNameTypeInfo": {
            "creatorName": "string",
            "nameType": "string"
          },
          "givenName": "string",
          "familyName": "string",
          "nameIdentifier": "string",
          "creatorAffiliationInfo": {
            "affiliation": "string",
            "affiliationIdentifier": "string"
          }
        }
      ],
      "title": "string",
      "publicationYear": "string",
      "resourceTypesInfo": [
        {
          "resourceType": "string",
          "resourceTypeGeneral": "string"
        }
      ],
      "created": "string",
      "updated": "string",
      "eoscRelatedStandards": [
        "URL"
      ],
      "rights": [
        {
          "rightTitle": "string",
          "rightURI": "URL",
          "rightIdentifier": "string"
        }
      ],
      "description": "string",
      "status": "string",
      "domain": "string",
      "eoscGuidelineType": "string",
      "eoscIntegrationOptions": [
        "string"
      ]
    }

  ### Provider:
    {
      "id": "(required on PUT only)",
      "abbreviation": "string",
      "name": "string",
      "website": "URL,
      "legalEntity": "boolean",
      "legalStatus": "string",
      "hostingLegalEntity": "string",
      "description": "string",
      "logo": "URL",
      "multimedia": [
        {
          "multimediaURL": "URL",
          "multimediaName": "string"
        }
      ],
      "scientificDomains": [
        {
          "scientificDomain": "string",
          "scientificSubdomain": "string"
        }
      ],
      "tags": [
        "string"
      ],
      "structureTypes": [
        "string"
      ],
      "location": {
        "streetNameAndNumber": "string",
        "postalCode": "string",
        "city": "string",
        "region": "string",
        "country": "string"
      },
      "mainContact": {
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string",
        "position": "string"
      },
      "publicContacts": [
        {
          "firstName": "string",
          "lastName": "string",
          "email": "string",
          "phone": "string",
          "position": "string"
        }
      ],
      "lifeCycleStatus": "string",
      "certifications": [
        "string"
      ],
      "participatingCountries": [
        "string"
      ],
      "affiliations": [
        "string"
      ],
      "networks": [
        "string"
      ],
      "catalogueId": "string",
      "esfriDomains": [
        "string"
      ],
      "esfriType": "string",
      "merilScientificDomains": [
        {
          "merilScientificDomain": "string",
          "merilScientificSubdomain": "string"
        }
      ],
      "areasOfActivity": [
        "string"
      ],
      "societalGrandChallenges": [
        "string"
      ],
      "nationalRoadmaps": [
        "string"
      ],
      "users": [
        {
          "email": "string",
          "id": "string",
          "name": "string",
          "surname": "string"
        }
      ]
    }

  ### Service:
    {
      "id": "(required on PUT only)",
      "abbreviation": "string",
      "name": "string",
      "resourceOrganisation": "string",
      "resourceProviders": [
        "string"
      ],
      "webpage": "URL",
      "description": "string",
      "tagline": "string",
      "logo": "URL",
      "multimedia": [
        {
          "multimediaURL": "URL",
          "multimediaName": "string"
        }
      ],
      "useCases": [
        {
          "useCaseURL": "URL",
          "useCaseName": "string"
        }
      ],
      "scientificDomains": [
        {
          "scientificDomain": "string",
          "scientificSubdomain": "string"
        }
      ],
      "categories": [
        {
          "category": "string",
          "subcategory": "string"
        }
      ],
      "targetUsers": [
        "string"
      ],
      "accessTypes": [
        "string"
      ],
      "accessModes": [
        "string"
      ],
      "tags": [
        "string"
      ],
      "geographicalAvailabilities": [
        "string"
      ],
      "languageAvailabilities": [
        "string"
      ],
      "resourceGeographicLocations": [
        "string"
      ],
      "mainContact": {
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string",
        "position": "string",
        "organisation": "string"
      },
      "publicContacts": [
        {
          "firstName": "string",
          "lastName": "string",
          "email": "string",
          "phone": "string",
          "position": "string",
          "organisation": "string"
        }
      ],
      "helpdeskEmail": "string",
      "securityContactEmail": "string",
      "trl": "string",
      "lifeCycleStatus": "string",
      "certifications": [
        "string"
      ],
      "standards": [
        "string"
      ],
      "openSourceTechnologies": [
        "string"
      ],
      "version": "string",
      "lastUpdate": "string",
      "changeLog": [
        "string"
      ],
      "requiredResources": [
        "string"
      ],
      "relatedResources": [
        "string"
      ],
      "relatedPlatforms": [
        "string"
      ],
      "catalogueId": "string",
      "fundingBody": [
        "string"
      ],
      "fundingPrograms": [
        "string"
      ],
      "grantProjectNames": [
        "string"
      ],
      "helpdeskPage": "URL",
      "userManual": "URL",
      "termsOfUse": "URL",
      "privacyPolicy": "URL",
      "accessPolicy": "URL",
      "resourceLevel": "URL",
      "trainingInformation": "URL",
      "statusMonitoring": "URL",
      "maintenance": "URL",
      "orderType": "string",
      "order": "URL",
      "paymentModel": "URL",
      "pricing": "URL"
    }
    
  ### Training Resource:
    {
      "id": "(required on PUT only)",
      "title": "string",
      "resourceOrganisation": "string",
      "resourceProviders": [
        "string"
      ],
      "authors": [
        "string"
      ],
      "url": "URL",
      "urlType": "string",
      "eoscRelatedServices": [
        "string"
      ],
      "description": "string",
      "keywords": [
        "string"
      ],
      "license": "string",
      "accessRights": "string",
      "versionDate": "Date",
      "targetGroups": [
        "string"
      ],
      "learningResourceTypes": [
        "string"
      ],
      "learningOutcomes": [
        "string"
      ],
      "expertiseLevel": "string",
      "contentResourceTypes": [
        "string"
      ],
      "qualifications": [
        "string"
      ],
      "duration": "string",
      "languages": [
        "string"
      ],
      "geographicalAvailabilities": [
        "string"
      ],
      "scientificDomains": [
        {
          "scientificDomain": "string",
          "scientificSubdomain": "string"
        }
      ],
      "contact": {
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string",
        "position": "string",
        "organisation": "string"
      },
      "catalogueId": "string"
    }

  ### Resource Extras:
    {
      "eoscIFGuidelines": [
        {
          "label": "string",
          "pid": "string",
          "semanticRelationship": "string",
          "url": "URL"
        }
      ],
      "horizontalService": false,
      "researchCategories": [
        "string"
      ]
    }
    
  ### Resource Interoperability Record:
    {
      "id": "(required on PUT only)",
      "resourceId": "string",
      "catalogueId": "string",
      "interoperabilityRecordIds": [
        "string"
      ]
    }

  ### Helpdesk:
    {
      "id": "(required on PUT only)",
      "serviceId": "string",
      "services": [
        "string"
      ],
      "helpdeskType": "string",
      "supportGroups": [
        "string"
      ],
      "organisation": "string",
      "emails": [
        "string"
      ],
      "agents": [
        "string"
      ],
      "signatures": [
        "string"
      ],
      "ticketPreservation": "boolean",
      "webform": "boolean
    }

  ### Monitoring:
    {
      "id": "(required on PUT only)",
      "serviceId": "string",
      "monitoredBy": "string",
      "monitoringGroups": [
        {
          "serviceType": "string",
          "endpoint": "URL",
          "metrics": [
            {
              "probe": "string",
              "metric": "string"
            }
          ]
        }
      ]
    }
    
  ### Vocabulary:
    {
      "description": "string",
      "extras": {},
      "id": "string",
      "name": "string",
      "parentId": "string",
      "type": "string"
    }

## Vocabulary Types:
  - [ACCESS_MODE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ACCESS_MODE.json)
  - [ACCESS_TYPE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/ACCESS_TYPE.json)
  - [CATALOGUE_STATE](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CATALOGUE_STATE.json)
  - [CATEGORY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/CATEGORY.json)
  - [COUNTRY](https://github.com/madgeek-arc/resource-catalogue-docs/blob/master/vocabularies/COUNTRY.json)
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
