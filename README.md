<div align="center">
  <img src='https://eosc-portal.eu/sites/all/themes/theme1/logo.png'></img>
</div>

# Resource Catalogue Documentation

- [Vocabularies](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/vocabularies)
- [Migration Scripts](https://github.com/madgeek-arc/resource-catalogue-docs/tree/master/scripts)

## Swagger UI Instances:

- [Production](https://api.eosc-portal.eu/)
- [Sandbox](https://beta.providers.eosc-portal.eu/api/)
- [Beta](https://sandbox.providers.eosc-portal.eu/api/)

## API:

- https://providers.eosc-portal.eu/api, https://api.eosc-portal.eu/
- https://beta.providers.eosc-portal.eu/api/
- https://sandbox.providers.eosc-portal.eu/api/

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
    - Get a specific Catalogue given its ID:
      ```diff
      /catalogue/{id}
      Params:
        id: String (required)
      ```
  - POST
    - Creates a new Catalogue:
      ```diff
      /catalogue
      Body:
        Catalogue JSON (required)
      ```
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
  
- ### Resource
  #### CRUD operations for Services
  (Mapping also supports '/resource')
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
    - Get all Resources in the catalogue organized by an attribute:
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
      "id":"(required on PUT only)",
      "abbreviation":"string",
      "name":"string",
      "website":"https://example.com",
      "legalEntity":false,
      "legalStatus":"string",
      "hostingLegalEntity":"string",
      "description":"string",
      "logo":"https://example.com",
      "multimedia":[
        {
           "multimediaURL":"string",
           "multimediaName":"string"
        }
      ],
      "scientificDomains":[
        {
           "scientificDomain":"string",
           "scientificSubdomain":"string"
        }
      ],
      "tags":[
        "string"
      ],
      "location":{
        "streetNameAndNumber":"string",
        "postalCode":"string",
        "city":"string",
        "region":"string",
        "country":"string"
      },
      "mainContact":{
        "firstName":"string",
        "lastName":"string",
        "email":"string",
        "phone":"string",
        "position":"string"
      },
      "publicContacts":[
        {
           "firstName":"string",
           "lastName":"string",
           "email":"string",
           "phone":"string",
           "position":"string"
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
           "email":"string",
           "id":"string",
           "name":"string",
           "surname":"string"
        }
      ]
    }
    
  ### Datasource:
    {
      "id": "(required on PUT only)",
      "submissionPolicyURL": "https://example.com",
      "abbreviation": "string",
      "preservationPolicyURL": "https://example.com",
      "name": "string",
      "versionControl": false,
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
      "webpage": "https://example.com",
      "description": "string",
      "researchEntityTypes": [
        "string"
      ],
      "tagline": "string",
      "thematic": false,
      "logo": "https://example.com",
      "researchProductLicensings": [
        {
          "researchProductLicenseName": "string",
          "researchProductLicenseURL": "string"
        }
      ],
      "multimedia": [
        {
          "multimediaURL": "string",
          "multimediaName": "string"
        }
      ],
      "researchProductAccessPolicies": [
        "string"
      ],
      "researchProductMetadataLicensing": {
        "researchProductMetadataLicenseName": "string",
        "researchProductMetadataLicenseURL": "string"
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
      "lastUpdate": "2020-01-01",
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
      "helpdeskPage": "https://example.com",
      "userManual": "https://example.com",
      "termsOfUse": "https://example.com",
      "privacyPolicy": "https://example.com",
      "accessPolicy": "https://example.com",
      "resourceLevel": "https://example.com",
      "trainingInformation": "https://example.com",
      "statusMonitoring": "https://example.com",
      "maintenance": "https://example.com",
      "orderType": "string",
      "order": "https://example.com",
      "paymentModel": "https://example.com",
      "pricing": "https://example.com"
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
      "publicationYear": 0,
      "resourceTypesInfo": [
        {
          "resourceType": "string",
          "resourceTypeGeneral": "string"
        }
      ],
      "created": "string",
      "updated": "string",
      "eoscRelatedStandards": [
        null
      ],
      "rights": [
        {
          "rightTitle": "string",
          "rightURI": "string",
          "rightIdentifier": "string"
        }
      ],
      "description": "string",
      "status": "string",
      "domain": "string",
      "eoscGuidelineType": "string",
      "eoscIntegrationOptions": [
        "string"
      ],
      "eoscAAI": false
    }

  ### Provider:
    {
      "id": "(required on PUT only)",
      "abbreviation": "string",
      "name": "string",
      "website": "https://example.com",
      "legalEntity": false,
      "legalStatus": "string",
      "hostingLegalEntity": "string",
      "description": "string",
      "logo": "https://example.com",
      "multimedia": [
        {
          "multimediaURL": "string",
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
      "webpage": "https://example.com",
      "description": "string",
      "tagline": "string",
      "logo": "https://example.com",
      "multimedia": [
        {
          "multimediaURL": "string",
          "multimediaName": "string"
        }
      ],
      "useCases": [
        {
          "useCaseURL": "string",
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
      "lastUpdate": "2020-01-01",
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
      "helpdeskPage": "https://example.com",
      "userManual": "https://example.com",
      "termsOfUse": "https://example.com",
      "privacyPolicy": "https://example.com",
      "accessPolicy": "https://example.com",
      "resourceLevel": "https://example.com",
      "trainingInformation": "https://example.com",
      "statusMonitoring": "https://example.com",
      "maintenance": "https://example.com",
      "orderType": "string",
      "order": "https://example.com",
      "paymentModel": "https://example.com",
      "pricing": "https://example.com"
    }

  ### Resource Extras:
    {
      "eoscIFGuidelines": [
        {
          "label": "string",
          "pid": "string",
          "semanticRelationship": "string",
          "url": "string"
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
      "ticketPreservation": false,
      "webform": false
    }

  ### Monitoring:
    {
      "id": "(required on PUT only)",
      "serviceId": "string",
      "monitoredBy": "string",
      "monitoringGroups": [
        {
          "serviceType": "string",
          "endpoint": "string",
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
  - ACCESS_MODE
  - ACCESS_TYPE
  - CATALOGUE_STATE
  - CATEGORY
  - COUNTRY
  - DS_CLASSIFICATION
  - DS_COAR_ACCESS_RIGHTS_1_0
  - DS_JURISDICTION
  - DS_PERSISTENT_IDENTITY_SCHEME
  - DS_RESEARCH_ENTITY_TYPE
  - FUNDING_BODY
  - FUNDING_PROGRAM
  - GEOGRAPHIC_LOCATION
  - IR_DOMAIN
  - IR_EOSC_GUIDELINE_TYPE
  - IR_IDENTIFIER_TYPE
  - IR_NAME_TYPE
  - IR_RESOURCE_TYPE_GENERAL
  - IR_STATUS
  - LANGUAGE
  - LIFE_CYCLE_STATUS
  - MONITORING_MONITORED_BY
  - ORDER_TYPE
  - PROVIDER_AREA_OF_ACTIVITY
  - PROVIDER_ESFRI_DOMAIN
  - PROVIDER_ESFRI_TYPE
  - PROVIDER_HOSTING_LEGAL_ENTITY
  - PROVIDER_LEGAL_STATUS
  - PROVIDER_LIFE_CYCLE_STATUS
  - PROVIDER_MERIL_SCIENTIFIC_DOMAIN
  - PROVIDER_MERIL_SCIENTIFIC_SUBDOMAIN
  - PROVIDER_NETWORK
  - PROVIDER_SOCIETAL_GRAND_CHALLENGE
  - PROVIDER_STATE
  - PROVIDER_STRUCTURE_TYPE
  - REGION
  - RELATED_PLATFORM
  - RESEARCH_CATEGORY
  - RESOURCE_STATE
  - SCIENTIFIC_DOMAIN
  - SCIENTIFIC_SUBDOMAIN
  - SEMANTIC_RELATIONSHIP
  - SUBCATEGORY
  - SUPERCATEGORY
  - TARGET_USER
  - TEMPLATE_STATE
  - TRL
