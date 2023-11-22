######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

###################################################### GLOBALS #########################################################
datasourceIds = []
datasourceFolder = '/datasource/'
serviceFolder = '/service/'
otherFolders = ['/provider/', '/training_resource/', '/interoperability_record/']
###################################################### GLOBALS #########################################################

######################################## PREDEFINED MARKETPLACE LOCATION VALUES ########################################
access_computing_and_storage_resources = ['grena.gcloudge', 'geant.l3vpn', 'bluebridge.software_integration_support',
                                          'incd.application_lifecycle_enabler_4_cloud',
                                          'grycap.oscar', 'eosc.grycap.oscar',
                                          'openrisknet.squonk_computational_notebook', 'desy.pan_faas',
                                          'infn.indigo_identity_and_access_management', 'brfaa.nanocrystal',
                                          'ukim_fcse.finki_cloud', 'edelweiss_connect.squonk_computational_notebook',
                                          'desy.pan_data', 'northern_data_cloud_services.northern_data_cloud_services',
                                          'ipb.paradox-iv_cluster', 'egi-fed.egi_software_distribution',
                                          'smartsmear.new_particle_formation_event_analysis',
                                          'ipb.simple_storage_service',
                                          'rolos.machine_intelligence_platfrom_for_research', 'csc-fi.puhti',
                                          'cineca.iscra', 'infn.paas_orchestrator', 'ifca-csic.ai4eosc_platform',
                                          'uot.ur', 'vu.itoac', 'tum-net.slices-vpostum', 'ni4os.grena.gcloudge',
                                          'eosc.geant.l3vpn', 'eosc.bluebridge.software_integration_support',
                                          'eosc.incd.application_lifecycle_enabler_4_cloud',
                                          'eosc.openrisknet.squonk_computational_notebook', 'eosc.desy.pan_faas',
                                          'eosc.infn.indigo_identity_and_access_management', 'ni4os.brfaa.nanocrystal',
                                          'ni4os.ukim_fcse.finki_cloud',
                                          'eosc.edelweiss_connect.squonk_computational_notebook', 'eosc.desy.pan_data',
                                          'eosc.northern_data_cloud_services.northern_data_cloud_services',
                                          'ni4os.ipb.paradox-iv_cluster', 'eosc.egi-fed.egi_software_distribution',
                                          'eosc.smartsmear.new_particle_formation_event_analysis',
                                          'ni4os.ipb.simple_storage_service',
                                          'eosc.rolos.machine_intelligence_platfrom_for_research', 'eosc.csc-fi.puhti',
                                          'eosc.cineca.iscra', 'eosc.infn.paas_orchestrator',
                                          'eosc.ifca-csic.ai4eosc_platform', 'eosc-nordic.uot.ur',
                                          'eosc-nordic.vu.itoac', 'eosc.tum-net.slices-vpostum',
                                          'sixsq.snap-based_jupyter_notebook_for_eo_exploration',
                                          'geant.geant_cloud_flow',
                                          'eosc.sixsq.snap-based_jupyter_notebook_for_eo_exploration',
                                          'eosc.geant.geant_cloud_flow', 'egi-fed.egi_replay',
                                          'openminted.builder_of_tdm_applications', 'eosc.egi-fed.egi_replay',
                                          'eosc.openminted.builder_of_tdm_applications']
access_research_infrastructures = ['openrisknet.jaqpot', 'geant.inacademia', 'eosc.geant.inacademia', 'eudat.b2access',
                                   'enhancer.swiss_escience_grid_certificates', 'authenix.authenix',
                                   'egi-fed.check-in', 'eosc.egi-fed.check-in',
                                   'eosc.enhancer.swiss_escience_grid_certificates', 'eosc.authenix.authenix',
                                   'komanord.guardomic', 'eosc.komanord.guardomic', 'eosc.eudat.b2access',
                                   'geant.trusted_introducer', 'eosc.geant.trusted_introducer',
                                   'edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                                   'epos.envri_catalog_of_services', 'geant.open', 'edelweiss_connect.jaqpot',
                                   'geant.plus', 'geant.eduroam_managed_idp',
                                   'sixsq.snap-based_jupyter_notebook_for_eo_exploration', 'grnet.ni4os-europe_login',
                                   'geant.eduteams', 'geant.edugain_federation_as_a_service',
                                   'grnet.argo_monitoring_engine', 'geant.geant_cloud_flow', 'geant.perfsonar',
                                   'geant.testbeds_service', 'geant.edugain', 'vecma.vecma_vvuq_toolkit_vecmatk',
                                   'geant.eduvpn_-_access_your_institutes_network_or_the_internet_using_an_encrypted_connection',
                                   'geant.eduroam', 'geant.edumeet_-_webbased_videoconferencing_platform', 'geant.ip',
                                   'geant.edupert', 'geant.geant_sandbox resource profile', 'esrf.visa',
                                   'iisas.edudns_dynamic_dns_service_for_academia',
                                   'geant.ocre_cloud services by setcor', 'geant.ocre_cloud services by t-systems',
                                   'geant.ocre_cloud services by vancis', 'geant.ocre_cloud services by sentia',
                                   'geant.trusted_certificate_service', 'geant.ocre_cloud services by scc',
                                   'geant.ocre_cloud services by proact', 'geant.ocre_cloud services by cloud and heat',
                                   'geant.ocre_cloud services by x-ion', 'geant.wifimon', 'geant.lambda',
                                   'ess_eric.ess_labs', 'geant.mdvpn', 'geant.ocrecleura', 'geant.ocrecomtrade',
                                   'operas.vera', 'geant.ocrecloudsigma', 'geant.ocrecsipiemonte', 'geant.ocreaws',
                                   'geant.ocre100', 'geant.ocreequinix', 'geant.ocreionos', 'geant.ocregoogle',
                                   'geant.ocreexoscale', 'geant.ocreibm', 'geant.ocrecloudferro', 'geant.ocreoracle',
                                   'geant.ocreovhcloud', 'geant.ocreorangebusiness', 'geant.ocreazure',
                                   'geant.ocreposita', 'geant.ocresafespring', 'uot.plutof', 'ekt.nephos',
                                   'geant.ocreorange', 'eosc.openrisknet.jaqpot',
                                   'eosc.edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                                   'eosc.epos.envri_catalog_of_services', 'eosc.geant.open',
                                   'eosc.edelweiss_connect.jaqpot', 'eosc.geant.plus', 'eosc.geant.eduroam_managed_idp',
                                   'eosc.sixsq.snap-based_jupyter_notebook_for_eo_exploration',
                                   'ni4os.grnet.ni4os-europe_login', 'eosc.geant.eduteams',
                                   'eosc.geant.edugain_federation_as_a_service', 'ni4os.grnet.argo_monitoring_engine',
                                   'eosc.geant.geant_cloud_flow', 'eosc.geant.perfsonar', 'eosc.geant.testbeds_service',
                                   'eosc.geant.edugain', 'eosc.vecma.vecma_vvuq_toolkit_vecmatk',
                                   'eosc.geant.eduvpn_-_access_your_institutes_network_or_the_internet_using_an_encrypted_connection',
                                   'eosc.geant.eduroam', 'eosc.geant.edumeet_-_webbased_videoconferencing_platform',
                                   'eosc.geant.ip', 'eosc.geant.edupert', 'eosc.geant.geant_sandbox resource profile',
                                   'eosc.esrf.visa', 'eosc.iisas.edudns_dynamic_dns_service_for_academia',
                                   'eosc.geant.ocre_cloud services by setcor',
                                   'eosc.geant.ocre_cloud services by t-systems',
                                   'eosc.geant.ocre_cloud services by vancis',
                                   'eosc.geant.ocre_cloud services by sentia', 'eosc.geant.trusted_certificate_service',
                                   'eosc.geant.ocre_cloud services by scc', 'eosc.geant.ocre_cloud services by proact',
                                   'eosc.geant.ocre_cloud services by cloud and heat',
                                   'eosc.geant.ocre_cloud services by x-ion', 'eosc.geant.wifimon', 'eosc.geant.lambda',
                                   'eosc.ess_eric.ess_labs', 'eosc.geant.mdvpn', 'eosc.geant.ocrecleura',
                                   'eosc.geant.ocrecomtrade', 'eosc.operas.vera', 'eosc.geant.ocrecloudsigma',
                                   'eosc.geant.ocrecsipiemonte', 'eosc.geant.ocreaws', 'eosc.geant.ocre100',
                                   'eosc.geant.ocreequinix', 'eosc.geant.ocreionos', 'eosc.geant.ocregoogle',
                                   'eosc.geant.ocreexoscale', 'eosc.geant.ocreibm', 'eosc.geant.ocrecloudferro',
                                   'eosc.geant.ocreoracle', 'eosc.geant.ocreovhcloud', 'eosc.geant.ocreorangebusiness',
                                   'eosc.geant.ocreazure', 'eosc.geant.ocreposita', 'eosc.geant.ocresafespring',
                                   'eosc-nordic.uot.plutof', 'eosc.ekt.nephos', 'eosc.geant.ocreorange', 'geant.l3vpn',
                                   'infn.indigo_identity_and_access_management', 'eosc.geant.l3vpn',
                                   'eosc.infn.indigo_identity_and_access_management', 'bluebridge.accounting_framework',
                                   'eosc.bluebridge.accounting_framework']
access_training_material = ['bifi_-_unizar.hm', 'e-cam.e-cam_online_training_portal',
                            'collabwith.collabwith_marketplace', 'hzdr.pan-trainingeu', 'eosc.hzdr.pan-trainingeu',
                            'eosc-dih.piloting_and_co-design_of_the_business_pilots',
                            'compbiomed.compbiomed_training_portal', 'bluebridge.scientific_training_environment',
                            'ess.pan-learning-org', 'openaire.openplato', 'psnc.learneosc-synergy',
                            'openaire.open_science_helpdesk', 'eosc.bifi_-_unizar.hm',
                            'eosc.e-cam.e-cam_online_training_portal', 'eosc.collabwith.collabwith_marketplace',
                            'eosc.eosc-dih.piloting_and_co-design_of_the_business_pilots',
                            'eosc.compbiomed.compbiomed_training_portal',
                            'eosc.bluebridge.scientific_training_environment', 'eosc.ess.pan-learning-org',
                            'eosc.openaire.openplato', 'eosc.psnc.learneosc-synergy',
                            'eosc.openaire.open_science_helpdesk', 'openminted.catalogue_of_ancillary_resources',
                            'eosc.openminted.catalogue_of_ancillary_resources', 'openminted.support_and_training',
                            'compbiomed.software_hub', 'eosc.openminted.support_and_training',
                            'eosc.compbiomed.software_hub']
discover_research_outputs = ['ehri.conny_kristel_fellowship_programme', 'eosc.ehri.conny_kristel_fellowship_programme',
                             'exoscale.european_cloud_hosting', 'eosc.exoscale.european_cloud_hosting'
                             'clarin-eric.virtual_language_observatory', 'eosc.clarin-eric.virtual_language_observatory',
                             'elsevier.digital_commons', 'seadatanet.marine_data_viewer', 'esa-int.geoss_web_portal',
                             'brfaa.chembioserver', 'ukim_fcse.gaussian_api', 'aginfra.geoanalytics_visualization',
                             'bluebridge.indian_ocean_tuna_commission_spatial_data_catalog', 'bineo.cos4env',
                             'ceric-eric.ceric-data-portal', 'nsl-ge.digital_repository_of_georgian_scientific_works',
                             'openminted.catalogue_of_corpora', 'bluebridge.global_record_of_stocks_and_fishery',
                             'sstir.public_rd_resource_graph_of_AI_in_Shanghai', 'inoe_2000.infra-art_spectral_library',
                             'openaire.funder_dashboard', 'beia.farmsustainabl',
                             'eosc.cnb-csic.covid-19_structural_hub', 'blue-cloud.discovery_access', 'ulb-sa.share_it',
                             'blue-cloud.mei_generator', 'openaire.open_science_observatory',
                             'suite5.furniture_enterprise_analytics', 'bluebridge.d4science_spatial_data_repository',
                             'iagos.iagos_data_portal', 'bluebridge.access_to_open_data_platforms',
                             'bluebridge.biodiversity', 'bluebridge.d4science_spatial_data_catalog',
                             'sciences_po.web_panel_sample_service', 'embrc-eric.biobanks',
                             'bluebridge.regional_database_for_fishery_stock_management',
                             'mobile_observation_integration_service.dark_sky_meter_datasource',
                             'bluebridge.protected_area_impact_maps_spatial_data_repository', 'ibceb.eeghub',
                             'cnio.pandrugs', 'meeo.mea_platform', 'lifewatch-eric.arms_otu_unifier',
                             'icos_eric.open_sparql_endpoint_gui', 'aginfra.agris_elastic_index', 'dkrz.wdcc',
                             'icos_eric.stilt_worker', 'ubfzf.repopsi', 'eodc.eo-mqs',
                             'bluebridge.western_central_atlantic_fishery_commission_spatial_data_repository',
                             'icos_eric.open_sparl_endpoint', 'lnec.opencoasts_portal', 'plantnet.ai-geospecies',
                             'openminted.catalogue_of_ancillary_resources',
                             'bluebridge.global_tuna_atlas_spatial_data_repository',
                             'ifremer.argo_floats_data_discovery', 'nilu.actris_data_portal',
                             'sios.sios_data_access_portal', 'dsmz.bacdive__the_bacterial_diversity_metadatabase',
                             'eosc.elsevier.digital_commons', 'eosc.seadatanet.marine_data_viewer',
                             'eosc.esa-int.geoss_web_portal', 'ni4os.brfaa.chembioserver',
                             'ni4os.ukim_fcse.gaussian_api', 'eosc.aginfra.geoanalytics_visualization',
                             'eosc.bluebridge.indian_ocean_tuna_commission_spatial_data_catalog', 'eosc.bineo.cos4env',
                             'eosc.ceric-eric.ceric-data-portal',
                             'ni4os.nsl-ge.digital_repository_of_georgian_scientific_works',
                             'eosc.openminted.catalogue_of_corpora',
                             'eosc.bluebridge.global_record_of_stocks_and_fishery',
                             'eosc.sstir.public_rd_resource_graph_of_AI_in_Shanghai',
                             'eosc.inoe_2000.infra-art_spectral_library', 'eosc.openaire.funder_dashboard',
                             'eosc.beia.farmsustainabl', 'eosc.eosc.cnb-csic.covid-19_structural_hub',
                             'eosc.blue-cloud.discovery_access', 'eosc.ulb-sa.share_it',
                             'eosc.blue-cloud.mei_generator', 'eosc.openaire.open_science_observatory',
                             'eosc.suite5.furniture_enterprise_analytics',
                             'eosc.bluebridge.d4science_spatial_data_repository', 'eosc.iagos.iagos_data_portal',
                             'eosc.bluebridge.access_to_open_data_platforms', 'eosc.bluebridge.biodiversity',
                             'eosc.bluebridge.d4science_spatial_data_catalog',
                             'eosc.sciences_po.web_panel_sample_service', 'eosc.embrc-eric.biobanks',
                             'eosc.bluebridge.regional_database_for_fishery_stock_management',
                             'eosc.mobile_observation_integration_service.dark_sky_meter_datasource',
                             'eosc.bluebridge.protected_area_impact_maps_spatial_data_repository', 'ni4os.ibceb.eeghub',
                             'eosc.cnio.pandrugs', 'eosc.meeo.mea_platform', 'eosc.lifewatch-eric.arms_otu_unifier',
                             'eosc.icos_eric.open_sparql_endpoint_gui', 'eosc.aginfra.agris_elastic_index',
                             'eosc.dkrz.wdcc', 'eosc.icos_eric.stilt_worker', 'eosc.ubfzf.repopsi', 'eosc.eodc.eo-mqs',
                             'eosc.bluebridge.western_central_atlantic_fishery_commission_spatial_data_repository',
                             'eosc.icos_eric.open_sparl_endpoint', 'eosc.lnec.opencoasts_portal',
                             'eosc.plantnet.ai-geospecies', 'eosc.openminted.catalogue_of_ancillary_resources',
                             'eosc.bluebridge.global_tuna_atlas_spatial_data_repository',
                             'eosc.ifremer.argo_floats_data_discovery', 'eosc.nilu.actris_data_portal',
                             'eosc.sios.sios_data_access_portal',
                             'eosc.dsmz.bacdive__the_bacterial_diversity_metadatabase',
                             'collabwith.collabwith_marketplace', 'eosc.collabwith.collabwith_marketplace',
                             'embl-ebi.icr', 'hits.fairdomhub', 'ror-org.ror',
                             'cern.cod', 'awi_bremerhaven.pangaea', 'ceric-eric.ceric-data-portal',
                             'seadatanet.european_directory_of_the_cruise_summary_reports_csr',
                             'cnr_-_isti.isti_open_portal', 'dkrz.wdcc', 'gdansk_tech.most', 'lapp.ossr',
                             'zpid.psycharchives', 'ku_leuven.ku_leuven_rdr', 'sj-ucp.veritati', 'csuc.corardr',
                             'vliz.worms', 'fris.fris', 'unibi-ub.pub', 'icos_eric.data_discovery_and_access_portal',
                             'acdh-ch.arche', 'scipedia.spaosp',
                             'seadatanet.european_directory_of_marine_environmental_research_projects',
                             'seadatanet.european_directory_of_marine_environmental_data_edmed', 'cyfronet.rodbuk',
                             'unipd.rdu', 'seadatanet.seadatanet_cdi', 'ku_leuven.lirias', 'blue-cloud.grsf',
                             'sobigdata.sbdservicesandproducts', 'sobigdata.sbdliteracy', 'sanu.dais', 'fcub.cherry',
                             'ichtm.cer', 'ibiss.ibiss_radar', 'obsparis.padc', 'obsparis.vespa_query_portal',
                             'bbmri-eric.bbmri-eric_crc-cohort', 'bbmri-eric.bbmri-eric_directory',
                             'seadatanet.seadatanet_cdi_ogc_wms',
                             'seadatanet.european_directory_of_the_initial_ocean-observing_systems_edios',
                             'uniwersytet_opolski.bk_uniopole', 'gwdg.textgrid_repository', 'seadatanet.webodv',
                             'seadatanet.seadatanet_cdi_sparql', 'seadatanet.seadatanet_cdi_ogc_wfs',
                             'seadatanet.european_directory_of_marine_organisations_edmo',
                             'lindatclariah-cz.lindatclariah-cz_repository', 'lida.lida_survey_data',
                             'eosc.embl-ebi.icr', 'eosc.hits.fairdomhub', 'eosc.ror-org.ror',
                             'eosc.cern.cod', 'eosc.awi_bremerhaven.pangaea',
                             'eosc.ceric-eric.ceric-data-portal',
                             'eosc.seadatanet.european_directory_of_the_cruise_summary_reports_csr',
                             'eosc.cnr_-_isti.isti_open_portal', 'eosc.dkrz.wdcc', 'eosc.gdansk_tech.most',
                             'eosc.lapp.ossr', 'eosc.zpid.psycharchives', 'eosc.ku_leuven.ku_leuven_rdr',
                             'eosc.sj-ucp.veritati', 'eosc.csuc.corardr', 'eosc.vliz.worms', 'eosc.fris.fris',
                             'eosc.unibi-ub.pub', 'eosc.icos_eric.data_discovery_and_access_portal',
                             'eosc.acdh-ch.arche', 'eosc.scipedia.spaosp',
                             'eosc.seadatanet.european_directory_of_marine_environmental_research_projects',
                             'eosc.seadatanet.european_directory_of_marine_environmental_data_edmed',
                             'eosc.cyfronet.rodbuk', 'eosc.unipd.rdu', 'eosc.seadatanet.seadatanet_cdi',
                             'eosc.ku_leuven.lirias', 'eosc.blue-cloud.grsf', 'eosc.sobigdata.sbdservicesandproducts',
                             'eosc.sobigdata.sbdliteracy', 'ni4os.sanu.dais', 'ni4os.fcub.cherry', 'ni4os.ichtm.cer',
                             'ni4os.ibiss.ibiss_radar', 'eosc.obsparis.padc', 'eosc.obsparis.vespa_query_portal',
                             'eosc.bbmri-eric.bbmri-eric_crc-cohort', 'eosc.bbmri-eric.bbmri-eric_directory',
                             'eosc.seadatanet.seadatanet_cdi_ogc_wms',
                             'eosc.seadatanet.european_directory_of_the_initial_ocean-observing_systems_edios',
                             'eosc.uniwersytet_opolski.bk_uniopole', 'eosc.gwdg.textgrid_repository',
                             'eosc.seadatanet.webodv', 'eosc.seadatanet.seadatanet_cdi_sparql',
                             'eosc.seadatanet.seadatanet_cdi_ogc_wfs',
                             'eosc.seadatanet.european_directory_of_marine_organisations_edmo',
                             'eosc.lindatclariah-cz.lindatclariah-cz_repository', 'eosc.lida.lida_survey_data']
find_instruments_and_equipment = ['terradue.high-resolution_change_monitoring_for_the_alpine_region',
                                  'eosc.terradue.high-resolution_change_monitoring_for_the_alpine_region']
manage_research_data = ['bluebridge.aquaculture_atlas_generation_spatial_data_catalog', 'eudat.b2stage',
                        'openaire.broker', 'eosc.openaire.broker', 'lifewatch-eric.pema_converter',
                        'openaire.technical_support_towards_openaire_compliance',
                        'openaire.validator', 'eosc.openaire.validator',
                        'eosc.openaire.technical_support_towards_openaire_compliance',
                        'dtu.sciencedata', 'incd.sqaaas', 'doabf.prism', 'ubi.tsddp',
                        'openaire.data_provider_dashboard', 'eosc.openaire.data_provider_dashboard',
                        'ictlc.3rd-party_data_security_assessment', 'fzj-inm7.datalad', 'net7.pundit',
                        'expertai.recommender_api', 'eudat.b2note', 'bluebridge.data-driven_atlas_production',
                        'csc-fi.fairdata_services', 'vi-seem.clowder', 'aginfra.data_transformation_service',
                        'cnb-csic.3dbionotes-ws', 'aginfra.semantic_linking_service',
                        'charite_bih_brain_simulation.vre', 'bluebridge.accounting_framework',
                        'openaire.fp7_post-grant_gold_open_access_pilot', 'openminted.consulting_on_licences_for_tdm',
                        'carlzeissm.aper', 'infn.dodasp', 'bluebridge.secure_file_sharing_and_storage',
                        'euro-bioimaging.batchconvert', 'aginfra.ontology_engineering_service', 'olos.olos',
                        'bluebridge.french_tuna_atlas_spatial_data_repository',
                        'european_xfel.european_xfel_metadata_catalogue', 'eosc.lifewatch-eric.pema_converter',
                        'taltechdata.tallinn_university_of_technology_data_repository',
                        'ifremer.envri-fair_marine_essential_ocean_variables_data_broker', 'fairmat.nomad',
                        'blue-cloud.plankton_eov_vlab', 'cessda-eric.cvs', 'blue-cloud.carbon_notebooks',
                        'cesnet.science_mesh_service', 'seadatanet.seadatanet_cdi_ogc_wms', 'athena.lct', 'progedo.qpd',
                        'seadatanet.seadatanet_cdi', 'seadatanet.seadatanet_cdi_sparql',
                        'seadatanet.seadatanet_cdi_ogc_wfs',
                        'eosc.bluebridge.aquaculture_atlas_generation_spatial_data_catalog', 'eosc.eudat.b2stage',
                        'eosc.dtu.sciencedata', 'eosc.incd.sqaaas', 'eosc.doabf.prism', 'eosc.ubi.tsddp',
                        'eosc.ictlc.3rd-party_data_security_assessment', 'eosc.fzj-inm7.datalad', 'eosc.net7.pundit',
                        'eosc.expertai.recommender_api', 'eosc.eudat.b2note',
                        'eosc.bluebridge.data-driven_atlas_production', 'eosc.csc-fi.fairdata_services',
                        'eosc.vi-seem.clowder', 'eosc.aginfra.data_transformation_service',
                        'eosc.cnb-csic.3dbionotes-ws', 'eosc.aginfra.semantic_linking_service',
                        'eosc.charite_bih_brain_simulation.vre', 'eosc.bluebridge.accounting_framework',
                        'eosc.openaire.fp7_post-grant_gold_open_access_pilot',
                        'eosc.openminted.consulting_on_licences_for_tdm', 'eosc.carlzeissm.aper', 'eosc.infn.dodasp',
                        'eosc.bluebridge.secure_file_sharing_and_storage', 'eosc.euro-bioimaging.batchconvert',
                        'eosc.aginfra.ontology_engineering_service', 'eosc.olos.olos',
                        'eosc.bluebridge.french_tuna_atlas_spatial_data_repository',
                        'eosc.european_xfel.european_xfel_metadata_catalogue',
                        'eosc.taltechdata.tallinn_university_of_technology_data_repository',
                        'eosc.ifremer.envri-fair_marine_essential_ocean_variables_data_broker', 'eosc.fairmat.nomad',
                        'eosc.blue-cloud.plankton_eov_vlab', 'eosc.cessda-eric.cvs', 'eosc.blue-cloud.carbon_notebooks',
                        'eosc.cesnet.science_mesh_service', 'eosc.seadatanet.seadatanet_cdi_ogc_wms', 'eosc.athena.lct',
                        'eosc.progedo.qpd', 'eosc.seadatanet.seadatanet_cdi', 'eosc.seadatanet.seadatanet_cdi_sparql',
                        'eosc.seadatanet.seadatanet_cdi_ogc_wfs', 'infn.paas_orchestrator',
                        'ifca-csic.ai4eosc_platform', 'eosc.infn.paas_orchestrator', 'eosc.ifca-csic.ai4eosc_platform',
                        'esrf.visa', 'eosc.esrf.visa', 'nilu.actris_data_portal', 'sios.sios_data_access_portal',
                        'eosc.nilu.actris_data_portal', 'eosc.sios.sios_data_access_portal',
                        'bluebridge.dynamic_reporting', 'bluebridge.nym_framework', 'bluebridge.aquaculture_farming',
                        'bluebridge.data_miner_analytics_service', 'rbi.dariah_science_gateway',
                        'emso_eric.eosc_future_environment_dashboard', 'ukri_-_stfc.idaaas', 'geant.geantargus',
                        'eosc.bluebridge.dynamic_reporting', 'eosc.bluebridge.nym_framework',
                        'eosc.bluebridge.aquaculture_farming', 'eosc.bluebridge.data_miner_analytics_service',
                        'eosc.rbi.dariah_science_gateway', 'eosc.emso_eric.eosc_future_environment_dashboard',
                        'eosc.ukri_-_stfc.idaaas', 'eosc.geant.geantargus', 'bluebridge.support_for_data_publication',
                        'eosc.bluebridge.support_for_data_publication',
                        'bluebridge.french_tuna_atlas_spatial_data_catalog',
                        'bluebridge.aquaculture_atlas_spatial_data_repository',
                        'eosc.bluebridge.french_tuna_atlas_spatial_data_catalog',
                        'eosc.bluebridge.aquaculture_atlas_spatial_data_repository']
process_and_analyze = ['openminted.catalogue_of_tdm_components', 'lifewatch-eric.rvlab_runner', 'desy.pan_notebook',
                       'bluebridge.spatial_data_infrastructure_laboratory_catalog',
                       'eosc.bluebridge.spatial_data_infrastructure_laboratory_catalog',
                       'athena.rolect', 'eosc.athena.rolect', 'grycap.oscar', 'eosc.grycap.oscar',
                       'rasdaman.datacube', 'eosc.rasdaman.datacube', 'bluebridge.bionym', 'eosc.bluebridge.bionym',
                       'asgc.icomcot_tsunami_wave_propagation_simulation_portal',
                       'wenmr.fanten_finding_anisotropy_tensor', 'eosc.wenmr.fanten_finding_anisotropy_tensor',
                       'eosc.asgc.icomcot_tsunami_wave_propagation_simulation_portal',
                       'openminted.catalogue_of_tdm_applications', 'eosc.openminted.catalogue_of_tdm_applications',
                       'bluebridge.global_tuna_atlas_spatial_data_catalog', 'icos_eric.stilt_viewer',
                       'eosc.bluebridge.global_tuna_atlas_spatial_data_catalog', 'eosc.icos_eric.stilt_viewer',
                       'bluebridge.dynamic_reporting', 'egi-fed.egi_replay', 'icos_eric.icos_jupyter_hub',
                       'bluebridge.scalable_data_mining', 'infn.fgsg_science_software_on_demand', 'brfaa.dreamm',
                       'bluebridge.nym_framework', 'openminted.support_and_training', 'bluebridge.aquaculture_farming',
                       'compbiomed.software_hub', 'brfaa.feprepare', 'embimos.mecoda',
                       'bluebridge.data_miner_analytics_service', 'aginfra.chart_visualization',
                       'edelweiss_connect.lazar', 'rbi.dariah_science_gateway', 'uob-rcub.repol', 'ni4os.uob-rcub.repol',
                       'openminted.builder_of_tdm_applications', 'openrisknet.e-infrastructure', 'eodc.openeo_platform',
                       'openrisknet.lazar', 'ukim_fcse.schrodinger_api', 'bluebridge.stock_assessment_support',
                       'blue-cloud.oceanpatterns', 'data_revenue.py-muvr', 'bluebridge.species_modeling',
                       'bluebridge.data_warehousing_facilities', 'blue-cloud.storm_ssi',
                       'openminted.tdm_applications_executor', 'desy.desy_visa',
                       'bluebridge.data_miner_analytics_prototype_service', 'cnb-csic.covid-19_structural_hub',
                       'brfaa.ingredio', 'earthwatch.mics_measuring_the_impact_of_citizen_science',
                       'bluebridge.western_central_atlantic_fishery_commission_spatial_data_catalog',
                       'bluebridge.spatial_planning', 'egi-fed.fedearthdata', 'blue-cloud.phytoplankton_eovs',
                       'lifewatch-eric.occurrences_datacube_builder', 'university_of_sussex.lhc',
                       'blue-cloud.blue-cloud_vre', 'openaire.openapc', 'norce.openlab_drilling',
                       'sethsoftware.ai4pheno', 'upf.multilingual_corpus_of_survey_questionnaires',
                       'ifca-csic.imagine_platform', 'blue-cloud.jupyter_hub', 'blue-cloud.plankton_interact',
                       'blue-cloud.plankton_genomics_vlab', 'blue-cloud.mei_vlab', 'blue-cloud.oceanregimes',
                       'rb.sentiment_analysis_api__text_analytics_api', 'ill.biosas_jupyter_notebook',
                       'blue-cloud.zooplankton_eovs', 'blue-cloud.analytics_engine', 'blue-cloud.fisheries_atlas',
                       'blue-cloud.rstudio', 'adv_met.easy-amanida', 'emso_eric.eosc_future_environment_dashboard',
                       'ukri_-_stfc.idaaas', 'geant.geantargus', 'dynaikon.fcc', 'geant.geanttimemap',
                       'psi.panet_ontology_service', 'leaena.leaena', 'ibergrid.fair_eva',
                       'eosc.openminted.catalogue_of_tdm_components', 'eosc.lifewatch-eric.rvlab_runner',
                       'eosc.desy.pan_notebook', 'eosc.bluebridge.dynamic_reporting', 'eosc.egi-fed.egi_replay',
                       'eosc.icos_eric.icos_jupyter_hub', 'eosc.bluebridge.scalable_data_mining',
                       'eosc.infn.fgsg_science_software_on_demand', 'ni4os.brfaa.dreamm',
                       'eosc.bluebridge.nym_framework', 'eosc.openminted.support_and_training',
                       'eosc.bluebridge.aquaculture_farming', 'eosc.compbiomed.software_hub', 'ni4os.brfaa.feprepare',
                       'eosc.embimos.mecoda', 'eosc.bluebridge.data_miner_analytics_service',
                       'eosc.aginfra.chart_visualization', 'eosc.edelweiss_connect.lazar',
                       'eosc.rbi.dariah_science_gateway', 'eosc.openminted.builder_of_tdm_applications',
                       'eosc.openrisknet.e-infrastructure', 'eosc.eodc.openeo_platform', 'eosc.openrisknet.lazar',
                       'ni4os.ukim_fcse.schrodinger_api', 'eosc.bluebridge.stock_assessment_support',
                       'eosc.blue-cloud.oceanpatterns', 'eosc.data_revenue.py-muvr', 'eosc.bluebridge.species_modeling',
                       'eosc.bluebridge.data_warehousing_facilities', 'eosc.blue-cloud.storm_ssi',
                       'eosc.openminted.tdm_applications_executor', 'eosc.desy.desy_visa',
                       'eosc.bluebridge.data_miner_analytics_prototype_service',
                       'eosc.cnb-csic.covid-19_structural_hub', 'ni4os.brfaa.ingredio',
                       'eosc.earthwatch.mics_measuring_the_impact_of_citizen_science',
                       'eosc.bluebridge.western_central_atlantic_fishery_commission_spatial_data_catalog',
                       'eosc.bluebridge.spatial_planning', 'eosc.egi-fed.fedearthdata',
                       'eosc.blue-cloud.phytoplankton_eovs', 'eosc.lifewatch-eric.occurrences_datacube_builder',
                       'eosc.university_of_sussex.lhc', 'eosc.blue-cloud.blue-cloud_vre', 'eosc.openaire.openapc',
                       'eosc.norce.openlab_drilling', 'eosc.sethsoftware.ai4pheno',
                       'eosc.upf.multilingual_corpus_of_survey_questionnaires', 'eosc.ifca-csic.imagine_platform',
                       'eosc.blue-cloud.jupyter_hub', 'eosc.blue-cloud.plankton_interact',
                       'eosc.blue-cloud.plankton_genomics_vlab', 'eosc.blue-cloud.mei_vlab',
                       'eosc.blue-cloud.oceanregimes', 'eosc.rb.sentiment_analysis_api__text_analytics_api',
                       'eosc.ill.biosas_jupyter_notebook', 'eosc.blue-cloud.zooplankton_eovs',
                       'eosc.blue-cloud.analytics_engine', 'eosc.blue-cloud.fisheries_atlas', 'eosc.blue-cloud.rstudio',
                       'eosc.adv_met.easy-amanida', 'eosc.emso_eric.eosc_future_environment_dashboard',
                       'eosc.ukri_-_stfc.idaaas', 'eosc.geant.geantargus', 'eosc.dynaikon.fcc',
                       'eosc.geant.geanttimemap', 'eosc.psi.panet_ontology_service', 'eosc.leaena.leaena',
                       'eosc.ibergrid.fair_eva', 'grena.gcloudge', 'incd.application_lifecycle_enabler_4_cloud',
                       'openrisknet.squonk_computational_notebook', 'smartsmear.new_particle_formation_event_analysis',
                       'ni4os.grena.gcloudge', 'eosc.incd.application_lifecycle_enabler_4_cloud',
                       'eosc.openrisknet.squonk_computational_notebook',
                       'eosc.smartsmear.new_particle_formation_event_analysis', 'openrisknet.jaqpot',
                       'edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                       'epos.envri_catalog_of_services', 'edelweiss_connect.jaqpot', 'eosc.openrisknet.jaqpot',
                       'eosc.edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                       'eosc.epos.envri_catalog_of_services', 'eosc.edelweiss_connect.jaqpot', 'brfaa.chembioserver',
                       'blue-cloud.mei_generator', 'bluebridge.d4science_spatial_data_catalog',
                       'bluebridge.regional_database_for_fishery_stock_management', 'icos_eric.stilt_worker',
                       'ni4os.brfaa.chembioserver', 'eosc.blue-cloud.mei_generator',
                       'eosc.bluebridge.d4science_spatial_data_catalog',
                       'eosc.bluebridge.regional_database_for_fishery_stock_management', 'eosc.icos_eric.stilt_worker',
                       'blue-cloud.plankton_eov_vlab', 'eosc.blue-cloud.plankton_eov_vlab']
publish_research_outputs = ['bluebridge.support_for_data_publication', 'openminted.corpus_builder_for_scholarly_works',
                            'ierek.ierek', 'eosc.ierek.ierek',
                            'ibergrid.sqaaas', 'eosc.bluebridge.support_for_data_publication',
                            'bluebridge.software_repository', 'eosc.bluebridge.software_repository',
                            'eosc.openminted.corpus_builder_for_scholarly_works', 'eosc.ibergrid.sqaaas',
                            'aginfra.geoanalytics_visualization', 'ceric-eric.ceric-data-portal',
                            'eosc.aginfra.geoanalytics_visualization', 'eosc.ceric-eric.ceric-data-portal',
                            'aginfra.ontology_engineering_service', 'eosc.aginfra.ontology_engineering_service',
                            'blue-cloud.blue-cloud_vre', 'eosc.blue-cloud.blue-cloud_vre',
                            'bluebridge.collaboration_framework', 'eosc.bluebridge.collaboration_framework']
######################################## PREDEFINED MARKETPLACE LOCATION VALUES ########################################

##################################################### FUNCTIONS ########################################################
def datasource_migration(directory):
    for file in os.listdir(directory + datasourceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + datasourceFolder + file, 'r') as json_file:
                json_data = migrate_datasources(json_file, isVersion)
                # write to file
                with open(directory + datasourceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + datasourceFolder + file)
            for versionFile in versionFiles:
                with open(directory + datasourceFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate_datasources(json_file, isVersion)
                    # write to file
                    with open(directory + datasourceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def other_resources_migration(directory):
    for otherFolder in otherFolders:
        for file in os.listdir(args.path + otherFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + otherFolder + file, 'r') as json_file:
                    json_data = migrate_other_resources(json_file, otherFolder.replace("/", ""), isVersion)
                    # write to file
                    with open(directory + otherFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + otherFolder + file)
                for versionFile in versionFiles:
                    with open(directory + otherFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_other_resources(json_file, otherFolder.replace("/", ""), isVersion)
                        # write to file
                        with open(directory + otherFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def service_migration(directory):
    for file in os.listdir(directory + serviceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + serviceFolder + file, 'r') as json_file:
                json_data = migrate_services(json_file, isVersion)
                # write to file
                with open(directory + serviceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + serviceFolder + file)
            for versionFile in versionFiles:
                with open(directory + serviceFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate_services(json_file, isVersion)
                    # write to file
                    with open(directory + serviceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def migrate_datasources(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()
    datasource = root.find('{http://einfracentral.eu}datasource')

    # prefill DatasourceIDs to migrate Service's serviceCategory later
    if not isVersion:
        datasourceId = datasource.find('{http://einfracentral.eu}id')
        if datasourceId is not None:
            if datasourceId.text not in datasourceIds:
                datasourceIds.append(datasourceId.text)

    # alternativeIdentifiers
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            for alternativeIdentifier in alternativeIdentifiers:
                alternativeIdentifierValue = alternativeIdentifier.find('{http://einfracentral.eu}value')
                if alternativeIdentifierValue is not None:
                    originalOpenAIREId = ET.Element("tns:originalOpenAIREId")
                    originalOpenAIREId.text = alternativeIdentifierValue.text
                    tree.append(originalOpenAIREId)
                    break
            identifiers.remove(alternativeIdentifiers)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def migrate_other_resources(json_file, resourceType, isVersion):
    global resource
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    match resourceType:
        case "provider":
            resource = root.find('{http://einfracentral.eu}provider')
        case "training_resource":
            resource = root.find('{http://einfracentral.eu}trainingResource')
        case "interoperability_record":
            resource = root.find('{http://einfracentral.eu}interoperabilityRecord')
    migrate_alternative_identifiers(root, resource)

    root.write(resourceType + '-output.xml')
    with open(resourceType + "-output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def migrate_services(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    service = root.find('{http://einfracentral.eu}service')
    id = service.find('{http://einfracentral.eu}id')

    # serviceCategory field
    # existingServiceCategories = service.find('{http://einfracentral.eu}serviceCategories')
    # if existingServiceCategories is not None:
    #     service.remove(existingServiceCategories)

    serviceCategories = ET.Element("tns:serviceCategories")
    serviceCategory = ET.Element("tns:serviceCategory")
    if id in datasourceIds:
        serviceCategory.text = "service_category-data_source"
    else:
        categories = service.find('{http://einfracentral.eu}categories')
        if categories is not None:
            for category in categories:
                if category is not None:
                    categoryEntry = category.find('{http://einfracentral.eu}category')
                    if categoryEntry is not None:
                        if categoryEntry.text == "category-access_physical_and_eInfrastructures-compute":
                            serviceCategory.text = "service_category-compute"
                            break
                        elif categoryEntry.text == "category-access_physical_and_eInfrastructures-data_storage":
                            serviceCategory.text = "service_category-storage"
                            break
    if serviceCategory.text is None:
        serviceCategory.text = "service_category-other"
    serviceCategories.append(serviceCategory)
    service.append(serviceCategories)

    # marketplaceLocation field / remove ResourceExtras -> researchCategories
    # existingMarketplaceLocations = service.find('{http://einfracentral.eu}marketplaceLocations')
    # if existingMarketplaceLocations is not None:
    #     service.remove(existingMarketplaceLocations)

    marketplaceLocations = ET.Element("tns:marketplaceLocations")
    marketplaceLocation = ET.Element("tns:marketplaceLocation")
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    entered = False
    if resourceExtras is not None:
        researchCategories = resourceExtras.find('{http://einfracentral.eu}researchCategories')
        if researchCategories is not None:
            for researchCategory in researchCategories:
                if researchCategory is not None:
                    entered = True
                    if researchCategory.text == "research_category-dro" or \
                            researchCategory.text == "research_category-dro ":  # 4 malformed entries
                        marketplaceLocation.text = "marketplace_location-discover_research_outputs"
                    elif researchCategory.text == "research_category-pro":
                        marketplaceLocation.text = "marketplace_location-publish_research_outputs"
                    elif researchCategory.text == "research_category-pa":
                        marketplaceLocation.text = "marketplace_location-process_and_analyze"
                    elif researchCategory.text == "research_category-acr":
                        marketplaceLocation.text = "marketplace_location-access_computing_and_storage_resources"
                    elif researchCategory.text == "research_category-fie":
                        marketplaceLocation.text = "marketplace_location-find_instruments_and_equipment"
                    elif researchCategory.text == "research_category-atm":
                        marketplaceLocation.text = "marketplace_location-access_training_material"
                    elif researchCategory.text == "research_category-ari":
                        marketplaceLocation.text = "marketplace_location-access_research_infrastructures"
                    elif researchCategory.text == "research_category-mrd":
                        marketplaceLocation.text = "marketplace_location-manage_research_data"
                    marketplaceLocations.append(marketplaceLocation)
            resourceExtras.remove(researchCategories)
    if not entered:
        choose_predefined_marketplace_locations(id.text, marketplaceLocations)
    service.append(marketplaceLocations)

    # horizontalService / remove ResourceExtras -> horizontalService
    # existingHorizontalServiceInsideService = service.find('{http://einfracentral.eu}horizontalService')
    # if existingHorizontalServiceInsideService is not None:
    #     service.remove(existingHorizontalServiceInsideService)

    horizontalService = ET.Element("tns:horizontalService")
    if resourceExtras is not None:
        existingHorizontalService = resourceExtras.find('{http://einfracentral.eu}horizontalService')
        if existingHorizontalService is not None:
            horizontalService.text = existingHorizontalService.text
            resourceExtras.remove(existingHorizontalService)
    service.append(horizontalService)

    # alternativeIdentifiers
    migrate_alternative_identifiers(root, service)

    root.write('output.xml')
    with open("../EOSCProfilev4.08_M30Release/output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def migrate_alternative_identifiers(root, resource):
    # existingalternativeIdentifiers = resource.find('{http://einfracentral.eu}alternativeIdentifiers')
    # if existingalternativeIdentifiers is not None:
    #     resource.remove(existingalternativeIdentifiers)

    # alternativeIdentifiers
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            for alternativeIdentifier in alternativeIdentifiers:
                if alternativeIdentifier is not None:
                    alternativeIdentifierType = alternativeIdentifier.find('{http://einfracentral.eu}type')
                    if alternativeIdentifierType.text == 'PID':
                        alternativeIdentifierType.text = 'EOSC PID'
        resource.append(alternativeIdentifiers.__copy__())
        identifiers.remove(alternativeIdentifiers)


def choose_predefined_marketplace_locations(id, marketplaceLocations):
    if id in discover_research_outputs:
        fill_predefined_marketplace_locations(marketplaceLocations, 'marketplace_location-discover_research_outputs')
    if id in process_and_analyze:
        fill_predefined_marketplace_locations(marketplaceLocations, 'marketplace_location-process_and_analyze')
    if id in manage_research_data:
        fill_predefined_marketplace_locations(marketplaceLocations, 'marketplace_location-manage_research_data')
    if id in access_computing_and_storage_resources:
        fill_predefined_marketplace_locations(marketplaceLocations,
                                              'marketplace_location-access_computing_and_storage_resources')
    if id in access_research_infrastructures:
        fill_predefined_marketplace_locations(marketplaceLocations,
                                              'marketplace_location-access_research_infrastructures')
    if id in publish_research_outputs:
        fill_predefined_marketplace_locations(marketplaceLocations, 'marketplace_location-publish_research_outputs')
    if id in access_training_material:
        fill_predefined_marketplace_locations(marketplaceLocations, 'marketplace_location-access_training_material')
    if id in find_instruments_and_equipment:
        fill_predefined_marketplace_locations(marketplaceLocations,
                                              'marketplace_location-find_instruments_and_equipment')


def fill_predefined_marketplace_locations(marketplaceLocations, vocabulary):
    marketplaceLocation = ET.Element("tns:marketplaceLocation")
    marketplaceLocation.text = vocabulary
    marketplaceLocations.append(marketplaceLocation)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
datasource_migration(args.path)
other_resources_migration(args.path)
service_migration(args.path)
################################################## ANOTHER RAPHAEL #####################################################