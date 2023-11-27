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
catalogueFolder = '/catalogue/'
otherFolders = ['/provider/', '/training_resource/', '/interoperability_record/']
###################################################### GLOBALS #########################################################

######################################## PREDEFINED MARKETPLACE LOCATION VALUES ########################################
access_computing_and_storage_resources = ['grena.gcloudge', 'geant.l3vpn', 'openrisknet.squonk_computational_notebook',
                                          'desy.pan_faas', 'brfaa.nanocrystal', 'ukim_fcse.finki_cloud',
                                          'edelweiss_connect.squonk_computational_notebook', 'desy.pan_data',
                                          'northern_data_cloud_services.northern_data_cloud_services',
                                          'ipb.paradox-iv_cluster', 'smartsmear.new_particle_formation_event_analysis',
                                          'grycap.oscar', 'csc-fi.puhti', 'cineca.iscra', 'infn.paas_orchestrator',
                                          'ifca-csic.ai4eosc_platform', 'uot.ur', 'vu.itoac', 'geant.ocregoogle',
                                          'geant.ocreexoscale', 'tum-net.slices-vpostum', 'geant.ocreorange',
                                          'exoscale.european_cloud_hosting', 'ni4os.grena.gcloudge', 'eosc.geant.l3vpn',
                                          'eosc.openrisknet.squonk_computational_notebook', 'eosc.desy.pan_faas',
                                          'ni4os.brfaa.nanocrystal', 'ni4os.ukim_fcse.finki_cloud',
                                          'eosc.edelweiss_connect.squonk_computational_notebook', 'eosc.desy.pan_data',
                                          'eosc.northern_data_cloud_services.northern_data_cloud_services',
                                          'ni4os.ipb.paradox-iv_cluster',
                                          'eosc.smartsmear.new_particle_formation_event_analysis', 'eosc.grycap.oscar',
                                          'eosc.csc-fi.puhti', 'eosc.cineca.iscra', 'eosc.infn.paas_orchestrator',
                                          'eosc.ifca-csic.ai4eosc_platform', 'eosc-nordic.uot.ur',
                                          'eosc-nordic.vu.itoac', 'eosc.geant.ocregoogle', 'eosc.geant.ocreexoscale',
                                          'eosc.tum-net.slices-vpostum', 'eosc.geant.ocreorange',
                                          'eosc.exoscale.european_cloud_hosting',
                                          'sixsq.snap-based_jupyter_notebook_for_eo_exploration',
                                          'openminted.builder_of_tdm_applications', 'geant.geant_cloud_flow',
                                          'geant.ocrecsipiemonte', 'geant.ocreaws', 'geant.ocre100', 'geant.ocreibm',
                                          'geant.ocrecloudferro', 'geant.ocreoracle', 'geant.ocreovhcloud',
                                          'geant.ocreorangebusiness', 'geant.ocreazure',
                                          'eosc.sixsq.snap-based_jupyter_notebook_for_eo_exploration',
                                          'eosc.openminted.builder_of_tdm_applications', 'eosc.geant.geant_cloud_flow',
                                          'eosc.geant.ocrecsipiemonte', 'eosc.geant.ocreaws', 'eosc.geant.ocre100',
                                          'eosc.geant.ocreibm', 'eosc.geant.ocrecloudferro', 'eosc.geant.ocreoracle',
                                          'eosc.geant.ocreovhcloud', 'eosc.geant.ocreorangebusiness',
                                          'eosc.geant.ocreazure']
access_research_infrastructures = ['openrisknet.jaqpot', 'epos.envri_catalog_of_services', 'grnet.ni4os-europe_login',
                                   'geant.geant_sandbox resource profile', 'esrf.visa',
                                   'geant.ocre_cloud services by setcor', 'geant.ocre_cloud services by t-systems',
                                   'geant.ocre_cloud services by vancis', 'geant.ocre_cloud services by sentia',
                                   'geant.ocre_cloud services by proact', 'geant.ocre_cloud services by cloud and heat',
                                   'geant.ocre_cloud services by x-ion', 'ess_eric.ess_labs', 'geant.ocrecleura',
                                   'geant.ocrecomtrade', 'operas.vera', 'geant.ocrecloudsigma', 'geant.ocrecsipiemonte',
                                   'geant.ocreaws', 'geant.ocre100', 'geant.ocreequinix', 'geant.ocreionos',
                                   'geant.ocreibm', 'geant.ocrecloudferro', 'geant.ocreoracle', 'geant.ocreovhcloud',
                                   'eosc.openrisknet.jaqpot', 'eosc.epos.envri_catalog_of_services',
                                   'ni4os.grnet.ni4os-europe_login', 'eosc.geant.geant_sandbox resource profile',
                                   'eosc.esrf.visa', 'eosc.geant.ocre_cloud services by setcor',
                                   'eosc.geant.ocre_cloud services by t-systems',
                                   'eosc.geant.ocre_cloud services by vancis',
                                   'eosc.geant.ocre_cloud services by sentia',
                                   'eosc.geant.ocre_cloud services by proact',
                                   'eosc.geant.ocre_cloud services by cloud and heat',
                                   'eosc.geant.ocre_cloud services by x-ion', 'eosc.ess_eric.ess_labs',
                                   'eosc.geant.ocrecleura', 'eosc.geant.ocrecomtrade', 'eosc.operas.vera',
                                   'eosc.geant.ocrecloudsigma', 'eosc.geant.ocrecsipiemonte', 'eosc.geant.ocreaws',
                                   'eosc.geant.ocre100', 'eosc.geant.ocreequinix', 'eosc.geant.ocreionos',
                                   'eosc.geant.ocreibm', 'eosc.geant.ocrecloudferro', 'eosc.geant.ocreoracle',
                                   'eosc.geant.ocreovhcloud', 'infn.indigo_identity_and_access_management',
                                   'bluebridge.accounting_framework', 'eosc.infn.indigo_identity_and_access_management',
                                   'eosc.bluebridge.accounting_framework']
access_training_material = ['e-cam.e-cam_online_training_portal',
                            'eosc-dih.piloting_and_co-design_of_the_business_pilots',
                            'compbiomed.compbiomed_training_portal', 'hzdr.pan-trainingeu', 'ess.pan-learning-org',
                            'psnc.learneosc-synergy', 'eosc.e-cam.e-cam_online_training_portal',
                            'eosc.eosc-dih.piloting_and_co-design_of_the_business_pilots',
                            'eosc.compbiomed.compbiomed_training_portal', 'eosc.hzdr.pan-trainingeu',
                            'eosc.ess.pan-learning-org', 'eosc.psnc.learneosc-synergy',
                            'openminted.support_and_training', 'compbiomed.software_hub',
                            'openminted.catalogue_of_ancillary_resources', 'bluebridge.scientific_training_environment',
                            'openaire.openplato', 'eosc.openminted.support_and_training',
                            'eosc.compbiomed.software_hub', 'eosc.openminted.catalogue_of_ancillary_resources',
                            'eosc.bluebridge.scientific_training_environment', 'eosc.openaire.openplato']
build_analysis_environment = ['incd.sqaaas',
                              'edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                              'edelweiss_connect.jaqpot', 'bluebridge.software_integration_support',
                              'incd.application_lifecycle_enabler_4_cloud',
                              'sixsq.snap-based_jupyter_notebook_for_eo_exploration', 'expertai.recommender_api',
                              'infn.indigo_identity_and_access_management', 'csc-fi.fairdata_services',
                              'vecma.vecma_vvuq_toolkit_vecmatk', 'lifewatch-eric.arms_otu_unifier',
                              'euro-bioimaging.batchconvert', 'ipb.simple_storage_service',
                              'rolos.machine_intelligence_platfrom_for_research', 'geant.edupert',
                              'ifca-csic.imagine_platform', 'geant.ocreorangebusiness', 'geant.ocreazure',
                              'geant.geanttimemap', 'ekt.nephos', 'leaena.leaena', 'eosc.incd.sqaaas',
                              'eosc.edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                              'eosc.edelweiss_connect.jaqpot', 'eosc.bluebridge.software_integration_support',
                              'eosc.incd.application_lifecycle_enabler_4_cloud',
                              'eosc.sixsq.snap-based_jupyter_notebook_for_eo_exploration',
                              'eosc.expertai.recommender_api', 'eosc.infn.indigo_identity_and_access_management',
                              'eosc.csc-fi.fairdata_services', 'eosc.vecma.vecma_vvuq_toolkit_vecmatk',
                              'eosc.lifewatch-eric.arms_otu_unifier', 'eosc.euro-bioimaging.batchconvert',
                              'ni4os.ipb.simple_storage_service',
                              'eosc.rolos.machine_intelligence_platfrom_for_research', 'eosc.geant.edupert',
                              'eosc.ifca-csic.imagine_platform', 'eosc.geant.ocreorangebusiness',
                              'eosc.geant.ocreazure', 'eosc.geant.geanttimemap', 'eosc.ekt.nephos',
                              'eosc.leaena.leaena', 'grena.gcloudge', 'eudat.b2stage', 'bluebridge.dynamic_reporting',
                              'egi-fed.egi_replay', 'bluebridge.scalable_data_mining', 'bluebridge.aquaculture_farming',
                              'brfaa.feprepare', 'geant.l3vpn', 'ictlc.3rd-party_data_security_assessment',
                              'aginfra.chart_visualization', 'fzj-inm7.datalad', 'rbi.dariah_science_gateway',
                              'openaire.funder_dashboard', 'desy.pan_faas', 'eodc.openeo_platform',
                              'bluebridge.stock_assessment_support', 'eodc.eo-mqs',
                              'bluebridge.secure_file_sharing_and_storage', 'egi-fed.egi_software_distribution',
                              'brfaa.ingredio', 'lifewatch-eric.pema_converter', 'bluebridge.bionym',
                              'komanord.guardomic', 'blue-cloud.rstudio', 'geant.ocreexoscale',
                              'cesnet.science_mesh_service', 'tum-net.slices-vpostum',
                              'seadatanet.seadatanet_cdi_ogc_wfs', 'ni4os.grena.gcloudge', 'eosc.eudat.b2stage',
                              'eosc.bluebridge.dynamic_reporting', 'eosc.egi-fed.egi_replay',
                              'eosc.bluebridge.scalable_data_mining', 'eosc.bluebridge.aquaculture_farming',
                              'ni4os.brfaa.feprepare', 'eosc.geant.l3vpn',
                              'eosc.ictlc.3rd-party_data_security_assessment', 'eosc.aginfra.chart_visualization',
                              'eosc.fzj-inm7.datalad', 'eosc.rbi.dariah_science_gateway',
                              'eosc.openaire.funder_dashboard', 'eosc.desy.pan_faas', 'eosc.eodc.openeo_platform',
                              'eosc.bluebridge.stock_assessment_support', 'eosc.eodc.eo-mqs',
                              'eosc.bluebridge.secure_file_sharing_and_storage',
                              'eosc.egi-fed.egi_software_distribution', 'ni4os.brfaa.ingredio',
                              'eosc.lifewatch-eric.pema_converter', 'eosc.bluebridge.bionym', 'eosc.komanord.guardomic',
                              'eosc.blue-cloud.rstudio', 'eosc.geant.ocreexoscale', 'eosc.cesnet.science_mesh_service',
                              'eosc.tum-net.slices-vpostum', 'eosc.seadatanet.seadatanet_cdi_ogc_wfs']
discover_research_outputs = ['elsevier.digital_commons', 'seadatanet.marine_data_viewer', 'esa-int.geoss_web_portal',
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
                             'embrc-eric.biobanks', 'bluebridge.regional_database_for_fishery_stock_management',
                             'mobile_observation_integration_service.dark_sky_meter_datasource',
                             'bluebridge.protected_area_impact_maps_spatial_data_repository', 'ibceb.eeghub',
                             'cnio.pandrugs', 'meeo.mea_platform', 'icos_eric.open_sparql_endpoint_gui',
                             'aginfra.agris_elastic_index', 'dkrz.wdcc', 'icos_eric.stilt_worker', 'ubfzf.repopsi',
                             'eodc.eo-mqs',
                             'bluebridge.western_central_atlantic_fishery_commission_spatial_data_repository',
                             'icos_eric.open_sparl_endpoint', 'lnec.opencoasts_portal', 'plantnet.ai-geospecies',
                             'openminted.catalogue_of_ancillary_resources',
                             'bluebridge.global_tuna_atlas_spatial_data_repository',
                             'bluebridge.collaboration_framework', 'ehri.conny_kristel_fellowship_programme',
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
                             'eosc.bluebridge.d4science_spatial_data_catalog', 'eosc.embrc-eric.biobanks',
                             'eosc.bluebridge.regional_database_for_fishery_stock_management',
                             'eosc.mobile_observation_integration_service.dark_sky_meter_datasource',
                             'eosc.bluebridge.protected_area_impact_maps_spatial_data_repository', 'ni4os.ibceb.eeghub',
                             'eosc.cnio.pandrugs', 'eosc.meeo.mea_platform', 'eosc.icos_eric.open_sparql_endpoint_gui',
                             'eosc.aginfra.agris_elastic_index', 'eosc.dkrz.wdcc', 'eosc.icos_eric.stilt_worker',
                             'eosc.ubfzf.repopsi', 'eosc.eodc.eo-mqs',
                             'eosc.bluebridge.western_central_atlantic_fishery_commission_spatial_data_repository',
                             'eosc.icos_eric.open_sparl_endpoint', 'eosc.lnec.opencoasts_portal',
                             'eosc.plantnet.ai-geospecies', 'eosc.openminted.catalogue_of_ancillary_resources',
                             'eosc.bluebridge.global_tuna_atlas_spatial_data_repository',
                             'eosc.bluebridge.collaboration_framework', 'eosc.ehri.conny_kristel_fellowship_programme',
                             'eosc.ifremer.argo_floats_data_discovery', 'eosc.nilu.actris_data_portal',
                             'eosc.sios.sios_data_access_portal',
                             'eosc.dsmz.bacdive__the_bacterial_diversity_metadatabase',
                             'collabwith.collabwith_marketplace', 'ierek.ierek', 'geant.geanttimemap',
                             'eosc.collabwith.collabwith_marketplace', 'eosc.ierek.ierek', 'eosc.geant.geanttimemap',
                             'eosc.csuc.corardr', 'eosc.ku_leuven.lirias', 'seadatanet.seadatanet_cdi',
                             'sobigdata.sbdliteracy', 'sanu.dais', 'eosc.obsparis.padc',
                             'seadatanet.european_directory_of_the_initial_ocean-observing_systems_edios',
                             'lida.lida_survey_data', 'eosc.acdh-ch.arche', 'bbmri-eric.bbmri-eric_directory',
                             'vliz.worms', 'eosc.zpid.psycharchives', 'lapp.ossr',
                             'eosc.seadatanet.european_directory_of_marine_environmental_data_edmed',
                             'eosc.seadatanet.seadatanet_cdi', 'eosc.seadatanet.seadatanet_cdi_ogc_wms',
                             'ni4os.fcub.cherry', 'seadatanet.european_directory_of_marine_environmental_data_edmed',
                             'lindatclariah-cz.lindatclariah-cz_repository', 'eosc.cnr_-_isti.isti_open_portal',
                             'ror-org.ror', 'cnr_-_isti.isti_open_portal', 'blue-cloud.grsf',
                             'eosc.gwdg.textgrid_repository', 'eosc.scipedia.spaosp', 'eosc.gdansk_tech.most',
                             'eosc.unibi-ub.pub', 'eosc.icos_eric.data_discovery_and_access_portal', 'obsparis.padc',
                             'seadatanet.seadatanet_cdi_ogc_wfs', 'hits.fairdomhub', 'fris.fris', 'cern.cod',
                             'unibi-ub.pub', 'eosc.vliz.worms', 'bbmri-eric.bbmri-eric_crc-cohort',
                             'eosc.seadatanet.european_directory_of_marine_environmental_research_projects',
                             'eosc.obsparis.vespa_query_portal', 'ni4os.ichtm.cer',
                             'eosc.uniwersytet_opolski.bk_uniopole', 'eosc.ku_leuven.ku_leuven_rdr',
                             'uniwersytet_opolski.bk_uniopole', 'eosc.bbmri-eric.bbmri-eric_crc-cohort',
                             'eosc.lida.lida_survey_data', 'embl-ebi.icr',
                             'eosc.seadatanet.european_directory_of_the_cruise_summary_reports_csr', 'ichtm.cer',
                             'eosc.hits.fairdomhub', 'eosc.seadatanet.webodv',
                             'eosc.seadatanet.european_directory_of_the_initial_ocean-observing_systems_edios',
                             'obsparis.vespa_query_portal', 'ku_leuven.lirias',
                             'eosc.seadatanet.european_directory_of_marine_organisations_edmo',
                             'seadatanet.seadatanet_cdi_ogc_wms', 'seadatanet.webodv', 'eosc.awi_bremerhaven.pangaea',
                             'icos_eric.data_discovery_and_access_portal', 'eosc.sobigdata.sbdliteracy',
                             'acdh-ch.arche', 'eosc.lapp.ossr', 'eosc.seadatanet.seadatanet_cdi_sparql',
                             'eosc.cyfronet.rodbuk', 'zpid.psycharchives', 'eosc.fris.fris', 'csuc.corardr',
                             'eosc.sj-ucp.veritati', 'eosc.blue-cloud.grsf', 'gdansk_tech.most', 'fcub.cherry',
                             'eosc.lindatclariah-cz.lindatclariah-cz_repository', 'ni4os.sanu.dais',
                             'seadatanet.seadatanet_cdi_sparql', 'eosc.embl-ebi.icr',
                             'eosc.bbmri-eric.bbmri-eric_directory', 'awi_bremerhaven.pangaea',
                             'gwdg.textgrid_repository', 'cyfronet.rodbuk', 'sj-ucp.veritati', 'eosc.ror-org.ror',
                             'seadatanet.european_directory_of_marine_environmental_research_projects',
                             'seadatanet.european_directory_of_marine_organisations_edmo', 'ni4os.ibiss.ibiss_radar',
                             'eosc.seadatanet.seadatanet_cdi_ogc_wfs', 'sobigdata.sbdservicesandproducts',
                             'eosc.sobigdata.sbdservicesandproducts', 'scipedia.spaosp', 'ibiss.ibiss_radar',
                             'ku_leuven.ku_leuven_rdr', 'unipd.rdu',
                             'seadatanet.european_directory_of_the_cruise_summary_reports_csr', 'eosc.unipd.rdu',
                             'eosc.cern.cod']
explore_other_research_catalogues = ['collabwith.collabwith_marketplace', 'geant.wifimon',
                                     'eosc.collabwith.collabwith_marketplace', 'eosc.geant.wifimon',
                                     'epos.envri_catalog_of_services', 'compbiomed.compbiomed_training_portal',
                                     'university_of_sussex.lhc', 'eosc.epos.envri_catalog_of_services',
                                     'eosc.compbiomed.compbiomed_training_portal', 'eosc.university_of_sussex.lhc']
find_instruments_and_equipment = ['terradue.high-resolution_change_monitoring_for_the_alpine_region',
                                  'eosc.terradue.high-resolution_change_monitoring_for_the_alpine_region']
find_supporting_services_for_eInfras = ['geant.open', 'geant.plus', 'geant.eduroam_managed_idp', 'geant.eduteams',
                                        'bifi_-_unizar.hm', 'geant.edugain_federation_as_a_service',
                                        'grnet.argo_monitoring_engine', 'geant.geant_cloud_flow', 'geant.perfsonar',
                                        'geant.testbeds_service', 'geant.edugain',
                                        'sciences_po.web_panel_sample_service',
                                        'geant.eduvpn_-_access_your_institutes_network_or_the_internet_using_an_encrypted_connection',
                                        'bluebridge.accounting_framework', 'geant.eduroam',
                                        'geant.edumeet_-_webbased_videoconferencing_platform',
                                        'openaire.fp7_post-grant_gold_open_access_pilot', 'eudat.b2access',
                                        'authenix.authenix', 'egi-fed.check-in', 'egi-fed.egi_software_distribution',
                                        'geant.inacademia', 'geant.ip', 'enhancer.swiss_escience_grid_certificates',
                                        'geant.trusted_introducer', 'bluebridge.scientific_training_environment',
                                        'iisas.edudns_dynamic_dns_service_for_academia',
                                        'geant.trusted_certificate_service', 'komanord.guardomic',
                                        'geant.ocre_cloud services by scc', 'geant.lambda', 'openaire.openplato',
                                        'geant.mdvpn', 'blue-cloud.mei_vlab', 'geant.ocreposita', 'geant.geantargus',
                                        'ibergrid.sqaaas', 'geant.ocresafespring', 'ibergrid.fair_eva',
                                        'openaire.open_science_helpdesk', 'eosc.geant.open', 'eosc.geant.plus',
                                        'eosc.geant.eduroam_managed_idp', 'eosc.geant.eduteams',
                                        'eosc.bifi_-_unizar.hm', 'eosc.geant.edugain_federation_as_a_service',
                                        'ni4os.grnet.argo_monitoring_engine', 'eosc.geant.geant_cloud_flow',
                                        'eosc.geant.perfsonar', 'eosc.geant.testbeds_service', 'eosc.geant.edugain',
                                        'eosc.sciences_po.web_panel_sample_service',
                                        'eosc.geant.eduvpn_-_access_your_institutes_network_or_the_internet_using_an_encrypted_connection',
                                        'eosc.bluebridge.accounting_framework', 'eosc.geant.eduroam',
                                        'eosc.geant.edumeet_-_webbased_videoconferencing_platform',
                                        'eosc.openaire.fp7_post-grant_gold_open_access_pilot', 'eosc.eudat.b2access',
                                        'eosc.authenix.authenix', 'eosc.egi-fed.check-in',
                                        'eosc.egi-fed.egi_software_distribution', 'eosc.geant.inacademia',
                                        'eosc.geant.ip', 'eosc.enhancer.swiss_escience_grid_certificates',
                                        'eosc.geant.trusted_introducer',
                                        'eosc.bluebridge.scientific_training_environment',
                                        'eosc.iisas.edudns_dynamic_dns_service_for_academia',
                                        'eosc.geant.trusted_certificate_service', 'eosc.komanord.guardomic',
                                        'eosc.geant.ocre_cloud services by scc', 'eosc.geant.lambda',
                                        'eosc.openaire.openplato', 'eosc.geant.mdvpn', 'eosc.blue-cloud.mei_vlab',
                                        'eosc.geant.ocreposita', 'eosc.geant.geantargus', 'eosc.ibergrid.sqaaas',
                                        'eosc.geant.ocresafespring', 'eosc.ibergrid.fair_eva',
                                        'eosc.openaire.open_science_helpdesk', 'incd.sqaaas', 'doabf.prism',
                                        'grnet.ni4os-europe_login', 'expertai.recommender_api', 'geant.edupert',
                                        'openaire.data_provider_dashboard', 'openaire.broker',
                                        'openaire.technical_support_towards_openaire_compliance', 'openaire.validator',
                                        'upf.multilingual_corpus_of_survey_questionnaires', 'ekt.nephos',
                                        'leaena.leaena', 'eosc.incd.sqaaas', 'eosc.doabf.prism',
                                        'ni4os.grnet.ni4os-europe_login', 'eosc.expertai.recommender_api',
                                        'eosc.geant.edupert', 'eosc.openaire.data_provider_dashboard',
                                        'eosc.openaire.broker',
                                        'eosc.openaire.technical_support_towards_openaire_compliance',
                                        'eosc.openaire.validator',
                                        'eosc.upf.multilingual_corpus_of_survey_questionnaires', 'eosc.ekt.nephos',
                                        'eosc.leaena.leaena']
manage_research_data = ['bluebridge.aquaculture_atlas_generation_spatial_data_catalog', 'eudat.b2stage',
                        'dtu.sciencedata', 'doabf.prism', 'ubi.tsddp', 'ictlc.3rd-party_data_security_assessment',
                        'fzj-inm7.datalad', 'net7.pundit', 'eudat.b2note', 'bluebridge.data-driven_atlas_production',
                        'vi-seem.clowder', 'aginfra.data_transformation_service', 'cnb-csic.3dbionotes-ws',
                        'aginfra.semantic_linking_service', 'charite_bih_brain_simulation.vre',
                        'openminted.consulting_on_licences_for_tdm', 'carlzeissm.aper', 'infn.dodasp',
                        'bluebridge.secure_file_sharing_and_storage', 'aginfra.ontology_engineering_service',
                        'lifewatch-eric.pema_converter', 'athena.rolect', 'olos.olos',
                        'bluebridge.french_tuna_atlas_spatial_data_repository',
                        'european_xfel.european_xfel_metadata_catalogue',
                        'taltechdata.tallinn_university_of_technology_data_repository',
                        'ifremer.envri-fair_marine_essential_ocean_variables_data_broker',
                        'openaire.data_provider_dashboard', 'openaire.broker',
                        'openaire.technical_support_towards_openaire_compliance', 'openaire.validator', 'fairmat.nomad',
                        'upf.multilingual_corpus_of_survey_questionnaires', 'blue-cloud.plankton_eov_vlab',
                        'cessda-eric.cvs', 'blue-cloud.carbon_notebooks', 'cesnet.science_mesh_service',
                        'seadatanet.seadatanet_cdi_ogc_wms', 'athena.lct', 'progedo.qpd', 'seadatanet.seadatanet_cdi',
                        'seadatanet.seadatanet_cdi_sparql', 'seadatanet.seadatanet_cdi_ogc_wfs', 'uot.plutof',
                        'eosc.bluebridge.aquaculture_atlas_generation_spatial_data_catalog', 'eosc.eudat.b2stage',
                        'eosc.dtu.sciencedata', 'eosc.doabf.prism', 'eosc.ubi.tsddp',
                        'eosc.ictlc.3rd-party_data_security_assessment', 'eosc.fzj-inm7.datalad', 'eosc.net7.pundit',
                        'eosc.eudat.b2note', 'eosc.bluebridge.data-driven_atlas_production', 'eosc.vi-seem.clowder',
                        'eosc.aginfra.data_transformation_service', 'eosc.cnb-csic.3dbionotes-ws',
                        'eosc.aginfra.semantic_linking_service', 'eosc.charite_bih_brain_simulation.vre',
                        'eosc.openminted.consulting_on_licences_for_tdm', 'eosc.carlzeissm.aper', 'eosc.infn.dodasp',
                        'eosc.bluebridge.secure_file_sharing_and_storage', 'eosc.aginfra.ontology_engineering_service',
                        'eosc.lifewatch-eric.pema_converter', 'eosc.athena.rolect', 'eosc.olos.olos',
                        'eosc.bluebridge.french_tuna_atlas_spatial_data_repository',
                        'eosc.european_xfel.european_xfel_metadata_catalogue',
                        'eosc.taltechdata.tallinn_university_of_technology_data_repository',
                        'eosc.ifremer.envri-fair_marine_essential_ocean_variables_data_broker',
                        'eosc.openaire.data_provider_dashboard', 'eosc.openaire.broker',
                        'eosc.openaire.technical_support_towards_openaire_compliance', 'eosc.openaire.validator',
                        'eosc.fairmat.nomad', 'eosc.upf.multilingual_corpus_of_survey_questionnaires',
                        'eosc.blue-cloud.plankton_eov_vlab', 'eosc.cessda-eric.cvs', 'eosc.blue-cloud.carbon_notebooks',
                        'eosc.cesnet.science_mesh_service', 'eosc.seadatanet.seadatanet_cdi_ogc_wms', 'eosc.athena.lct',
                        'eosc.progedo.qpd', 'eosc.seadatanet.seadatanet_cdi', 'eosc.seadatanet.seadatanet_cdi_sparql',
                        'eosc.seadatanet.seadatanet_cdi_ogc_wfs', 'eosc-nordic.uot.plutof', 'bluebridge.nym_framework',
                        'bluebridge.data_miner_analytics_service', 'bluebridge.support_for_data_publication',
                        'csc-fi.fairdata_services', 'bluebridge.french_tuna_atlas_spatial_data_catalog',
                        'bluebridge.aquaculture_atlas_spatial_data_repository', 'esrf.visa', 'infn.paas_orchestrator',
                        'ifca-csic.ai4eosc_platform', 'nilu.actris_data_portal',
                        'emso_eric.eosc_future_environment_dashboard', 'sios.sios_data_access_portal',
                        'ukri_-_stfc.idaaas', 'geant.geantargus', 'ibergrid.fair_eva', 'eosc.bluebridge.nym_framework',
                        'eosc.bluebridge.data_miner_analytics_service', 'eosc.bluebridge.support_for_data_publication',
                        'eosc.csc-fi.fairdata_services', 'eosc.bluebridge.french_tuna_atlas_spatial_data_catalog',
                        'eosc.bluebridge.aquaculture_atlas_spatial_data_repository', 'eosc.esrf.visa',
                        'eosc.infn.paas_orchestrator', 'eosc.ifca-csic.ai4eosc_platform',
                        'eosc.nilu.actris_data_portal', 'eosc.emso_eric.eosc_future_environment_dashboard',
                        'eosc.sios.sios_data_access_portal', 'eosc.ukri_-_stfc.idaaas', 'eosc.geant.geantargus',
                        'eosc.ibergrid.fair_eva']
process_and_analyze = ['openminted.catalogue_of_tdm_components', 'lifewatch-eric.rvlab_runner', 'desy.pan_notebook',
                       'bluebridge.dynamic_reporting', 'egi-fed.egi_replay', 'icos_eric.icos_jupyter_hub',
                       'bluebridge.scalable_data_mining', 'infn.fgsg_science_software_on_demand', 'brfaa.dreamm',
                       'bluebridge.nym_framework', 'openminted.support_and_training', 'bluebridge.aquaculture_farming',
                       'compbiomed.software_hub', 'brfaa.feprepare', 'embimos.mecoda',
                       'bluebridge.data_miner_analytics_service', 'aginfra.chart_visualization',
                       'edelweiss_connect.lazar', 'rbi.dariah_science_gateway',
                       'openminted.builder_of_tdm_applications', 'openrisknet.e-infrastructure', 'eodc.openeo_platform',
                       'openrisknet.lazar', 'ukim_fcse.schrodinger_api', 'bluebridge.stock_assessment_support',
                       'blue-cloud.oceanpatterns', 'data_revenue.py-muvr', 'bluebridge.species_modeling',
                       'bluebridge.data_warehousing_facilities', 'blue-cloud.storm_ssi',
                       'openminted.tdm_applications_executor', 'desy.desy_visa',
                       'bluebridge.data_miner_analytics_prototype_service', 'cnb-csic.covid-19_structural_hub',
                       'brfaa.ingredio', 'earthwatch.mics_measuring_the_impact_of_citizen_science', 'rasdaman.datacube',
                       'bluebridge.french_tuna_atlas_spatial_data_catalog',
                       'bluebridge.aquaculture_atlas_spatial_data_repository', 'uob-rcub.repol',
                       'openminted.catalogue_of_tdm_applications', 'icos_eric.stilt_viewer',
                       'bluebridge.spatial_data_infrastructure_laboratory_catalog',
                       'wenmr.fanten_finding_anisotropy_tensor', 'bluebridge.global_tuna_atlas_spatial_data_catalog',
                       'bluebridge.western_central_atlantic_fishery_commission_spatial_data_catalog',
                       'bluebridge.spatial_planning', 'bluebridge.bionym', 'egi-fed.fedearthdata',
                       'blue-cloud.phytoplankton_eovs', 'asgc.icomcot_tsunami_wave_propagation_simulation_portal',
                       'lifewatch-eric.occurrences_datacube_builder', 'university_of_sussex.lhc',
                       'blue-cloud.blue-cloud_vre', 'openaire.openapc', 'norce.openlab_drilling',
                       'sethsoftware.ai4pheno', 'blue-cloud.jupyter_hub', 'blue-cloud.plankton_interact',
                       'blue-cloud.plankton_genomics_vlab', 'blue-cloud.oceanregimes',
                       'rb.sentiment_analysis_api__text_analytics_api', 'ill.biosas_jupyter_notebook',
                       'blue-cloud.zooplankton_eovs', 'blue-cloud.analytics_engine', 'blue-cloud.fisheries_atlas',
                       'blue-cloud.rstudio', 'adv_met.easy-amanida', 'emso_eric.eosc_future_environment_dashboard',
                       'ukri_-_stfc.idaaas', 'dynaikon.fcc', 'psi.panet_ontology_service',
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
                       'eosc.earthwatch.mics_measuring_the_impact_of_citizen_science', 'eosc.rasdaman.datacube',
                       'eosc.bluebridge.french_tuna_atlas_spatial_data_catalog',
                       'eosc.bluebridge.aquaculture_atlas_spatial_data_repository', 'ni4os.uob-rcub.repol',
                       'eosc.openminted.catalogue_of_tdm_applications', 'eosc.icos_eric.stilt_viewer',
                       'eosc.bluebridge.spatial_data_infrastructure_laboratory_catalog',
                       'eosc.wenmr.fanten_finding_anisotropy_tensor',
                       'eosc.bluebridge.global_tuna_atlas_spatial_data_catalog',
                       'eosc.bluebridge.western_central_atlantic_fishery_commission_spatial_data_catalog',
                       'eosc.bluebridge.spatial_planning', 'eosc.bluebridge.bionym', 'eosc.egi-fed.fedearthdata',
                       'eosc.blue-cloud.phytoplankton_eovs',
                       'eosc.asgc.icomcot_tsunami_wave_propagation_simulation_portal',
                       'eosc.lifewatch-eric.occurrences_datacube_builder', 'eosc.university_of_sussex.lhc',
                       'eosc.blue-cloud.blue-cloud_vre', 'eosc.openaire.openapc', 'eosc.norce.openlab_drilling',
                       'eosc.sethsoftware.ai4pheno', 'eosc.blue-cloud.jupyter_hub', 'eosc.blue-cloud.plankton_interact',
                       'eosc.blue-cloud.plankton_genomics_vlab', 'eosc.blue-cloud.oceanregimes',
                       'eosc.rb.sentiment_analysis_api__text_analytics_api', 'eosc.ill.biosas_jupyter_notebook',
                       'eosc.blue-cloud.zooplankton_eovs', 'eosc.blue-cloud.analytics_engine',
                       'eosc.blue-cloud.fisheries_atlas', 'eosc.blue-cloud.rstudio', 'eosc.adv_met.easy-amanida',
                       'eosc.emso_eric.eosc_future_environment_dashboard', 'eosc.ukri_-_stfc.idaaas',
                       'eosc.dynaikon.fcc', 'eosc.psi.panet_ontology_service', 'openrisknet.jaqpot',
                       'edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                       'edelweiss_connect.jaqpot', 'brfaa.chembioserver', 'incd.application_lifecycle_enabler_4_cloud',
                       'openrisknet.squonk_computational_notebook', 'blue-cloud.mei_generator',
                       'bluebridge.d4science_spatial_data_catalog',
                       'bluebridge.regional_database_for_fishery_stock_management', 'icos_eric.stilt_worker',
                       'smartsmear.new_particle_formation_event_analysis',
                       'rolos.machine_intelligence_platfrom_for_research', 'grycap.oscar',
                       'blue-cloud.plankton_eov_vlab', 'eosc.openrisknet.jaqpot',
                       'eosc.edelweiss_connect.openrisknet_-_open_e-infrastructure_to_support_data_sharing_knowledge_integration_and_in_silico_analysis_and_modelling_in_risk_assessment',
                       'eosc.edelweiss_connect.jaqpot', 'ni4os.brfaa.chembioserver',
                       'eosc.incd.application_lifecycle_enabler_4_cloud',
                       'eosc.openrisknet.squonk_computational_notebook', 'eosc.blue-cloud.mei_generator',
                       'eosc.bluebridge.d4science_spatial_data_catalog',
                       'eosc.bluebridge.regional_database_for_fishery_stock_management', 'eosc.icos_eric.stilt_worker',
                       'eosc.smartsmear.new_particle_formation_event_analysis',
                       'eosc.rolos.machine_intelligence_platfrom_for_research', 'eosc.grycap.oscar',
                       'eosc.blue-cloud.plankton_eov_vlab']
publish_research_outputs = ['bluebridge.support_for_data_publication', 'openminted.corpus_builder_for_scholarly_works',
                            'bluebridge.software_repository', 'ierek.ierek',
                            'eosc.bluebridge.support_for_data_publication',
                            'eosc.openminted.corpus_builder_for_scholarly_works', 'eosc.bluebridge.software_repository',
                            'eosc.ierek.ierek', 'aginfra.geoanalytics_visualization', 'ceric-eric.ceric-data-portal',
                            'aginfra.ontology_engineering_service', 'bluebridge.collaboration_framework',
                            'athena.rolect', 'blue-cloud.blue-cloud_vre', 'eosc.aginfra.geoanalytics_visualization',
                            'eosc.ceric-eric.ceric-data-portal', 'eosc.aginfra.ontology_engineering_service',
                            'eosc.bluebridge.collaboration_framework', 'eosc.athena.rolect',
                            'eosc.blue-cloud.blue-cloud_vre']


######################################## PREDEFINED MARKETPLACE LOCATION VALUES ########################################

##################################################### FUNCTIONS ########################################################
def catalogue_migration(directory):
    for file in os.listdir(directory + catalogueFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + catalogueFolder + file, 'r') as json_file:
                json_data = migrate_catalogues(json_file, isVersion)
                # write to file
                with open(directory + catalogueFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + catalogueFolder + file)
            for versionFile in versionFiles:
                with open(directory + catalogueFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate_catalogues(json_file, isVersion)
                    # write to file
                    with open(directory + catalogueFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


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


def migrate_catalogues(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    catalogue = root.find('{http://einfracentral.eu}catalogue')

    # scope
    scope = ET.Element("tns:scope")
    scope.text = 'TBD'
    catalogue.append(scope)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


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
    if id in build_analysis_environment:
        fill_predefined_marketplace_locations(marketplaceLocations,
                                              'marketplace_location-build_analysis_environment')
    if id in find_supporting_services_for_eInfras:
        fill_predefined_marketplace_locations(marketplaceLocations,
                                              'marketplace_location-find_supporting_services_for_eInfras')
    if id in explore_other_research_catalogues:
        fill_predefined_marketplace_locations(marketplaceLocations,
                                              'marketplace_location-explore_other_research_catalogues')


def fill_predefined_marketplace_locations(marketplaceLocations, vocabulary):
    marketplaceLocation = ET.Element("tns:marketplaceLocation")
    marketplaceLocation.text = vocabulary
    marketplaceLocations.append(marketplaceLocation)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
catalogue_migration(args.path)
datasource_migration(args.path)
other_resources_migration(args.path)
service_migration(args.path)
######################################################## RUN ###########################################################
