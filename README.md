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

- https://providers.eosc-portal.eu/api OR https://api.eosc-portal.eu/
- https://beta.providers.eosc-portal.eu/api/
- https://sandbox.providers.eosc-portal.eu/api/

## Controllers:

- ### Catalogue
  #### CRUD operations for Catalogues + external (non EOSC) resources (Datasources, Providers, Services)
  - DELETE
    - Deletes the Datasource of the specific Catalogue given its ID:
        ```diff
        /catalogue/{catalogueId}/datasource/{id}
        ```
    - Deletes the Provider of the specific Catalogue given its ID:
        ```diff
        /catalogue/{catalogueId}/provider/{id}
        ```
    - Deletes the Service of the specific Catalogue given its ID:
        ```diff
        /catalogue/{catalogueId}/resource/{id}
        ```
  - GET
    - Get a list of all Catalogues in the Portal:
        ```diff
        /catalogue/all
        ```
    - Returns the Datasource of the specific Catalogue given its ID:
        ```diff
        /catalogue/{catalogueId}/datasource/{resourceId}
        ```
    - Get a list of all Providers of the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/provider/all
        ```
    - Returns the Provider of the specific Catalogue given its ID:
        ```diff
        /catalogue/{catalogueId}/provider/{providerId}
        ```
    - Returns the Service of the specific Catalogue given its ID:
        ```diff
        /catalogue/{catalogueId}/resource/{resourceId}
        ```
    - Get a list of all Datasources of the specific Provider of the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/{providerId}/datasource/all
        ```
    - Get a list of all Service of the specific Provider of the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/{providerId}/resource/all
        ```
    - Get a specific Catalogue given its ID:
        ```diff
        /catalogue/{id}
        ```
  - POST
    - Creates a new Catalogue:
        ```diff
        /catalogue
        ```
    - Creates a new Datasource for the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/datasource
        ```
    - Creates a new Provider for the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/provider
        ```
    - Creates a new Service for the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/resource
        ```
  - PUT
    - Updates a specific Catalogue:
        ```diff
        /catalogue
        ```
    - Updates the Datasource of the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/datasource
        ```
    - Updates the Provider of the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/provider
        ```
    - Updates the Service of the specific Catalogue:
        ```diff
        /catalogue/{catalogueId}/resource
        ```

- ### Datasource
  #### CRUD operations for EOSC Datasources
  
- ### Provider
  #### CRUD operations for EOSC Providers

- ### Public
  #### Get information about Public resources (Datasources, Providers, Services)
  
- ### Resource
  #### CRUD operations for EOSC Services
  
- ### Service Extensions
  #### CRUD operations for Service Extensions

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
        ```
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
