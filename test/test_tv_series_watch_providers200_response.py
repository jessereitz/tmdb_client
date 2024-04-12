# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response import TvSeriesWatchProviders200Response

class TestTvSeriesWatchProviders200Response(unittest.TestCase):
    """TvSeriesWatchProviders200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200Response:
        """Test TvSeriesWatchProviders200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200Response`
        """
        model = TvSeriesWatchProviders200Response()
        if include_optional:
            return TvSeriesWatchProviders200Response(
                id = 1399,
                results = openapi_client.models.tv_series_watch_providers_200_response_results.tv_series_watch_providers_200_response_results(
                    ae = openapi_client.models.tv_series_watch_providers_200_response_results_ae.tv_series_watch_providers_200_response_results_AE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=AE', 
                        flatrate = [
                            openapi_client.models.tv_series_watch_providers_200_response_results_ae_flatrate_inner.tv_series_watch_providers_200_response_results_AE_flatrate_inner(
                                logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg', 
                                provider_id = 629, 
                                provider_name = 'OSN', 
                                display_priority = 11, )
                            ], ), 
                    ar = openapi_client.models.tv_series_watch_providers_200_response_results_ar.tv_series_watch_providers_200_response_results_AR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=AR', ), 
                    at = openapi_client.models.tv_series_watch_providers_200_response_results_at.tv_series_watch_providers_200_response_results_AT(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=AT', 
                        buy = [
                            openapi_client.models.movie_watch_providers_200_response_results_at_buy_inner.movie_watch_providers_200_response_results_AT_buy_inner(
                                logo_path = '/5NyLm42TmCqCMOZFvH4fcoSNKEW.jpg', 
                                provider_id = 10, 
                                provider_name = 'Amazon Video', 
                                display_priority = 3, )
                            ], ), 
                    au = openapi_client.models.tv_series_watch_providers_200_response_results_au.tv_series_watch_providers_200_response_results_AU(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=AU', ), 
                    ba = openapi_client.models.tv_series_watch_providers_200_response_results_ba.tv_series_watch_providers_200_response_results_BA(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BA', ), 
                    bb = openapi_client.models.tv_series_watch_providers_200_response_results_bb.tv_series_watch_providers_200_response_results_BB(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BB', ), 
                    be = openapi_client.models.tv_series_watch_providers_200_response_results_be.tv_series_watch_providers_200_response_results_BE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BE', ), 
                    bg = openapi_client.models.tv_series_watch_providers_200_response_results_bg.tv_series_watch_providers_200_response_results_BG(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BG', ), 
                    bo = openapi_client.models.tv_series_watch_providers_200_response_results_bo.tv_series_watch_providers_200_response_results_BO(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BO', ), 
                    br = openapi_client.models.tv_series_watch_providers_200_response_results_br.tv_series_watch_providers_200_response_results_BR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BR', ), 
                    bs = openapi_client.models.tv_series_watch_providers_200_response_results_bs.tv_series_watch_providers_200_response_results_BS(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=BS', ), 
                    ca = openapi_client.models.tv_series_watch_providers_200_response_results_ca.tv_series_watch_providers_200_response_results_CA(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CA', ), 
                    ch = openapi_client.models.tv_series_watch_providers_200_response_results_ch.tv_series_watch_providers_200_response_results_CH(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CH', ), 
                    ci = openapi_client.models.tv_series_watch_providers_200_response_results_ci.tv_series_watch_providers_200_response_results_CI(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CI', ), 
                    cl = openapi_client.models.tv_series_watch_providers_200_response_results_cl.tv_series_watch_providers_200_response_results_CL(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CL', ), 
                    co = openapi_client.models.tv_series_watch_providers_200_response_results_co.tv_series_watch_providers_200_response_results_CO(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CO', ), 
                    cr = openapi_client.models.tv_series_watch_providers_200_response_results_cr.tv_series_watch_providers_200_response_results_CR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CR', ), 
                    cz = openapi_client.models.tv_series_watch_providers_200_response_results_cz.tv_series_watch_providers_200_response_results_CZ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CZ', ), 
                    de = openapi_client.models.tv_series_watch_providers_200_response_results_de.tv_series_watch_providers_200_response_results_DE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=DE', ), 
                    dk = openapi_client.models.tv_series_watch_providers_200_response_results_dk.tv_series_watch_providers_200_response_results_DK(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=DK', ), 
                    do = openapi_client.models.tv_series_watch_providers_200_response_results_do.tv_series_watch_providers_200_response_results_DO(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=DO', ), 
                    dz = openapi_client.models.tv_series_watch_providers_200_response_results_dz.tv_series_watch_providers_200_response_results_DZ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=DZ', ), 
                    ec = openapi_client.models.tv_series_watch_providers_200_response_results_ec.tv_series_watch_providers_200_response_results_EC(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=EC', ), 
                    eg = openapi_client.models.tv_series_watch_providers_200_response_results_eg.tv_series_watch_providers_200_response_results_EG(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=EG', ), 
                    es = openapi_client.models.tv_series_watch_providers_200_response_results_es.tv_series_watch_providers_200_response_results_ES(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=ES', ), 
                    fi = openapi_client.models.tv_series_watch_providers_200_response_results_fi.tv_series_watch_providers_200_response_results_FI(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=FI', ), 
                    fr = openapi_client.models.tv_series_watch_providers_200_response_results_fr.tv_series_watch_providers_200_response_results_FR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=FR', ), 
                    gb = openapi_client.models.tv_series_watch_providers_200_response_results_gb.tv_series_watch_providers_200_response_results_GB(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GB', ), 
                    gf = openapi_client.models.tv_series_watch_providers_200_response_results_gf.tv_series_watch_providers_200_response_results_GF(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GF', ), 
                    gh = openapi_client.models.tv_series_watch_providers_200_response_results_gh.tv_series_watch_providers_200_response_results_GH(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GH', ), 
                    gq = openapi_client.models.tv_series_watch_providers_200_response_results_gq.tv_series_watch_providers_200_response_results_GQ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GQ', ), 
                    gt = openapi_client.models.tv_series_watch_providers_200_response_results_gt.tv_series_watch_providers_200_response_results_GT(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=GT', ), 
                    hk = openapi_client.models.tv_series_watch_providers_200_response_results_hk.tv_series_watch_providers_200_response_results_HK(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=HK', ), 
                    hn = openapi_client.models.tv_series_watch_providers_200_response_results_hn.tv_series_watch_providers_200_response_results_HN(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=HN', ), 
                    hr = openapi_client.models.tv_series_watch_providers_200_response_results_hr.tv_series_watch_providers_200_response_results_HR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=HR', ), 
                    hu = openapi_client.models.tv_series_watch_providers_200_response_results_hu.tv_series_watch_providers_200_response_results_HU(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=HU', ), 
                    id = openapi_client.models.tv_series_watch_providers_200_response_results_id.tv_series_watch_providers_200_response_results_ID(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=ID', ), 
                    ie = openapi_client.models.tv_series_watch_providers_200_response_results_ie.tv_series_watch_providers_200_response_results_IE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=IE', ), 
                    il = openapi_client.models.tv_series_watch_providers_200_response_results_il.tv_series_watch_providers_200_response_results_IL(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=IL', ), 
                    iq = openapi_client.models.tv_series_watch_providers_200_response_results_iq.tv_series_watch_providers_200_response_results_IQ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=IQ', ), 
                    it = openapi_client.models.tv_series_watch_providers_200_response_results_it.tv_series_watch_providers_200_response_results_IT(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=IT', ), 
                    jm = openapi_client.models.tv_series_watch_providers_200_response_results_jm.tv_series_watch_providers_200_response_results_JM(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=JM', ), 
                    jp = openapi_client.models.tv_series_watch_providers_200_response_results_jp.tv_series_watch_providers_200_response_results_JP(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=JP', 
                        rent = [
                            openapi_client.models.tv_series_watch_providers_200_response_results_jp_buy_inner.tv_series_watch_providers_200_response_results_JP_buy_inner(
                                logo_path = '/5NyLm42TmCqCMOZFvH4fcoSNKEW.jpg', 
                                provider_id = 10, 
                                provider_name = 'Amazon Video', 
                                display_priority = 6, )
                            ], ), 
                    ke = openapi_client.models.tv_series_watch_providers_200_response_results_ke.tv_series_watch_providers_200_response_results_KE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=KE', ), 
                    kr = openapi_client.models.tv_series_watch_providers_200_response_results_kr.tv_series_watch_providers_200_response_results_KR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=KR', ), 
                    lb = openapi_client.models.tv_series_watch_providers_200_response_results_lb.tv_series_watch_providers_200_response_results_LB(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=LB', ), 
                    lt = openapi_client.models.tv_series_watch_providers_200_response_results_lt.tv_series_watch_providers_200_response_results_LT(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=LT', ), 
                    ly = openapi_client.models.tv_series_watch_providers_200_response_results_ly.tv_series_watch_providers_200_response_results_LY(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=LY', ), 
                    md = openapi_client.models.tv_series_watch_providers_200_response_results_md.tv_series_watch_providers_200_response_results_MD(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MD', ), 
                    mk = openapi_client.models.tv_series_watch_providers_200_response_results_mk.tv_series_watch_providers_200_response_results_MK(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MK', ), 
                    mu = openapi_client.models.tv_series_watch_providers_200_response_results_mu.tv_series_watch_providers_200_response_results_MU(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MU', ), 
                    mx = openapi_client.models.tv_series_watch_providers_200_response_results_mx.tv_series_watch_providers_200_response_results_MX(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MX', ), 
                    my = openapi_client.models.tv_series_watch_providers_200_response_results_my.tv_series_watch_providers_200_response_results_MY(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MY', ), 
                    mz = openapi_client.models.tv_series_watch_providers_200_response_results_mz.tv_series_watch_providers_200_response_results_MZ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MZ', ), 
                    ne = openapi_client.models.tv_series_watch_providers_200_response_results_ne.tv_series_watch_providers_200_response_results_NE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NE', ), 
                    ng = openapi_client.models.tv_series_watch_providers_200_response_results_ng.tv_series_watch_providers_200_response_results_NG(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NG', ), 
                    nl = openapi_client.models.tv_series_watch_providers_200_response_results_nl.tv_series_watch_providers_200_response_results_NL(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NL', ), 
                    no = openapi_client.models.tv_series_watch_providers_200_response_results_no.tv_series_watch_providers_200_response_results_NO(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NO', ), 
                    nz = openapi_client.models.tv_series_watch_providers_200_response_results_nz.tv_series_watch_providers_200_response_results_NZ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NZ', ), 
                    pa = openapi_client.models.tv_series_watch_providers_200_response_results_pa.tv_series_watch_providers_200_response_results_PA(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PA', ), 
                    pe = openapi_client.models.tv_series_watch_providers_200_response_results_pe.tv_series_watch_providers_200_response_results_PE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PE', ), 
                    ph = openapi_client.models.tv_series_watch_providers_200_response_results_ph.tv_series_watch_providers_200_response_results_PH(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PH', ), 
                    pl = openapi_client.models.tv_series_watch_providers_200_response_results_pl.tv_series_watch_providers_200_response_results_PL(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PL', ), 
                    ps = openapi_client.models.tv_series_watch_providers_200_response_results_ps.tv_series_watch_providers_200_response_results_PS(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PS', ), 
                    pt = openapi_client.models.tv_series_watch_providers_200_response_results_pt.tv_series_watch_providers_200_response_results_PT(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PT', ), 
                    py = openapi_client.models.tv_series_watch_providers_200_response_results_py.tv_series_watch_providers_200_response_results_PY(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PY', ), 
                    ro = openapi_client.models.tv_series_watch_providers_200_response_results_ro.tv_series_watch_providers_200_response_results_RO(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=RO', ), 
                    rs = openapi_client.models.tv_series_watch_providers_200_response_results_rs.tv_series_watch_providers_200_response_results_RS(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=RS', ), 
                    ru = openapi_client.models.tv_series_watch_providers_200_response_results_ru.tv_series_watch_providers_200_response_results_RU(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=RU', 
                        ads = [
                            openapi_client.models.tv_series_watch_providers_200_response_results_ru_ads_inner.tv_series_watch_providers_200_response_results_RU_ads_inner(
                                logo_path = '/3jJtMOIwtvcrCyeRMUvv4wsfhJk.jpg', 
                                provider_id = 577, 
                                provider_name = 'TvIgle', 
                                display_priority = 22, )
                            ], ), 
                    sa = openapi_client.models.tv_series_watch_providers_200_response_results_sa.tv_series_watch_providers_200_response_results_SA(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SA', ), 
                    sc = openapi_client.models.tv_series_watch_providers_200_response_results_sc.tv_series_watch_providers_200_response_results_SC(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SC', ), 
                    se = openapi_client.models.tv_series_watch_providers_200_response_results_se.tv_series_watch_providers_200_response_results_SE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SE', ), 
                    sg = openapi_client.models.tv_series_watch_providers_200_response_results_sg.tv_series_watch_providers_200_response_results_SG(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SG', ), 
                    si = openapi_client.models.tv_series_watch_providers_200_response_results_si.tv_series_watch_providers_200_response_results_SI(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SI', ), 
                    sk = openapi_client.models.tv_series_watch_providers_200_response_results_sk.tv_series_watch_providers_200_response_results_SK(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SK', ), 
                    sn = openapi_client.models.tv_series_watch_providers_200_response_results_sn.tv_series_watch_providers_200_response_results_SN(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SN', ), 
                    sv = openapi_client.models.tv_series_watch_providers_200_response_results_sv.tv_series_watch_providers_200_response_results_SV(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SV', ), 
                    th = openapi_client.models.tv_series_watch_providers_200_response_results_th.tv_series_watch_providers_200_response_results_TH(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TH', ), 
                    tr = openapi_client.models.tv_series_watch_providers_200_response_results_tr.tv_series_watch_providers_200_response_results_TR(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TR', ), 
                    tt = openapi_client.models.tv_series_watch_providers_200_response_results_tt.tv_series_watch_providers_200_response_results_TT(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TT', ), 
                    tw = openapi_client.models.tv_series_watch_providers_200_response_results_tw.tv_series_watch_providers_200_response_results_TW(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TW', ), 
                    tz = openapi_client.models.tv_series_watch_providers_200_response_results_tz.tv_series_watch_providers_200_response_results_TZ(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TZ', ), 
                    ug = openapi_client.models.tv_series_watch_providers_200_response_results_ug.tv_series_watch_providers_200_response_results_UG(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=UG', ), 
                    us = openapi_client.models.tv_series_watch_providers_200_response_results_us.tv_series_watch_providers_200_response_results_US(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=US', 
                        free = [
                            openapi_client.models.tv_series_watch_providers_200_response_results_br_flatrate_inner.tv_series_watch_providers_200_response_results_BR_flatrate_inner(
                                logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                                provider_id = 384, 
                                provider_name = 'HBO Max', 
                                display_priority = 7, )
                            ], ), 
                    uy = openapi_client.models.tv_series_watch_providers_200_response_results_uy.tv_series_watch_providers_200_response_results_UY(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=UY', ), 
                    ve = openapi_client.models.tv_series_watch_providers_200_response_results_ve.tv_series_watch_providers_200_response_results_VE(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=VE', ), 
                    za = openapi_client.models.tv_series_watch_providers_200_response_results_za.tv_series_watch_providers_200_response_results_ZA(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=ZA', ), 
                    zm = openapi_client.models.tv_series_watch_providers_200_response_results_zm.tv_series_watch_providers_200_response_results_ZM(
                        link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=ZM', ), )
            )
        else:
            return TvSeriesWatchProviders200Response(
        )
        """

    def testTvSeriesWatchProviders200Response(self):
        """Test TvSeriesWatchProviders200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
