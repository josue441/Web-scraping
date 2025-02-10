from bs4 import BeautifulSoup
import requests

lista = ['p-26a_34_m2','p-36a','bf2c_1','os2u_1','os2u_3','tbd-1_1938','b_18a','p-26a_33','p-26b_35','p-36c','f3f-2',
        'sb2u-2','sb2u-3','pby-5','pby-5a','f2a-1','tbf-1c','sbd-3','pbm_1','f3f-2_galer','p-26a_34','p-36c_rb',
        'p-36a_rasmussen','f2a-1_thach','b_10b','p-400','p-36g','f2a-3','p-51_a-36','b_34','p-38e','p-38g',
        'p-40e','p-40f_10','f4f-3','f4f-4','f6f-3','a-20g','b_25j_1','p-39n','p-39q_5','p-51c-10-nt','f4u-1a',
        'f4u-1a_usmc','f4u-1d','sb2c_1c','sb2c_4','b_25j_20','p-40e_td','p-40c','ki_43_2_late','p-38','p-51a_tl',
        'p-43a-1','p-38g_metal','pbm_3','ki_61_1a_otsu_usa','p-63a-5','p-51_mk1a_usaaf','p-51d-5','f4u-4','pbj_1j',
        'pbj_1h','b_26b_c','p-63a-10','p-63c-5','p-47d_22_re','f8f1b','f7f1','douglas_ad_2','douglas_ad_4','am_1_mauler',
        'b-29','xa_38','p-38j_marge','p-51d-20-na','p-38k','p-51d-10','a-26c','p-47m-1-re','a-26c-45-dt','p-47m-1-re_boxted',
        'p-59a','fw-190a-8_usa','f4u-4b_vmf_214','spitfire_ix_usa','f4u-6_au-1','douglas_a_1h','f2g-1','f7f','f-80a','f-84b','f-84g',
        'f2h-2','f3d_1','b-57','b-57b','f-80','f-86a-5','f-86f-25','f9f-2','f9f-5','f9f-8','f-84f','f-89b','a2d','f-89d',
        'f-86f-35','f-104a','f-104c','f-86f-2','f3h-2','a_4b','fj_4b','f-100d','f8u-2','av_8c','a_4e_early','fj_4b_agm_12b',
        'f_117','f11f_1_late','av_8a','f4d_1','a_10a_early','f-5e','f-4c','f-8e','a_10a_late','f-105d','f-4e','f-4j','a_7d','a_7e',
        'f_111a','a_10c','f_111f','f-5c','f-5a','a_6e_tram','a_7k','f-4s','av_8b_na','f_16a_block_10','f_16a_block_15_adf','f_15a',
        'f_14a','_early','av_8b_plus','f_15e','f_16c_block_50','f_15c_msip2','f_14b','f_20a','f_14a_iriaf','bf-109b_2','he51a1','he51b1',
        'he51c1','he51c1_late','do_17z_7','hs-123a-1','do_17e_1','do_17z_2','bf-109c_1','he_112v_5','he_112a_0','do_217j_1','do_217j_2',
        'ju-87b-2','ju-87r-2','he_115c_1','bv-138c-1','he_100d_1','ju-87g_1','ju-87g_2','he-111h-2','bf-109a_1','he51b_2w','ju-87r-2_snake',
        'arado-196a-3','fiat_cr42_marcolin','fw-189a-1','fiat_cr42','fiat_g50_seria2','fiat_g50_seria7as','bf-109c_1_promo','mc200_serie3',
        'mc200_serie7','mc-202','bf-109e-1','he_112b_0','ju-88c-6','hs-129b-3','hs-129b-2','fw_200c_1','bf-109e-3','bf-109e-4','fw-190a-1',
        'do_217n_1','do_217n_2','ju-87d-3','ju-87d-5','ju-88a-1','ju-88a-4','bf-109f-1','bf-109f-2','bf-110c-4','bf-110f-2','me-410a-1_u4',
        'me-410b-2_u4','he-111h-6','he-111h-16_winter','he_112b_1','wellington_mk1c_luftwaffe','il_2_1942_luftwaffe','he_112b_2','bf-110c-6',
        'h-75a-2_finland','yak-1b_luftwaffe','bf-109e-7','bv-238','sm_79_1936','sm_79_1939','sm_79_1941','sm_79_1943','sm_79_iar','sm_79_1937',
        'sm_79_1942','bf-109f-4','bf-109f-4_trop','fw-190a-4','fw-190a-5_u2','bf-110g-2','bf_110g_4','me-410a-1','me-410b-1','me_264','fw-190d-9',
        'me-410a-1_u2','me-410b-1_u2','do_335a_1','do_335a_0','do_217e_2','do_217e_4','p-47d_16_re_germany','hs-129b-2_romania','ta_154a_1',
        'p-47d_luftwaffe','fw_190a_5_u14','la-5fn_luftwaffe','bf-109g-2_romania','bv-155b-1','bf-109g-2','bf-109g-6','fw-190a-5_cannons','fw-190a-8',
        'me-410b-6_r3','fw-190f-8','do_217k_1','do_217m_1','bf-109g-14','bf-109g-10','fw-190a-5','fw-190d-12','me-262a-1a_u4','ju-188a-2','bf-109k-4',
        'ta-152h-1','ta-152c','he-177a-5','he_219a_7','bf-109z','do_335b_2','ju-388j','tempest_mkv_luftwaffe','fw-190c','ju-288c','fw-190d-13','he-177a-3',
        'me-262a-1a','me-262c-1a','me-262c-2b','he-162a-2','go229_v3','me-262a-1a_early','arado-234','arado-234c-3','me-163b','me-163b-0','mig-15bis_nr23_german',
        'il_28_german','me-262a1_u1','he-162a-1','sea_hawk_mk100','me-262a-2a','fiat_g91_r4_german','f-86_canadair_german','f-86_cl_13b_mk6','mig-17p_lim_5p','fiat_g91_r3',
        'f-84f_germany','mig_23bn','f-86k_late_german','mig-19s','alpha_jet_a','hunter_f58_switzerland','ffa_p16','mig-21_sps_k','f-104g','mig-21_mf','mig-21_bis_sau',
        'su_22um3k','f-4f_late','mig_23mla','su_22m4','mig-21_bis_lazur','f-4f','tornado_ids_de_wtd61','mig_23mf_germany','su_22m4_de_wtd61','f-4f_kws_lv','mig_29_9_12_germany',
        'tornado_ids_de_assta1','ef_2000_block_10','mig_29_9_12g','tornado_ids_de_mfg','i-16_type5','i-15_1934','i-15_1935','i-15_1935_moscow','po-2','sb_2m_100','sb_2m_103c',
        'mig_3_series_1_15','i-15bis','i-153_m62','bb-1','su-2_mv5','su-2_tss1','su-2_m82','yak-4','i-16_type10','i-16_type18','i-16_type24','pe-3_early','pe-3','ar_2',
        'sb_2m_103u_mv3','sb_2m_105','sb_2m_103u','sb_2m_103_mv3','yak_2_kabb','i-15bis_krasnolutsky','mbr-2','pby-5a_ussr','po-2m','hp52_hampden_tbmk1_ussr_utk1','tb_3_m17_32',
        'tandem_mai','i-153_m62_zhukovskiy','yak-1_early','yak-1b','mig_3_series_1_15_bk_pod','mig_3_series_34','lagg-3-8','lagg-3-11','il_2_1941','db_3b','il-4','yak-7b',
        'i-16_type27','lagg-3-35','lagg-3-66','il-2i','il_2_37_1943','pe-2-1','pe-2-31','pe-2-83','yak-9','yak-9b','la-5_type37_early','la-5_type39','pe-3_bis','lagg-3-4',
        'lagg-3-23','p-40e_ussr','i_29','hurricanemkii_ussr','il_2_m82','i-153p','i_180','i-16_type28','lagg-3-34','p-39k_1','lagg-i-301','yak-9t','yak-9k','i_185_m82','la-5fn',
        'il_2m_1943','il-2m','er-2_m105_mv3','er-2_m105r_lu2b','er-2_m105_tat','er-2_m105r_tat','yak-3','yak-9u','i_185_m71_standard','la-7','su-6_m71','pe-2-110','pe-2-359',
        'pe-8_m82','a_20g_30_ussr','il-2m_mstitel','p-39n_su','yak-9m','p-39q_15','pe-2-205','p-63a-5_ussr','il_8_1944','p-47d_ussr','tis_ma','b_25j_30_vvs_ussr','itp_m1',
        'yak-3_eremin','tu-2_early','yak-3p','yak-9p','i_225','la-7b-20','su-6_am42','er-2_ach30b_early','er-2_ach30b_late','yak-3u','yak-9ut','la-9','il-10','il-10_1946',
        'tu-2','tu-2_postwar','tu-2_postwar_late','su_6_single','p-63c-5_ussr','la-7_dolgushin','p-63a-10_ussr','be_6','su-8','la-11','fw-190d-9_ussr','spitfire_ix_ussr',
        'yak-3t','yak-3_vk107','tu-1','yak-15_early','yak-15','yak-17','mig-9','mig-9_ussr','su-9','il_28','il_28sh','tu_4','yak-23','mig-15_ns23','mig-15','la_200_toriy',
        'la-15','tu_14t','su-11','bi','mig-15bis_ish','la_174','yak-30d','mig-17','su-7b','su-7bkl','su_25','yak-28b','yak-38m','mig-19pt','mig-21_f13','mig-17_cuba',
        'mig-21_pfm','yak-38','su-7bmk','mig-21_s','su_25k','mig-21_smt','mig-21_bis','su_17m2','su_25t','mig_27m','mig_27k','mig_23m','mig_23mld','su_17m4','su_24m',
        'su_22m3','su_25_558arz','mig_23ml','su_25tm','yak_141','mig_29_9_13','su_27','su_25sm3','su_34','mig_29smt_9_19','su_27sm','su_33','fury_mk1','fury_mk2',
        'gladiator_mk2_france','nimrod_mk1','v_156_b1','swordfish_mk1','gladiator_mk2_silver','nimrod_mk2','blenheim_mkiv','beaufort_mkviii','hp52_hampden_mk1_late',
        'hp52_hampden_tbmk1','gladiator_mk2','gladiator_mk2_navy','gladiator_mk2_tuck','swordfish_mk2','wirraway','pby-5a_raf','hurricanemkii','hurricane_mk1','spitfire_mk1',
        'spitfiremkiia','hurricane_mk1b','hurricane_mk4','sunderland_mk3a','sunderland_mk5','typhoon_mk1a','spitfiremkii','hurricane_mk1c','beaufighter_mk6c','beaufighter_mkx',
        'beaufighter_mk21','wellington_mk1c','wellington_mk1c_late','spitfire_mk5b','spitfire_mk5b_notrop','firebrand_tf4','tempest_mkv_vikkers','wellington_mk3','wellington_mk10',
        'avenger_mk1','intruder_mk_1','hudson_mk_v','beaufighter_mk1_40mm','b_48_firecrest','boston_mk_1','corsair_fmk2','db_7','spitfiremkiia_ep','hurricane_mk1_late_ep','d_520',
        'f4f-4_martlet_mk4','d_521','boomerang_mki','boomerang_mkii','typhoon_mk1b_late','spitfire_ix_early','spitfire_xvi','firefly_mk1','firefly_mk5','mosquito_fb_mk6','mosquito_fb_mk18',
        'halifax_mk3','spitfire_mk5c','spitfire_mk5c_notrop','seafire_mk3','brigand_b1','whirlwind_mk1','stirling_mk1','stirling_mk3','hellcat_fmk1','typhoon_mk1b','thunderbolt_mk1','whirlwind_p9',
        'p-51b','spitfire_mk9c_4cannons','tempest_mkv','spitfire_mk14e','spitfire_mk18e','spitfire_ix','seafire_mk17','seafire_fr47','hornet_mk3','lancaster_mk1','lancaster_mk3','tempest_mk2',
        'spitfire_f22','spitfire_f24','sea_fury_fb11','lincoln_b2','shackleton_mr_mk_2','mb_5','wyvern_s4','hornet_mk1','spitfire_mk14c','spitfire_ix_plagis','spitfire_fr_mk14e','strikemaster_mk88',
        'vampire_fb5','meteor_fmk3','meteor_fmk3_navy','attaker_fb1','swift_f1','canberra_bmk2','canberra_bimk6','venom_fb4','meteor_fmk4_lw','meteor_fmk4_sw','meteor_fmk8','sea_hawk_fga6','sea_venom_faw20',
        'swift_f7','meteor_fmk8_reaper','attaker_fb2','dh_110_sea_vixen','hunter_f1','javelin_fmk9','scimitar_f1','jaguar_gr1','buccaneer_s2','hunter_f6','lightning_f6','harrier_gr3','lightning_f53',
        'buccaneer_s1','harrier_gr1','hunter_f9_rhodesia','f-4m_fgr2','harrier_frs1_early','jaguar_gr1a','buccaneer_s2b','f-4k','f_111c_raaf','harrier_frs1','jaguar_is','f-4jk',
        'saab_jas39c_south_africa','tornado_f3','sea_harrier_fa2','harrier_gr7','tornado_gr1','ef_2000_fgr4','tornado_f3_late','tornado_gr4','mig-21_bison','f1m2','ki_10_1',
        'ki_10_2','ki_10_1_commander','ki_10_2_commander','ki-45_tei','ki-45_otsu','b5n2','ki_32','a5m4','ki-27_otsu','ki-45_ko','ki-45_hei','d3a1','ki_21_1ko','ki_43_1',
        'ki_43_2','ki_109','b6n1','h6k4','a5m4_hagiri','ki-27_otsu_ep','a6m2_n_zero','n1k1_kyuofu','ki_44_1','ki_61_1a_ko','j1n1_mod11_early','b6n2','b6n2a','g4m1',
        'a6m2_mod11','a6m2_zero','ki_44_2_hei','ki_61_1a_otsu','ki_102_otsu','d4y1','d4y2','h8k2','d4y3','ki-49_1','ki-49_2a','a7he1','ki_48_2_otsu','ki_44_1_ep','ki_21_1hei','ki_44_2_otsu',
        'bf-109e-3_japan','h8k3','f4u-1a_japan','a6m3_zero','a6m3_mod22_zero','a6m3_mod22ko_zero','ki_43_3_otsu','ki_108','p1y1_mod11','ki-49_2b','ki-49_2b_late','a6m5_zero','ki_61_1a_tei','ki_61_2_early',
        'j2m2','b7a2','g5n1','ki_100_early','j5n1','ki_67_1_ko','ki_67_1_otsu','ki-96','p-51c-11-nt_japan','ki_100_2','b7a2_homare_23','sb2c_5_thailand','a6m5otsu','a6m5hei','ki_61_1a_hei','j7w1',
        'g8n1','a7m2','ki_84_ko','ki_84_otsu','j2m3','j2m5','n1k1_ja','n1k2_j','n1k2_jko','ki_84_hei','ki-83','b-17e_japan','a6m6c','a7m1','a6m5ko','ki_61_1a_hei_ep','fw-190a-5_japan',
        'j2m4_kai','ki_94_2','j2m5_30mm','j6k1','ki_87','kitsuka','j8m1','f-84g_thailand','r2y2_v1','r2y2_v2','r2y2_kai','f-86f-30_japan',
        'f-86f-40_japan','f-86f-40_japan_blue_impulse','f-104j','t2','alpha_jet_a_thailand','f1','alpha_jet_th_phase_1','t2_early','av_8s_thailand','f-4ej','a_7e_thailand',
        'f-5a_thailand','av_8s_late_thailand','f-5t_thailand','f-5e_fcu_thailand','f-4ej_adtw','f-4ej_kai','f_16aj','f_16a_block_15_ocu_thailand','f_15j','saab_jas39c_thailand',
        'f_15j_kai','gladiator_mk1_china','i-15bis_china','hs-123a-1_china','martin_139wc','ki-27_otsu_china','ki_43_3_ko','i-16_chung_28','i-16_type5_1935_china','v_11g','cw_21',
        'i-153_m62_china','v_12d','hawk_iii','d_510c','p-66','i-16_type10_china','a_29_hudson','db_3a_china','sb_2m_103u_china','p-40e_china','p-43a-1_china','i-16_type17_china',
        'p1y1_mod11_china','p-40c_china','ki-45_hei_tei_china','p-47d_23_ra_china_rocaf','p-47d_30_china','ki_44_2_hei_china','mosquito_fb_mk26_china','b_25j_30_china',
        'p-51d-20_china','p-51k','ki_61_1a_otsu_china','p-38l_1_china_rocaf','a6m2_zero_china','p-51c-11-nt_china','f_47n_25_re_china','la-11_china','il-10_1946_china',
        'pb4y-2_china','la-9_china','tu-2_postwar_china','ki_84_ko_china','f-86f-30_china','f-86f-40_china','mig-9_china','mig-9_late_china','f-84g_china','tu_4_china',
        'mig-15bis_nr23_china','mig-17_china','il_28_china','f-84g-31-re_china','f-100a_china','mig-19j_6a','j_7_mk2','q_5_early','f-104a_china','q_5a','mig-17_f5',
        'f_100f_china','a_5c','f-104g_china','j_7e','q_5l','f-5a_china','f-5e_aidc','j_8b','j_7d','f_16a_block_20_mlu','j_8f','jh_7a','j_10a','j_11','mirage_2000_5ei',
        'j_11a','jf_17','ro_44','cr_32','cr_32_quater','ba_65_k14_l','ju-87r-2_italy','s_81_ar125','re_2000_int','re_2000_ga','fiat_cr42_italy','breda_88','p_108a_serie2',
        'br_20_dr','br_20m_m1','fiat_g50_seria2_italy','fiat_g50_seria7as_italy','fc_20_bis','sm_79_1936_italy','sm_79_1939_italy','fiat_cr42_marcolin_italy','cr_32_bis',
        're_2002_early','mc200_serie3_italy','mc200_serie7_italy','ju-87d-3_italy','sm_79_1941_italy','sm_79_1943_italy','sm_79_iar_italy','re_2001_serie1','re_2001_cb',
        'mc-202_italy','mc-205_serie1','sm_91','z_1007_bis_serie3','z_1007_bis_serie5','he_112b_1_italy','iar_81c','re_2001_serie1_ep','ro_57_quadriarma','mc-202_d',
        're_2001_cn','mc-202_ec','sm_92','p_108b_serie1','p_108b_serie2','g_55_serie1_ss0','mc-205_n2','p-47d_30_italy','hs-129b-2_romania_italy','bf_110g_4_hungary',
        'spitfire_mk5b_italy','bf-109f-4_hungary','g_55_serie1','re_2005_serie0','mc-205_serie3','il-10_1946_hungary','tu-2_postwar_late_hungary','yak-9p_hungary',
        'g_56','bf-109g-14as','bf-109g-2_hungary','g_55s','vampire_fb52a_italy','fiat_g91_ps','fiat_g91_r1','f-84g_italy','il_28_hungary','mig-15bis_nr23_hungary',
        'f-86_cl_13_mk4_italy','fiat_g91_r4','f-86k_late_italy','sagittario_2','f-84f_italy','mig-17pf_hungary','f-104g_italy','fiat_g91_y','fiat_g91_ys','ariete',
        'iar_93b','f-104s','amx','tornado_ids_it','su_22m3_hungary','mig-21_mf_hungary','mig-21_bis_sau_hungary','f-104s_asa','mig_23mf_hungary','amx_a_1a_brazil',
        'f-104s_cb','f_16a_block_15_adf_italy','tornado_adv','tornado_ids_it_mod95','mig_29_9_12b_hungary','ef_2000a','av_8b_plus_italy','saab_jas39c_hungary',
        'd_371','d_373','d_500','d_501','v_156_f','potez_633','gladiator_mk1_belgium','caudron_cr714','h-75a-1_france','h-75a-4_france','br_693_ab2','f_222_2',
        'ms_405c1','ms_406c1','maryland_mk1_france','mb_174_a3','d_510','late_298d','pby-5a_late_france','d_371_hs9','mb_151c1','ms_410c1','potez_630','potez_631',
        'a-35b','nc_223_3','fokker_g1a','vg_33','d_520_france','f6f-5_france','mb_175t','leo_451_early','leo_451_late','p-40f-5_france_ep','mb_152c1','vb_10c1',
        'mb_157','sb2c_5_france','b_26c_france','firefly_mk4_netherlands','vb_10_02','p-63c-5_france','mb_162','p-47d_22_re_france','p-39q_25_france','yak-9t_france',
        'p-51c-10_france','yak-3_france','seafire_mk3_france','f6f-5n_france','douglas_ad_4_france','pb4y-2_france','spitfire_fr_mk14e_belgium','sea_fury_fb51','f8f1b_france',
        'f4u-7','lancaster_mr7_france','so_8000_narval','fw-190a-8_france','douglas_ad_4na_france','md_450b_ouragan','md_450b_barougan','so_4050_vautour_2n_late','f-84g_france',
        'meteor_fmk8_belgium','md_452_mystere_2a','md_452_mystere_2c_preproduction','sea_hawk_fga50_netherlands','md_454_mystere_4a','md_460','f-86k_late','f-84f_france',
        'so_4050_vautour_2b','so_4050_vautour_2a','hunter_f6_holland','alpha_jet_e','f-100d_france','etndard_4m','so_4050_vautour_2n','f-84f_iaf','mirage_milan',
        'so_4050_vautour_2a_iaf','md_460_yt_cup_2019','mirage_3c','mirage_3e','f-8e_fn','mirage_5f','super_etendard_97','mirage_5ba','mirage_f1c','mirage_f1ct',
        'jaguar_a','f-104g_belgium','mirage_f1c_200','jaguar_e','mirage_2000c_s5','mirage_4000','mirage_2000d_r1','f_16a_block_15_belgium','mirage_2000_5f',
        'mirage_2000d_rmv','f_16am_block_15_mlu_belgium','rafale_c_f3','mirage_2000c_s4','gladiator_j8a','j6b','saab_b17bs','he_115a_2_sweden','fokker_d21_serie3_finland',
        'fiat_cr42_j11','saab_b17b','saab_b17a','saab_b3c','gladiator_j8a_iacobi','arado-196a-5','re_2000_j20','saab_b18a','b_239_finland','ffvs_j22_a','ju-88a-4_finland','hurricane_mk1_late_finland',
        'fokker_d21_mod20','j9_early','morko_morane','vl_myrsky_2_late','ffvs_j22_b','saab_b18b','p-51d-20-na_j26','saab_t18b_1','saab_t18b_2','p-51b_7_sweden','pyorremyrsky',
        'saab_j21a_1','saab_j21a_2','saab_a21a_3','bf-109g-2_finland','bf-109g-6_erla_finland','bf-109g-6_finland','saab_j21ra','saab_a21rb','saab_sk60b','vampire_fb5_j28b','vampire_fb52_finland',
        'saab_j29a','saab_j29b','saab_105g','saab_105oe','saab_j29d','saab_j29f','saab_a32a','hunter_f50_sweden','saab_j32b','saab_a32a_red_adam','saab_j35a','saab_j35d','saab_aj37',
        'mig_21_bis_finland','saab_ja37','saab_ajs37','saab_j35xs','saab_ja37d','saab_ja37di','saab_jas39a','saab_jas39c','saab_ja37di_f21','spitfire_mk9c_iaf','s_199','b-17g_iaf',
        'spitfire_lf_mk9e_iaf','p-51d-20-na_iaf','spitfire_lf_mk9e_weisman','meteor_nfmk13','md_450b_ouragan_iaf','meteor_fmk8_iaf','md_454_mystere_4a_iaf','a_4h',
        'a_4e_early_iaf','so_4050_vautour_2a_israel_iaf','so_4050_vautour_2n_iaf','md_460_sambad','md_460_saar','a_4n','f-84f_israel_iaf','a_4e_late_iaf',
        'mirage_3cj','f-4e_iaf','nesher','kfir_c7','kfir_canard','kfir_c2','f_16a_block_10_iaf','f-4e_kurnass_2000','f_16d_block_40_barak_2',
        'f_16c_block_40_barak_2','f_15a_iaf','f_15i_raam','p-47d','f8f1','p-61c_1','b-17e','b-17e_late','p-38j','p-38l','p-47d-28',
        'p-47n-15','f6f-5n','pb4y-2','a6m2_zero_usa','xf5f','btd-1','p-61a_1','xp-55','pv_2d','xp-50',
        'p-63c-5_kingcobra_animal_version','bf-109f-4_usa','pbm_5a','f-82e','p-51d-30_usaaf_korea',
        'f4u-1c','f4u-4b','a-26b_10','a-26b','b-17g','b_24d','p-51h-5_na','f_15c_baz_msip','kfir_c10_colombia']

LINK = "https://wiki.warthunder.com/unit/"

def encontrar(enlace):
    #Busca un avión en la lista y obtiene su información de la web de War Thunder
    newList2 = []

    avion = enlace.replace("_", "").replace("-", "")
    
    for i in lista:
        normalizado = i.replace("_", "").replace("-", "").lower()
        if normalizado.startswith(avion):
            newList2.append(i)
    
    if not newList2:
        return "❌ No se encontró el avión."

    avion_url = f"{LINK}{newList2[0]}"
    result = requests.get(avion_url)

    if result.status_code != 200:
        return f"⚠ Error al obtener los datos: {result.status_code}"

    bs = BeautifulSoup(result.text, "lxml")
    temp = bs.find_all("div", "game-unit_card-info_value")

    rank = temp[0].text.strip() if len(temp) > 0 else "Desconocido"
    nation = temp[4].text.strip() if len(temp) > 4 else "Desconocido"
    unit = temp[5].text.strip() if len(temp) > 5 else "Desconocido"
    operator = temp[6].text.strip() if len(temp) > 6 else "Desconocido"

    if rank == "II":
        rank = temp[0].text.strip()
        nation = temp[2].text.strip()
        unit = temp[3].text.strip()
        operator = temp[2].text.strip()

    if rank == "I" or rank == "III" or rank == "V" or rank == "IV":
        rank = temp[0].text.strip()
        nation = temp[2].text.strip()
        unit = temp[3].text.strip()
        operator = temp[2].text.strip()

    return f"""✈ **Avión:** {newList2[0]}
🔹 **Rank:** {rank}
🌍 **Game Nation:** {nation}
🎯 **Main Role:** {unit}
🏳 **Operator Country:** {operator}
🔗 **Link:** {avion_url}"""